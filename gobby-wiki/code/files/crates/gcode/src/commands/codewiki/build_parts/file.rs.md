---
title: crates/gcode/src/commands/codewiki/build_parts/file.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/file.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/file.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/file.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/file.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `FileDocPosition` | class | 'FileDocPosition' is a crate-visible struct that stores a document’s zero-based 'index' and its 'total' count as 'usize' values. [crates/gcode/src/commands/codewiki/build_parts/file.rs:13-16] |
| `build_file_doc` | function | Builds a 'FileDoc' for a source file by optionally reusing a cached page summary, emitting progress, and generating or skipping per-symbol documentation and verification work according to 'ai_depth' and the provided generator/verifier/reuse plans. [crates/gcode/src/commands/codewiki/build_parts/file.rs:19-162] |
| `build_file_body` | function | Build_file_body conditionally generates an aggregate file narrative from either content or symbol evidence, verifies and grounds the generated text against source spans with citations, and falls back to 'structural_file_body' while marking 'degraded' on generation or verification failure. [crates/gcode/src/commands/codewiki/build_parts/file.rs:172-230] |
| `structural_file_body` | function | Builds and returns a string containing two documentation sections, "Overview" from 'structural_file_summary(file, symbols)' and "How it fits" describing the file’s indexed-symbol-based role and linkage to sibling files. [crates/gcode/src/commands/codewiki/build_parts/file.rs:236-252] |
| `file_summary_from_body` | function | Returns the first non-empty, non-heading paragraph from 'body' as a 'String', or falls back to 'structural_file_summary(file, symbols)' if no such block exists. [crates/gcode/src/commands/codewiki/build_parts/file.rs:258-264] |

