---
title: crates/gwiki/src/synthesis/write.rs
type: code_file
provenance:
- file: crates/gwiki/src/synthesis/write.rs
  ranges:
  - 15-29
  - 31-102
  - 104-128
  - 130-164
  - 166-185
  - 187-197
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/synthesis/write.rs:15-29](crates/gwiki/src/synthesis/write.rs#L15-L29), [crates/gwiki/src/synthesis/write.rs:31-102](crates/gwiki/src/synthesis/write.rs#L31-L102), [crates/gwiki/src/synthesis/write.rs:104-128](crates/gwiki/src/synthesis/write.rs#L104-L128), [crates/gwiki/src/synthesis/write.rs:130-164](crates/gwiki/src/synthesis/write.rs#L130-L164), [crates/gwiki/src/synthesis/write.rs:166-185](crates/gwiki/src/synthesis/write.rs#L166-L185), [crates/gwiki/src/synthesis/write.rs:187-197](crates/gwiki/src/synthesis/write.rs#L187-L197)

</details>

# crates/gwiki/src/synthesis/write.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file handles safe writing of synthesized wiki pages into the vault. `ensure_page_write_allowed` is an advisory check that rejects overwriting an existing page when `WritePolicy::RequireMergeIntent` is in effect, while `write_synthesized_page` performs the real guarded write by validating the target path is inside the vault, creating parent directories, and then choosing between create-new and overwrite-after-merge behavior. The lower-level helpers support that flow: `write_created_synthesized_page` writes and fsyncs a newly created file with cleanup on failure, `write_synthesized_page_atomically` writes to a temporary sibling and atomically renames it into place, `sync_parent_dir` flushes the parent directory on Unix, and `temp_sibling_path` builds the temporary filename used for atomic replacement.
[crates/gwiki/src/synthesis/write.rs:15-29]
[crates/gwiki/src/synthesis/write.rs:31-102]
[crates/gwiki/src/synthesis/write.rs:104-128]
[crates/gwiki/src/synthesis/write.rs:130-164]
[crates/gwiki/src/synthesis/write.rs:166-185]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ensure_page_write_allowed` | function | `pub fn ensure_page_write_allowed(` | `ensure_page_write_allowed [function]` | `49c79991-c3fb-5d13-8d39-db9fc2977c16` | 15-29 [crates/gwiki/src/synthesis/write.rs:15-29] | Returns an error if the target page already exists and the write policy is 'RequireMergeIntent', otherwise it allows the write by returning 'Ok(())'. [crates/gwiki/src/synthesis/write.rs:15-29] |
| `write_synthesized_page` | function | `pub fn write_synthesized_page(` | `write_synthesized_page [function]` | `f74ce39e-687e-5291-9022-b4138bcf5fc4` | 31-102 [crates/gwiki/src/synthesis/write.rs:31-102] | Writes a synthesized wiki page into a vault-safe path, creating parent directories as needed and enforcing 'WritePolicy' by either requiring a new file or allowing an overwrite path after merge handling, while returning the resulting 'PageWriteOutcome' or a 'WikiError'. [crates/gwiki/src/synthesis/write.rs:31-102] |
| `write_created_synthesized_page` | function | `fn write_created_synthesized_page(` | `write_created_synthesized_page [function]` | `98a4e06d-f486-5146-99a8-b88f5faff8e6` | 104-128 [crates/gwiki/src/synthesis/write.rs:104-128] | Writes the given bytes to a file and fsyncs it, and on either write or sync failure closes the file, deletes the target path, and returns a 'WikiError::Io' annotated with the page path and failed action. [crates/gwiki/src/synthesis/write.rs:104-128] |
| `write_synthesized_page_atomically` | function | `fn write_synthesized_page_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {` | `write_synthesized_page_atomically [function]` | `651d7a15-d89f-5623-8a02-980d15d0d494` | 130-164 [crates/gwiki/src/synthesis/write.rs:130-164] | Creates a temporary sibling file, writes and fsyncs 'contents' to it, atomically renames it over 'path', syncs the parent directory, and cleans up the temp file on any I/O failure. [crates/gwiki/src/synthesis/write.rs:130-164] |
| `sync_parent_dir` | function | `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {` | `sync_parent_dir [function]` | `449d7b64-76a5-597d-92b0-3a571d00417c` | 166-185 [crates/gwiki/src/synthesis/write.rs:166-185] | On Unix, it opens 'path''s parent directory and calls 'sync_all()' to flush it to disk, mapping any I/O error into 'WikiError::Io' with action '"sync synthesized page directory"' and the parent path; on non-Unix platforms it returns 'Ok(())' without doing anything. [crates/gwiki/src/synthesis/write.rs:166-185] |
| `temp_sibling_path` | function | `fn temp_sibling_path(path: &Path) -> PathBuf {` | `temp_sibling_path [function]` | `00fc693e-7832-5ed3-a282-75e59b65d790` | 187-197 [crates/gwiki/src/synthesis/write.rs:187-197] | Constructs a sibling temporary file path by taking the input path’s file name as UTF-8 (defaulting to 'page.md'), then replacing it with a hidden name of the form '.{file_name}.{process_id}.{unix_nanos}.tmp' using the current process ID and current UNIX timestamp in nanoseconds. [crates/gwiki/src/synthesis/write.rs:187-197] |
