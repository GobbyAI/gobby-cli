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

The `code_symbols` vector module owns semantic indexing and search for extracted code symbols. It turns `Symbol` records into embedding text and Qdrant payloads, supports daemon-routed or direct embedding configuration through `EmbeddingSource`, and wraps embedding calls in `EmbeddingBackend`, which validates direct embedding config before building a client (`embedding.rs:22-48`). Payloads preserve symbol identity, source ranges, provenance, confidence, and optional summaries for round-tripping search hits back to indexed code (`types.rs:6-65`).

Lifecycle management is centered on `CodeSymbolVectorLifecycle`: it resolves the project collection name, validates the Qdrant boundary, initializes embedding and HTTP clients, and provides flows for ensuring collections, syncing file symbols, clearing project vectors, and rebuilding symbol vectors (`lifecycle.rs:22-57`). Qdrant-specific helpers keep collection naming compatible with the wider `gobby_core::qdrant` schema, expose project/file deletion helpers, and clean up vectors for files no longer present in the indexed set (`qdrant.rs:14-60`).

The module collaborates outward with `crate::config` for `EmbeddingConfig`, `QdrantConfig`, `CodeVectorSettings`, and `CODE_SYMBOL_COLLECTION_PREFIX`; with `crate::models::Symbol` for indexed code facts; and with `gobby_core` for AI routing, Qdrant request shapes, collection name validation, and degradation state (`embedding.rs:3-12`, `lifecycle.rs:5-18`, `qdrant.rs:6-10`). Internally, lifecycle code calls embedding helpers such as `dimension_probe_text` and `vector_text_for_symbol`, then uses Qdrant helpers such as `collection_name`, `collection_path`, `parse_collection_schema`, and delete APIs to maintain the vector store (`lifecycle.rs:12-20`).

| Area | Public symbols |
| --- | --- |
| Embedding | `EmbeddingSource`, `EmbeddingBackend`, `embedding_source_from_context`, `resolve_embedding_ai_context`, `embed_text`, `embed_text_batch`, `embed_query`, `probe_embedding_dim`, `vector_text_for_symbol` |
| Lifecycle | `CodeSymbolVectorLifecycle`, `resolve_lifecycle_qdrant_config`, `lifecycle_status`, `payload_map`, `point_ids` |
| Qdrant | `VectorOrphanCleanup`, `collection_name`, `delete_project_collection`, `delete_file_vectors`, `cleanup_orphan_file_vectors`, `delete_code_symbol_collections_with_prefix`, `parse_collection_schema` |
| Repository/Search | `fetch_symbols_for_file`, `fetch_symbols_for_project`, `search_code_symbols`, `semantic_search`, `vector_search` |
| Types | `CodeSymbolVectorSearchRequest`, `CodeSymbolVectorSearchHit`, `CodeSymbolVectorPayload`, `CodeSymbolVectorLifecycleStatus`, `VectorCollectionSchema`, `VectorLifecycleError` |

| Environment variable | Purpose | Default |
| --- | --- | --- |
| `GCODE_QDRANT_DELETE_TIMEOUT_SECS` | Overrides Qdrant delete timeout | `60s` (`qdrant.rs:14-17`) |
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

