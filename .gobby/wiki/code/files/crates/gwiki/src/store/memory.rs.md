---
title: crates/gwiki/src/store/memory.rs
type: code_file
provenance:
- file: crates/gwiki/src/store/memory.rs
  ranges:
  - 16-28
  - 30-81
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/store/memory.rs

Module: [[code/modules/crates/gwiki/src/store|crates/gwiki/src/store]]

## Purpose

This file implements `MemoryWikiStore`, an in-memory `WikiIndexStore` used by local shell commands and tests. It keeps wiki state in `BTreeMap`s and vectors for documents, chunks, links, sources, file hashes, ingestions, and deleted paths, while also tracking simple counters for how often each kind of write happens. The trait methods mostly clone or insert data into those collections, validate chunk and link paths before replacing derived rows, record ingestion and file-hash metadata, and handle deletion of derived data for a path.
[crates/gwiki/src/store/memory.rs:16-28]
[crates/gwiki/src/store/memory.rs:30-81]
[crates/gwiki/src/store/memory.rs:31-33]
[crates/gwiki/src/store/memory.rs:35-39]
[crates/gwiki/src/store/memory.rs:41-46]

## API Symbols

- `MemoryWikiStore` (class) component `MemoryWikiStore [class]` (`471ad5cd-38e5-5097-8647-346a22f56acb`) lines 16-28 [crates/gwiki/src/store/memory.rs:16-28]
  - Signature: `pub struct MemoryWikiStore {`
  - Purpose: Indexed class `MemoryWikiStore` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:16-28]
- `MemoryWikiStore` (class) component `MemoryWikiStore [class]` (`aa6230aa-f886-533c-bb2d-925417bebe1f`) lines 30-81 [crates/gwiki/src/store/memory.rs:30-81]
  - Signature: `impl WikiIndexStore for MemoryWikiStore {`
  - Purpose: Indexed class `MemoryWikiStore` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:30-81]
- `MemoryWikiStore.indexed_hashes` (method) component `MemoryWikiStore.indexed_hashes [method]` (`99513529-e0df-5c0e-b6b0-605370d5c4ef`) lines 31-33 [crates/gwiki/src/store/memory.rs:31-33]
  - Signature: `fn indexed_hashes(&mut self) -> Result<BTreeMap<PathBuf, String>, StoreError> {`
  - Purpose: Indexed method `MemoryWikiStore.indexed_hashes` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:31-33]
- `MemoryWikiStore.upsert_document` (method) component `MemoryWikiStore.upsert_document [method]` (`c2fb8efe-0517-50e0-be53-75578a31734b`) lines 35-39 [crates/gwiki/src/store/memory.rs:35-39]
  - Signature: `fn upsert_document(&mut self, document: WikiDocument) -> Result<(), StoreError> {`
  - Purpose: Indexed method `MemoryWikiStore.upsert_document` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:35-39]
- `MemoryWikiStore.replace_chunks` (method) component `MemoryWikiStore.replace_chunks [method]` (`07647b82-41b2-57bc-b8cf-f313cdd6fbe4`) lines 41-46 [crates/gwiki/src/store/memory.rs:41-46]
  - Signature: `fn replace_chunks(&mut self, path: &Path, chunks: Vec<WikiChunk>) -> Result<(), StoreError> {`
  - Purpose: Indexed method `MemoryWikiStore.replace_chunks` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:41-46]
- `MemoryWikiStore.replace_links` (method) component `MemoryWikiStore.replace_links [method]` (`1e428d30-f1e7-559f-a668-371a41acc996`) lines 48-53 [crates/gwiki/src/store/memory.rs:48-53]
  - Signature: `fn replace_links(&mut self, path: &Path, links: Vec<WikiLink>) -> Result<(), StoreError> {`
  - Purpose: Indexed method `MemoryWikiStore.replace_links` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:48-53]
- `MemoryWikiStore.upsert_source` (method) component `MemoryWikiStore.upsert_source [method]` (`549f7764-1f18-5f91-8f6f-5678bfa40d64`) lines 55-59 [crates/gwiki/src/store/memory.rs:55-59]
  - Signature: `fn upsert_source(&mut self, source: WikiSource) -> Result<(), StoreError> {`
  - Purpose: Indexed method `MemoryWikiStore.upsert_source` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:55-59]
- `MemoryWikiStore.record_ingestion` (method) component `MemoryWikiStore.record_ingestion [method]` (`a7cca8e5-67d1-5ae8-85cb-495919abcfba`) lines 61-64 [crates/gwiki/src/store/memory.rs:61-64]
  - Signature: `fn record_ingestion(&mut self, ingestion: WikiIngestion) -> Result<(), StoreError> {`
  - Purpose: Indexed method `MemoryWikiStore.record_ingestion` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:61-64]
- `MemoryWikiStore.record_file_hash` (method) component `MemoryWikiStore.record_file_hash [method]` (`612e1196-d61f-50ff-968e-d285169c514e`) lines 66-69 [crates/gwiki/src/store/memory.rs:66-69]
  - Signature: `fn record_file_hash(&mut self, path: PathBuf, content_hash: String) -> Result<(), StoreError> {`
  - Purpose: Indexed method `MemoryWikiStore.record_file_hash` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:66-69]
- `MemoryWikiStore.delete_derived_rows` (method) component `MemoryWikiStore.delete_derived_rows [method]` (`682f720c-3ac7-5cea-b1a2-700d8c2c1f86`) lines 71-80 [crates/gwiki/src/store/memory.rs:71-80]
  - Signature: `fn delete_derived_rows(&mut self, path: &Path) -> Result<(), StoreError> {`
  - Purpose: Indexed method `MemoryWikiStore.delete_derived_rows` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:71-80]

