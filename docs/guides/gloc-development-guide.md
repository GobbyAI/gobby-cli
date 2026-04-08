# gloc Development Guide

Technical internals for developers and agents working in the gloc codebase.

## Architecture Overview

```
CLI (main.rs, clap)
  → Config::load (--config → .gobby/gloc.yaml → ~/.gobby/gloc.yaml → compiled default)
  → Handle special modes (--init, --dump-config) → exit
  → resolve_backend (--backend flag or auto-detect in config order)
  → apply --url override
  → resolve_client (--client flag or first alphabetically in BTreeMap)
  → resolve_model (--model flag → client.default_model → alias lookup)
  → Handle --status → print diagnostics → exit
  → ensure_model_ready (Ollama: check → pull → warmup; LM Studio: no-op)
  → exec_client
    → build_env (resolve templates against backend + model)
    → build_args (model_flag + model + default_args + passthrough)
    → CommandExt::exec() (replaces process, does not return)
```

### Why exec()?

gloc uses `std::os::unix::process::CommandExt::exec()` instead of spawning a child process. This replaces the gloc process entirely with the client binary — no wrapper overhead, no signal forwarding, no zombie processes. The tradeoff is Unix-only (no Windows support), but that matches the target audience (developers running local LLMs on macOS/Linux).

## Config System

**File:** `src/config.rs`

### Config Resolution

First found wins entirely — no merging (same pattern as gsqz):

| Priority | Path | Purpose |
|----------|------|---------|
| 1 | `--config <PATH>` | Explicit CLI override |
| 2 | `.gobby/gloc.yaml` | Project-level config |
| 3 | `~/.gobby/gloc.yaml` | Global config (auto-created on first run) |
| 4 | Compiled into binary (`config.yaml` via `include_str!`) | Built-in default |

On first run with no config, the default is auto-exported to `~/.gobby/gloc.yaml`. The `--init` flag writes to `.gobby/gloc.yaml` (project-level), backing up any existing file to `gloc.yaml.bak`.

### Data Structures

```rust
pub struct Config {
    pub settings: Settings,
    pub backends: Vec<Backend>,           // ordered — probe priority
    pub clients: BTreeMap<String, Client>, // sorted — first is default
    pub aliases: BTreeMap<String, String>,
}

pub struct Settings {
    pub probe_timeout_ms: u64,  // default: 500
    pub auto_load: bool,        // default: true
    pub auto_pull: bool,        // default: false
}

pub struct Backend {
    pub name: String,       // "lmstudio" or "ollama"
    pub url: String,        // "http://localhost:1234"
    pub probe: String,      // "/v1/models" or "/api/tags"
    pub auth_token: String, // "lmstudio" or "ollama"
}

pub struct Client {
    pub binary: String,                      // "claude" or "codex"
    pub env: BTreeMap<String, String>,       // template env vars (higher priority)
    pub model_flag: String,                  // "--model"
    pub default_model: String,               // "qwen3-coder"
    pub default_args: Vec<String>,           // extra args always passed
    pub default_env: BTreeMap<String, String>, // extra env vars (lower priority)
}
```

### Why Vec for Backends, BTreeMap for Clients?

**Backends are a Vec** because probe order is the user's priority signal. The first backend that responds wins. Rearranging the YAML list changes the behavior.

**Clients are a BTreeMap** because we need deterministic "default client" behavior. BTreeMap iterates alphabetically, so `"claude"` naturally sorts before `"codex"`. This gives a stable default without an explicit `default_client` field.

### Template Resolution

**Function:** `resolve_template(template, backend, model) -> String`

Simple string replacement — no recursive expansion, no escaping needed:

| Variable | Source |
|----------|--------|
| `{backend.url}` | `Backend.url` |
| `{backend.auth_token}` | `Backend.auth_token` |
| `{backend.name}` | `Backend.name` |
| `{model}` | Resolved model name |

