# Contributing to gobby-cli

Thanks for your interest in contributing! This workspace is part of the [Gobby](https://github.com/GobbyAI/gobby) suite.

## Getting Started

```bash
git clone https://github.com/GobbyAI/gobby-cli.git
cd gobby-cli
cargo build --workspace --no-default-features
cargo nextest run --workspace --no-default-features
cargo test --doc --workspace --no-default-features
```

The `rust-toolchain.toml` ensures you have the right toolchain and components (clippy, rustfmt) installed automatically. Install `cargo-nextest` separately before running the test commands. CI uses `--no-default-features`; keep that build clean even when a crate has no default feature set.

## Development

### Building

```bash
cargo build --workspace                          # Full build (gcode embeddings require cmake)
cargo build --workspace --no-default-features    # Build without embeddings
cargo build -p gobby-code                        # gcode only
cargo build -p gobby-squeeze                     # gsqz only
```

### Testing

```bash
cargo nextest run --workspace --no-default-features     # All non-doctest tests (without embeddings)
cargo test --doc --workspace --no-default-features      # Doctests (without embeddings)
cargo nextest run -p gobby-code --no-default-features   # gcode tests only
cargo nextest run -p gobby-squeeze --no-default-features # gsqz tests only
cargo clippy --workspace -- -D warnings          # Lint
cargo fmt --all --check                          # Check formatting
```

All PRs must pass CI (fmt, clippy, tests) before merging.

### Workspace Structure

```
crates/
  gcode/                 — AST-aware code search (heavy: tree-sitter, PostgreSQL, opt-level=3)
    src/
      main.rs            — CLI entry point, command dispatch
      config.rs          — Runtime context resolution, service configs
      db.rs              — PostgreSQL hub connection helpers
      models.rs          — Data types: Symbol, IndexedFile, SearchResult, etc.
      secrets.rs         — Fernet decryption for Gobby secrets
      falkor.rs          — FalkorDB client for graph queries
      commands/          — Subcommand handlers (init, index, search, graph, etc.)
      index/             — Indexing pipeline (walker, parser, chunker, hasher, indexer)
      search/            — Search pipeline (pg_search BM25, semantic, graph_boost, RRF)
  gsqz/                  — Output compressor (tiny: regex, opt-level="z")
    src/
      main.rs            — CLI entry point, command execution, ANSI stripping
      config.rs          — Layered config loading, step deserialization
      compressor.rs      — Pipeline matching, step orchestration, thresholds
      daemon.rs          — Optional gobby daemon HTTP integration
      primitives/        — filter, group (8 modes), truncate, dedup
    config.yaml          — Built-in pipeline definitions (35+ pipelines)
```

## gcode: Adding a Language

1. Add the `tree-sitter-<lang>` dependency to `crates/gcode/Cargo.toml`
2. Add a grammar entry in `src/index/languages.rs` mapping file extensions to the grammar
3. Add query patterns in `src/index/parser.rs` if the language needs custom symbol extraction
4. Add tests
5. Document the tier in the README

## gcode: Adding a Command

1. Add the variant to the `Command` enum in `src/main.rs` with clap attributes
2. Create or extend the handler function in the appropriate `src/commands/*.rs` module
3. Wire the dispatch in `main()` — if the command needs to work on uninitialized projects, add it to the early-dispatch block before `Context::resolve()`
4. Add tests
5. Document in the README and `assets/SKILL.md`

## gsqz: Adding a Pipeline

Add a new entry to `config.yaml`:

```yaml
pipelines:
  my-tool:
    match: '\bmy-tool\b'    # Regex matched against the full command
    steps:
      - filter_lines:
          patterns:
            - '^\s*$'       # Remove blank lines
      - group_lines:
          mode: errors_warnings
      - truncate:
          head: 20
          tail: 10
      - dedup: {}
```

## gsqz: Adding a Group Mode

1. Add the function in `src/primitives/group.rs`
2. Add the mode name to the `group_lines()` dispatcher match
3. Add tests
4. Document in the README

## Key Constraints

- **UUID5 parity with Python** (gcode) — Symbol IDs must be deterministic UUID5 using namespace `c0de1de0-0000-4000-8000-000000000000`. Must match the Python daemon's `Symbol.make_id()` exactly.
- **Non-destructive to Gobby databases** (gcode) — Detect and skip existing Gobby-owned databases and tables. Never alter `project.json` or Gobby-managed schema.
- **Exit code 0** (gsqz) — Always exit 0. The LLM reads pass/fail from content, not exit codes.

## Pull Requests

- Keep PRs focused — one feature or fix per PR
- Add tests for new functionality
- Run `cargo clippy --workspace --no-default-features -- -D warnings` before committing
- Write clear commit messages in the format `[gobby-cli-#N] Description`

## Reporting Issues

[Open an issue](https://github.com/GobbyAI/gobby-cli/issues/new) with:
- What you expected to happen
- What actually happened
- The command and output (if applicable)
- Your platform and tool version (`gcode --version` / `gsqz --version`)

## License

By contributing, you agree that your contributions will be licensed under the [Apache 2.0 License](LICENSE).
