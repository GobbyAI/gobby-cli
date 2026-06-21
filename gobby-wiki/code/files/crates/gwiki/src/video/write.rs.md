---
title: crates/gwiki/src/video/write.rs
type: code_file
provenance:
- file: crates/gwiki/src/video/write.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/video/write.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/video/write.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gwiki/src/video/write.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `write_video_markdown_atomic` | function | Atomically writes a byte slice to a file using a temporary sibling file and atomic rename operation, with implicit existing-file replacement and parent directory synchronization. [crates/gwiki/src/video/write.rs:9-65] |
| `temp_sibling_path` | function | Generates a PathBuf for a temporary hidden sibling file by formatting the filename as '.{original_filename}.{pid}.{nanoseconds_since_epoch}.tmp'. [crates/gwiki/src/video/write.rs:67-77] |
| `sync_parent_dir` | function | Flushes the parent directory to disk on Unix systems using 'sync_all()' to ensure metadata durability; no-op on non-Unix platforms, returning 'WikiError::Io' on I/O failure. [crates/gwiki/src/video/write.rs:79-98] |

