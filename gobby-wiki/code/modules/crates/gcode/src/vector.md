---
title: crates/gcode/src/vector
type: code_module
provenance:
- file: crates/gcode/src/vector/code_symbols.rs
  ranges:
  - 1-29
- file: crates/gcode/src/vector/code_symbols/embedding.rs
  ranges:
  - 21-23
  - 26-29
  - 32-34
  - 38-40
  - 44-47
  - 50-64
  - 66-72
  - 74-101
  - 103-120
  - 123-126
  - 128-140
  - 142-145
  - 147-179
  - 181-203
  - 205-211
  - 213-216
  - 218-224
  - 226-247
  - 249-270
  - 272-287
  - 289-320
  - 331-333
  - 336-340
  - 344-346
  - 348-353
  - 357-391
  - 394-416
  - 419-442
- file: crates/gcode/src/vector/code_symbols/lifecycle.rs
  ranges:
  - 29-37
  - 39-43
  - 45-56
  - 59-82
  - 84-86
  - 88-98
  - 100-118
  - 120-141
  - 143-160
  - 162-182
  - 184-201
  - 203-205
  - 207-217
  - 219-240
  - 242-261
  - 263-282
  - 284-292
  - 294-307
  - 309-326
  - 328-367
  - 369-375
  - 378-389
  - 391-393
- file: crates/gcode/src/vector/code_symbols/qdrant.rs
  ranges:
  - 21-27
  - 29-35
  - 37-39
  - 41-48
  - 50-58
  - 60-85
  - 87-143
  - 145-163
  - 165-192
  - 194-215
  - 217-227
  - 229-240
  - 242-257
  - 259-268
  - 270-280
  - 282-289
  - 291-310
  - 312-333
  - 335-343
  - 345-415
  - 417-427
  - 434-439
  - 442-452
- file: crates/gcode/src/vector/code_symbols/repository.rs
  ranges:
  - 6-18
  - 20-25
  - 27-35
  - 38-43
  - 45-56
  - 59-77
- file: crates/gcode/src/vector/code_symbols/search.rs
  ranges:
  - 8-14
  - 17-25
  - 30-58
  - 63-81
- file: crates/gcode/src/vector/code_symbols/tests.rs
  ranges:
  - 20-41
  - 43-51
  - 53-67
  - 69-98
  - 100-120
  - 122-162
- file: crates/gcode/src/vector/code_symbols/types.rs
  ranges:
  - 7-12
  - 15-18
  - 21-23
  - 29-57
  - 60-95
  - 100-105
  - 108-112
  - 115-118
  - 121-124
  - 127-137
  - 140-162
  - 165-202
  - 206-208
