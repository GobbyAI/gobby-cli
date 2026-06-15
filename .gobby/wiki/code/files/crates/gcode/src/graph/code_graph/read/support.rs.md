---
title: crates/gcode/src/graph/code_graph/read/support.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/support.rs
  ranges:
  - 38-86
  - 88-120
  - 122-131
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/read/support.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Purpose

This file provides shared helpers for reading code-graph query results and normalizing them into the API’s graph model. Its constants define Cypher predicates, type-dispatch `CASE` expressions, metadata return fields, and a global maximum graph limit used by the query helpers. The functions work together to turn raw `Row` values into `GraphResult` records with fallback column-name resolution, clamp requested `limit` and `offset` values to safe bounds, deduplicate and sort blast rows by distance and node identity before truncating them, and extract a resilient row count from the first result row.
[crates/gcode/src/graph/code_graph/read/support.rs:38-83]
[crates/gcode/src/graph/code_graph/read/support.rs:84-86]
[crates/gcode/src/graph/code_graph/read/support.rs:88-90]
[crates/gcode/src/graph/code_graph/read/support.rs:91-120]
[crates/gcode/src/graph/code_graph/read/support.rs:122-131]

## API Symbols

- `row_to_graph_result` (function) component `row_to_graph_result [function]` (`9e549371-0349-597f-92dd-9501cc2c6aa4`) lines 38-83 [crates/gcode/src/graph/code_graph/read/support.rs:38-83]
  - Signature: `pub(crate) fn row_to_graph_result(row: &Row) -> GraphResult {`
  - Purpose: 'row_to_graph_result' constructs a 'GraphResult' by extracting string, numeric, and optional relation fields from a 'Row', using a priority chain of alternate column names for 'id' and 'name', defaulting missing strings to '""' and missing numbers to '0', and populating 'metadata' via 'row_to_projection_metadata(row)'. [crates/gcode/src/graph/code_graph/read/support.rs:38-83]
- `clamp_limit` (function) component `clamp_limit [function]` (`c45885db-9ca0-5717-bbd2-fcfde99d0c0b`) lines 84-86 [crates/gcode/src/graph/code_graph/read/support.rs:84-86]
  - Signature: `pub(super) fn clamp_limit(limit: usize) -> usize {`
  - Purpose: Returns 'limit' clamped to 'MAX_GRAPH_LIMIT' by delegating to 'typed_query::clamp_limit'. [crates/gcode/src/graph/code_graph/read/support.rs:84-86]
- `clamp_offset` (function) component `clamp_offset [function]` (`988daf2c-dd54-5244-81c9-774407c48634`) lines 88-90 [crates/gcode/src/graph/code_graph/read/support.rs:88-90]
  - Signature: `pub(super) fn clamp_offset(offset: usize) -> usize {`
  - Purpose: Returns 'typed_query::clamp_offset(offset, MAX_GRAPH_LIMIT)', clamping the given 'offset' to the maximum graph limit. [crates/gcode/src/graph/code_graph/read/support.rs:88-90]
- `dedupe_limited_blast_rows` (function) component `dedupe_limited_blast_rows [function]` (`8e032768-05b5-5f1f-a38a-17610c4cb637`) lines 91-120 [crates/gcode/src/graph/code_graph/read/support.rs:91-120]
  - Signature: `pub(in crate::graph::code_graph) fn dedupe_limited_blast_rows(`
  - Purpose: Sorts the input rows by 'distance', then 'node_name', then 'node_id', removes rows lacking 'node_id' or with duplicate 'node_id's, truncates the result to 'clamp_limit(limit)', and returns the deduplicated subset. [crates/gcode/src/graph/code_graph/read/support.rs:91-120]
- `count_from_rows` (function) component `count_from_rows [function]` (`0cbf7a96-e174-57c4-b116-61e5c0f21f68`) lines 122-131 [crates/gcode/src/graph/code_graph/read/support.rs:122-131]
  - Signature: `pub(super) fn count_from_rows(rows: &[Row]) -> usize {`
  - Purpose: Returns the 'cnt' field from the first 'Row' as a 'usize', accepting either unsigned or nonnegative signed integers and defaulting to '0' if the row, field, conversion, or parse is missing or invalid. [crates/gcode/src/graph/code_graph/read/support.rs:122-131]

