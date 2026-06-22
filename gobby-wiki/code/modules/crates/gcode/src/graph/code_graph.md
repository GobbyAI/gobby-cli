---
title: crates/gcode/src/graph/code_graph
type: code_module
provenance:
- file: crates/gcode/src/graph/code_graph/connection.rs
- file: crates/gcode/src/graph/code_graph/lifecycle.rs
- file: crates/gcode/src/graph/code_graph/payload.rs
- file: crates/gcode/src/graph/code_graph/read.rs
- file: crates/gcode/src/graph/code_graph/read/graph_payloads.rs
- file: crates/gcode/src/graph/code_graph/read/payload_queries.rs
- file: crates/gcode/src/graph/code_graph/read/relationship_queries.rs
- file: crates/gcode/src/graph/code_graph/read/relationships.rs
- file: crates/gcode/src/graph/code_graph/read/support.rs
- file: crates/gcode/src/graph/code_graph/tests.rs
- file: crates/gcode/src/graph/code_graph/write.rs
- file: crates/gcode/src/graph/code_graph/write/deletion.rs
- file: crates/gcode/src/graph/code_graph/write/mutation.rs
- file: crates/gcode/src/graph/code_graph/write/support.rs
- file: crates/gcode/src/graph/code_graph/write/sync_plan.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph

Parent: [[code/modules/crates/gcode/src/graph|crates/gcode/src/graph]]

## Overview

## crates/gcode/src/graph/code\_graph

This module is the authoritative owner of the code-index graph projection within the `gcode` crate. It is the declared exception to the broader rule that Gobby-owned graph stores are managed externally: `gcode` itself reads and writes FalkorDB `Code*` nodes and edges that are derived from its PostgreSQL index rows (write.rs:1–6). The module is organised into five focused sub-files — `connection`, `lifecycle`, `payload`, `read`, and `write` — plus a companion `tests` module, with `read` and `write` promoted to child modules containing their own sub-files for queries, mutations, deletions, sync planning, and support helpers.

The write path centers on `CodeGraph`, a short-lived struct that holds a `project_id` and a mutable `GraphClient` reference (write.rs:45–62). Its `sync_file` method orchestrates a full file projection cycle: it mints a sync token, builds import items via `import_graph_items`, resolves symbol definitions through `definition_graph_symbols`, partitions call targets with `partition_call_graph_items`, and then executes batched mutation queries through `plan_sync_batches` and `execute_write_query`. Exported deletion helpers — `cleanup_orphans_queries`, `clear_all_code_index_query`, `clear_project_query`, `delete_file_graph_queries`, and `delete_file_node_query` — keep all destructive operations project-scoped and label-restricted to the five `PROJECT_INDEXED_LABELS` (write.rs:38–43). The read path (child module `read`) exposes graph-view functions such as `project_overview_graph`, `file_graph`, `symbol_neighbors`, and `blast_radius`, backed by corresponding `*_query` helpers that emit parameterised Cypher and map FalkorDB `Row` values back into `GraphPayload` structs through row-extraction utilities (`row_string_owned`, `row_usize`, `add_node_from_row`, `add_link_from_row`).

`GraphPayload` (payload.rs) is the universal serialisation container returned by every read function. It maintains an internal `HashSet<String>` node-ID cache that is lazily populated on first `push_node` call to guarantee deduplication without cost on construction (payload.rs:33–47). It also provides `analytics_graph_from_parts`, which converts raw `(id, kind, weight)` and `(source, target, kind)` iterables directly into the `gobby_core::graph_analytics::AnalyticsGraph` type consumed by the wider analytics pipeline. `GraphNode` and `GraphLink` each carry `from_row` constructors that deserialise FalkorDB rows, and `GraphLink` preserves full `ProjectionMetadata` including provenance, confidence, source system, source file path, and source line — fields asserted in the test suite (tests.rs:23–35).