Resolution happens in `exec::build_env()`, which calls `resolve_template()` for each env var value. The config module owns the template definition; the exec module owns the invocation timing.

### Alias Resolution

**Method:** `Config::resolve_alias(model) -> String`

Aliases are a flat `BTreeMap<String, String>`. Lookup is exact-match only (no prefix matching, no chaining). If the model name isn't in the alias map, it passes through unchanged.

Resolution happens early in `main()` via `resolve_model()` — the resolved name flows through the entire pipeline (model management, env templates, CLI args).

## Backend Detection

**File:** `src/backend.rs`

### Probing

`detect_backend(backends, timeout_ms)` iterates through backends in config order, sending `GET {url}{probe}` to each. First 2xx response wins. Each probe uses `timeout_connect` and `timeout_read` set to `probe_timeout_ms` (default 500ms).

`validate_backend(backend, timeout_ms)` does the same for a single backend — used when `--backend` is specified explicitly. Even with an explicit flag, gloc validates reachability before proceeding.

### Ollama Model Management

`ensure_model_ready(backend, model, settings)` orchestrates the Ollama model lifecycle. For non-Ollama backends (LM Studio, any unknown), it's a no-op — LM Studio uses JIT loading.

```
ensure_model_ready("ollama", "qwen3-coder", settings)
│
├─ ollama_check_model → GET /api/tags
│  ├─ Not downloaded → auto_pull?
│  │  ├─ true → ollama_pull_model (POST /api/pull, 10min timeout)
│  │  │         → auto_load? → ollama_warmup_model
│  │  └─ false → Err(NotFound) → exit with "run ollama pull <model>"
│  ├─ Downloaded, not loaded → auto_load?
│  │  ├─ true → ollama_warmup_model (POST /api/generate, 2min timeout)
│  │  └─ false → Ok (proceed, Ollama will load on first request)
│  └─ Already loaded → Ok (proceed immediately)
```

### Model Name Matching

`model_name_matches(entry, model)` handles Ollama's naming convention where models can have tags:

- `"qwen3-coder"` matches `"qwen3-coder"`, `"qwen3-coder:latest"`, `"qwen3-coder:q4_0"`
- Uses `starts_with("{model}:")` for tag variants

The function checks both `"name"` and `"model"` JSON fields because Ollama's `/api/tags` and `/api/ps` responses use different field names.

### Timeout Strategy

| Operation | Timeout | Rationale |
|-----------|---------|-----------|
| Backend probe | `probe_timeout_ms` (500ms) | Fast fail for detection |
| Model check (`/api/tags`) | max(5s, `probe_timeout_ms`) | Model list can be large |
| Model pull (`/api/pull`) | 10 minutes | Large models (30B+) take time |
| Model warmup (`/api/generate`) | 2 minutes | GPU memory allocation |

### Error Handling

`ModelError` is a custom enum (no anyhow) with four variants:

| Variant | Meaning | Fatal? |
|---------|---------|--------|
| `NotFound` | Model not in Ollama's downloaded list | Yes (exit 1) |
| `PullFailed` | `POST /api/pull` failed | Yes (exit 1) |
| `WarmupFailed` | `POST /api/generate` failed | **No** — print warning, continue |
| `NetworkError` | HTTP request failed entirely | Yes (exit 1) |

`WarmupFailed` is intentionally non-fatal. The model is downloaded and Ollama will load it on first request from the client. Warmup is a performance optimization, not a requirement.

## Exec

**File:** `src/exec.rs`

### Environment Building

`build_env(client, backend, model)` merges two env maps:

1. `client.default_env` — applied first (lower priority)
2. `client.env` — applied second (overwrites conflicts)

Both maps have their values template-resolved against the backend and model. This two-layer approach lets users set base env vars in `default_env` that client-specific templates can override.

### Argument Building

`build_args(client, model, passthrough)` constructs the argument list:

