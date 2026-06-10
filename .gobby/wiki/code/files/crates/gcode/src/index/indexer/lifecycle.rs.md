---
title: crates/gcode/src/index/indexer/lifecycle.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/lifecycle.rs
  ranges:
  - 16-54
  - 56-69
  - 71-81
  - 84-121
  - 125-152
  - 154-181
  - 183-229
  - 232-235
  - 237-260
  - 262-294
  - 296-305
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/lifecycle.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

`crates/gcode/src/index/indexer/lifecycle.rs` exposes 11 indexed API symbols.
[crates/gcode/src/index/indexer/lifecycle.rs:16-54]
[crates/gcode/src/index/indexer/lifecycle.rs:56-69]
[crates/gcode/src/index/indexer/lifecycle.rs:71-81]
[crates/gcode/src/index/indexer/lifecycle.rs:84-121]
[crates/gcode/src/index/indexer/lifecycle.rs:125-152]
[crates/gcode/src/index/indexer/lifecycle.rs:154-181]
[crates/gcode/src/index/indexer/lifecycle.rs:183-229]
[crates/gcode/src/index/indexer/lifecycle.rs:232-235]
[crates/gcode/src/index/indexer/lifecycle.rs:237-260]
[crates/gcode/src/index/indexer/lifecycle.rs:262-294]
[crates/gcode/src/index/indexer/lifecycle.rs:296-305]

## API Symbols

- `cleanup_deleted_file_projections` (function) component `cleanup_deleted_file_projections [function]` (`27cff566-a652-5c21-906c-54247b567ec0`) lines 16-54 [crates/gcode/src/index/indexer/lifecycle.rs:16-54]
  - Signature: `pub(super) fn cleanup_deleted_file_projections(`
  - Purpose: Removes a deleted file's code graph and vector database projections while recording any deletion failures as index outcome degradations. [crates/gcode/src/index/indexer/lifecycle.rs:16-54]
- `push_projection_cleanup_degradation` (function) component `push_projection_cleanup_degradation [function]` (`5ea81afb-c78f-589e-9c62-6ad75a49ad6b`) lines 56-69 [crates/gcode/src/index/indexer/lifecycle.rs:56-69]
  - Signature: `fn push_projection_cleanup_degradation(`
  - Purpose: Appends a `ProjectionCleanupFailed` degradation to the outcome's degraded collection, recording the specified file path, projection target, and error message. [crates/gcode/src/index/indexer/lifecycle.rs:56-69]
- `attach_projection_sync` (function) component `attach_projection_sync [function]` (`9fd4f6ac-7ca7-5f00-8eda-97975a6e638f`) lines 71-81 [crates/gcode/src/index/indexer/lifecycle.rs:71-81]
  - Signature: `pub(super) fn attach_projection_sync(outcome: &mut IndexOutcome, request: &IndexRequest) {`
  - Purpose: Creates and attaches a pending projection synchronization request for graph and vector targets to the outcome when the input request has sync_projections enabled. [crates/gcode/src/index/indexer/lifecycle.rs:71-81]
- `invalidate` (function) component `invalidate [function]` (`baa7789a-c6ed-5e9d-8147-e2f915311202`) lines 84-121 [crates/gcode/src/index/indexer/lifecycle.rs:84-121]
  - Signature: `pub fn invalidate(`
  - Purpose: Atomically removes all code index records (symbols, files, chunks, imports, and calls) for a specified project from the database in a single transaction and optionally notifies a daemon of the invalidation. [crates/gcode/src/index/indexer/lifecycle.rs:84-121]
- `notify_daemon_invalidate` (function) component `notify_daemon_invalidate [function]` (`2b812e49-5999-553b-a85d-aebd28c2e43e`) lines 125-152 [crates/gcode/src/index/indexer/lifecycle.rs:125-152]
  - Signature: `fn notify_daemon_invalidate(base_url: &str, project_id: &str) {`
  - Purpose: Sends a POST request with a 1-second timeout to a daemon's code-index invalidation API endpoint to invalidate the cached code index for the specified project. [crates/gcode/src/index/indexer/lifecycle.rs:125-152]
- `refresh_project_stats` (function) component `refresh_project_stats [function]` (`88cf7807-7b3d-54fd-a997-c4c1cc9e39f8`) lines 154-181 [crates/gcode/src/index/indexer/lifecycle.rs:154-181]
  - Signature: `pub(super) fn refresh_project_stats(`
  - Purpose: Aggregates indexed file and symbol counts for a project and upserts project statistics including indexing duration and timestamp to the database, with error logging. [crates/gcode/src/index/indexer/lifecycle.rs:154-181]
- `get_stale_files` (function) component `get_stale_files [function]` (`e5ef0115-76fe-5b3b-9fa4-26706f94b854`) lines 183-229 [crates/gcode/src/index/indexer/lifecycle.rs:183-229]
  - Signature: `pub(super) fn get_stale_files(`
  - Purpose: Queries PostgreSQL for indexed file hashes of a project and returns file paths where the current content hash differs from or is absent in the indexed set. [crates/gcode/src/index/indexer/lifecycle.rs:183-229]
- `CurrentFileState` (class) component `CurrentFileState [class]` (`55465b3a-9f29-555e-a54d-a6c4e7c8b590`) lines 232-235 [crates/gcode/src/index/indexer/lifecycle.rs:232-235]
  - Signature: `pub(super) struct CurrentFileState {`
  - Purpose: `CurrentFileState` is a `pub(super)` struct that maintains file system state by storing a HashMap of path-to-hash mappings and a HashSet of currently present file paths. [crates/gcode/src/index/indexer/lifecycle.rs:232-235]
- `current_file_state` (function) component `current_file_state [function]` (`9fee873c-a767-5fba-a249-877666585ef9`) lines 237-260 [crates/gcode/src/index/indexer/lifecycle.rs:237-260]
  - Signature: `pub(super) fn current_file_state(`
  - Purpose: Constructs a `CurrentFileState` containing relative file paths and their content hashes for incremental index change detection. [crates/gcode/src/index/indexer/lifecycle.rs:237-260]
- `get_orphan_files` (function) component `get_orphan_files [function]` (`38e31014-9d04-56a9-961a-fac722544e40`) lines 262-294 [crates/gcode/src/index/indexer/lifecycle.rs:262-294]
  - Signature: `pub(super) fn get_orphan_files(`
  - Purpose: **Identifies and returns database-indexed file paths for a given project that are no longer present in the filesystem by comparing against a provided set of currently existing paths.** [crates/gcode/src/index/indexer/lifecycle.rs:262-294]
- `count_rows` (function) component `count_rows [function]` (`9facb226-8885-5b36-a141-3365f419c479`) lines 296-305 [crates/gcode/src/index/indexer/lifecycle.rs:296-305]
  - Signature: `fn count_rows(conn: &mut Client, table: &str, project_id: &str) -> usize {`
  - Purpose: Returns the row count from a validated table (`code_indexed_files` or `code_symbols`) filtered by the provided `project_id`, or 0 if the table is invalid or the query fails. [crates/gcode/src/index/indexer/lifecycle.rs:296-305]

