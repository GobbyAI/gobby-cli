---
title: crates/gcode/src/index/import_resolution/parser/mod.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/mod.rs
  ranges:
  - 29-54
  - 56-74
  - 76-126
  - 128-203
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/mod.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution/parser|crates/gcode/src/index/import_resolution/parser]]

## Purpose

This module coordinates import-resolution parsing across languages. It dispatches each import statement to the appropriate language-specific parser, falls back to recording an unparsed import when the language is unsupported, seeds external module-root bindings from the import resolution context for Rust and Elixir, and resolves external function callees back to their source modules by combining those bindings with qualified-path analysis and wildcard-import ambiguity checks.
[crates/gcode/src/index/import_resolution/parser/mod.rs:29-54]
[crates/gcode/src/index/import_resolution/parser/mod.rs:56-74]
[crates/gcode/src/index/import_resolution/parser/mod.rs:76-126]
[crates/gcode/src/index/import_resolution/parser/mod.rs:128-203]

## API Symbols

- `parse_import_statement` (function) component `parse_import_statement [function]` (`42ae76be-6ef2-51f4-a9d0-db788ea9cbba`) lines 29-54 [crates/gcode/src/index/import_resolution/parser/mod.rs:29-54]
  - Signature: `pub(crate) fn parse_import_statement(`
  - Purpose: Dispatches import statement parsing to language-specific handler functions based on the input language parameter, with fallback to unparsed import tracking for unsupported languages. [crates/gcode/src/index/import_resolution/parser/mod.rs:29-54]
- `push_unparsed_import` (function) component `push_unparsed_import [function]` (`ebf4eb51-028a-5909-8da9-325dbbb89705`) lines 56-74 [crates/gcode/src/index/import_resolution/parser/mod.rs:56-74]
  - Signature: `pub(super) fn push_unparsed_import(`
  - Purpose: Validates and records an unparsed import fallback by appending a prefixed `ImportRelation` to the extracted imports collection. [crates/gcode/src/index/import_resolution/parser/mod.rs:56-74]
- `seed_import_bindings` (function) component `seed_import_bindings [function]` (`3d6658af-dec0-5ed6-9ef6-23af85f8d081`) lines 76-126 [crates/gcode/src/index/import_resolution/parser/mod.rs:76-126]
  - Signature: `pub(crate) fn seed_import_bindings(`
  - Purpose: # Summary

Populates the `ImportBindings` external_roots map with language-specific external module root bindings extracted from the `ImportResolutionContext`, applying distinct resolution logic for Rust and Elixir. [crates/gcode/src/index/import_resolution/parser/mod.rs:76-126]
- `resolve_external_callee` (function) component `resolve_external_callee [function]` (`4be33aa6-bc44-53dc-a95e-2d90037f0ff0`) lines 128-203 [crates/gcode/src/index/import_resolution/parser/mod.rs:128-203]
  - Signature: `pub(crate) fn resolve_external_callee(`
  - Purpose: Resolves an external function callee to its source module by consulting import bindings and qualified paths, disambiguating between bare and qualified calls while detecting ambiguous wildcard imports. [crates/gcode/src/index/import_resolution/parser/mod.rs:128-203]

