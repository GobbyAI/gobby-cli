---
title: crates/gcode/src/index/import_resolution/parser/rest.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/rest.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/rest.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/parser/rest.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/parser/rest.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `parse_swift_import_statement` | function | Parses a trimmed Swift 'import' statement, records the import relation for the current file, and, when the leading module name is non-empty, non-keyword, and not a known local module, registers it as an external root binding in 'ExtractedImports'. [crates/gcode/src/index/import_resolution/parser/rest.rs:10-54] |
| `parse_ruby_import_statement` | function | Parses a Ruby import-like statement, records an 'ImportRelation' for the trimmed source text, and when the statement is a 'require' with a resolvable non-local root, registers that root as an external binding in 'extracted.bindings.external_roots'. [crates/gcode/src/index/import_resolution/parser/rest.rs:56-92] |
| `parse_dart_import_statement` | function | Parses a Dart 'import' declaration, records the imported URI as an 'ImportRelation', and classifies it into external alias/bare bindings or resolved local-import file bindings based on whether the URI is external and whether the import uses an 'as' prefix. [crates/gcode/src/index/import_resolution/parser/rest.rs:94-152] |
| `parse_elixir_import_statement` | function | Parses an Elixir 'alias'/'import'/'require' statement, records the resolved import relation for the current file, and, when the target refers to a locally defined module root, binds aliases or imports to the corresponding local module files in 'ExtractedImports'. [crates/gcode/src/index/import_resolution/parser/rest.rs:154-233] |

