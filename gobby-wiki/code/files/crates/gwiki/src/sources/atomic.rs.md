---
title: crates/gwiki/src/sources/atomic.rs
type: code_file
provenance:
- file: crates/gwiki/src/sources/atomic.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/sources/atomic.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/sources/atomic.rs` exposes 6 indexed API symbols.

## How it fits

`crates/gwiki/src/sources/atomic.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `write_atomic` | function | Writes 'contents' to a temporary sibling file, 'fsync's it, atomically replaces 'path' with that temp file, cleans up the temp file on any failure, and then syncs the parent directory to make the update durable. [crates/gwiki/src/sources/atomic.rs:7-44] |
| `replace_atomic` | function | On Windows, it first deletes any existing file at 'path' (ignoring 'NotFound') and then renames 'temp_path' to 'path', returning the 'std::io::Result' from the rename operation. [crates/gwiki/src/sources/atomic.rs:46-56] |
| `temp_sibling_path` | function | Returns a temporary sibling 'PathBuf' for atomic writes by validating that 'path' has a UTF-8 filename, then constructing a hidden '.name.pid.nanos.uuid.tmp' filename in the same directory. [crates/gwiki/src/sources/atomic.rs:58-83] |
| `sync_parent_dir` | function | On Unix, opens 'path'’s parent directory and calls 'sync_all()' to flush it to stable storage, mapping any I/O error into 'WikiError::Io' with the parent path and action label, while on non-Unix platforms or for paths without a parent it returns 'Ok(())'. [crates/gwiki/src/sources/atomic.rs:85-104] |
| `temp_sibling_path_rejects_missing_file_name` | function | Asserts that 'temp_sibling_path(Path::new("/"))' fails with 'WikiError::Config' when the input path has no file name. [crates/gwiki/src/sources/atomic.rs:111-116] |
| `temp_sibling_path_rejects_non_utf8_file_name` | function | Verifies that 'temp_sibling_path' returns a 'WikiError::Config' error when given a 'PathBuf' whose filename contains invalid UTF-8 bytes. [crates/gwiki/src/sources/atomic.rs:120-129] |

