---
title: crates/gcode/src/commands/codewiki/build_parts/file.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/file.rs
  ranges:
  - 12-15
  - 18-166
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/file.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

This file orchestrates file-level documentation generation for a code documentation system. FileDocPosition tracks a file's position (index/total) for progress reporting. The build_file_doc function constructs documentation for a single file by: checking if a previously generated file doc can be reused via content hash lookup, emitting progress messages, iterating through symbols to generate or build individual symbol documentation with fallback structural summaries when AI generation is disabled, and handling different AI depth levels to determine which components require generation versus structural construction.
[crates/gcode/src/commands/codewiki/build_parts/file.rs:12-15]
[crates/gcode/src/commands/codewiki/build_parts/file.rs:18-166]

## API Symbols

- `FileDocPosition` (class) component `FileDocPosition [class]` (`8d59ef26-ccef-5cf1-a529-c928e227580c`) lines 12-15 [crates/gcode/src/commands/codewiki/build_parts/file.rs:12-15]
  - Signature: `pub(crate) struct FileDocPosition {`
  - Purpose: Indexed class `FileDocPosition` in `crates/gcode/src/commands/codewiki/build_parts/file.rs`. [crates/gcode/src/commands/codewiki/build_parts/file.rs:12-15]
- `build_file_doc` (function) component `build_file_doc [function]` (`74c5ab7d-bf59-509b-9f27-335f9307e219`) lines 18-166 [crates/gcode/src/commands/codewiki/build_parts/file.rs:18-166]
  - Signature: `pub(crate) fn build_file_doc(`
  - Purpose: Indexed function `build_file_doc` in `crates/gcode/src/commands/codewiki/build_parts/file.rs`. [crates/gcode/src/commands/codewiki/build_parts/file.rs:18-166]

