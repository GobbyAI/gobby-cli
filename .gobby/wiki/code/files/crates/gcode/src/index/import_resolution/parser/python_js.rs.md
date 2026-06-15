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

This file contains import-resolution parsers for Python and JavaScript source text. `parse_python_import_statement` recognizes `import` and `from ... import ...` forms, records module dependencies, and registers aliases for external Python modules, while `parse_js_import_statement` extracts a JS module specifier and classifies namespace and named imports into binding maps; both rely on shared helpers, external-module predicates, and fallback handling for imports they cannot fully parse.
[crates/gcode/src/index/import_resolution/parser/python_js.rs:11-98]
[crates/gcode/src/index/import_resolution/parser/python_js.rs:100-194]

## API Symbols

- `parse_python_import_statement` (function) component `parse_python_import_statement [function]` (`3ea5626f-08bc-55a2-b9b6-ba688ae21f0a`) lines 11-98 [crates/gcode/src/index/import_resolution/parser/python_js.rs:11-98]
  - Signature: `pub(crate) fn parse_python_import_statement(`
  - Purpose: Parses Python `import` and `from...import` statements to extract module dependencies and register bindings for external Python modules with their aliases. [crates/gcode/src/index/import_resolution/parser/python_js.rs:11-98]
- `parse_js_import_statement` (function) component `parse_js_import_statement [function]` (`6be4b17d-d357-5b96-acbc-fab4a2a49803`) lines 100-194 [crates/gcode/src/index/import_resolution/parser/python_js.rs:100-194]
  - Signature: `pub(crate) fn parse_js_import_statement(`
  - Purpose: Parses a JavaScript import statement to extract the module specifier and categorize imported bindings—namespace imports (`* as`) and named imports with aliases—into member and bare binding collections. [crates/gcode/src/index/import_resolution/parser/python_js.rs:100-194]

