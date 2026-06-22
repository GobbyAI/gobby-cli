---
title: crates/gcode/src/freshness.rs
type: code_file
provenance:
- file: crates/gcode/src/freshness.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/freshness.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/freshness.rs` exposes 22 indexed API symbols.

## How it fits

`crates/gcode/src/freshness.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `FreshnessScope` | type | Indexed type `FreshnessScope` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:13-16] |
| `FreshnessStatus` | type | Indexed type `FreshnessStatus` in `crates/gcode/src/freshness.rs`. [crates/gcode/src/freshness.rs:19-22] |
| `ensure_fresh` | function | 'ensure_fresh' short-circuits if a freshness pass is already in flight or, for whole-project scope, if the project is already up to date on disk, otherwise it acquires a freshness guard and project lock and reindexes either the entire project or the requested explicit files before returning the resulting 'FreshnessStatus'. [crates/gcode/src/freshness.rs:24-83] |
| `project_needs_refresh` | function | Returns 'true' if the project has never been indexed or if 'api::project_changed_since' reports that files under 'ctx.project_root' have changed since the stored 'last_indexed_at' timestamp for 'ctx.project_id', using the indexed file path list and current 'respect_gitignore' setting. [crates/gcode/src/freshness.rs:93-121] |
| `ensure_symbol_fresh` | function | Returns 'FreshnessStatus::Checked' immediately when the inflight env var is set, the symbol ID is not visible, or the symbol slice is already current; otherwise it calls 'ensure_fresh' for the symbol’s source file path. [crates/gcode/src/freshness.rs:123-144] |
| `symbol_slice_is_current` | function | Returns 'false' if the symbol has no stored content hash or its source file cannot be read, otherwise recomputes the symbol’s content hash from the file bytes at 'byte_start..byte_end' and compares it to 'sym.content_hash' to determine whether the slice is current. [crates/gcode/src/freshness.rs:146-160] |
| `normalize_file_path` | function | Returns a string path for 'path' resolved against 'root', canonicalized and stripped to a relative path under the canonicalized root when possible, otherwise falling back to the original path string. [crates/gcode/src/freshness.rs:162-182] |
| `FreshnessGuard` | class | 'FreshnessGuard' is a forward-declared 'struct' type with no visible members or behavior specified in the provided signature. [crates/gcode/src/freshness.rs:184] |
| `FreshnessGuard::enter` | method | Marks the CLI process as “in-flight” by unsafely setting 'INFLIGHT_ENV' to '"1"' before returning 'Self'. [crates/gcode/src/freshness.rs:187-192] |
| `FreshnessGuard::drop` | method | On drop, it unsafely removes the 'INFLIGHT_ENV' environment variable via 'std::env::remove_var', clearing the in-flight marker. [crates/gcode/src/freshness.rs:196-199] |
| `context_for` | function | Creates a 'Context' configured for a test project by setting a fixed local PostgreSQL URL, using the provided 'root' as 'project_root', assigning default project/indexing settings, disabling external services and daemon access, and marking the context as quiet with a single-project index scope. [crates/gcode/src/freshness.rs:208-222] |
| `symbol_hash` | function | Computes and returns the symbol content hash for the byte slice range '[start, end)' by delegating to 'hasher::symbol_content_hash', panicking with '"symbol hash"' if hashing fails. [crates/gcode/src/freshness.rs:224-226] |
| `postgres_test_context` | function | Constructs and returns a 'Context' for PostgreSQL freshness tests by reading 'GCODE_POSTGRES_TEST_DATABASE_URL', asserting a read-write DB connection, and populating the context with the given 'project_id', a fixed temp project root, quiet mode, default vector/indexing settings, no optional backends, and 'ProjectIndexScope::Single'. [crates/gcode/src/freshness.rs:228-245] |
| `postgres_context_with_root` | function | Creates a 'Context' for a PostgreSQL-backed freshness test by reading 'GCODE_POSTGRES_TEST_DATABASE_URL', verifying a read-write database connection, and populating the context with the given 'project_id' and 'root' plus default or disabled backend/indexing settings. [crates/gcode/src/freshness.rs:247-264] |
| `hold_project_lock` | function | Connects to the project database in read-write mode, acquires a PostgreSQL advisory lock for the project ID with 'pg_advisory_lock', and returns the locked connection. [crates/gcode/src/freshness.rs:266-273] |
| `set_mtime` | function | Opens the file at 'path' with read/write access and updates its modification timestamp to 'time', panicking if either the open or 'set_modified' operation fails. [crates/gcode/src/freshness.rs:275-283] |
| `invalidate_test_project` | function | Connects to the test PostgreSQL database using the context’s 'database_url' and invalidates the index for 'ctx.project_id' via 'crate::index::indexer::invalidate', panicking if either step fails. [crates/gcode/src/freshness.rs:285-290] |
| `full_index` | function | Invokes 'api::index_files' to perform a full index of the project root with no path filter or explicit file list, 'full' enabled, and C++ semantics, projection sync, and related options disabled, then panics if indexing fails. [crates/gcode/src/freshness.rs:292-305] |
| `busy_project_lock_skips_freshness_refresh` | function | Verifies that when a project lock is already held, 'ensure_fresh' for 'FreshnessScope::Project' returns 'FreshnessStatus::SkippedBusy' instead of performing a freshness refresh. [crates/gcode/src/freshness.rs:328-335] |
| `pre_gate_skips_lock_when_unchanged_and_trips_after_a_change` | function | Verifies that 'ensure_fresh' on a project scope bypasses acquiring the advisory lock and returns 'FreshnessStatus::Checked' when the indexed tree is unchanged, but after a tracked file’s mtime is advanced it follows the lock path and returns 'FreshnessStatus::SkippedBusy' while the lock is held. [crates/gcode/src/freshness.rs:343-382] |

_Verified by 2 in-file unit tests._

