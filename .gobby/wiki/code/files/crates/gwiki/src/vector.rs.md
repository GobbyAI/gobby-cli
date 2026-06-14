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
  - 50-59
  - '61'
  - 63-67
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
  - 347-354
  - 356-371
  - 373-375
  - 377-381
  - 383-416
  - 425-452
  - 455-522
  - 525-566
  - 570-604
  - 607-617
  - 619-622
  - 624-635
  - 637-640
  - 642-648
  - 651-655
  - 657-660
  - 662-693
  - 695-704
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/vector.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the wiki vector synchronization layer for `gwiki`: it defines the chunk and point records, a sync result type, and a unified error type, then provides traits and concrete adapters for reading wiki chunks from Postgres, generating embeddings, and writing/deleting vectors in Qdrant. The main `sync_scope_vectors` flow resolves the collection for a `SearchScope`, loads current chunks and stale paths, batches chunk content through the embedder, validates embedding shape, builds payloads and deterministic point IDs, upserts the vectors, and removes vectors for deleted paths. The file also includes helpers for scope-based collection/filter mapping, payload construction, UUID/snippet generation, row parsing, and test doubles plus tests that verify collection selection, batching, embedding, upserts, deletions, and error handling.
[crates/gwiki/src/vector.rs:17-26]
[crates/gwiki/src/vector.rs:29-33]
[crates/gwiki/src/vector.rs:36-40]
[crates/gwiki/src/vector.rs:43-48]
[crates/gwiki/src/vector.rs:50-59]

## API Symbols

- `WikiVectorChunk` (class) component `WikiVectorChunk [class]` (`9cdd8803-e898-5b11-b5c0-acc8c1551c0a`) lines 17-26 [crates/gwiki/src/vector.rs:17-26]
  - Signature: `pub(crate) struct WikiVectorChunk {`
  - Purpose: 'WikiVectorChunk' is an internal data record representing a contiguous chunk of wiki text, identified by 'id' and 'path', with optional 'title' and 'heading', positional metadata ('chunk_index', 'byte_start', 'byte_end'), and the chunk’s 'content' payload. [crates/gwiki/src/vector.rs:17-26]
- `WikiVectorPoint` (class) component `WikiVectorPoint [class]` (`b6a5a546-3f8d-506e-bce5-64231cf5916c`) lines 29-33 [crates/gwiki/src/vector.rs:29-33]
  - Signature: `pub(crate) struct WikiVectorPoint {`
  - Purpose: 'WikiVectorPoint' is a crate-visible struct representing a vector index record with a string 'id', an embedding stored as 'Vec<f32>', and arbitrary JSON-like metadata in 'payload' ('Map<String, Value>'). [crates/gwiki/src/vector.rs:29-33]
- `WikiVectorSyncOutcome` (class) component `WikiVectorSyncOutcome [class]` (`39f3a50d-15f4-58ed-8fca-6e098e0fd7da`) lines 36-40 [crates/gwiki/src/vector.rs:36-40]
  - Signature: `pub(crate) struct WikiVectorSyncOutcome {`
  - Purpose: 'WikiVectorSyncOutcome' is an internal Rust struct that records the results of a wiki vector synchronization run by counting processed chunks, upserted vectors, and stale paths deleted. [crates/gwiki/src/vector.rs:36-40]
- `WikiVectorError` (type) component `WikiVectorError [type]` (`e355b097-4535-5a3f-abc3-b3aab164bf74`) lines 43-48 [crates/gwiki/src/vector.rs:43-48]
  - Signature: `pub(crate) enum WikiVectorError {`
  - Purpose: Indexed type `WikiVectorError` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:43-48]
- `WikiVectorError` (class) component `WikiVectorError [class]` (`55c05160-bd3c-503f-b5e4-c70ff00f988d`) lines 50-59 [crates/gwiki/src/vector.rs:50-59]
  - Signature: `impl fmt::Display for WikiVectorError {`
  - Purpose: 'WikiVectorError' implements 'fmt::Display' by rendering each variant as a distinct, prefixed human-readable error message for store, embedding, Qdrant, or invalid-data failures. [crates/gwiki/src/vector.rs:50-59]
