---
title: crates/gcode/src/vector
type: code_module
provenance:
- file: crates/gcode/src/vector/code_symbols.rs
- file: crates/gcode/src/vector/code_symbols/embedding.rs
- file: crates/gcode/src/vector/code_symbols/lifecycle.rs
- file: crates/gcode/src/vector/code_symbols/qdrant.rs
- file: crates/gcode/src/vector/code_symbols/repository.rs
- file: crates/gcode/src/vector/code_symbols/search.rs
- file: crates/gcode/src/vector/code_symbols/tests.rs
- file: crates/gcode/src/vector/code_symbols/types.rs
- file: crates/gcode/src/vector/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

## Module: `crates/gcode/src/vector`

This module is the vector-search subsystem of the `gcode` crate. Its sole public entry point, `pub mod code_symbols` (mod.rs:1), aggregates six internal submodules — `embedding`, `lifecycle`, `qdrant`, `repository`, `search`, and `types` — behind a single flat re-export surface (code_symbols.rs:1-25). Consumers of the wider crate import everything they need from `gcode::vector::code_symbols` without having to reach into the individual submodules.

The module covers three major concerns. First, **embedding**: it wraps an AI backend (`EmbeddingBackend`) that converts code-symbol text into dense vectors via `embed_text`, `embed_text_batch`, and `embed_query`/`embed_query_with_source`, and exposes helpers such as `probe_embedding_dim` and `vector_text_for_symbol` for dimensionality probing and text preparation (code_symbols.rs:8-11). Second, **collection lifecycle**: `CodeSymbolVectorLifecycle` manages the full lifecycle of a Qdrant collection — creation, schema compatibility checks, symbol upsert, stale-vector pruning, and full rebuilds — backed by `resolve_lifecycle_qdrant_config` and `lifecycle_status` (code_symbols.rs:12). Third, **Qdrant I/O and search**: low-level Qdrant helpers (`collection_name`, `delete_project_collection`, `delete_file_vectors`, `cleanup_orphan_file_vectors`, `delete_code_symbol_collections_with_prefix`, `vector_search`, `VectorOrphanCleanup`) handle HTTP communication, collection naming conventions, and cosine-distance search (code_symbols.rs:13-17); `search_code_symbols` and `semantic_search` in the `search` submodule sit above that layer and return typed `CodeSymbolVectorSearchHit` results (code_symbols.rs:19).

Repository queries (`fetch_symbols_for_file`, `fetch_symbols_for_project`) and the full type vocabulary (`CodeSymbolVectorPayload`, `CodeSymbolVectorSearchRequest`, `CodeSymbolVectorSearchHit`, `VectorCollectionSchema`, `CodeSymbolVectorLifecycleStatus`, `VectorLifecycleError`, etc.) are also re-exported here so callers have a single import path (code_symbols.rs:18-24).

### Public API surface

| Symbol | Kind | Source submodule |
|---|---|---|
| `EmbeddingBackend` | struct | `embedding` |
| `EmbeddingSource` | type | `embedding` |
| `embed_text` / `embed_text_batch` | fn | `embedding` |
| `embed_query` / `embed_query_with_source` | fn | `embedding` |
| `embedding_client` | fn | `embedding` |
| `probe_embedding_dim` | fn | `embedding` |
| `embedding_source_from_context` | fn | `embedding` |
| `vector_text_for_symbol` | fn | `embedding` |
| `CodeSymbolVectorLifecycle` | struct | `lifecycle` |
| `lifecycle_status` | fn | `lifecycle` |
| `resolve_lifecycle_qdrant_config` | fn | `lifecycle` |
| `VectorOrphanCleanup` | struct | `qdrant` |
| `collection_name` | fn | `qdrant` |
| `delete_project_collection` / `delete_file_vectors` | fn | `qdrant` |
| `cleanup_orphan_file_vectors` | fn | `qdrant` |
| `delete_code_symbol_collections_with_prefix` | fn | `qdrant` |
| `vector_search` | fn | `qdrant` |
| `VECTOR_DISTANCE_COSINE` | const | `qdrant` |
| `fetch_symbols_for_file` / `fetch_symbols_for_project` | fn | `repository` |
| `search_code_symbols` / `semantic_search` | fn | `search` |
| `SearchError` | type | `search` |
| `CodeSymbolVectorPayload` | struct | `types` |
| `CodeSymbolVectorSearchRequest` / `CodeSymbolVectorSearchHit` | struct | `types` |
| `VectorCollectionSchema` | struct | `types` |
| `CodeSymbolVectorLifecycleAction` / `CodeSymbolVectorLifecycleStatus` / `CodeSymbolVectorLifecycleOutput` | type/struct | `types` |
| `VectorLifecycleError` | type | `types` |
[crates/gcode/src/vector/code_symbols/embedding.rs:21-23]
[crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37]
[crates/gcode/src/vector/code_symbols/qdrant.rs:21-27]
[crates/gcode/src/vector/code_symbols/repository.rs:6-18]
[crates/gcode/src/vector/code_symbols/search.rs:8-14]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/vector/code_symbols\|crates/gcode/src/vector/code_symbols]] | ## Module: `crates/gcode/src/vector/code_symbols` |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/vector/code_symbols.rs\|crates/gcode/src/vector/code_symbols.rs]] | `crates/gcode/src/vector/code_symbols.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/vector/mod.rs\|crates/gcode/src/vector/mod.rs]] | `crates/gcode/src/vector/mod.rs` has no indexed API symbols. |

