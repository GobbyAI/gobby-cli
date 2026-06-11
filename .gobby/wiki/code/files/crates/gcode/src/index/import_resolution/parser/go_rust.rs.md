---
title: crates/gcode/src/index/import_resolution/parser/go_rust.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/go_rust.rs
  ranges:
  - 12-40
  - 42-77
  - 79-106
  - 108-136
  - 138-188
  - 195-206
  - 209-219
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/go_rust.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution/parser|crates/gcode/src/index/import_resolution/parser]]

## Purpose

`crates/gcode/src/index/import_resolution/parser/go_rust.rs` exposes 7 indexed API symbols.
[crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40]
[crates/gcode/src/index/import_resolution/parser/go_rust.rs:42-77]
[crates/gcode/src/index/import_resolution/parser/go_rust.rs:79-106]
[crates/gcode/src/index/import_resolution/parser/go_rust.rs:108-136]
[crates/gcode/src/index/import_resolution/parser/go_rust.rs:138-188]

## API Symbols

- `parse_go_import_statement` (function) component `parse_go_import_statement [function]` (`09b2efc9-1277-55d5-bcd5-177f6318698b`) lines 12-40 [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40]
  - Signature: `pub(crate) fn parse_go_import_statement(`
  - Purpose: Parses and validates a Go import statement in single or parenthesized block form, delegating individual import specification extraction to a helper function. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40]
- `parse_go_import_spec` (function) component `parse_go_import_spec [function]` (`4f70d13c-23e0-5f16-a6c6-69ce69537432`) lines 42-77 [crates/gcode/src/index/import_resolution/parser/go_rust.rs:42-77]
  - Signature: `fn parse_go_import_spec(`
  - Purpose: Extracts the module name from a Go import specification, tracks the file-to-module import relation, and registers the alias binding for external dependencies. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:42-77]
- `parse_rust_import_statement` (function) component `parse_rust_import_statement [function]` (`ead7eba1-e088-5d34-ba91-e3ccc61cd99f`) lines 79-106 [crates/gcode/src/index/import_resolution/parser/go_rust.rs:79-106]
  - Signature: `pub(crate) fn parse_rust_import_statement(`
  - Purpose: Parses a Rust `use` import statement and registers the extracted module path or import group with an import resolution context via specialized handlers, deferring unexpanded glob imports. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:79-106]
- `register_rust_group_imports` (function) component `register_rust_group_imports [function]` (`82851c31-bf0c-5a9e-87cc-fa0437fb8915`) lines 108-136 [crates/gcode/src/index/import_resolution/parser/go_rust.rs:108-136]
  - Signature: `fn register_rust_group_imports(`
  - Purpose: Recursively parses a comma-separated Rust `use` group, registering individual non-wildcard import paths by composing them with a prefix and recursively processing nested groups. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:108-136]
- `register_rust_path_import` (function) component `register_rust_path_import [function]` (`cd7395b3-be22-5552-8d59-09fe129eee76`) lines 138-188 [crates/gcode/src/index/import_resolution/parser/go_rust.rs:138-188]
  - Signature: `fn register_rust_path_import(`
  - Purpose: Registers a Rust import path by parsing its module hierarchy, validating the external root module, and populating extraction bindings for the root, imported symbol, and optional local alias. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:138-188]
- `non_import_go_statement_does_not_record_raw_import` (function) component `non_import_go_statement_does_not_record_raw_import [function]` (`5bf53bfb-5e8c-5982-8126-7de7c1838571`) lines 195-206 [crates/gcode/src/index/import_resolution/parser/go_rust.rs:195-206]
  - Signature: `fn non_import_go_statement_does_not_record_raw_import() {`
  - Purpose: This test function verifies that `parse_go_import_statement` rejects non-import Go statements (like package declarations) and does not populate the extracted imports collection. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:195-206]
- `non_use_rust_statement_does_not_record_raw_import` (function) component `non_use_rust_statement_does_not_record_raw_import [function]` (`1198e746-172a-5cb1-b20f-e9369afc0ee6`) lines 209-219 [crates/gcode/src/index/import_resolution/parser/go_rust.rs:209-219]
  - Signature: `fn non_use_rust_statement_does_not_record_raw_import() {`
  - Purpose: This test verifies that parsing a Rust module declaration statement (`mod tests;`) does not populate the `ExtractedImports::imports` collection. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:209-219]

