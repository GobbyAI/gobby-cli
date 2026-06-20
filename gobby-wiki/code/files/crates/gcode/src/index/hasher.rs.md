---
title: crates/gcode/src/index/hasher.rs
type: code_file
provenance:
- file: crates/gcode/src/index/hasher.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/hasher.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

`crates/gcode/src/index/hasher.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gcode/src/index/hasher.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `file_content_hash` | function | Returns the content hash of the file at 'path' by delegating to 'gobby_core::indexing::file_content_hash' and propagating any error as 'anyhow::Result<String>'. [crates/gcode/src/index/hasher.rs:7-9] |
| `content_hash` | function | Computes and returns the content hash of the provided byte slice by delegating to 'gobby_core::indexing::content_hash'. [crates/gcode/src/index/hasher.rs:12-14] |
| `symbol_content_hash` | function | Returns the content hash of the byte slice 'source[start..end]' as a 'String', or an 'anyhow::Error' if the range is out of bounds. [crates/gcode/src/index/hasher.rs:17-27] |

_Verified by 2 in-file unit tests._

