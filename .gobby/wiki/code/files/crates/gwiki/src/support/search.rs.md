---
title: crates/gwiki/src/support/search.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/search.rs
  ranges:
  - 11-13
  - 15-22
  - 16-21
  - '24'
  - 26-39
  - 27-38
  - 41-43
  - 46-51
  - 53-57
  - 60-161
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/search.rs

Module: [[code/modules/crates/gwiki/src/support|crates/gwiki/src/support]]

## Purpose

`crates/gwiki/src/support/search.rs` exposes 10 indexed API symbols.
[crates/gwiki/src/support/search.rs:11-13]
[crates/gwiki/src/support/search.rs:15-22]
[crates/gwiki/src/support/search.rs:16-21]
[crates/gwiki/src/support/search.rs:24]
[crates/gwiki/src/support/search.rs:26-39]

## API Symbols

- `StoreBm25Backend` (class) component `StoreBm25Backend [class]` (`57275bba-d082-54ff-b944-52fdd9f97c05`) lines 11-13 [crates/gwiki/src/support/search.rs:11-13]
  - Signature: `pub(crate) struct StoreBm25Backend {`
  - Purpose: StoreBm25Backend is a crate-private struct that holds an atomic reference-counted slice of WikiSearchResult objects representing BM25 search hits. [crates/gwiki/src/support/search.rs:11-13]
- `StoreBm25Backend` (class) component `StoreBm25Backend [class]` (`8eb2ef98-3345-5b48-b9ce-625bdc330f44`) lines 15-22 [crates/gwiki/src/support/search.rs:15-22]
  - Signature: `impl search::bm25::Bm25SearchBackend for StoreBm25Backend {`
  - Purpose: StoreBm25Backend implements the Bm25SearchBackend trait to return a limited slice of pre-computed search hits from an internal collection, truncated to the requested limit. [crates/gwiki/src/support/search.rs:15-22]
- `StoreBm25Backend.search_bm25` (method) component `StoreBm25Backend.search_bm25 [method]` (`1f0c3d0f-f271-5426-a656-c12b82843f34`) lines 16-21 [crates/gwiki/src/support/search.rs:16-21]
  - Signature: `fn search_bm25(`
  - Purpose: Returns a `Result` containing a vector of up to `request.limit` cloned `WikiSearchResult` items from an internal `hits` collection. [crates/gwiki/src/support/search.rs:16-21]
- `UnavailableSemanticBackend` (class) component `UnavailableSemanticBackend [class]` (`0ab4dcb5-bbbc-51a8-b5ef-972b072e1658`) lines 24-24 [crates/gwiki/src/support/search.rs:24]
  - Signature: `pub(crate) struct UnavailableSemanticBackend;`
  - Purpose: `UnavailableSemanticBackend` is a crate-private unit struct that serves as a sentinel type indicating the absence of semantic backend functionality. [crates/gwiki/src/support/search.rs:24]
- `UnavailableSemanticBackend` (class) component `UnavailableSemanticBackend [class]` (`4f1ae42c-5d04-5187-8aec-95d9b9af2b9d`) lines 26-39 [crates/gwiki/src/support/search.rs:26-39]
  - Signature: `impl search::semantic::SemanticSearchBackend for UnavailableSemanticBackend {`
  - Purpose: `UnavailableSemanticBackend` is a stub implementation of `SemanticSearchBackend` that always returns empty search results with a `ServiceUnavailable` degradation status indicating Qdrant is not configured. [crates/gwiki/src/support/search.rs:26-39]
- `UnavailableSemanticBackend.search_semantic` (method) component `UnavailableSemanticBackend.search_semantic [method]` (`15803901-4cc1-572d-a4ba-7110dfe6fe1a`) lines 27-38 [crates/gwiki/src/support/search.rs:27-38]
  - Signature: `fn search_semantic(`
  - Purpose: This method returns a `SemanticSearchOutcome` with empty hits and a `ServiceUnavailable` degradation status, indicating the Qdrant semantic search service is not configured. [crates/gwiki/src/support/search.rs:27-38]
- `PostgresConfigSource` (class) component `PostgresConfigSource [class]` (`7c1fea1d-963a-5541-9f57-2744e8bb5f8d`) lines 41-43 [crates/gwiki/src/support/search.rs:41-43]
  - Signature: `pub(crate) struct PostgresConfigSource<'a> {`
  - Purpose: `PostgresConfigSource` is a lifetime-parameterized, crate-scoped struct that wraps a mutable reference to a PostgreSQL database client for configuration sourcing. [crates/gwiki/src/support/search.rs:41-43]
- `config_value` (function) component `config_value [function]` (`2325a736-cca6-5936-9f50-8c4900f9f802`) lines 46-51 [crates/gwiki/src/support/search.rs:46-51]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Retrieves a configuration value from PostgreSQL for the given key, decodes it from raw format, and returns `Option<String>`. [crates/gwiki/src/support/search.rs:46-51]
- `resolve_value` (function) component `resolve_value [function]` (`70142db5-bd7d-559f-b313-2ac7ee7cb55b`) lines 53-57 [crates/gwiki/src/support/search.rs:53-57]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Resolves encrypted secret references (prefixed with `$secret:`) in configuration values through shared CLI-side Fernet decryption. [crates/gwiki/src/support/search.rs:53-57]
- `store_search_hits` (function) component `store_search_hits [function]` (`23d15dc3-e88a-5fc5-8acf-a92884afbccf`) lines 60-161 [crates/gwiki/src/support/search.rs:60-161]
  - Signature: `pub(crate) fn store_search_hits(`
  - Purpose: Performs BM25-based keyword search on a wiki document store, scoring and ranking documents by query token relevance and returning WikiSearchResult objects. [crates/gwiki/src/support/search.rs:60-161]

