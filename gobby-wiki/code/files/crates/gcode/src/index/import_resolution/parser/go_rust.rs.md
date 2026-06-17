---
title: crates/gcode/src/index/import_resolution/parser/go_rust.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/go_rust.rs
  ranges:
  - 12-40
  - 42-96
  - 98-125
  - 127-162
  - 164-229
  - 236-247
  - 250-260
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L12-L40), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:42-96](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L42-L96), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:98-125](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L98-L125), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:127-162](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L127-L162), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:164-229](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L164-L229), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:236-247](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L236-L247), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:250-260](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L250-L260)

</details>

# crates/gcode/src/index/import_resolution/parser/go_rust.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

Parses Go and Rust import syntax for the import-resolution indexer. `parse_go_import_statement` and `parse_go_import_spec` extract quoted module paths from single or grouped Go imports, record each import relation, and, when applicable, register local aliases or external bindings while skipping blank and dot imports. `parse_rust_import_statement`, `register_rust_group_imports`, and `register_rust_path_import` do the same for Rust `use` statements, handling grouped imports, path imports, and external-root binding resolution. The two tests confirm that ordinary Go or Rust statements that are not imports do not create raw import records.
[crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40]
[crates/gcode/src/index/import_resolution/parser/go_rust.rs:42-96]
[crates/gcode/src/index/import_resolution/parser/go_rust.rs:98-125]
[crates/gcode/src/index/import_resolution/parser/go_rust.rs:127-162]
[crates/gcode/src/index/import_resolution/parser/go_rust.rs:164-229]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `parse_go_import_statement` | function | `pub(crate) fn parse_go_import_statement(` | `parse_go_import_statement [function]` | `09b2efc9-1277-55d5-bcd5-177f6318698b` | 12-40 [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40] | Indexed function `parse_go_import_statement` in `crates/gcode/src/index/import_resolution/parser/go_rust.rs`. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40] |
| `parse_go_import_spec` | function | `fn parse_go_import_spec(` | `parse_go_import_spec [function]` | `4f70d13c-23e0-5f16-a6c6-69ce69537432` | 42-96 [crates/gcode/src/index/import_resolution/parser/go_rust.rs:42-96] | Indexed function `parse_go_import_spec` in `crates/gcode/src/index/import_resolution/parser/go_rust.rs`. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:42-96] |
| `parse_rust_import_statement` | function | `pub(crate) fn parse_rust_import_statement(` | `parse_rust_import_statement [function]` | `9c57e3f5-8a2a-5fa3-a1a7-baf71c849708` | 98-125 [crates/gcode/src/index/import_resolution/parser/go_rust.rs:98-125] | Indexed function `parse_rust_import_statement` in `crates/gcode/src/index/import_resolution/parser/go_rust.rs`. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:98-125] |
| `register_rust_group_imports` | function | `fn register_rust_group_imports(` | `register_rust_group_imports [function]` | `b9f7233b-7a03-51ab-887d-6c70c7d6c327` | 127-162 [crates/gcode/src/index/import_resolution/parser/go_rust.rs:127-162] | Indexed function `register_rust_group_imports` in `crates/gcode/src/index/import_resolution/parser/go_rust.rs`. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:127-162] |
| `register_rust_path_import` | function | `fn register_rust_path_import(` | `register_rust_path_import [function]` | `4f47792a-3f24-5996-ad3e-8f5e2fd5e681` | 164-229 [crates/gcode/src/index/import_resolution/parser/go_rust.rs:164-229] | Indexed function `register_rust_path_import` in `crates/gcode/src/index/import_resolution/parser/go_rust.rs`. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:164-229] |
| `non_import_go_statement_does_not_record_raw_import` | function | `fn non_import_go_statement_does_not_record_raw_import() {` | `non_import_go_statement_does_not_record_raw_import [function]` | `c131ab9b-ef95-501b-b4a9-618083b0fd0e` | 236-247 [crates/gcode/src/index/import_resolution/parser/go_rust.rs:236-247] | Indexed function `non_import_go_statement_does_not_record_raw_import` in `crates/gcode/src/index/import_resolution/parser/go_rust.rs`. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:236-247] |
| `non_use_rust_statement_does_not_record_raw_import` | function | `fn non_use_rust_statement_does_not_record_raw_import() {` | `non_use_rust_statement_does_not_record_raw_import [function]` | `09c34044-9a13-5a41-acce-165cca2751eb` | 250-260 [crates/gcode/src/index/import_resolution/parser/go_rust.rs:250-260] | Indexed function `non_use_rust_statement_does_not_record_raw_import` in `crates/gcode/src/index/import_resolution/parser/go_rust.rs`. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:250-260] |
