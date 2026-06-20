---
title: crates/gcode/src/index/chunker.rs
type: code_file
provenance:
- file: crates/gcode/src/index/chunker.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/chunker.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

`crates/gcode/src/index/chunker.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gcode/src/index/chunker.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `chunk_file_content` | function | Splits UTF-8-lossy file bytes into newline-delimited, overlapping line windows of size 'CHUNK_SIZE', skips blank chunks, and returns a 'Vec<ContentChunk>' populated with per-chunk metadata including stable chunk IDs, line ranges, project/file identifiers, language (defaulting to '"unknown"'), and creation timestamp. [crates/gcode/src/index/chunker.rs:19-62] |
| `epoch_secs_str` | function | Returns the current Unix epoch timestamp in whole seconds as a 'String', using 'SystemTime::now()' and defaulting to '0' if the system clock is earlier than the Unix epoch. [crates/gcode/src/index/chunker.rs:64-72] |

_Verified by 1 in-file unit test._

