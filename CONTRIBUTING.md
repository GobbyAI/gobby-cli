# Contributing to gobby-code

Thanks for your interest in contributing to gobby-code! This project is part of the [Gobby](https://github.com/GobbyAI/gobby) suite.

## Getting Started

```bash
git clone https://github.com/GobbyAI/gobby-code.git
cd gobby-code
cargo build --no-default-features
cargo test --no-default-features
```

The `--no-default-features` flag builds without the `embeddings` feature, which requires cmake. If you have cmake installed, you can build with full features using `cargo build`.

## Development

### Building

```bash
cargo build                              # Dev build with embeddings (requires cmake)
cargo build --no-default-features        # Dev build without embeddings
cargo build --release                    # Optimized release build
cargo build --release --no-default-features  # Release without embeddings
```

### Testing

```bash
cargo test                               # All tests (with embeddings)
cargo test --no-default-features         # All tests (without embeddings)
cargo test <test_name>                   # Single test
cargo clippy -- -D warnings             # Lint (zero warnings required)
cargo clippy --no-default-features -- -D warnings  # Lint without embeddings
```

All PRs must pass CI (clippy, tests) for both feature configurations before merging.

### Project Structure

```
src/
  main.rs              — CLI entry point (clap), command dispatch
  config.rs            — Runtime context resolution, service configs
  db.rs                — SQLite connection helpers (WAL, busy timeout)
  models.rs            — Data types: Symbol, IndexedFile, SearchResult, etc.
  schema.rs            — Self-initializing SQLite schema (tables, FTS5, triggers)
  output.rs            — Output formatting (text vs JSON)
  project.rs           — Project identity files (.gobby/gcode.json)
  progress.rs          — TTY-aware progress bar for indexing
  secrets.rs           — Fernet decryption for Gobby secrets
  neo4j.rs             — Neo4j HTTP client for graph queries
  savings.rs           — Token savings tracking
  skill.rs             — AI CLI skill installation
  commands/
    init.rs            — gcode init (identity + skills + index)
    index.rs           — gcode index (full/incremental)
    search.rs          — gcode search, search-text, search-content
    symbols.rs         — gcode outline, symbol, symbols, tree
    graph.rs           — gcode callers, usages, imports, blast-radius
    status.rs          — gcode status, invalidate, projects
    summary.rs         — gcode summary, repo-outline
  index/
    walker.rs          — File discovery via `ignore` crate
    parser.rs          — Tree-sitter AST extraction per language
    languages.rs       — Extension → tree-sitter grammar mapping
    chunker.rs         — Content splitting for FTS5
    hasher.rs          — SHA-256 for incremental indexing
    indexer.rs         — Indexing orchestrator (SQLite + Neo4j + Qdrant writes)
    security.rs        — Path validation
  search/
    fts.rs             — FTS5 symbol + content search
    semantic.rs        — Qdrant vector search + GGUF embeddings
    graph_boost.rs     — Neo4j relevance boost
    rrf.rs             — Reciprocal Rank Fusion (merge ranked results)
```

### Adding a Language

1. Add the `tree-sitter-<lang>` dependency to `Cargo.toml`
2. Add a grammar entry in `src/index/languages.rs` mapping file extensions to the grammar
3. Add query patterns in `src/index/parser.rs` if the language needs custom symbol extraction
4. Add tests
5. Document the tier in the README

### Adding a Command

1. Add the variant to the `Command` enum in `src/main.rs` with clap attributes
2. Create or extend the handler function in the appropriate `src/commands/*.rs` module
3. Wire the dispatch in `main()` — if the command needs to work on uninitialized projects, add it to the early-dispatch block before `Context::resolve()`
4. Add tests
5. Document in the README and `assets/SKILL.md`

## Key Constraints

- **UUID5 parity with Python** — Symbol IDs must be deterministic UUID5 using namespace `c0de1de0-0000-4000-8000-000000000000` and key format `{project_id}:{file_path}:{name}:{kind}:{byte_start}`. Must match the Python daemon's `Symbol.make_id()` exactly.
- **Non-destructive to Gobby databases** — gcode must detect and skip existing Gobby-owned databases and tables. Never alter `project.json` or Gobby-managed schema.
- **Config resolution order** — env vars → `config_store` table → hardcoded defaults. Don't short-circuit this chain.

## Pull Requests

- Keep PRs focused — one feature or fix per PR
- Add tests for new functionality
- Run `cargo clippy --no-default-features -- -D warnings` before committing
- Write clear commit messages in the format `[gobby-code-#N] Description`

## Reporting Issues

[Open an issue](https://github.com/GobbyAI/gobby-code/issues/new) with:
- What you expected to happen
- What actually happened
- The command and output (if applicable)
- Your platform and gcode version (`gcode --version`)

## License

By contributing, you agree that your contributions will be licensed under the [Apache 2.0 License](LICENSE).
