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
  - 187-192
  - 195-200
  - 196-199
  - 208-222
  - 224-226
  - 228-249
  - 251-274
  - 276-283
  - 285-293
  - 295-300
  - 302-315
  - 322-330
  - 334-343
  - 347-388
  - 392-428
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/freshness.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

`crates/gcode/src/freshness.rs` exposes 24 indexed API symbols.
[crates/gcode/src/freshness.rs:13-16]
[crates/gcode/src/freshness.rs:19-22]
[crates/gcode/src/freshness.rs:24-83]
[crates/gcode/src/freshness.rs:93-121]
[crates/gcode/src/freshness.rs:123-144]
[crates/gcode/src/freshness.rs:146-160]
[crates/gcode/src/freshness.rs:162-182]
[crates/gcode/src/freshness.rs:184]
[crates/gcode/src/freshness.rs:186-193]
[crates/gcode/src/freshness.rs:187-192]
[crates/gcode/src/freshness.rs:195-200]
[crates/gcode/src/freshness.rs:196-199]
[crates/gcode/src/freshness.rs:208-222]
[crates/gcode/src/freshness.rs:224-226]
[crates/gcode/src/freshness.rs:228-249]
[crates/gcode/src/freshness.rs:251-274]
[crates/gcode/src/freshness.rs:276-283]
[crates/gcode/src/freshness.rs:285-293]
[crates/gcode/src/freshness.rs:295-300]
[crates/gcode/src/freshness.rs:302-315]
[crates/gcode/src/freshness.rs:322-330]
[crates/gcode/src/freshness.rs:334-343]
[crates/gcode/src/freshness.rs:347-388]
[crates/gcode/src/freshness.rs:392-428]

## API Symbols

- `FreshnessScope` (type) component `FreshnessScope [type]` (`f61fe7d0-cb35-5fa9-ab58-80938ba8529f`) lines 13-16 [crates/gcode/src/freshness.rs:13-16]
  - Signature: `pub enum FreshnessScope {`
  - Purpose: Indexed type `FreshnessScope` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:13-16]
- `FreshnessStatus` (type) component `FreshnessStatus [type]` (`b4ef28ed-7a8f-597c-96af-fe09a246a5b1`) lines 19-22 [crates/gcode/src/freshness.rs:19-22]
  - Signature: `pub enum FreshnessStatus {`
  - Purpose: Indexed type `FreshnessStatus` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:19-22]
- `ensure_fresh` (function) component `ensure_fresh [function]` (`c8af2110-ca73-5c67-932b-0c884dd653dd`) lines 24-83 [crates/gcode/src/freshness.rs:24-83]
  - Signature: `pub fn ensure_fresh(ctx: &Context, scope: FreshnessScope) -> anyhow::Result<FreshnessStatus> {`
  - Purpose: Indexed function `ensure_fresh` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:24-83]
- `project_needs_refresh` (function) component `project_needs_refresh [function]` (`6970c8cd-4aa3-51fa-832f-cc2a313fa9b0`) lines 93-121 [crates/gcode/src/freshness.rs:93-121]
  - Signature: `fn project_needs_refresh(ctx: &Context) -> anyhow::Result<bool> {`
  - Purpose: Indexed function `project_needs_refresh` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:93-121]
- `ensure_symbol_fresh` (function) component `ensure_symbol_fresh [function]` (`27e3bed4-eb80-526e-bb22-4465aa356e45`) lines 123-144 [crates/gcode/src/freshness.rs:123-144]
  - Signature: `pub fn ensure_symbol_fresh(ctx: &Context, id: &str) -> anyhow::Result<FreshnessStatus> {`
  - Purpose: Indexed function `ensure_symbol_fresh` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:123-144]
- `symbol_slice_is_current` (function) component `symbol_slice_is_current [function]` (`9f86c033-896a-53a7-8c17-44012ae81185`) lines 146-160 [crates/gcode/src/freshness.rs:146-160]
  - Signature: `fn symbol_slice_is_current(ctx: &Context, sym: &Symbol) -> bool {`
  - Purpose: Returns `true` only when `sym.content_hash` is non-empty, the symbol’s file can be read from `ctx.project_root.join(sym.file_path)`, and the hash computed over `sym.byte_start..sym.byte_end` exactly matches `sym.content_hash`. [crates/gcode/src/freshness.rs:146-160]
- `normalize_file_path` (function) component `normalize_file_path [function]` (`0279e83e-5e1a-5c8e-b538-9b116d7eab9b`) lines 162-182 [crates/gcode/src/freshness.rs:162-182]
  - Signature: `fn normalize_file_path(root: &Path, path: &Path) -> String {`
  - Purpose: Resolves `path` against `root` when relative, canonicalizes both paths, returns the canonical path relative to the canonicalized `root` when it lies under that root, and otherwise falls back to the original `path`, converted lossily to a `String`. [crates/gcode/src/freshness.rs:162-182]
- `FreshnessGuard` (class) component `FreshnessGuard [class]` (`4d8390fd-df77-5e9c-bcb0-c4afa141068e`) lines 184-184 [crates/gcode/src/freshness.rs:184]
  - Signature: `struct FreshnessGuard;`
  - Purpose: Indexed class `FreshnessGuard` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:184]
- `FreshnessGuard` (class) component `FreshnessGuard [class]` (`e46d16c8-6fb7-5d4e-8bbe-25c4d6d9a9ff`) lines 186-193 [crates/gcode/src/freshness.rs:186-193]
  - Signature: `impl FreshnessGuard {`
  - Purpose: Indexed class `FreshnessGuard` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:186-193]
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
  - Purpose: Indexed function `symbol_hash` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:224-226]
