---
title: crates/gcode/src/index/import_resolution/parser/mod.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/mod.rs
  ranges:
  - 40-69
  - 71-89
  - 91-141
  - 143-218
  - 220-233
  - 235-254
  - 265-291
  - 302-323
  - 334-351
  - 360-384
  - 402-439
  - 441-453
  - 469-507
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/parser/mod.rs:40-69](crates/gcode/src/index/import_resolution/parser/mod.rs#L40-L69), [crates/gcode/src/index/import_resolution/parser/mod.rs:71-89](crates/gcode/src/index/import_resolution/parser/mod.rs#L71-L89), [crates/gcode/src/index/import_resolution/parser/mod.rs:91-141](crates/gcode/src/index/import_resolution/parser/mod.rs#L91-L141), [crates/gcode/src/index/import_resolution/parser/mod.rs:143-218](crates/gcode/src/index/import_resolution/parser/mod.rs#L143-L218), [crates/gcode/src/index/import_resolution/parser/mod.rs:220-233](crates/gcode/src/index/import_resolution/parser/mod.rs#L220-L233), [crates/gcode/src/index/import_resolution/parser/mod.rs:235-254](crates/gcode/src/index/import_resolution/parser/mod.rs#L235-L254), [crates/gcode/src/index/import_resolution/parser/mod.rs:265-291](crates/gcode/src/index/import_resolution/parser/mod.rs#L265-L291), [crates/gcode/src/index/import_resolution/parser/mod.rs:302-323](crates/gcode/src/index/import_resolution/parser/mod.rs#L302-L323), [crates/gcode/src/index/import_resolution/parser/mod.rs:334-351](crates/gcode/src/index/import_resolution/parser/mod.rs#L334-L351), [crates/gcode/src/index/import_resolution/parser/mod.rs:360-384](crates/gcode/src/index/import_resolution/parser/mod.rs#L360-L384), [crates/gcode/src/index/import_resolution/parser/mod.rs:402-439](crates/gcode/src/index/import_resolution/parser/mod.rs#L402-L439), [crates/gcode/src/index/import_resolution/parser/mod.rs:441-453](crates/gcode/src/index/import_resolution/parser/mod.rs#L441-L453), [crates/gcode/src/index/import_resolution/parser/mod.rs:469-507](crates/gcode/src/index/import_resolution/parser/mod.rs#L469-L507)

</details>

# crates/gcode/src/index/import_resolution/parser/mod.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

This module is the import-resolution parser for indexed source files. `parse_import_statement` dispatches by language to the appropriate language-specific import parser, while `push_unparsed_import` records imports that could not be fully interpreted. `seed_import_bindings` builds the initial binding state from extracted imports and context, and the various `resolve_*_callee` helpers then map call sites to imported targets or local symbols across languages like Ruby, PHP, Swift, Dart, Elixir, Rust, and C#.
[crates/gcode/src/index/import_resolution/parser/mod.rs:40-69]
[crates/gcode/src/index/import_resolution/parser/mod.rs:71-89]
[crates/gcode/src/index/import_resolution/parser/mod.rs:91-141]
[crates/gcode/src/index/import_resolution/parser/mod.rs:143-218]
[crates/gcode/src/index/import_resolution/parser/mod.rs:220-233]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `parse_import_statement` | function | `pub(crate) fn parse_import_statement(` | `parse_import_statement [function]` | `9d0855cb-3d92-571d-83b9-a1ad069e87e6` | 40-69 [crates/gcode/src/index/import_resolution/parser/mod.rs:40-69] | Indexed function `parse_import_statement` in `crates/gcode/src/index/import_resolution/parser/mod.rs`. [crates/gcode/src/index/import_resolution/parser/mod.rs:40-69] |
| `push_unparsed_import` | function | `pub(super) fn push_unparsed_import(` | `push_unparsed_import [function]` | `11ca3348-1d6a-5111-8f72-a5aeaa606614` | 71-89 [crates/gcode/src/index/import_resolution/parser/mod.rs:71-89] | Indexed function `push_unparsed_import` in `crates/gcode/src/index/import_resolution/parser/mod.rs`. [crates/gcode/src/index/import_resolution/parser/mod.rs:71-89] |
| `seed_import_bindings` | function | `pub(crate) fn seed_import_bindings(` | `seed_import_bindings [function]` | `82839e7b-dca9-57a5-a62b-6014b02782d8` | 91-141 [crates/gcode/src/index/import_resolution/parser/mod.rs:91-141] | Indexed function `seed_import_bindings` in `crates/gcode/src/index/import_resolution/parser/mod.rs`. [crates/gcode/src/index/import_resolution/parser/mod.rs:91-141] |
| `resolve_external_callee` | function | `pub(crate) fn resolve_external_callee(` | `resolve_external_callee [function]` | `830a7161-e44c-5286-9282-4efe3ec9137a` | 143-218 [crates/gcode/src/index/import_resolution/parser/mod.rs:143-218] | Indexed function `resolve_external_callee` in `crates/gcode/src/index/import_resolution/parser/mod.rs`. [crates/gcode/src/index/import_resolution/parser/mod.rs:143-218] |
| `resolve_local_callee` | function | `pub(crate) fn resolve_local_callee(` | `resolve_local_callee [function]` | `fa6161a5-bd8c-5e90-83c9-f3ec61f9ba92` | 220-233 [crates/gcode/src/index/import_resolution/parser/mod.rs:220-233] | Indexed function `resolve_local_callee` in `crates/gcode/src/index/import_resolution/parser/mod.rs`. [crates/gcode/src/index/import_resolution/parser/mod.rs:220-233] |
| `resolve_local_member_callee` | function | `pub(crate) fn resolve_local_member_callee(` | `resolve_local_member_callee [function]` | `4288d21a-f368-5308-9fc5-3cd40b8bf5b9` | 235-254 [crates/gcode/src/index/import_resolution/parser/mod.rs:235-254] | Indexed function `resolve_local_member_callee` in `crates/gcode/src/index/import_resolution/parser/mod.rs`. [crates/gcode/src/index/import_resolution/parser/mod.rs:235-254] |
| `resolve_ruby_local_member_callee` | function | `pub(crate) fn resolve_ruby_local_member_callee(` | `resolve_ruby_local_member_callee [function]` | `afb86bf9-eac2-5548-ad9f-b7e686b9fe64` | 265-291 [crates/gcode/src/index/import_resolution/parser/mod.rs:265-291] | Indexed function `resolve_ruby_local_member_callee` in `crates/gcode/src/index/import_resolution/parser/mod.rs`. [crates/gcode/src/index/import_resolution/parser/mod.rs:265-291] |
| `resolve_php_local_member_callee` | function | `pub(crate) fn resolve_php_local_member_callee(` | `resolve_php_local_member_callee [function]` | `2253dff6-aefd-5b3c-8e1b-8af0871c1a1a` | 302-323 [crates/gcode/src/index/import_resolution/parser/mod.rs:302-323] | Indexed function `resolve_php_local_member_callee` in `crates/gcode/src/index/import_resolution/parser/mod.rs`. [crates/gcode/src/index/import_resolution/parser/mod.rs:302-323] |
| `resolve_swift_local_callee` | function | `pub(crate) fn resolve_swift_local_callee(` | `resolve_swift_local_callee [function]` | `5b715a52-6ec5-5290-9277-c9c020e34f3f` | 334-351 [crates/gcode/src/index/import_resolution/parser/mod.rs:334-351] | Indexed function `resolve_swift_local_callee` in `crates/gcode/src/index/import_resolution/parser/mod.rs`. [crates/gcode/src/index/import_resolution/parser/mod.rs:334-351] |
| `resolve_dart_local_callee` | function | `pub(crate) fn resolve_dart_local_callee(` | `resolve_dart_local_callee [function]` | `2bff1cb0-961b-54f2-bf2f-986941f45406` | 360-384 [crates/gcode/src/index/import_resolution/parser/mod.rs:360-384] | Indexed function `resolve_dart_local_callee` in `crates/gcode/src/index/import_resolution/parser/mod.rs`. [crates/gcode/src/index/import_resolution/parser/mod.rs:360-384] |
| `resolve_elixir_local_callee` | function | `pub(crate) fn resolve_elixir_local_callee(` | `resolve_elixir_local_callee [function]` | `07bf3cce-3e07-5d73-9a9a-06455b9fc8a2` | 402-439 [crates/gcode/src/index/import_resolution/parser/mod.rs:402-439] | Indexed function `resolve_elixir_local_callee` in `crates/gcode/src/index/import_resolution/parser/mod.rs`. [crates/gcode/src/index/import_resolution/parser/mod.rs:402-439] |
| `resolve_rust_local_qualified_callee` | function | `pub(crate) fn resolve_rust_local_qualified_callee(` | `resolve_rust_local_qualified_callee [function]` | `d36a5bac-400a-508f-9beb-30b2304de6c2` | 441-453 [crates/gcode/src/index/import_resolution/parser/mod.rs:441-453] | Indexed function `resolve_rust_local_qualified_callee` in `crates/gcode/src/index/import_resolution/parser/mod.rs`. [crates/gcode/src/index/import_resolution/parser/mod.rs:441-453] |
| `resolve_csharp_local_member_callee` | function | `pub(crate) fn resolve_csharp_local_member_callee(` | `resolve_csharp_local_member_callee [function]` | `292df235-702b-5f7a-98ee-e3702e20a962` | 469-507 [crates/gcode/src/index/import_resolution/parser/mod.rs:469-507] | Indexed function `resolve_csharp_local_member_callee` in `crates/gcode/src/index/import_resolution/parser/mod.rs`. [crates/gcode/src/index/import_resolution/parser/mod.rs:469-507] |
