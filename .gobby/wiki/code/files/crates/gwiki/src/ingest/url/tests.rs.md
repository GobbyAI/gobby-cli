---
title: crates/gwiki/src/ingest/url/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/url/tests.rs
  ranges:
  - 21-60
  - 63-93
  - 96-107
  - 110-152
  - 155-175
  - 178-193
  - 196-216
  - 219-224
  - 226-242
  - 245-248
  - 250-283
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/url/tests.rs

Module: [[code/modules/crates/gwiki/src/ingest/url|crates/gwiki/src/ingest/url]]

## Purpose

Test module for URL ingestion. It exercises the end-to-end ingest pipeline and its helpers: writing raw snapshots and source manifests, preserving non-HTML responses as typed assets, extracting readable text from HTML, handling batch partial success and single indexing passes, enforcing fetch size/IP limits, and resolving redirects.

The file also defines shared test support: `test_snapshot` builds synthetic `UrlSnapshot` values, and `CountingStore` wraps `MemoryWikiStore` to forward all store operations while counting `indexed_hashes()` calls so tests can verify indexing behavior.
[crates/gwiki/src/ingest/url/tests.rs:21-60]
[crates/gwiki/src/ingest/url/tests.rs:63-93]
[crates/gwiki/src/ingest/url/tests.rs:96-107]
[crates/gwiki/src/ingest/url/tests.rs:110-152]
[crates/gwiki/src/ingest/url/tests.rs:155-175]

## API Symbols

- `url_ingest_writes_raw_and_manifest` (function) component `url_ingest_writes_raw_and_manifest [function]` (`dc1bc4da-6d0f-5fff-9eb7-f5a9d4488b61`) lines 21-60 [crates/gwiki/src/ingest/url/tests.rs:21-60]
  - Signature: `fn url_ingest_writes_raw_and_manifest() {`
  - Purpose: Indexed function `url_ingest_writes_raw_and_manifest` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:21-60]
- `url_ingest_preserves_non_html_as_typed_asset` (function) component `url_ingest_preserves_non_html_as_typed_asset [function]` (`270f239e-942c-5b9c-93fb-e603a581ff4c`) lines 63-93 [crates/gwiki/src/ingest/url/tests.rs:63-93]
  - Signature: `fn url_ingest_preserves_non_html_as_typed_asset() {`
  - Purpose: Verifies that ingesting a URL snapshot whose response is PDF content preserves the original bytes as a typed asset, records the raw metadata with 'source_kind: pdf' and 'media_degradation: url_non_html_asset', omits the binary body from the markdown, and classifies the manifest entry as 'SourceKind::Pdf'. [crates/gwiki/src/ingest/url/tests.rs:63-93]
- `html_parser_extracts_body_text_and_decodes_entities` (function) component `html_parser_extracts_body_text_and_decodes_entities [function]` (`9910df43-b2d5-5366-801a-2a532122b7f2`) lines 96-107 [crates/gwiki/src/ingest/url/tests.rs:96-107]
  - Signature: `fn html_parser_extracts_body_text_and_decodes_entities() {`
  - Purpose: Verifies that the HTML parser decodes entities in both the document title and body text, while 'html_to_markdownish_text' extracts only visible body content and omits script content. [crates/gwiki/src/ingest/url/tests.rs:96-107]
- `batch_url_ingest_accepts_successes_and_records_failures` (function) component `batch_url_ingest_accepts_successes_and_records_failures [function]` (`a18ae2a6-e388-5b49-bfa5-cdce243b04f6`) lines 110-152 [crates/gwiki/src/ingest/url/tests.rs:110-152]
  - Signature: `fn batch_url_ingest_accepts_successes_and_records_failures() {`
  - Purpose: Verifies that 'ingest_urls_with_fetcher' processes a URL batch as partial success when one fetch succeeds and one fails, returns exit code 0, records the accepted and failed entries in the result, writes the accepted document to the store and source manifest, and omits the failed URL from the manifest. [crates/gwiki/src/ingest/url/tests.rs:110-152]
