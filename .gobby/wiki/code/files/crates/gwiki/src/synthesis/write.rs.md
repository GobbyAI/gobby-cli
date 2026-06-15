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

# crates/gwiki/src/synthesis/write.rs

Module: [[code/modules/crates/gwiki/src/synthesis|crates/gwiki/src/synthesis]]

## Purpose

Utilities for safely writing synthesized wiki pages into a vault. It first offers a preflight check that rejects overwriting an existing page when the policy requires merge intent, then the main write path validates the target stays inside the vault, creates parent directories, and either creates a new file or overwrites atomically depending on `WritePolicy`. Supporting helpers perform the actual file write and fsync, clean up on failure, sync the parent directory for durability, and generate a unique sibling temp path for atomic replacement.
[crates/gwiki/src/synthesis/write.rs:15-29]
[crates/gwiki/src/synthesis/write.rs:31-102]
[crates/gwiki/src/synthesis/write.rs:104-128]
[crates/gwiki/src/synthesis/write.rs:130-164]
[crates/gwiki/src/synthesis/write.rs:166-185]

## API Symbols

- `ensure_page_write_allowed` (function) component `ensure_page_write_allowed [function]` (`49c79991-c3fb-5d13-8d39-db9fc2977c16`) lines 15-29 [crates/gwiki/src/synthesis/write.rs:15-29]
  - Signature: `pub fn ensure_page_write_allowed(`
  - Purpose: Returns an error if the target page already exists and the 'WritePolicy' requires merge intent, otherwise अनुमति/permits the write by returning 'Ok(())'. [crates/gwiki/src/synthesis/write.rs:15-29]
- `write_synthesized_page` (function) component `write_synthesized_page [function]` (`f74ce39e-687e-5291-9022-b4138bcf5fc4`) lines 31-102 [crates/gwiki/src/synthesis/write.rs:31-102]
  - Signature: `pub fn write_synthesized_page(`
  - Purpose: Writes a synthesized wiki page to disk within the vault, creating parent directories as needed, enforcing path-safety checks, and using the write policy to either require merge intent for new files or allow overwrite after merge while returning the resulting write outcome. [crates/gwiki/src/synthesis/write.rs:31-102]
- `write_created_synthesized_page` (function) component `write_created_synthesized_page [function]` (`98a4e06d-f486-5146-99a8-b88f5faff8e6`) lines 104-128 [crates/gwiki/src/synthesis/write.rs:104-128]
  - Signature: `fn write_created_synthesized_page(`
  - Purpose: Writes 'contents' to 'file' and fsyncs it, and on either write or sync failure closes the file, deletes 'path', and վերադարձs a 'WikiError::Io' tagged as 'write synthesized wiki page'. [crates/gwiki/src/synthesis/write.rs:104-128]
- `write_synthesized_page_atomically` (function) component `write_synthesized_page_atomically [function]` (`651d7a15-d89f-5623-8a02-980d15d0d494`) lines 130-164 [crates/gwiki/src/synthesis/write.rs:130-164]
  - Signature: `fn write_synthesized_page_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Writes 'contents' to a sibling temporary file, fsyncs it, atomically renames it over 'path', and syncs the parent directory, returning 'WikiError::Io' on any filesystem failure while cleaning up the temp file. [crates/gwiki/src/synthesis/write.rs:130-164]
- `sync_parent_dir` (function) component `sync_parent_dir [function]` (`449d7b64-76a5-597d-92b0-3a571d00417c`) lines 166-185 [crates/gwiki/src/synthesis/write.rs:166-185]
  - Signature: `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: On Unix, it opens 'path''s parent directory and calls 'sync_all()' to flush it to disk, returning 'Ok(())' on non-Unix platforms or when no parent exists, and wrapping any I/O failure in 'WikiError::Io' with action '"sync synthesized page directory"' and the parent path. [crates/gwiki/src/synthesis/write.rs:166-185]
- `temp_sibling_path` (function) component `temp_sibling_path [function]` (`00fc693e-7832-5ed3-a282-75e59b65d790`) lines 187-197 [crates/gwiki/src/synthesis/write.rs:187-197]
  - Signature: `fn temp_sibling_path(path: &Path) -> PathBuf {`
  - Purpose: Builds a temporary sibling path by taking the input path’s filename (or 'page.md' if unavailable), prefixing it with a dot, and appending the current process ID and current UNIX-epoch nanoseconds before a '.tmp' suffix. [crates/gwiki/src/synthesis/write.rs:187-197]