- `WikiVectorError.fmt` (method) component `WikiVectorError.fmt [method]` (`b534d755-64da-558c-8db5-17aa5884ce3a`) lines 51-58 [crates/gwiki/src/vector.rs:51-58]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Implements 'Display' by pattern-matching the error variant and writing a variant-specific 'wiki vector ... error: {message}' string to the formatter. [crates/gwiki/src/vector.rs:51-58]
- `WikiVectorError` (class) component `WikiVectorError [class]` (`3862bd4e-a1d8-51c6-8549-b4142ceaf0cf`) lines 61-61 [crates/gwiki/src/vector.rs:61]
  - Signature: `impl std::error::Error for WikiVectorError {}`
  - Purpose: 'WikiVectorError' is a Rust error type that implements the 'std::error::Error' trait, allowing it to participate in standard error handling and propagation. [crates/gwiki/src/vector.rs:61]
- `WikiVectorError` (class) component `WikiVectorError [class]` (`a9105d24-683c-55b4-a9c1-d0c51e865ceb`) lines 63-67 [crates/gwiki/src/vector.rs:63-67]
  - Signature: `impl From<postgres::Error> for WikiVectorError {`
  - Purpose: 'WikiVectorError' implements 'From<postgres::Error>' by converting any PostgreSQL error into 'WikiVectorError::Store' containing the error’s string representation. [crates/gwiki/src/vector.rs:63-67]
- `WikiVectorError.from` (method) component `WikiVectorError.from [method]` (`2d9f8282-93da-5a3e-875c-0068eddccbe2`) lines 64-66 [crates/gwiki/src/vector.rs:64-66]
  - Signature: `fn from(error: postgres::Error) -> Self {`
  - Purpose: Converts a 'postgres::Error' into this type by wrapping the error’s string representation in 'Self::Store'. [crates/gwiki/src/vector.rs:64-66]
- `WikiVectorChunkSource` (type) component `WikiVectorChunkSource [type]` (`93c74053-9428-58ca-b5a5-4f7458c8ec24`) lines 69-73 [crates/gwiki/src/vector.rs:69-73]
  - Signature: `pub(crate) trait WikiVectorChunkSource {`
  - Purpose: Indexed type `WikiVectorChunkSource` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:69-73]
- `WikiVectorEmbedder` (type) component `WikiVectorEmbedder [type]` (`2648f184-aacd-5c51-9737-eef18da4f969`) lines 75-77 [crates/gwiki/src/vector.rs:75-77]
  - Signature: `pub(crate) trait WikiVectorEmbedder {`
  - Purpose: Indexed type `WikiVectorEmbedder` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:75-77]
- `WikiVectorStore` (type) component `WikiVectorStore [type]` (`ac32127e-ace4-5e6f-a564-b177750bd1be`) lines 79-99 [crates/gwiki/src/vector.rs:79-99]
  - Signature: `pub(crate) trait WikiVectorStore {`
  - Purpose: Indexed type `WikiVectorStore` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:79-99]
- `WikiVectorStore.resolve_collection` (method) component `WikiVectorStore.resolve_collection [method]` (`f914fc26-57ae-52f1-a43c-d0fdc1a323ec`) lines 80-84 [crates/gwiki/src/vector.rs:80-84]
  - Signature: `fn resolve_collection(&mut self, scope: &SearchScope) -> Result<String, WikiVectorError> {`
  - Purpose: Returns the vector collection name for the given 'SearchScope' via 'collection_for_scope', or yields 'WikiVectorError::InvalidData("global scope has no vector collection")' if no collection exists. [crates/gwiki/src/vector.rs:80-84]
- `sync_scope_vectors` (function) component `sync_scope_vectors [function]` (`e3ee6d1f-e4a1-501a-b2f2-2a72e0deaaa7`) lines 101-193 [crates/gwiki/src/vector.rs:101-193]
  - Signature: `pub(crate) fn sync_scope_vectors<S, E, V>(`
  - Purpose: Synchronizes wiki vectors for a search scope by resolving the target collection, deleting points for stale paths, batching source chunks through the embedder, and validating embedding count and vector dimensionality before writing the resulting points to the store. [crates/gwiki/src/vector.rs:101-193]