- `batch_url_ingest_indexes_once_after_accepted_batch` (function) component `batch_url_ingest_indexes_once_after_accepted_batch [function]` (`ea11c97a-4a6f-5c17-bf3f-5bfe3a3c8fe8`) lines 155-175 [crates/gwiki/src/ingest/url/tests.rs:155-175]
  - Signature: `fn batch_url_ingest_indexes_once_after_accepted_batch() {`
  - Purpose: Verifies that a successful batch URL ingest accepts both URLs, returns 'ingested', and performs exactly one indexed-hash read against the store. [crates/gwiki/src/ingest/url/tests.rs:155-175]
- `url_fetch_limits_content_length_and_stream_bytes` (function) component `url_fetch_limits_content_length_and_stream_bytes [function]` (`ebc06a55-a3e1-508e-a71c-79ae95b34bcb`) lines 178-193 [crates/gwiki/src/ingest/url/tests.rs:178-193]
  - Signature: `fn url_fetch_limits_content_length_and_stream_bytes() {`
  - Purpose: Verifies that response content-length values above the byte limit are rejected, invalid content-length headers are ignored, and streamed bodies larger than the limit fail with 'response_too_large' while bodies at the limit are accepted. [crates/gwiki/src/ingest/url/tests.rs:178-193]
- `url_fetch_rejects_private_and_local_addresses` (function) component `url_fetch_rejects_private_and_local_addresses [function]` (`5122fa23-568d-5c76-9002-ac467cd4b7d1`) lines 196-216 [crates/gwiki/src/ingest/url/tests.rs:196-216]
  - Signature: `fn url_fetch_rejects_private_and_local_addresses() {`
  - Purpose: Indexed function `url_fetch_rejects_private_and_local_addresses` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:196-216]
- `redirect_url_resolution_handles_relative_locations` (function) component `redirect_url_resolution_handles_relative_locations [function]` (`c277ee98-3ba2-5a69-b3d3-7a367778c8ac`) lines 219-224 [crates/gwiki/src/ingest/url/tests.rs:219-224]
  - Signature: `fn redirect_url_resolution_handles_relative_locations() {`
  - Purpose: Verifies that 'resolve_redirect_url' correctly resolves a relative redirect location ('"../next"') against the base URL '"https://example.com/a/b"' to produce '"https://example.com/next"'. [crates/gwiki/src/ingest/url/tests.rs:219-224]
- `test_snapshot` (function) component `test_snapshot [function]` (`242d9bc6-25df-5dc5-b7b7-242079068a47`) lines 226-242 [crates/gwiki/src/ingest/url/tests.rs:226-242]
  - Signature: `fn test_snapshot(`
  - Purpose: Constructs and returns a 'UrlSnapshot' populated with the provided requested/final URLs and fetch timestamp, plus an HTML body and 'text/html' content type derived from 'title'. [crates/gwiki/src/ingest/url/tests.rs:226-242]
- `CountingStore` (class) component `CountingStore [class]` (`bae02c35-ce0a-5c31-af41-2ffb4e358285`) lines 245-248 [crates/gwiki/src/ingest/url/tests.rs:245-248]
  - Signature: `struct CountingStore {`
  - Purpose: 'CountingStore' is a wrapper struct around 'MemoryWikiStore' that additionally tracks the number of indexed hash reads via a 'usize' counter. [crates/gwiki/src/ingest/url/tests.rs:245-248]
- `CountingStore` (class) component `CountingStore [class]` (`c18ae269-e60a-57f9-a660-ba0a57220b7f`) lines 250-283 [crates/gwiki/src/ingest/url/tests.rs:250-283]
  - Signature: `impl WikiIndexStore for CountingStore {`
  - Purpose: 'CountingStore' is a 'WikiIndexStore' wrapper that increments an 'indexed_hash_reads' counter on each 'indexed_hashes()' call and forwards all other store operations unchanged to its inner implementation. [crates/gwiki/src/ingest/url/tests.rs:250-283]
- `CountingStore.indexed_hashes` (method) component `CountingStore.indexed_hashes [method]` (`4a4e0d07-296e-56f8-a944-2760bd5eba96`) lines 251-254 [crates/gwiki/src/ingest/url/tests.rs:251-254]
  - Signature: `fn indexed_hashes(&mut self) -> Result<BTreeMap<PathBuf, String>, StoreError> {`
  - Purpose: Increments 'indexed_hash_reads' by one, then delegates to 'self.inner.indexed_hashes()' and returns its 'Result<BTreeMap<PathBuf, String>, StoreError>'. [crates/gwiki/src/ingest/url/tests.rs:251-254]
