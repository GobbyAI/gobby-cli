---
title: crates/gcode/src/index_lock.rs
type: code_file
provenance:
- file: crates/gcode/src/index_lock.rs
  ranges:
  - 15-21
  - 23-30
  - 24-29
  - 33-36
  - 38-47
  - 49-52
  - 54-92
  - 94-125
  - 127-132
  - 134-146
  - 148-154
  - 156-160
  - 162-191
  - 163-190
  - 200-214
  - 216-225
  - 227-233
  - 236-238
  - 241-243
  - 250-268
  - 272-298
  - 302-320
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index_lock.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

`crates/gcode/src/index_lock.rs` exposes 22 indexed API symbols.
[crates/gcode/src/index_lock.rs:15-21]
[crates/gcode/src/index_lock.rs:23-30]
[crates/gcode/src/index_lock.rs:24-29]
[crates/gcode/src/index_lock.rs:33-36]
[crates/gcode/src/index_lock.rs:38-47]

## API Symbols

- `IndexLockPolicy` (type) component `IndexLockPolicy [type]` (`a4a4ee4b-ba48-5dc4-aa1a-9bf259639711`) lines 15-21 [crates/gcode/src/index_lock.rs:15-21]
  - Signature: `pub(crate) enum IndexLockPolicy {`
  - Purpose: Indexed type `IndexLockPolicy` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:15-21]
- `IndexLockPolicy` (class) component `IndexLockPolicy [class]` (`d9a68714-3c34-529b-b434-67faab0c000b`) lines 23-30 [crates/gcode/src/index_lock.rs:23-30]
  - Signature: `impl IndexLockPolicy {`
  - Purpose: `IndexLockPolicy` provides a `brief_freshness_try` constructor that returns the `BriefTry` variant configured with a 150 ms total wait budget and a 25 ms polling interval for short-lived freshness lock acquisition attempts. [crates/gcode/src/index_lock.rs:23-30]
- `IndexLockPolicy.brief_freshness_try` (method) component `IndexLockPolicy.brief_freshness_try [method]` (`b9c7b001-b46b-5d26-95f4-97ad89733a4b`) lines 24-29 [crates/gcode/src/index_lock.rs:24-29]
  - Signature: `pub(crate) fn brief_freshness_try() -> Self {`
  - Purpose: Constructs and returns `Self::BriefTry` with a `total_wait` of 150 ms and a `poll` interval of 25 ms. [crates/gcode/src/index_lock.rs:24-29]
- `IndexLockResult` (type) component `IndexLockResult [type]` (`cfaa2da9-4ca0-5c8b-9cc1-e9bbc141950a`) lines 33-36 [crates/gcode/src/index_lock.rs:33-36]
  - Signature: `pub(crate) enum IndexLockResult<T> {`
  - Purpose: Indexed type `IndexLockResult` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:33-36]
- `with_project_lock` (function) component `with_project_lock [function]` (`c96a3a9a-8ba5-521a-9057-fe9cc2eafe82`) lines 38-47 [crates/gcode/src/index_lock.rs:38-47]
  - Signature: `pub(crate) fn with_project_lock<T>(`
  - Purpose: Attempts to acquire the project index lock with the given `Context` and `IndexLockPolicy`, returning `IndexLockResult::Busy` if the lock cannot be obtained, or otherwise running `f` under the acquired lock and wrapping its successful result in `IndexLockResult::Acquired` while propagating any error. [crates/gcode/src/index_lock.rs:38-47]
- `ProjectIndexLockAttempt` (type) component `ProjectIndexLockAttempt [type]` (`9ee44c9c-cb2e-5877-8df8-97cff4fa795a`) lines 49-52 [crates/gcode/src/index_lock.rs:49-52]
  - Signature: `enum ProjectIndexLockAttempt {`
  - Purpose: Indexed type `ProjectIndexLockAttempt` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:49-52]
- `acquire_project_lock` (function) component `acquire_project_lock [function]` (`46dad12d-f8f2-5580-87a9-9adf1d6fe92b`) lines 54-92 [crates/gcode/src/index_lock.rs:54-92]
  - Signature: `fn acquire_project_lock(`
  - Purpose: Connects to PostgreSQL, attempts to acquire a project-scoped advisory lock using either blocking or bounded retry semantics from `IndexLockPolicy`, emits a wait-time warning if acquisition is slow, and returns either an owned `ProjectIndexLock` guard or `Busy`. [crates/gcode/src/index_lock.rs:54-92]
