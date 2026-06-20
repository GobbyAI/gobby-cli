---
title: crates/gcode/src/index/indexer/lifecycle.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/lifecycle.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/lifecycle.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Overview

`crates/gcode/src/index/indexer/lifecycle.rs` exposes 11 indexed API symbols.

## How it fits

`crates/gcode/src/index/indexer/lifecycle.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `cleanup_deleted_file_projections` | function | Deletes the file’s graph projection and, when Qdrant is configured, its symbol vectors, recording any failures as projection-cleanup degradations in 'outcome' and flagging missing Qdrant as a vectors cleanup degradation only if vectors were previously synced. [crates/gcode/src/index/indexer/lifecycle.rs:16-54] |
| `push_projection_cleanup_degradation` | function | Appends a 'ProjectionCleanupFailed' 'IndexDegradation' record to 'outcome.degraded', capturing the file path, projection target, and error message as a cleanup failure degradation. [crates/gcode/src/index/indexer/lifecycle.rs:56-69] |
| `attach_projection_sync` | function | If 'request.sync_projections' is enabled, this function sets 'outcome.projection_sync' to a pending post-code-fact-write 'ProjectionSyncRequest' for the current project and indexed file paths targeting both 'Graph' and 'Vectors'; otherwise it does nothing. [crates/gcode/src/index/indexer/lifecycle.rs:71-81] |
| `invalidate` | function | Deletes all indexed code records for the given 'project_id' across the project, symbols, files, chunks, imports, and calls tables within a transaction, commits the purge, optionally notifies the daemon, and logs the invalidation. [crates/gcode/src/index/indexer/lifecycle.rs:84-121] |
| `notify_daemon_invalidate` | function | Sends a blocking 'POST' request with a 1-second timeout to '{base_url}/api/code-index/invalidate' containing '{"project_id": project_id}', and logs warnings if the client cannot be built, the request fails, or the response is non-successful. [crates/gcode/src/index/indexer/lifecycle.rs:125-152] |
| `refresh_project_stats` | function | 'refresh_project_stats' recomputes a project’s indexed file and symbol counts from the database, builds an 'IndexedProject' record with the current root path, timestamp, indexing duration, and optional eligible-file count, and attempts to upsert it via 'api::upsert_project_stats', logging a warning on failure. [crates/gcode/src/index/indexer/lifecycle.rs:154-181] |
| `get_stale_files` | function | Queries the 'code_indexed_files' table for the given 'project_id', builds a map of indexed file paths to content hashes, and returns the set of current file paths whose hash is missing or differs from the stored hash. [crates/gcode/src/index/indexer/lifecycle.rs:183-229] |
| `CurrentFileState` | class | 'CurrentFileState' tracks the current file set by storing a map of file hashes keyed by path and a set of paths that are presently available. [crates/gcode/src/index/indexer/lifecycle.rs:232-235] |
| `current_file_state` | function | Builds a 'CurrentFileState' by iterating over 'candidates' and 'content_only', recording each path relative to 'root_path' as present, and storing its file-content hash when hashing succeeds while emitting a warning on hash failure. [crates/gcode/src/index/indexer/lifecycle.rs:237-260] |
| `get_orphan_files` | function | Queries 'code_indexed_files' for the given 'project_id' and returns every indexed 'file_path' not present in 'present_paths', skipping malformed rows and propagating database errors. [crates/gcode/src/index/indexer/lifecycle.rs:262-294] |
| `count_rows` | function | Counts rows in the allowed tables 'code_indexed_files' or 'code_symbols' for a given 'project_id' by executing 'SELECT COUNT(*)' and returning the result as 'usize', or '0' on unsupported table names or any query/extraction failure. [crates/gcode/src/index/indexer/lifecycle.rs:296-305] |

