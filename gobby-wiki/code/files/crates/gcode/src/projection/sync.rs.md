---
title: crates/gcode/src/projection/sync.rs
type: code_file
provenance:
- file: crates/gcode/src/projection/sync.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/projection/sync.rs

Module: [[code/modules/crates/gcode/src/projection|crates/gcode/src/projection]]

## Overview

`crates/gcode/src/projection/sync.rs` exposes 31 indexed API symbols.

## How it fits

`crates/gcode/src/projection/sync.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ProjectionTarget` | type | Indexed type `ProjectionTarget` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:12-15] |
| `ProjectionSyncRequest` | class | 'ProjectionSyncRequest' is a request payload containing a 'project_id', a list of file path strings to synchronize, and a list of 'ProjectionTarget' destinations. [crates/gcode/src/projection/sync.rs:18-22] |
| `ProjectionSyncStatus` | class | 'ProjectionSyncStatus' is a status record for a project’s synchronization state, containing the project ID, the list of affected file paths, and boolean flags indicating whether graph and vector updates are still pending. [crates/gcode/src/projection/sync.rs:25-30] |
| `ProjectionStatus` | type | Indexed type `ProjectionStatus` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:34-38] |
| `ProjectionSyncError` | class | 'ProjectionSyncError' is a struct that represents a projection synchronization failure by carrying a string 'kind' discriminator and a human-readable 'message'. [crates/gcode/src/projection/sync.rs:41-44] |
| `ProjectionSyncReport` | class | 'ProjectionSyncReport' is a sync outcome summary that records the projection’s final status, counts of synced/skipped/failed files and synced symbols, whether the run degraded, and an optional 'ProjectionSyncError'. [crates/gcode/src/projection/sync.rs:47-55] |
| `ProjectionSyncReport::ok` | method | Constructs a new 'Self' by delegating to 'Self::ok_with_counts(synced_files, synced_symbols, 0, 0)', using zero for the two additional count fields. [crates/gcode/src/projection/sync.rs:58-60] |
| `ProjectionSyncReport::ok_with_counts` | method | Constructs and returns a 'Self' value representing a successful projection state by setting 'status' to 'ProjectionStatus::Ok', populating the provided file/symbol counts, and clearing 'degraded' and 'error'. [crates/gcode/src/projection/sync.rs:62-77] |
| `ProjectionSyncReport::degraded` | method | Constructs a degraded state by converting 'kind' and 'message' into 'String' values and delegating to 'degraded_with_counts' with the provided synced file/symbol counts and zero unsynced file/symbol counts. [crates/gcode/src/projection/sync.rs:79-86] |
| `ProjectionSyncReport::degraded_with_counts` | method | Constructs a 'ProjectionSync' value in 'Degraded' status with 'degraded = true', populates the synced/skipped/failed file and symbol counts, and attaches an 'error' containing the provided 'kind' and 'message'. [crates/gcode/src/projection/sync.rs:88-108] |
| `ProjectionSyncReport::degraded_from_error` | method | 'degraded_from_error' constructs a degraded 'Self' state from an 'anyhow::Error' and the current synced file/symbol counts, defaulting the unsynced counts to zero by delegating to 'degraded_from_error_with_counts'. [crates/gcode/src/projection/sync.rs:110-116] |
| `ProjectionSyncReport::degraded_from_error_with_counts` | method | Constructs a 'ProjectionStats'-like value in a degraded state by projecting the provided 'anyhow::Error' to a typed error, setting 'status' to 'ProjectionStatus::Degraded', copying the supplied file/symbol counts, marking 'degraded' true, and storing the typed error in 'error'. [crates/gcode/src/projection/sync.rs:118-135] |
| `ProjectionSyncReports` | class | 'ProjectionSyncReports' is a struct that groups two 'ProjectionSyncReport' values, 'graph' and 'vector', representing sync reports for those two projection modes. [crates/gcode/src/projection/sync.rs:139-142] |
| `ProjectionFileSyncOutcome` | type | Indexed type `ProjectionFileSyncOutcome` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:145-148] |
| `pending_after_code_fact_write` | function | Constructs a 'ProjectionSyncStatus' from a 'ProjectionSyncRequest', marking 'graph_pending' and 'vectors_pending' based on whether 'request.targets' contains 'ProjectionTarget::Graph' or 'ProjectionTarget::Vectors', and copying through 'project_id' and 'file_paths'. [crates/gcode/src/projection/sync.rs:150-157] |
| `sync_after_index` | function | Creates and returns a 'ProjectionSyncReports' by synchronizing graph files and vector files for the given 'file_paths' with the provided 'Context', propagating any error from either sync operation. [crates/gcode/src/projection/sync.rs:159-167] |
| `sync_files_with_state` | function | Iterates over 'file_paths', invoking 'sync_one' for each to accumulate synced/skipped/failed counts and error messages, then returns an 'ok_with_counts' report when no errors occurred or a 'degraded_with_counts' report with the first error kind and concatenated diagnostics otherwise. [crates/gcode/src/projection/sync.rs:169-224] |
| `sync_graph_files` | function | Synchronizes the given file paths into the code graph using a read-write database connection, tracking synced/skipped/failed counts and reconciliation errors, and returns an 'ok' or degraded 'ProjectionSyncReport' depending on whether any file-level or graph-access errors occurred. [crates/gcode/src/projection/sync.rs:226-310] |
| `sync_vector_files` | function | Synchronizes the given vector file paths by building a 'VectorProjectionState' from the context and a read-write database connection, returning an OK report for an empty input or a degraded report if lifecycle initialization fails, otherwise delegating to 'sync_files_with_state' with 'VectorProjectionState::sync_file'. [crates/gcode/src/projection/sync.rs:312-340] |
| `sync_graph_file` | function | Attempts to mark a project file for graph sync, loads its persisted graph facts, applies them to 'code_graph::CodeGraph::sync_file', then marks the file synced and returns either 'Synced' with the number of definitions or 'SkippedMissingIndexedFile' if the file was missing from the index. [crates/gcode/src/projection/sync.rs:342-365] |
| `VectorProjectionState` | class | 'VectorProjectionState<'a>' is a state container holding a borrowed 'Context', an owned 'postgres::Client' connection, and a 'CodeSymbolVectorLifecycle' for managing vector projection operations. [crates/gcode/src/projection/sync.rs:367-371] |
| `sync_file` | function | Checks whether the file is indexed, fetches its symbols and syncs them into the lifecycle, then marks its vectors as synced and returns either 'Synced { symbols }' or 'SkippedMissingIndexedFile' if the file is absent or could not be marked. [crates/gcode/src/projection/sync.rs:374-389] |
| `vector_lifecycle_from_context` | function | Builds a 'CodeSymbolVectorLifecycle' from a 'Context' by cloning the configured Qdrant client and code vector settings, resolving the embedding source from the context, and returning an error if either Qdrant or embedding configuration is missing. [crates/gcode/src/projection/sync.rs:392-407] |
| `typed_projection_error` | function | Converts an 'anyhow::Error' into a 'ProjectionSyncError' by classifying it as a 'VectorLifecycleError' or 'GraphReadError' kind when possible, otherwise defaulting to '"sync_failed"', and copying the error's string representation into 'message'. [crates/gcode/src/projection/sync.rs:409-419] |
| `graph_error_kind` | function | Returns a static error-kind string label by pattern-matching 'GraphReadError' variants, mapping each variant to a corresponding FalkorDB or invalid-target identifier. [crates/gcode/src/projection/sync.rs:421-428] |
| `vector_error_kind` | function | Returns a static string error category for a 'VectorLifecycleError' by matching each variant to a fixed lowercase, underscore-separated kind label. [crates/gcode/src/projection/sync.rs:430-441] |
| `test_context` | function | Constructs and returns a 'Context' test fixture with hardcoded placeholder values, including a nonexistent PostgreSQL URL and project root, 'project-1' ID, 'quiet = true', no optional service endpoints, default indexing configuration, and 'ProjectIndexScope::Single'. [crates/gcode/src/projection/sync.rs:448-462] |
| `sync_state_continues_after_projection_errors` | function | Verifies that 'sync_files_with_state' continues processing subsequent files after a projection write error, marks the overall report as 'Degraded', and correctly aggregates synced/failed counts and the 'sync_failed' error kind. [crates/gcode/src/projection/sync.rs:465-500] |
| `State` | class | 'State' is a struct with a single field, 'synced: Vec<String>', used to store a list of synced string values. [crates/gcode/src/projection/sync.rs:472-474] |
| `sync_state_treats_missing_indexed_file_as_non_degraded_skip` | function | Verifies that 'sync_files_with_state' counts 'ProjectionFileSyncOutcome::SkippedMissingIndexedFile' as a non-degrading skip, leaving the overall report 'Ok' with one synced file, one skipped file, no failures, and 'degraded == false'. [crates/gcode/src/projection/sync.rs:503-528] |
| `State` | class | 'State' is a struct that stores a single field, 'synced', which is a vector of strings representing synced items. [crates/gcode/src/projection/sync.rs:506-508] |

