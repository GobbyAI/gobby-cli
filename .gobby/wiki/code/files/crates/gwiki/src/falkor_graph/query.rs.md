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

# crates/gwiki/src/falkor_graph/query.rs

Module: [[code/modules/crates/gwiki/src/falkor_graph|crates/gwiki/src/falkor_graph]]

## Purpose

Provides small FalkorDB query helpers for the wiki graph layer. `scope_params` turns an optional `SearchScope` filter into escaped Cypher string parameters for `scope_kind` and `scope_id`, while `row_string`, `optional_row_string`, and `optional_row_usize` extract typed fields from a `Row`: the first reports a backend error if a required string key is missing, and the latter two safely return optional owned strings or `usize` values when present and valid.
[crates/gwiki/src/falkor_graph/query.rs:8-23]
[crates/gwiki/src/falkor_graph/query.rs:25-28]
[crates/gwiki/src/falkor_graph/query.rs:30-34]
[crates/gwiki/src/falkor_graph/query.rs:36-40]

## API Symbols

- `scope_params` (function) component `scope_params [function]` (`ab081406-4af2-588d-bb69-ce33342eefcd`) lines 8-23 [crates/gwiki/src/falkor_graph/query.rs:8-23]
  - Signature: `pub(super) fn scope_params(scope: &SearchScope) -> Option<HashMap<String, String>> {`
  - Purpose: Returns 'Some(HashMap)' containing escaped 'scope_kind' and 'scope_id' parameters derived from 'scope.scope_filter()', or 'None' if the scope has no filter. [crates/gwiki/src/falkor_graph/query.rs:8-23]
- `row_string` (function) component `row_string [function]` (`d9d3982e-ff9d-5a7b-8e09-7101173d7770`) lines 25-28 [crates/gwiki/src/falkor_graph/query.rs:25-28]
  - Signature: `pub(super) fn row_string(row: &Row, key: &'static str) -> Result<String, SearchError> {`
  - Purpose: Returns the optional string value for 'key' from a 'Row', or converts its absence into a 'SearchError::Backend' stating that the FalkorDB wiki graph row is missing that key. [crates/gwiki/src/falkor_graph/query.rs:25-28]
- `optional_row_string` (function) component `optional_row_string [function]` (`cd2b16d3-36c1-51d6-a305-49c704bb7253`) lines 30-34 [crates/gwiki/src/falkor_graph/query.rs:30-34]
  - Signature: `pub(super) fn optional_row_string(row: &Row, key: &'static str) -> Option<String> {`
  - Purpose: Attempts to read 'key' from 'row' as a 'Value', return its string slice if present, and convert it into an owned 'String', otherwise return 'None'. [crates/gwiki/src/falkor_graph/query.rs:30-34]
- `optional_row_usize` (function) component `optional_row_usize [function]` (`8354d785-37a3-5443-94aa-d343bb5881fa`) lines 36-40 [crates/gwiki/src/falkor_graph/query.rs:36-40]
  - Signature: `pub(super) fn optional_row_usize(row: &Row, key: &'static str) -> Option<usize> {`
  - Purpose: Returns 'Some(usize)' when the row value for 'key' exists, is an unsigned integer, and fits in 'usize', otherwise returns 'None'. [crates/gwiki/src/falkor_graph/query.rs:36-40]

