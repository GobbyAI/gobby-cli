---
title: crates/gwiki/src/store/postgres.rs
type: code_file
provenance:
- file: crates/gwiki/src/store/postgres.rs
  ranges:
  - 18-22
  - 24-28
  - 31-37
  - 39-46
  - 48-75
  - 79-95
  - 97-153
  - 155-251
  - 253-322
  - 324-368
  - 370-415
  - 417-424
  - 426-451
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/store/postgres.rs:18-22](crates/gwiki/src/store/postgres.rs#L18-L22), [crates/gwiki/src/store/postgres.rs:24-28](crates/gwiki/src/store/postgres.rs#L24-L28), [crates/gwiki/src/store/postgres.rs:31-37](crates/gwiki/src/store/postgres.rs#L31-L37), [crates/gwiki/src/store/postgres.rs:39-46](crates/gwiki/src/store/postgres.rs#L39-L46), [crates/gwiki/src/store/postgres.rs:48-75](crates/gwiki/src/store/postgres.rs#L48-L75), [crates/gwiki/src/store/postgres.rs:79-95](crates/gwiki/src/store/postgres.rs#L79-L95), [crates/gwiki/src/store/postgres.rs:97-153](crates/gwiki/src/store/postgres.rs#L97-L153), [crates/gwiki/src/store/postgres.rs:155-251](crates/gwiki/src/store/postgres.rs#L155-L251), [crates/gwiki/src/store/postgres.rs:253-322](crates/gwiki/src/store/postgres.rs#L253-L322), [crates/gwiki/src/store/postgres.rs:324-368](crates/gwiki/src/store/postgres.rs#L324-L368), [crates/gwiki/src/store/postgres.rs:370-415](crates/gwiki/src/store/postgres.rs#L370-L415), [crates/gwiki/src/store/postgres.rs:417-424](crates/gwiki/src/store/postgres.rs#L417-L424), [crates/gwiki/src/store/postgres.rs:426-451](crates/gwiki/src/store/postgres.rs#L426-L451)

</details>

# crates/gwiki/src/store/postgres.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the Postgres-backed `WikiIndexStore` for a scoped wiki ingestion/indexing workflow. `PostgresWikiStore` holds a mutable Postgres client, the active `WikiStoreScope`, and an in-memory cache of per-path `DocumentMeta` so repeated document lookups avoid extra queries. The helpers compute scope parameters and load document metadata from `gwiki_documents`, while the store methods use that metadata to upsert documents and sources, replace chunk and link rows, record ingestion status and file hashes, return indexed hashes, and delete derived rows when reprocessing or rolling back indexed content.
[crates/gwiki/src/store/postgres.rs:18-22]
[crates/gwiki/src/store/postgres.rs:24-28]
[crates/gwiki/src/store/postgres.rs:31-37]
[crates/gwiki/src/store/postgres.rs:39-46]
[crates/gwiki/src/store/postgres.rs:48-75]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `DocumentMeta` | class | `struct DocumentMeta {` | `DocumentMeta [class]` | `dd3cf6fd-b416-5b98-bfc6-8cc64c666857` | 18-22 [crates/gwiki/src/store/postgres.rs:18-22] | Indexed class `DocumentMeta` in `crates/gwiki/src/store/postgres.rs`. [crates/gwiki/src/store/postgres.rs:18-22] |
| `PostgresWikiStore` | class | `pub struct PostgresWikiStore<'a> {` | `PostgresWikiStore [class]` | `93c4fb76-5399-5f16-b669-ce57e18ffba3` | 24-28 [crates/gwiki/src/store/postgres.rs:24-28] | Indexed class `PostgresWikiStore` in `crates/gwiki/src/store/postgres.rs`. [crates/gwiki/src/store/postgres.rs:24-28] |
| `new` | function | `pub fn new(conn: &'a mut ::postgres::Client, scope: WikiStoreScope) -> Self {` | `new [function]` | `00be2b94-0b3b-55b2-a0e6-1a96870b19c2` | 31-37 [crates/gwiki/src/store/postgres.rs:31-37] | Indexed function `new` in `crates/gwiki/src/store/postgres.rs`. [crates/gwiki/src/store/postgres.rs:31-37] |
| `scope_params` | function | `fn scope_params(&self) -> (String, String, Option<String>, Option<String>) {` | `scope_params [function]` | `440893f1-b63d-5df8-968e-49b1acfcee31` | 39-46 [crates/gwiki/src/store/postgres.rs:39-46] | Indexed function `scope_params` in `crates/gwiki/src/store/postgres.rs`. [crates/gwiki/src/store/postgres.rs:39-46] |
| `document_meta` | function | `fn document_meta(&mut self, path: &Path) -> Result<DocumentMeta, StoreError> {` | `document_meta [function]` | `eb7905c0-edac-5745-b2d1-ffdb910f6898` | 48-75 [crates/gwiki/src/store/postgres.rs:48-75] | Indexed function `document_meta` in `crates/gwiki/src/store/postgres.rs`. [crates/gwiki/src/store/postgres.rs:48-75] |
| `indexed_hashes` | function | `fn indexed_hashes(&mut self) -> Result<BTreeMap<PathBuf, String>, StoreError> {` | `indexed_hashes [function]` | `5dcfb813-96ec-5bef-bb30-938ea6711c8c` | 79-95 [crates/gwiki/src/store/postgres.rs:79-95] | Indexed function `indexed_hashes` in `crates/gwiki/src/store/postgres.rs`. [crates/gwiki/src/store/postgres.rs:79-95] |
| `upsert_document` | function | `fn upsert_document(&mut self, document: WikiDocument) -> Result<(), StoreError> {` | `upsert_document [function]` | `779e2c92-0acd-57ae-a3d9-e245cfd62ad9` | 97-153 [crates/gwiki/src/store/postgres.rs:97-153] | Indexed function `upsert_document` in `crates/gwiki/src/store/postgres.rs`. [crates/gwiki/src/store/postgres.rs:97-153] |
| `replace_chunks` | function | `fn replace_chunks(&mut self, path: &Path, chunks: Vec<WikiChunk>) -> Result<(), StoreError> {` | `replace_chunks [function]` | `5de7a549-abee-579a-aafe-34062356486c` | 155-251 [crates/gwiki/src/store/postgres.rs:155-251] | Indexed function `replace_chunks` in `crates/gwiki/src/store/postgres.rs`. [crates/gwiki/src/store/postgres.rs:155-251] |
| `replace_links` | function | `fn replace_links(&mut self, path: &Path, links: Vec<WikiLink>) -> Result<(), StoreError> {` | `replace_links [function]` | `519dbccf-25a4-5c1a-81d4-c97eac28d0bc` | 253-322 [crates/gwiki/src/store/postgres.rs:253-322] | Indexed function `replace_links` in `crates/gwiki/src/store/postgres.rs`. [crates/gwiki/src/store/postgres.rs:253-322] |
| `upsert_source` | function | `fn upsert_source(&mut self, source: WikiSource) -> Result<(), StoreError> {` | `upsert_source [function]` | `b2c0144e-822a-54a1-8545-316046cdb22d` | 324-368 [crates/gwiki/src/store/postgres.rs:324-368] | Indexed function `upsert_source` in `crates/gwiki/src/store/postgres.rs`. [crates/gwiki/src/store/postgres.rs:324-368] |
| `record_ingestion` | function | `fn record_ingestion(&mut self, ingestion: WikiIngestion) -> Result<(), StoreError> {` | `record_ingestion [function]` | `90d9507c-2a45-53bf-8885-6b996c1cdfcb` | 370-415 [crates/gwiki/src/store/postgres.rs:370-415] | Indexed function `record_ingestion` in `crates/gwiki/src/store/postgres.rs`. [crates/gwiki/src/store/postgres.rs:370-415] |
| `record_file_hash` | function | `fn record_file_hash(` | `record_file_hash [function]` | `8e8d1d2e-a409-5aa5-9a5e-a490b1257108` | 417-424 [crates/gwiki/src/store/postgres.rs:417-424] | Indexed function `record_file_hash` in `crates/gwiki/src/store/postgres.rs`. [crates/gwiki/src/store/postgres.rs:417-424] |
| `delete_derived_rows` | function | `fn delete_derived_rows(&mut self, path: &Path) -> Result<(), StoreError> {` | `delete_derived_rows [function]` | `956bbf09-d81b-5ca3-bec2-01022cab0dc7` | 426-451 [crates/gwiki/src/store/postgres.rs:426-451] | Indexed function `delete_derived_rows` in `crates/gwiki/src/store/postgres.rs`. [crates/gwiki/src/store/postgres.rs:426-451] |
