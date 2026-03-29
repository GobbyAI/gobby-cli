# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

`gobby-code` is a Rust CLI (binary: `gcode`) for Gobby's code index. It provides AST-aware search, symbol navigation, and dependency graph analysis. It reads/writes the same databases as the Gobby daemon — SQLite for symbols/search, Neo4j for the call graph, Qdrant for semantic vectors.

## Build & Test Commands

```bash
cargo build --release                        # Build with embeddings (requires cmake)
cargo build --release --no-default-features  # Build without embeddings
cargo test                                   # Run all tests (with embeddings)
cargo test --no-default-features             # Run all tests (without embeddings)
cargo test <test_name>                       # Run a single test
cargo clippy                                 # Lint
```

The `embeddings` feature (default: on) enables local GGUF embedding via `llama-cpp-2` and requires cmake. macOS builds use Metal GPU acceleration. Linux/Windows CI builds disable embeddings (`--no-default-features`).

## Architecture

### Data Flow

`main.rs` parses CLI args via clap → resolves a `config::Context` (project root, DB path, service configs) → dispatches to the appropriate command handler in `commands/`.

### Core Modules

- **`config`** — Resolves runtime context: `~/.gobby/bootstrap.yaml` → SQLite `config_store` → Neo4j/Qdrant configs. Detects project root by walking up from cwd looking for `.gobby/project.json`. Resolves `$secret:NAME` patterns via `secrets`.
- **`db`** — Thin SQLite connection helpers (`open_readwrite` with WAL, `open_readonly`). All connections use 5s busy timeout.
- **`models`** — All data types: `Symbol`, `IndexedFile`, `ContentChunk`, `SearchResult`, `GraphResult`, etc.
- **`secrets`** — Fernet decryption of Gobby secrets using `~/.gobby/machine_id` + `~/.gobby/.secret_salt` for key derivation.
- **`neo4j`** — HTTP client for Neo4j Cypher queries (callers, usages, imports, blast radius).
- **`output`** — Output formatting (text vs JSON).

### `commands/` — CLI Command Handlers

Each subcommand maps to a function: `index::run`, `search::search`, `symbols::outline`, `graph::callers`, etc. Commands accept `&Context` and an output `Format`.

### `index/` — Indexing Pipeline

`walker` (file discovery via `ignore` crate) → `parser` (tree-sitter AST extraction per language) → `chunker` (content splitting for FTS) → `hasher` (SHA-256 for incremental indexing) → `indexer` (SQLite writes + FTS5 population). `languages` maps extensions to tree-sitter grammars. `security` validates paths.

### `search/` — Search Pipeline

`fts` (FTS5 symbol + content search) + `semantic` (Qdrant vector search) + `graph_boost` (Neo4j relevance boost) → `rrf` (Reciprocal Rank Fusion to merge ranked results).

### Graceful Degradation

Neo4j/Qdrant/GGUF model can each be unavailable independently. Graph commands return `[]` when Neo4j is down; search loses the corresponding boost but FTS5 always works if the project is indexed.

## Key Constraints

- **UUID5 parity with Python**: Symbol IDs are deterministic UUID5 using namespace `c0de1de0-0000-4000-8000-000000000000` and key format `{project_id}:{file_path}:{name}:{kind}:{byte_start}`. Must match the Python daemon's `Symbol.make_id()` exactly.
- **Config resolution order**: env vars (`GOBBY_NEO4J_URL`, etc.) → `config_store` table → hardcoded defaults.
- **Tree-sitter grammars**: Tier 1 (Python/JS/TS/Go/Rust/Java/C/C++/C#/Ruby/PHP/Swift/Kotlin), Tier 2 (Dart/Elixir), Tier 3 (JSON/YAML/Markdown). Adding a language requires a new `tree-sitter-*` dep in `Cargo.toml` and a grammar entry in `index/languages`.
