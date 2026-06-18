---
title: crates/gcode/src/index/import_resolution/parser/objc.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/objc.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/objc.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/parser/objc.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/parser/objc.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `parse_objc_import_statement` | function | Parses an Objective-C '#import'/'#include' statement, records the import relation, and for non-system imports resolves candidate files to populate 'ExtractedImports' bindings for referenced functions and types with deduplicated candidate-file lists. [crates/gcode/src/index/import_resolution/parser/objc.rs:8-69] |
| `resolve_objc_local_callee` | function | Returns a 'LocalCallBinding' for an Objective-C bare call name when that name is not already defined in 'symbols' and there is at least one unique imported Objective-C file, otherwise returns 'None'. [crates/gcode/src/index/import_resolution/parser/objc.rs:71-85] |
| `objc_import_path` | function | Parses an Objective-C import specifier by returning a quoted path as '(path, false)' or a trimmed non-empty angle-bracket path as '(path, true)', and 'None' if neither form is present. [crates/gcode/src/index/import_resolution/parser/objc.rs:87-95] |