- file: crates/gcode/src/vector/mod.rs
  ranges:
  - 1-2
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/vector/code_symbols.rs:1-29](crates/gcode/src/vector/code_symbols.rs#L1-L29)
- [crates/gcode/src/vector/code_symbols/embedding.rs:21-23](crates/gcode/src/vector/code_symbols/embedding.rs#L21-L23), [crates/gcode/src/vector/code_symbols/embedding.rs:26-29](crates/gcode/src/vector/code_symbols/embedding.rs#L26-L29), [crates/gcode/src/vector/code_symbols/embedding.rs:32-34](crates/gcode/src/vector/code_symbols/embedding.rs#L32-L34), [crates/gcode/src/vector/code_symbols/embedding.rs:38-40](crates/gcode/src/vector/code_symbols/embedding.rs#L38-L40), [crates/gcode/src/vector/code_symbols/embedding.rs:44-47](crates/gcode/src/vector/code_symbols/embedding.rs#L44-L47), [crates/gcode/src/vector/code_symbols/embedding.rs:50-64](crates/gcode/src/vector/code_symbols/embedding.rs#L50-L64), [crates/gcode/src/vector/code_symbols/embedding.rs:66-72](crates/gcode/src/vector/code_symbols/embedding.rs#L66-L72), [crates/gcode/src/vector/code_symbols/embedding.rs:74-101](crates/gcode/src/vector/code_symbols/embedding.rs#L74-L101), [crates/gcode/src/vector/code_symbols/embedding.rs:103-120](crates/gcode/src/vector/code_symbols/embedding.rs#L103-L120), [crates/gcode/src/vector/code_symbols/embedding.rs:123-126](crates/gcode/src/vector/code_symbols/embedding.rs#L123-L126), [crates/gcode/src/vector/code_symbols/embedding.rs:128-140](crates/gcode/src/vector/code_symbols/embedding.rs#L128-L140), [crates/gcode/src/vector/code_symbols/embedding.rs:142-145](crates/gcode/src/vector/code_symbols/embedding.rs#L142-L145), [crates/gcode/src/vector/code_symbols/embedding.rs:147-179](crates/gcode/src/vector/code_symbols/embedding.rs#L147-L179), [crates/gcode/src/vector/code_symbols/embedding.rs:181-203](crates/gcode/src/vector/code_symbols/embedding.rs#L181-L203), [crates/gcode/src/vector/code_symbols/embedding.rs:205-211](crates/gcode/src/vector/code_symbols/embedding.rs#L205-L211), [crates/gcode/src/vector/code_symbols/embedding.rs:213-216](crates/gcode/src/vector/code_symbols/embedding.rs#L213-L216), [crates/gcode/src/vector/code_symbols/embedding.rs:218-224](crates/gcode/src/vector/code_symbols/embedding.rs#L218-L224), [crates/gcode/src/vector/code_symbols/embedding.rs:226-247](crates/gcode/src/vector/code_symbols/embedding.rs#L226-L247), [crates/gcode/src/vector/code_symbols/embedding.rs:249-270](crates/gcode/src/vector/code_symbols/embedding.rs#L249-L270), [crates/gcode/src/vector/code_symbols/embedding.rs:272-287](crates/gcode/src/vector/code_symbols/embedding.rs#L272-L287), [crates/gcode/src/vector/code_symbols/embedding.rs:289-320](crates/gcode/src/vector/code_symbols/embedding.rs#L289-L320), [crates/gcode/src/vector/code_symbols/embedding.rs:331-333](crates/gcode/src/vector/code_symbols/embedding.rs#L331-L333), [crates/gcode/src/vector/code_symbols/embedding.rs:336-340](crates/gcode/src/vector/code_symbols/embedding.rs#L336-L340), [crates/gcode/src/vector/code_symbols/embedding.rs:344-346](crates/gcode/src/vector/code_symbols/embedding.rs#L344-L346), [crates/gcode/src/vector/code_symbols/embedding.rs:348-353](crates/gcode/src/vector/code_symbols/embedding.rs#L348-L353), [crates/gcode/src/vector/code_symbols/embedding.rs:357-391](crates/gcode/src/vector/code_symbols/embedding.rs#L357-L391), [crates/gcode/src/vector/code_symbols/embedding.rs:394-416](crates/gcode/src/vector/code_symbols/embedding.rs#L394-L416), [crates/gcode/src/vector/code_symbols/embedding.rs:419-442](crates/gcode/src/vector/code_symbols/embedding.rs#L419-L442)
- [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37](crates/gcode/src/vector/code_symbols/lifecycle.rs#L29-L37), [crates/gcode/src/vector/code_symbols/lifecycle.rs:39-43](crates/gcode/src/vector/code_symbols/lifecycle.rs#L39-L43), [crates/gcode/src/vector/code_symbols/lifecycle.rs:45-56](crates/gcode/src/vector/code_symbols/lifecycle.rs#L45-L56), [crates/gcode/src/vector/code_symbols/lifecycle.rs:59-82](crates/gcode/src/vector/code_symbols/lifecycle.rs#L59-L82), [crates/gcode/src/vector/code_symbols/lifecycle.rs:84-86](crates/gcode/src/vector/code_symbols/lifecycle.rs#L84-L86), [crates/gcode/src/vector/code_symbols/lifecycle.rs:88-98](crates/gcode/src/vector/code_symbols/lifecycle.rs#L88-L98), [crates/gcode/src/vector/code_symbols/lifecycle.rs:100-118](crates/gcode/src/vector/code_symbols/lifecycle.rs#L100-L118), [crates/gcode/src/vector/code_symbols/lifecycle.rs:120-141](crates/gcode/src/vector/code_symbols/lifecycle.rs#L120-L141), [crates/gcode/src/vector/code_symbols/lifecycle.rs:143-160](crates/gcode/src/vector/code_symbols/lifecycle.rs#L143-L160), [crates/gcode/src/vector/code_symbols/lifecycle.rs:162-182](crates/gcode/src/vector/code_symbols/lifecycle.rs#L162-L182), [crates/gcode/src/vector/code_symbols/lifecycle.rs:184-201](crates/gcode/src/vector/code_symbols/lifecycle.rs#L184-L201), [crates/gcode/src/vector/code_symbols/lifecycle.rs:203-205](crates/gcode/src/vector/code_symbols/lifecycle.rs#L203-L205), [crates/gcode/src/vector/code_symbols/lifecycle.rs:207-217](crates/gcode/src/vector/code_symbols/lifecycle.rs#L207-L217), [crates/gcode/src/vector/code_symbols/lifecycle.rs:219-240](crates/gcode/src/vector/code_symbols/lifecycle.rs#L219-L240), [crates/gcode/src/vector/code_symbols/lifecycle.rs:242-261](crates/gcode/src/vector/code_symbols/lifecycle.rs#L242-L261), [crates/gcode/src/vector/code_symbols/lifecycle.rs:263-282](crates/gcode/src/vector/code_symbols/lifecycle.rs#L263-L282), [crates/gcode/src/vector/code_symbols/lifecycle.rs:284-292](crates/gcode/src/vector/code_symbols/lifecycle.rs#L284-L292), [crates/gcode/src/vector/code_symbols/lifecycle.rs:294-307](crates/gcode/src/vector/code_symbols/lifecycle.rs#L294-L307), [crates/gcode/src/vector/code_symbols/lifecycle.rs:309-326](crates/gcode/src/vector/code_symbols/lifecycle.rs#L309-L326), [crates/gcode/src/vector/code_symbols/lifecycle.rs:328-367](crates/gcode/src/vector/code_symbols/lifecycle.rs#L328-L367), [crates/gcode/src/vector/code_symbols/lifecycle.rs:369-375](crates/gcode/src/vector/code_symbols/lifecycle.rs#L369-L375), [crates/gcode/src/vector/code_symbols/lifecycle.rs:378-389](crates/gcode/src/vector/code_symbols/lifecycle.rs#L378-L389), [crates/gcode/src/vector/code_symbols/lifecycle.rs:391-393](crates/gcode/src/vector/code_symbols/lifecycle.rs#L391-L393)
- [crates/gcode/src/vector/code_symbols/qdrant.rs:21-27](crates/gcode/src/vector/code_symbols/qdrant.rs#L21-L27), [crates/gcode/src/vector/code_symbols/qdrant.rs:29-35](crates/gcode/src/vector/code_symbols/qdrant.rs#L29-L35), [crates/gcode/src/vector/code_symbols/qdrant.rs:37-39](crates/gcode/src/vector/code_symbols/qdrant.rs#L37-L39), [crates/gcode/src/vector/code_symbols/qdrant.rs:41-48](crates/gcode/src/vector/code_symbols/qdrant.rs#L41-L48), [crates/gcode/src/vector/code_symbols/qdrant.rs:50-58](crates/gcode/src/vector/code_symbols/qdrant.rs#L50-L58), [crates/gcode/src/vector/code_symbols/qdrant.rs:60-85](crates/gcode/src/vector/code_symbols/qdrant.rs#L60-L85), [crates/gcode/src/vector/code_symbols/qdrant.rs:87-143](crates/gcode/src/vector/code_symbols/qdrant.rs#L87-L143), [crates/gcode/src/vector/code_symbols/qdrant.rs:145-163](crates/gcode/src/vector/code_symbols/qdrant.rs#L145-L163), [crates/gcode/src/vector/code_symbols/qdrant.rs:165-192](crates/gcode/src/vector/code_symbols/qdrant.rs#L165-L192), [crates/gcode/src/vector/code_symbols/qdrant.rs:194-215](crates/gcode/src/vector/code_symbols/qdrant.rs#L194-L215), [crates/gcode/src/vector/code_symbols/qdrant.rs:217-227](crates/gcode/src/vector/code_symbols/qdrant.rs#L217-L227), [crates/gcode/src/vector/code_symbols/qdrant.rs:229-240](crates/gcode/src/vector/code_symbols/qdrant.rs#L229-L240), [crates/gcode/src/vector/code_symbols/qdrant.rs:242-257](crates/gcode/src/vector/code_symbols/qdrant.rs#L242-L257), [crates/gcode/src/vector/code_symbols/qdrant.rs:259-268](crates/gcode/src/vector/code_symbols/qdrant.rs#L259-L268), [crates/gcode/src/vector/code_symbols/qdrant.rs:270-280](crates/gcode/src/vector/code_symbols/qdrant.rs#L270-L280), [crates/gcode/src/vector/code_symbols/qdrant.rs:282-289](crates/gcode/src/vector/code_symbols/qdrant.rs#L282-L289), [crates/gcode/src/vector/code_symbols/qdrant.rs:291-310](crates/gcode/src/vector/code_symbols/qdrant.rs#L291-L310), [crates/gcode/src/vector/code_symbols/qdrant.rs:312-333](crates/gcode/src/vector/code_symbols/qdrant.rs#L312-L333), [crates/gcode/src/vector/code_symbols/qdrant.rs:335-343](crates/gcode/src/vector/code_symbols/qdrant.rs#L335-L343), [crates/gcode/src/vector/code_symbols/qdrant.rs:345-415](crates/gcode/src/vector/code_symbols/qdrant.rs#L345-L415), [crates/gcode/src/vector/code_symbols/qdrant.rs:417-427](crates/gcode/src/vector/code_symbols/qdrant.rs#L417-L427), [crates/gcode/src/vector/code_symbols/qdrant.rs:434-439](crates/gcode/src/vector/code_symbols/qdrant.rs#L434-L439), [crates/gcode/src/vector/code_symbols/qdrant.rs:442-452](crates/gcode/src/vector/code_symbols/qdrant.rs#L442-L452)
- [crates/gcode/src/vector/code_symbols/repository.rs:6-18](crates/gcode/src/vector/code_symbols/repository.rs#L6-L18), [crates/gcode/src/vector/code_symbols/repository.rs:20-25](crates/gcode/src/vector/code_symbols/repository.rs#L20-L25), [crates/gcode/src/vector/code_symbols/repository.rs:27-35](crates/gcode/src/vector/code_symbols/repository.rs#L27-L35), [crates/gcode/src/vector/code_symbols/repository.rs:38-43](crates/gcode/src/vector/code_symbols/repository.rs#L38-L43), [crates/gcode/src/vector/code_symbols/repository.rs:45-56](crates/gcode/src/vector/code_symbols/repository.rs#L45-L56), [crates/gcode/src/vector/code_symbols/repository.rs:59-77](crates/gcode/src/vector/code_symbols/repository.rs#L59-L77)
- [crates/gcode/src/vector/code_symbols/search.rs:8-14](crates/gcode/src/vector/code_symbols/search.rs#L8-L14), [crates/gcode/src/vector/code_symbols/search.rs:17-25](crates/gcode/src/vector/code_symbols/search.rs#L17-L25), [crates/gcode/src/vector/code_symbols/search.rs:30-58](crates/gcode/src/vector/code_symbols/search.rs#L30-L58), [crates/gcode/src/vector/code_symbols/search.rs:63-81](crates/gcode/src/vector/code_symbols/search.rs#L63-L81)
- [crates/gcode/src/vector/code_symbols/tests.rs:20-41](crates/gcode/src/vector/code_symbols/tests.rs#L20-L41), [crates/gcode/src/vector/code_symbols/tests.rs:43-51](crates/gcode/src/vector/code_symbols/tests.rs#L43-L51), [crates/gcode/src/vector/code_symbols/tests.rs:53-67](crates/gcode/src/vector/code_symbols/tests.rs#L53-L67), [crates/gcode/src/vector/code_symbols/tests.rs:69-98](crates/gcode/src/vector/code_symbols/tests.rs#L69-L98), [crates/gcode/src/vector/code_symbols/tests.rs:100-120](crates/gcode/src/vector/code_symbols/tests.rs#L100-L120), [crates/gcode/src/vector/code_symbols/tests.rs:122-162](crates/gcode/src/vector/code_symbols/tests.rs#L122-L162)
- [crates/gcode/src/vector/code_symbols/types.rs:7-12](crates/gcode/src/vector/code_symbols/types.rs#L7-L12), [crates/gcode/src/vector/code_symbols/types.rs:15-18](crates/gcode/src/vector/code_symbols/types.rs#L15-L18), [crates/gcode/src/vector/code_symbols/types.rs:21-23](crates/gcode/src/vector/code_symbols/types.rs#L21-L23), [crates/gcode/src/vector/code_symbols/types.rs:29-57](crates/gcode/src/vector/code_symbols/types.rs#L29-L57), [crates/gcode/src/vector/code_symbols/types.rs:60-95](crates/gcode/src/vector/code_symbols/types.rs#L60-L95), [crates/gcode/src/vector/code_symbols/types.rs:100-105](crates/gcode/src/vector/code_symbols/types.rs#L100-L105), [crates/gcode/src/vector/code_symbols/types.rs:108-112](crates/gcode/src/vector/code_symbols/types.rs#L108-L112), [crates/gcode/src/vector/code_symbols/types.rs:115-118](crates/gcode/src/vector/code_symbols/types.rs#L115-L118), [crates/gcode/src/vector/code_symbols/types.rs:121-124](crates/gcode/src/vector/code_symbols/types.rs#L121-L124), [crates/gcode/src/vector/code_symbols/types.rs:127-137](crates/gcode/src/vector/code_symbols/types.rs#L127-L137), [crates/gcode/src/vector/code_symbols/types.rs:140-162](crates/gcode/src/vector/code_symbols/types.rs#L140-L162), [crates/gcode/src/vector/code_symbols/types.rs:165-202](crates/gcode/src/vector/code_symbols/types.rs#L165-L202), [crates/gcode/src/vector/code_symbols/types.rs:206-208](crates/gcode/src/vector/code_symbols/types.rs#L206-L208)
- [crates/gcode/src/vector/mod.rs:1-2](crates/gcode/src/vector/mod.rs#L1-L2)

</details>

# crates/gcode/src/vector

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The `crates/gcode/src/vector` module serves as the primary entry point for vector-related operations and code-symbol indexing within the `gcode` crate [crates/gcode/src/vector/mod.rs:1-2]. By re-exporting APIs from its underlying `code_symbols` submodule, this module aggregates and coordinates embedding generation, lifecycle management, Qdrant/vector database interactions, repository lookups, semantic searches, and common data structures [crates/gcode/src/vector/code_symbols.rs:1-29]. It plays a critical role in bridging codebase symbol extraction with vector retrieval, enabling the system to transform symbol metadata into embeddings and maintain synchronized index collections [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37, crates/gcode/src/vector/code_symbols/repository.rs:6-18].

Key workflows within the module involve translating extracted symbol metadata into serializable payloads, coordinating database connections, and managing collection schemas [crates/gcode/src/vector/code_symbols/types.rs:29-57, crates/gcode/src/vector/code_symbols/qdrant.rs:21-27]. The module works hand-in-hand with the `gobby_core` crate to dynamically leverage AI daemon environments or establish direct connections to embedding providers via the `EmbeddingBackend` [crates/gcode/src/vector/code_symbols/embedding.rs:21-23, crates/gcode/src/vector/code_symbols/embedding.rs:44-47]. In instances where transport configurations are absent or network errors arise, it is designed to degrade gracefully rather than fail abruptly, reporting appropriate warnings to the user [crates/gcode/src/vector/code_symbols/search.rs:63-81].

| Area | Re-exported Public API Symbols | Source Reference |
| --- | --- | --- |
| **Embeddings** | `EmbeddingBackend`, `EmbeddingSource`, `embed_query`, `embed_query_with_source`, `embed_text`, `embed_text_batch`, `embedding_client`, `embedding_source_from_context`, `probe_embedding_dim`, `vector_text_for_symbol` | [crates/gcode/src/vector/code_symbols.rs:7-12] |
| **Lifecycle** | `CodeSymbolVectorLifecycle`, `lifecycle_status`, `resolve_lifecycle_qdrant_config` | [crates/gcode/src/vector/code_symbols.rs:13] |
| **Qdrant Storage** | `VECTOR_DISTANCE_COSINE`, `VectorOrphanCleanup`, `cleanup_orphan_file_vectors`, `collection_name`, `delete_code_symbol_collections_with_prefix`, `delete_file_vectors`, `delete_project_collection`, `vector_search` | [crates/gcode/src/vector/code_symbols.rs:14-18] |
| **Repository Lookup** | `fetch_symbols_for_file`, `fetch_symbols_for_project` | [crates/gcode/src/vector/code_symbols.rs:19] |
| **Search** | `SearchError`, `search_code_symbols`, `semantic_search` | [crates/gcode/src/vector/code_symbols.rs:20] |
| **Types & Payloads** | `CodeSymbolVectorLifecycleAction`, `CodeSymbolVectorLifecycleOutput`, `CodeSymbolVectorLifecycleStatus`, `CodeSymbolVectorPayload`, `CodeSymbolVectorSearchHit`, `CodeSymbolVectorSearchRequest`, `VectorCollectionSchema`, `VectorLifecycleError` | [crates/gcode/src/vector/code_symbols.rs:21-26] |

## Dependency Diagram

`degraded: graph-truncated`

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/vector/code_symbols\|crates/gcode/src/vector/code_symbols]] | The `crates/gcode/src/vector/code_symbols` module manages the lifecycle, indexing, and vector searching of project code-symbol definitions within a Qdrant database instance [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37]. It bridges database symbol storage with embedding generators and Qdrant collections [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37, crates/gcode/src/vector/code_symbols/repository.rs:6-18]. The module coordinates with the `gobby_core` crate to leverage AI daemon environments or directly configure connections to embedding providers via an `EmbeddingBackend` [crates/gcode/src/vector/code_symbols/embedding.rs:21-23, crates/gcode/src/vector/code_symbols/embedding.rs:44-47]. Through these collaboration points, it translates extracted symbol metadata into serializable payloads, resolves Qdrant configurations, handles collection schemas, and gracefully degrades when transport errors or missing configurations prevent a full search [crates/gcode/src/vector/code_symbols/types.rs:29-57, crates/gcode/src/vector/code_symbols/qdrant.rs:21-27, crates/gcode/src/vector/code_symbols/search.rs:63-81]. Key operations flow through several primary pipelines. In the indexing flow, symbols are fetched from the database repository using SQL predicates and ordered by location [crates/gcode/src/vector/code_symbols/repository.rs:27-35, crates/gcode/src/vector/code_symbols/repository.rs:45-56]. The lifecycle manager converts these symbols into vector payloads and batches them to Qdrant [crates/gcode/src/vector/code_symbols/lifecycle.rs:45-56, crates/gcode/src/vector/code_symbols/types.rs:29-57]. The cleanup flow utilizes paginated Qdrant scrolling to list stored files and target orphaned or stale records for removal [crates/gcode/src/vector/code_symbols/qdrant.rs:50-58]. Finally, the search flow processes natural-language queries, converts them to embedding vectors via the configured backend, executes searches against collection endpoints, and formats scores into structured hits to ranking layers [crates/gcode/src/vector/code_symbols/search.rs:17-25, crates/gcode/src/vector/code_symbols/search.rs:30-58]. ### Environment Variables \| Variable \| Description \| \| --- \| --- \| \| `GCODE_QDRANT_DELETE_TIMEOUT_SECS` \| Sets the custom duration in seconds for Qdrant collection and vector deletion timeouts . \| ### Public API Symbols \| Symbol \| Type \| Description \| \| --- \| --- \| --- \| \| `CodeSymbolVectorLifecycle` \| struct \| Ties together project states, embedding backends, and Qdrant requests for schema and vector synchronization [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37]. \| \| `EmbeddingBackend` \| struct \| Routes direct or daemon-based embedding computations for raw text or search queries [crates/gcode/src/vector/code_symbols/embedding.rs:44-47]. \| \| `EmbeddingSource` \| enum \| Represents direct configuration or daemon-backed AI context [crates/gcode/src/vector/code_symbols/embedding.rs:26-29]. \| \| `VectorOrphanCleanup` \| struct \| Captures status metrics for orphaned vector scanning and deletion [crates/gcode/src/vector/code_symbols/qdrant.rs:21-27]. \| \| `CodeSymbolVectorPayload` \| struct \| Standard serializable layout for symbol attributes and provenance [crates/gcode/src/vector/code_symbols/types.rs:29-57]. \| \| `CodeSymbolVectorSearchRequest` \| struct \| Encapsulates request parameters for querying vector collections [crates/gcode/src/vector/code_symbols/types.rs:7-12]. \| \| `CodeSymbolVectorSearchHit` \| struct \| Represents a matched symbol ID and score pair from a vector search [crates/gcode/src/vector/code_symbols/types.rs:15-18]. \| \| `search_code_symbols` \| function \| Runs a vector search by embedding a query and calling Qdrant collections [crates/gcode/src/vector/code_symbols/search.rs:30-58]. \| \| `semantic_search` \| function \| Sits above vector search to act as the primary semantic ranking entry point [crates/gcode/src/vector/code_symbols/search.rs:63-81]. \| \| `fetch_symbols_for_file` \| function \| Retrieves symbols for a specific file from the database repository [crates/gcode/src/vector/code_symbols/repository.rs:6-18]. \| \| `fetch_symbols_for_project` \| function \| Retrieves symbols for an entire project from the database repository [crates/gcode/src/vector/code_symbols/repository.rs:20-25]. \| \| `delete_project_collection` \| function \| Deletes a project's entire vector collection in Qdrant [crates/gcode/src/vector/code_symbols/qdrant.rs:37-39]. \| \| `delete_file_vectors` \| function \| Clears vector embeddings associated with a single file [crates/gcode/src/vector/code_symbols/qdrant.rs:41-48]. \| \| `cleanup_orphan_file_vectors` \| function \| Deletes orphan file vectors by contrasting indexed files with Qdrant scrolls [crates/gcode/src/vector/code_symbols/qdrant.rs:50-58]. \| |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/vector/code_symbols.rs\|crates/gcode/src/vector/code_symbols.rs]] | Exports the code-symbol vector indexing and search API for the `gcode` crate, wiring together embedding, lifecycle management, Qdrant/vector storage, repository lookup, search, and shared types so other modules can work with symbol vectors through one entry point. [crates/gcode/src/vector/code_symbols.rs:1-29] |
| [[code/files/crates/gcode/src/vector/mod.rs\|crates/gcode/src/vector/mod.rs]] | Declares the `code_symbols` submodule for the `vector` crate module, indicating this file serves as the module entry point for vector-related code symbols. [crates/gcode/src/vector/mod.rs:1-2] |
