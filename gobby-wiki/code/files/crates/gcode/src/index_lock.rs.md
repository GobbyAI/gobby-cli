---
title: crates/gcode/src/index_lock.rs
type: code_file
provenance:
- file: crates/gcode/src/index_lock.rs
  ranges:
  - 15-21
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
  - 163-190
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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index_lock.rs:15-21](crates/gcode/src/index_lock.rs#L15-L21), [crates/gcode/src/index_lock.rs:24-29](crates/gcode/src/index_lock.rs#L24-L29), [crates/gcode/src/index_lock.rs:33-36](crates/gcode/src/index_lock.rs#L33-L36), [crates/gcode/src/index_lock.rs:38-47](crates/gcode/src/index_lock.rs#L38-L47), [crates/gcode/src/index_lock.rs:49-52](crates/gcode/src/index_lock.rs#L49-L52), [crates/gcode/src/index_lock.rs:54-92](crates/gcode/src/index_lock.rs#L54-L92), [crates/gcode/src/index_lock.rs:94-125](crates/gcode/src/index_lock.rs#L94-L125), [crates/gcode/src/index_lock.rs:127-132](crates/gcode/src/index_lock.rs#L127-L132), [crates/gcode/src/index_lock.rs:134-146](crates/gcode/src/index_lock.rs#L134-L146), [crates/gcode/src/index_lock.rs:148-154](crates/gcode/src/index_lock.rs#L148-L154), [crates/gcode/src/index_lock.rs:156-160](crates/gcode/src/index_lock.rs#L156-L160), [crates/gcode/src/index_lock.rs:163-190](crates/gcode/src/index_lock.rs#L163-L190), [crates/gcode/src/index_lock.rs:200-214](crates/gcode/src/index_lock.rs#L200-L214), [crates/gcode/src/index_lock.rs:216-221](crates/gcode/src/index_lock.rs#L216-L221), [crates/gcode/src/index_lock.rs:223-229](crates/gcode/src/index_lock.rs#L223-L229), [crates/gcode/src/index_lock.rs:232-234](crates/gcode/src/index_lock.rs#L232-L234), [crates/gcode/src/index_lock.rs:237-239](crates/gcode/src/index_lock.rs#L237-L239), [crates/gcode/src/index_lock.rs:250-266](crates/gcode/src/index_lock.rs#L250-L266), [crates/gcode/src/index_lock.rs:274-298](crates/gcode/src/index_lock.rs#L274-L298), [crates/gcode/src/index_lock.rs:306-322](crates/gcode/src/index_lock.rs#L306-L322)

</details>

# crates/gcode/src/index_lock.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Implements project-scoped PostgreSQL advisory locking for gcode indexing. `IndexLockPolicy` selects either a blocking `Wait` lock or a short `BriefTry` freshness check, and `with_project_lock` wraps that acquisition so callers either run their closure under the lock or get `Busy`. The lower-level helpers connect to the database, derive a stable lock key from `project_id`, retry `pg_try_advisory_lock` until a deadline, and emit a warning when lock acquisition is slow. `ProjectIndexLock` is an RAII guard that releases the advisory lock on drop, and the tests verify key derivation, project isolation, and the difference between brief try and blocking behavior.
[crates/gcode/src/index_lock.rs:15-21]
[crates/gcode/src/index_lock.rs:24-29]
[crates/gcode/src/index_lock.rs:33-36]
[crates/gcode/src/index_lock.rs:38-47]
[crates/gcode/src/index_lock.rs:49-52]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `IndexLockPolicy` | type | `pub(crate) enum IndexLockPolicy {` | `IndexLockPolicy [type]` | `a4a4ee4b-ba48-5dc4-aa1a-9bf259639711` | 15-21 [crates/gcode/src/index_lock.rs:15-21] | Indexed type `IndexLockPolicy` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:15-21] |
| `IndexLockPolicy::brief_freshness_try` | method | `pub(crate) fn brief_freshness_try() -> Self {` | `IndexLockPolicy::brief_freshness_try [method]` | `b9c7b001-b46b-5d26-95f4-97ad89733a4b` | 24-29 [crates/gcode/src/index_lock.rs:24-29] | Indexed method `IndexLockPolicy::brief_freshness_try` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:24-29] |
| `IndexLockResult` | type | `pub(crate) enum IndexLockResult<T> {` | `IndexLockResult [type]` | `cfaa2da9-4ca0-5c8b-9cc1-e9bbc141950a` | 33-36 [crates/gcode/src/index_lock.rs:33-36] | Indexed type `IndexLockResult` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:33-36] |
| `with_project_lock` | function | `pub(crate) fn with_project_lock<T>(` | `with_project_lock [function]` | `c96a3a9a-8ba5-521a-9057-fe9cc2eafe82` | 38-47 [crates/gcode/src/index_lock.rs:38-47] | Indexed function `with_project_lock` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:38-47] |
| `ProjectIndexLockAttempt` | type | `enum ProjectIndexLockAttempt {` | `ProjectIndexLockAttempt [type]` | `9ee44c9c-cb2e-5877-8df8-97cff4fa795a` | 49-52 [crates/gcode/src/index_lock.rs:49-52] | Indexed type `ProjectIndexLockAttempt` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:49-52] |
| `acquire_project_lock` | function | `fn acquire_project_lock(` | `acquire_project_lock [function]` | `46dad12d-f8f2-5580-87a9-9adf1d6fe92b` | 54-92 [crates/gcode/src/index_lock.rs:54-92] | Indexed function `acquire_project_lock` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:54-92] |
| `try_advisory_lock_until` | function | `fn try_advisory_lock_until(` | `try_advisory_lock_until [function]` | `bee371b0-6a42-52ef-947a-4bcd1ba343eb` | 94-125 [crates/gcode/src/index_lock.rs:94-125] | Indexed function `try_advisory_lock_until` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:94-125] |
| `try_advisory_lock` | function | `fn try_advisory_lock(conn: &mut Client, key: i64) -> anyhow::Result<bool> {` | `try_advisory_lock [function]` | `e1274b3b-e147-5bd2-ab53-7046b3aa4485` | 127-132 [crates/gcode/src/index_lock.rs:127-132] | Indexed function `try_advisory_lock` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:127-132] |
| `project_lock_key` | function | `pub(crate) fn project_lock_key(project_id: &str) -> i64 {` | `project_lock_key [function]` | `4e2cddcd-9637-56c6-80e9-c3709ec155c5` | 134-146 [crates/gcode/src/index_lock.rs:134-146] | Indexed function `project_lock_key` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:134-146] |
| `advisory_lock_delay_warning` | function | `fn advisory_lock_delay_warning() -> Duration {` | `advisory_lock_delay_warning [function]` | `35d4b618-a1a0-57ca-8204-c2c53ddfba5e` | 148-154 [crates/gcode/src/index_lock.rs:148-154] | Indexed function `advisory_lock_delay_warning` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:148-154] |
| `ProjectIndexLock` | class | `struct ProjectIndexLock {` | `ProjectIndexLock [class]` | `2652f13c-4e1b-55fe-92ec-e23feeea62a3` | 156-160 [crates/gcode/src/index_lock.rs:156-160] | Indexed class `ProjectIndexLock` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:156-160] |
| `ProjectIndexLock::drop` | method | `fn drop(&mut self) {` | `ProjectIndexLock::drop [method]` | `f4f1ce2c-c984-53f3-9675-e52d858a778c` | 163-190 [crates/gcode/src/index_lock.rs:163-190] | Indexed method `ProjectIndexLock::drop` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:163-190] |
| `context_for` | function | `fn context_for(database_url: String, project_id: &str) -> Context {` | `context_for [function]` | `85b117b7-bb60-5d10-a9be-cf809f79fe6a` | 200-214 [crates/gcode/src/index_lock.rs:200-214] | Indexed function `context_for` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:200-214] |
| `connect_postgres_test_db` | function | `fn connect_postgres_test_db() -> String {` | `connect_postgres_test_db [function]` | `73c49d7e-d58b-5aae-8ba5-43ab46c514cb` | 216-221 [crates/gcode/src/index_lock.rs:216-221] | Indexed function `connect_postgres_test_db` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:216-221] |
| `hold_project_lock` | function | `fn hold_project_lock(database_url: &str, project_id: &str) -> Client {` | `hold_project_lock [function]` | `8a3d943a-86b7-5bc1-bffc-fa23556511db` | 223-229 [crates/gcode/src/index_lock.rs:223-229] | Indexed function `hold_project_lock` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:223-229] |
| `project_lock_key_matches_fixture` | function | `fn project_lock_key_matches_fixture() {` | `project_lock_key_matches_fixture [function]` | `b4c162d0-b497-5609-8a19-68e9a30e9118` | 232-234 [crates/gcode/src/index_lock.rs:232-234] | Indexed function `project_lock_key_matches_fixture` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:232-234] |
| `project_lock_key_is_project_scoped` | function | `fn project_lock_key_is_project_scoped() {` | `project_lock_key_is_project_scoped [function]` | `03e58d56-06c2-5630-a74d-1577eb76c28e` | 237-239 [crates/gcode/src/index_lock.rs:237-239] | Indexed function `project_lock_key_is_project_scoped` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:237-239] |
| `brief_try_returns_busy_while_same_project_lock_is_held` | function | `fn brief_try_returns_busy_while_same_project_lock_is_held() {` | `brief_try_returns_busy_while_same_project_lock_is_held [function]` | `33180984-54e1-59b8-a3cf-d142488fe408` | 250-266 [crates/gcode/src/index_lock.rs:250-266] | Indexed function `brief_try_returns_busy_while_same_project_lock_is_held` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:250-266] |
| `wait_blocks_until_same_project_lock_is_released` | function | `fn wait_blocks_until_same_project_lock_is_released() {` | `wait_blocks_until_same_project_lock_is_released [function]` | `b0ff08fa-643c-5981-89a5-0621fbcb8362` | 274-298 [crates/gcode/src/index_lock.rs:274-298] | Indexed function `wait_blocks_until_same_project_lock_is_released` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:274-298] |
| `different_project_ids_do_not_block_each_other` | function | `fn different_project_ids_do_not_block_each_other() {` | `different_project_ids_do_not_block_each_other [function]` | `c184843a-46aa-5af2-b2fa-69aa47f56f8c` | 306-322 [crates/gcode/src/index_lock.rs:306-322] | Indexed function `different_project_ids_do_not_block_each_other` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:306-322] |
