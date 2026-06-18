---
title: crates/gcode/src/index/import_resolution/parser/python_js.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/python_js.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/python_js.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/parser/python_js.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/parser/python_js.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `parse_python_import_statement` | function | Parses a Python 'import' or 'from ... import ...' statement, records the referenced module in 'extracted.imports', maps external imports to local member bindings when applicable, and otherwise delegates unrecognized statements to 'push_unparsed_import'. [crates/gcode/src/index/import_resolution/parser/python_js.rs:14-123] |
| `python_local_module_lookup` | function | Resolves a Python relative import like '.foo.bar' against a local '.py'/'.pyi' file path by walking up package levels from 'rel_path', appending the import suffix, and returning the resulting dotted module name or 'None' if the resolution escapes the package root. [crates/gcode/src/index/import_resolution/parser/python_js.rs:125-155] |
| `parse_js_import_statement` | function | Normalizes a JS import statement, extracts and records its module specifier as an 'ImportRelation', ignores empty/type-only clauses, delegates local-module clause parsing, and for external modules populates namespace and named import bindings from the top-level import clause. [crates/gcode/src/index/import_resolution/parser/python_js.rs:157-252] |
| `parse_js_local_import_clause` | function | Resolves a JavaScript import clause against candidate files and records local bindings by parsing namespace and named specifiers, skipping type-only entries and clearing conflicting bindings in 'extracted' before inserting the corresponding 'LocalCallBinding's. [crates/gcode/src/index/import_resolution/parser/python_js.rs:254-319] |

