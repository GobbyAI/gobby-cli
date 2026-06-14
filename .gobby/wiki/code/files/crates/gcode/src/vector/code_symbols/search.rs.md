---
title: crates/gcode/src/vector/code_symbols/search.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/search.rs
  ranges:
  - 8-14
  - 16-26
  - '28'
  - 30-58
  - 63-81
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols/search.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

This file defines the error type and search entrypoints for vector-based code-symbol lookup. `SearchError` captures missing Qdrant or embedding configuration, query-embedding failure, invalid collection naming, and vector-search transport errors, with `Display` and `Error` implementations for human-readable reporting.

`search_code_symbols` is the core fallible path: it pulls Qdrant and embedding settings from `Context`, embeds the query, builds the target collection name, runs a Qdrant vector search, and converts raw `(symbol_id, score)` pairs into `CodeSymbolVectorSearchHit` values. `semantic_search` wraps that behavior as a degraded semantic-ranking signal, returning results up to the requested limit while logging errors and falling back to an empty list on failure.
[crates/gcode/src/vector/code_symbols/search.rs:8-14]
[crates/gcode/src/vector/code_symbols/search.rs:16-26]
[crates/gcode/src/vector/code_symbols/search.rs:17-25]
[crates/gcode/src/vector/code_symbols/search.rs:28]
[crates/gcode/src/vector/code_symbols/search.rs:30-58]

## API Symbols

- `SearchError` (type) component `SearchError [type]` (`ca2cca63-43fb-5fcd-8465-ad658533af84`) lines 8-14 [crates/gcode/src/vector/code_symbols/search.rs:8-14]
  - Signature: `pub enum SearchError {`
  - Purpose: Indexed type `SearchError` in `crates/gcode/src/vector/code_symbols/search.rs`. [crates/gcode/src/vector/code_symbols/search.rs:8-14]
- `SearchError` (class) component `SearchError [class]` (`8bec6f02-0521-5397-b923-f7c761c22b69`) lines 16-26 [crates/gcode/src/vector/code_symbols/search.rs:16-26]
  - Signature: `impl std::fmt::Display for SearchError {`
  - Purpose: This `Display` trait implementation converts five `SearchError` enum variants (configuration missing, embedding failures, and vector search errors) into human-readable error messages for formatted output. [crates/gcode/src/vector/code_symbols/search.rs:16-26]
- `SearchError.fmt` (method) component `SearchError.fmt [method]` (`f436a18c-8cf7-5b9e-9e4a-e27b807cf9ab`) lines 17-25 [crates/gcode/src/vector/code_symbols/search.rs:17-25]
  - Signature: `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
  - Purpose: Implements the `Display` trait's `fmt` method for an error enum, pattern-matching on self to write variant-specific error messages to the provided formatter. [crates/gcode/src/vector/code_symbols/search.rs:17-25]
- `SearchError` (class) component `SearchError [class]` (`e966272b-cde9-5967-b74e-45ad9acd3bd8`) lines 28-28 [crates/gcode/src/vector/code_symbols/search.rs:28]
  - Signature: `impl std::error::Error for SearchError {}`
  - Purpose: SearchError is a type that implements the standard Rust `std::error::Error` trait with no additional custom methods or behavior. [crates/gcode/src/vector/code_symbols/search.rs:28]
- `search_code_symbols` (function) component `search_code_symbols [function]` (`003db78b-65f7-5705-8c3f-72c5bf727909`) lines 30-58 [crates/gcode/src/vector/code_symbols/search.rs:30-58]
  - Signature: `pub fn search_code_symbols(`
  - Purpose: Searches a Qdrant vector collection for code symbols semantically similar to an embedded query, returning scored hits. [crates/gcode/src/vector/code_symbols/search.rs:30-58]
- `semantic_search` (function) component `semantic_search [function]` (`9f88a5e7-6c65-506a-b878-616b591cf929`) lines 63-81 [crates/gcode/src/vector/code_symbols/search.rs:63-81]
  - Signature: `pub fn semantic_search(ctx: &Context, query: &str, limit: usize) -> Vec<(String, f64)> {`
  - Purpose: Performs a vector-based semantic search on code symbols and returns up to `limit` results as (symbol_id, relevance_score) tuples, with errors logged and handled by returning an empty vector. [crates/gcode/src/vector/code_symbols/search.rs:63-81]