```
[model_flag, model, ...default_args, ...passthrough]
```

If `model_flag` or `model` is empty, the model args are skipped entirely. This supports clients that don't use a `--model` flag.

### Binary Resolution

`which_binary(name)` searches `PATH` for the binary. Used only by `--status` mode to show the full resolved path. The actual `exec()` call lets the OS resolve `PATH` — `Command::new("claude")` handles lookup natively.

### The exec() Call

```rust
pub fn exec_client(...) -> ! {
    let mut cmd = Command::new(&client.binary);
    cmd.args(&args);
    for (key, val) in &env {
        cmd.env(key, val);
    }
    let err = cmd.exec();
    // Only reached if exec fails
    eprintln!("gloc: failed to exec {}: {}", client.binary, err);
    std::process::exit(1);
}
```

The return type `-> !` (never) documents that this function either replaces the process or exits. The lines after `cmd.exec()` only execute if exec fails (binary not found, permission denied, etc.).

## Design Decisions

### No Async Runtime

gloc uses `ureq` (blocking HTTP) instead of `reqwest`/`hyper` + tokio. The operations are sequential by nature (probe → check → pull → warmup → exec), and the total binary size stays tiny with `opt-level = "z"`. Adding tokio would 5x the binary for zero benefit.

### No Error Crate

Following gsqz's pattern: `eprintln!` + `std::process::exit(1)` for CLI-level errors, `ModelError` enum for backend operations. The binary has <10 error paths total — anyhow's `?` operator doesn't save enough boilerplate to justify the dependency.

### Template Variables vs. Hardcoded Env Vars

Early versions hardcoded the env var mapping per backend (LM Studio → these 3 vars, Ollama → those 3 vars). The template approach is better because:

1. Adding a new client is config-only (no code changes)
2. Users can customize env vars per-client without forking
3. The same backend can serve different clients with different var mappings
4. `default_env` allows base vars that all clients share

### Auto-Export vs --init

Two separate operations:

| | Auto-export | --init |
|---|---|---|
| **When** | First run, no config found | Explicit flag |
| **Where** | `~/.gobby/gloc.yaml` (global) | `.gobby/gloc.yaml` (project) |
| **Backup** | No (only creates if missing) | Yes (renames to `.bak`) |
| **Purpose** | Give users an editable config | Reset project config |

This matches gsqz behavior. Global auto-export means `gloc` works out of the box. Project-level `--init` lets teams share backend preferences.

## Testing

### Unit Tests

Each module has `#[cfg(test)] mod tests` with comprehensive coverage:

- **config.rs**: Default config loading, backend/client/alias field validation, template resolution (all variables, no variables, empty strings), config dump, file override loading
- **backend.rs**: Unreachable port detection (no false positives), non-Ollama backends are no-op, model name matching (exact, `:latest`, tagged, `model` field variant), error display
- **exec.rs**: Claude and Codex env resolution, arg building with/without passthrough, empty model flag handling, `default_env` priority, binary PATH lookup

### Integration Tests

Backend tests that require running Ollama/LM Studio are marked `#[ignore]`. They verify the HTTP interaction without being part of CI.

### Running Tests

```bash
cargo test -p gobby-local              # all unit tests
cargo test -p gobby-local -- --ignored # integration tests (requires running backends)
```

## Adding a New Backend

1. Add an entry to the `backends` list in `config.yaml`
2. Choose a `probe` endpoint that returns 2xx when the backend is healthy
3. If the backend needs model management (like Ollama), add a branch to `ensure_model_ready()` matching on `backend.name`
4. Add the corresponding client entry in `clients` with the right env var templates

## Adding a New Client

Config-only — no code changes needed:

1. Add an entry to `clients` in `config.yaml`
2. Set `binary` to the CLI executable name
3. Map `env` vars using template variables
4. Set `model_flag`, `default_model`, `default_args` as appropriate
5. Optionally add aliases for common models
