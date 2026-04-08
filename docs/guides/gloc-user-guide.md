# gloc User Guide

gloc launches AI CLI tools (Claude Code, Codex) against local LLM backends. It auto-detects LM Studio or Ollama, loads the model if needed, sets the right environment variables, and hands off to your chosen CLI.

## Installation

Download from [GitHub Releases](https://github.com/GobbyAI/gobby-cli/releases/latest) or build from source:

```bash
cargo install gobby-local
```

If you use [Gobby](https://github.com/GobbyAI/gobby), gloc is already installed.

## Quick Start

Start LM Studio or Ollama with a model loaded, then:

```bash
# Launch Claude Code with auto-detected backend
gloc

# Specify a model
gloc --model qwen3-coder

# Use an alias
gloc --model qwen

# Launch Codex instead of Claude
gloc --client codex

# Force a specific backend
gloc --backend ollama --model qwen3-coder

# Override the backend URL
gloc --url http://192.168.1.50:11434

# Pass extra args to the client
gloc --model qwen -- --verbose

# Check what gloc would do (no launch)
gloc --status
```

## How It Works

1. gloc loads its config (layered: `--config` > `.gobby/gloc.yaml` > `~/.gobby/gloc.yaml` > built-in default)
2. Probes each backend in config order via HTTP GET (500ms timeout per probe)
3. First responding backend wins — or use `--backend` to skip detection
4. Resolves model aliases (e.g. `qwen` -> `qwen3-coder`)
5. For Ollama: checks if the model is downloaded, optionally pulls and warms it up
6. For LM Studio: no-op — LM Studio loads models on first request (JIT)
7. Sets environment variables from the client's template config
8. `exec()`s into the client binary (gloc replaces itself — no wrapper process)

## Backends

Backends are probed in the order they appear in config. The default config tries LM Studio first, then Ollama.

### LM Studio

LM Studio uses JIT model loading — when Claude Code sends its first request, LM Studio loads the model automatically. No explicit load step needed.

| Env Var | Value |
|---------|-------|
| `ANTHROPIC_BASE_URL` | `http://localhost:1234` |
| `ANTHROPIC_AUTH_TOKEN` | `lmstudio` |
| `ANTHROPIC_API_KEY` | `""` |

### Ollama

Ollama has explicit model lifecycle management. gloc can handle this automatically:

| Condition | Config | Behavior |
|-----------|--------|----------|
| Model not downloaded | `auto_pull: true` | Pulls from Ollama registry (blocking) |
| Model not downloaded | `auto_pull: false` | Exits with "run `ollama pull <model>`" |
| Model downloaded, not loaded | `auto_load: true` | Warms up via `/api/generate` |
| Model already loaded | — | Proceeds immediately |

| Env Var | Value |
|---------|-------|
| `ANTHROPIC_BASE_URL` | `http://localhost:11434` |
| `ANTHROPIC_AUTH_TOKEN` | `ollama` |
| `ANTHROPIC_API_KEY` | `""` |

## Clients

Clients are the AI CLI tools that gloc launches. The default client is the first one alphabetically in the config (`claude` before `codex`).

### Claude Code

```bash
gloc                          # default client
gloc --client claude          # explicit
```

### Codex CLI

```bash
gloc --client codex
```

Codex uses OpenAI-compatible env vars and gets `--provider openai` appended automatically.

## Configuration

### Config Layers

| Priority | Path | Purpose |
|----------|------|---------|
| 1 | `--config path/to/file.yaml` | Explicit CLI override |
| 2 | `.gobby/gloc.yaml` | Project-level config |
| 3 | `~/.gobby/gloc.yaml` | Global config (auto-created on first run) |
| 4 | Compiled into binary | Built-in default |

First found wins — no merging between layers. Run `gloc --init` to write the default config to `.gobby/gloc.yaml` (backs up existing to `gloc.yaml.bak`).

### Full Config Reference

```yaml
settings:
  probe_timeout_ms: 500    # timeout per backend probe
  auto_load: true           # load model into backend before exec
  auto_pull: false          # (ollama) pull model if not downloaded

backends:
  - name: lmstudio
    url: "http://localhost:1234"
    probe: "/v1/models"
    auth_token: "lmstudio"
  - name: ollama
    url: "http://localhost:11434"
    probe: "/api/tags"
    auth_token: "ollama"

clients:
  claude:
    binary: "claude"
    env:
      ANTHROPIC_BASE_URL: "{backend.url}"
      ANTHROPIC_AUTH_TOKEN: "{backend.auth_token}"
      ANTHROPIC_API_KEY: ""
    model_flag: "--model"
    default_model: "qwen3-coder"
    default_args: []
    default_env: {}
  codex:
    binary: "codex"
    env:
      OPENAI_BASE_URL: "{backend.url}/v1"
      OPENAI_API_KEY: "{backend.auth_token}"
    model_flag: "--model"
    default_model: "qwen3-coder"
    default_args: ["--provider", "openai"]
    default_env: {}

aliases:
  qwen: "qwen3-coder"
  glm: "glm-4.7:cloud"
```

### Template Variables

Client `env` values support these interpolations:

| Variable | Resolves To |
|----------|-------------|
| `{backend.url}` | Selected backend's `url` field |
| `{backend.auth_token}` | Selected backend's `auth_token` field |
| `{backend.name}` | Selected backend's `name` field |
| `{model}` | Resolved model name (after alias lookup) |

### Adding a New Client

To add support for another AI CLI tool, add an entry to `clients`:

```yaml
clients:
  aider:
    binary: "aider"
    env:
      OPENAI_API_BASE: "{backend.url}/v1"
      OPENAI_API_KEY: "{backend.auth_token}"
    model_flag: "--model"
    default_model: "qwen3-coder"
    default_args: []
    default_env: {}
```

### Changing Backend Priority

To prefer Ollama over LM Studio, reorder the `backends` list:

```yaml
backends:
  - name: ollama
    url: "http://localhost:11434"
    probe: "/api/tags"
    auth_token: "ollama"
  - name: lmstudio
    url: "http://localhost:1234"
    probe: "/v1/models"
    auth_token: "lmstudio"
```

## Debugging

```bash
# See which backend, client, model, and env vars would be used
gloc --status

# Dump the resolved config
gloc --dump-config
```

`--status` output:

```text
Backend:  ollama (http://localhost:11434)
Client:   claude (claude)
Binary:   /usr/local/bin/claude
Model:    qwen3-coder
Env:
  ANTHROPIC_API_KEY=""
  ANTHROPIC_AUTH_TOKEN=ollama
  ANTHROPIC_BASE_URL=http://localhost:11434
Args:     claude --model qwen3-coder
```
