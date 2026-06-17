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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/report/rows.rs:11-19](crates/gcode/src/graph/report/rows.rs#L11-L19), [crates/gcode/src/graph/report/rows.rs:21-31](crates/gcode/src/graph/report/rows.rs#L21-L31), [crates/gcode/src/graph/report/rows.rs:33-39](crates/gcode/src/graph/report/rows.rs#L33-L39), [crates/gcode/src/graph/report/rows.rs:41-66](crates/gcode/src/graph/report/rows.rs#L41-L66), [crates/gcode/src/graph/report/rows.rs:68-78](crates/gcode/src/graph/report/rows.rs#L68-L78), [crates/gcode/src/graph/report/rows.rs:80-106](crates/gcode/src/graph/report/rows.rs#L80-L106), [crates/gcode/src/graph/report/rows.rs:108-112](crates/gcode/src/graph/report/rows.rs#L108-L112), [crates/gcode/src/graph/report/rows.rs:119-128](crates/gcode/src/graph/report/rows.rs#L119-L128), [crates/gcode/src/graph/report/rows.rs:131-140](crates/gcode/src/graph/report/rows.rs#L131-L140), [crates/gcode/src/graph/report/rows.rs:143-154](crates/gcode/src/graph/report/rows.rs#L143-L154), [crates/gcode/src/graph/report/rows.rs:157-162](crates/gcode/src/graph/report/rows.rs#L157-L162)

</details>

# crates/gcode/src/graph/report/rows.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

This file contains row-parsing helpers for graph report data, converting `falkor::Row` values into typed report structures and simple aggregates. `rows_to_named_counts` builds a `BTreeMap<String, usize>` from `name`/`count` rows, while the `row_to_*` helpers map individual rows into `GraphHotspot`, `TargetFrequency`, and `BridgeEdgeHypothesis`, supplying defaults and skipping invalid or missing fields through shared accessors like `row_string`, `row_usize`, and `row_f64`.
[crates/gcode/src/graph/report/rows.rs:11-19]
[crates/gcode/src/graph/report/rows.rs:21-31]
[crates/gcode/src/graph/report/rows.rs:33-39]
[crates/gcode/src/graph/report/rows.rs:41-66]
[crates/gcode/src/graph/report/rows.rs:68-78]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `rows_to_named_counts` | function | `pub(super) fn rows_to_named_counts(rows: Vec<Row>) -> BTreeMap<String, usize> {` | `rows_to_named_counts [function]` | `5c906575-9e41-5977-bcb0-058c2b77120f` | 11-19 [crates/gcode/src/graph/report/rows.rs:11-19] | Indexed function `rows_to_named_counts` in `crates/gcode/src/graph/report/rows.rs`. [crates/gcode/src/graph/report/rows.rs:11-19] |
| `row_to_graph_hotspot` | function | `pub(super) fn row_to_graph_hotspot(row: &Row) -> Option<GraphHotspot> {` | `row_to_graph_hotspot [function]` | `9f12f72e-998f-5b8f-b11c-c8a184ab2174` | 21-31 [crates/gcode/src/graph/report/rows.rs:21-31] | Indexed function `row_to_graph_hotspot` in `crates/gcode/src/graph/report/rows.rs`. [crates/gcode/src/graph/report/rows.rs:21-31] |
| `row_to_target_frequency` | function | `pub(super) fn row_to_target_frequency(row: &Row) -> Option<TargetFrequency> {` | `row_to_target_frequency [function]` | `1217d1cb-e173-540c-be3d-1b8fa3699c23` | 33-39 [crates/gcode/src/graph/report/rows.rs:33-39] | Indexed function `row_to_target_frequency` in `crates/gcode/src/graph/report/rows.rs`. [crates/gcode/src/graph/report/rows.rs:33-39] |
| `row_to_bridge_edge_hypothesis` | function | `pub(super) fn row_to_bridge_edge_hypothesis(row: &Row) -> Option<BridgeEdgeHypothesis> {` | `row_to_bridge_edge_hypothesis [function]` | `49480ab2-1284-52c3-909e-d3892295f42e` | 41-66 [crates/gcode/src/graph/report/rows.rs:41-66] | Indexed function `row_to_bridge_edge_hypothesis` in `crates/gcode/src/graph/report/rows.rs`. [crates/gcode/src/graph/report/rows.rs:41-66] |
| `row_string` | function | `fn row_string(row: &Row, keys: &[&str]) -> Option<String> {` | `row_string [function]` | `5f45b090-aa30-584f-a6d1-47f0e0b97a39` | 68-78 [crates/gcode/src/graph/report/rows.rs:68-78] | Indexed function `row_string` in `crates/gcode/src/graph/report/rows.rs`. [crates/gcode/src/graph/report/rows.rs:68-78] |
| `row_usize` | function | `fn row_usize(row: &Row, keys: &[&str]) -> Option<usize> {` | `row_usize [function]` | `6b4d0e55-9ec2-5842-9ff3-fe81a05ec714` | 80-106 [crates/gcode/src/graph/report/rows.rs:80-106] | Indexed function `row_usize` in `crates/gcode/src/graph/report/rows.rs`. [crates/gcode/src/graph/report/rows.rs:80-106] |
| `row_f64` | function | `fn row_f64(row: &Row, keys: &[&str]) -> Option<f64> {` | `row_f64 [function]` | `1ef10d37-1300-5751-8121-68ea5132b223` | 108-112 [crates/gcode/src/graph/report/rows.rs:108-112] | Indexed function `row_f64` in `crates/gcode/src/graph/report/rows.rs`. [crates/gcode/src/graph/report/rows.rs:108-112] |
| `row_string_skips_empty_candidate_keys` | function | `fn row_string_skips_empty_candidate_keys() {` | `row_string_skips_empty_candidate_keys [function]` | `ad700713-0954-5630-8300-e191d8b4253d` | 119-128 [crates/gcode/src/graph/report/rows.rs:119-128] | Indexed function `row_string_skips_empty_candidate_keys` in `crates/gcode/src/graph/report/rows.rs`. [crates/gcode/src/graph/report/rows.rs:119-128] |
| `row_usize_skips_invalid_candidate_keys` | function | `fn row_usize_skips_invalid_candidate_keys() {` | `row_usize_skips_invalid_candidate_keys [function]` | `bed47a27-db47-59cd-926e-3891cf833025` | 131-140 [crates/gcode/src/graph/report/rows.rs:131-140] | Indexed function `row_usize_skips_invalid_candidate_keys` in `crates/gcode/src/graph/report/rows.rs`. [crates/gcode/src/graph/report/rows.rs:131-140] |
| `rows_to_named_counts_skips_missing_counts` | function | `fn rows_to_named_counts_skips_missing_counts() {` | `rows_to_named_counts_skips_missing_counts [function]` | `b895a14c-6fdf-5ef7-aa06-d6c888849b5b` | 143-154 [crates/gcode/src/graph/report/rows.rs:143-154] | Indexed function `rows_to_named_counts_skips_missing_counts` in `crates/gcode/src/graph/report/rows.rs`. [crates/gcode/src/graph/report/rows.rs:143-154] |
| `row_usize_rejects_negative_values` | function | `fn row_usize_rejects_negative_values() {` | `row_usize_rejects_negative_values [function]` | `5fb8773e-5154-5998-801e-b9a8d82cd331` | 157-162 [crates/gcode/src/graph/report/rows.rs:157-162] | Indexed function `row_usize_rejects_negative_values` in `crates/gcode/src/graph/report/rows.rs`. [crates/gcode/src/graph/report/rows.rs:157-162] |
