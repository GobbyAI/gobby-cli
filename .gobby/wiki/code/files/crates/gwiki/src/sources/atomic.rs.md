---
title: crates/gwiki/src/sources/atomic.rs
type: code_file
provenance:
- file: crates/gwiki/src/sources/atomic.rs
  ranges:
  - 7-44
  - 46-56
  - 58-83
  - 85-104
  - 111-116
  - 120-129
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/sources/atomic.rs

Module: [[code/modules/crates/gwiki/src/sources|crates/gwiki/src/sources]]

## Purpose

`crates/gwiki/src/sources/atomic.rs` exposes 6 indexed API symbols.
[crates/gwiki/src/sources/atomic.rs:7-44]
[crates/gwiki/src/sources/atomic.rs:46-56]
[crates/gwiki/src/sources/atomic.rs:58-83]
[crates/gwiki/src/sources/atomic.rs:85-104]
[crates/gwiki/src/sources/atomic.rs:111-116]

## API Symbols

- `write_atomic` (function) component `write_atomic [function]` (`d727156b-09a1-574e-ae55-ec7e16497c1f`) lines 7-44 [crates/gwiki/src/sources/atomic.rs:7-44]
  - Signature: `pub(crate) fn write_atomic(`
  - Purpose: Atomically writes byte contents to a file by writing to a temporary sibling, syncing to disk, then atomically replacing the target path and syncing the parent directory. [crates/gwiki/src/sources/atomic.rs:7-44]
- `replace_atomic` (function) component `replace_atomic [function]` (`145c1170-f37f-5dce-876e-e31177f6123b`) lines 46-56 [crates/gwiki/src/sources/atomic.rs:46-56]
  - Signature: `fn replace_atomic(temp_path: &Path, path: &Path) -> std::io::Result<()> {`
  - Purpose: Atomically replaces a file by removing the destination on Windows (if it exists) and renaming a temporary file to the target path. [crates/gwiki/src/sources/atomic.rs:46-56]
- `temp_sibling_path` (function) component `temp_sibling_path [function]` (`3890ab81-748a-5f41-8438-989da59810ce`) lines 58-83 [crates/gwiki/src/sources/atomic.rs:58-83]
  - Signature: `fn temp_sibling_path(path: &Path) -> Result<PathBuf, WikiError> {`
  - Purpose: Generates a uniquely-named temporary sibling file path for atomic writes by appending the process ID, a UUID, and nanosecond-precision timestamp to the original filename, with validation that the path contains a valid UTF-8 file name. [crates/gwiki/src/sources/atomic.rs:58-83]
- `sync_parent_dir` (function) component `sync_parent_dir [function]` (`119d0c70-66bd-5558-bbfb-48af00da6966`) lines 85-104 [crates/gwiki/src/sources/atomic.rs:85-104]
  - Signature: `pub(crate) fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: On Unix systems, this function fsync's the parent directory to ensure durability of atomic file operations; on non-Unix platforms, it's a no-op. [crates/gwiki/src/sources/atomic.rs:85-104]
- `temp_sibling_path_rejects_missing_file_name` (function) component `temp_sibling_path_rejects_missing_file_name [function]` (`76ca60eb-5da6-5d7f-8316-5dd10384941b`) lines 111-116 [crates/gwiki/src/sources/atomic.rs:111-116]
  - Signature: `fn temp_sibling_path_rejects_missing_file_name() {`
  - Purpose: Tests that `temp_sibling_path()` rejects paths without a file name component by returning a `WikiError::Config` error. [crates/gwiki/src/sources/atomic.rs:111-116]
- `temp_sibling_path_rejects_non_utf8_file_name` (function) component `temp_sibling_path_rejects_non_utf8_file_name [function]` (`95ebb71d-e9d2-5fce-9afb-6fe792c0d65f`) lines 120-129 [crates/gwiki/src/sources/atomic.rs:120-129]
  - Signature: `fn temp_sibling_path_rejects_non_utf8_file_name() {`
  - Purpose: Unit test asserting that `temp_sibling_path()` returns a `WikiError::Config` error when passed a PathBuf containing invalid UTF-8 bytes. [crates/gwiki/src/sources/atomic.rs:120-129]

