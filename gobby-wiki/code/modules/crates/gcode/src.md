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

`crates/gcode/src` is the main gcode application crate: it owns the CLI surface, configuration/context resolution, PostgreSQL code-index access, graph/vector projection lifecycle, search/grep commands, setup, freshness, visibility, and shared output/model contracts. The command layer is thin orchestration: handlers resolve `Context`, connect to backing services, apply scope and visibility rules, then render through `output::Format`; `grep` follows this pattern over indexed chunks, while `search` merges exact, BM25, vector, and graph-style results (`crates/gcode/src/commands/grep.rs:1-100`, `crates/gcode/src/commands/search.rs:1-100`).

The data flow centers on PostgreSQL as the indexed fact store and optional projections for richer retrieval. The `db` boundary resolves the hub DSN, opens read/write or read-only connections, validates schema, and exposes query APIs over indexed files, projects, graph facts, and sync state (`crates/gcode/src/db/mod.rs:1-36`, `crates/gcode/src/db/queries.rs:1-100`). Graph projection is owned under `graph::code_graph`: `CodeGraph::sync_file` turns PostgreSQL imports, definitions, and calls into FalkorDB `IMPORTS`, `DEFINES`, and `CALLS` edges with provenance metadata (`crates/gcode/src/graph/code_graph/write.rs:18-31`, `crates/gcode/src/graph/code_graph/write.rs:43-100`, `crates/gcode/src/graph/code_graph/write/mutation.rs:1-100`). Vector projection is exposed through `vector::code_symbols`, which embeds extracted `Symbol` records and stores Qdrant payloads with source metadata (`crates/gcode/src/vector/mod.rs:1-2`, `crates/gcode/src/vector/code_symbols.rs:1-23`).

Collaboration points are explicit. The config layer imports `gobby_core` AI/config/provisioning APIs, `postgres::Client`, crate-local `db`, and `secrets`, then resolves service values from environment, PostgreSQL config, standalone config, and secret expansion (`crates/gcode/src/config/services.rs:1-18`, `crates/gcode/src/config/services.rs:24-57`). Graph read commands import `Context`, `db`, `graph::code_graph`, FTS symbol resolution, shared models, and output formatting, degrading to empty paged responses with hints when FalkorDB is missing or unreachable (`crates/gcode/src/commands/graph/reads.rs:1-64`). Search similarly imports FTS, graph boost, RRF, vector symbols, visibility, models, and output, then fetches generously for merged ranking (`crates/gcode/src/commands/search.rs:1-56`).

| Public Surface | Responsibility |
| --- | --- |
| `Cli`, `Command`, `GraphCommand`, `VectorCommand`, `EmbeddingsCommand` | Parsed CLI entry points and command families |
| `Context`, `ServiceConfigSelection`, `FalkorConfig`, `CodeVectorSettings` | Runtime project and service configuration |
| `Symbol`, `IndexedFile`, `ImportRelation`, `CallRelation`, `SearchResult`, `GraphResult` | Shared code-index and result models |
| `connect_readonly`, `connect_readwrite`, `read_graph_file_facts` | PostgreSQL access and indexed fact queries |
| `CodeGraph`, `sync_file`, `clear_project`, `cleanup_orphans` | FalkorDB projection lifecycle |
| `Format`, `print_json`, `print_text` | Shared output rendering |

