---
title: crates/gcode/src/index/import_resolution/parser/rest.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/rest.rs
  ranges:
  - 10-54
  - 56-92
  - 94-152
  - 154-233
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/parser/rest.rs:10-54](crates/gcode/src/index/import_resolution/parser/rest.rs#L10-L54), [crates/gcode/src/index/import_resolution/parser/rest.rs:56-92](crates/gcode/src/index/import_resolution/parser/rest.rs#L56-L92), [crates/gcode/src/index/import_resolution/parser/rest.rs:94-152](crates/gcode/src/index/import_resolution/parser/rest.rs#L94-L152), [crates/gcode/src/index/import_resolution/parser/rest.rs:154-233](crates/gcode/src/index/import_resolution/parser/rest.rs#L154-L233)

</details>

# crates/gcode/src/index/import_resolution/parser/rest.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

Parses import-like statements for several languages and records them as `ImportRelation` entries, while also resolving external root bindings when the import can be mapped to a non-local module. The four parsers handle language-specific syntax for Swift, Ruby, Dart, and Elixir, but share the same pattern: normalize the line, extract the module or quoted target, push the import into `ExtractedImports`, and consult `ImportResolutionContext` plus helper predicates/functions to decide whether to register an external root or alias information.
[crates/gcode/src/index/import_resolution/parser/rest.rs:10-54]
[crates/gcode/src/index/import_resolution/parser/rest.rs:56-92]
[crates/gcode/src/index/import_resolution/parser/rest.rs:94-152]
[crates/gcode/src/index/import_resolution/parser/rest.rs:154-233]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `parse_swift_import_statement` | function | `pub(crate) fn parse_swift_import_statement(` | `parse_swift_import_statement [function]` | `e43548a5-2a3b-51ca-a297-cf5686b2dc57` | 10-54 [crates/gcode/src/index/import_resolution/parser/rest.rs:10-54] | Indexed function `parse_swift_import_statement` in `crates/gcode/src/index/import_resolution/parser/rest.rs`. [crates/gcode/src/index/import_resolution/parser/rest.rs:10-54] |
| `parse_ruby_import_statement` | function | `pub(crate) fn parse_ruby_import_statement(` | `parse_ruby_import_statement [function]` | `bdf2899e-c0cb-53d5-9e06-78efe985bb44` | 56-92 [crates/gcode/src/index/import_resolution/parser/rest.rs:56-92] | Indexed function `parse_ruby_import_statement` in `crates/gcode/src/index/import_resolution/parser/rest.rs`. [crates/gcode/src/index/import_resolution/parser/rest.rs:56-92] |
| `parse_dart_import_statement` | function | `pub(crate) fn parse_dart_import_statement(` | `parse_dart_import_statement [function]` | `b7b78884-8762-5fa4-87ba-b83d91ca6c80` | 94-152 [crates/gcode/src/index/import_resolution/parser/rest.rs:94-152] | Indexed function `parse_dart_import_statement` in `crates/gcode/src/index/import_resolution/parser/rest.rs`. [crates/gcode/src/index/import_resolution/parser/rest.rs:94-152] |
| `parse_elixir_import_statement` | function | `pub(crate) fn parse_elixir_import_statement(` | `parse_elixir_import_statement [function]` | `50be796b-ea81-528d-8c6c-9654adee1305` | 154-233 [crates/gcode/src/index/import_resolution/parser/rest.rs:154-233] | Indexed function `parse_elixir_import_statement` in `crates/gcode/src/index/import_resolution/parser/rest.rs`. [crates/gcode/src/index/import_resolution/parser/rest.rs:154-233] |