- `collection_for_scope` (function) component `collection_for_scope [function]` (`a0320acc-5c46-5374-ae64-bc7c02bd537f`) lines 195-197 [crates/gwiki/src/vector.rs:195-197]
  - Signature: `pub(crate) fn collection_for_scope(scope: &SearchScope) -> Option<String> {`
  - Purpose: Delegates to 'crate::search::semantic::collection_for_scope' to map a 'SearchScope' to an optional collection name ('Option<String>'). [crates/gwiki/src/vector.rs:195-197]
- `delete_filter_for_path` (function) component `delete_filter_for_path [function]` (`bd6661a4-4777-5104-ad4b-d4298689bd37`) lines 199-205 [crates/gwiki/src/vector.rs:199-205]
  - Signature: `pub(crate) fn delete_filter_for_path(scope: &SearchScope, path: &str) -> Value {`
  - Purpose: Builds a semantic payload filter for the given 'SearchScope' and, if the filter has a mutable 'must' array, appends a 'path' equality match for the provided 'path' before returning the JSON 'Value'. [crates/gwiki/src/vector.rs:199-205]
- `payload_for_chunk` (function) component `payload_for_chunk [function]` (`f59ab735-6343-5dcc-84de-e73e2db297a2`) lines 207-245 [crates/gwiki/src/vector.rs:207-245]
  - Signature: `fn payload_for_chunk(scope: &SearchScope, chunk: &WikiVectorChunk) -> Map<String, Value> {`
  - Purpose: Builds a JSON-like payload map for a wiki vector chunk, including fixed metadata ('namespace', 'chunk_id', scope fields), scope-specific identifiers, path/title/heading when present, chunk offsets, full content, and a derived content snippet. [crates/gwiki/src/vector.rs:207-245]
- `point_id_for_chunk` (function) component `point_id_for_chunk [function]` (`6f5dc16c-c1d7-5337-ba63-d0f459f08d4b`) lines 247-249 [crates/gwiki/src/vector.rs:247-249]
  - Signature: `fn point_id_for_chunk(chunk: &WikiVectorChunk) -> String {`
  - Purpose: Generates a deterministic UUID v5 string for a 'WikiVectorChunk' by hashing the chunk’s 'id' bytes with 'WIKI_VECTOR_UUID_NAMESPACE'. [crates/gwiki/src/vector.rs:247-249]
- `snippet` (function) component `snippet [function]` (`ae5e65cf-3e18-573d-8194-e636842939e3`) lines 251-253 [crates/gwiki/src/vector.rs:251-253]
  - Signature: `fn snippet(content: &str) -> String {`
  - Purpose: Returns the result of 'crate::support::text::snippet_from_text(content)', producing a 'String' snippet derived from the input text. [crates/gwiki/src/vector.rs:251-253]
- `PostgresWikiVectorChunkSource` (class) component `PostgresWikiVectorChunkSource [class]` (`3243b5e9-d507-5383-8b6c-809fe330e6fd`) lines 255-257 [crates/gwiki/src/vector.rs:255-257]
  - Signature: `pub(crate) struct PostgresWikiVectorChunkSource<'a> {`
  - Purpose: 'PostgresWikiVectorChunkSource<'a>' is a crate-private wrapper around a mutable 'postgres::Client' reference, used as a data source for retrieving wiki vector chunks from PostgreSQL. [crates/gwiki/src/vector.rs:255-257]
- `new` (function) component `new [function]` (`97d3d134-3c9b-5144-b358-904050981848`) lines 260-262 [crates/gwiki/src/vector.rs:260-262]
  - Signature: `pub(crate) fn new(conn: &'a mut postgres::Client) -> Self {`
  - Purpose: Constructs a new instance by wrapping the provided mutable 'postgres::Client' reference in 'Self' as the 'conn' field. [crates/gwiki/src/vector.rs:260-262]
- `chunks` (function) component `chunks [function]` (`5a418124-5a05-5b70-b1ed-394e1c9128d1`) lines 266-282 [crates/gwiki/src/vector.rs:266-282]
  - Signature: `fn chunks(&mut self, scope: &SearchScope) -> Result<Vec<WikiVectorChunk>, WikiVectorError> {`
  - Purpose: Queries all 'gwiki_chunks' rows for the given 'SearchScope', joining 'gwiki_documents' to enrich each row with document metadata, ordering by path and chunk index, and converts the result set into a 'Vec<WikiVectorChunk>'. [crates/gwiki/src/vector.rs:266-282]
