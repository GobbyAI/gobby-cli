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

## crates/gcode/src/graph/code_graph/write

This module is the write layer of the code-graph pipeline. It translates parsed source-code artefacts — symbols, imports, and call relations — into parameterised Cypher mutations that are executed against a FalkorDB instance. The four files have distinct concerns: `mutation.rs` owns query construction, `deletion.rs` owns teardown, `support.rs` owns the thin execution wrapper and parameter helpers, and `sync_plan.rs` owns bounded batch scheduling. Together they form the only path through which the broader `code_graph` module commits state changes to the graph store.

`mutation.rs` declares the Cypher templates for the three main write operations. `ADD_IMPORTS_CYPHER` (mutation.rs:17-24) merges `CodeFile → IMPORTS → CodeModule` edges. `ADD_DEFINITIONS_CYPHER` (mutation.rs:25-44) merges `CodeFile → DEFINES → CodeSymbol` nodes with full metadata. `ADD_SYMBOL_CALLS_CYPHER` (mutation.rs:44-53) merges `CALLS` edges between `CodeSymbol` pairs. Every mutation carries a `sync_token` derived from a per-process `AtomicU64` counter (mutation.rs:15) so that stale rows written by an older run can be identified and pruned. The public builder functions — `ensure_file_node_query`, `add_imports_query`, `add_definitions_query`, `add_symbol_calls_query`, `add_external_calls_query`, and `add_unresolved_calls_query` — consume a `SyncFileMutation` struct and return `TypedQuery` values ready for execution.

`sync_plan.rs` solves a scalability problem (gobby-cli #678): the original single fused `UNWIND` over all rows in a file could grow to multiple megabytes for pathological data files, hanging FalkorDB. `plan_sync_batches` (sync_plan.rs:29) now produces an ordered, bounded query list: first the file-header `MERGE` via `ensure_file_node_query`, then each of imports, definitions, and calls chunked at `GRAPH_SYNC_BATCH_SIZE = 500` rows (sync_plan.rs:21). Because the `add_*_query` builders are idempotent `MERGE` operations, the chunks are order-independent within each category. `deletion.rs` complements this with two targeted teardown helpers: `delete_file_graph_queries` (deletion.rs:7) removes stale `IMPORTS`, `DEFINES`, and `CALLS` edges for a re-synced file and detach-deletes any `CodeSymbol` nodes absent from `current_symbol_ids`; `delete_stale_file_graph_queries` prunes nodes by `sync_token` after a full pass. All four files route through `support.rs`, which wraps `GraphClient::query` (support.rs:6-12) and supplies the three shared helpers below.

| Symbol | File | Purpose |
|---|---|---|
| `execute_write_query` | support.rs:6 | Executes one `TypedQuery` against a `GraphClient` |
| `typed_query` | support.rs:14 | Constructs a `TypedQuery` from a Cypher string and parameter iterator |
| `usize_value` | support.rs:22 | Converts `usize` to `TypedValue::Integer`, enforcing i64 bounds |
| `sync_token_param` | support.rs:29 | Produces the `("sync_token", TypedValue::String)` param tuple |
| `plan_sync_batches` | sync_plan.rs:29 | Returns the ordered, chunked `Vec<TypedQuery>` for one `sync_file` call |
| `GRAPH_SYNC_BATCH_SIZE` | sync_plan.rs:21 | Batch ceiling: 500 rows per request |
| `delete_file_graph_queries` | deletion.rs:7 | Teardown queries for a re-indexed file |
| `delete_stale_file_graph_queries` | deletion.rs:65 | Prunes rows whose `sync_token` no longer matches |

| Graph node / relationship | Managed by |
|---|---|
| `CodeFile` | mutation.rs, deletion.rs |
| `CodeSymbol` | mutation.rs, deletion.rs |
| `CodeModule` | mutation.rs, deletion.rs |
| `UnresolvedCallee` | deletion.rs (PROJECT_NODE_PREDICATE, deletion.rs:5) |
| `ExternalSymbol` | deletion.rs (PROJECT_NODE_PREDICATE, deletion.rs:5) |
| `IMPORTS` | mutation.rs:17, deletion.rs:21 |
| `DEFINES` | mutation.rs:25, deletion.rs:26 |
| `CALLS` | mutation.rs:44, deletion.rs:31 |

External dependencies consumed here include `gobby_core::falkor::GraphClient` (support.rs:4), `crate::graph::typed_query::{TypedQuery, TypedValue}` used throughout, and domain models from `crate::models` including `CallRelation`, `ImportRelation`, `Symbol`, `make_external_symbol_id`, and `make_unresolved_callee_id` (mutation.rs:7-9). The parent `code_graph` module calls into this write layer by invoking `plan_sync_batches` and the deletion helpers, then dispatching the resulting `TypedQuery` values through `execute_write_query`.
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

