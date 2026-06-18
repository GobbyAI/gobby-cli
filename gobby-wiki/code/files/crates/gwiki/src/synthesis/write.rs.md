---
title: crates/gwiki/src/synthesis/write.rs
type: code_file
provenance:
- file: crates/gwiki/src/synthesis/write.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/synthesis/write.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/synthesis/write.rs` exposes 6 indexed API symbols.

## How it fits

`crates/gwiki/src/synthesis/write.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ensure_page_write_allowed` | function | Returns an error if the target page already exists and the write policy is 'RequireMergeIntent', otherwise it allows the write by returning 'Ok(())'. [crates/gwiki/src/synthesis/write.rs:15-29] |
| `write_synthesized_page` | function | 'write_synthesized_page' normalizes a synthesized page’s Markdown, verifies the target path and parent directory stay within 'vault_root', creates the parent directories, and then writes the file according to 'WritePolicy', returning the resulting 'PageWriteOutcome' or a 'WikiError'. [crates/gwiki/src/synthesis/write.rs:31-103] |
| `write_created_synthesized_page` | function | Writes the provided bytes to a file, forces them to disk with 'sync_all', and on either failure closes the file, deletes the target path, and returns a 'WikiError::Io' annotated as a synthesized wiki page write. [crates/gwiki/src/synthesis/write.rs:105-129] |
| `write_synthesized_page_atomically` | function | Atomically writes 'contents' to 'path' by creating a temporary sibling file, writing and 'sync_all'-flushing it, renaming it over the target, and syncing the parent directory, while mapping any I/O failure to 'WikiError::Io' and cleaning up the temp file on error. [crates/gwiki/src/synthesis/write.rs:131-165] |
| `sync_parent_dir` | function | On Unix, it opens 'path''s parent directory and calls 'sync_all()' to flush directory metadata to disk, returning an 'Io'-wrapped 'WikiError' on failure; on non-Unix platforms or when no parent exists, it returns 'Ok(())'. [crates/gwiki/src/synthesis/write.rs:167-186] |
| `temp_sibling_path` | function | Returns a temporary sibling 'PathBuf' by taking the input path’s filename (defaulting to 'page.md' if missing or non-UTF-8) and replacing it with a hidden '.{name}.{process_id}.{unix_nanos}.tmp' filename to minimize collisions. [crates/gwiki/src/synthesis/write.rs:188-198] |

