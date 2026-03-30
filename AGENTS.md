# AGENTS.md — Guide for AI Agents

This file is for AI coding agents (Claude, Copilot, Cursor, etc.) working on the gobby-code codebase. It supplements CLAUDE.md with constraints and patterns that prevent common mistakes.

## What This Is

`gobby-code` is a Rust CLI (`gcode`) that provides AST-aware code search, symbol navigation, and dependency graph analysis. It reads/writes SQLite for symbols/search, Neo4j for call graphs, and Qdrant for semantic vectors. It works standalone or alongside the Gobby daemon.

## Build & Test

```bash
cargo build --no-default-features           # Build without embeddings (no cmake needed)
cargo test --no-default-features            # Run all tests
cargo clippy --no-default-features -- -D warnings  # Lint (must be zero warnings)
```

The `embeddings` feature (default: on) requires cmake. CI builds use `--no-default-features`.

## Architecture

```
main.rs (clap CLI)
  → config::Context::resolve()     # Resolves project root, DB path, service configs
  → commands/*::run()              # Command handler
    → db::open_readwrite/readonly  # SQLite connection
    → index/*                      # Indexing pipeline (walker → parser → chunker → indexer)
    → search/*                     # Search pipeline (fts + semantic + graph_boost → rrf)
    → neo4j::*                     # Graph queries via HTTP
```

## Critical Constraints

### 1. Non-destructive to Gobby databases

gcode must detect and skip existing Gobby-owned databases and schema. Never:
- Write to `.gobby/project.json` (that's Gobby's file)
- ALTER or DROP tables that Gobby created
- Modify the `config_store` table

The schema module (`src/schema.rs`) checks if `code_symbols` exists before creating anything. If it exists, schema creation is skipped entirely.

### 2. UUID5 parity with Python

Symbol IDs are deterministic UUID5 using:
- Namespace: `c0de1de0-0000-4000-8000-000000000000`
- Key: `{project_id}:{file_path}:{name}:{kind}:{byte_start}`

These must match the Python daemon's `Symbol.make_id()` exactly. See `src/models.rs`.

### 3. Config resolution order

Always: env vars (`GOBBY_NEO4J_URL`, etc.) → `config_store` table → hardcoded defaults. Don't short-circuit.

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
- `src/search/fts.rs` — FTS5 symbol and content search
- `src/search/semantic.rs` — Qdrant vector similarity
- `src/search/graph_boost.rs` — Neo4j graph relevance

### Modify the indexing pipeline

The pipeline in `src/index/indexer.rs` orchestrates:
- `walker.rs` — file discovery
- `parser.rs` — tree-sitter AST extraction
- `chunker.rs` — content splitting for FTS5
- `hasher.rs` — SHA-256 for incremental detection

## What NOT to Do

- Don't modify Gobby-owned tables or files (see constraint #1)
- Don't change UUID5 generation without verifying Python parity
- Don't add `println!` for user output — use `eprintln!` for status, and `output::print_json` / `output::print_text` for command results
- Don't skip the `--no-default-features` test pass — CI runs both configurations
- Don't assume Neo4j or Qdrant are available — all code must handle `None` configs gracefully
