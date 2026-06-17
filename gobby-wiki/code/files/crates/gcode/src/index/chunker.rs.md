---
title: crates/gcode/src/index/chunker.rs
type: code_file
provenance:
- file: crates/gcode/src/index/chunker.rs
  ranges:
  - 19-62
  - 64-72
  - 77-90
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/chunker.rs:19-62](crates/gcode/src/index/chunker.rs#L19-L62), [crates/gcode/src/index/chunker.rs:64-72](crates/gcode/src/index/chunker.rs#L64-L72), [crates/gcode/src/index/chunker.rs:77-90](crates/gcode/src/index/chunker.rs#L77-L90)

</details>

# crates/gcode/src/index/chunker.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

This file implements gcode’s line-based content chunking for FTS indexing: `chunk_file_content` converts file bytes into overlapping 100-line `ContentChunk` records, assigning IDs and metadata such as project, path, language, line range, and a creation timestamp. `epoch_secs_str` provides that timestamp as a Unix-seconds string without adding a chrono dependency, and `chunker_stays_gcode_owned_with_documented_narrowing` documents that this chunking logic remains in gcode because it projects domain-specific indexing state rather than generic byte-range chunking.
[crates/gcode/src/index/chunker.rs:19-62]
[crates/gcode/src/index/chunker.rs:64-72]
[crates/gcode/src/index/chunker.rs:77-90]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `chunk_file_content` | function | `pub fn chunk_file_content(` | `chunk_file_content [function]` | `d21e3ef6-4770-50f4-9d52-d1ba8459f999` | 19-62 [crates/gcode/src/index/chunker.rs:19-62] | Indexed function `chunk_file_content` in `crates/gcode/src/index/chunker.rs`. [crates/gcode/src/index/chunker.rs:19-62] |
| `epoch_secs_str` | function | `fn epoch_secs_str() -> String {` | `epoch_secs_str [function]` | `2398bbf7-1243-50b1-aa90-4b17e9cba4bc` | 64-72 [crates/gcode/src/index/chunker.rs:64-72] | Indexed function `epoch_secs_str` in `crates/gcode/src/index/chunker.rs`. [crates/gcode/src/index/chunker.rs:64-72] |
| `chunker_stays_gcode_owned_with_documented_narrowing` | function | `fn chunker_stays_gcode_owned_with_documented_narrowing() {` | `chunker_stays_gcode_owned_with_documented_narrowing [function]` | `ae1546cd-8c8e-5a2f-906b-8d4c24c77584` | 77-90 [crates/gcode/src/index/chunker.rs:77-90] | Indexed function `chunker_stays_gcode_owned_with_documented_narrowing` in `crates/gcode/src/index/chunker.rs`. [crates/gcode/src/index/chunker.rs:77-90] |
