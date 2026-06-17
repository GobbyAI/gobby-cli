---
title: crates/gwiki/src/store/memory.rs
type: code_file
provenance:
- file: crates/gwiki/src/store/memory.rs
  ranges:
  - 16-28
  - 31-33
  - 35-39
  - 41-46
  - 48-53
  - 55-59
  - 61-64
  - 66-69
  - 71-80
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/store/memory.rs:16-28](crates/gwiki/src/store/memory.rs#L16-L28), [crates/gwiki/src/store/memory.rs:31-33](crates/gwiki/src/store/memory.rs#L31-L33), [crates/gwiki/src/store/memory.rs:35-39](crates/gwiki/src/store/memory.rs#L35-L39), [crates/gwiki/src/store/memory.rs:41-46](crates/gwiki/src/store/memory.rs#L41-L46), [crates/gwiki/src/store/memory.rs:48-53](crates/gwiki/src/store/memory.rs#L48-L53), [crates/gwiki/src/store/memory.rs:55-59](crates/gwiki/src/store/memory.rs#L55-L59), [crates/gwiki/src/store/memory.rs:61-64](crates/gwiki/src/store/memory.rs#L61-L64), [crates/gwiki/src/store/memory.rs:66-69](crates/gwiki/src/store/memory.rs#L66-L69), [crates/gwiki/src/store/memory.rs:71-80](crates/gwiki/src/store/memory.rs#L71-L80)

</details>

# crates/gwiki/src/store/memory.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/store/memory.rs` defines `MemoryWikiStore`, an in-memory `WikiIndexStore` implementation used by local shell commands and tests. It keeps indexed wiki state in `BTreeMap`s and `Vec`s for documents, chunks, links, sources, file hashes, ingestions, and deleted paths, while also tracking how many document, chunk, link, and source writes have occurred. Its methods either return cloned hash state or mutate these collections by upserting documents/sources, replacing chunks/links after validating their paths, recording ingestions and file hashes, and deleting derived rows for a path.
[crates/gwiki/src/store/memory.rs:16-28]
[crates/gwiki/src/store/memory.rs:31-33]
[crates/gwiki/src/store/memory.rs:35-39]
[crates/gwiki/src/store/memory.rs:41-46]
[crates/gwiki/src/store/memory.rs:48-53]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `MemoryWikiStore` | class | `pub struct MemoryWikiStore {` | `MemoryWikiStore [class]` | `471ad5cd-38e5-5097-8647-346a22f56acb` | 16-28 [crates/gwiki/src/store/memory.rs:16-28] | Indexed class `MemoryWikiStore` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:16-28] |
| `MemoryWikiStore::indexed_hashes` | method | `fn indexed_hashes(&mut self) -> Result<BTreeMap<PathBuf, String>, StoreError> {` | `MemoryWikiStore::indexed_hashes [method]` | `99513529-e0df-5c0e-b6b0-605370d5c4ef` | 31-33 [crates/gwiki/src/store/memory.rs:31-33] | Indexed method `MemoryWikiStore::indexed_hashes` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:31-33] |
| `MemoryWikiStore::upsert_document` | method | `fn upsert_document(&mut self, document: WikiDocument) -> Result<(), StoreError> {` | `MemoryWikiStore::upsert_document [method]` | `c2fb8efe-0517-50e0-be53-75578a31734b` | 35-39 [crates/gwiki/src/store/memory.rs:35-39] | Indexed method `MemoryWikiStore::upsert_document` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:35-39] |
| `MemoryWikiStore::replace_chunks` | method | `fn replace_chunks(&mut self, path: &Path, chunks: Vec<WikiChunk>) -> Result<(), StoreError> {` | `MemoryWikiStore::replace_chunks [method]` | `07647b82-41b2-57bc-b8cf-f313cdd6fbe4` | 41-46 [crates/gwiki/src/store/memory.rs:41-46] | Indexed method `MemoryWikiStore::replace_chunks` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:41-46] |
| `MemoryWikiStore::replace_links` | method | `fn replace_links(&mut self, path: &Path, links: Vec<WikiLink>) -> Result<(), StoreError> {` | `MemoryWikiStore::replace_links [method]` | `1e428d30-f1e7-559f-a668-371a41acc996` | 48-53 [crates/gwiki/src/store/memory.rs:48-53] | Indexed method `MemoryWikiStore::replace_links` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:48-53] |
| `MemoryWikiStore::upsert_source` | method | `fn upsert_source(&mut self, source: WikiSource) -> Result<(), StoreError> {` | `MemoryWikiStore::upsert_source [method]` | `549f7764-1f18-5f91-8f6f-5678bfa40d64` | 55-59 [crates/gwiki/src/store/memory.rs:55-59] | Indexed method `MemoryWikiStore::upsert_source` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:55-59] |
| `MemoryWikiStore::record_ingestion` | method | `fn record_ingestion(&mut self, ingestion: WikiIngestion) -> Result<(), StoreError> {` | `MemoryWikiStore::record_ingestion [method]` | `a7cca8e5-67d1-5ae8-85cb-495919abcfba` | 61-64 [crates/gwiki/src/store/memory.rs:61-64] | Indexed method `MemoryWikiStore::record_ingestion` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:61-64] |
| `MemoryWikiStore::record_file_hash` | method | `fn record_file_hash(&mut self, path: PathBuf, content_hash: String) -> Result<(), StoreError> {` | `MemoryWikiStore::record_file_hash [method]` | `612e1196-d61f-50ff-968e-d285169c514e` | 66-69 [crates/gwiki/src/store/memory.rs:66-69] | Indexed method `MemoryWikiStore::record_file_hash` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:66-69] |
| `MemoryWikiStore::delete_derived_rows` | method | `fn delete_derived_rows(&mut self, path: &Path) -> Result<(), StoreError> {` | `MemoryWikiStore::delete_derived_rows [method]` | `682f720c-3ac7-5cea-b1a2-700d8c2c1f86` | 71-80 [crates/gwiki/src/store/memory.rs:71-80] | Indexed method `MemoryWikiStore::delete_derived_rows` in `crates/gwiki/src/store/memory.rs`. [crates/gwiki/src/store/memory.rs:71-80] |
