---
title: crates/gwiki/src/support/search.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/search.rs
  ranges:
  - 11-13
  - 16-21
  - '24'
  - 27-38
  - 41-43
  - 46-51
  - 53-57
  - 60-161
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/support/search.rs:11-13](crates/gwiki/src/support/search.rs#L11-L13), [crates/gwiki/src/support/search.rs:16-21](crates/gwiki/src/support/search.rs#L16-L21), [crates/gwiki/src/support/search.rs:24](crates/gwiki/src/support/search.rs#L24), [crates/gwiki/src/support/search.rs:27-38](crates/gwiki/src/support/search.rs#L27-L38), [crates/gwiki/src/support/search.rs:41-43](crates/gwiki/src/support/search.rs#L41-L43), [crates/gwiki/src/support/search.rs:46-51](crates/gwiki/src/support/search.rs#L46-L51), [crates/gwiki/src/support/search.rs:53-57](crates/gwiki/src/support/search.rs#L53-L57), [crates/gwiki/src/support/search.rs:60-161](crates/gwiki/src/support/search.rs#L60-L161)

</details>

# crates/gwiki/src/support/search.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file provides support implementations for the wiki search pipeline. It includes a BM25 backend that simply returns precomputed store hits up to the requested limit, a semantic backend placeholder that always returns no results with a `qdrant` not-configured degradation, and a `PostgresConfigSource` adapter that reads and resolves config values from a PostgreSQL client. The `store_search_hits` helper ties the store side together by tokenizing the query, rejecting empty queries, scanning in-memory documents, filtering and scoring them with the shared text helpers, and assembling ranked `WikiSearchResult` values.
[crates/gwiki/src/support/search.rs:11-13]
[crates/gwiki/src/support/search.rs:16-21]
[crates/gwiki/src/support/search.rs:24]
[crates/gwiki/src/support/search.rs:27-38]
[crates/gwiki/src/support/search.rs:41-43]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `StoreBm25Backend` | class | `pub(crate) struct StoreBm25Backend {` | `StoreBm25Backend [class]` | `57275bba-d082-54ff-b944-52fdd9f97c05` | 11-13 [crates/gwiki/src/support/search.rs:11-13] | Indexed class `StoreBm25Backend` in `crates/gwiki/src/support/search.rs`. [crates/gwiki/src/support/search.rs:11-13] |
| `StoreBm25Backend::search_bm25` | method | `fn search_bm25(` | `StoreBm25Backend::search_bm25 [method]` | `1f0c3d0f-f271-5426-a656-c12b82843f34` | 16-21 [crates/gwiki/src/support/search.rs:16-21] | Indexed method `StoreBm25Backend::search_bm25` in `crates/gwiki/src/support/search.rs`. [crates/gwiki/src/support/search.rs:16-21] |
| `UnavailableSemanticBackend` | class | `pub(crate) struct UnavailableSemanticBackend;` | `UnavailableSemanticBackend [class]` | `0ab4dcb5-bbbc-51a8-b5ef-972b072e1658` | 24-24 [crates/gwiki/src/support/search.rs:24] | Indexed class `UnavailableSemanticBackend` in `crates/gwiki/src/support/search.rs`. [crates/gwiki/src/support/search.rs:24] |
| `UnavailableSemanticBackend::search_semantic` | method | `fn search_semantic(` | `UnavailableSemanticBackend::search_semantic [method]` | `15803901-4cc1-572d-a4ba-7110dfe6fe1a` | 27-38 [crates/gwiki/src/support/search.rs:27-38] | Indexed method `UnavailableSemanticBackend::search_semantic` in `crates/gwiki/src/support/search.rs`. [crates/gwiki/src/support/search.rs:27-38] |
| `PostgresConfigSource` | class | `pub(crate) struct PostgresConfigSource<'a> {` | `PostgresConfigSource [class]` | `7c1fea1d-963a-5541-9f57-2744e8bb5f8d` | 41-43 [crates/gwiki/src/support/search.rs:41-43] | Indexed class `PostgresConfigSource` in `crates/gwiki/src/support/search.rs`. [crates/gwiki/src/support/search.rs:41-43] |
| `config_value` | function | `fn config_value(&mut self, key: &str) -> Option<String> {` | `config_value [function]` | `2325a736-cca6-5936-9f50-8c4900f9f802` | 46-51 [crates/gwiki/src/support/search.rs:46-51] | Indexed function `config_value` in `crates/gwiki/src/support/search.rs`. [crates/gwiki/src/support/search.rs:46-51] |
| `resolve_value` | function | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `resolve_value [function]` | `70142db5-bd7d-559f-b313-2ac7ee7cb55b` | 53-57 [crates/gwiki/src/support/search.rs:53-57] | Indexed function `resolve_value` in `crates/gwiki/src/support/search.rs`. [crates/gwiki/src/support/search.rs:53-57] |
| `store_search_hits` | function | `pub(crate) fn store_search_hits(` | `store_search_hits [function]` | `23d15dc3-e88a-5fc5-8acf-a92884afbccf` | 60-161 [crates/gwiki/src/support/search.rs:60-161] | Indexed function `store_search_hits` in `crates/gwiki/src/support/search.rs`. [crates/gwiki/src/support/search.rs:60-161] |
