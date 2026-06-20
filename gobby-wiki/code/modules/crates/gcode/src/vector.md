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

The `crates/gcode/src/vector` module is a narrow public entry point for vector-backed code-symbol functionality. Its root module currently exposes only `code_symbols`, while `code_symbols.rs` fans out into embedding, lifecycle, Qdrant, repository, search, and type submodules, then re-exports their public surface for callers (`crates/gcode/src/vector/mod.rs:1-2`, `crates/gcode/src/vector/code_symbols.rs:1-23`). The child module owns semantic indexing and search for extracted `Symbol` records: it builds embedding text, creates Qdrant payloads that preserve symbol identity and source metadata, and supports daemon-routed or direct embedding configuration through `EmbeddingSource`.

The main flow starts with repository fetches for file or project symbols, converts each symbol into vector text and payloads, embeds those texts through `EmbeddingBackend` or standalone embedding helpers, and synchronizes them into Qdrant collections through `CodeSymbolVectorLifecycle` (`crates/gcode/src/vector/code_symbols.rs:7-19`). Search reverses the path: query text is embedded, `vector_search` retrieves Qdrant matches, and `search_code_symbols` / `semantic_search` expose higher-level code-symbol search results (`crates/gcode/src/vector/code_symbols.rs:13-21`). Lifecycle helpers also cover collection creation, schema compatibility, stale-vector deletion, rebuilds, project cleanup, and orphan cleanup.

Collaboration is intentionally concentrated through re-exports. External code imports from `vector::code_symbols` instead of reaching into internal files, while this facade calls out internally to `embedding`, `lifecycle`, `qdrant`, `repository`, `search`, and `types` (`crates/gcode/src/vector/code_symbols.rs:1-23`). The module also imports its own test module behind `#[cfg(test)]`, keeping tests colocated without exposing them in normal builds (`crates/gcode/src/vector/code_symbols.rs:25-26`).

| Public area | Symbols |
| --- | --- |
| Embedding | `EmbeddingBackend`, `EmbeddingSource`, `embed_query`, `embed_query_with_source`, `embed_text`, `embed_text_batch`, `embedding_client`, `embedding_source_from_context`, `probe_embedding_dim`, `vector_text_for_symbol` |
| Lifecycle | `CodeSymbolVectorLifecycle`, `lifecycle_status`, `resolve_lifecycle_qdrant_config` |
| Qdrant | `VECTOR_DISTANCE_COSINE`, `VectorOrphanCleanup`, `cleanup_orphan_file_vectors`, `collection_name`, `delete_code_symbol_collections_with_prefix`, `delete_file_vectors`, `delete_project_collection`, `vector_search` |
| Repository | `fetch_symbols_for_file`, `fetch_symbols_for_project` |
| Search | `SearchError`, `search_code_symbols`, `semantic_search` |
| Types | `CodeSymbolVectorLifecycleAction`, `CodeSymbolVectorLifecycleOutput`, `CodeSymbolVectorLifecycleStatus`, `CodeSymbolVectorPayload`, `CodeSymbolVectorSearchHit`, `CodeSymbolVectorSearchRequest`, `VectorCollectionSchema`, `VectorLifecycleError` |

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/vector/code_symbols\|crates/gcode/src/vector/code_symbols]] | The `code_symbols` vector module owns semantic indexing and search for extracted code symbols. It turns `Symbol` records into embedding text and Qdrant payloads, supports daemon-routed or direct embedding configuration through `EmbeddingSource`, and wraps embedding calls in `EmbeddingBackend`, which validates direct embedding config before building a client (`embedding.rs:22-48`). Payloads preserve symbol identity, source ranges, provenance, confidence, and optional summaries for round-tripping search hits back to indexed code (`types.rs:6-65`). |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/vector/code_symbols.rs\|crates/gcode/src/vector/code_symbols.rs]] | `crates/gcode/src/vector/code_symbols.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/vector/mod.rs\|crates/gcode/src/vector/mod.rs]] | `crates/gcode/src/vector/mod.rs` has no indexed API symbols. |

