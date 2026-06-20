---
title: crates/gcode/src/projection
type: code_module
provenance:
- file: crates/gcode/src/projection/mod.rs
- file: crates/gcode/src/projection/sync.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/projection

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/projection` owns projection synchronization and cleanup for graph and vector backends. `mod.rs` exposes the projection submodule and provides deleted-file reconciliation: when graph configuration exists it deletes the graph projection, and when Qdrant is configured it deletes stored vectors, returning per-target failures instead of stopping at the first error (`crates/gcode/src/projection/mod.rs:1-36`).

`sync.rs` defines the request, status, target, report, and error shapes used to coordinate projection work. Its public data model distinguishes graph vs. vector targets, tracks pending state per backend, and reports `ok`, `degraded`, or `failed` outcomes with file/symbol counts plus optional typed error details (`crates/gcode/src/projection/sync.rs:8-100`).

The module collaborates outward with configuration, database, graph, and vector subsystems: it imports `Context`, `db`, `code_graph`, graph read errors, code symbol vector lifecycle helpers, vector lifecycle errors, and embedding-source construction (`crates/gcode/src/projection/sync.rs:1-7`). The cleanup path calls into `code_graph::delete_file_projection` and `code_symbols::delete_file_vectors`, gated by configured FalkorDB and Qdrant state (`crates/gcode/src/projection/mod.rs:14-31`).

| Public symbol | Kind | Role |
| --- | --- | --- |
| `ProjectionReconcileFailure` | struct | Per-target deleted-file cleanup failure |
| `reconcile_deleted_file` | function | Removes graph/vector projections for a deleted file |
| `ProjectionTarget` | enum | Selects `Graph` or `Vectors` |
| `ProjectionSyncRequest` | struct | Project, files, and target list for sync |
| `ProjectionSyncStatus` | struct | Pending graph/vector status for files |
| `ProjectionStatus` | enum | `Ok`, `Degraded`, or `Failed` sync state |
| `ProjectionSyncError` | struct | Typed error kind and message |
| `ProjectionSyncReport` | struct | Counts, degraded flag, and optional error |
| `ProjectionSyncReports` | struct | Aggregate sync reporting |
| `sync_after_index` | function | Sync entry point after indexing |
| `sync_files_with_state` | function | Stateful multi-file sync |
| `sync_graph_files` / `sync_vector_files` | functions | Backend-specific batch sync |
| `sync_graph_file` / `sync_file` | functions | Backend/file-level sync helpers |
| `pending_after_code_fact_write` | function | Computes pending projection state after fact writes |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/projection/mod.rs\|crates/gcode/src/projection/mod.rs]] | `crates/gcode/src/projection/mod.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gcode/src/projection/sync.rs\|crates/gcode/src/projection/sync.rs]] | `crates/gcode/src/projection/sync.rs` exposes 31 indexed API symbols. |