- `stale_paths` (function) component `stale_paths [function]` (`910cae98-a441-54fc-a123-b0af7687e970`) lines 284-298 [crates/gwiki/src/vector.rs:284-298]
  - Signature: `fn stale_paths(&mut self, scope: &SearchScope) -> Result<Vec<String>, WikiVectorError> {`
  - Purpose: Queries 'gwiki_ingestions' for the latest record per 'path' within the given 'SearchScope' and returns the sorted list of paths whose most recent status is 'deleted'. [crates/gwiki/src/vector.rs:284-298]
- `row_to_vector_chunk` (function) component `row_to_vector_chunk [function]` (`5251140b-5d8e-5a49-b97f-aa8377a0e212`) lines 301-323 [crates/gwiki/src/vector.rs:301-323]
  - Signature: `fn row_to_vector_chunk(row: postgres::Row) -> Result<WikiVectorChunk, WikiVectorError> {`
  - Purpose: 'row_to_vector_chunk' converts a 'postgres::Row' into a 'WikiVectorChunk' by extracting required fields, joining a non-empty 'heading_path' into an optional 'heading', and validating that 'chunk_index' is non-negative before converting it to 'usize'. [crates/gwiki/src/vector.rs:301-323]
- `required_row_usize` (function) component `required_row_usize [function]` (`78f467cb-84c0-503d-aa4f-4b8fe08a3cac`) lines 325-330 [crates/gwiki/src/vector.rs:325-330]
  - Signature: `fn required_row_usize(row: &postgres::Row, column: &'static str) -> Result<usize, WikiVectorError> {`
  - Purpose: Fetches the named PostgreSQL row column as an optional string, converts any retrieval error into 'WikiVectorError::InvalidData', and then parses the value into a required 'usize' via 'parse_required_usize'. [crates/gwiki/src/vector.rs:325-330]
- `parse_required_usize` (function) component `parse_required_usize [function]` (`c3aa0e0d-b7e0-5f89-85f8-0d122bf541b3`) lines 332-340 [crates/gwiki/src/vector.rs:332-340]
  - Signature: `fn parse_required_usize(`
  - Purpose: 'parse_required_usize' requires an 'Option<String>' value, returns 'InvalidData' if it is missing, and otherwise parses it as 'usize', mapping parse failures to an 'InvalidData' error that includes the column name, raw value, and parse error. [crates/gwiki/src/vector.rs:332-340]
- `GwikiEmbeddingBackend` (class) component `GwikiEmbeddingBackend [class]` (`d12dee8c-13df-59b1-8524-9354ef5aa456`) lines 342-345 [crates/gwiki/src/vector.rs:342-345]
  - Signature: `pub(crate) struct GwikiEmbeddingBackend {`
  - Purpose: 'GwikiEmbeddingBackend' is an internal backend wrapper that stores a 'SemanticEmbedding' implementation alongside an 'OpenAiEmbeddingBackend' used to service embedding queries. [crates/gwiki/src/vector.rs:342-345]
- `GwikiEmbeddingBackend` (class) component `GwikiEmbeddingBackend [class]` (`89b80d13-4dee-570f-8a4c-f0b78eb6979f`) lines 347-354 [crates/gwiki/src/vector.rs:347-354]
  - Signature: `impl GwikiEmbeddingBackend {`
  - Purpose: 'GwikiEmbeddingBackend' is a backend wrapper that stores a 'SemanticEmbedding' and initializes an internal 'OpenAiEmbeddingBackend' for query embedding via its 'new' constructor. [crates/gwiki/src/vector.rs:347-354]
- `GwikiEmbeddingBackend.new` (method) component `GwikiEmbeddingBackend.new [method]` (`a2d29562-d4b9-5fd3-a1e7-927adc6158b3`) lines 348-353 [crates/gwiki/src/vector.rs:348-353]
  - Signature: `pub(crate) fn new(embedding: SemanticEmbedding) -> Self {`
  - Purpose: Constructs and returns a new instance initialized with the provided 'SemanticEmbedding' and a freshly created 'OpenAiEmbeddingBackend' as its 'query_backend'. [crates/gwiki/src/vector.rs:348-353]
