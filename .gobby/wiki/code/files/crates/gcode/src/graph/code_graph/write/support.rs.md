---
title: crates/gcode/src/graph/code_graph/write/support.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/write/support.rs
  ranges:
  - 6-13
  - 15-21
  - 23-27
  - 29-31
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/write/support.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/write|crates/gcode/src/graph/code_graph/write]]

## Purpose

Provides small write-side helpers for the code graph layer: it wraps execution of a prepared `TypedQuery` against a `GraphClient`, builds typed Cypher queries with parameter maps, converts `usize` values into Falkor-compatible integer `TypedValue`s with an overflow check, and formats the fixed `sync_token` parameter used by write queries.
[crates/gcode/src/graph/code_graph/write/support.rs:6-13]
[crates/gcode/src/graph/code_graph/write/support.rs:15-21]
[crates/gcode/src/graph/code_graph/write/support.rs:23-27]
[crates/gcode/src/graph/code_graph/write/support.rs:29-31]

## API Symbols

- `execute_write_query` (function) component `execute_write_query [function]` (`9a139bb4-bbb8-5ff1-9d8c-f4fdb030fc1b`) lines 6-13 [crates/gcode/src/graph/code_graph/write/support.rs:6-13]
  - Signature: `pub(super) fn execute_write_query(`
  - Purpose: Indexed function `execute_write_query` in `crates/gcode/src/graph/code_graph/write/support.rs`. [crates/gcode/src/graph/code_graph/write/support.rs:6-13]
- `typed_query` (function) component `typed_query [function]` (`045f2ab8-46a9-5246-b469-16df5dd31fdd`) lines 15-21 [crates/gcode/src/graph/code_graph/write/support.rs:15-21]
  - Signature: `pub(super) fn typed_query<I, K>(cypher: impl Into<String>, params: I) -> anyhow::Result<TypedQuery>`
  - Purpose: Indexed function `typed_query` in `crates/gcode/src/graph/code_graph/write/support.rs`. [crates/gcode/src/graph/code_graph/write/support.rs:15-21]
- `usize_value` (function) component `usize_value [function]` (`82ffa7ef-b98b-5c9e-a1f5-5f413151f0ae`) lines 23-27 [crates/gcode/src/graph/code_graph/write/support.rs:23-27]
  - Signature: `pub(super) fn usize_value(value: usize) -> anyhow::Result<TypedValue> {`
  - Purpose: Indexed function `usize_value` in `crates/gcode/src/graph/code_graph/write/support.rs`. [crates/gcode/src/graph/code_graph/write/support.rs:23-27]
- `sync_token_param` (function) component `sync_token_param [function]` (`f2717d2f-b914-56b6-85a9-8502cf6a598f`) lines 29-31 [crates/gcode/src/graph/code_graph/write/support.rs:29-31]
  - Signature: `pub(super) fn sync_token_param(sync_token: &str) -> (&'static str, TypedValue) {`
  - Purpose: Indexed function `sync_token_param` in `crates/gcode/src/graph/code_graph/write/support.rs`. [crates/gcode/src/graph/code_graph/write/support.rs:29-31]

