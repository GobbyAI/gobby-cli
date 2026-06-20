---
title: crates/gcode/src/graph/code_graph/write
type: code_module
provenance:
- file: crates/gcode/src/graph/code_graph/write/deletion.rs
- file: crates/gcode/src/graph/code_graph/write/mutation.rs
- file: crates/gcode/src/graph/code_graph/write/support.rs
- file: crates/gcode/src/graph/code_graph/write/sync_plan.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/write

Parent: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Overview

This module owns write-side code graph persistence: it builds typed Falkor/Cypher mutations for files, symbols, imports, and calls, plus cleanup queries for stale graph state. The mutation layer imports typed query primitives and model types such as `Symbol`, `ImportRelation`, `CallRelation`, unresolved callees, and external symbol IDs, then encodes `IMPORTS`, `DEFINES`, and `CALLS` graph writes with provenance, confidence, source-system, source-file, and sync-token metadata (`crates/gcode/src/graph/code_graph/write/mutation.rs:1-100`).

The main sync flow is planned by `sync_plan`: `plan_sync_batches` first emits a file header query, then batches imports, definitions, symbol calls, unresolved calls, and external calls using a shared sync token. Its explicit purpose is to avoid oversized `UNWIND` requests against FalkorDB by limiting each batch to 500 rows, while preserving idempotent `MERGE` behavior in the add-query builders (`crates/gcode/src/graph/code_graph/write/sync_plan.rs:1-100`).

Deletion is the counterpart flow. `delete_file_graph_queries` removes a file’s `IMPORTS`, `DEFINES`, and outgoing `CALLS` relationships, then either deletes all symbols for the file or only symbols no longer present in `current_symbol_ids`. `delete_stale_file_graph_queries` follows the same project/file/sync-token model for post-sync cleanup (`crates/gcode/src/graph/code_graph/write/deletion.rs:1-100`). Shared support code adapts module-generated `TypedQuery` values to `GraphClient::query`, centralizes parameter construction, safely converts `usize` to Falkor-compatible `i64`, and provides the common `sync_token` parameter helper (`crates/gcode/src/graph/code_graph/write/support.rs:1-32`).

| Symbol | Kind | Responsibility | Anchor |
| --- | --- | --- | --- |
| `plan_sync_batches` | Function | Builds ordered, bounded write queries for one file sync | `crates/gcode/src/graph/code_graph/write/sync_plan.rs:1-100` |
| `GRAPH_SYNC_BATCH_SIZE` | Constant | Caps graph-sync batches at 500 rows | `crates/gcode/src/graph/code_graph/write/sync_plan.rs:1-100` |
| `delete_file_graph_queries` | Function | Builds cleanup queries for a specific file graph | `crates/gcode/src/graph/code_graph/write/deletion.rs:1-100` |
| `delete_stale_file_graph_queries` | Function | Builds sync-token-based stale cleanup queries | `crates/gcode/src/graph/code_graph/write/deletion.rs:1-100` |
| `execute_write_query` | Helper | Executes one `TypedQuery` through `GraphClient` | `crates/gcode/src/graph/code_graph/write/support.rs:1-32` |
| `typed_query` | Helper | Constructs parameterized `TypedQuery` values | `crates/gcode/src/graph/code_graph/write/support.rs:1-32` |
| `usize_value` | Helper | Converts Rust `usize` into FalkorDB integer values | `crates/gcode/src/graph/code_graph/write/support.rs:1-32` |
| `sync_token_param` | Helper | Produces the shared `sync_token` query parameter | `crates/gcode/src/graph/code_graph/write/support.rs:1-32` |
[crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81]
[crates/gcode/src/graph/code_graph/write/deletion.rs:8-66]
[crates/gcode/src/graph/code_graph/write/mutation.rs:89-96]
[crates/gcode/src/graph/code_graph/write/support.rs:6-13]
[crates/gcode/src/graph/code_graph/write/sync_plan.rs:89-110]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/graph/code_graph/write/deletion.rs\|crates/gcode/src/graph/code_graph/write/deletion.rs]] | `crates/gcode/src/graph/code_graph/write/deletion.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/write/mutation.rs\|crates/gcode/src/graph/code_graph/write/mutation.rs]] | `crates/gcode/src/graph/code_graph/write/mutation.rs` exposes 24 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/write/support.rs\|crates/gcode/src/graph/code_graph/write/support.rs]] | `crates/gcode/src/graph/code_graph/write/support.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/write/sync_plan.rs\|crates/gcode/src/graph/code_graph/write/sync_plan.rs]] | `crates/gcode/src/graph/code_graph/write/sync_plan.rs` exposes 4 indexed API symbols. |

