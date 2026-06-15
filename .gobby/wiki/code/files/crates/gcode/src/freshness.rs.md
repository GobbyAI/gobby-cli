---
title: crates/gcode/src/freshness.rs
type: code_file
provenance:
- file: crates/gcode/src/freshness.rs
  ranges:
  - 13-16
  - 19-22
  - 24-83
  - 93-121
  - 123-144
  - 146-160
  - 162-182
  - '184'
  - 186-193
  - 195-200
  - 208-222
  - 224-226
  - 228-245
  - 247-264
  - 266-273
  - 275-283
  - 285-290
  - 292-305
  - 312-320
  - 328-335
  - 343-382
  - 386-422
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/freshness.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Coordinates freshness checks for the gcode index. It defines `FreshnessScope` and `FreshnessStatus`, then `ensure_fresh` uses an in-flight environment marker plus a lock-free project precheck to skip unnecessary work, otherwise taking the project advisory lock and reindexing either the whole project or a normalized set of explicit file paths. The helper functions support that flow by detecting stale project indexes, validating symbol byte-slice hashes, normalizing file paths, and building test/Postgres contexts and locks for the freshness tests that exercise the short-circuit, busy-lock, and slice-validity paths.
[crates/gcode/src/freshness.rs:13-16]
[crates/gcode/src/freshness.rs:19-22]
[crates/gcode/src/freshness.rs:24-83]
[crates/gcode/src/freshness.rs:93-121]
[crates/gcode/src/freshness.rs:123-144]

## API Symbols

- `FreshnessScope` (type) component `FreshnessScope [type]` (`f61fe7d0-cb35-5fa9-ab58-80938ba8529f`) lines 13-16 [crates/gcode/src/freshness.rs:13-16]
  - Signature: `pub enum FreshnessScope {`
  - Purpose: Indexed type `FreshnessScope` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:13-16]
- `FreshnessStatus` (type) component `FreshnessStatus [type]` (`b4ef28ed-7a8f-597c-96af-fe09a246a5b1`) lines 19-22 [crates/gcode/src/freshness.rs:19-22]
  - Signature: `pub enum FreshnessStatus {`
  - Purpose: Indexed type `FreshnessStatus` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:19-22]
- `ensure_fresh` (function) component `ensure_fresh [function]` (`c8af2110-ca73-5c67-932b-0c884dd653dd`) lines 24-83 [crates/gcode/src/freshness.rs:24-83]
  - Signature: `pub fn ensure_fresh(ctx: &Context, scope: FreshnessScope) -> anyhow::Result<FreshnessStatus> {`
  - Purpose: Ensures project file index freshness by conditionally reindexing either the entire project or specified files under an advisory lock, with lock-free pre-checks to skip unnecessary work. [crates/gcode/src/freshness.rs:24-83]
- `project_needs_refresh` (function) component `project_needs_refresh [function]` (`6970c8cd-4aa3-51fa-832f-cc2a313fa9b0`) lines 93-121 [crates/gcode/src/freshness.rs:93-121]
  - Signature: `fn project_needs_refresh(ctx: &Context) -> anyhow::Result<bool> {`
  - Purpose: Returns `true` if a project's code index has never been created or if any tracked file paths have changed since the last recorded indexing timestamp. [crates/gcode/src/freshness.rs:93-121]
- `ensure_symbol_fresh` (function) component `ensure_symbol_fresh [function]` (`27e3bed4-eb80-526e-bb22-4465aa356e45`) lines 123-144 [crates/gcode/src/freshness.rs:123-144]
  - Signature: `pub fn ensure_symbol_fresh(ctx: &Context, id: &str) -> anyhow::Result<FreshnessStatus> {`
  - Purpose: Validates a symbol's freshness by checking if its file slice is current, and if not, ensures its source file is re-processed. [crates/gcode/src/freshness.rs:123-144]
- `symbol_slice_is_current` (function) component `symbol_slice_is_current [function]` (`9f86c033-896a-53a7-8c17-44012ae81185`) lines 146-160 [crates/gcode/src/freshness.rs:146-160]
  - Signature: `fn symbol_slice_is_current(ctx: &Context, sym: &Symbol) -> bool {`
  - Purpose: Returns `true` only when `sym.content_hash` is non-empty, the symbol’s file can be read from `ctx.project_root.join(sym.file_path)`, and the hash computed over `sym.byte_start..sym.byte_end` exactly matches `sym.content_hash`. [crates/gcode/src/freshness.rs:146-160]
- `normalize_file_path` (function) component `normalize_file_path [function]` (`0279e83e-5e1a-5c8e-b538-9b116d7eab9b`) lines 162-182 [crates/gcode/src/freshness.rs:162-182]
  - Signature: `fn normalize_file_path(root: &Path, path: &Path) -> String {`
  - Purpose: Resolves `path` against `root` when relative, canonicalizes both paths, returns the canonical path relative to the canonicalized `root` when it lies under that root, and otherwise falls back to the original `path`, converted lossily to a `String`. [crates/gcode/src/freshness.rs:162-182]
