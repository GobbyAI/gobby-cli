---
title: crates/gcode/src/commands/codewiki/build_parts/file.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/file.rs
  ranges:
  - 10-13
  - 15-115
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/file.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

`crates/gcode/src/commands/codewiki/build_parts/file.rs` exposes 2 indexed API symbols.
[crates/gcode/src/commands/codewiki/build_parts/file.rs:10-13]
[crates/gcode/src/commands/codewiki/build_parts/file.rs:15-115]

## API Symbols

- `FileDocPosition` (class) component `FileDocPosition [class]` (`aaa333ac-1941-55aa-a7e5-8e034478fef3`) lines 10-13 [crates/gcode/src/commands/codewiki/build_parts/file.rs:10-13]
  - Signature: `pub(crate) struct FileDocPosition {`
  - Purpose: `FileDocPosition` is a crate-private struct that tracks a document's position via an index and total count within a file or collection. [crates/gcode/src/commands/codewiki/build_parts/file.rs:10-13]
- `build_file_doc` (function) component `build_file_doc [function]` (`118b1b7a-620e-5083-b760-42e6f9be9815`) lines 15-115 [crates/gcode/src/commands/codewiki/build_parts/file.rs:15-115]
  - Signature: `pub(crate) fn build_file_doc(`
  - Purpose: Constructs a FileDoc by converting input symbols to SymbolDoc entries with optionally AI-generated purposes grounded to source spans and citations, while emitting incremental progress updates. [crates/gcode/src/commands/codewiki/build_parts/file.rs:15-115]

