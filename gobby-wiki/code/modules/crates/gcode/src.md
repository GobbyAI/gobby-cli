---
title: crates/gcode/src
type: code_module
provenance:
- file: crates/gcode/src/commands/codewiki/architecture_diagrams.rs
- file: crates/gcode/src/commands/codewiki/build_parts/audit.rs
- file: crates/gcode/src/commands/codewiki/io.rs
- file: crates/gcode/src/commands/codewiki/prompts.rs
- file: crates/gcode/src/commands/codewiki/system_model.rs
- file: crates/gcode/src/commands/codewiki/text/sanitize.rs
- file: crates/gcode/src/commands/codewiki/types.rs
- file: crates/gcode/src/commands/graph/lifecycle.rs
- file: crates/gcode/src/commands/graph/reads.rs
- file: crates/gcode/src/commands/grep.rs
- file: crates/gcode/src/commands/search.rs
- file: crates/gcode/src/commands/status.rs
- file: crates/gcode/src/commands/symbol_at.rs
- file: crates/gcode/src/config/context.rs
- file: crates/gcode/src/config/services.rs
- file: crates/gcode/src/config/tests.rs
- file: crates/gcode/src/contract.rs
- file: crates/gcode/src/db/queries.rs
- file: crates/gcode/src/db/resolution.rs
- file: crates/gcode/src/graph/code_graph/payload.rs
- file: crates/gcode/src/graph/code_graph/write.rs
- file: crates/gcode/src/graph/report/types.rs
- file: crates/gcode/src/graph/typed_query.rs
- file: crates/gcode/src/index/languages.rs
- file: crates/gcode/src/index/semantic.rs
- file: crates/gcode/src/models.rs
- file: crates/gcode/src/projection/sync.rs
- file: crates/gcode/src/search/fts/tests.rs
- file: crates/gcode/src/vector/code_symbols/embedding.rs
- file: crates/gcode/src/visibility.rs
provenance_truncated: 185
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src

Parent: [[code/modules/crates/gcode|crates/gcode]]

## Overview

## crates/gcode/src

`crates/gcode/src` is the complete source tree for `gcode`, a Rust CLI binary that provides a unified code-intelligence platform over a PostgreSQL code index, an optional FalkorDB graph projection, and an optional Qdrant vector store. The binary entry point at `main.rs` initialises signal handling and delegates to `dispatch.rs`, which parses the Clap command tree defined in `cli.rs`, resolves a `Context` (project identity + database URL + optional service configs) through `config/context.rs` and `config/services.rs`, and routes each command to a handler. Early-exit commands such as `setup` bypass full context resolution so they can run without a live database connection `crates/gcode/src/dispatch.rs`.

The module is organised into eleven child sub-modules whose concerns are cleanly separated: `config` holds multi-source configuration resolution (environment variables, Postgres config store, `gcore_config` TOML, standalone bootstrap files); `db` holds all SQL queries against the Postgres code index; `index` drives file discovery, AST parsing, and fact ingestion; `graph` manages the FalkorDB code graph (connection pooling in `code_graph/connection.rs`, write batching in `code_graph/write/mutation.rs`, sync plans in `code_graph/write/sync_plan.rs`, and orphan cleanup in `code_graph/write/deletion.rs`); `search` performs multi-source symbol and content search with BM25 FTS, Qdrant vector retrieval, and FalkorDB graph boosting fused by Reciprocal Rank Fusion; `vector` wraps Qdrant lifecycle operations; `projection` coordinates post-index projection syncing across graph and vector backends; `dispatch` stitches context resolution to command dispatch; `setup` handles first-run schema provisioning; `cli` defines the Clap command/flag tree; and `commands` implements the user-facing operations (search, grep, graph reads, graph lifecycle, outline, symbol-at, etc.). Cross-cutting concerns — freshness gating (`freshness.rs`), advisory index locking (`index_lock.rs`), output formatting (`output.rs`), progress rendering (`progress.rs`), and token-budget management — live at the crate root.

The search command (`commands/search.rs`) illustrates the widest collaboration: it opens a read-only Postgres connection via `db::connect_readonly`, calls `fts::search_symbols_exact_first_visible` and `fts::search_symbols_fts_visible` for BM25 ranked results, calls into `code_symbols` for Qdrant semantic results, and optionally calls `graph_boost` for FalkorDB-reranked results, then merges all three with `rrf::merge` before serialising through `output::Format` `crates/gcode/src/commands/search.rs:1-100`. Graph read commands (`commands/graph/reads.rs`) follow a similar pattern but wrap every FalkorDB call in graceful degradation — returning an empty paged response with a typed `GraphReadError` hint when FalkorDB is not configured or unreachable `crates/gcode/src/commands/graph/reads.rs:1-100`. Configuration resolution chains environment variables, the Postgres config store (read via `gobby_core::postgres::read_config_value`), and a `StandaloneConfig` fallback, with secrets resolved through `secrets::resolve_config_value` `crates/gcode/src/config/services.rs:1-100`.

