---
title: crates/gcode/src/index_lock.rs
type: code_file
provenance:
- file: crates/gcode/src/index_lock.rs
  ranges:
  - 15-21
  - 23-30
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
  - 200-214
  - 216-221
  - 223-229
  - 232-234
  - 237-239
  - 250-266
  - 274-298
  - 306-322
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index_lock.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Implements project-scoped PostgreSQL advisory locking for gcode indexing. It defines lock policies and results, computes a deterministic per-project lock key, acquires the lock with either blocking or brief retry semantics, warns if acquisition is slow, and returns a RAII guard that releases the lock on drop.

The helper `with_project_lock` runs a closure only after the lock is acquired and reports `Busy` otherwise. Test helpers and cases verify key generation, lock contention behavior, and that different project IDs do not block each other.
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
- `connect_postgres_test_db` (function) component `connect_postgres_test_db [function]` (`73c49d7e-d58b-5aae-8ba5-43ab46c514cb`) lines 216-221 [crates/gcode/src/index_lock.rs:216-221]
  - Signature: `fn connect_postgres_test_db() -> String {`
  - Purpose: Indexed function `connect_postgres_test_db` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:216-221]
- `hold_project_lock` (function) component `hold_project_lock [function]` (`8a3d943a-86b7-5bc1-bffc-fa23556511db`) lines 223-229 [crates/gcode/src/index_lock.rs:223-229]
  - Signature: `fn hold_project_lock(database_url: &str, project_id: &str) -> Client {`
  - Purpose: Indexed function `hold_project_lock` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:223-229]
- `project_lock_key_matches_fixture` (function) component `project_lock_key_matches_fixture [function]` (`b4c162d0-b497-5609-8a19-68e9a30e9118`) lines 232-234 [crates/gcode/src/index_lock.rs:232-234]
  - Signature: `fn project_lock_key_matches_fixture() {`
  - Purpose: Indexed function `project_lock_key_matches_fixture` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:232-234]
- `project_lock_key_is_project_scoped` (function) component `project_lock_key_is_project_scoped [function]` (`03e58d56-06c2-5630-a74d-1577eb76c28e`) lines 237-239 [crates/gcode/src/index_lock.rs:237-239]
  - Signature: `fn project_lock_key_is_project_scoped() {`
  - Purpose: Verifies that 'project_lock_key' generates project-scoped lock keys by asserting the keys for '"proj-a"' and '"proj-b"' are not equal. [crates/gcode/src/index_lock.rs:237-239]
- `brief_try_returns_busy_while_same_project_lock_is_held` (function) component `brief_try_returns_busy_while_same_project_lock_is_held [function]` (`33180984-54e1-59b8-a3cf-d142488fe408`) lines 250-266 [crates/gcode/src/index_lock.rs:250-266]
  - Signature: `fn brief_try_returns_busy_while_same_project_lock_is_held() {`
  - Purpose: Verifies that 'with_project_lock' using 'IndexLockPolicy::BriefTry' returns 'IndexLockResult::Busy' without executing the closure when the same project lock is already held. [crates/gcode/src/index_lock.rs:250-266]
- `wait_blocks_until_same_project_lock_is_released` (function) component `wait_blocks_until_same_project_lock_is_released [function]` (`b0ff08fa-643c-5981-89a5-0621fbcb8362`) lines 274-298 [crates/gcode/src/index_lock.rs:274-298]
  - Signature: `fn wait_blocks_until_same_project_lock_is_released() {`
  - Purpose: Verifies that 'with_project_lock(..., IndexLockPolicy::Wait, ...)' blocks until an existing lock on the same project is released, then successfully acquires the lock and returns 'IndexLockResult::Acquired(())'. [crates/gcode/src/index_lock.rs:274-298]
- `different_project_ids_do_not_block_each_other` (function) component `different_project_ids_do_not_block_each_other [function]` (`c184843a-46aa-5af2-b2fa-69aa47f56f8c`) lines 306-322 [crates/gcode/src/index_lock.rs:306-322]
  - Signature: `fn different_project_ids_do_not_block_each_other() {`
  - Purpose: Verifies that a project index lock held for one project ID does not prevent 'with_project_lock' from acquiring and executing successfully for a different project ID, returning 'IndexLockResult::Acquired(7)'. [crates/gcode/src/index_lock.rs:306-322]

