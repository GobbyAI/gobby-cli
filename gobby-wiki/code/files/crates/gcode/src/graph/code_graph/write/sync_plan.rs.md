---
title: crates/gcode/src/graph/code_graph/write/sync_plan.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/write/sync_plan.rs
  ranges:
  - 30-81
  - 89-110
  - 113-156
  - 159-177
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81](crates/gcode/src/graph/code_graph/write/sync_plan.rs#L30-L81), [crates/gcode/src/graph/code_graph/write/sync_plan.rs:89-110](crates/gcode/src/graph/code_graph/write/sync_plan.rs#L89-L110), [crates/gcode/src/graph/code_graph/write/sync_plan.rs:113-156](crates/gcode/src/graph/code_graph/write/sync_plan.rs#L113-L156), [crates/gcode/src/graph/code_graph/write/sync_plan.rs:159-177](crates/gcode/src/graph/code_graph/write/sync_plan.rs#L159-L177)

</details>

# crates/gcode/src/graph/code_graph/write/sync_plan.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Implements bounded write planning for `sync_file`: it always emits a header query that upserts the `CodeFile` with the final symbol count and sync token, then splits imports, symbol definitions, and call data into fixed-size batches so each graph-sync mutation stays small and idempotent. The helper tests verify the batching behavior, including the normal case of one header plus one batch per chunk and the small-file case where everything still fits in a single definition batch.
[crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81]
[crates/gcode/src/graph/code_graph/write/sync_plan.rs:89-110]
[crates/gcode/src/graph/code_graph/write/sync_plan.rs:113-156]
[crates/gcode/src/graph/code_graph/write/sync_plan.rs:159-177]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `plan_sync_batches` | function | `pub(super) fn plan_sync_batches(input: SyncFileMutation<'_>) -> anyhow::Result<Vec<TypedQuery>> {` | `plan_sync_batches [function]` | `6bd8d0a9-f677-5035-9a9b-4a79920c778b` | 30-81 [crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81] | Indexed function `plan_sync_batches` in `crates/gcode/src/graph/code_graph/write/sync_plan.rs`. [crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81] |
| `test_symbol` | function | `fn test_symbol(i: usize) -> Symbol {` | `test_symbol [function]` | `8063daf0-5051-5564-8d4c-2b8a1fa5ff6a` | 89-110 [crates/gcode/src/graph/code_graph/write/sync_plan.rs:89-110] | Indexed function `test_symbol` in `crates/gcode/src/graph/code_graph/write/sync_plan.rs`. [crates/gcode/src/graph/code_graph/write/sync_plan.rs:89-110] |
| `plans_header_then_one_definition_batch_per_chunk` | function | `fn plans_header_then_one_definition_batch_per_chunk() {` | `plans_header_then_one_definition_batch_per_chunk [function]` | `284b67d6-d34b-5105-9685-d0b95fd6e276` | 113-156 [crates/gcode/src/graph/code_graph/write/sync_plan.rs:113-156] | Indexed function `plans_header_then_one_definition_batch_per_chunk` in `crates/gcode/src/graph/code_graph/write/sync_plan.rs`. [crates/gcode/src/graph/code_graph/write/sync_plan.rs:113-156] |
| `small_file_plans_header_and_single_definition_batch` | function | `fn small_file_plans_header_and_single_definition_batch() {` | `small_file_plans_header_and_single_definition_batch [function]` | `319a1033-0bd7-575d-a7ba-7f6ebc24f235` | 159-177 [crates/gcode/src/graph/code_graph/write/sync_plan.rs:159-177] | Indexed function `small_file_plans_header_and_single_definition_batch` in `crates/gcode/src/graph/code_graph/write/sync_plan.rs`. [crates/gcode/src/graph/code_graph/write/sync_plan.rs:159-177] |
