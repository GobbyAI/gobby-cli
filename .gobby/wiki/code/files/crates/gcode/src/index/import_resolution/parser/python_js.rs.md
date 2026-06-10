---
title: crates/gcode/src/index/import_resolution/parser/python_js.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/python_js.rs
  ranges:
  - 11-98
  - 100-194
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/python_js.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution/parser|crates/gcode/src/index/import_resolution/parser]]

## Purpose

`crates/gcode/src/index/import_resolution/parser/python_js.rs` exposes 2 indexed API symbols.
[crates/gcode/src/index/import_resolution/parser/python_js.rs:11-98]
[crates/gcode/src/index/import_resolution/parser/python_js.rs:100-194]

## API Symbols

- `parse_python_import_statement` (function) component `parse_python_import_statement [function]` (`3ea5626f-08bc-55a2-b9b6-ba688ae21f0a`) lines 11-98 [crates/gcode/src/index/import_resolution/parser/python_js.rs:11-98]
  - Signature: `pub(crate) fn parse_python_import_statement(`
  - Purpose: Parses Python `import` and `from...import` statements to extract module dependencies and register bindings for external Python modules with their aliases. [crates/gcode/src/index/import_resolution/parser/python_js.rs:11-98]
- `parse_js_import_statement` (function) component `parse_js_import_statement [function]` (`6be4b17d-d357-5b96-acbc-fab4a2a49803`) lines 100-194 [crates/gcode/src/index/import_resolution/parser/python_js.rs:100-194]
  - Signature: `pub(crate) fn parse_js_import_statement(`
  - Purpose: Parses a JavaScript import statement to extract the module specifier and categorize imported bindings—namespace imports (`* as`) and named imports with aliases—into member and bare binding collections. [crates/gcode/src/index/import_resolution/parser/python_js.rs:100-194]

