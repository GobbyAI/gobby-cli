---
title: crates/gcode/src/graph/code_graph/read/support.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/support.rs
  ranges:
  - 43-97
  - 99-131
  - 133-142
  - 150-162
  - 165-187
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/read/support.rs:43-97](crates/gcode/src/graph/code_graph/read/support.rs#L43-L97), [crates/gcode/src/graph/code_graph/read/support.rs:99-131](crates/gcode/src/graph/code_graph/read/support.rs#L99-L131), [crates/gcode/src/graph/code_graph/read/support.rs:133-142](crates/gcode/src/graph/code_graph/read/support.rs#L133-L142), [crates/gcode/src/graph/code_graph/read/support.rs:150-162](crates/gcode/src/graph/code_graph/read/support.rs#L150-L162), [crates/gcode/src/graph/code_graph/read/support.rs:165-187](crates/gcode/src/graph/code_graph/read/support.rs#L165-L187)

</details>

# crates/gcode/src/graph/code_graph/read/support.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Purpose

This file provides shared helpers for reading graph-code query rows and turning them into graph model results. `row_to_graph_result` normalizes a Falkor row into a `GraphResult` by pulling the first available id, name, type, and metadata fields from several possible column names, while the clamp and dedupe helpers enforce graph pagination limits and remove repeated rows from limited blast results. The confidence tests show that graph result confidence defaults to `EXTRACTED` when metadata is absent and otherwise derives from provenance labels and metadata score.
[crates/gcode/src/graph/code_graph/read/support.rs:43-94]
[crates/gcode/src/graph/code_graph/read/support.rs:95-97]
[crates/gcode/src/graph/code_graph/read/support.rs:99-101]
[crates/gcode/src/graph/code_graph/read/support.rs:102-131]
[crates/gcode/src/graph/code_graph/read/support.rs:133-142]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `row_to_graph_result` | function | `pub(crate) fn row_to_graph_result(row: &Row) -> GraphResult {` | `row_to_graph_result [function]` | `7d8cd042-01c8-51f8-b12b-e86b1aed614c` | 43-94 [crates/gcode/src/graph/code_graph/read/support.rs:43-94] | Indexed function `row_to_graph_result` in `crates/gcode/src/graph/code_graph/read/support.rs`. [crates/gcode/src/graph/code_graph/read/support.rs:43-94] |
| `clamp_limit` | function | `pub(super) fn clamp_limit(limit: usize) -> usize {` | `clamp_limit [function]` | `b12da834-1ad0-513b-8140-d1e831914a66` | 95-97 [crates/gcode/src/graph/code_graph/read/support.rs:95-97] | Indexed function `clamp_limit` in `crates/gcode/src/graph/code_graph/read/support.rs`. [crates/gcode/src/graph/code_graph/read/support.rs:95-97] |
| `clamp_offset` | function | `pub(super) fn clamp_offset(offset: usize) -> usize {` | `clamp_offset [function]` | `be54a66a-cfe8-5d4f-b27f-96535fbf8d83` | 99-101 [crates/gcode/src/graph/code_graph/read/support.rs:99-101] | Indexed function `clamp_offset` in `crates/gcode/src/graph/code_graph/read/support.rs`. [crates/gcode/src/graph/code_graph/read/support.rs:99-101] |
| `dedupe_limited_blast_rows` | function | `pub(in crate::graph::code_graph) fn dedupe_limited_blast_rows(` | `dedupe_limited_blast_rows [function]` | `0327d13c-4dc4-551d-83b9-9657723a709e` | 102-131 [crates/gcode/src/graph/code_graph/read/support.rs:102-131] | Indexed function `dedupe_limited_blast_rows` in `crates/gcode/src/graph/code_graph/read/support.rs`. [crates/gcode/src/graph/code_graph/read/support.rs:102-131] |
| `count_from_rows` | function | `pub(super) fn count_from_rows(rows: &[Row]) -> usize {` | `count_from_rows [function]` | `e3394d0c-3784-5f1a-b7a9-1419af3ba1a6` | 133-142 [crates/gcode/src/graph/code_graph/read/support.rs:133-142] | Indexed function `count_from_rows` in `crates/gcode/src/graph/code_graph/read/support.rs`. [crates/gcode/src/graph/code_graph/read/support.rs:133-142] |
| `graph_result_confidence_defaults_to_extracted_without_metadata` | function | `fn graph_result_confidence_defaults_to_extracted_without_metadata() {` | `graph_result_confidence_defaults_to_extracted_without_metadata [function]` | `51b3792a-a303-5cba-ae42-775e227d707d` | 150-162 [crates/gcode/src/graph/code_graph/read/support.rs:150-162] | Indexed function `graph_result_confidence_defaults_to_extracted_without_metadata` in `crates/gcode/src/graph/code_graph/read/support.rs`. [crates/gcode/src/graph/code_graph/read/support.rs:150-162] |
| `graph_result_confidence_uses_provenance_label_with_metadata_score` | function | `fn graph_result_confidence_uses_provenance_label_with_metadata_score() {` | `graph_result_confidence_uses_provenance_label_with_metadata_score [function]` | `c43425b5-852c-5354-a945-983d2a79e0a9` | 165-187 [crates/gcode/src/graph/code_graph/read/support.rs:165-187] | Indexed function `graph_result_confidence_uses_provenance_label_with_metadata_score` in `crates/gcode/src/graph/code_graph/read/support.rs`. [crates/gcode/src/graph/code_graph/read/support.rs:165-187] |
