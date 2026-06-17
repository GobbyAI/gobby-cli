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
  - 187-192
  - 196-199
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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/freshness.rs:13-16](crates/gcode/src/freshness.rs#L13-L16), [crates/gcode/src/freshness.rs:19-22](crates/gcode/src/freshness.rs#L19-L22), [crates/gcode/src/freshness.rs:24-83](crates/gcode/src/freshness.rs#L24-L83), [crates/gcode/src/freshness.rs:93-121](crates/gcode/src/freshness.rs#L93-L121), [crates/gcode/src/freshness.rs:123-144](crates/gcode/src/freshness.rs#L123-L144), [crates/gcode/src/freshness.rs:146-160](crates/gcode/src/freshness.rs#L146-L160), [crates/gcode/src/freshness.rs:162-182](crates/gcode/src/freshness.rs#L162-L182), [crates/gcode/src/freshness.rs:184](crates/gcode/src/freshness.rs#L184), [crates/gcode/src/freshness.rs:187-192](crates/gcode/src/freshness.rs#L187-L192), [crates/gcode/src/freshness.rs:196-199](crates/gcode/src/freshness.rs#L196-L199), [crates/gcode/src/freshness.rs:208-222](crates/gcode/src/freshness.rs#L208-L222), [crates/gcode/src/freshness.rs:224-226](crates/gcode/src/freshness.rs#L224-L226), [crates/gcode/src/freshness.rs:228-245](crates/gcode/src/freshness.rs#L228-L245), [crates/gcode/src/freshness.rs:247-264](crates/gcode/src/freshness.rs#L247-L264), [crates/gcode/src/freshness.rs:266-273](crates/gcode/src/freshness.rs#L266-L273), [crates/gcode/src/freshness.rs:275-283](crates/gcode/src/freshness.rs#L275-L283), [crates/gcode/src/freshness.rs:285-290](crates/gcode/src/freshness.rs#L285-L290), [crates/gcode/src/freshness.rs:292-305](crates/gcode/src/freshness.rs#L292-L305), [crates/gcode/src/freshness.rs:312-320](crates/gcode/src/freshness.rs#L312-L320), [crates/gcode/src/freshness.rs:328-335](crates/gcode/src/freshness.rs#L328-L335), [crates/gcode/src/freshness.rs:343-382](crates/gcode/src/freshness.rs#L343-L382), [crates/gcode/src/freshness.rs:386-422](crates/gcode/src/freshness.rs#L386-L422)

</details>

# crates/gcode/src/freshness.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This file implements freshness checks for the gcode index. `FreshnessScope` selects either a whole-project refresh or a targeted file refresh, and `FreshnessStatus` reports whether the check ran or was skipped because the project lock was busy. `ensure_fresh` is the entry point: it short-circuits when the in-flight env var is set, uses `project_needs_refresh` as a lock-free pre-gate for whole-project reads, then enters `FreshnessGuard` and takes the project advisory lock before reindexing either the full project or normalized explicit file paths. The remaining helpers support that flow by deciding when a project is stale, checking symbol slices and hashes, setting up test/Postgres contexts, holding locks, forcing mtimes to change, and providing test cases that cover the pre-gate, lock skipping, env short-circuiting, and symbol-slice freshness behavior.
[crates/gcode/src/freshness.rs:13-16]
[crates/gcode/src/freshness.rs:19-22]
[crates/gcode/src/freshness.rs:24-83]
[crates/gcode/src/freshness.rs:93-121]
[crates/gcode/src/freshness.rs:123-144]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `FreshnessScope` | type | `pub enum FreshnessScope {` | `FreshnessScope [type]` | `f61fe7d0-cb35-5fa9-ab58-80938ba8529f` | 13-16 [crates/gcode/src/freshness.rs:13-16] | Indexed type `FreshnessScope` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:13-16] |
| `FreshnessStatus` | type | `pub enum FreshnessStatus {` | `FreshnessStatus [type]` | `b4ef28ed-7a8f-597c-96af-fe09a246a5b1` | 19-22 [crates/gcode/src/freshness.rs:19-22] | Indexed type `FreshnessStatus` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:19-22] |
| `ensure_fresh` | function | `pub fn ensure_fresh(ctx: &Context, scope: FreshnessScope) -> anyhow::Result<FreshnessStatus> {` | `ensure_fresh [function]` | `c8af2110-ca73-5c67-932b-0c884dd653dd` | 24-83 [crates/gcode/src/freshness.rs:24-83] | Indexed function `ensure_fresh` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:24-83] |
| `project_needs_refresh` | function | `fn project_needs_refresh(ctx: &Context) -> anyhow::Result<bool> {` | `project_needs_refresh [function]` | `6970c8cd-4aa3-51fa-832f-cc2a313fa9b0` | 93-121 [crates/gcode/src/freshness.rs:93-121] | Indexed function `project_needs_refresh` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:93-121] |
| `ensure_symbol_fresh` | function | `pub fn ensure_symbol_fresh(ctx: &Context, id: &str) -> anyhow::Result<FreshnessStatus> {` | `ensure_symbol_fresh [function]` | `27e3bed4-eb80-526e-bb22-4465aa356e45` | 123-144 [crates/gcode/src/freshness.rs:123-144] | Indexed function `ensure_symbol_fresh` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:123-144] |
| `symbol_slice_is_current` | function | `fn symbol_slice_is_current(ctx: &Context, sym: &Symbol) -> bool {` | `symbol_slice_is_current [function]` | `9f86c033-896a-53a7-8c17-44012ae81185` | 146-160 [crates/gcode/src/freshness.rs:146-160] | Indexed function `symbol_slice_is_current` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:146-160] |
| `normalize_file_path` | function | `fn normalize_file_path(root: &Path, path: &Path) -> String {` | `normalize_file_path [function]` | `0279e83e-5e1a-5c8e-b538-9b116d7eab9b` | 162-182 [crates/gcode/src/freshness.rs:162-182] | Indexed function `normalize_file_path` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:162-182] |
| `FreshnessGuard` | class | `struct FreshnessGuard;` | `FreshnessGuard [class]` | `4d8390fd-df77-5e9c-bcb0-c4afa141068e` | 184-184 [crates/gcode/src/freshness.rs:184] | Indexed class `FreshnessGuard` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:184] |
| `FreshnessGuard::enter` | method | `fn enter() -> Self {` | `FreshnessGuard::enter [method]` | `71e65cf6-f900-5130-98c7-04dd8ed8ed40` | 187-192 [crates/gcode/src/freshness.rs:187-192] | Indexed method `FreshnessGuard::enter` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:187-192] |
| `FreshnessGuard::drop` | method | `fn drop(&mut self) {` | `FreshnessGuard::drop [method]` | `3d1b84ec-2be8-570c-920b-a124276a9dec` | 196-199 [crates/gcode/src/freshness.rs:196-199] | Indexed method `FreshnessGuard::drop` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:196-199] |
| `context_for` | function | `fn context_for(root: &Path) -> Context {` | `context_for [function]` | `d65f924d-9fc6-57c4-9336-56b7592a4b13` | 208-222 [crates/gcode/src/freshness.rs:208-222] | Indexed function `context_for` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:208-222] |
| `symbol_hash` | function | `fn symbol_hash(source: &[u8], start: usize, end: usize) -> String {` | `symbol_hash [function]` | `77932652-b9d3-5e58-aeac-0e74ca70877f` | 224-226 [crates/gcode/src/freshness.rs:224-226] | Indexed function `symbol_hash` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:224-226] |
| `postgres_test_context` | function | `fn postgres_test_context(project_id: &str) -> Context {` | `postgres_test_context [function]` | `2525dc46-d85e-555e-8fe5-7b170c985f2d` | 228-245 [crates/gcode/src/freshness.rs:228-245] | Indexed function `postgres_test_context` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:228-245] |
| `postgres_context_with_root` | function | `fn postgres_context_with_root(project_id: &str, root: &Path) -> Context {` | `postgres_context_with_root [function]` | `db970b82-436f-5da7-aff4-3adb610737a4` | 247-264 [crates/gcode/src/freshness.rs:247-264] | Indexed function `postgres_context_with_root` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:247-264] |
| `hold_project_lock` | function | `fn hold_project_lock(ctx: &Context) -> Client {` | `hold_project_lock [function]` | `a9f2c37b-f389-51a0-a072-9e0a37c211d8` | 266-273 [crates/gcode/src/freshness.rs:266-273] | Indexed function `hold_project_lock` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:266-273] |
| `set_mtime` | function | `fn set_mtime(path: &Path, time: SystemTime) {` | `set_mtime [function]` | `db6a25a4-60ce-5c9d-b451-3ad0dfb142fa` | 275-283 [crates/gcode/src/freshness.rs:275-283] | Indexed function `set_mtime` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:275-283] |
| `invalidate_test_project` | function | `fn invalidate_test_project(ctx: &Context) {` | `invalidate_test_project [function]` | `c795b9ab-9a3a-5bc0-bb23-1af5b39714cf` | 285-290 [crates/gcode/src/freshness.rs:285-290] | Indexed function `invalidate_test_project` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:285-290] |
| `full_index` | function | `fn full_index(ctx: &Context) {` | `full_index [function]` | `a39e2d92-ff91-5403-8947-b40af9ff64bf` | 292-305 [crates/gcode/src/freshness.rs:292-305] | Indexed function `full_index` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:292-305] |
| `no_freshness_env_short_circuits_project_refresh` | function | `fn no_freshness_env_short_circuits_project_refresh() {` | `no_freshness_env_short_circuits_project_refresh [function]` | `882a8f06-d15a-56ac-9fd2-4ec5425a3638` | 312-320 [crates/gcode/src/freshness.rs:312-320] | Indexed function `no_freshness_env_short_circuits_project_refresh` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:312-320] |
| `busy_project_lock_skips_freshness_refresh` | function | `fn busy_project_lock_skips_freshness_refresh() {` | `busy_project_lock_skips_freshness_refresh [function]` | `6e155bbb-4b2d-50fd-ae4b-655f4a75e04f` | 328-335 [crates/gcode/src/freshness.rs:328-335] | Indexed function `busy_project_lock_skips_freshness_refresh` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:328-335] |
| `pre_gate_skips_lock_when_unchanged_and_trips_after_a_change` | function | `fn pre_gate_skips_lock_when_unchanged_and_trips_after_a_change() {` | `pre_gate_skips_lock_when_unchanged_and_trips_after_a_change [function]` | `033cbdbd-93ca-508c-91e8-3189ffb13a43` | 343-382 [crates/gcode/src/freshness.rs:343-382] | Indexed function `pre_gate_skips_lock_when_unchanged_and_trips_after_a_change` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:343-382] |
| `symbol_slice_check_uses_stored_byte_range_hash` | function | `fn symbol_slice_check_uses_stored_byte_range_hash() {` | `symbol_slice_check_uses_stored_byte_range_hash [function]` | `636cf13c-5179-546e-9c0a-b6e7d3eeffaf` | 386-422 [crates/gcode/src/freshness.rs:386-422] | Indexed function `symbol_slice_check_uses_stored_byte_range_hash` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:386-422] |
