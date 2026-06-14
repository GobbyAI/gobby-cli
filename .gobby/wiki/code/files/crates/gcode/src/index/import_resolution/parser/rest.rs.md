---
title: crates/gcode/src/index/import_resolution/parser/rest.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/rest.rs
  ranges:
  - 10-54
  - 56-92
  - 94-121
  - 123-176
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/rest.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution/parser|crates/gcode/src/index/import_resolution/parser]]

## Purpose

`crates/gcode/src/index/import_resolution/parser/rest.rs` implements language-specific import parsing for the import-resolution indexer. It handles Swift, Ruby, Dart, and Elixir import-like statements, extracts the imported module or root binding, records an `ImportRelation`, and registers external dependencies when the target is not a local module or language keyword.
[crates/gcode/src/index/import_resolution/parser/rest.rs:10-54]
[crates/gcode/src/index/import_resolution/parser/rest.rs:56-92]
[crates/gcode/src/index/import_resolution/parser/rest.rs:94-121]
[crates/gcode/src/index/import_resolution/parser/rest.rs:123-176]

## API Symbols

- `parse_swift_import_statement` (function) component `parse_swift_import_statement [function]` (`77ba50c7-a30b-5dd0-8037-7d2f0f2ea69b`) lines 10-54 [crates/gcode/src/index/import_resolution/parser/rest.rs:10-54]
  - Signature: `pub(crate) fn parse_swift_import_statement(`
  - Purpose: Parses Swift import statements to extract the top-level module identifier, records import relations, and registers external module dependencies while excluding local modules and type-declaration keywords. [crates/gcode/src/index/import_resolution/parser/rest.rs:10-54]
- `parse_ruby_import_statement` (function) component `parse_ruby_import_statement [function]` (`9d13c163-29db-520d-899f-f584bb13933a`) lines 56-92 [crates/gcode/src/index/import_resolution/parser/rest.rs:56-92]
  - Signature: `pub(crate) fn parse_ruby_import_statement(`
  - Purpose: Parses a Ruby import statement, extracts the quoted module name, records the import relation, and registers external root bindings for non-local `require` directives while filtering out local constant roots. [crates/gcode/src/index/import_resolution/parser/rest.rs:56-92]
- `parse_dart_import_statement` (function) component `parse_dart_import_statement [function]` (`bf2026d2-540d-5f58-9f42-2702565a0aa5`) lines 94-121 [crates/gcode/src/index/import_resolution/parser/rest.rs:94-121]
  - Signature: `pub(crate) fn parse_dart_import_statement(`
  - Purpose: Parses Dart import statements to extract module URIs and classify external imports as either aliased bindings or bare wildcard modules. [crates/gcode/src/index/import_resolution/parser/rest.rs:94-121]
- `parse_elixir_import_statement` (function) component `parse_elixir_import_statement [function]` (`73cc590f-f921-59aa-b038-486b2307a92c`) lines 123-176 [crates/gcode/src/index/import_resolution/parser/rest.rs:123-176]
  - Signature: `pub(crate) fn parse_elixir_import_statement(`
  - Purpose: Parses Elixir alias/import/require statements and extracts import relations and name bindings (member aliases, wildcard imports, external module roots) for resolving external module dependencies. [crates/gcode/src/index/import_resolution/parser/rest.rs:123-176]