- `try_advisory_lock_until` (function) component `try_advisory_lock_until [function]` (`bee371b0-6a42-52ef-947a-4bcd1ba343eb`) lines 94-125 [crates/gcode/src/index_lock.rs:94-125]
  - Signature: `fn try_advisory_lock_until(`
  - Purpose: Repeatedly calls `try_advisory_lock` on `conn` for `key` until it succeeds or `total_wait` elapses, sleeping for `max(poll, MIN_LOCK_POLL)` capped by the remaining timeout (or yielding the thread when `poll` is zero), and returns `Ok(true)` on lock acquisition or `Ok(false)` on timeout. [crates/gcode/src/index_lock.rs:94-125]
- `try_advisory_lock` (function) component `try_advisory_lock [function]` (`e1274b3b-e147-5bd2-ab53-7046b3aa4485`) lines 127-132 [crates/gcode/src/index_lock.rs:127-132]
  - Signature: `fn try_advisory_lock(conn: &mut Client, key: i64) -> anyhow::Result<bool> {`
  - Purpose: Attempts to acquire a PostgreSQL advisory lock for the given `i64` key via `pg_try_advisory_lock($1)`, returning the resulting boolean and wrapping any query or row-decoding failure in `anyhow::Error` context. [crates/gcode/src/index_lock.rs:127-132]
- `project_lock_key` (function) component `project_lock_key [function]` (`4e2cddcd-9637-56c6-80e9-c3709ec155c5`) lines 134-146 [crates/gcode/src/index_lock.rs:134-146]
  - Signature: `pub(crate) fn project_lock_key(project_id: &str) -> i64 {`
  - Purpose: Computes a deterministic 64-bit PostgreSQL advisory lock key for a project by SHA-256 hashing the `b"gcode:index:"` namespace plus `project_id` and interpreting the first 8 digest bytes as a big-endian `i64`. [crates/gcode/src/index_lock.rs:134-146]
- `advisory_lock_delay_warning` (function) component `advisory_lock_delay_warning [function]` (`35d4b618-a1a0-57ca-8204-c2c53ddfba5e`) lines 148-154 [crates/gcode/src/index_lock.rs:148-154]
  - Signature: `fn advisory_lock_delay_warning() -> Duration {`
  - Purpose: Returns a warning-threshold `Duration` by reading `ADVISORY_LOCK_DELAY_WARNING_MS_ENV` as a `u64` millisecond value and falling back to `DEFAULT_ADVISORY_LOCK_DELAY_WARNING_MS` if the variable is unset or unparsable. [crates/gcode/src/index_lock.rs:148-154]
- `ProjectIndexLock` (class) component `ProjectIndexLock [class]` (`2652f13c-4e1b-55fe-92ec-e23feeea62a3`) lines 156-160 [crates/gcode/src/index_lock.rs:156-160]
  - Signature: `struct ProjectIndexLock {`
  - Purpose: `ProjectIndexLock` is a lock handle that holds a `Client` connection, a 64-bit lock key, and a `quiet` flag to control output during project index locking operations. [crates/gcode/src/index_lock.rs:156-160]
- `ProjectIndexLock` (class) component `ProjectIndexLock [class]` (`672ee214-3ed6-5c37-a4aa-2884f5061138`) lines 162-191 [crates/gcode/src/index_lock.rs:162-191]
  - Signature: `impl Drop for ProjectIndexLock {`
  - Purpose: `ProjectIndexLock` is an RAII guard that attempts to release a PostgreSQL advisory lock with `pg_advisory_unlock(self.key)` on drop and logs or optionally prints warnings if the unlock fails or the lock was not held. [crates/gcode/src/index_lock.rs:162-191]
- `ProjectIndexLock.drop` (method) component `ProjectIndexLock.drop [method]` (`f4f1ce2c-c984-53f3-9675-e52d858a778c`) lines 163-190 [crates/gcode/src/index_lock.rs:163-190]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Releases the PostgreSQL advisory lock identified by `self.key` via `pg_advisory_unlock`, and logs or optionally prints a warning if the unlock fails, reports the lock was not held, or the returned value cannot be decoded. [crates/gcode/src/index_lock.rs:163-190]
- `context_for` (function) component `context_for [function]` (`85b117b7-bb60-5d10-a9be-cf809f79fe6a`) lines 200-214 [crates/gcode/src/index_lock.rs:200-214]
  - Signature: `fn context_for(database_url: String, project_id: &str) -> Context {`
  - Purpose: `context_for` constructs and returns a `Context` initialized with the supplied `database_url` and `project_id`, a fixed temporary `project_root`, `quiet = true`, no FalkorDB/Qdrant/embedding/daemon URL, default vector and indexing settings, and `ProjectIndexScope::Single`. [crates/gcode/src/index_lock.rs:200-214]