- `FreshnessGuard` (class) component `FreshnessGuard [class]` (`4d8390fd-df77-5e9c-bcb0-c4afa141068e`) lines 184-184 [crates/gcode/src/freshness.rs:184]
  - Signature: `struct FreshnessGuard;`
  - Purpose: `FreshnessGuard` is a zero-sized marker struct with no fields or methods visible in the provided declaration. [crates/gcode/src/freshness.rs:184]
- `FreshnessGuard` (class) component `FreshnessGuard [class]` (`e46d16c8-6fb7-5d4e-8bbe-25c4d6d9a9ff`) lines 186-193 [crates/gcode/src/freshness.rs:186-193]
  - Signature: `impl FreshnessGuard {`
  - Purpose: FreshnessGuard is an RAII guard that sets an environment variable to mark active freshness indexing within a CLI process. [crates/gcode/src/freshness.rs:186-193]
- `FreshnessGuard.enter` (method) component `FreshnessGuard.enter [method]` (`71e65cf6-f900-5130-98c7-04dd8ed8ed40`) lines 187-192 [crates/gcode/src/freshness.rs:187-192]
  - Signature: `fn enter() -> Self {`
  - Purpose: Marks the current CLI process as in-flight by unsafely setting `INFLIGHT_ENV` to `"1"` and then returning `Self`. [crates/gcode/src/freshness.rs:187-192]
- `FreshnessGuard` (class) component `FreshnessGuard [class]` (`3ae4a5dd-3b1c-5d54-8152-9d1f54789cc0`) lines 195-200 [crates/gcode/src/freshness.rs:195-200]
  - Signature: `impl Drop for FreshnessGuard {`
  - Purpose: `FreshnessGuard` is a Rust RAII guard whose `Drop` implementation unsafely removes the `INFLIGHT_ENV` environment variable when the guard goes out of scope, clearing the freshness/in-flight marker. [crates/gcode/src/freshness.rs:195-200]
- `FreshnessGuard.drop` (method) component `FreshnessGuard.drop [method]` (`3d1b84ec-2be8-570c-920b-a124276a9dec`) lines 196-199 [crates/gcode/src/freshness.rs:196-199]
  - Signature: `fn drop(&mut self) {`
  - Purpose: On drop, it clears the inflight marker by unsafely removing the `INFLIGHT_ENV` environment variable via `std::env::remove_var`. [crates/gcode/src/freshness.rs:196-199]
- `context_for` (function) component `context_for [function]` (`d65f924d-9fc6-57c4-9336-56b7592a4b13`) lines 208-222 [crates/gcode/src/freshness.rs:208-222]
  - Signature: `fn context_for(root: &Path) -> Context {`
  - Purpose: Creates and returns a `Context` for a test project rooted at `root`, using a fixed PostgreSQL test database URL and project ID, `quiet = true`, default code-vector and indexing settings, `Single` index scope, and all external service/daemon fields unset. [crates/gcode/src/freshness.rs:208-222]
- `symbol_hash` (function) component `symbol_hash [function]` (`77932652-b9d3-5e58-aeac-0e74ca70877f`) lines 224-226 [crates/gcode/src/freshness.rs:224-226]
  - Signature: `fn symbol_hash(source: &[u8], start: usize, end: usize) -> String {`
  - Purpose: Computes a hash of the byte content between the specified start and end indices, returning it as a String. [crates/gcode/src/freshness.rs:224-226]
- `postgres_test_context` (function) component `postgres_test_context [function]` (`2525dc46-d85e-555e-8fe5-7b170c985f2d`) lines 228-245 [crates/gcode/src/freshness.rs:228-245]
  - Signature: `fn postgres_test_context(project_id: &str) -> Context {`
  - Purpose: 'postgres_test_context' constructs a quiet test 'Context' for a given 'project_id' by loading 'GCODE_POSTGRES_TEST_DATABASE_URL', verifying a read-write PostgreSQL connection, and populating the context with that database URL plus fixed default test configuration values. [crates/gcode/src/freshness.rs:228-245]
- `postgres_context_with_root` (function) component `postgres_context_with_root [function]` (`db970b82-436f-5da7-aff4-3adb610737a4`) lines 247-264 [crates/gcode/src/freshness.rs:247-264]
  - Signature: `fn postgres_context_with_root(project_id: &str, root: &Path) -> Context {`
  - Purpose: Creates a 'Context' for a specific project root and ID by reading 'GCODE_POSTGRES_TEST_DATABASE_URL', establishing a read-write PostgreSQL test connection to verify freshness, and populating the context with defaults for all non-Postgres backends and single-project indexing. [crates/gcode/src/freshness.rs:247-264]
