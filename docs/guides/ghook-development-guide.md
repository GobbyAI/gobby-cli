# ghook Development Guide

Technical internals for developers and agents working in the ghook codebase.

## Architecture Overview

```text
host AI CLI (Claude Code / Codex / Gemini / Qwen)
  │  spawns: ghook --gobby-owned --cli=<c> --type=<t> [--critical] [--detach]
  │  pipes:  stdin = hook payload (JSON object)
  ▼
main.rs::run_gobby_owned
  │
  ├─ project::find_project_root + read_project_id      (gobby-core)
  │     ── walk-up BEFORE any detach; sandbox-safe.
  │
  ├─ stdin → serde_json::from_slice
  │     ── on malformed: transport::quarantine_malformed → exit
  │
  ├─ cli_config::CliConfig::for_cli(cli)
  │     ── per-CLI critical/terminal_context registry
  │
  ├─ terminal_context::inject  (if cfg.wants_terminal_context)
  │
  ├─ envelope::Envelope::new
  │
  ├─ transport::enqueue_to(envelope, ~/.gobby/hooks/inbox/)
  │     ── atomic write: tmp → fsync → rename
  │
  ├─ detach::detach()  (if --detach: setsid on Unix)
  │
  └─ transport::post_and_cleanup
        │
        ├─ POST {daemon_url}/api/hooks/execute  (30s timeout)
        ├─ 2xx     → fs::remove_file(envelope) → ExitCode::SUCCESS
        └─ failure → leave envelope               → ExitCode::SUCCESS or 2
                                                    (drain worker replays)
```

Spool-first ordering is load-bearing. The envelope is on disk before anything risky (network I/O, detach) happens, so the daemon's drain worker is the source of truth even if ghook dies mid-POST.

### Why a Separate Binary?

The original Python `hook_dispatcher.py` ran inside the daemon process. That made it sensitive to daemon downtime: hook → daemon socket → daemon process. ghook is a small standalone binary so:

1. It can run when the daemon is dead. Envelopes spool to disk.
2. It can survive sandbox FS-read denials that would crash an embedded interpreter.
3. Host CLIs can invoke it from any context (including detached sessions).
4. Failure modes are constrained: writing one file, sending one HTTP request.

## Module Map

`crates/ghook/src/`:

| Module | Responsibility |
|--------|----------------|
| `main.rs` | Arg parsing (clap), mode dispatch (`--gobby-owned`/`--diagnose`/`--version`), orchestrates the dispatch flow. |
| `cli_config.rs` | Per-CLI registry (claude/codex/gemini/qwen) — which hooks are critical, which want terminal context. Compile-time frozen. |
| `envelope.rs` | `Envelope` struct + `SCHEMA_VERSION = 1`. Serializes to the inbox JSON shape. |
| `transport.rs` | Inbox path resolution, atomic write, enqueue, POST + cleanup, quarantine for malformed stdin. |
| `terminal_context.rs` | Captures parent PID, TTY, tmux pane/socket, `TERM_PROGRAM`, `GOBBY_*` env vars. Injects under `input_data.terminal_context`. |
| `diagnose.rs` | `--diagnose` mode — pure introspection, no I/O side effects. Returns `DiagnoseOutput` matching `schemas/diagnose-output.v1.schema.json`. |
| `detach.rs` | Unix `setsid(2)` / Windows `FreeConsole()` — best-effort detach from controlling TTY and process group. |

`crates/ghook/schemas/`:

| File | Validated against in |
|------|----------------------|
| `inbox-envelope.v1.schema.json` | `envelope::tests::envelope_validates_against_v1_schema` |
| `diagnose-output.v1.schema.json` | `diagnose::tests::diagnose_output_validates_against_v1_schema` |

## Envelope Schema (v1)

The envelope is what ghook writes to `~/.gobby/hooks/inbox/` and what the daemon's drain worker replays. Schema is frozen at v1 — consumers must reject unknown versions.

