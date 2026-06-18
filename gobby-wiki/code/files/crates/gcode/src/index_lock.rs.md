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

`crates/gcode/src/index_lock.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `IndexLockPolicy` | type | Indexed type `IndexLockPolicy` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:15-21] |
| `IndexLockPolicy::brief_freshness_try` | method | Indexed method `IndexLockPolicy::brief_freshness_try` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:24-29] |
| `IndexLockResult` | type | Indexed type `IndexLockResult` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:33-36] |
| `with_project_lock` | function | Indexed function `with_project_lock` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:38-47] |
| `ProjectIndexLockAttempt` | type | Indexed type `ProjectIndexLockAttempt` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:49-52] |
| `acquire_project_lock` | function | Indexed function `acquire_project_lock` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:54-92] |
| `try_advisory_lock_until` | function | Indexed function `try_advisory_lock_until` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:94-125] |
| `try_advisory_lock` | function | Indexed function `try_advisory_lock` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:127-132] |
| `project_lock_key` | function | Indexed function `project_lock_key` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:134-146] |
| `advisory_lock_delay_warning` | function | Indexed function `advisory_lock_delay_warning` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:148-154] |
| `ProjectIndexLock` | class | Indexed class `ProjectIndexLock` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:156-160] |
| `ProjectIndexLock::drop` | method | Indexed method `ProjectIndexLock::drop` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:163-190] |
| `context_for` | function | Indexed function `context_for` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:200-214] |
| `connect_postgres_test_db` | function | Indexed function `connect_postgres_test_db` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:216-221] |
| `hold_project_lock` | function | Indexed function `hold_project_lock` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:223-229] |
| `project_lock_key_matches_fixture` | function | Indexed function `project_lock_key_matches_fixture` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:232-234] |
| `project_lock_key_is_project_scoped` | function | Indexed function `project_lock_key_is_project_scoped` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:237-239] |
| `brief_try_returns_busy_while_same_project_lock_is_held` | function | Indexed function `brief_try_returns_busy_while_same_project_lock_is_held` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:250-266] |
| `wait_blocks_until_same_project_lock_is_released` | function | Indexed function `wait_blocks_until_same_project_lock_is_released` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:274-298] |
| `different_project_ids_do_not_block_each_other` | function | Indexed function `different_project_ids_do_not_block_each_other` in `crates/gcode/src/index_lock.rs`. [crates/gcode/src/index_lock.rs:306-322] |

