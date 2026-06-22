---
title: crates/gcode/src/index_lock.rs
type: code_file
provenance:
- file: crates/gcode/src/index_lock.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index_lock.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/index_lock.rs` exposes 20 indexed API symbols.

## How it fits

`crates/gcode/src/index_lock.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `IndexLockPolicy` | type | Indexed type `IndexLockPolicy` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:15-21] |
| `IndexLockPolicy::brief_freshness_try` | method | Constructs and returns a 'Self::BriefTry' configuration with 'total_wait' set to 150 milliseconds and 'poll' set to 25 milliseconds. [crates/gcode/src/index_lock.rs:24-29] |
| `IndexLockResult` | type | Indexed type `IndexLockResult` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:33-36] |
| `with_project_lock` | function | Attempts to acquire the project index lock using the given context and policy, then either runs the closure and wraps its result in 'IndexLockResult::Acquired' or returns 'IndexLockResult::Busy' if the lock is unavailable. [crates/gcode/src/index_lock.rs:38-47] |
| `ProjectIndexLockAttempt` | type | Indexed type `ProjectIndexLockAttempt` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:49-52] |
| `acquire_project_lock` | function | Attempts to acquire a PostgreSQL advisory lock for the current project using either blocking wait or bounded polling, emits a warning if acquisition is slow, and returns either an acquired 'ProjectIndexLock' holding the DB connection or 'ProjectIndexLockAttempt::Busy'. [crates/gcode/src/index_lock.rs:54-92] |
| `try_advisory_lock_until` | function | Repeatedly attempts to acquire a PostgreSQL advisory lock for 'key' on 'conn' until 'total_wait' elapses, using a bounded polling/sleep interval between retries, and returns 'Ok(true)' on success or 'Ok(false)' on timeout. [crates/gcode/src/index_lock.rs:94-125] |
| `try_advisory_lock` | function | Attempts to acquire a PostgreSQL advisory lock for the given 'i64' key via 'pg_try_advisory_lock', returning 'Ok(true)' if obtained, 'Ok(false)' if not, or an error if the query or result extraction fails. [crates/gcode/src/index_lock.rs:127-132] |
| `project_lock_key` | function | Computes a deterministic 64-bit PostgreSQL advisory lock key by hashing 'b"gcode:index:"' plus the 'project_id' with SHA-256 and interpreting the first 8 digest bytes as a big-endian 'i64'. [crates/gcode/src/index_lock.rs:134-146] |
| `advisory_lock_delay_warning` | function | Returns the advisory-lock delay warning threshold as a 'Duration', using the 'ADVISORY_LOCK_DELAY_WARNING_MS_ENV' environment variable if it exists and parses as 'u64', otherwise falling back to 'DEFAULT_ADVISORY_LOCK_DELAY_WARNING_MS' milliseconds. [crates/gcode/src/index_lock.rs:148-154] |
| `ProjectIndexLock` | class | 'ProjectIndexLock' is a struct that encapsulates a 'Client' connection, an 'i64' lock key, and a 'bool' flag controlling quiet behavior for managing a project index lock. [crates/gcode/src/index_lock.rs:156-160] |
| `ProjectIndexLock::drop` | method | Releases the advisory lock identified by 'self.key' via 'SELECT pg_advisory_unlock($1)', and logs or optionally prints warnings if the unlock fails, returns 'false', or the result cannot be decoded. [crates/gcode/src/index_lock.rs:163-190] |
| `context_for` | function | Constructs and returns a 'Context' for a single-project index test setup by populating the supplied database URL and project ID, hardcoding the project root to '/tmp/gcode-index-lock-test', enabling quiet mode, leaving external service URLs and clients unset, and using default code-vector and indexing settings. [crates/gcode/src/index_lock.rs:200-214] |
| `connect_postgres_test_db` | function | Reads 'GCODE_POSTGRES_TEST_DATABASE_URL' from the environment, verifies a read-write PostgreSQL connection can be established via 'db::connect_readwrite', and returns the database URL string. [crates/gcode/src/index_lock.rs:216-221] |
| `hold_project_lock` | function | Opens a read-write PostgreSQL connection, computes the project’s advisory-lock key from 'project_id', acquires 'pg_advisory_lock' on that key to block concurrent holders, and returns the locked 'Client'. [crates/gcode/src/index_lock.rs:223-229] |
| `brief_try_returns_busy_while_same_project_lock_is_held` | function | Verifies that 'with_project_lock' using 'IndexLockPolicy::BriefTry' returns 'IndexLockResult::Busy' without invoking the closure when the same project lock is already held. [crates/gcode/src/index_lock.rs:250-266] |
| `wait_blocks_until_same_project_lock_is_released` | function | Verifies that 'with_project_lock' using 'IndexLockPolicy::Wait' blocks while another thread holds the same project lock, then succeeds and returns 'IndexLockResult::Acquired(())' after the lock is released. [crates/gcode/src/index_lock.rs:274-298] |
| `different_project_ids_do_not_block_each_other` | function | Verifies that a held index lock for one project ID does not prevent 'with_project_lock' from acquiring and executing successfully for a different project ID, returning 'IndexLockResult::Acquired(7)'. [crates/gcode/src/index_lock.rs:306-322] |

_Verified by 2 in-file unit tests._