| Environment / Config Key | Purpose |
| --- | --- |
| `GOBBY_FALKORDB_HOST` / `databases.falkordb.host` | FalkorDB host override (`crates/gcode/src/config/services.rs:24-38`) |
| `GOBBY_FALKORDB_PORT` / `databases.falkordb.port` | FalkorDB port override (`crates/gcode/src/config/services.rs:24-38`) |
| `GOBBY_FALKORDB_PASSWORD` / `databases.falkordb.password` | FalkorDB password override (`crates/gcode/src/config/services.rs:24-38`) |
| `GOBBY_QDRANT_URL` / `databases.qdrant.url` | Qdrant endpoint override (`crates/gcode/src/config/services.rs:24-38`) |
| `GOBBY_QDRANT_API_KEY` / `databases.qdrant.api_key` | Qdrant API key override (`crates/gcode/src/config/services.rs:24-38`) |

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/cli\|crates/gcode/src/cli]] | The `crates/gcode/src/cli` test surface enforces that every leaf Clap command exposed by `Cli::command()` is documented in the generated Gobby contract. It imports the parent CLI definitions with `super::*`, uses Clap’s `CommandFactory`, and compares discovered command paths against `gobby_code::contract::contract().commands` . |
| [[code/modules/crates/gcode/src/commands\|crates/gcode/src/commands]] | `crates/gcode/src/commands` is the CLI command layer for indexing, search, inspection, setup, status, graph/vector lifecycle, and CodeWiki generation. Command handlers consistently take resolved configuration context, connect to backing services, apply scope/visibility filters, and render through the shared output layer: `grep` imports `Context`, `ProjectIndexScope`, `db`, `output::Format`, FTS helpers, and visibility controls before its `run` opens a readonly database connection, builds filters, loads indexed chunks, and applies the matcher (`crates/gcode/src/commands/grep.rs:1-100`).… |
| [[code/modules/crates/gcode/src/config\|crates/gcode/src/config]] | `crates/gcode/src/config` is the gcode configuration layer. Its `context.rs` facade documents the resolution order as `bootstrap.yaml -> PostgreSQL hub -> config_store -> service configs`, including `$secret:NAME` and `${VAR}` expansion, and exposes the typed service settings used by the rest of gcode . It delegates concrete service resolution to `services.rs`, importing `resolve_falkordb_config`, `resolve_qdrant_config`, `resolve_embedding_config`, `resolve_code_vector_settings`, `resolve_indexing_settings`, and standalone config loading . |
| [[code/modules/crates/gcode/src/db\|crates/gcode/src/db]] | `crates/gcode/src/db` is the gcode database boundary: it resolves the hub PostgreSQL DSN, opens read/write or read-only connections, validates the runtime schema, delegates config reads to `gobby_core`, and re-exports the query and resolution APIs from its submodules (`crates/gcode/src/db/mod.rs:1-36`). Its query layer works over `postgres::GenericClient` and the gcode model types to read indexed file paths, project/file existence, graph facts, and graph sync state from hub tables such as `code_indexed_files` and `code_indexed_projects` (`crates/gcode/src/db/queries.rs:1-100`). |
| [[code/modules/crates/gcode/src/dispatch\|crates/gcode/src/dispatch]] | The `dispatch` module is responsible for turning parsed CLI commands into early execution decisions, service-configuration requirements, and stderr logging behavior. Its tests exercise dispatch internals via `use super::*`, while collaborating with CLI parsing and format resolution through `crate::cli::{Cli, effective_format}` and `clap::Parser` (`crates/gcode/src/dispatch/tests.rs:1-3`). |
| [[code/modules/crates/gcode/src/graph\|crates/gcode/src/graph]] | The `crates/gcode/src/graph` module is the public graph namespace for `gcode`, exposing `code_graph`, `report`, and `typed_query` as child modules (`crates/gcode/src/graph/mod.rs:1-3`). `code_graph` owns the code-index graph projection: it persists `Code*` FalkorDB nodes and edges derived from PostgreSQL index rows, making the projection a `gcode`-owned store (`crates/gcode/src/graph/code_graph/write.rs:1-4`). Its central write flow is `CodeGraph::sync_file`, which creates a sync token, maps imports, definitions, and calls into graph items, partitions call relations, then delegates mutation… |
| [[code/modules/crates/gcode/src/index\|crates/gcode/src/index]] | `crates/gcode/src/index` is the code indexing subsystem: it discovers files, classifies them for AST or content-only indexing, detects language, extracts symbols/imports/calls, chunks and hashes content, resolves imports, optionally performs C/C++ semantic call resolution, and persists facts. The language registry supplies tree-sitter extension/query specs through `LanguageSpec` (`crates/gcode/src/index/languages.rs:1-16`), while parser call extraction can fall back to textual language-specific scanners such as Dart, which filters imports/declarations and materializes call relations with… |
| [[code/modules/crates/gcode/src/projection\|crates/gcode/src/projection]] | `crates/gcode/src/projection` owns projection synchronization and cleanup for graph and vector backends. `mod.rs` exposes the projection submodule and provides deleted-file reconciliation: when graph configuration exists it deletes the graph projection, and when Qdrant is configured it deletes stored vectors, returning per-target failures instead of stopping at the first error (`crates/gcode/src/projection/mod.rs:1-36`). |
| [[code/modules/crates/gcode/src/search\|crates/gcode/src/search]] | The `crates/gcode/src/search` module is the search facade for gcode: it groups pg_search BM25 full-text search, graph-based ranking support, and Reciprocal Rank Fusion under `fts`, `graph_boost`, and `rrf` submodules (`crates/gcode/src/search/mod.rs:1-11`). The FTS layer keeps the legacy module name while executing PostgreSQL `pg_search` BM25 keyword search against Gobby’s PostgreSQL hub (`crates/gcode/src/search/fts.rs:1-4`). Its child modules cover symbols, content, counts, graph-symbol resolution, path/language filtering, snippets, and shared query sanitation via… |
| [[code/modules/crates/gcode/src/setup\|crates/gcode/src/setup]] | `crates/gcode/src/setup` owns standalone provisioning for the gcode PostgreSQL code index: request/status DTOs, secret redaction, DDL construction, identifier qualification, catalog contracts, compatibility checks, and reset helpers. `GcodeStandaloneSetup` carries a schema, qualifies relations, emits PostgreSQL object definitions, and implements the `gobby_core::setup::StandaloneSetup` contract; its DDL includes `pg_search` plus code-index tables such as `code_indexed_projects`, `code_indexed_files`, `code_symbols`, `code_content_chunks`, `code_imports`, and `code_calls`… |
| [[code/modules/crates/gcode/src/vector\|crates/gcode/src/vector]] | The `crates/gcode/src/vector` module is a narrow public entry point for vector-backed code-symbol functionality. Its root module currently exposes only `code_symbols`, while `code_symbols.rs` fans out into embedding, lifecycle, Qdrant, repository, search, and type submodules, then re-exports their public surface for callers (`crates/gcode/src/vector/mod.rs:1-2`, `crates/gcode/src/vector/code_symbols.rs:1-23`). The child module owns semantic indexing and search for extracted `Symbol` records: it builds embedding text, creates Qdrant payloads that preserve symbol identity and source metadata,… |

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

