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

## crates/gcode/src/projection

The `projection` module is responsible for synchronising parsed code data into the two downstream stores that power gcode's search and analysis features: a graph database (FalkorDB) and a vector store (Qdrant). It acts as the orchestration layer that fans a set of file paths out to the appropriate backend, tracks per-file outcomes, and aggregates results into a structured report. The module also handles the inverse operation — reconciling deletions — by removing projections from both stores when a source file is removed.

The primary entry points live in the `sync` sub-module (`sync.rs`). `sync_after_index` drives the top-level sync flow after indexing completes, dispatching to `sync_graph_files` and `sync_vector_files` depending on which `ProjectionTarget` values are requested. Each of those delegates further to per-file helpers (`sync_graph_file`, `sync_file`) that read indexed facts from the database via `crate::db`, call into `crate::graph::code_graph` for graph writes (sync.rs:4), and call into `crate::vector::code_symbols` for embedding and upsert operations (sync.rs:5–8). Pending state after a write is tracked through `pending_after_code_fact_write`, and `VectorProjectionState` carries lifecycle context across the vector sync loop. Error classification is centralised in `typed_projection_error`, `graph_error_kind`, and `vector_error_kind`, ensuring that transient or missing-file conditions are distinguished from hard failures without aborting remaining files.

Deletion reconciliation is handled in `mod.rs` by `reconcile_deleted_file` (mod.rs:13). It checks whether FalkorDB is configured (`ctx.falkordb.is_some()`) before calling `code_graph::delete_file_projection`, and checks for Qdrant before calling `code_symbols::delete_file_vectors` (mod.rs:16–31). Any failures are collected into `ProjectionReconcileFailure` values keyed by `ProjectionTarget` and returned to the caller rather than panicking, allowing the caller to decide how to surface them.

The module is imported by higher-level orchestration code that constructs a `ProjectionSyncRequest`, submits it, and inspects the resulting `ProjectionSyncReport` or `ProjectionSyncStatus`. Internally it imports `crate::config::Context` for database handles and project identity, `crate::db` for indexed fact reads, `crate::graph::code_graph` for graph projection writes, and `crate::vector::code_symbols` (including `CodeSymbolVectorLifecycle` and `embedding_source_from_context`) for vector writes (sync.rs:1–8, mod.rs:1–3).

### Public API

| Symbol | Kind | Notes |
|---|---|---|
| `ProjectionTarget` | enum | `Graph` \| `Vectors`; selects which store to sync (sync.rs:11–14) |
| `ProjectionSyncRequest` | struct | Carries `project_id`, `file_paths`, and `targets` (sync.rs:17–21) |
| `ProjectionSyncStatus` | struct | Reflects pending state per target after a sync pass (sync.rs:23–29) |
| `ProjectionStatus` | enum | `Ok` \| `Degraded` \| `Failed`; overall health of a sync (sync.rs:31–36) |
| `ProjectionSyncError` | struct | `kind` + `message` pair describing a failure (sync.rs:38–41) |
| `ProjectionSyncReport` | struct | Aggregated counts (`synced_files`, `synced_symbols`, `skipped_files`, `failed_files`) plus `ProjectionStatus` (sync.rs:43–53) |
| `ProjectionSyncReports` | struct | Collection of per-target `ProjectionSyncReport` values |
| `ProjectionFileSyncOutcome` | type alias | Per-file result type used inside the sync loop |
| `ProjectionReconcileFailure` | struct | Target + message for a deletion reconcile error (mod.rs:8–11) |
| `reconcile_deleted_file` | fn | Removes file projections from both stores; returns failures (mod.rs:13) |
| `sync_after_index` | fn | Top-level post-index sync dispatcher |
| `sync_files_with_state` | fn | Iterates files with shared state, collecting outcomes |
| `sync_graph_files` | fn | Dispatches graph projection for a file list |
| `sync_vector_files` | fn | Dispatches vector projection for a file list |
| `sync_graph_file` | fn | Syncs a single file to the graph store |
| `sync_file` | fn | Syncs a single file to the vector store |
| `VectorProjectionState` | struct | Lifecycle state shared across vector sync iterations |
| `vector_lifecycle_from_context` | fn | Constructs `CodeSymbolVectorLifecycle` from `Context` |
| `pending_after_code_fact_write` | fn | Determines whether a file remains pending after a write |
| `typed_projection_error` | fn | Maps raw errors to `ProjectionSyncError` with a typed `kind` |
| `graph_error_kind` | fn | Classifies a `GraphReadError` into a kind string |
| `vector_error_kind` | fn | Classifies a `VectorLifecycleError` into a kind string |

### `ProjectionSyncReport` constructors

| Method | Status set | Degraded flag |
|---|---|---|
| `ok(files, symbols)` | `Ok` | `false` |
| `ok_with_counts(files, symbols, skipped, failed)` | `Ok` | `false` |
| `degraded(kind, msg, files, symbols)` | `Degraded` | `true` |
| `degraded_with_counts(kind, msg, files, symbols, skipped, failed)` | `Degraded` | `true` |
| `degraded_from_error(kind, msg, files, symbols)` | `Degraded` | `true` |
| `degraded_from_error_with_counts(…)` | `Degraded` | `true` |
[crates/gcode/src/projection/mod.rs:8-11]
[crates/gcode/src/projection/sync.rs:12-15]
[crates/gcode/src/projection/mod.rs:13-35]
[crates/gcode/src/projection/sync.rs:18-22]
[crates/gcode/src/projection/sync.rs:25-30]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/projection/mod.rs\|crates/gcode/src/projection/mod.rs]] | `crates/gcode/src/projection/mod.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gcode/src/projection/sync.rs\|crates/gcode/src/projection/sync.rs]] | `crates/gcode/src/projection/sync.rs` exposes 31 indexed API symbols. |