The crate imports heavily from `gobby_core` (AI context, config primitives, provisioning, RRF, chunking, BM25 schema) and from `gobby_core::postgres` for low-level query helpers. Outbound integration points are FalkorDB (via the `falkordb` crate, accessed through `graph/code_graph/connection.rs`), Qdrant (HTTP client in `vector`), the clangd LSP subprocess (in the `index` sub-module for C/C++ semantic resolution), and external AI endpoints for embedding and text generation.

### Top-level CLI commands

| Command group | Type alias |
|---|---|
| Root dispatcher | `Command` |
| Code graph lifecycle / reads | `GraphCommand` |
| Vector index lifecycle | `VectorCommand` |
| Embeddings diagnostics | `EmbeddingsCommand` |

### Key configuration & environment variables

| Key / Env var | Purpose |
|---|---|
| `GOBBY_FALKORDB_HOST` / `databases.falkordb.host` | FalkorDB host |
| `GOBBY_FALKORDB_PORT` / `databases.falkordb.port` | FalkorDB port |
| `GOBBY_FALKORDB_PASSWORD` / `databases.falkordb.password` | FalkorDB password |
| `GOBBY_QDRANT_URL` / `databases.qdrant.url` | Qdrant endpoint |
| `GOBBY_QDRANT_API_KEY` / `databases.qdrant.api_key` | Qdrant auth key |
| `GOBBY_POSTGRES_DSN` / `GCODE_DATABASE_URL` | Postgres connection (falling back in that order) |

### Core public model types