- `hold_project_lock` (function) component `hold_project_lock [function]` (`a9f2c37b-f389-51a0-a072-9e0a37c211d8`) lines 266-273 [crates/gcode/src/freshness.rs:266-273]
  - Signature: `fn hold_project_lock(ctx: &Context) -> Client {`
  - Purpose: Opens a read-write PostgreSQL connection for 'ctx.database_url', computes the project’s advisory lock key from 'ctx.project_id', acquires 'pg_advisory_lock' on that key, and returns the locked connection. [crates/gcode/src/freshness.rs:266-273]
- `set_mtime` (function) component `set_mtime [function]` (`db6a25a4-60ce-5c9d-b451-3ad0dfb142fa`) lines 275-283 [crates/gcode/src/freshness.rs:275-283]
  - Signature: `fn set_mtime(path: &Path, time: SystemTime) {`
  - Purpose: Opens the file at 'path' with read/write access and sets its last-modified timestamp to 'time', panicking if either the open or timestamp update fails. [crates/gcode/src/freshness.rs:275-283]
- `invalidate_test_project` (function) component `invalidate_test_project [function]` (`c795b9ab-9a3a-5bc0-bb23-1af5b39714cf`) lines 285-290 [crates/gcode/src/freshness.rs:285-290]
  - Signature: `fn invalidate_test_project(ctx: &Context) {`
  - Purpose: Connects to the test PostgreSQL database with read-write access and calls the indexer’s 'invalidate' for the current project ID with no specific target, expecting both operations to succeed. [crates/gcode/src/freshness.rs:285-290]
- `full_index` (function) component `full_index [function]` (`a39e2d92-ff91-5403-8947-b40af9ff64bf`) lines 292-305 [crates/gcode/src/freshness.rs:292-305]
  - Signature: `fn full_index(ctx: &Context) {`
  - Purpose: Triggers a full project index by calling 'api::index_files' with the current 'project_root', no path filter or explicit files, 'full: true', and both 'require_cpp_semantics' and 'sync_projections' disabled, then panics on failure. [crates/gcode/src/freshness.rs:292-305]
- `no_freshness_env_short_circuits_project_refresh` (function) component `no_freshness_env_short_circuits_project_refresh [function]` (`882a8f06-d15a-56ac-9fd2-4ec5425a3638`) lines 312-320 [crates/gcode/src/freshness.rs:312-320]
  - Signature: `fn no_freshness_env_short_circuits_project_refresh() {`
  - Purpose: Verifies that when the in-flight freshness environment variable is set, 'ensure_fresh' short-circuits project-scope refresh checks and returns 'FreshnessStatus::Checked' without performing a refresh. [crates/gcode/src/freshness.rs:312-320]
- `busy_project_lock_skips_freshness_refresh` (function) component `busy_project_lock_skips_freshness_refresh [function]` (`6e155bbb-4b2d-50fd-ae4b-655f4a75e04f`) lines 328-335 [crates/gcode/src/freshness.rs:328-335]
  - Signature: `fn busy_project_lock_skips_freshness_refresh() {`
  - Purpose: Verifies that when a project lock is already held, 'ensure_fresh(&ctx, FreshnessScope::Project)' returns 'FreshnessStatus::SkippedBusy' instead of performing a freshness refresh. [crates/gcode/src/freshness.rs:328-335]
- `pre_gate_skips_lock_when_unchanged_and_trips_after_a_change` (function) component `pre_gate_skips_lock_when_unchanged_and_trips_after_a_change [function]` (`033cbdbd-93ca-508c-91e8-3189ffb13a43`) lines 343-382 [crates/gcode/src/freshness.rs:343-382]
  - Signature: `fn pre_gate_skips_lock_when_unchanged_and_trips_after_a_change() {`
  - Purpose: Verifies that 'ensure_fresh' bypasses the project advisory lock and returns 'Checked' when the indexed project is unchanged, but after a tracked file’s mtime advances it follows the lock path and returns 'SkippedBusy' if the lock is already held. [crates/gcode/src/freshness.rs:343-382]
- `symbol_slice_check_uses_stored_byte_range_hash` (function) component `symbol_slice_check_uses_stored_byte_range_hash [function]` (`636cf13c-5179-546e-9c0a-b6e7d3eeffaf`) lines 386-422 [crates/gcode/src/freshness.rs:386-422]
  - Signature: `fn symbol_slice_check_uses_stored_byte_range_hash() {`
  - Purpose: Verifies that 'symbol_slice_is_current' returns true when a symbol’s stored byte range and content hash match the current file contents, and false after the file is shifted so that the same symbol no longer occupies that exact slice. [crates/gcode/src/freshness.rs:386-422]

