---
title: crates/gwiki/src/research/storage.rs
type: code_file
provenance:
- file: crates/gwiki/src/research/storage.rs
  ranges:
  - 12-59
  - 61-91
  - 93-95
  - 97-135
  - 137-151
  - 153-155
  - 157-159
  - 168-177
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/research/storage.rs

Module: [[code/modules/crates/gwiki/src/research|crates/gwiki/src/research]]

## Purpose

`crates/gwiki/src/research/storage.rs` exposes 8 indexed API symbols.
[crates/gwiki/src/research/storage.rs:12-59]
[crates/gwiki/src/research/storage.rs:61-91]
[crates/gwiki/src/research/storage.rs:93-95]
[crates/gwiki/src/research/storage.rs:97-135]
[crates/gwiki/src/research/storage.rs:137-151]
[crates/gwiki/src/research/storage.rs:153-155]
[crates/gwiki/src/research/storage.rs:157-159]
[crates/gwiki/src/research/storage.rs:168-177]

## API Symbols

- `append_raw_index_locked` (function) component `append_raw_index_locked [function]` (`8350b255-90ba-5990-a64e-0be468f89b09`) lines 12-59 [crates/gwiki/src/research/storage.rs:12-59]
  - Signature: `pub(crate) fn append_raw_index_locked(`
  - Purpose: Appends a markdown link entry to a locked raw index file, using file locking to serialize the read-modify-write sequence and prevent concurrent modification. [crates/gwiki/src/research/storage.rs:12-59]
- `lock_raw_index` (function) component `lock_raw_index [function]` (`f102ddcd-2977-5479-b47b-5ab922ea849b`) lines 61-91 [crates/gwiki/src/research/storage.rs:61-91]
  - Signature: `pub(crate) fn lock_raw_index(lock: &fs::File, lock_path: &Path) -> Result<(), WikiError> {`
  - Purpose: Acquires an exclusive file lock with configurable timeout and polling retry, returning a WikiError if the lock cannot be obtained within the timeout period. [crates/gwiki/src/research/storage.rs:61-91]
- `raw_index_lock_path` (function) component `raw_index_lock_path [function]` (`e4a7d4e9-4b8a-5ac0-bd98-6bb67cad59ee`) lines 93-95 [crates/gwiki/src/research/storage.rs:93-95]
  - Signature: `pub(crate) fn raw_index_lock_path(vault_root: &Path) -> PathBuf {`
  - Purpose: Constructs a PathBuf representing the lock file for the raw index by joining the vault root with the subdirectories `raw/INDEX.md.lock`. [crates/gwiki/src/research/storage.rs:93-95]
- `write_file_atomically` (function) component `write_file_atomically [function]` (`adbe7184-ed5f-5dd8-81b5-c18605d3255e`) lines 97-135 [crates/gwiki/src/research/storage.rs:97-135]
  - Signature: `pub(crate) fn write_file_atomically(`
  - Purpose: Atomically writes byte content to a file using the write-to-temporary-then-rename pattern with fsync durability guarantees and error-induced cleanup. [crates/gwiki/src/research/storage.rs:97-135]
- `temp_sibling_path` (function) component `temp_sibling_path [function]` (`ad72a37c-2940-58a4-a9da-1ab2cc134772`) lines 137-151 [crates/gwiki/src/research/storage.rs:137-151]
  - Signature: `pub(crate) fn temp_sibling_path(path: &Path) -> PathBuf {`
  - Purpose: Generates a uniquely-named temporary file path in the same directory as the input path, using a dot-prefixed filename that incorporates the original filename, process ID, nanosecond timestamp, and an atomically-incremented counter. [crates/gwiki/src/research/storage.rs:137-151]
- `slugify` (function) component `slugify [function]` (`3524a1ec-5f88-5205-8039-b2fb2444c9bb`) lines 153-155 [crates/gwiki/src/research/storage.rs:153-155]
  - Signature: `pub(crate) fn slugify(title: &str) -> String {`
  - Purpose: Converts a title string into a URL-friendly slug with the "research-note" prefix by wrapping `slugify_with_options`. [crates/gwiki/src/research/storage.rs:153-155]
- `unix_timestamp_ms` (function) component `unix_timestamp_ms [function]` (`593726c8-23ee-50b6-8cd1-183cce9ff468`) lines 157-159 [crates/gwiki/src/research/storage.rs:157-159]
  - Signature: `pub(crate) fn unix_timestamp_ms() -> Result<u64, WikiError> {`
  - Purpose: Returns the current Unix timestamp in milliseconds as a `u64`, or a `WikiError` if the operation fails. [crates/gwiki/src/research/storage.rs:157-159]
- `temp_sibling_path_uses_unique_counter_suffix` (function) component `temp_sibling_path_uses_unique_counter_suffix [function]` (`4e521ef2-ee96-56ee-92de-b3af8f2a5ffa`) lines 168-177 [crates/gwiki/src/research/storage.rs:168-177]
  - Signature: `fn temp_sibling_path_uses_unique_counter_suffix() {`
  - Purpose: This test verifies that `temp_sibling_path()` generates unique temporary paths as siblings (same parent directory) of the input path. [crates/gwiki/src/research/storage.rs:168-177]