| Type | Role |
|---|---|
| `Symbol` | Indexed code symbol with stable UUID (`CODE_INDEX_UUID_NAMESPACE`) `crates/gcode/src/models.rs:1-100` |
| `ProjectionProvenance` (`Extracted` / `Inferred` / `Ambiguous`) | Confidence classification for graph/vector facts `crates/gcode/src/models.rs:1-100` |
| `ProjectionMetadata` | Provenance envelope attached to `GraphResult` and projection payloads |
| `IndexedFile`, `ContentChunk`, `ImportRelation`, `CallRelation` | Core code-fact record types persisted to Postgres |
| `PagedResponse<T>`, `GraphResult`, `SearchResult` | Wire-format response envelopes for JSON and text output |
| `Context` | Resolved runtime context (project identity, database URL, optional service configs) |
[crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81]
[crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98]
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29]
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:9-21]
[crates/gcode/src/graph/code_graph/write/deletion.rs:8-66]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/cli\|crates/gcode/src/cli]] | ## crates/gcode/src/cli |
| [[code/modules/crates/gcode/src/commands\|crates/gcode/src/commands]] | ## Module: `crates/gcode/src/commands` |
| [[code/modules/crates/gcode/src/config\|crates/gcode/src/config]] | ## crates/gcode/src/config |
| [[code/modules/crates/gcode/src/db\|crates/gcode/src/db]] | ## crates/gcode/src/db |
| [[code/modules/crates/gcode/src/dispatch\|crates/gcode/src/dispatch]] | ## crates/gcode/src/dispatch |
| [[code/modules/crates/gcode/src/graph\|crates/gcode/src/graph]] | ## crates/gcode/src/graph |
| [[code/modules/crates/gcode/src/index\|crates/gcode/src/index]] | ## Module: `crates/gcode/src/index` |
| [[code/modules/crates/gcode/src/projection\|crates/gcode/src/projection]] | ## crates/gcode/src/projection |
| [[code/modules/crates/gcode/src/search\|crates/gcode/src/search]] | ## Module: crates/gcode/src/search |
| [[code/modules/crates/gcode/src/setup\|crates/gcode/src/setup]] | ## crates/gcode/src/setup |
| [[code/modules/crates/gcode/src/vector\|crates/gcode/src/vector]] | ## Module: `crates/gcode/src/vector` |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/cli.rs\|crates/gcode/src/cli.rs]] | `crates/gcode/src/cli.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/graph/lifecycle.rs\|crates/gcode/src/commands/graph/lifecycle.rs]] | `crates/gcode/src/commands/graph/lifecycle.rs` exposes 25 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/graph/payload.rs\|crates/gcode/src/commands/graph/payload.rs]] | `crates/gcode/src/commands/graph/payload.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/graph/reads.rs\|crates/gcode/src/commands/graph/reads.rs]] | `crates/gcode/src/commands/graph/reads.rs` exposes 42 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/graph/tests.rs\|crates/gcode/src/commands/graph/tests.rs]] | `crates/gcode/src/commands/graph/tests.rs` exposes 24 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/search.rs\|crates/gcode/src/commands/search.rs]] | `crates/gcode/src/commands/search.rs` exposes 39 indexed API symbols. |
| [[code/files/crates/gcode/src/config.rs\|crates/gcode/src/config.rs]] | `crates/gcode/src/config.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/config/context.rs\|crates/gcode/src/config/context.rs]] | `crates/gcode/src/config/context.rs` exposes 38 indexed API symbols. |
| [[code/files/crates/gcode/src/config/services.rs\|crates/gcode/src/config/services.rs]] | `crates/gcode/src/config/services.rs` exposes 53 indexed API symbols. |
| [[code/files/crates/gcode/src/config/tests.rs\|crates/gcode/src/config/tests.rs]] | `crates/gcode/src/config/tests.rs` exposes 27 indexed API symbols. |
| [[code/files/crates/gcode/src/contract.rs\|crates/gcode/src/contract.rs]] | `crates/gcode/src/contract.rs` exposes 28 indexed API symbols. |
| [[code/files/crates/gcode/src/db/queries.rs\|crates/gcode/src/db/queries.rs]] | `crates/gcode/src/db/queries.rs` exposes 36 indexed API symbols. |
| [[code/files/crates/gcode/src/dispatch.rs\|crates/gcode/src/dispatch.rs]] | `crates/gcode/src/dispatch.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gcode/src/freshness.rs\|crates/gcode/src/freshness.rs]] | `crates/gcode/src/freshness.rs` exposes 22 indexed API symbols. |
| [[code/files/crates/gcode/src/git.rs\|crates/gcode/src/git.rs]] | `crates/gcode/src/git.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/connection.rs\|crates/gcode/src/graph/code_graph/connection.rs]] | `crates/gcode/src/graph/code_graph/connection.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/write.rs\|crates/gcode/src/graph/code_graph/write.rs]] | `crates/gcode/src/graph/code_graph/write.rs` exposes 27 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/write/deletion.rs\|crates/gcode/src/graph/code_graph/write/deletion.rs]] | `crates/gcode/src/graph/code_graph/write/deletion.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/write/mutation.rs\|crates/gcode/src/graph/code_graph/write/mutation.rs]] | `crates/gcode/src/graph/code_graph/write/mutation.rs` exposes 24 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/write/support.rs\|crates/gcode/src/graph/code_graph/write/support.rs]] | `crates/gcode/src/graph/code_graph/write/support.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/write/sync_plan.rs\|crates/gcode/src/graph/code_graph/write/sync_plan.rs]] | `crates/gcode/src/graph/code_graph/write/sync_plan.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/index_lock.rs\|crates/gcode/src/index_lock.rs]] | `crates/gcode/src/index_lock.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/gcode/src/lib.rs\|crates/gcode/src/lib.rs]] | `crates/gcode/src/lib.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gcode/src/main.rs\|crates/gcode/src/main.rs]] | `crates/gcode/src/main.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/models.rs\|crates/gcode/src/models.rs]] | `crates/gcode/src/models.rs` exposes 51 indexed API symbols. |
| [[code/files/crates/gcode/src/output.rs\|crates/gcode/src/output.rs]] | `crates/gcode/src/output.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/progress.rs\|crates/gcode/src/progress.rs]] | `crates/gcode/src/progress.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/project.rs\|crates/gcode/src/project.rs]] | `crates/gcode/src/project.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gcode/src/savings.rs\|crates/gcode/src/savings.rs]] | `crates/gcode/src/savings.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/schema.rs\|crates/gcode/src/schema.rs]] | `crates/gcode/src/schema.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gcode/src/search/fts/tests.rs\|crates/gcode/src/search/fts/tests.rs]] | `crates/gcode/src/search/fts/tests.rs` exposes 34 indexed API symbols. |
| [[code/files/crates/gcode/src/secrets.rs\|crates/gcode/src/secrets.rs]] | `crates/gcode/src/secrets.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/setup.rs\|crates/gcode/src/setup.rs]] | `crates/gcode/src/setup.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/skill.rs\|crates/gcode/src/skill.rs]] | `crates/gcode/src/skill.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gcode/src/utils.rs\|crates/gcode/src/utils.rs]] | `crates/gcode/src/utils.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/visibility.rs\|crates/gcode/src/visibility.rs]] | `crates/gcode/src/visibility.rs` exposes 28 indexed API symbols. |

