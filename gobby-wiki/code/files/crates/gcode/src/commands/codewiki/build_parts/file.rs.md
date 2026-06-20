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
| `build_file_body` | function | The 'build_file_body' function constructs a file's narrative documentation by conditionally generating and verifying text via an AI model based on symbol summaries, source excerpts, and relationship facts, falling back to a structured representation of the file's symbols if AI generation is skipped or fails. [crates/gcode/src/commands/codewiki/build_parts/file.rs:202-261] |
| `structural_file_body` | function | The 'structural_file_body' function constructs and returns a string containing "Overview" and "How it fits" documentation sections for a specified file based on its path and a slice of its indexed symbols. [crates/gcode/src/commands/codewiki/build_parts/file.rs:267-283] |
| `file_summary_from_body` | function | This function returns the first trimmed, non-empty paragraph block from the body text that does not start with a '#' character, falling back to a structural file summary generated from the file path and symbol documentation if no such block is found. [crates/gcode/src/commands/codewiki/build_parts/file.rs:289-295] |

