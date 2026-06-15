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

This file defines `FileDocPosition`, a small progress-tracking struct for a file’s place in the current generation run, and `build_file_doc`, which assembles a `FileDoc` for one source file. `build_file_doc` first checks whether the file can be reused from an existing `ReusePlan`, emits status updates, then iterates the file’s symbols to either generate symbol docs or fall back to structural summaries depending on `ai_depth`, using the leading chunk and generation hooks to fill in the final document.
[crates/gcode/src/commands/codewiki/build_parts/file.rs:12-15]
[crates/gcode/src/commands/codewiki/build_parts/file.rs:18-166]

## API Symbols

- `FileDocPosition` (class) component `FileDocPosition [class]` (`8d59ef26-ccef-5cf1-a529-c928e227580c`) lines 12-15 [crates/gcode/src/commands/codewiki/build_parts/file.rs:12-15]
  - Signature: `pub(crate) struct FileDocPosition {`
  - Purpose: 'FileDocPosition' is a crate-visible struct that tracks a document file’s current zero-based 'index' and the 'total' number of positions. [crates/gcode/src/commands/codewiki/build_parts/file.rs:12-15]
- `build_file_doc` (function) component `build_file_doc [function]` (`74c5ab7d-bf59-509b-9f27-335f9307e219`) lines 18-166 [crates/gcode/src/commands/codewiki/build_parts/file.rs:18-166]
  - Signature: `pub(crate) fn build_file_doc(`
  - Purpose: Builds a 'FileDoc' for a file by checking page reuse from a 'ReusePlan', emitting progress, and either generating or skipping per-symbol documentation based on 'ai_depth', with structural fallbacks recorded when generation fails or is disabled. [crates/gcode/src/commands/codewiki/build_parts/file.rs:18-166]

