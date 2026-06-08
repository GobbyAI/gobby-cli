---
title: crates/gcode/src/commands/codewiki/build.rs
type: code_file
source_files:
- file: crates/gcode/src/commands/codewiki/build.rs
  ranges:
  - 3-73
  - 75-164
---

# crates/gcode/src/commands/codewiki/build.rs

Module: [[modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/build.rs` exposes 2 indexed API symbols. [crates/gcode/src/commands/codewiki/build.rs:3-73] [crates/gcode/src/commands/codewiki/build.rs:75-164]

## API Symbols

- `build_file_doc` (function) component `build_file_doc [function]` (`a386d836-407f-501d-8f4c-d57e93e59079`) lines 3-73 [crates/gcode/src/commands/codewiki/build.rs:3-73]
  - Signature: `pub(crate) fn build_file_doc(`
  - Purpose: Constructs a `FileDoc` by generating descriptions for each code symbol (via AI generation or structural fallback) and aggregating the resulting `SymbolDoc` entries with their source spans and component metadata. [crates/gcode/src/commands/codewiki/build.rs:3-73]
- `build_module_docs` (function) component `build_module_docs [function]` (`85beae98-6074-5a5d-b5a6-3d0e5996fd56`) lines 75-164 [crates/gcode/src/commands/codewiki/build.rs:75-164]
  - Signature: `pub(crate) fn build_module_docs(`
  - Purpose: Constructs a hierarchical module documentation structure by aggregating input files and their child modules for each discovered module, processed in reverse-depth order. [crates/gcode/src/commands/codewiki/build.rs:75-164]

