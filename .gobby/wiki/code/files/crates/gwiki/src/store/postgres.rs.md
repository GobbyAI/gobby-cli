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

# crates/gwiki/src/store/postgres.rs

Module: [[code/modules/crates/gwiki/src/store|crates/gwiki/src/store]]

## Purpose

This file implements a PostgreSQL-backed `WikiIndexStore` for a scoped wiki, centered on a `PostgresWikiStore` wrapper around a mutable `postgres::Client` plus an in-memory cache of document metadata. It resolves scope parameters and document metadata, using the cache first and falling back to `gwiki_documents` when needed, then exposes operations to list indexed hashes and upsert documents, sources, and ingestions. It also manages derived content atomically: chunks and links are replaced in transactions, file-hash recording is a no-op because that state lives in Postgres, and deleting a document removes all related rows from the database and the local index.
[crates/gwiki/src/store/postgres.rs:18-22]
[crates/gwiki/src/store/postgres.rs:24-28]
[crates/gwiki/src/store/postgres.rs:31-37]
[crates/gwiki/src/store/postgres.rs:39-46]
[crates/gwiki/src/store/postgres.rs:48-75]

## API Symbols

- `DocumentMeta` (class) component `DocumentMeta [class]` (`dd3cf6fd-b416-5b98-bfc6-8cc64c666857`) lines 18-22 [crates/gwiki/src/store/postgres.rs:18-22]
  - Signature: `struct DocumentMeta {`
  - Purpose: 'DocumentMeta' is a struct that stores three string fields identifying a document ('id'), its origin category ('source_kind'), and a checksum or fingerprint of its contents ('content_hash'). [crates/gwiki/src/store/postgres.rs:18-22]
- `PostgresWikiStore` (class) component `PostgresWikiStore [class]` (`93c4fb76-5399-5f16-b669-ce57e18ffba3`) lines 24-28 [crates/gwiki/src/store/postgres.rs:24-28]
  - Signature: `pub struct PostgresWikiStore<'a> {`
  - Purpose: 'PostgresWikiStore<'a>' is a mutable, lifetime-bound wrapper around a 'postgres::Client' that tracks a 'WikiStoreScope' and an in-memory 'BTreeMap<PathBuf, DocumentMeta>' index of documents. [crates/gwiki/src/store/postgres.rs:24-28]
- `new` (function) component `new [function]` (`00be2b94-0b3b-55b2-a0e6-1a96870b19c2`) lines 31-37 [crates/gwiki/src/store/postgres.rs:31-37]
  - Signature: `pub fn new(conn: &'a mut ::postgres::Client, scope: WikiStoreScope) -> Self {`
  - Purpose: Constructs a new instance by storing the provided mutable 'postgres::Client' reference and 'WikiStoreScope', and initializing 'documents' to an empty 'BTreeMap'. [crates/gwiki/src/store/postgres.rs:31-37]
- `scope_params` (function) component `scope_params [function]` (`440893f1-b63d-5df8-968e-49b1acfcee31`) lines 39-46 [crates/gwiki/src/store/postgres.rs:39-46]
  - Signature: `fn scope_params(&self) -> (String, String, Option<String>, Option<String>) {`
  - Purpose: Returns a 4-tuple containing the scope kind and scope ID as strings, plus the optional project ID and topic name from 'self.scope'. [crates/gwiki/src/store/postgres.rs:39-46]
- `document_meta` (function) component `document_meta [function]` (`eb7905c0-edac-5745-b2d1-ffdb910f6898`) lines 48-75 [crates/gwiki/src/store/postgres.rs:48-75]
  - Signature: `fn document_meta(&mut self, path: &Path) -> Result<DocumentMeta, StoreError> {`
  - Purpose: Looks up a document’s 'DocumentMeta' from the in-memory cache or, on a cache miss, queries 'gwiki_documents' by current scope and path, returns 'InvalidData' if absent, caches the retrieved metadata, and clones it to the caller. [crates/gwiki/src/store/postgres.rs:48-75]
- `indexed_hashes` (function) component `indexed_hashes [function]` (`5dcfb813-96ec-5bef-bb30-938ea6711c8c`) lines 79-95 [crates/gwiki/src/store/postgres.rs:79-95]
  - Signature: `fn indexed_hashes(&mut self) -> Result<BTreeMap<PathBuf, String>, StoreError> {`
  - Purpose: Queries 'gwiki_documents' for the current scope’s 'path' and 'content_hash' rows, converts each stored path string into a 'PathBuf', and returns them collected into a 'BTreeMap<PathBuf, String>'. [crates/gwiki/src/store/postgres.rs:79-95]
