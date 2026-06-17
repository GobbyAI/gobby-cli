---
title: crates/gwiki/src/search/semantic.rs
type: code_file
provenance:
- file: crates/gwiki/src/search/semantic.rs
  ranges:
  - 18-22
  - 25-28
  - 30-35
  - 37-54
  - 57-61
  - 63-70
  - 72-163
  - 165-170
  - 172-174
  - 176-182
  - 184-204
  - 206-211
  - 214-226
  - 234-245
  - 250-252
  - 256-260
  - 265-267
  - 272-288
  - 290-305
  - 309-323
  - '327'
  - 331-333
  - 338-350
  - 355-364
  - 368-376
  - '379'
  - 382-389
  - 392-396
  - 398-411
  - 413-457
  - 459-461
  - 463-468
  - 470-478
  - 480-509
  - '512'
  - 516-524
  - 528-531
  - 535-540
  - 545-552
  - 556-560
  - 564-570
  - 575-584
  - '588'
  - 592-598
  - '602'
  - 606-613
  - 617-619
  - 623-637
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/search/semantic.rs:18-22](crates/gwiki/src/search/semantic.rs#L18-L22), [crates/gwiki/src/search/semantic.rs:25-28](crates/gwiki/src/search/semantic.rs#L25-L28), [crates/gwiki/src/search/semantic.rs:30-35](crates/gwiki/src/search/semantic.rs#L30-L35), [crates/gwiki/src/search/semantic.rs:37-54](crates/gwiki/src/search/semantic.rs#L37-L54), [crates/gwiki/src/search/semantic.rs:57-61](crates/gwiki/src/search/semantic.rs#L57-L61), [crates/gwiki/src/search/semantic.rs:63-70](crates/gwiki/src/search/semantic.rs#L63-L70), [crates/gwiki/src/search/semantic.rs:72-163](crates/gwiki/src/search/semantic.rs#L72-L163), [crates/gwiki/src/search/semantic.rs:165-170](crates/gwiki/src/search/semantic.rs#L165-L170), [crates/gwiki/src/search/semantic.rs:172-174](crates/gwiki/src/search/semantic.rs#L172-L174), [crates/gwiki/src/search/semantic.rs:176-182](crates/gwiki/src/search/semantic.rs#L176-L182), [crates/gwiki/src/search/semantic.rs:184-204](crates/gwiki/src/search/semantic.rs#L184-L204), [crates/gwiki/src/search/semantic.rs:206-211](crates/gwiki/src/search/semantic.rs#L206-L211), [crates/gwiki/src/search/semantic.rs:214-226](crates/gwiki/src/search/semantic.rs#L214-L226), [crates/gwiki/src/search/semantic.rs:234-245](crates/gwiki/src/search/semantic.rs#L234-L245), [crates/gwiki/src/search/semantic.rs:250-252](crates/gwiki/src/search/semantic.rs#L250-L252), [crates/gwiki/src/search/semantic.rs:256-260](crates/gwiki/src/search/semantic.rs#L256-L260), [crates/gwiki/src/search/semantic.rs:265-267](crates/gwiki/src/search/semantic.rs#L265-L267), [crates/gwiki/src/search/semantic.rs:272-288](crates/gwiki/src/search/semantic.rs#L272-L288), [crates/gwiki/src/search/semantic.rs:290-305](crates/gwiki/src/search/semantic.rs#L290-L305), [crates/gwiki/src/search/semantic.rs:309-323](crates/gwiki/src/search/semantic.rs#L309-L323), [crates/gwiki/src/search/semantic.rs:327](crates/gwiki/src/search/semantic.rs#L327), [crates/gwiki/src/search/semantic.rs:331-333](crates/gwiki/src/search/semantic.rs#L331-L333), [crates/gwiki/src/search/semantic.rs:338-350](crates/gwiki/src/search/semantic.rs#L338-L350), [crates/gwiki/src/search/semantic.rs:355-364](crates/gwiki/src/search/semantic.rs#L355-L364), [crates/gwiki/src/search/semantic.rs:368-376](crates/gwiki/src/search/semantic.rs#L368-L376), [crates/gwiki/src/search/semantic.rs:379](crates/gwiki/src/search/semantic.rs#L379), [crates/gwiki/src/search/semantic.rs:382-389](crates/gwiki/src/search/semantic.rs#L382-L389), [crates/gwiki/src/search/semantic.rs:392-396](crates/gwiki/src/search/semantic.rs#L392-L396), [crates/gwiki/src/search/semantic.rs:398-411](crates/gwiki/src/search/semantic.rs#L398-L411), [crates/gwiki/src/search/semantic.rs:413-457](crates/gwiki/src/search/semantic.rs#L413-L457), [crates/gwiki/src/search/semantic.rs:459-461](crates/gwiki/src/search/semantic.rs#L459-L461), [crates/gwiki/src/search/semantic.rs:463-468](crates/gwiki/src/search/semantic.rs#L463-L468), [crates/gwiki/src/search/semantic.rs:470-478](crates/gwiki/src/search/semantic.rs#L470-L478), [crates/gwiki/src/search/semantic.rs:480-509](crates/gwiki/src/search/semantic.rs#L480-L509), [crates/gwiki/src/search/semantic.rs:512](crates/gwiki/src/search/semantic.rs#L512), [crates/gwiki/src/search/semantic.rs:516-524](crates/gwiki/src/search/semantic.rs#L516-L524), [crates/gwiki/src/search/semantic.rs:528-531](crates/gwiki/src/search/semantic.rs#L528-L531), [crates/gwiki/src/search/semantic.rs:535-540](crates/gwiki/src/search/semantic.rs#L535-L540), [crates/gwiki/src/search/semantic.rs:545-552](crates/gwiki/src/search/semantic.rs#L545-L552), [crates/gwiki/src/search/semantic.rs:556-560](crates/gwiki/src/search/semantic.rs#L556-L560), [crates/gwiki/src/search/semantic.rs:564-570](crates/gwiki/src/search/semantic.rs#L564-L570), [crates/gwiki/src/search/semantic.rs:575-584](crates/gwiki/src/search/semantic.rs#L575-L584), [crates/gwiki/src/search/semantic.rs:588](crates/gwiki/src/search/semantic.rs#L588), [crates/gwiki/src/search/semantic.rs:592-598](crates/gwiki/src/search/semantic.rs#L592-L598), [crates/gwiki/src/search/semantic.rs:602](crates/gwiki/src/search/semantic.rs#L602), [crates/gwiki/src/search/semantic.rs:606-613](crates/gwiki/src/search/semantic.rs#L606-L613), [crates/gwiki/src/search/semantic.rs:617-619](crates/gwiki/src/search/semantic.rs#L617-L619), [crates/gwiki/src/search/semantic.rs:623-637](crates/gwiki/src/search/semantic.rs#L623-L637)

</details>

# crates/gwiki/src/search/semantic.rs

Module: [[code/modules/crates/gwiki/src/search|crates/gwiki/src/search]]

## Purpose

This file implements the semantic search pipeline for the wiki: it defines the request and outcome types, abstracts embedding and vector retrieval behind `QueryEmbedder` and `VectorSearchBackend`, and provides the top-level `search_semantic` flow that short-circuits empty requests, resolves the target collection by scope, embeds queries, runs the Qdrant search, and converts hits into wiki results. It also contains helpers for scope-to-collection mapping, payload filtering, result/degradation handling, and concrete backend adapters for direct, daemon, and OpenAI embeddings plus Qdrant-backed search. The remaining backend types are support and test doubles for unavailable, fixed, recording, failing, and status-based behavior.
[crates/gwiki/src/search/semantic.rs:18-22]
[crates/gwiki/src/search/semantic.rs:25-28]
[crates/gwiki/src/search/semantic.rs:30-35]
[crates/gwiki/src/search/semantic.rs:37-54]
[crates/gwiki/src/search/semantic.rs:44-53]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `SemanticSearchRequest` | class | `pub struct SemanticSearchRequest {` | `SemanticSearchRequest [class]` | `d6edffdf-1297-5822-aae4-00a043fe8092` | 18-22 [crates/gwiki/src/search/semantic.rs:18-22] | Indexed class `SemanticSearchRequest` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:18-22] |
| `SemanticSearchOutcome` | class | `pub struct SemanticSearchOutcome {` | `SemanticSearchOutcome [class]` | `95ea6dda-0ac2-5969-8bce-57f6cf74dfa1` | 25-28 [crates/gwiki/src/search/semantic.rs:25-28] | Indexed class `SemanticSearchOutcome` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:25-28] |
| `SemanticSearchBackend` | type | `pub trait SemanticSearchBackend {` | `SemanticSearchBackend [type]` | `964f66d5-41d8-50a4-abe7-7e7cd382834e` | 30-35 [crates/gwiki/src/search/semantic.rs:30-35] | Indexed type `SemanticSearchBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:30-35] |
| `QueryEmbedder` | type | `pub trait QueryEmbedder {` | `QueryEmbedder [type]` | `aa0b0e5d-7e99-5107-9a5c-8cd065d8c67a` | 37-54 [crates/gwiki/src/search/semantic.rs:37-54] | Indexed type `QueryEmbedder` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:37-54] |
| `QueryEmbedder.embed_queries` | method | `fn embed_queries(` | `QueryEmbedder.embed_queries [method]` | `40da33c3-a2c0-517a-8b45-6baf6e17108e` | 44-53 [crates/gwiki/src/search/semantic.rs:44-53] | Indexed method `QueryEmbedder.embed_queries` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:44-53] |
| `SemanticEmbedding` | type | `pub enum SemanticEmbedding {` | `SemanticEmbedding [type]` | `ed766e3a-dee2-5c09-ae98-11b3cb1edb6c` | 57-61 [crates/gwiki/src/search/semantic.rs:57-61] | Indexed type `SemanticEmbedding` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:57-61] |
| `VectorSearchBackend` | type | `pub trait VectorSearchBackend {` | `VectorSearchBackend [type]` | `77087767-c390-5ad9-8503-6415578f32aa` | 63-70 [crates/gwiki/src/search/semantic.rs:63-70] | Indexed type `VectorSearchBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:63-70] |
| `search_semantic` | function | `pub fn search_semantic<E, V>(` | `search_semantic [function]` | `a15a29e6-9caf-5477-aca8-2159fa3bcd6c` | 72-163 [crates/gwiki/src/search/semantic.rs:72-163] | Indexed function `search_semantic` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:72-163] |
| `semantic_embedding_query` | function | `fn semantic_embedding_query(config: &EmbeddingConfig, query: &str) -> String {` | `semantic_embedding_query [function]` | `e7e52f31-36dd-5f38-9fb3-4d877021128c` | 165-170 [crates/gwiki/src/search/semantic.rs:165-170] | Indexed function `semantic_embedding_query` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:165-170] |
| `collection_for_scope` | function | `pub fn collection_for_scope(scope: &SearchScope) -> Option<String> {` | `collection_for_scope [function]` | `a80fcd6d-1997-54e8-bdda-b73358d8aae6` | 172-174 [crates/gwiki/src/search/semantic.rs:172-174] | Indexed function `collection_for_scope` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:172-174] |
| `qdrant_collection_scope` | function | `fn qdrant_collection_scope(scope: &SearchScope) -> Option<CollectionScope<'_>> {` | `qdrant_collection_scope [function]` | `9b627ece-45a5-5290-90bb-f7c37255bba5` | 176-182 [crates/gwiki/src/search/semantic.rs:176-182] | Indexed function `qdrant_collection_scope` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:176-182] |
| `payload_filter` | function | `pub fn payload_filter(scope: &SearchScope) -> Value {` | `payload_filter [function]` | `550c2c0b-2c44-513a-9092-6f7362d7091f` | 184-204 [crates/gwiki/src/search/semantic.rs:184-204] | Indexed function `payload_filter` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:184-204] |
| `GobbySemanticBackend` | class | `pub struct GobbySemanticBackend<E, V> {` | `GobbySemanticBackend [class]` | `bd5626de-b898-5a11-b600-fecd2f33ef81` | 206-211 [crates/gwiki/src/search/semantic.rs:206-211] | Indexed class `GobbySemanticBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:206-211] |
| `new` | function | `pub fn new(` | `new [function]` | `576d5cb0-9daa-517e-9bb5-63bef7cb4578` | 214-226 [crates/gwiki/src/search/semantic.rs:214-226] | Indexed function `new` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:214-226] |
| `search_semantic` | function | `fn search_semantic(` | `search_semantic [function]` | `1bf478cc-b39f-5e99-995d-0ca75a1058d4` | 234-245 [crates/gwiki/src/search/semantic.rs:234-245] | Indexed function `search_semantic` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:234-245] |
| `OpenAiEmbeddingBackend` | class | `pub struct OpenAiEmbeddingBackend {` | `OpenAiEmbeddingBackend [class]` | `e1789e22-b2b0-500f-be70-197f0899b7cf` | 250-252 [crates/gwiki/src/search/semantic.rs:250-252] | Indexed class `OpenAiEmbeddingBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:250-252] |
| `OpenAiEmbeddingBackend::default` | method | `fn default() -> Self {` | `OpenAiEmbeddingBackend::default [method]` | `ece5a9f4-aa45-5237-86c8-87565ae31085` | 256-260 [crates/gwiki/src/search/semantic.rs:256-260] | Indexed method `OpenAiEmbeddingBackend::default` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:256-260] |
| `OpenAiEmbeddingBackend::new` | method | `pub fn new() -> Self {` | `OpenAiEmbeddingBackend::new [method]` | `2ab99996-d154-5f0a-905b-fcb5d2f9c62f` | 265-267 [crates/gwiki/src/search/semantic.rs:265-267] | Indexed method `OpenAiEmbeddingBackend::new` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:265-267] |
| `OpenAiEmbeddingBackend::embed_query` | method | `fn embed_query(` | `OpenAiEmbeddingBackend::embed_query [method]` | `9d290002-e63f-51b2-8789-20e00e994aeb` | 272-288 [crates/gwiki/src/search/semantic.rs:272-288] | Indexed method `OpenAiEmbeddingBackend::embed_query` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:272-288] |
| `OpenAiEmbeddingBackend::embed_queries` | method | `fn embed_queries(` | `OpenAiEmbeddingBackend::embed_queries [method]` | `3e5c6516-7d7b-5dfd-9c57-ea322f818b50` | 290-305 [crates/gwiki/src/search/semantic.rs:290-305] | Indexed method `OpenAiEmbeddingBackend::embed_queries` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:290-305] |
| `embed_direct_queries` | function | `fn embed_direct_queries(` | `embed_direct_queries [function]` | `c73a05c9-11de-5f55-bbc8-2d839c17768c` | 309-323 [crates/gwiki/src/search/semantic.rs:309-323] | Indexed function `embed_direct_queries` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:309-323] |
| `OpenAiEmbeddingBackend` | class | `pub struct OpenAiEmbeddingBackend;` | `OpenAiEmbeddingBackend [class]` | `b8dcdbdb-8eb6-5ec9-9ba7-bca1397c09fd` | 327-327 [crates/gwiki/src/search/semantic.rs:327] | Indexed class `OpenAiEmbeddingBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:327] |
| `OpenAiEmbeddingBackend::new` | method | `pub fn new() -> Self {` | `OpenAiEmbeddingBackend::new [method]` | `4ac5fdda-2aa1-5559-8d05-dc3548bc63a1` | 331-333 [crates/gwiki/src/search/semantic.rs:331-333] | Indexed method `OpenAiEmbeddingBackend::new` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:331-333] |
| `OpenAiEmbeddingBackend::embed_query` | method | `fn embed_query(` | `OpenAiEmbeddingBackend::embed_query [method]` | `1e6f24e6-88ef-533b-a262-90c856e9b2ee` | 338-350 [crates/gwiki/src/search/semantic.rs:338-350] | Indexed method `OpenAiEmbeddingBackend::embed_query` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:338-350] |
| `OpenAiEmbeddingBackend::embed_query` | method | `fn embed_query(` | `OpenAiEmbeddingBackend::embed_query [method]` | `6c12087d-e424-5a18-8c0c-2a1475e4e1a9` | 355-364 [crates/gwiki/src/search/semantic.rs:355-364] | Indexed method `OpenAiEmbeddingBackend::embed_query` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:355-364] |
| `embed_daemon_query` | function | `fn embed_daemon_query(context: &AiContext, query: &str) -> Result<Vec<f32>, SearchError> {` | `embed_daemon_query [function]` | `06b9608d-606c-5193-82e7-12263f23d17a` | 368-376 [crates/gwiki/src/search/semantic.rs:368-376] | Indexed function `embed_daemon_query` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:368-376] |
| `GobbyQdrantBackend` | class | `pub struct GobbyQdrantBackend;` | `GobbyQdrantBackend [class]` | `6570a6e4-6307-5af9-822e-3aafe8d5f53b` | 379-379 [crates/gwiki/src/search/semantic.rs:379] | Indexed class `GobbyQdrantBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:379] |
| `GobbyQdrantBackend::search` | method | `fn search(` | `GobbyQdrantBackend::search [method]` | `18be91b5-215c-57a8-a113-35143841770d` | 382-389 [crates/gwiki/src/search/semantic.rs:382-389] | Indexed method `GobbyQdrantBackend::search` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:382-389] |
| `required_service_error` | function | `fn required_service_error(service: &str, detail: &str) -> SearchError {` | `required_service_error [function]` | `f7624e02-1bb3-50f0-af68-0d43e3cfc449` | 392-396 [crates/gwiki/src/search/semantic.rs:392-396] | Indexed function `required_service_error` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:392-396] |
| `payload_matches_scope` | function | `fn payload_matches_scope(payload: &Map<String, Value>, scope: &SearchScope) -> bool {` | `payload_matches_scope [function]` | `aafb800f-8717-594b-8248-becc9d6069af` | 398-411 [crates/gwiki/src/search/semantic.rs:398-411] | Indexed function `payload_matches_scope` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:398-411] |
| `hit_to_result` | function | `fn hit_to_result(hit: SearchHit, scope: &SearchScope) -> Option<WikiSearchResult> {` | `hit_to_result [function]` | `63421599-fd6c-5332-8274-76b5bfbbfeb6` | 413-457 [crates/gwiki/src/search/semantic.rs:413-457] | Indexed function `hit_to_result` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:413-457] |
| `payload_string` | function | `fn payload_string(payload: &Map<String, Value>, key: &str) -> Option<String> {` | `payload_string [function]` | `bca4e613-b421-596c-a803-b72bcfbe2d58` | 459-461 [crates/gwiki/src/search/semantic.rs:459-461] | Indexed function `payload_string` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:459-461] |
| `payload_usize` | function | `fn payload_usize(payload: &Map<String, Value>, key: &str) -> Option<usize> {` | `payload_usize [function]` | `3bfa7530-6717-5406-bda1-f02eb1504763` | 463-468 [crates/gwiki/src/search/semantic.rs:463-468] | Indexed function `payload_usize` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:463-468] |
| `degraded` | function | `fn degraded(service: &str, state: gobby_core::degradation::ServiceState) -> SemanticSearchOutcome {` | `degraded [function]` | `81c916dd-6f47-5fa9-9ee6-d7984c403816` | 470-478 [crates/gwiki/src/search/semantic.rs:470-478] | Indexed function `degraded` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:470-478] |
| `qdrant_degradation` | function | `fn qdrant_degradation(error: anyhow::Error) -> SemanticSearchOutcome {` | `qdrant_degradation [function]` | `c3aadf88-0434-5ffe-91d1-6ec63067862f` | 480-509 [crates/gwiki/src/search/semantic.rs:480-509] | Indexed function `qdrant_degradation` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:480-509] |
| `UnavailableSemanticBackend` | class | `pub struct UnavailableSemanticBackend;` | `UnavailableSemanticBackend [class]` | `ae502464-896d-59c6-ba4b-899972bb3249` | 512-512 [crates/gwiki/src/search/semantic.rs:512] | Indexed class `UnavailableSemanticBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:512] |
| `UnavailableSemanticBackend::search_semantic` | method | `fn search_semantic(` | `UnavailableSemanticBackend::search_semantic [method]` | `d458326e-45fb-5c26-a721-378426725213` | 516-524 [crates/gwiki/src/search/semantic.rs:516-524] | Indexed method `UnavailableSemanticBackend::search_semantic` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:516-524] |
| `FixedEmbedder` | class | `struct FixedEmbedder {` | `FixedEmbedder [class]` | `229359d9-b506-5b8f-8eab-e4689ccede18` | 528-531 [crates/gwiki/src/search/semantic.rs:528-531] | Indexed class `FixedEmbedder` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:528-531] |
| `FixedEmbedder::new` | method | `fn new(vector: Vec<f32>) -> Self {` | `FixedEmbedder::new [method]` | `e6979e46-22b9-56c8-bbaf-c1d887c0163c` | 535-540 [crates/gwiki/src/search/semantic.rs:535-540] | Indexed method `FixedEmbedder::new` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:535-540] |
| `FixedEmbedder::embed_query` | method | `fn embed_query(` | `FixedEmbedder::embed_query [method]` | `6fd06202-1b73-5177-a670-361ded1747ce` | 545-552 [crates/gwiki/src/search/semantic.rs:545-552] | Indexed method `FixedEmbedder::embed_query` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:545-552] |
| `RecordingVectorBackend` | class | `struct RecordingVectorBackend {` | `RecordingVectorBackend [class]` | `563ea9bc-0313-5891-8548-976d54b55d6e` | 556-560 [crates/gwiki/src/search/semantic.rs:556-560] | Indexed class `RecordingVectorBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:556-560] |
| `RecordingVectorBackend::new` | method | `fn new(hits: Vec<SearchHit>) -> Self {` | `RecordingVectorBackend::new [method]` | `3a4d69a7-62d6-5a13-b911-68f919b80ac1` | 564-570 [crates/gwiki/src/search/semantic.rs:564-570] | Indexed method `RecordingVectorBackend::new` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:564-570] |
| `RecordingVectorBackend::search` | method | `fn search(` | `RecordingVectorBackend::search [method]` | `88d6660e-06a2-51a6-b984-6f95637a1eca` | 575-584 [crates/gwiki/src/search/semantic.rs:575-584] | Indexed method `RecordingVectorBackend::search` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:575-584] |
| `FailingEmbedder` | class | `struct FailingEmbedder;` | `FailingEmbedder [class]` | `cd81caa4-39cf-5b20-83e2-4004551759fa` | 588-588 [crates/gwiki/src/search/semantic.rs:588] | Indexed class `FailingEmbedder` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:588] |
| `FailingEmbedder::embed_query` | method | `fn embed_query(` | `FailingEmbedder::embed_query [method]` | `381d678b-9362-5b15-8e55-4b5c283bcb02` | 592-598 [crates/gwiki/src/search/semantic.rs:592-598] | Indexed method `FailingEmbedder::embed_query` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:592-598] |
| `FailingVectorBackend` | class | `struct FailingVectorBackend;` | `FailingVectorBackend [class]` | `dd201376-fadd-5fb9-94d2-b346649d3920` | 602-602 [crates/gwiki/src/search/semantic.rs:602] | Indexed class `FailingVectorBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:602] |
| `FailingVectorBackend::search` | method | `fn search(` | `FailingVectorBackend::search [method]` | `06c4c211-94cd-507d-bbe5-2988a585c0a6` | 606-613 [crates/gwiki/src/search/semantic.rs:606-613] | Indexed method `FailingVectorBackend::search` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:606-613] |
| `QdrantStatusVectorBackend` | class | `struct QdrantStatusVectorBackend {` | `QdrantStatusVectorBackend [class]` | `9ae3231d-caad-585e-b9dd-7c91e4b62516` | 617-619 [crates/gwiki/src/search/semantic.rs:617-619] | Indexed class `QdrantStatusVectorBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:617-619] |
| `QdrantStatusVectorBackend::search` | method | `fn search(` | `QdrantStatusVectorBackend::search [method]` | `955afd6f-48c6-5a3c-8f9c-8e2985d66b7b` | 623-637 [crates/gwiki/src/search/semantic.rs:623-637] | Indexed method `QdrantStatusVectorBackend::search` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:623-637] |