- `GwikiEmbeddingBackend` (class) component `GwikiEmbeddingBackend [class]` (`25a55da2-570b-5097-997d-9b6d69bd1327`) lines 356-371 [crates/gwiki/src/vector.rs:356-371]
  - Signature: `impl WikiVectorEmbedder for GwikiEmbeddingBackend {`
  - Purpose: 'GwikiEmbeddingBackend' implements 'WikiVectorEmbedder' by embedding a batch of texts through either the AI daemon or the direct query backend, returning the resulting 'Vec<Vec<f32>>' and converting backend failures into 'WikiVectorError::Embedding'. [crates/gwiki/src/vector.rs:356-371]
- `GwikiEmbeddingBackend.embed_texts` (method) component `GwikiEmbeddingBackend.embed_texts [method]` (`6fe6977c-810c-5d6c-a013-1fb67bb91a69`) lines 357-370 [crates/gwiki/src/vector.rs:357-370]
  - Signature: `fn embed_texts(&mut self, texts: &[String]) -> Result<Vec<Vec<f32>>, WikiVectorError> {`
  - Purpose: Embeds each input text string by dispatching to either the daemon-based AI embedding path or the direct query backend, returning the resulting 'Vec<Vec<f32>>' or mapping any failure into 'WikiVectorError::Embedding'. [crates/gwiki/src/vector.rs:357-370]
- `GwikiQdrantVectorStore` (class) component `GwikiQdrantVectorStore [class]` (`5138dc99-6a97-5a9c-8958-dd923bcc2765`) lines 373-375 [crates/gwiki/src/vector.rs:373-375]
  - Signature: `pub(crate) struct GwikiQdrantVectorStore {`
  - Purpose: 'GwikiQdrantVectorStore' is a crate-visible wrapper struct that holds a 'QdrantConfig' and serves as the Qdrant-backed vector store configuration/state container. [crates/gwiki/src/vector.rs:373-375]
- `GwikiQdrantVectorStore` (class) component `GwikiQdrantVectorStore [class]` (`42bee84f-fde9-57bf-8c69-15a10ed010d4`) lines 377-381 [crates/gwiki/src/vector.rs:377-381]
  - Signature: `impl GwikiQdrantVectorStore {`
  - Purpose: 'GwikiQdrantVectorStore' is a Qdrant-backed vector-store wrapper that stores a 'QdrantConfig' and exposes a crate-visible 'new' constructor to initialize the instance. [crates/gwiki/src/vector.rs:377-381]
- `GwikiQdrantVectorStore.new` (method) component `GwikiQdrantVectorStore.new [method]` (`7047955d-6ddf-5b82-a64a-9dc54f0c3f09`) lines 378-380 [crates/gwiki/src/vector.rs:378-380]
  - Signature: `pub(crate) fn new(config: QdrantConfig) -> Self {`
  - Purpose: Constructs a new instance by initializing 'Self' with the provided 'QdrantConfig' stored in its 'config' field. [crates/gwiki/src/vector.rs:378-380]
- `GwikiQdrantVectorStore` (class) component `GwikiQdrantVectorStore [class]` (`a690d5b3-4461-52b1-9c1b-6b7a4280806a`) lines 383-416 [crates/gwiki/src/vector.rs:383-416]
  - Signature: `impl WikiVectorStore for GwikiQdrantVectorStore {`
  - Purpose: 'GwikiQdrantVectorStore' is a 'WikiVectorStore' adapter that delegates Qdrant collection creation, filtered point deletion, and batched point upserts to 'gobby_core::qdrant', converting 'WikiVectorPoint' values into 'UpsertRequest's and mapping any backend errors into 'WikiVectorError::Qdrant'. [crates/gwiki/src/vector.rs:383-416]
