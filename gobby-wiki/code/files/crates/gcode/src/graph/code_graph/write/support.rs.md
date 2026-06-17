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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/write/support.rs:6-13](crates/gcode/src/graph/code_graph/write/support.rs#L6-L13), [crates/gcode/src/graph/code_graph/write/support.rs:15-21](crates/gcode/src/graph/code_graph/write/support.rs#L15-L21), [crates/gcode/src/graph/code_graph/write/support.rs:23-27](crates/gcode/src/graph/code_graph/write/support.rs#L23-L27), [crates/gcode/src/graph/code_graph/write/support.rs:29-31](crates/gcode/src/graph/code_graph/write/support.rs#L29-L31)

</details>

# crates/gcode/src/graph/code_graph/write/support.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Provides small write-side helpers for the code graph layer. `execute_write_query` unwraps a `TypedQuery` and sends its Cypher plus parameters to `GraphClient`, returning a plain result. `typed_query` builds a `TypedQuery` from Cypher and an iterator of typed parameters. `usize_value` converts a `usize` into a FalkorDB-compatible integer value with a range check, and `sync_token_param` packages a sync token string as the standard `"sync_token"` query parameter. Together these functions standardize query construction and execution for graph writes.
[crates/gcode/src/graph/code_graph/write/support.rs:6-13]
[crates/gcode/src/graph/code_graph/write/support.rs:15-21]
[crates/gcode/src/graph/code_graph/write/support.rs:23-27]
[crates/gcode/src/graph/code_graph/write/support.rs:29-31]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute_write_query` | function | `pub(super) fn execute_write_query(` | `execute_write_query [function]` | `9a139bb4-bbb8-5ff1-9d8c-f4fdb030fc1b` | 6-13 [crates/gcode/src/graph/code_graph/write/support.rs:6-13] | Indexed function `execute_write_query` in `crates/gcode/src/graph/code_graph/write/support.rs`. [crates/gcode/src/graph/code_graph/write/support.rs:6-13] |
| `typed_query` | function | `pub(super) fn typed_query<I, K>(cypher: impl Into<String>, params: I) -> anyhow::Result<TypedQuery>` | `typed_query [function]` | `045f2ab8-46a9-5246-b469-16df5dd31fdd` | 15-21 [crates/gcode/src/graph/code_graph/write/support.rs:15-21] | Indexed function `typed_query` in `crates/gcode/src/graph/code_graph/write/support.rs`. [crates/gcode/src/graph/code_graph/write/support.rs:15-21] |
| `usize_value` | function | `pub(super) fn usize_value(value: usize) -> anyhow::Result<TypedValue> {` | `usize_value [function]` | `82ffa7ef-b98b-5c9e-a1f5-5f413151f0ae` | 23-27 [crates/gcode/src/graph/code_graph/write/support.rs:23-27] | Indexed function `usize_value` in `crates/gcode/src/graph/code_graph/write/support.rs`. [crates/gcode/src/graph/code_graph/write/support.rs:23-27] |
| `sync_token_param` | function | `pub(super) fn sync_token_param(sync_token: &str) -> (&'static str, TypedValue) {` | `sync_token_param [function]` | `f2717d2f-b914-56b6-85a9-8502cf6a598f` | 29-31 [crates/gcode/src/graph/code_graph/write/support.rs:29-31] | Indexed function `sync_token_param` in `crates/gcode/src/graph/code_graph/write/support.rs`. [crates/gcode/src/graph/code_graph/write/support.rs:29-31] |
