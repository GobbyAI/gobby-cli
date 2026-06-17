---
title: crates/gcode/src/vector/code_symbols/search.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/search.rs
  ranges:
  - 8-14
  - 17-25
  - 30-58
  - 63-81
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/vector/code_symbols/search.rs:8-14](crates/gcode/src/vector/code_symbols/search.rs#L8-L14), [crates/gcode/src/vector/code_symbols/search.rs:17-25](crates/gcode/src/vector/code_symbols/search.rs#L17-L25), [crates/gcode/src/vector/code_symbols/search.rs:30-58](crates/gcode/src/vector/code_symbols/search.rs#L30-L58), [crates/gcode/src/vector/code_symbols/search.rs:63-81](crates/gcode/src/vector/code_symbols/search.rs#L63-L81)

</details>

# crates/gcode/src/vector/code_symbols/search.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

This file implements vector-based code-symbol search and its error handling. `SearchError` captures the failure cases for the search pipeline, including missing Qdrant or embedding config, failed query embedding, invalid collection names, and vector-search failures, and its `Display` impl turns those into user-facing messages. `search_code_symbols` pulls the needed config from `Context`, embeds the query, builds the Qdrant collection name, runs the vector search, and converts raw `(symbol_id, score)` results into `CodeSymbolVectorSearchHit` values. `semantic_search` sits above that as the semantic-ranking entry point, using this machinery as a ranking signal and degrading gracefully when transport or config issues prevent a full search.
[crates/gcode/src/vector/code_symbols/search.rs:8-14]
[crates/gcode/src/vector/code_symbols/search.rs:17-25]
[crates/gcode/src/vector/code_symbols/search.rs:30-58]
[crates/gcode/src/vector/code_symbols/search.rs:63-81]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `SearchError` | type | `pub enum SearchError {` | `SearchError [type]` | `ca2cca63-43fb-5fcd-8465-ad658533af84` | 8-14 [crates/gcode/src/vector/code_symbols/search.rs:8-14] | Indexed type `SearchError` in `crates/gcode/src/vector/code_symbols/search.rs`. [crates/gcode/src/vector/code_symbols/search.rs:8-14] |
| `SearchError::fmt` | method | `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {` | `SearchError::fmt [method]` | `f436a18c-8cf7-5b9e-9e4a-e27b807cf9ab` | 17-25 [crates/gcode/src/vector/code_symbols/search.rs:17-25] | Indexed method `SearchError::fmt` in `crates/gcode/src/vector/code_symbols/search.rs`. [crates/gcode/src/vector/code_symbols/search.rs:17-25] |
| `search_code_symbols` | function | `pub fn search_code_symbols(` | `search_code_symbols [function]` | `003db78b-65f7-5705-8c3f-72c5bf727909` | 30-58 [crates/gcode/src/vector/code_symbols/search.rs:30-58] | Indexed function `search_code_symbols` in `crates/gcode/src/vector/code_symbols/search.rs`. [crates/gcode/src/vector/code_symbols/search.rs:30-58] |
| `semantic_search` | function | `pub fn semantic_search(ctx: &Context, query: &str, limit: usize) -> Vec<(String, f64)> {` | `semantic_search [function]` | `9f88a5e7-6c65-506a-b878-616b591cf929` | 63-81 [crates/gcode/src/vector/code_symbols/search.rs:63-81] | Indexed function `semantic_search` in `crates/gcode/src/vector/code_symbols/search.rs`. [crates/gcode/src/vector/code_symbols/search.rs:63-81] |
