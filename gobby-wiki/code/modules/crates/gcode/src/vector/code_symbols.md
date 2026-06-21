---
title: crates/gcode/src/vector/code_symbols
type: code_module
provenance:
- file: crates/gcode/src/vector/code_symbols/embedding.rs
- file: crates/gcode/src/vector/code_symbols/lifecycle.rs
- file: crates/gcode/src/vector/code_symbols/qdrant.rs
- file: crates/gcode/src/vector/code_symbols/repository.rs
- file: crates/gcode/src/vector/code_symbols/search.rs
- file: crates/gcode/src/vector/code_symbols/tests.rs
- file: crates/gcode/src/vector/code_symbols/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols

Parent: [[code/modules/crates/gcode/src/vector|crates/gcode/src/vector]]

## Overview

## Module: `crates/gcode/src/vector/code_symbols`

This module implements the full vector-search pipeline for code symbols, covering every concern from raw text embedding through Qdrant collection management to scored semantic search. It is subdivided into five functional layers — types, embedding, lifecycle, Qdrant I/O, repository queries, and search — plus a test harness. The module keeps all Qdrant collections under a shared naming convention (`CODE_SYMBOL_COLLECTION_PREFIX`) enforced by `collection_name` (qdrant.rs) so that collections remain compatible with the Python daemon's existing Qdrant schema (qdrant.rs:13-14).

The embedding layer (`embedding.rs`) exposes an `EmbeddingBackend` that accepts two sources: a daemon-routed `AiContext` (using `gobby_core::ai::{daemon, effective_route}`) or a direct `EmbeddingConfig` with a raw HTTP client (embedding.rs:1-18). It provides single-text, query, and batch embedding entry points, and probes the model's output dimensionality via the sentinel string `"dimension_probe"` (embedding.rs:16-22). The lifecycle layer (`lifecycle.rs`) wraps `EmbeddingBackend` in `CodeSymbolVectorLifecycle`, which owns a `QdrantConfig`, a `reqwest` blocking client, and per-project collection state. Its methods manage the full collection lifecycle: schema creation, schema compatibility checks, per-file symbol upsert (in batches of `DEFAULT_UPSERT_BATCH_SIZE`), stale-vector deletion, and full project rebuilds. The Qdrant I/O layer (`qdrant.rs`) contains all raw HTTP calls — collection creation and deletion, filtered vector deletes, scroll-based file-path enumeration, and orphan cleanup — all keyed on a singleton `OnceLock<reqwest::blocking::Client>` (qdrant.rs:17-18). The repository layer (`repository.rs`) wraps SQL queries for fetching `Symbol` rows per file or project, while `search.rs` embeds a query, issues a `SearchRequest` to Qdrant, and maps results to `CodeSymbolVectorSearchHit` records.

The module sits inside `crates/gcode::vector` and is called into by higher-level gcode orchestration that drives indexing and semantic search flows. It imports from `gobby_core::ai_context`, `gobby_core::ai_types`, `gobby_core::degradation`, `gobby_core::qdrant`, and `gobby_core::config`, treating `gobby_core` as the shared infrastructure layer. Inbound callers receive `CodeSymbolVectorLifecycleStatus` / `CodeSymbolVectorLifecycleOutput` as progress/result envelopes and either a `VectorLifecycleError` or a `SearchError` on failure. The `tests.rs` file provides builder helpers (`test_symbol`, `test_context`, `spawn_http_responses`) and integration-style tests (`resolves_via_shared_routing`, `reads_endpoint_from_shared_binding`, `direct_source_uses_resolved_embedding_config`) that exercise the routing and config-resolution paths without requiring a live Qdrant instance.

### Public Types

| Symbol | Kind | File | Role |
|---|---|---|---|
| `EmbeddingSource` | enum | embedding.rs | Selects daemon vs. direct embedding path |
| `EmbeddingBackend` | struct | embedding.rs | HTTP client wrapper for embedding calls |
| `CodeSymbolVectorLifecycle` | struct | lifecycle.rs | Stateful collection + embedding manager |
| `CodeSymbolVectorLifecycleStatus` | struct | types.rs | Pre-run status envelope |
| `CodeSymbolVectorLifecycleOutput` | struct | types.rs | Post-run result envelope |
| `CodeSymbolVectorLifecycleAction` | type alias | types.rs | Enum of sync/rebuild/clear actions |
| `CodeSymbolVectorPayload` | struct | types.rs | Qdrant point payload schema |
| `CodeSymbolVectorSearchRequest` | struct | types.rs | Semantic search request parameters |
| `CodeSymbolVectorSearchHit` | struct | types.rs | Scored search result (symbol_id + score) |
| `VectorCollectionSchema` | struct | types.rs | Expected schema description |
| `ExistingVectorCollectionSchema` | struct | types.rs | Schema read back from Qdrant |
| `VectorLifecycleError` | type | types.rs | Lifecycle error variants |
| `SearchError` | type | search.rs | Search-phase error variants |
| `VectorOrphanCleanup` | struct | qdrant.rs | Orphan-deletion result summary |

