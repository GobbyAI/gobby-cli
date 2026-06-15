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

# crates/gcode/src/graph/code_graph/write/sync_plan.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/write|crates/gcode/src/graph/code_graph/write]]

## Purpose

Provides bounded batch planning for `sync_file` mutations so a file update is split into a small ordered set of `TypedQuery`s instead of one huge fused write. `plan_sync_batches` first emits a header query that merges the `CodeFile` with its final `symbol_count` and `sync_token`, then chunks imports, symbol definitions, and call records into `GRAPH_SYNC_BATCH_SIZE` batches using the mutation-specific query builders; the tests verify the header-plus-batched-query shape for both large and small files.
[crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81]
[crates/gcode/src/graph/code_graph/write/sync_plan.rs:89-110]
[crates/gcode/src/graph/code_graph/write/sync_plan.rs:113-156]
[crates/gcode/src/graph/code_graph/write/sync_plan.rs:159-177]

## API Symbols

- `plan_sync_batches` (function) component `plan_sync_batches [function]` (`6bd8d0a9-f677-5035-9a9b-4a79920c778b`) lines 30-81 [crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81]
  - Signature: `pub(super) fn plan_sync_batches(input: SyncFileMutation<'_>) -> anyhow::Result<Vec<TypedQuery>> {`
  - Purpose: Builds and returns a vector of batched graph-sync 'TypedQuery's for a file mutation by first emitting the file-node merge query, then chunking imports, symbols, and call records into 'GRAPH_SYNC_BATCH_SIZE'-sized insert queries while skipping empty segments. [crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81]
- `test_symbol` (function) component `test_symbol [function]` (`8063daf0-5051-5564-8d4c-2b8a1fa5ff6a`) lines 89-110 [crates/gcode/src/graph/code_graph/write/sync_plan.rs:89-110]
  - Signature: `fn test_symbol(i: usize) -> Symbol {`
  - Purpose: Constructs and returns a 'Symbol' initialized with deterministic metadata derived from 'i' for 'id', 'name', 'qualified_name', and 'line_start'/'line_end', while all other fields are fixed defaults or empty values. [crates/gcode/src/graph/code_graph/write/sync_plan.rs:89-110]
- `plans_header_then_one_definition_batch_per_chunk` (function) component `plans_header_then_one_definition_batch_per_chunk [function]` (`284b67d6-d34b-5105-9685-d0b95fd6e276`) lines 113-156 [crates/gcode/src/graph/code_graph/write/sync_plan.rs:113-156]
  - Signature: `fn plans_header_then_one_definition_batch_per_chunk() {`
  - Purpose: Verifies that a large symbol set is planned into a single header 'MERGE' query plus one 'UNWIND $symbols AS symbol' definition batch per 'GRAPH_SYNC_BATCH_SIZE', with the final 'symbol_count' on the header and a shared 'sync_token' on every query but no 'symbol_ids' parameter. [crates/gcode/src/graph/code_graph/write/sync_plan.rs:113-156]
- `small_file_plans_header_and_single_definition_batch` (function) component `small_file_plans_header_and_single_definition_batch [function]` (`319a1033-0bd7-575d-a7ba-7f6ebc24f235`) lines 159-177 [crates/gcode/src/graph/code_graph/write/sync_plan.rs:159-177]
  - Signature: `fn small_file_plans_header_and_single_definition_batch() {`
  - Purpose: Verifies that 'plan_sync_batches' for a small file with three definitions and no imports/calls produces exactly two Cypher queries, the first merging the 'CodeFile' node and the second unwinding 'symbols' for batch insertion. [crates/gcode/src/graph/code_graph/write/sync_plan.rs:159-177]