- `connect_postgres_test_db` (function) component `connect_postgres_test_db [function]` (`73c49d7e-d58b-5aae-8ba5-43ab46c514cb`) lines 216-225 [crates/gcode/src/index_lock.rs:216-225]
  - Signature: `fn connect_postgres_test_db() -> Option<String> {`
  - Purpose: Returns `Some(database_url)` only if `GCODE_POSTGRES_TEST_DATABASE_URL` is set and `db::connect_readwrite` can open it, otherwise logs that PostgreSQL is unavailable for advisory-lock tests and returns `None`. [crates/gcode/src/index_lock.rs:216-225]
- `hold_project_lock` (function) component `hold_project_lock [function]` (`e2673ab8-a2ba-5e22-a7aa-c246d740b25b`) lines 227-233 [crates/gcode/src/index_lock.rs:227-233]
  - Signature: `fn hold_project_lock(database_url: &str, project_id: &str) -> Client {`
  - Purpose: Opens a read-write PostgreSQL connection to `database_url`, computes the advisory lock key for `project_id`, acquires `pg_advisory_lock` on that key, and returns the live `Client` while the lock is held. [crates/gcode/src/index_lock.rs:227-233]
- `project_lock_key_matches_fixture` (function) component `project_lock_key_matches_fixture [function]` (`a4d87a32-3a04-5506-b8bf-10947b418925`) lines 236-238 [crates/gcode/src/index_lock.rs:236-238]
  - Signature: `fn project_lock_key_matches_fixture() {`
  - Purpose: Verifies that `project_lock_key("proj")` deterministically returns the fixture hash value `-9102099203869195108`. [crates/gcode/src/index_lock.rs:236-238]
- `project_lock_key_is_project_scoped` (function) component `project_lock_key_is_project_scoped [function]` (`ee8443d6-54d8-542f-8b50-b2b2198707ef`) lines 241-243 [crates/gcode/src/index_lock.rs:241-243]
  - Signature: `fn project_lock_key_is_project_scoped() {`
  - Purpose: Verifies that `project_lock_key` is scoped per project by asserting it returns different lock keys for `"proj-a"` and `"proj-b"`. [crates/gcode/src/index_lock.rs:241-243]
- `brief_try_returns_busy_while_same_project_lock_is_held` (function) component `brief_try_returns_busy_while_same_project_lock_is_held [function]` (`7928a51c-6844-59ab-bdd4-5d57316208a4`) lines 250-268 [crates/gcode/src/index_lock.rs:250-268]
  - Signature: `fn brief_try_returns_busy_while_same_project_lock_is_held() {`
  - Purpose: Verifies that `with_project_lock` using `IndexLockPolicy::BriefTry` returns `IndexLockResult::Busy` when the same project lock is already held, and does not execute the provided closure. [crates/gcode/src/index_lock.rs:250-268]
- `wait_blocks_until_same_project_lock_is_released` (function) component `wait_blocks_until_same_project_lock_is_released [function]` (`7d26c8ba-20d2-5d22-b2bb-44fb96310daf`) lines 272-298 [crates/gcode/src/index_lock.rs:272-298]
  - Signature: `fn wait_blocks_until_same_project_lock_is_released() {`
  - Purpose: Verifies that `with_project_lock` under `IndexLockPolicy::Wait` blocks on an already-held same-project lock, then completes successfully and returns `IndexLockResult::Acquired(())` once the lock is dropped. [crates/gcode/src/index_lock.rs:272-298]
- `different_project_ids_do_not_block_each_other` (function) component `different_project_ids_do_not_block_each_other [function]` (`ab61e402-2065-5151-b229-0f8e4749550d`) lines 302-320 [crates/gcode/src/index_lock.rs:302-320]
  - Signature: `fn different_project_ids_do_not_block_each_other() {`
  - Purpose: Verifies that holding a PostgreSQL project lock for one project ID does not prevent `with_project_lock` from immediately acquiring and executing under a different project ID, returning `IndexLockResult::Acquired(7)`. [crates/gcode/src/index_lock.rs:302-320]