- `GwikiQdrantVectorStore.ensure_collection` (method) component `GwikiQdrantVectorStore.ensure_collection [method]` (`843e2a80-167a-5b29-822c-ef68cfb4dd68`) lines 384-392 [crates/gwiki/src/vector.rs:384-392]
  - Signature: `fn ensure_collection(`
  - Purpose: Forwards to 'gobby_core::qdrant::ensure_collection' to create or verify the named Qdrant collection with the given schema, then maps success to '()' and converts any Qdrant error into 'WikiVectorError::Qdrant' via its stringified message. [crates/gwiki/src/vector.rs:384-392]
- `GwikiQdrantVectorStore.delete_points` (method) component `GwikiQdrantVectorStore.delete_points [method]` (`8911b9db-605e-5f14-a10f-b2e2ee667ef3`) lines 394-397 [crates/gwiki/src/vector.rs:394-397]
  - Signature: `fn delete_points(&mut self, collection: &str, filter: Value) -> Result<(), WikiVectorError> {`
  - Purpose: Deletes points from the specified Qdrant collection by filter using the current configuration, mapping any Qdrant error into 'WikiVectorError::Qdrant' and returning 'Result<(), WikiVectorError>'. [crates/gwiki/src/vector.rs:394-397]
- `GwikiQdrantVectorStore.upsert_points` (method) component `GwikiQdrantVectorStore.upsert_points [method]` (`ab966236-2ae3-56cb-951b-64ec2f51f940`) lines 399-415 [crates/gwiki/src/vector.rs:399-415]
  - Signature: `fn upsert_points(`
  - Purpose: Converts a 'Vec<WikiVectorPoint>' into Qdrant 'UpsertRequest's and forwards them to 'gobby_core::qdrant::upsert_batched' for the specified collection, returning 'Ok(())' on success or wrapping any Qdrant error as 'WikiVectorError::Qdrant'. [crates/gwiki/src/vector.rs:399-415]
- `vector_collection_and_path_filter_match_scope_contract` (function) component `vector_collection_and_path_filter_match_scope_contract [function]` (`7c64ff70-df9f-5766-af18-1cb52a41525d`) lines 425-452 [crates/gwiki/src/vector.rs:425-452]
  - Signature: `fn vector_collection_and_path_filter_match_scope_contract() {`
  - Purpose: Verifies that scope-specific vector collection names are derived correctly for project and topic scopes, and that path deletion filters include the expected scope identifier and path values. [crates/gwiki/src/vector.rs:425-452]
- `vector_sync_embeds_upserts_and_deletes_stale_vectors` (function) component `vector_sync_embeds_upserts_and_deletes_stale_vectors [function]` (`cf13da1f-4db4-5087-9163-195445aabcf0`) lines 455-522 [crates/gwiki/src/vector.rs:455-522]
  - Signature: `fn vector_sync_embeds_upserts_and_deletes_stale_vectors() {`
  - Purpose: Synchronizes vectors for a search scope by embedding current chunks, ensuring the target collection, upserting the resulting vector points, and deleting stale vectors for removed paths while reporting chunk, upsert, and deletion counts. [crates/gwiki/src/vector.rs:455-522]
- `vector_sync_batches_embedding_and_upserts` (function) component `vector_sync_batches_embedding_and_upserts [function]` (`ec4fdd6a-0eb8-5d8a-a015-e6633a97f206`) lines 525-566 [crates/gwiki/src/vector.rs:525-566]
  - Signature: `fn vector_sync_batches_embedding_and_upserts() {`
  - Purpose: Verifies that 'sync_scope_vectors' embeds and upserts 129 project chunks in two batches of 128 and 1, preserving chunk metadata in the final upsert payload. [crates/gwiki/src/vector.rs:525-566]
- `direct_embedding_backend_batches_texts` (function) component `direct_embedding_backend_batches_texts [function]` (`b761d88e-52b4-549e-80cb-6ceb8cb08bce`) lines 570-604 [crates/gwiki/src/vector.rs:570-604]
  - Signature: `fn direct_embedding_backend_batches_texts() {`
  - Purpose: Verifies that 'GwikiEmbeddingBackend::embed_texts' sends a single 'POST /embeddings' request with the configured bearer token, model, and batched text array, and returns the two embedding vectors from the JSON response in order. [crates/gwiki/src/vector.rs:570-604]
