---
title: crates/gwiki/src/vector.rs
type: code_file
provenance:
- file: crates/gwiki/src/vector.rs
  ranges:
  - 17-26
  - 29-33
  - 36-40
  - 43-48
  - 51-58
  - 64-66
  - 69-73
  - 75-77
  - 79-99
  - 101-193
  - 195-197
  - 199-205
  - 207-245
  - 247-249
  - 251-253
  - 255-257
  - 260-262
  - 266-282
  - 284-298
  - 301-323
  - 325-330
  - 332-340
  - 342-345
  - 348-353
  - 357-370
  - 373-375
  - 378-380
  - 384-392
  - 394-397
  - 399-415
  - 425-452
  - 455-522
  - 525-566
  - 570-604
  - 607-617
  - 619-622
  - 625-630
  - 632-634
  - 637-640
  - 643-647
  - 651-655
  - 657-660
  - 663-671
  - 673-680
  - 682-692
  - 695-704
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/vector.rs:17-26](crates/gwiki/src/vector.rs#L17-L26), [crates/gwiki/src/vector.rs:29-33](crates/gwiki/src/vector.rs#L29-L33), [crates/gwiki/src/vector.rs:36-40](crates/gwiki/src/vector.rs#L36-L40), [crates/gwiki/src/vector.rs:43-48](crates/gwiki/src/vector.rs#L43-L48), [crates/gwiki/src/vector.rs:51-58](crates/gwiki/src/vector.rs#L51-L58), [crates/gwiki/src/vector.rs:64-66](crates/gwiki/src/vector.rs#L64-L66), [crates/gwiki/src/vector.rs:69-73](crates/gwiki/src/vector.rs#L69-L73), [crates/gwiki/src/vector.rs:75-77](crates/gwiki/src/vector.rs#L75-L77), [crates/gwiki/src/vector.rs:79-99](crates/gwiki/src/vector.rs#L79-L99), [crates/gwiki/src/vector.rs:101-193](crates/gwiki/src/vector.rs#L101-L193), [crates/gwiki/src/vector.rs:195-197](crates/gwiki/src/vector.rs#L195-L197), [crates/gwiki/src/vector.rs:199-205](crates/gwiki/src/vector.rs#L199-L205), [crates/gwiki/src/vector.rs:207-245](crates/gwiki/src/vector.rs#L207-L245), [crates/gwiki/src/vector.rs:247-249](crates/gwiki/src/vector.rs#L247-L249), [crates/gwiki/src/vector.rs:251-253](crates/gwiki/src/vector.rs#L251-L253), [crates/gwiki/src/vector.rs:255-257](crates/gwiki/src/vector.rs#L255-L257), [crates/gwiki/src/vector.rs:260-262](crates/gwiki/src/vector.rs#L260-L262), [crates/gwiki/src/vector.rs:266-282](crates/gwiki/src/vector.rs#L266-L282), [crates/gwiki/src/vector.rs:284-298](crates/gwiki/src/vector.rs#L284-L298), [crates/gwiki/src/vector.rs:301-323](crates/gwiki/src/vector.rs#L301-L323), [crates/gwiki/src/vector.rs:325-330](crates/gwiki/src/vector.rs#L325-L330), [crates/gwiki/src/vector.rs:332-340](crates/gwiki/src/vector.rs#L332-L340), [crates/gwiki/src/vector.rs:342-345](crates/gwiki/src/vector.rs#L342-L345), [crates/gwiki/src/vector.rs:348-353](crates/gwiki/src/vector.rs#L348-L353), [crates/gwiki/src/vector.rs:357-370](crates/gwiki/src/vector.rs#L357-L370), [crates/gwiki/src/vector.rs:373-375](crates/gwiki/src/vector.rs#L373-L375), [crates/gwiki/src/vector.rs:378-380](crates/gwiki/src/vector.rs#L378-L380), [crates/gwiki/src/vector.rs:384-392](crates/gwiki/src/vector.rs#L384-L392), [crates/gwiki/src/vector.rs:394-397](crates/gwiki/src/vector.rs#L394-L397), [crates/gwiki/src/vector.rs:399-415](crates/gwiki/src/vector.rs#L399-L415), [crates/gwiki/src/vector.rs:425-452](crates/gwiki/src/vector.rs#L425-L452), [crates/gwiki/src/vector.rs:455-522](crates/gwiki/src/vector.rs#L455-L522), [crates/gwiki/src/vector.rs:525-566](crates/gwiki/src/vector.rs#L525-L566), [crates/gwiki/src/vector.rs:570-604](crates/gwiki/src/vector.rs#L570-L604), [crates/gwiki/src/vector.rs:607-617](crates/gwiki/src/vector.rs#L607-L617), [crates/gwiki/src/vector.rs:619-622](crates/gwiki/src/vector.rs#L619-L622), [crates/gwiki/src/vector.rs:625-630](crates/gwiki/src/vector.rs#L625-L630), [crates/gwiki/src/vector.rs:632-634](crates/gwiki/src/vector.rs#L632-L634), [crates/gwiki/src/vector.rs:637-640](crates/gwiki/src/vector.rs#L637-L640), [crates/gwiki/src/vector.rs:643-647](crates/gwiki/src/vector.rs#L643-L647), [crates/gwiki/src/vector.rs:651-655](crates/gwiki/src/vector.rs#L651-L655), [crates/gwiki/src/vector.rs:657-660](crates/gwiki/src/vector.rs#L657-L660), [crates/gwiki/src/vector.rs:663-671](crates/gwiki/src/vector.rs#L663-L671), [crates/gwiki/src/vector.rs:673-680](crates/gwiki/src/vector.rs#L673-L680), [crates/gwiki/src/vector.rs:682-692](crates/gwiki/src/vector.rs#L682-L692), [crates/gwiki/src/vector.rs:695-704](crates/gwiki/src/vector.rs#L695-L704)

</details>

# crates/gwiki/src/vector.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/vector.rs` defines the wiki vector indexing pipeline: it models extracted wiki chunks, embedded vector points, sync results, and a unified error type, then ties together three abstractions for chunk sourcing, text embedding, and vector storage. `sync_scope_vectors` is the central workflow that takes chunks from a `WikiVectorChunkSource`, embeds their text with a `WikiVectorEmbedder`, converts them into point payloads and IDs, upserts them through a `WikiVectorStore`, and removes stale paths for the active `SearchScope`. The concrete implementations adapt Postgres as a chunk source, OpenAI-backed embeddings as the embedder, and Qdrant as the vector store, while the helper functions handle collection naming, delete filters, payload construction, point ID generation, snippet extraction, and row parsing. The tests use mock and recording implementations to verify batching, collection/filter behavior, stale deletion, and offset parsing.
[crates/gwiki/src/vector.rs:17-26]
[crates/gwiki/src/vector.rs:29-33]
[crates/gwiki/src/vector.rs:36-40]
[crates/gwiki/src/vector.rs:43-48]
[crates/gwiki/src/vector.rs:51-58]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `WikiVectorChunk` | class | `pub(crate) struct WikiVectorChunk {` | `WikiVectorChunk [class]` | `9cdd8803-e898-5b11-b5c0-acc8c1551c0a` | 17-26 [crates/gwiki/src/vector.rs:17-26] | Indexed class `WikiVectorChunk` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:17-26] |
| `WikiVectorPoint` | class | `pub(crate) struct WikiVectorPoint {` | `WikiVectorPoint [class]` | `b6a5a546-3f8d-506e-bce5-64231cf5916c` | 29-33 [crates/gwiki/src/vector.rs:29-33] | Indexed class `WikiVectorPoint` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:29-33] |
| `WikiVectorSyncOutcome` | class | `pub(crate) struct WikiVectorSyncOutcome {` | `WikiVectorSyncOutcome [class]` | `39f3a50d-15f4-58ed-8fca-6e098e0fd7da` | 36-40 [crates/gwiki/src/vector.rs:36-40] | Indexed class `WikiVectorSyncOutcome` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:36-40] |
| `WikiVectorError` | type | `pub(crate) enum WikiVectorError {` | `WikiVectorError [type]` | `e355b097-4535-5a3f-abc3-b3aab164bf74` | 43-48 [crates/gwiki/src/vector.rs:43-48] | Indexed type `WikiVectorError` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:43-48] |
| `WikiVectorError::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `WikiVectorError::fmt [method]` | `b534d755-64da-558c-8db5-17aa5884ce3a` | 51-58 [crates/gwiki/src/vector.rs:51-58] | Indexed method `WikiVectorError::fmt` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:51-58] |
| `WikiVectorError::from` | method | `fn from(error: postgres::Error) -> Self {` | `WikiVectorError::from [method]` | `2d9f8282-93da-5a3e-875c-0068eddccbe2` | 64-66 [crates/gwiki/src/vector.rs:64-66] | Indexed method `WikiVectorError::from` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:64-66] |
| `WikiVectorChunkSource` | type | `pub(crate) trait WikiVectorChunkSource {` | `WikiVectorChunkSource [type]` | `93c74053-9428-58ca-b5a5-4f7458c8ec24` | 69-73 [crates/gwiki/src/vector.rs:69-73] | Indexed type `WikiVectorChunkSource` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:69-73] |
| `WikiVectorEmbedder` | type | `pub(crate) trait WikiVectorEmbedder {` | `WikiVectorEmbedder [type]` | `2648f184-aacd-5c51-9737-eef18da4f969` | 75-77 [crates/gwiki/src/vector.rs:75-77] | Indexed type `WikiVectorEmbedder` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:75-77] |
| `WikiVectorStore` | type | `pub(crate) trait WikiVectorStore {` | `WikiVectorStore [type]` | `ac32127e-ace4-5e6f-a564-b177750bd1be` | 79-99 [crates/gwiki/src/vector.rs:79-99] | Indexed type `WikiVectorStore` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:79-99] |
| `WikiVectorStore.resolve_collection` | method | `fn resolve_collection(&mut self, scope: &SearchScope) -> Result<String, WikiVectorError> {` | `WikiVectorStore.resolve_collection [method]` | `f914fc26-57ae-52f1-a43c-d0fdc1a323ec` | 80-84 [crates/gwiki/src/vector.rs:80-84] | Indexed method `WikiVectorStore.resolve_collection` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:80-84] |
| `sync_scope_vectors` | function | `pub(crate) fn sync_scope_vectors<S, E, V>(` | `sync_scope_vectors [function]` | `e3ee6d1f-e4a1-501a-b2f2-2a72e0deaaa7` | 101-193 [crates/gwiki/src/vector.rs:101-193] | Indexed function `sync_scope_vectors` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:101-193] |
| `collection_for_scope` | function | `pub(crate) fn collection_for_scope(scope: &SearchScope) -> Option<String> {` | `collection_for_scope [function]` | `a0320acc-5c46-5374-ae64-bc7c02bd537f` | 195-197 [crates/gwiki/src/vector.rs:195-197] | Indexed function `collection_for_scope` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:195-197] |
| `delete_filter_for_path` | function | `pub(crate) fn delete_filter_for_path(scope: &SearchScope, path: &str) -> Value {` | `delete_filter_for_path [function]` | `bd6661a4-4777-5104-ad4b-d4298689bd37` | 199-205 [crates/gwiki/src/vector.rs:199-205] | Indexed function `delete_filter_for_path` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:199-205] |
| `payload_for_chunk` | function | `fn payload_for_chunk(scope: &SearchScope, chunk: &WikiVectorChunk) -> Map<String, Value> {` | `payload_for_chunk [function]` | `f59ab735-6343-5dcc-84de-e73e2db297a2` | 207-245 [crates/gwiki/src/vector.rs:207-245] | Indexed function `payload_for_chunk` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:207-245] |
| `point_id_for_chunk` | function | `fn point_id_for_chunk(chunk: &WikiVectorChunk) -> String {` | `point_id_for_chunk [function]` | `6f5dc16c-c1d7-5337-ba63-d0f459f08d4b` | 247-249 [crates/gwiki/src/vector.rs:247-249] | Indexed function `point_id_for_chunk` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:247-249] |
| `snippet` | function | `fn snippet(content: &str) -> String {` | `snippet [function]` | `ae5e65cf-3e18-573d-8194-e636842939e3` | 251-253 [crates/gwiki/src/vector.rs:251-253] | Indexed function `snippet` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:251-253] |
| `PostgresWikiVectorChunkSource` | class | `pub(crate) struct PostgresWikiVectorChunkSource<'a> {` | `PostgresWikiVectorChunkSource [class]` | `3243b5e9-d507-5383-8b6c-809fe330e6fd` | 255-257 [crates/gwiki/src/vector.rs:255-257] | Indexed class `PostgresWikiVectorChunkSource` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:255-257] |
| `new` | function | `pub(crate) fn new(conn: &'a mut postgres::Client) -> Self {` | `new [function]` | `97d3d134-3c9b-5144-b358-904050981848` | 260-262 [crates/gwiki/src/vector.rs:260-262] | Indexed function `new` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:260-262] |
| `chunks` | function | `fn chunks(&mut self, scope: &SearchScope) -> Result<Vec<WikiVectorChunk>, WikiVectorError> {` | `chunks [function]` | `5a418124-5a05-5b70-b1ed-394e1c9128d1` | 266-282 [crates/gwiki/src/vector.rs:266-282] | Indexed function `chunks` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:266-282] |
| `stale_paths` | function | `fn stale_paths(&mut self, scope: &SearchScope) -> Result<Vec<String>, WikiVectorError> {` | `stale_paths [function]` | `910cae98-a441-54fc-a123-b0af7687e970` | 284-298 [crates/gwiki/src/vector.rs:284-298] | Indexed function `stale_paths` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:284-298] |
| `row_to_vector_chunk` | function | `fn row_to_vector_chunk(row: postgres::Row) -> Result<WikiVectorChunk, WikiVectorError> {` | `row_to_vector_chunk [function]` | `5251140b-5d8e-5a49-b97f-aa8377a0e212` | 301-323 [crates/gwiki/src/vector.rs:301-323] | Indexed function `row_to_vector_chunk` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:301-323] |
| `required_row_usize` | function | `fn required_row_usize(row: &postgres::Row, column: &'static str) -> Result<usize, WikiVectorError> {` | `required_row_usize [function]` | `78f467cb-84c0-503d-aa4f-4b8fe08a3cac` | 325-330 [crates/gwiki/src/vector.rs:325-330] | Indexed function `required_row_usize` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:325-330] |
| `parse_required_usize` | function | `fn parse_required_usize(` | `parse_required_usize [function]` | `c3aa0e0d-b7e0-5f89-85f8-0d122bf541b3` | 332-340 [crates/gwiki/src/vector.rs:332-340] | Indexed function `parse_required_usize` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:332-340] |
| `GwikiEmbeddingBackend` | class | `pub(crate) struct GwikiEmbeddingBackend {` | `GwikiEmbeddingBackend [class]` | `d12dee8c-13df-59b1-8524-9354ef5aa456` | 342-345 [crates/gwiki/src/vector.rs:342-345] | Indexed class `GwikiEmbeddingBackend` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:342-345] |
| `GwikiEmbeddingBackend::new` | method | `pub(crate) fn new(embedding: SemanticEmbedding) -> Self {` | `GwikiEmbeddingBackend::new [method]` | `a2d29562-d4b9-5fd3-a1e7-927adc6158b3` | 348-353 [crates/gwiki/src/vector.rs:348-353] | Indexed method `GwikiEmbeddingBackend::new` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:348-353] |
| `GwikiEmbeddingBackend::embed_texts` | method | `fn embed_texts(&mut self, texts: &[String]) -> Result<Vec<Vec<f32>>, WikiVectorError> {` | `GwikiEmbeddingBackend::embed_texts [method]` | `6fe6977c-810c-5d6c-a013-1fb67bb91a69` | 357-370 [crates/gwiki/src/vector.rs:357-370] | Indexed method `GwikiEmbeddingBackend::embed_texts` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:357-370] |
| `GwikiQdrantVectorStore` | class | `pub(crate) struct GwikiQdrantVectorStore {` | `GwikiQdrantVectorStore [class]` | `5138dc99-6a97-5a9c-8958-dd923bcc2765` | 373-375 [crates/gwiki/src/vector.rs:373-375] | Indexed class `GwikiQdrantVectorStore` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:373-375] |
| `GwikiQdrantVectorStore::new` | method | `pub(crate) fn new(config: QdrantConfig) -> Self {` | `GwikiQdrantVectorStore::new [method]` | `7047955d-6ddf-5b82-a64a-9dc54f0c3f09` | 378-380 [crates/gwiki/src/vector.rs:378-380] | Indexed method `GwikiQdrantVectorStore::new` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:378-380] |
| `GwikiQdrantVectorStore::ensure_collection` | method | `fn ensure_collection(` | `GwikiQdrantVectorStore::ensure_collection [method]` | `843e2a80-167a-5b29-822c-ef68cfb4dd68` | 384-392 [crates/gwiki/src/vector.rs:384-392] | Indexed method `GwikiQdrantVectorStore::ensure_collection` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:384-392] |
| `GwikiQdrantVectorStore::delete_points` | method | `fn delete_points(&mut self, collection: &str, filter: Value) -> Result<(), WikiVectorError> {` | `GwikiQdrantVectorStore::delete_points [method]` | `8911b9db-605e-5f14-a10f-b2e2ee667ef3` | 394-397 [crates/gwiki/src/vector.rs:394-397] | Indexed method `GwikiQdrantVectorStore::delete_points` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:394-397] |
| `GwikiQdrantVectorStore::upsert_points` | method | `fn upsert_points(` | `GwikiQdrantVectorStore::upsert_points [method]` | `ab966236-2ae3-56cb-951b-64ec2f51f940` | 399-415 [crates/gwiki/src/vector.rs:399-415] | Indexed method `GwikiQdrantVectorStore::upsert_points` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:399-415] |
| `vector_collection_and_path_filter_match_scope_contract` | function | `fn vector_collection_and_path_filter_match_scope_contract() {` | `vector_collection_and_path_filter_match_scope_contract [function]` | `7c64ff70-df9f-5766-af18-1cb52a41525d` | 425-452 [crates/gwiki/src/vector.rs:425-452] | Indexed function `vector_collection_and_path_filter_match_scope_contract` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:425-452] |
| `vector_sync_embeds_upserts_and_deletes_stale_vectors` | function | `fn vector_sync_embeds_upserts_and_deletes_stale_vectors() {` | `vector_sync_embeds_upserts_and_deletes_stale_vectors [function]` | `cf13da1f-4db4-5087-9163-195445aabcf0` | 455-522 [crates/gwiki/src/vector.rs:455-522] | Indexed function `vector_sync_embeds_upserts_and_deletes_stale_vectors` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:455-522] |
| `vector_sync_batches_embedding_and_upserts` | function | `fn vector_sync_batches_embedding_and_upserts() {` | `vector_sync_batches_embedding_and_upserts [function]` | `ec4fdd6a-0eb8-5d8a-a015-e6633a97f206` | 525-566 [crates/gwiki/src/vector.rs:525-566] | Indexed function `vector_sync_batches_embedding_and_upserts` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:525-566] |
| `direct_embedding_backend_batches_texts` | function | `fn direct_embedding_backend_batches_texts() {` | `direct_embedding_backend_batches_texts [function]` | `b761d88e-52b4-549e-80cb-6ceb8cb08bce` | 570-604 [crates/gwiki/src/vector.rs:570-604] | Indexed function `direct_embedding_backend_batches_texts` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:570-604] |
| `vector_required_offset_parser_rejects_missing_and_malformed_values` | function | `fn vector_required_offset_parser_rejects_missing_and_malformed_values() {` | `vector_required_offset_parser_rejects_missing_and_malformed_values [function]` | `c294d46a-84c1-5b70-a520-c5f4304a057e` | 607-617 [crates/gwiki/src/vector.rs:607-617] | Indexed function `vector_required_offset_parser_rejects_missing_and_malformed_values` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:607-617] |
| `MockChunkSource` | class | `struct MockChunkSource {` | `MockChunkSource [class]` | `55dbb8ab-edcc-59d3-98fe-66eb2474d453` | 619-622 [crates/gwiki/src/vector.rs:619-622] | Indexed class `MockChunkSource` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:619-622] |
| `MockChunkSource::chunks` | method | `fn chunks(` | `MockChunkSource::chunks [method]` | `df30372e-a182-5d77-8268-572a1dbfd8ad` | 625-630 [crates/gwiki/src/vector.rs:625-630] | Indexed method `MockChunkSource::chunks` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:625-630] |
| `MockChunkSource::stale_paths` | method | `fn stale_paths(&mut self, _scope: &SearchScope) -> Result<Vec<String>, WikiVectorError> {` | `MockChunkSource::stale_paths [method]` | `44431d53-440b-5e3c-8833-9184a7660977` | 632-634 [crates/gwiki/src/vector.rs:632-634] | Indexed method `MockChunkSource::stale_paths` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:632-634] |
| `MockEmbedder` | class | `struct MockEmbedder {` | `MockEmbedder [class]` | `0f6472da-7ae5-5254-8811-cf0d486b50c0` | 637-640 [crates/gwiki/src/vector.rs:637-640] | Indexed class `MockEmbedder` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:637-640] |
| `MockEmbedder::embed_texts` | method | `fn embed_texts(&mut self, texts: &[String]) -> Result<Vec<Vec<f32>>, WikiVectorError> {` | `MockEmbedder::embed_texts [method]` | `55b7d681-e1f6-5fb2-be30-31ba1bc3e5af` | 643-647 [crates/gwiki/src/vector.rs:643-647] | Indexed method `MockEmbedder::embed_texts` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:643-647] |
| `RecordingVectorStore` | class | `struct RecordingVectorStore {` | `RecordingVectorStore [class]` | `71837415-89dd-51b4-8604-80e20aad83d2` | 651-655 [crates/gwiki/src/vector.rs:651-655] | Indexed class `RecordingVectorStore` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:651-655] |
| `RecordedUpsert` | class | `struct RecordedUpsert {` | `RecordedUpsert [class]` | `87e6a16d-6b45-5f15-884f-e511d08f6dfa` | 657-660 [crates/gwiki/src/vector.rs:657-660] | Indexed class `RecordedUpsert` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:657-660] |
| `RecordingVectorStore::ensure_collection` | method | `fn ensure_collection(` | `RecordingVectorStore::ensure_collection [method]` | `84303008-e522-575d-b2e3-a3cb925be502` | 663-671 [crates/gwiki/src/vector.rs:663-671] | Indexed method `RecordingVectorStore::ensure_collection` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:663-671] |
| `RecordingVectorStore::delete_points` | method | `fn delete_points(` | `RecordingVectorStore::delete_points [method]` | `3c44c2bb-954d-5612-8787-8bb97bffecbd` | 673-680 [crates/gwiki/src/vector.rs:673-680] | Indexed method `RecordingVectorStore::delete_points` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:673-680] |
| `RecordingVectorStore::upsert_points` | method | `fn upsert_points(` | `RecordingVectorStore::upsert_points [method]` | `a5dd24c3-e627-5214-8c65-f8326959bd94` | 682-692 [crates/gwiki/src/vector.rs:682-692] | Indexed method `RecordingVectorStore::upsert_points` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:682-692] |
| `filter_value` | function | `fn filter_value(filter: &Value, key: &str) -> Option<String> {` | `filter_value [function]` | `c8e9e71d-978e-5281-91dd-190c26c6c90a` | 695-704 [crates/gwiki/src/vector.rs:695-704] | Indexed function `filter_value` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:695-704] |