- `upsert_document` (function) component `upsert_document [function]` (`779e2c92-0acd-57ae-a3d9-e245cfd62ad9`) lines 97-153 [crates/gwiki/src/store/postgres.rs:97-153]
  - Signature: `fn upsert_document(&mut self, document: WikiDocument) -> Result<(), StoreError> {`
  - Purpose: Upserts a 'WikiDocument' into 'gwiki_documents' by computing its scoped ID and metadata, inserting a new row or updating the existing row matched on '(scope_kind, scope_id, path)' with refreshed document fields and timestamps. [crates/gwiki/src/store/postgres.rs:97-153]
- `replace_chunks` (function) component `replace_chunks [function]` (`5de7a549-abee-579a-aafe-34062356486c`) lines 155-251 [crates/gwiki/src/store/postgres.rs:155-251]
  - Signature: `fn replace_chunks(&mut self, path: &Path, chunks: Vec<WikiChunk>) -> Result<(), StoreError> {`
  - Purpose: Validates the supplied chunks for 'path', converts chunk indices to PostgreSQL 'INTEGER', and in a single transaction deletes all existing 'gwiki_chunks' rows for that scoped path before inserting the new chunks (or committing the deletion if the list is empty). [crates/gwiki/src/store/postgres.rs:155-251]
- `replace_links` (function) component `replace_links [function]` (`519dbccf-25a4-5c1a-81d4-c97eac28d0bc`) lines 253-322 [crates/gwiki/src/store/postgres.rs:253-322]
  - Signature: `fn replace_links(&mut self, path: &Path, links: Vec<WikiLink>) -> Result<(), StoreError> {`
  - Purpose: Replaces all stored wiki-link records for the given 'path' within the current scope by validating the links, deleting existing rows, and inserting the new links in a transaction with conflict-updating upserts and rollback on failure. [crates/gwiki/src/store/postgres.rs:253-322]
- `upsert_source` (function) component `upsert_source [function]` (`b2c0144e-822a-54a1-8545-316046cdb22d`) lines 324-368 [crates/gwiki/src/store/postgres.rs:324-368]
  - Signature: `fn upsert_source(&mut self, source: WikiSource) -> Result<(), StoreError> {`
  - Purpose: Inserts a 'WikiSource' into 'gwiki_sources' with scope-derived identifiers and metadata, or atomically updates the existing row on '(scope_kind, scope_id, document_path)' conflict by replacing its fields and refreshing 'captured_at'. [crates/gwiki/src/store/postgres.rs:324-368]
- `record_ingestion` (function) component `record_ingestion [function]` (`90d9507c-2a45-53bf-8885-6b996c1cdfcb`) lines 370-415 [crates/gwiki/src/store/postgres.rs:370-415]
  - Signature: `fn record_ingestion(&mut self, ingestion: WikiIngestion) -> Result<(), StoreError> {`
  - Purpose: 'record_ingestion' computes a scoped ingestion ID and metadata from a 'WikiIngestion', then upserts a corresponding row into 'gwiki_ingestions' with the current timestamp, updating the stored project, topic, source kind, content hash, frontmatter, provenance, and status on conflict. [crates/gwiki/src/store/postgres.rs:370-415]
- `record_file_hash` (function) component `record_file_hash [function]` (`8e8d1d2e-a409-5aa5-9a5e-a490b1257108`) lines 417-424 [crates/gwiki/src/store/postgres.rs:417-424]
  - Signature: `fn record_file_hash(`
  - Purpose: No-op method that accepts a file path and content hash and returns 'Ok(())', with file-hash persistence delegated to PostgreSQL via 'upsert_document'. [crates/gwiki/src/store/postgres.rs:417-424]
- `delete_derived_rows` (function) component `delete_derived_rows [function]` (`956bbf09-d81b-5ca3-bec2-01022cab0dc7`) lines 426-451 [crates/gwiki/src/store/postgres.rs:426-451]
  - Signature: `fn delete_derived_rows(&mut self, path: &Path) -> Result<(), StoreError> {`
  - Purpose: Deletes all database rows derived from the given document path across 'gwiki_chunks', 'gwiki_links', 'gwiki_sources', and 'gwiki_documents' within the current scope in a single transaction, then removes the document from the in-memory index. [crates/gwiki/src/store/postgres.rs:426-451]