- `vector_required_offset_parser_rejects_missing_and_malformed_values` (function) component `vector_required_offset_parser_rejects_missing_and_malformed_values [function]` (`c294d46a-84c1-5b70-a520-c5f4304a057e`) lines 607-617 [crates/gwiki/src/vector.rs:607-617]
  - Signature: `fn vector_required_offset_parser_rejects_missing_and_malformed_values() {`
  - Purpose: Verifies that 'parse_required_usize' returns 'WikiVectorError::InvalidData' when a required offset field is missing and when a provided value is non-numeric, with error messages identifying the field name and invalid input. [crates/gwiki/src/vector.rs:607-617]
- `MockChunkSource` (class) component `MockChunkSource [class]` (`55dbb8ab-edcc-59d3-98fe-66eb2474d453`) lines 619-622 [crates/gwiki/src/vector.rs:619-622]
  - Signature: `struct MockChunkSource {`
  - Purpose: 'MockChunkSource' is a test/dummy chunk source that holds an in-memory 'Vec<WikiVectorChunk>' plus a list of 'stale_paths' as 'Vec<String>' for simulating available and stale chunk references. [crates/gwiki/src/vector.rs:619-622]
- `MockChunkSource` (class) component `MockChunkSource [class]` (`bea372f0-d062-57b5-9486-3696a62530c3`) lines 624-635 [crates/gwiki/src/vector.rs:624-635]
  - Signature: `impl WikiVectorChunkSource for MockChunkSource {`
  - Purpose: 'MockChunkSource' is a test double for 'WikiVectorChunkSource' that returns cloned in-memory 'chunks' and 'stale_paths' values from its internal state, ignoring the provided 'SearchScope'. [crates/gwiki/src/vector.rs:624-635]
- `MockChunkSource.chunks` (method) component `MockChunkSource.chunks [method]` (`df30372e-a182-5d77-8268-572a1dbfd8ad`) lines 625-630 [crates/gwiki/src/vector.rs:625-630]
  - Signature: `fn chunks(`
  - Purpose: Returns a cloned 'Vec<WikiVectorChunk>' from 'self.chunks' wrapped in 'Ok', ignoring the provided 'SearchScope' and never producing an error in this implementation. [crates/gwiki/src/vector.rs:625-630]
- `MockChunkSource.stale_paths` (method) component `MockChunkSource.stale_paths [method]` (`44431d53-440b-5e3c-8833-9184a7660977`) lines 632-634 [crates/gwiki/src/vector.rs:632-634]
  - Signature: `fn stale_paths(&mut self, _scope: &SearchScope) -> Result<Vec<String>, WikiVectorError> {`
  - Purpose: Returns a cloned 'Vec<String>' of the vector index’s currently tracked stale paths, ignoring the provided 'SearchScope'. [crates/gwiki/src/vector.rs:632-634]
- `MockEmbedder` (class) component `MockEmbedder [class]` (`0f6472da-7ae5-5254-8811-cf0d486b50c0`) lines 637-640 [crates/gwiki/src/vector.rs:637-640]
  - Signature: `struct MockEmbedder {`
  - Purpose: 'MockEmbedder' is a test double that stores a sequence of embedding vectors ('Vec<Vec<f32>>') and the corresponding input strings ('Vec<String>') it was given. [crates/gwiki/src/vector.rs:637-640]
- `MockEmbedder` (class) component `MockEmbedder [class]` (`22eaba03-dee1-5054-ac6a-0c1ad0af605e`) lines 642-648 [crates/gwiki/src/vector.rs:642-648]
  - Signature: `impl WikiVectorEmbedder for MockEmbedder {`
  - Purpose: 'MockEmbedder' is a test 'WikiVectorEmbedder' implementation that records every input text into 'self.inputs' and returns up to 'texts.len()' preseeded vectors by draining them from the front of 'self.vectors'. [crates/gwiki/src/vector.rs:642-648]
