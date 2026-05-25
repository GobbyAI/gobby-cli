<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <img src="logo.png" alt="Gobby" width="160" />
</p>

<h1 align="center">gobby-cli</h1>

<p align="center">
  <strong>Rust CLI tools for AI-assisted development.</strong><br>
  Code search, symbol navigation, output compression, and local LLM launching — all from the terminal.
</p>

<p align="center">
  <a href="https://github.com/GobbyAI/gobby-cli/actions/workflows/ci.yml"><img src="https://github.com/GobbyAI/gobby-cli/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/GobbyAI/gobby-cli/releases/latest"><img src="https://img.shields.io/github/v/release/GobbyAI/gobby-cli" alt="Release"></a>
  <a href="https://github.com/GobbyAI/gobby-cli"><img src="built-with-gobby.svg" alt="Built with Gobby"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="License"></a>
</p>

---

## What's Inside

This workspace contains four Gobby CLI tools plus a shared library:

### gcode — Code Search & Navigation

AST-aware code search powered by tree-sitter. Indexes 18 languages plus safe
repo text files into the Gobby PostgreSQL hub, with pg_search BM25 for symbol
lookup, repo-content search across source/docs/config/scripts, file tree
navigation, and hybrid ranking. When FalkorDB, Qdrant, and an embeddings
endpoint are configured - typically through Gobby - `gcode` adds graph-aware
search, semantic search, optional graph expansion for exact symbol lookup
(`gcode search-symbol --with-graph`), dependency analysis (`callers`, `usages`,
`imports`, `blast-radius`), and daemon-backed graph lifecycle commands
(`gcode graph clear`, `gcode graph rebuild`).

For non-Gobby-managed projects, `gcode init` installs the bundled `gcode` skill
for Claude Code, Codex, Droid, Grok, Qwen, Gemini CLI (deprecated
compatibility), and Antigravity CLI. Gobby-managed projects skip those
project-local skill writes because Gobby owns CLI wiring.

### gsqz — Output Compression

Squeezes CLI output before it eats your context window. 28 built-in pipelines for git, cargo, pytest, eslint, ruff, npm, and more. Filters noise, groups errors by rule, collapses repeats, and typically reduces token consumption by >90%. ~9ms overhead. YAML-configurable with layered config (global → project → CLI).

### gloc — Local LLM Launcher

One command to launch Claude Code or Codex against a local LLM backend. Auto-detects LM Studio and Ollama, manages Ollama model lifecycle (pull, load, warmup), sets the right env vars, and `exec`s into your CLI of choice. YAML-configurable with aliases, per-client env templates, and ordered backend priority.

### ghook — Hook Dispatcher

Sandbox-tolerant hook dispatcher invoked by host AI CLIs (Claude Code, Codex, Gemini CLI, Qwen CLI) on lifecycle and tool-use events. Spools envelopes to `~/.gobby/hooks/inbox/` *before* POSTing to the local Gobby daemon, so the daemon's drain worker can replay any delivery lost to a sandbox FS-read denial, network blip, or daemon restart. You don't usually invoke it directly — Gobby wires it into your AI CLI for you.

`gobby-core` underpins them all — a small shared-primitives library (project root walk-up, bootstrap config, daemon URL). Not a standalone tool.

## Documentation

- [gcode User Guide](docs/guides/gcode-user-guide.md) — search, symbols, dependency graphs, project management
- [gsqz User Guide](docs/guides/gsqz-user-guide.md) — pipelines, step types, configuration, debugging
- [gloc User Guide](docs/guides/gloc-user-guide.md) — backends, clients, model management, configuration
- [ghook User Guide](docs/guides/ghook-user-guide.md) — hook wiring, diagnose mode, inbox/replay, troubleshooting
- [Changelog](CHANGELOG.md) — release history
- [gcode README](crates/gcode/README.md) — architecture and build details
- [gsqz README](crates/gsqz/README.md) — architecture and build details

## Install

### Pre-built binaries

Download from [GitHub Releases](https://github.com/GobbyAI/gobby-cli/releases/latest). Binaries are available for macOS (ARM/x86), Linux (x86/ARM), and Windows (x86/ARM).

### From crates.io

```bash
# gcode
cargo install gobby-code

# gsqz
cargo install gobby-squeeze

# gloc
cargo install gobby-local

# ghook
cargo install gobby-hooks
```

`gcode` graph and semantic features are configured at runtime. There are no
Cargo feature flags for FalkorDB, Qdrant, or embeddings support. Gobby-managed
projects read FalkorDB settings from `databases.falkordb.*`; daemon-independent
setups can use `GOBBY_FALKORDB_HOST`, `GOBBY_FALKORDB_PORT`, and
`GOBBY_FALKORDB_PASSWORD`.

`gcode` 0.8.0+ uses the migrated Gobby PostgreSQL hub. It asks the local daemon
broker for the hub DSN first. If the daemon is unavailable, it checks fallback
sources in order: `GCODE_DATABASE_URL`, `GOBBY_POSTGRES_DSN`,
`~/.gobby/gcode.yaml` `database_url`, then bootstrap `database_url`.
Bootstrap fallback is valid only when `hub_backend: postgres` and bootstrap
contains an inline `database_url`. Bootstrap `database_url_ref` is rejected
during bootstrap validation; it is never resolved or used to restart the
fallback chain.
Installing from source or crates.io requires Rust 1.88+.

### From source

```bash
git clone https://github.com/GobbyAI/gobby-cli.git
cd gobby-cli
cargo install --path crates/gcode
cargo install --path crates/gsqz
cargo install --path crates/gloc
cargo install --path crates/ghook
```

## Development

```bash
cargo build --workspace --no-default-features   # Build all tools
cargo test --workspace --no-default-features    # Test all tools
cargo clippy --workspace --no-default-features -- -D warnings  # Lint all tools
cargo fmt --all --check                         # Check formatting
```

## License

Apache 2.0 — see [LICENSE](LICENSE).