```rust
pub struct Envelope {
    pub schema_version: u32,            // const 1
    pub enqueued_at: String,            // RFC 3339 UTC
    pub critical: bool,
    pub hook_type: String,              // host-CLI-specific
    pub input_data: Value,              // verbatim stdin + optional terminal_context
    pub source: String,                 // "claude" / "codex" / "gemini" / "qwen" / passthrough
    pub headers: BTreeMap<String, String>,
}
```

### Field Semantics

| Field | Why It Exists |
|-------|---------------|
| `schema_version` | Forward-compat. Daemon rejects unknown versions rather than parsing partial data. |
| `enqueued_at` | Lets the drain worker compute hook latency and detect very-stale envelopes. |
| `critical` | Recorded so the daemon knows whether the host CLI was told this hook fail-closed. Influences alerting. |
| `hook_type` | Opaque — exact identifier the host CLI's hook system uses (`session-start`, `PreToolUse`, etc.). |
| `input_data` | Original stdin verbatim. `terminal_context` is *injected* into the existing object (mirrors Python's `setdefault`) — never overwritten if already present. |
| `source` | Recognized CLI → canonical name from `CliConfig::source`. Unknown CLI → the `--cli` value verbatim, so future CLIs route correctly without code changes. |
| `headers` | Mirrors what ghook sent (or would have sent) on the POST. Omitted headers are absent keys; **empty-string values are never emitted** — this matches `hook_dispatcher.py:695-700` behavior and is enforced by the schema (`additionalProperties.minLength: 1`). |

### Standard Headers

| Header | When Present | Source |
|--------|--------------|--------|
| `X-Gobby-Project-Id` | Project root resolved AND `project.json` has an `id`/`project_id` field | `gobby_core::project::read_project_id` |
| `X-Gobby-Session-Id` | `input_data.session_id` is a non-empty string | `input_data["session_id"]` |

Both are inserted only when non-empty. The schema enforces `minLength: 1` on header values to match.

## Diagnose Output Schema (v1)

`--diagnose` returns a JSON object validated against `schemas/diagnose-output.v1.schema.json`. It runs the same config-resolution code paths as `--gobby-owned` but stops short of any I/O side effect.

```rust
pub struct DiagnoseOutput {
    pub schema_version: u32,                 // const 1
    pub ghook_version: &'static str,         // env!("CARGO_PKG_VERSION")
    pub cli: String,
    pub hook_type: String,
    pub source: Option<String>,              // null if cli not recognized
    pub critical: bool,                      // would this hook be critical for this CLI?
    pub terminal_context_enabled: bool,
    pub daemon_url: String,
    pub daemon_host: String,
    pub daemon_port: u16,
    pub project_root: Option<PathBuf>,
    pub project_id: Option<String>,
    pub terminal_context_preview: Option<Value>,  // populated when terminal_context_enabled
    pub cli_recognized: bool,
}
```

The `terminal_context_preview` field is the actual context that *would* be injected — operators can inspect what the daemon will receive without sending a real hook.

## Transport: Spool & POST

**File:** `src/transport.rs`

### Filename Shape

```text
~/.gobby/hooks/inbox/<prefix>-<ts13>-<uuid>.json
                      └c│n┘ └13-digit ms┘ └v4┘
```

| Field | Purpose |
|-------|---------|
| `prefix` | `c` for critical, `n` for non-critical. Lets the drain worker prioritize critical envelopes. |
| `ts13` | Zero-padded 13-digit ms-since-epoch. Lex-sortable, so drain order matches enqueue order even within the same second. |
| `uuid` | Random v4. Disambiguates simultaneous enqueues from concurrent hook fires. |

`.tmp` suffix is reserved for the intermediate atomic-write stage. The drain ignores `*.tmp` — it's never a valid replay target.

### Atomic Write

```rust
atomic_write(final_path, bytes):
    create_dir_all(parent)
    tmp = final_path.with_suffix(".tmp")
    File::create(tmp).write_all(bytes).sync_all()  // fsync
    fs::rename(tmp, final_path)                    // atomic on POSIX
```

`sync_all()` is critical — without it, `rename` makes the directory entry visible but the file's contents may not have hit disk. A crash between `rename` and the OS's deferred write would leave a zero-byte envelope that the drain would parse-fail on.

### POST + Cleanup

`post_and_cleanup` POSTs a Python-compatible hook payload to `{daemon_url}/api/hooks/execute` with a 30-second timeout. The envelope's `headers` are mirrored as HTTP headers. On 2xx, the inbox file is deleted; otherwise it's left in place.

The 30s timeout is deliberately generous — the daemon may be doing real work (DB writes, agent reconciliation). `--detach` is the escape hatch for hooks where the host CLI tears down its session before 30s.

### Quarantine for Malformed Stdin

When stdin can't be parsed as JSON, `quarantine_malformed_at` writes two files into `~/.gobby/hooks/inbox/quarantine/`:

| File | Contents |
|------|----------|
| `<stem>.json` | `{"quarantined": true, "stdin_bytes_b64": "..."}` |
| `<stem>.meta.json` | `{"reason": "malformed_stdin", "json_error": "<parse error>", "stdin_bytes_b64": "..."}` |

The drain never replays quarantined envelopes — they surface via `gobby status` and daemon logs. Putting them under the inbox tree (rather than alongside) means they share the same disk-space-management story without polluting drain attempts.

## Terminal Context

**File:** `src/terminal_context.rs`

Captures the caller's process context for hooks that need it (mainly `session-start`/`SessionStart`). Port of `hook_dispatcher.py:181-223`.

| Field | Source | Notes |
|-------|--------|-------|
| `parent_pid` | `libc::getppid()` (Unix) / null (Windows) | The host CLI's PID — daemon uses this to reconcile spawned-terminal agents. |
| `tty` | `libc::ttyname(0)` | Controlling terminal device path. |
| `tmux_pane` | `TMUX_PANE` env var, **only if `TMUX` is set** | Sharp edge from dispatcher `:205` — `TMUX_PANE` is inherited by children spawned into *other* terminals (e.g. Ghostty), so emitting it without checking `TMUX` would point `kill_agent` at the parent's pane. |
| `tmux_socket_path` | First comma-separated segment of `TMUX` | Mirror of `gobby.sessions.tmux_context.parse_tmux_socket_path`. |
| `term_program` | `TERM_PROGRAM` env var | |
| `gobby_session_id`, `gobby_parent_session_id`, `gobby_agent_run_id`, `gobby_project_id`, `gobby_workflow_name` | Eponymous env vars | Set by the Gobby daemon when it spawns the host CLI; let us correlate hooks back to the spawning context. |

`inject(input_data)` only adds `terminal_context` when:

1. `input_data` is a JSON object (not an array, scalar, etc.).
2. The key isn't already present (`setdefault` semantics from dispatcher `:682`).

This means a host CLI can pre-populate `terminal_context` and ghook will respect it.

## Detach Semantics

**File:** `src/detach.rs`

`--detach` is requested for hooks where the host CLI exits very quickly after firing (e.g. `Stop`). On Unix it calls `setsid(2)` to escape the controlling terminal and the parent's process group — the host CLI can wait for ghook's exit code without ghook being killed when the host's session tears down.

On Windows, `setsid` doesn't exist. `DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP` would be the parallel, but those flags apply at `CreateProcess` time, not to an already-running process. `FreeConsole()` is the closest honest equivalent — it disables console I/O for the current process. The function exists on Windows so callers don't need `cfg` checks, but it does less than its Unix counterpart.

**Critical ordering** (`main.rs:127-128`): project-root walk-up happens *before* `detach::detach()`. macOS sandbox FS-read denials and the cwd semantics of detached processes would otherwise surprise us — the project root is captured while we still have the host CLI's full file-access context.

## Critical vs Non-Critical Exit Semantics

`ghook` keeps enqueue-first transport internals, but host-visible stdout/stderr/exit behavior is intended to match the legacy Python dispatcher contract rather than expose separate Rust-specific delivery semantics.

## Testing

### Unit Tests

Each module has `#[cfg(test)] mod tests` with comprehensive coverage:

- **envelope.rs**: serialization shape, schema validation against `inbox-envelope.v1.schema.json`, empty-headers serializing as empty object.
- **transport.rs**: 13-digit timestamp shape, filename prefix matches `critical`, atomic-write creates parents, no `.tmp` left on success, enqueue produces valid filename, quarantine pair structure.
- **diagnose.rs**: unknown CLI → not recognized + null source; known CLI/hook combos hit the right critical/terminal-context flags; schema validation for both recognized and unrecognized CLIs.
- **cli_config.rs**: per-CLI critical/terminal-context membership; case-insensitive CLI lookup; unknown CLIs remain unrecognized for diagnose and fall back to conservative Claude-like config on the live dispatch path.
- **terminal_context.rs**: tmux socket-path parsing edge cases, `inject` respects existing context, `inject` no-ops on non-objects, `capture` emits all expected keys.

### Schema Validation in Tests

Both schemas are validated end-to-end at test time using `jsonschema`:

```rust
let schema_bytes = include_bytes!("../schemas/inbox-envelope.v1.schema.json");
let schema: Value = serde_json::from_slice(schema_bytes).unwrap();
let compiled = jsonschema::JSONSchema::options()
    .with_draft(jsonschema::Draft::Draft7)
    .compile(&schema)
    .expect("schema compiles");
let instance = serde_json::to_value(&envelope).unwrap();
compiled.validate(&instance)?;
```

This means changing the Rust struct without updating the schema (or vice versa) breaks the build — they're kept in lockstep by the test suite.

### Running Tests

```bash
cargo test -p gobby-hooks
```

No integration tests — ghook's I/O is contained (one file write, one HTTP POST), and both are covered by unit tests using `tempfile::tempdir()` and dummy daemon URLs.

## Adding a New Host CLI

The flow to support a new CLI (say, "cursor"):

1. **Add a registry entry** in `cli_config.rs::CliConfig::for_cli`:

   ```rust
   "cursor" => Some(Self {
       source: "cursor",
       critical_hooks: ["session-start"].into_iter().collect(),
       terminal_context_hooks: ["session-start"].into_iter().collect(),
   }),
   ```

2. **Add a unit test** for the new entry in `cli_config.rs::tests`.

3. **Add a diagnose test** in `diagnose.rs::tests` confirming the new CLI is recognized.

4. **No envelope schema changes** — the schema is CLI-agnostic. `source` is just a string.

5. **No transport changes** — same inbox, same daemon endpoint.

Unknown CLIs fall back to conservative Claude-like dispatch behavior on the live path. Diagnose mode still reports them as unrecognized. Adding a registry entry upgrades that path from fallback behavior to first-class parity.

## Adding a New Hook Type

Almost always config-only. ghook treats `--type` as opaque. To make a hook critical or to enable terminal-context enrichment for it, add the hook type to the relevant set in the CLI's `CliConfig` entry. No envelope, transport, or schema changes required.

## Versioning

ghook is at `0.2.0`. `SCHEMA_VERSION` is also `1`. The two version numbers are independent:

- **Crate version** bumps for any code change (binary behavior, dependencies, perf, etc.).
- **`SCHEMA_VERSION`** bumps only when the envelope shape changes in a way the daemon must explicitly handle.

`--version` writes `~/.gobby/bin/.ghook-compatibility` with both numbers, so the daemon can detect mismatches at startup and refuse to drain envelopes from a future schema it doesn't understand.