- `MockEmbedder.embed_texts` (method) component `MockEmbedder.embed_texts [method]` (`55b7d681-e1f6-5fb2-be30-31ba1bc3e5af`) lines 643-647 [crates/gwiki/src/vector.rs:643-647]
  - Signature: `fn embed_texts(&mut self, texts: &[String]) -> Result<Vec<Vec<f32>>, WikiVectorError> {`
  - Purpose: Appends the provided 'texts' to 'self.inputs', then drains and returns up to 'min(texts.len(), self.vectors.len())' vectors from the front of 'self.vectors' as 'Ok(Vec<Vec<f32>>)'. [crates/gwiki/src/vector.rs:643-647]
- `RecordingVectorStore` (class) component `RecordingVectorStore [class]` (`71837415-89dd-51b4-8604-80e20aad83d2`) lines 651-655 [crates/gwiki/src/vector.rs:651-655]
  - Signature: `struct RecordingVectorStore {`
  - Purpose: 'RecordingVectorStore' is a test-recording data structure that captures vector-store operations by storing ensured entries as '(String, usize, String)' tuples, deleted values as 'Value' instances, and upsert events as 'RecordedUpsert' records. [crates/gwiki/src/vector.rs:651-655]
- `RecordedUpsert` (class) component `RecordedUpsert [class]` (`87e6a16d-6b45-5f15-884f-e511d08f6dfa`) lines 657-660 [crates/gwiki/src/vector.rs:657-660]
  - Signature: `struct RecordedUpsert {`
  - Purpose: 'RecordedUpsert' is a data-only struct that represents an upsert operation by pairing a target 'collection' name with a 'Vec<WikiVectorPoint>' of points to be written. [crates/gwiki/src/vector.rs:657-660]
- `RecordingVectorStore` (class) component `RecordingVectorStore [class]` (`c55d376c-ec6c-5a84-93fe-ca6acfdca7eb`) lines 662-693 [crates/gwiki/src/vector.rs:662-693]
  - Signature: `impl WikiVectorStore for RecordingVectorStore {`
  - Purpose: 'RecordingVectorStore' is a 'WikiVectorStore' test double that records 'ensure_collection' calls as '(collection, size, distance)', stores deleted-point filters, and captures each 'upsert_points' call with its target collection and points while always returning 'Ok(())'. [crates/gwiki/src/vector.rs:662-693]
- `RecordingVectorStore.ensure_collection` (method) component `RecordingVectorStore.ensure_collection [method]` (`84303008-e522-575d-b2e3-a3cb925be502`) lines 663-671 [crates/gwiki/src/vector.rs:663-671]
  - Signature: `fn ensure_collection(`
  - Purpose: Appends the collection name together with the schema’s vector size and distance to 'self.ensured', then returns 'Ok(())' without performing any validation or creation. [crates/gwiki/src/vector.rs:663-671]
- `RecordingVectorStore.delete_points` (method) component `RecordingVectorStore.delete_points [method]` (`3c44c2bb-954d-5612-8787-8bb97bffecbd`) lines 673-680 [crates/gwiki/src/vector.rs:673-680]
  - Signature: `fn delete_points(`
  - Purpose: 'delete_points' records the provided 'filter' by pushing it onto 'self.deleted' and then returns 'Ok(())', ignoring the '_collection' argument entirely. [crates/gwiki/src/vector.rs:673-680]
- `RecordingVectorStore.upsert_points` (method) component `RecordingVectorStore.upsert_points [method]` (`a5dd24c3-e627-5214-8c65-f8326959bd94`) lines 682-692 [crates/gwiki/src/vector.rs:682-692]
  - Signature: `fn upsert_points(`
  - Purpose: Appends a 'RecordedUpsert' containing the target 'collection' name and provided 'points' to 'self.upserts', then returns 'Ok(())' without performing any validation or persistence. [crates/gwiki/src/vector.rs:682-692]
- `filter_value` (function) component `filter_value [function]` (`c8e9e71d-978e-5281-91dd-190c26c6c90a`) lines 695-704 [crates/gwiki/src/vector.rs:695-704]
  - Signature: `fn filter_value(filter: &Value, key: &str) -> Option<String> {`
  - Purpose: 'filter_value' searches the 'filter["must"]' array for the first condition whose '"key"' matches 'key', then returns the string at '"/match/value"' in that condition as an owned 'String', or 'None' if any step is missing or not a string. [crates/gwiki/src/vector.rs:695-704]

