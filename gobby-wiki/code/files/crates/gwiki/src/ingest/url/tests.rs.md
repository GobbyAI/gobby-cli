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
  - 251-254
  - 256-258
  - 260-262
  - 264-266
  - 268-270
  - 272-274
  - 276-278
  - 280-282
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/url/tests.rs:21-60](crates/gwiki/src/ingest/url/tests.rs#L21-L60), [crates/gwiki/src/ingest/url/tests.rs:63-93](crates/gwiki/src/ingest/url/tests.rs#L63-L93), [crates/gwiki/src/ingest/url/tests.rs:96-107](crates/gwiki/src/ingest/url/tests.rs#L96-L107), [crates/gwiki/src/ingest/url/tests.rs:110-152](crates/gwiki/src/ingest/url/tests.rs#L110-L152), [crates/gwiki/src/ingest/url/tests.rs:155-175](crates/gwiki/src/ingest/url/tests.rs#L155-L175), [crates/gwiki/src/ingest/url/tests.rs:178-193](crates/gwiki/src/ingest/url/tests.rs#L178-L193), [crates/gwiki/src/ingest/url/tests.rs:196-216](crates/gwiki/src/ingest/url/tests.rs#L196-L216), [crates/gwiki/src/ingest/url/tests.rs:219-224](crates/gwiki/src/ingest/url/tests.rs#L219-L224), [crates/gwiki/src/ingest/url/tests.rs:226-242](crates/gwiki/src/ingest/url/tests.rs#L226-L242), [crates/gwiki/src/ingest/url/tests.rs:245-248](crates/gwiki/src/ingest/url/tests.rs#L245-L248), [crates/gwiki/src/ingest/url/tests.rs:251-254](crates/gwiki/src/ingest/url/tests.rs#L251-L254), [crates/gwiki/src/ingest/url/tests.rs:256-258](crates/gwiki/src/ingest/url/tests.rs#L256-L258), [crates/gwiki/src/ingest/url/tests.rs:260-262](crates/gwiki/src/ingest/url/tests.rs#L260-L262), [crates/gwiki/src/ingest/url/tests.rs:264-266](crates/gwiki/src/ingest/url/tests.rs#L264-L266), [crates/gwiki/src/ingest/url/tests.rs:268-270](crates/gwiki/src/ingest/url/tests.rs#L268-L270), [crates/gwiki/src/ingest/url/tests.rs:272-274](crates/gwiki/src/ingest/url/tests.rs#L272-L274), [crates/gwiki/src/ingest/url/tests.rs:276-278](crates/gwiki/src/ingest/url/tests.rs#L276-L278), [crates/gwiki/src/ingest/url/tests.rs:280-282](crates/gwiki/src/ingest/url/tests.rs#L280-L282)

</details>

# crates/gwiki/src/ingest/url/tests.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This test file exercises the URL ingestion pipeline end to end. It verifies that ingesting a snapshot writes the rendered raw document plus source manifest metadata, preserves non-HTML content as a typed asset, and that the HTML parser extracts body text and decodes entities correctly. It also covers batch ingestion behavior, including accepting partial successes while recording failures and indexing only once for an accepted batch, plus fetch safeguards such as content-length limits, blocking private/local addresses, and resolving relative redirect locations. A small `CountingStore` test double is included to track index/store method calls used by the ingestion flow.
[crates/gwiki/src/ingest/url/tests.rs:21-60]
[crates/gwiki/src/ingest/url/tests.rs:63-93]
[crates/gwiki/src/ingest/url/tests.rs:96-107]
[crates/gwiki/src/ingest/url/tests.rs:110-152]
[crates/gwiki/src/ingest/url/tests.rs:155-175]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `url_ingest_writes_raw_and_manifest` | function | `fn url_ingest_writes_raw_and_manifest() {` | `url_ingest_writes_raw_and_manifest [function]` | `dc1bc4da-6d0f-5fff-9eb7-f5a9d4488b61` | 21-60 [crates/gwiki/src/ingest/url/tests.rs:21-60] | Indexed function `url_ingest_writes_raw_and_manifest` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:21-60] |
| `url_ingest_preserves_non_html_as_typed_asset` | function | `fn url_ingest_preserves_non_html_as_typed_asset() {` | `url_ingest_preserves_non_html_as_typed_asset [function]` | `270f239e-942c-5b9c-93fb-e603a581ff4c` | 63-93 [crates/gwiki/src/ingest/url/tests.rs:63-93] | Indexed function `url_ingest_preserves_non_html_as_typed_asset` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:63-93] |
| `html_parser_extracts_body_text_and_decodes_entities` | function | `fn html_parser_extracts_body_text_and_decodes_entities() {` | `html_parser_extracts_body_text_and_decodes_entities [function]` | `9910df43-b2d5-5366-801a-2a532122b7f2` | 96-107 [crates/gwiki/src/ingest/url/tests.rs:96-107] | Indexed function `html_parser_extracts_body_text_and_decodes_entities` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:96-107] |
| `batch_url_ingest_accepts_successes_and_records_failures` | function | `fn batch_url_ingest_accepts_successes_and_records_failures() {` | `batch_url_ingest_accepts_successes_and_records_failures [function]` | `a18ae2a6-e388-5b49-bfa5-cdce243b04f6` | 110-152 [crates/gwiki/src/ingest/url/tests.rs:110-152] | Indexed function `batch_url_ingest_accepts_successes_and_records_failures` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:110-152] |
| `batch_url_ingest_indexes_once_after_accepted_batch` | function | `fn batch_url_ingest_indexes_once_after_accepted_batch() {` | `batch_url_ingest_indexes_once_after_accepted_batch [function]` | `ea11c97a-4a6f-5c17-bf3f-5bfe3a3c8fe8` | 155-175 [crates/gwiki/src/ingest/url/tests.rs:155-175] | Indexed function `batch_url_ingest_indexes_once_after_accepted_batch` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:155-175] |
| `url_fetch_limits_content_length_and_stream_bytes` | function | `fn url_fetch_limits_content_length_and_stream_bytes() {` | `url_fetch_limits_content_length_and_stream_bytes [function]` | `ebc06a55-a3e1-508e-a71c-79ae95b34bcb` | 178-193 [crates/gwiki/src/ingest/url/tests.rs:178-193] | Indexed function `url_fetch_limits_content_length_and_stream_bytes` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:178-193] |
| `url_fetch_rejects_private_and_local_addresses` | function | `fn url_fetch_rejects_private_and_local_addresses() {` | `url_fetch_rejects_private_and_local_addresses [function]` | `5122fa23-568d-5c76-9002-ac467cd4b7d1` | 196-216 [crates/gwiki/src/ingest/url/tests.rs:196-216] | Indexed function `url_fetch_rejects_private_and_local_addresses` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:196-216] |
| `redirect_url_resolution_handles_relative_locations` | function | `fn redirect_url_resolution_handles_relative_locations() {` | `redirect_url_resolution_handles_relative_locations [function]` | `c277ee98-3ba2-5a69-b3d3-7a367778c8ac` | 219-224 [crates/gwiki/src/ingest/url/tests.rs:219-224] | Indexed function `redirect_url_resolution_handles_relative_locations` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:219-224] |
| `test_snapshot` | function | `fn test_snapshot(` | `test_snapshot [function]` | `242d9bc6-25df-5dc5-b7b7-242079068a47` | 226-242 [crates/gwiki/src/ingest/url/tests.rs:226-242] | Indexed function `test_snapshot` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:226-242] |
| `CountingStore` | class | `struct CountingStore {` | `CountingStore [class]` | `bae02c35-ce0a-5c31-af41-2ffb4e358285` | 245-248 [crates/gwiki/src/ingest/url/tests.rs:245-248] | Indexed class `CountingStore` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:245-248] |
| `CountingStore::indexed_hashes` | method | `fn indexed_hashes(&mut self) -> Result<BTreeMap<PathBuf, String>, StoreError> {` | `CountingStore::indexed_hashes [method]` | `4a4e0d07-296e-56f8-a944-2760bd5eba96` | 251-254 [crates/gwiki/src/ingest/url/tests.rs:251-254] | Indexed method `CountingStore::indexed_hashes` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:251-254] |
| `CountingStore::upsert_document` | method | `fn upsert_document(&mut self, document: WikiDocument) -> Result<(), StoreError> {` | `CountingStore::upsert_document [method]` | `52f34138-c19e-56c5-ad66-3be5fc0dd4b7` | 256-258 [crates/gwiki/src/ingest/url/tests.rs:256-258] | Indexed method `CountingStore::upsert_document` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:256-258] |
| `CountingStore::replace_chunks` | method | `fn replace_chunks(&mut self, path: &Path, chunks: Vec<WikiChunk>) -> Result<(), StoreError> {` | `CountingStore::replace_chunks [method]` | `5fb4eb2d-23fa-5f0f-9202-b0fe589584ca` | 260-262 [crates/gwiki/src/ingest/url/tests.rs:260-262] | Indexed method `CountingStore::replace_chunks` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:260-262] |
| `CountingStore::replace_links` | method | `fn replace_links(&mut self, path: &Path, links: Vec<WikiLink>) -> Result<(), StoreError> {` | `CountingStore::replace_links [method]` | `ba0352de-22b0-54a0-b1ef-000a467d8acb` | 264-266 [crates/gwiki/src/ingest/url/tests.rs:264-266] | Indexed method `CountingStore::replace_links` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:264-266] |
| `CountingStore::upsert_source` | method | `fn upsert_source(&mut self, source: WikiSource) -> Result<(), StoreError> {` | `CountingStore::upsert_source [method]` | `badcee9b-37de-5e74-946b-1fa178053e29` | 268-270 [crates/gwiki/src/ingest/url/tests.rs:268-270] | Indexed method `CountingStore::upsert_source` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:268-270] |
| `CountingStore::record_ingestion` | method | `fn record_ingestion(&mut self, ingestion: WikiIngestion) -> Result<(), StoreError> {` | `CountingStore::record_ingestion [method]` | `01a66b80-f006-5fb4-8c35-1312f7b68adb` | 272-274 [crates/gwiki/src/ingest/url/tests.rs:272-274] | Indexed method `CountingStore::record_ingestion` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:272-274] |
| `CountingStore::record_file_hash` | method | `fn record_file_hash(&mut self, path: PathBuf, content_hash: String) -> Result<(), StoreError> {` | `CountingStore::record_file_hash [method]` | `0962ec4b-6488-58a8-b32b-030e362216ae` | 276-278 [crates/gwiki/src/ingest/url/tests.rs:276-278] | Indexed method `CountingStore::record_file_hash` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:276-278] |
| `CountingStore::delete_derived_rows` | method | `fn delete_derived_rows(&mut self, path: &Path) -> Result<(), StoreError> {` | `CountingStore::delete_derived_rows [method]` | `2573c39b-46fe-5265-897d-74aa7e1a8635` | 280-282 [crates/gwiki/src/ingest/url/tests.rs:280-282] | Indexed method `CountingStore::delete_derived_rows` in `crates/gwiki/src/ingest/url/tests.rs`. [crates/gwiki/src/ingest/url/tests.rs:280-282] |
