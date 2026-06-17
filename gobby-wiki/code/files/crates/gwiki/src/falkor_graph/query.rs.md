---
title: crates/gwiki/src/falkor_graph/query.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph/query.rs
  ranges:
  - 8-23
  - 25-28
  - 30-34
  - 36-40
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/falkor_graph/query.rs:8-23](crates/gwiki/src/falkor_graph/query.rs#L8-L23), [crates/gwiki/src/falkor_graph/query.rs:25-28](crates/gwiki/src/falkor_graph/query.rs#L25-L28), [crates/gwiki/src/falkor_graph/query.rs:30-34](crates/gwiki/src/falkor_graph/query.rs#L30-L34), [crates/gwiki/src/falkor_graph/query.rs:36-40](crates/gwiki/src/falkor_graph/query.rs#L36-L40)

</details>

# crates/gwiki/src/falkor_graph/query.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Builds and reads FalkorDB graph query data for the wiki search backend. `scope_params` turns an optional `SearchScope` filter into escaped `scope_kind` and `scope_id` query parameters for interpolated Cypher text, while `optional_row_string` and `optional_row_usize` extract typed values from a `Row` safely. `row_string` wraps the string extractor with a backend error when a required field is missing, so callers can treat query results as validated row data.
[crates/gwiki/src/falkor_graph/query.rs:8-23]
[crates/gwiki/src/falkor_graph/query.rs:25-28]
[crates/gwiki/src/falkor_graph/query.rs:30-34]
[crates/gwiki/src/falkor_graph/query.rs:36-40]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `scope_params` | function | `pub(super) fn scope_params(scope: &SearchScope) -> Option<HashMap<String, String>> {` | `scope_params [function]` | `ab081406-4af2-588d-bb69-ce33342eefcd` | 8-23 [crates/gwiki/src/falkor_graph/query.rs:8-23] | Indexed function `scope_params` in `crates/gwiki/src/falkor_graph/query.rs`. [crates/gwiki/src/falkor_graph/query.rs:8-23] |
| `row_string` | function | `pub(super) fn row_string(row: &Row, key: &'static str) -> Result<String, SearchError> {` | `row_string [function]` | `d9d3982e-ff9d-5a7b-8e09-7101173d7770` | 25-28 [crates/gwiki/src/falkor_graph/query.rs:25-28] | Indexed function `row_string` in `crates/gwiki/src/falkor_graph/query.rs`. [crates/gwiki/src/falkor_graph/query.rs:25-28] |
| `optional_row_string` | function | `pub(super) fn optional_row_string(row: &Row, key: &'static str) -> Option<String> {` | `optional_row_string [function]` | `cd2b16d3-36c1-51d6-a305-49c704bb7253` | 30-34 [crates/gwiki/src/falkor_graph/query.rs:30-34] | Indexed function `optional_row_string` in `crates/gwiki/src/falkor_graph/query.rs`. [crates/gwiki/src/falkor_graph/query.rs:30-34] |
| `optional_row_usize` | function | `pub(super) fn optional_row_usize(row: &Row, key: &'static str) -> Option<usize> {` | `optional_row_usize [function]` | `8354d785-37a3-5443-94aa-d343bb5881fa` | 36-40 [crates/gwiki/src/falkor_graph/query.rs:36-40] | Indexed function `optional_row_usize` in `crates/gwiki/src/falkor_graph/query.rs`. [crates/gwiki/src/falkor_graph/query.rs:36-40] |
