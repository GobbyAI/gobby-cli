---
title: crates/gcode/src/graph/report/rows.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/rows.rs
  ranges:
  - 11-19
  - 21-31
  - 33-39
  - 41-66
  - 68-78
  - 80-106
  - 108-112
  - 119-128
  - 131-140
  - 143-154
  - 157-162
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/report/rows.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

Provides row-conversion helpers for graph reporting, turning `gobby_core::falkor::Row` values into the report types used elsewhere in the graph layer. The main functions map query rows into a `BTreeMap<String, usize>`, `GraphHotspot`, `TargetFrequency`, and `BridgeEdgeHypothesis`, applying defaults and skipping rows when required fields are missing. The shared extractors `row_string`, `row_usize`, and `row_f64` centralize tolerant field lookup and type conversion, and the tests verify that empty or invalid candidate values are skipped and that missing counts are excluded.
[crates/gcode/src/graph/report/rows.rs:11-19]
[crates/gcode/src/graph/report/rows.rs:21-31]
[crates/gcode/src/graph/report/rows.rs:33-39]
[crates/gcode/src/graph/report/rows.rs:41-66]
[crates/gcode/src/graph/report/rows.rs:68-78]

## API Symbols

- `rows_to_named_counts` (function) component `rows_to_named_counts [function]` (`5c906575-9e41-5977-bcb0-058c2b77120f`) lines 11-19 [crates/gcode/src/graph/report/rows.rs:11-19]
  - Signature: `pub(super) fn rows_to_named_counts(rows: Vec<Row>) -> BTreeMap<String, usize> {`
  - Purpose: Transforms a vector of rows into a lexicographically-sorted map by extracting 'name' and 'count' fields from each row, skipping rows where extraction fails. [crates/gcode/src/graph/report/rows.rs:11-19]
- `row_to_graph_hotspot` (function) component `row_to_graph_hotspot [function]` (`9f12f72e-998f-5b8f-b11c-c8a184ab2174`) lines 21-31 [crates/gcode/src/graph/report/rows.rs:21-31]
  - Signature: `pub(super) fn row_to_graph_hotspot(row: &Row) -> Option<GraphHotspot> {`
  - Purpose: Converts a database row into a GraphHotspot object by extracting mandatory `id` and `name` fields and populating degree, node type, and directional metrics with sensible defaults. [crates/gcode/src/graph/report/rows.rs:21-31]
- `row_to_target_frequency` (function) component `row_to_target_frequency [function]` (`1217d1cb-e173-540c-be3d-1b8fa3699c23`) lines 33-39 [crates/gcode/src/graph/report/rows.rs:33-39]
  - Signature: `pub(super) fn row_to_target_frequency(row: &Row) -> Option<TargetFrequency> {`
  - Purpose: Constructs a `TargetFrequency` struct from a database `Row` by extracting required `id` and `name` string fields (returning `None` if either is missing) and an optional `count` field (defaulting to zero). [crates/gcode/src/graph/report/rows.rs:33-39]
- `row_to_bridge_edge_hypothesis` (function) component `row_to_bridge_edge_hypothesis [function]` (`49480ab2-1284-52c3-909e-d3892295f42e`) lines 41-66 [crates/gcode/src/graph/report/rows.rs:41-66]
  - Signature: `pub(super) fn row_to_bridge_edge_hypothesis(row: &Row) -> Option<BridgeEdgeHypothesis> {`
  - Purpose: Deserializes a database row into a `BridgeEdgeHypothesis` by extracting source and target identifiers, relation type, and optional metadata fields with default fallbacks. [crates/gcode/src/graph/report/rows.rs:41-66]
- `row_string` (function) component `row_string [function]` (`5f45b090-aa30-584f-a6d1-47f0e0b97a39`) lines 68-78 [crates/gcode/src/graph/report/rows.rs:68-78]
  - Signature: `fn row_string(row: &Row, keys: &[&str]) -> Option<String> {`
  - Purpose: Returns the first non-empty string value from a Row matching a sequence of keys, or None if all are absent or empty. [crates/gcode/src/graph/report/rows.rs:68-78]
- `row_usize` (function) component `row_usize [function]` (`6b4d0e55-9ec2-5842-9ff3-fe81a05ec714`) lines 80-106 [crates/gcode/src/graph/report/rows.rs:80-106]
  - Signature: `fn row_usize(row: &Row, keys: &[&str]) -> Option<usize> {`
  - Purpose: Extracts and converts the first available key's value from a Row to `usize`, attempting conversions from u64, non-negative i64, and non-fractional f64 in sequence. [crates/gcode/src/graph/report/rows.rs:80-106]
- `row_f64` (function) component `row_f64 [function]` (`1ef10d37-1300-5751-8121-68ea5132b223`) lines 108-112 [crates/gcode/src/graph/report/rows.rs:108-112]
  - Signature: `fn row_f64(row: &Row, keys: &[&str]) -> Option<f64> {`
  - Purpose: Retrieves the first value from a Row by iterating through provided keys and attempts to convert it to an f64 using `find_map` followed by `and_then`. [crates/gcode/src/graph/report/rows.rs:108-112]
- `row_string_skips_empty_candidate_keys` (function) component `row_string_skips_empty_candidate_keys [function]` (`ad700713-0954-5630-8300-e191d8b4253d`) lines 119-128 [crates/gcode/src/graph/report/rows.rs:119-128]
  - Signature: `fn row_string_skips_empty_candidate_keys() {`
  - Purpose: This test verifies that `row_string()` skips empty string values and returns the first non-empty value from a list of candidate keys. [crates/gcode/src/graph/report/rows.rs:119-128]
- `row_usize_skips_invalid_candidate_keys` (function) component `row_usize_skips_invalid_candidate_keys [function]` (`bed47a27-db47-59cd-926e-3891cf833025`) lines 131-140 [crates/gcode/src/graph/report/rows.rs:131-140]
  - Signature: `fn row_usize_skips_invalid_candidate_keys() {`
  - Purpose: This test verifies that `row_usize` returns the first valid `usize` value from a list of candidate keys, skipping those that cannot be converted to `usize`. [crates/gcode/src/graph/report/rows.rs:131-140]
- `rows_to_named_counts_skips_missing_counts` (function) component `rows_to_named_counts_skips_missing_counts [function]` (`b895a14c-6fdf-5ef7-aa06-d6c888849b5b`) lines 143-154 [crates/gcode/src/graph/report/rows.rs:143-154]
  - Signature: `fn rows_to_named_counts_skips_missing_counts() {`
  - Purpose: Unit test verifying that `rows_to_named_counts()` converts rows to a name-to-count mapping while excluding rows lacking a count field. [crates/gcode/src/graph/report/rows.rs:143-154]
- `row_usize_rejects_negative_values` (function) component `row_usize_rejects_negative_values [function]` (`5fb8773e-5154-5998-801e-b9a8d82cd331`) lines 157-162 [crates/gcode/src/graph/report/rows.rs:157-162]
  - Signature: `fn row_usize_rejects_negative_values() {`
  - Purpose: This test verifies that the `row_usize` function returns `None` when attempting to extract a negative value as an unsigned integer, confirming it rejects values incompatible with the `usize` type. [crates/gcode/src/graph/report/rows.rs:157-162]

