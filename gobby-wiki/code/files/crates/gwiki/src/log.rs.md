---
title: crates/gwiki/src/log.rs
type: code_file
provenance:
- file: crates/gwiki/src/log.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/log.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/log.rs` exposes 14 indexed API symbols.

## How it fits

`crates/gwiki/src/log.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `LogEntry` | class | 'LogEntry' is a structured record of an event, containing a timestamp, the associated 'ScopeIdentity', an action identifier, a human-readable summary, and a list of artifact paths ('PathBuf's). [crates/gwiki/src/log.rs:9-15] |
| `LogWriteReport` | class | 'LogWriteReport' is a report struct that records the filesystem path of a scope-specific log file and, optionally, the path of a global log file produced alongside it. [crates/gwiki/src/log.rs:19-22] |
| `append_logs` | function | Appends a 'LogEntry' to 'scope_root/log.md', then conditionally mirrors the same entry to 'global_hub_root/log.md' if provided and distinct, returning a 'LogWriteReport' with the written paths. [crates/gwiki/src/log.rs:25-49] |
| `append_log` | function | Appends a rendered 'LogEntry' to the file at 'path', creating parent directories and the log file if needed, writing a '# Log\n\n' header only when the file is newly empty, and mapping any I/O failure into 'WikiError::Io' with the relevant action and path. [crates/gwiki/src/log.rs:52-90] |
| `render_entry` | function | Formats a 'LogEntry' into a Markdown string containing a '## timestamp - action' heading, 'Scope:' line, summary text, an optional 'Artifacts:' bulleted list of artifact paths when present, and a final trailing newline. [crates/gwiki/src/log.rs:93-108] |
| `same_log_path` | function | Returns 'true' when two paths resolve to the same log location, either by normalized path equality or by matching filesystem identity via 'same_file_identity', so aliasing paths do not produce duplicate log entries. [crates/gwiki/src/log.rs:111-117] |
| `same_file_identity` | function | Returns 'true' only when both paths resolve successfully to filesystem metadata and refer to the same Unix inode on the same device ('dev' and 'ino' match), otherwise 'false'. [crates/gwiki/src/log.rs:121-128] |
| `same_file_identity` | function | Returns 'true' only when both paths resolve to existing Windows files whose '(volume_serial_number, file_index_high, file_index_low)' metadata tuples are present and exactly equal, otherwise 'false'. [crates/gwiki/src/log.rs:131-150] |
| `identity` | function | Returns 'None' if the path’s filesystem metadata lacks a valid file index, otherwise returns 'Some((volume_serial_number, file_index_high, file_index_low))' derived from the file’s metadata. [crates/gwiki/src/log.rs:134-144] |
| `same_file_identity` | function | Returns 'false' unconditionally for any two 'Path' values, so it never reports two paths as the same file identity. [crates/gwiki/src/log.rs:153-155] |
| `resolved_log_path` | function | Returns the canonicalized version of 'path' if 'Path::canonicalize()' succeeds, otherwise falls back to 'resolve_log_path_fallback(path)'. [crates/gwiki/src/log.rs:158-164] |
| `resolve_log_path_fallback` | function | Returns a path whose parent directory is canonicalized when possible by joining the original filename onto the resolved parent, otherwise falls back to cloning the input path unchanged. [crates/gwiki/src/log.rs:167-174] |

_Verified by 2 in-file unit tests._

