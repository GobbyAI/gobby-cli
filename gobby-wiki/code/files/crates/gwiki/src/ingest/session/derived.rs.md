---
title: crates/gwiki/src/ingest/session/derived.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/derived.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/session/derived.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/session/derived.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/session/derived.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `write_session_derived_markdown` | function | The 'write_session_derived_markdown' function resolves the relative path for a derived markdown file based on a 'SourceRecord', ensures its parent directories exist within the specified 'vault_root', atomically writes the markdown content to that path, and returns the relative path on success. [crates/gwiki/src/ingest/session/derived.rs:10-26] |
| `write_session_markdown_atomically` | function | Writes the provided byte contents to a target path atomically by writing and syncing a temporary file, persisting it to the destination path, and synchronizing the parent directory. [crates/gwiki/src/ingest/session/derived.rs:28-52] |
| `create_session_temp_file` | function | The 'create_session_temp_file' function creates and returns a 'NamedTempFile' prefixed with the provided path's file name and suffixed with '.tmp' within the path's parent directory, returning a 'WikiError' if the parent directory is missing or the file creation fails. [crates/gwiki/src/ingest/session/derived.rs:54-81] |
| `sync_parent_dir` | function | On Unix platforms, this function opens and synchronizes the parent directory of the specified path to persist directory entry changes to disk, returning a 'WikiError' on failure, while acting as a no-op on non-Unix platforms. [crates/gwiki/src/ingest/session/derived.rs:83-105] |

