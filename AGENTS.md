# AGENTS.md — Guide for AI Agents

This file is for AI coding agents (Claude, Copilot, Cursor, etc.) working on the gobby-code codebase. It supplements CLAUDE.md with constraints and patterns that prevent common mistakes.

## What This Is

`gobby-code` is a Rust CLI (`gcode`) that provides AST-aware code search, symbol navigation, and dependency graph analysis. It reads/writes the Gobby PostgreSQL hub for symbols/search, FalkorDB for call graphs, and Qdrant for semantic vectors. It works without the Gobby daemon process, but requires a migrated PostgreSQL hub bootstrap.

## Build & Test

```bash
cargo build --no-default-features           # CI-compatible build
cargo test --no-default-features            # Run all tests
cargo clippy --no-default-features -- -D warnings  # Lint (must be zero warnings)
```

CI builds use `--no-default-features`.

## Architecture

```text
main.rs (clap CLI)
  → config::Context::resolve()     # Resolves project root, PostgreSQL DSN, service configs
  → commands/*::run()              # Command handler
    → db::connect_readwrite/readonly # PostgreSQL hub connection
    → index/*                      # Indexing pipeline (walker → parser → chunker → indexer)
    → search/*                     # Search pipeline (fts + semantic + graph_boost → rrf)
    → falkor::*                     # Graph queries via FalkorDB
```

## Critical Constraints

### 1. Non-destructive to Gobby databases

gcode must treat Gobby-owned hub schema as externally managed. Never:
- Write to `.gobby/project.json` (that's Gobby's file)
- CREATE, ALTER, or DROP tables that Gobby created
- Modify the `config_store` table

The schema module (`src/schema.rs`) only validates required PostgreSQL tables, the `pg_search` extension, and BM25 indexes. It must not create or migrate schema.

### 2. UUID5 parity with Python

Symbol IDs are deterministic UUID5 using:
- Namespace: `c0de1de0-0000-4000-8000-000000000000`
- Key: `{project_id}:{file_path}:{name}:{kind}:{byte_start}`

These must match the Python daemon's `Symbol.make_id()` exactly. See `src/models.rs`.

### 3. Config resolution order

Infrastructure and hub-connection config stays env-first: env vars (`GOBBY_FALKORDB_HOST`, `GOBBY_FALKORDB_PORT`, `GOBBY_FALKORDB_PASSWORD`, PostgreSQL DSN, etc.) → `config_store` table → hardcoded defaults. Don't short-circuit those paths.

AI capability config is the carve-out: `ai.*` keys resolve from `config_store` → standalone `~/.gobby/gcore.yaml` → defaults, with no `GOBBY_*` env-var layer. CLI flags may still override for a single invocation.

### 4. Do NOT run `gcode invalidate`

`invalidate` destroys the project's code index and requires interactive confirmation. It exists for human use only. Use `gcode index` for incremental re-indexing instead.

## Common Tasks

### Add a new CLI command

1. Add variant to `Command` enum in `src/main.rs`
2. Add handler in `src/commands/*.rs`
3. Wire dispatch in `main()` — commands that work on uninitialized projects go in the early-dispatch block before `Context::resolve()`

### Add a language

1. Add `tree-sitter-<lang>` to `Cargo.toml`
2. Map extensions in `src/index/languages.rs`
3. Add query patterns in `src/index/parser.rs` if needed

### Modify search ranking

Search uses Reciprocal Rank Fusion in `src/search/rrf.rs` to merge results from:
- `src/search/fts.rs` — pg_search BM25 symbol and content search
- `src/search/semantic.rs` — Qdrant vector similarity
- `src/search/graph_boost.rs` — FalkorDB graph relevance

### Modify the indexing pipeline

The pipeline in `src/index/indexer.rs` orchestrates:
- `walker.rs` — file discovery
- `parser.rs` — tree-sitter AST extraction
- `chunker.rs` — content splitting for pg_search BM25 content search
- `hasher.rs` — SHA-256 for incremental detection

## What NOT to Do

- Don't modify Gobby-owned tables or files (see constraint #1)
- Don't change UUID5 generation without verifying Python parity
- Don't add `println!` for user output — use `eprintln!` for status, and `output::print_json` / `output::print_text` for command results
- Don't skip the `--no-default-features` test pass — CI runs both configurations
- Don't assume FalkorDB or Qdrant are available — all code must handle `None` configs gracefully
