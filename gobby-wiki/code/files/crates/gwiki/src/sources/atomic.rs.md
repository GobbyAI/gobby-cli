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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/sources/atomic.rs:7-44](crates/gwiki/src/sources/atomic.rs#L7-L44), [crates/gwiki/src/sources/atomic.rs:46-56](crates/gwiki/src/sources/atomic.rs#L46-L56), [crates/gwiki/src/sources/atomic.rs:58-83](crates/gwiki/src/sources/atomic.rs#L58-L83), [crates/gwiki/src/sources/atomic.rs:85-104](crates/gwiki/src/sources/atomic.rs#L85-L104), [crates/gwiki/src/sources/atomic.rs:111-116](crates/gwiki/src/sources/atomic.rs#L111-L116), [crates/gwiki/src/sources/atomic.rs:120-129](crates/gwiki/src/sources/atomic.rs#L120-L129)

</details>

# crates/gwiki/src/sources/atomic.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Provides atomic file-write helpers for wiki sources. `write_atomic` creates a sibling temp file, writes and `sync_all`s the data, then swaps it into place with `replace_atomic` and finally syncs the parent directory so the update is durable. `temp_sibling_path` builds a unique temp name next to the target and rejects paths without a file name or without a UTF-8 file name, while `replace_atomic` does the platform-specific rename step, removing an existing destination first on Windows.
[crates/gwiki/src/sources/atomic.rs:7-44]
[crates/gwiki/src/sources/atomic.rs:46-56]
[crates/gwiki/src/sources/atomic.rs:58-83]
[crates/gwiki/src/sources/atomic.rs:85-104]
[crates/gwiki/src/sources/atomic.rs:111-116]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `write_atomic` | function | `pub(crate) fn write_atomic(` | `write_atomic [function]` | `d727156b-09a1-574e-ae55-ec7e16497c1f` | 7-44 [crates/gwiki/src/sources/atomic.rs:7-44] | Indexed function `write_atomic` in `crates/gwiki/src/sources/atomic.rs`. [crates/gwiki/src/sources/atomic.rs:7-44] |
| `replace_atomic` | function | `fn replace_atomic(temp_path: &Path, path: &Path) -> std::io::Result<()> {` | `replace_atomic [function]` | `145c1170-f37f-5dce-876e-e31177f6123b` | 46-56 [crates/gwiki/src/sources/atomic.rs:46-56] | Indexed function `replace_atomic` in `crates/gwiki/src/sources/atomic.rs`. [crates/gwiki/src/sources/atomic.rs:46-56] |
| `temp_sibling_path` | function | `fn temp_sibling_path(path: &Path) -> Result<PathBuf, WikiError> {` | `temp_sibling_path [function]` | `3890ab81-748a-5f41-8438-989da59810ce` | 58-83 [crates/gwiki/src/sources/atomic.rs:58-83] | Indexed function `temp_sibling_path` in `crates/gwiki/src/sources/atomic.rs`. [crates/gwiki/src/sources/atomic.rs:58-83] |
| `sync_parent_dir` | function | `pub(crate) fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {` | `sync_parent_dir [function]` | `119d0c70-66bd-5558-bbfb-48af00da6966` | 85-104 [crates/gwiki/src/sources/atomic.rs:85-104] | Indexed function `sync_parent_dir` in `crates/gwiki/src/sources/atomic.rs`. [crates/gwiki/src/sources/atomic.rs:85-104] |
| `temp_sibling_path_rejects_missing_file_name` | function | `fn temp_sibling_path_rejects_missing_file_name() {` | `temp_sibling_path_rejects_missing_file_name [function]` | `76ca60eb-5da6-5d7f-8316-5dd10384941b` | 111-116 [crates/gwiki/src/sources/atomic.rs:111-116] | Indexed function `temp_sibling_path_rejects_missing_file_name` in `crates/gwiki/src/sources/atomic.rs`. [crates/gwiki/src/sources/atomic.rs:111-116] |
| `temp_sibling_path_rejects_non_utf8_file_name` | function | `fn temp_sibling_path_rejects_non_utf8_file_name() {` | `temp_sibling_path_rejects_non_utf8_file_name [function]` | `95ebb71d-e9d2-5fce-9afb-6fe792c0d65f` | 120-129 [crates/gwiki/src/sources/atomic.rs:120-129] | Indexed function `temp_sibling_path_rejects_non_utf8_file_name` in `crates/gwiki/src/sources/atomic.rs`. [crates/gwiki/src/sources/atomic.rs:120-129] |
