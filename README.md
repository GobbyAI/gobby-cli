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

This workspace contains three Gobby CLI tools:

### gcode — Code Search & Navigation

AST-aware code search powered by tree-sitter. Indexes 18 languages into SQLite FTS5 for instant symbol lookup, content search, and file tree navigation. With Gobby, adds semantic vector search (Qdrant) and dependency graph analysis (Neo4j) — callers, usages, imports, and blast-radius. Incremental indexing, cross-project queries, and graceful degradation when services are unavailable.

### gsqz — Output Compression

Squeezes CLI output before it eats your context window. 28 built-in pipelines for git, cargo, pytest, eslint, ruff, npm, and more. Filters noise, groups errors by rule, collapses repeats, and typically reduces token consumption by >90%. ~9ms overhead. YAML-configurable with layered config (global → project → CLI).

### gloc — Local LLM Launcher

One command to launch Claude Code or Codex against a local LLM backend. Auto-detects LM Studio and Ollama, manages Ollama model lifecycle (pull, load, warmup), sets the right env vars, and `exec`s into your CLI of choice. YAML-configurable with aliases, per-client env templates, and ordered backend priority.

## Documentation

- [gcode User Guide](docs/guides/gcode-user-guide.md) — search, symbols, dependency graphs, project management
- [gsqz User Guide](docs/guides/gsqz-user-guide.md) — pipelines, step types, configuration, debugging
- [gloc User Guide](docs/guides/gloc-user-guide.md) — backends, clients, model management, configuration
- [Changelog](CHANGELOG.md) — release history
- [gcode README](crates/gcode/README.md) — architecture and build details
- [gsqz README](crates/gsqz/README.md) — architecture and build details

## Install

### Pre-built binaries

Download from [GitHub Releases](https://github.com/GobbyAI/gobby-cli/releases/latest). Binaries are available for macOS (ARM/x86), Linux (x86/ARM), and Windows (x86/ARM).

### From crates.io

```bash
# gcode (with embeddings — requires cmake)
cargo install gobby-code

# gcode (with GPU acceleration — pick your backend)
cargo install gobby-code --features cuda    # NVIDIA (requires CUDA toolkit)
cargo install gobby-code --features vulkan  # Any GPU (requires Vulkan SDK)
cargo install gobby-code --features rocm    # AMD (requires ROCm)

# gcode (without embeddings)
cargo install gobby-code --no-default-features

# gsqz
cargo install gobby-squeeze

# gloc
cargo install gobby-local
```

On macOS, Metal GPU acceleration is enabled automatically. On Linux/Windows, embeddings use CPU inference by default — add a GPU feature flag for hardware acceleration.

### From source

```bash
git clone https://github.com/GobbyAI/gobby-cli.git
cd gobby-cli
cargo install --path crates/gcode
cargo install --path crates/gsqz
cargo install --path crates/gloc
```

## Development

```bash
cargo build --workspace --no-default-features   # Build all tools
cargo test --workspace --no-default-features    # Test all tools
cargo clippy --workspace -- -D warnings         # Lint all tools
cargo fmt --all --check                         # Check formatting
```

## License

Apache 2.0 — see [LICENSE](LICENSE).
