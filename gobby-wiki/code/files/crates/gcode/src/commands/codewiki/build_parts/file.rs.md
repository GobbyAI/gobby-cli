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

`crates/gcode/src/commands/codewiki/build_parts/file.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `FileDocPosition` | class | The 'FileDocPosition' struct is a crate-private representation of a document's position within a multi-document file, storing its sequence index and the total count of documents. [crates/gcode/src/commands/codewiki/build_parts/file.rs:14-17] |
| `build_file_doc` | function | The 'build_file_doc' function constructs a 'FileDoc' for a specified file, leveraging a reuse plan based on file and neighbor hashes to return cached documentation or compiling it from provided symbols, relationships, deprecations, and test indexes. [crates/gcode/src/commands/codewiki/build_parts/file.rs:20-192] |
| `build_file_body` | function | # Summary 'build_file_body' generates file-level documentation through conditional AI-based generation with optional verification, falling back to structural generation on failure or when AI processing is disabled. [crates/gcode/src/commands/codewiki/build_parts/file.rs:202-261] |
| `structural_file_body` | function | Constructs a documentation string containing an overview section derived from the file's indexed symbols and a contextual section describing the file's structural relationships within its module. [crates/gcode/src/commands/codewiki/build_parts/file.rs:267-283] |
| `file_summary_from_body` | function | Extracts the first non-empty, non-heading paragraph from the body text by splitting on double newlines, falling back to generating a structural file summary if no suitable paragraph exists. [crates/gcode/src/commands/codewiki/build_parts/file.rs:289-295] |

