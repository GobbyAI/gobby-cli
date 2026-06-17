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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/build_parts/file.rs:12-15](crates/gcode/src/commands/codewiki/build_parts/file.rs#L12-L15), [crates/gcode/src/commands/codewiki/build_parts/file.rs:18-166](crates/gcode/src/commands/codewiki/build_parts/file.rs#L18-L166)

</details>

# crates/gcode/src/commands/codewiki/build_parts/file.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

Defines the file-doc generation step for codewiki output. `FileDocPosition` carries the 1-based file index and total for progress messages, while `build_file_doc` orchestrates building a `FileDoc` from a file path, module name, symbols, and optional leading chunk by deciding whether to reuse an existing page or generate new text based on the reuse plan and AI depth. It then emits progress, builds per-symbol docs with generation or structural fallbacks, and assembles the file-level summary and provenance into the final document.
[crates/gcode/src/commands/codewiki/build_parts/file.rs:12-15]
[crates/gcode/src/commands/codewiki/build_parts/file.rs:18-166]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `FileDocPosition` | class | `pub(crate) struct FileDocPosition {` | `FileDocPosition [class]` | `8d59ef26-ccef-5cf1-a529-c928e227580c` | 12-15 [crates/gcode/src/commands/codewiki/build_parts/file.rs:12-15] | Indexed class `FileDocPosition` in `crates/gcode/src/commands/codewiki/build_parts/file.rs`. [crates/gcode/src/commands/codewiki/build_parts/file.rs:12-15] |
| `build_file_doc` | function | `pub(crate) fn build_file_doc(` | `build_file_doc [function]` | `74c5ab7d-bf59-509b-9f27-335f9307e219` | 18-166 [crates/gcode/src/commands/codewiki/build_parts/file.rs:18-166] | Indexed function `build_file_doc` in `crates/gcode/src/commands/codewiki/build_parts/file.rs`. [crates/gcode/src/commands/codewiki/build_parts/file.rs:18-166] |