The `lifecycle` sub-file provides the types and logic for out-of-band graph management operations (clear and rebuild) that are invoked via HTTP against a daemon URL. `GraphLifecycleAction` maps each action to its CLI command, REST endpoint, and success message; `GraphLifecycleTimeouts` reads overrides from environment variables with safe fallbacks; and `run_lifecycle_action` drives the full HTTP round-trip including timeout enforcement and structured error formatting via `format_http_error` and `compact_detail` (lifecycle.rs:1–100).

### GraphLifecycleAction mapping

| Action | cli\_command | endpoint\_path | success\_prefix |
|---|---|---|---|
| `Clear` | `gcode graph clear` | `/api/code-index/graph/clear` | `Cleared code-index graph` |
| `Rebuild` | `gcode graph rebuild` | `/api/code-index/graph/rebuild` | `Rebuilt code-index graph` |

### Lifecycle timeout environment variables

| Env var | Default (secs) | Controls |
|---|---|---|
| `GCODE_GRAPH_CLEAR_TIMEOUT_SECS` | 15 | HTTP timeout for clear action |
| `GCODE_GRAPH_REBUILD_TIMEOUT_SECS` | 120 | HTTP timeout for rebuild action |

### Public API surface (selected symbols)

| Symbol | Kind | Location |
|---|---|---|
| `CodeGraph::new` / `::sync_file` | struct + method | write.rs:45–80 |
| `GraphPayload` | struct | payload.rs:9 |
| `GraphPayload::push_node` | method | payload.rs:32 |
| `GraphPayload::analytics_graph_from_parts` | method | payload.rs:51 |
| `GraphNode` / `GraphLink` | structs | payload.rs |
| `GraphLifecycleAction` | enum | lifecycle.rs:17 |
| `GraphLifecycleRequest::from_context` | method | lifecycle.rs:55 |
| `GraphLifecycleTimeouts::from_env` | method | lifecycle.rs:80 |
| `run_lifecycle_action` | function | lifecycle.rs |
| `project_overview_graph` / `file_graph` / `symbol_neighbors` / `blast_radius` | functions | read child module |
| `cleanup_orphans_queries` / `clear_project_query` / `delete_file_node_query` | functions | write.rs:21–24 |
| `call_target_id` | public function | write.rs:25 |

### Graph node labels managed by this module

| Label |
|---|
| `CodeFile` |
| `CodeSymbol` |
| `CodeModule` |
| `UnresolvedCallee` |
| `ExternalSymbol` |

(write.rs:38–43)
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29]
[crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81]
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:9-21]
[crates/gcode/src/graph/code_graph/read/support.rs:43-94]
[crates/gcode/src/graph/code_graph/write/deletion.rs:8-66]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/graph/code_graph/read\|crates/gcode/src/graph/code_graph/read]] | ## crates/gcode/src/graph/code_graph/read |
| [[code/modules/crates/gcode/src/graph/code_graph/write\|crates/gcode/src/graph/code_graph/write]] | ## crates/gcode/src/graph/code_graph/write |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/graph/code_graph/connection.rs\|crates/gcode/src/graph/code_graph/connection.rs]] | `crates/gcode/src/graph/code_graph/connection.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/lifecycle.rs\|crates/gcode/src/graph/code_graph/lifecycle.rs]] | `crates/gcode/src/graph/code_graph/lifecycle.rs` exposes 22 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/payload.rs\|crates/gcode/src/graph/code_graph/payload.rs]] | `crates/gcode/src/graph/code_graph/payload.rs` exposes 25 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/read.rs\|crates/gcode/src/graph/code_graph/read.rs]] | `crates/gcode/src/graph/code_graph/read.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/tests.rs\|crates/gcode/src/graph/code_graph/tests.rs]] | `crates/gcode/src/graph/code_graph/tests.rs` exposes 22 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/write.rs\|crates/gcode/src/graph/code_graph/write.rs]] | `crates/gcode/src/graph/code_graph/write.rs` exposes 27 indexed API symbols. |

