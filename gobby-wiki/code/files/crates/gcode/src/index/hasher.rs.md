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

`crates/gcode/src/index/hasher.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `file_content_hash` | function | Returns the content hash of the file at 'path' by delegating to 'gobby_core::indexing::file_content_hash' and propagating any error as 'anyhow::Result<String>'. [crates/gcode/src/index/hasher.rs:7-9] |
| `content_hash` | function | Computes and returns the content hash of the provided byte slice by delegating to 'gobby_core::indexing::content_hash'. [crates/gcode/src/index/hasher.rs:12-14] |
| `symbol_content_hash` | function | Returns the content hash of the byte slice 'source[start..end]' as a 'String', or an 'anyhow::Error' if the range is out of bounds. [crates/gcode/src/index/hasher.rs:17-27] |
| `file_content_hash_delegates_to_gobby_core` | function | Verifies that the local 'file_content_hash' wrapper returns the same digest as 'gobby_core::indexing::file_content_hash' for a temp file and that the wrapper source delegates to the core implementation without reimplementing hashing locally. [crates/gcode/src/index/hasher.rs:35-49] |
| `content_hash_delegates_to_gobby_core` | function | Verifies that 'content_hash(source)' returns the same value as 'gobby_core::indexing::content_hash(source)' for a fixed byte slice, confirming delegation to 'gobby_core'. [crates/gcode/src/index/hasher.rs:52-59] |