### Key Public Functions

| Function | File | Description |
|---|---|---|
| `resolve_lifecycle_qdrant_config` | lifecycle.rs | Resolves `QdrantConfig` from a `ConfigSource` |
| `lifecycle_status` | lifecycle.rs | Constructs a pre-run `CodeSymbolVectorLifecycleStatus` |
| `search_code_symbols` | search.rs | End-to-end semantic search over a project's collection |
| `semantic_search` | search.rs | Lower-level Qdrant vector search call |
| `delete_project_collection` | qdrant.rs | Drops an entire project's Qdrant collection |
| `delete_file_vectors` | qdrant.rs | Removes all vectors for a specific file path |
| `cleanup_orphan_file_vectors` | qdrant.rs | Scrolls collection, removes files absent from the index |
| `delete_code_symbol_collections_with_prefix` | qdrant.rs | Bulk-deletes collections matching a prefix |
| `fetch_symbols_for_file` | repository.rs | SQL query: symbols by file path |
| `fetch_symbols_for_project` | repository.rs | SQL query: all symbols for a project |
| `embed_text` / `embed_query` / `embed_text_batch` | embedding.rs | Embedding call entry points |
| `probe_embedding_dim` | embedding.rs | Detects vector dimension from live model |
| `vector_text_for_symbol` | embedding.rs | Serialises a `Symbol` to its embedding input string |

### Environment Variables

| Variable | Default | Description |
|---|---|---|
| `GCODE_QDRANT_DELETE_TIMEOUT_SECS` | `60` s | Timeout for Qdrant delete operations (qdrant.rs:14-16) |

### Qdrant Collection Naming

Collections are constructed as `gcode:<CODE_SYMBOL_COLLECTION_PREFIX><project_id>` via `collection_name(collection_prefix, project_id)` (qdrant.rs:29-35), ensuring namespace isolation per project and compatibility with the daemon's Python-side collections (qdrant.rs:13).
[crates/gcode/src/vector/code_symbols/embedding.rs:21-23]
[crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37]
[crates/gcode/src/vector/code_symbols/qdrant.rs:21-27]
[crates/gcode/src/vector/code_symbols/repository.rs:6-18]
[crates/gcode/src/vector/code_symbols/search.rs:8-14]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/vector/code_symbols/embedding.rs\|crates/gcode/src/vector/code_symbols/embedding.rs]] | `crates/gcode/src/vector/code_symbols/embedding.rs` exposes 28 indexed API symbols. |
| [[code/files/crates/gcode/src/vector/code_symbols/lifecycle.rs\|crates/gcode/src/vector/code_symbols/lifecycle.rs]] | `crates/gcode/src/vector/code_symbols/lifecycle.rs` exposes 23 indexed API symbols. |
| [[code/files/crates/gcode/src/vector/code_symbols/qdrant.rs\|crates/gcode/src/vector/code_symbols/qdrant.rs]] | `crates/gcode/src/vector/code_symbols/qdrant.rs` exposes 23 indexed API symbols. |
| [[code/files/crates/gcode/src/vector/code_symbols/repository.rs\|crates/gcode/src/vector/code_symbols/repository.rs]] | `crates/gcode/src/vector/code_symbols/repository.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gcode/src/vector/code_symbols/search.rs\|crates/gcode/src/vector/code_symbols/search.rs]] | `crates/gcode/src/vector/code_symbols/search.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/vector/code_symbols/tests.rs\|crates/gcode/src/vector/code_symbols/tests.rs]] | `crates/gcode/src/vector/code_symbols/tests.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gcode/src/vector/code_symbols/types.rs\|crates/gcode/src/vector/code_symbols/types.rs]] | `crates/gcode/src/vector/code_symbols/types.rs` exposes 13 indexed API symbols. |