- `CountingStore.upsert_document` (method) component `CountingStore.upsert_document [method]` (`52f34138-c19e-56c5-ad66-3be5fc0dd4b7`) lines 256-258 [crates/gwiki/src/ingest/url/tests.rs:256-258]
  - Signature: `fn upsert_document(&mut self, document: WikiDocument) -> Result<(), StoreError> {`
  - Purpose: Forwards the provided 'WikiDocument' to 'self.inner.upsert_document' to insert or update it in the backing store, propagating any 'StoreError'. [crates/gwiki/src/ingest/url/tests.rs:256-258]
- `CountingStore.replace_chunks` (method) component `CountingStore.replace_chunks [method]` (`5fb4eb2d-23fa-5f0f-9202-b0fe589584ca`) lines 260-262 [crates/gwiki/src/ingest/url/tests.rs:260-262]
  - Signature: `fn replace_chunks(&mut self, path: &Path, chunks: Vec<WikiChunk>) -> Result<(), StoreError> {`
  - Purpose: Delegates to 'self.inner.replace_chunks' to atomically replace the chunk set associated with 'path' with the provided 'WikiChunk' vector, returning any 'StoreError' from the inner store. [crates/gwiki/src/ingest/url/tests.rs:260-262]
- `CountingStore.replace_links` (method) component `CountingStore.replace_links [method]` (`ba0352de-22b0-54a0-b1ef-000a467d8acb`) lines 264-266 [crates/gwiki/src/ingest/url/tests.rs:264-266]
  - Signature: `fn replace_links(&mut self, path: &Path, links: Vec<WikiLink>) -> Result<(), StoreError> {`
  - Purpose: Delegates to 'self.inner.replace_links(path, links)' to atomically replace the wiki links associated with 'path', returning any 'StoreError' from the inner store. [crates/gwiki/src/ingest/url/tests.rs:264-266]
- `CountingStore.upsert_source` (method) component `CountingStore.upsert_source [method]` (`badcee9b-37de-5e74-946b-1fa178053e29`) lines 268-270 [crates/gwiki/src/ingest/url/tests.rs:268-270]
  - Signature: `fn upsert_source(&mut self, source: WikiSource) -> Result<(), StoreError> {`
  - Purpose: Forwards a 'WikiSource' upsert request to 'self.inner.upsert_source', returning its 'Result<(), StoreError>' unchanged. [crates/gwiki/src/ingest/url/tests.rs:268-270]
- `CountingStore.record_ingestion` (method) component `CountingStore.record_ingestion [method]` (`01a66b80-f006-5fb4-8c35-1312f7b68adb`) lines 272-274 [crates/gwiki/src/ingest/url/tests.rs:272-274]
  - Signature: `fn record_ingestion(&mut self, ingestion: WikiIngestion) -> Result<(), StoreError> {`
  - Purpose: Forwards the 'WikiIngestion' record to the wrapped store implementation via 'self.inner.record_ingestion(ingestion)' and returns its 'Result<(), StoreError>'. [crates/gwiki/src/ingest/url/tests.rs:272-274]
- `CountingStore.record_file_hash` (method) component `CountingStore.record_file_hash [method]` (`0962ec4b-6488-58a8-b32b-030e362216ae`) lines 276-278 [crates/gwiki/src/ingest/url/tests.rs:276-278]
  - Signature: `fn record_file_hash(&mut self, path: PathBuf, content_hash: String) -> Result<(), StoreError> {`
  - Purpose: Delegates 'record_file_hash' to 'self.inner', recording the provided 'content_hash' for the given 'path' and returning the underlying 'Result<(), StoreError>'. [crates/gwiki/src/ingest/url/tests.rs:276-278]
- `CountingStore.delete_derived_rows` (method) component `CountingStore.delete_derived_rows [method]` (`2573c39b-46fe-5265-897d-74aa7e1a8635`) lines 280-282 [crates/gwiki/src/ingest/url/tests.rs:280-282]
  - Signature: `fn delete_derived_rows(&mut self, path: &Path) -> Result<(), StoreError> {`
  - Purpose: Forwards the 'path' argument to 'self.inner.delete_derived_rows(path)' and returns its 'Result<(), StoreError>'. [crates/gwiki/src/ingest/url/tests.rs:280-282]