- `postgres_test_context` (function) component `postgres_test_context [function]` (`2525dc46-d85e-555e-8fe5-7b170c985f2d`) lines 228-249 [crates/gcode/src/freshness.rs:228-249]
  - Signature: `fn postgres_test_context(project_id: &str) -> Option<Context> {`
  - Purpose: Returns a test `Context` for the given `project_id` only when `GCODE_POSTGRES_TEST_DATABASE_URL` is set and `db::connect_readwrite` succeeds, otherwise it logs that the PostgreSQL hub is unavailable and returns `None`. [crates/gcode/src/freshness.rs:228-249]
- `postgres_context_with_root` (function) component `postgres_context_with_root [function]` (`0d55b484-c5bd-5508-b2d2-afe0c8b67554`) lines 251-274 [crates/gcode/src/freshness.rs:251-274]
  - Signature: `fn postgres_context_with_root(project_id: &str, root: &Path) -> Option<Context> {`
  - Purpose: Reads `GCODE_POSTGRES_TEST_DATABASE_URL`, verifies it can open a read-write PostgreSQL connection, and returns a quiet `Context` configured for the given `project_id` and `root` with default indexing/vector settings, or `None` after logging a skip message if the database is unavailable. [crates/gcode/src/freshness.rs:251-274]
- `hold_project_lock` (function) component `hold_project_lock [function]` (`33ef1321-30a3-547d-8439-157e57e309d0`) lines 276-283 [crates/gcode/src/freshness.rs:276-283]
  - Signature: `fn hold_project_lock(ctx: &Context) -> Client {`
  - Purpose: It opens a read-write PostgreSQL connection for `ctx.database_url`, computes the project-specific advisory lock key from `ctx.project_id`, acquires that lock with `pg_advisory_lock`, and returns the locked `Client` connection. [crates/gcode/src/freshness.rs:276-283]
- `set_mtime` (function) component `set_mtime [function]` (`f028e1a6-8ba1-5105-8ba0-417521ce5f72`) lines 285-293 [crates/gcode/src/freshness.rs:285-293]
  - Signature: `fn set_mtime(path: &Path, time: SystemTime) {`
  - Purpose: Opens the file at `path` with read-write access and sets its last-modified timestamp to `time`, panicking if either operation fails. [crates/gcode/src/freshness.rs:285-293]
- `invalidate_test_project` (function) component `invalidate_test_project [function]` (`3720e36a-f4b2-548a-b670-5ad04ba03108`) lines 295-300 [crates/gcode/src/freshness.rs:295-300]
  - Signature: `fn invalidate_test_project(ctx: &Context) {`
  - Purpose: Connects to the PostgreSQL database at `ctx.database_url` with a read-write handle and invalidates the index for `ctx.project_id` via `crate::index::indexer::invalidate(..., None)`, panicking if either operation fails. [crates/gcode/src/freshness.rs:295-300]
- `full_index` (function) component `full_index [function]` (`a6f0e81f-88f7-5283-92cb-a725e91241fb`) lines 302-315 [crates/gcode/src/freshness.rs:302-315]
  - Signature: `fn full_index(ctx: &Context) {`
  - Purpose: Calls `api::index_files` with the context’s project root in a full-index mode (`path_filter: None`, no explicit files, no C++ semantics, no projection sync) and panics if indexing fails. [crates/gcode/src/freshness.rs:302-315]
- `no_freshness_env_short_circuits_project_refresh` (function) component `no_freshness_env_short_circuits_project_refresh [function]` (`5713ef22-5332-5977-88da-72674eb6e997`) lines 322-330 [crates/gcode/src/freshness.rs:322-330]
  - Signature: `fn no_freshness_env_short_circuits_project_refresh() {`
  - Purpose: Verifies that setting `INFLIGHT_ENV` short-circuits `ensure_fresh` for `FreshnessScope::Project`, causing it to return `FreshnessStatus::Checked` without performing a freshness refresh. [crates/gcode/src/freshness.rs:322-330]
- `busy_project_lock_skips_freshness_refresh` (function) component `busy_project_lock_skips_freshness_refresh [function]` (`cb13391f-f830-5379-9017-7f0e180b499f`) lines 334-343 [crates/gcode/src/freshness.rs:334-343]
  - Signature: `fn busy_project_lock_skips_freshness_refresh() {`
  - Purpose: Indexed function `busy_project_lock_skips_freshness_refresh` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:334-343]
- `pre_gate_skips_lock_when_unchanged_and_trips_after_a_change` (function) component `pre_gate_skips_lock_when_unchanged_and_trips_after_a_change [function]` (`16703327-90f7-56c2-9f86-373a36770ed1`) lines 347-388 [crates/gcode/src/freshness.rs:347-388]
  - Signature: `fn pre_gate_skips_lock_when_unchanged_and_trips_after_a_change() {`
  - Purpose: Indexed function `pre_gate_skips_lock_when_unchanged_and_trips_after_a_change` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:347-388]
- `symbol_slice_check_uses_stored_byte_range_hash` (function) component `symbol_slice_check_uses_stored_byte_range_hash [function]` (`dd72a5da-6d0b-5f25-945e-39d1f67e6232`) lines 392-428 [crates/gcode/src/freshness.rs:392-428]
  - Signature: `fn symbol_slice_check_uses_stored_byte_range_hash() {`
  - Purpose: Indexed function `symbol_slice_check_uses_stored_byte_range_hash` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:392-428]

