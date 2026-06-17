---
title: crates/gcode/src/index/import_resolution/parser/php_kotlin.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/php_kotlin.rs
  ranges:
  - 9-16
  - 18-61
  - 64-68
  - 70-136
  - 138-189
  - 199-226
  - 228-247
  - 249-262
  - 264-270
  - 272-292
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:9-16](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L9-L16), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:18-61](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L18-L61), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:64-68](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L64-L68), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:70-136](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L70-L136), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:138-189](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L138-L189), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:199-226](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L199-L226), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:228-247](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L228-L247), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:249-262](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L249-L262), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:264-270](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L264-L270), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:272-292](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L272-L292)

</details>

# crates/gcode/src/index/import_resolution/parser/php_kotlin.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

Parses PHP and Kotlin import statements for import resolution, normalizing each statement and turning it into `ExtractedImports` entries in the current `ImportResolutionContext`. The PHP side handles local-symbol checks, import kind detection, grouped and comma-separated `use` forms, wildcard/module derivation, and registration of class, function, and const imports; the Kotlin side does the same for `import` syntax, including alias and wildcard handling. Helper functions split and join PHP `use` paths, seed local PHP imports, and register either specific imports or wildcard/module bindings so downstream resolution can match local and external symbols consistently.
[crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:9-16]
[crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:18-61]
[crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:64-68]
[crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:70-136]
[crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:138-189]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `php_local_symbol_exists` | function | `pub(crate) fn php_local_symbol_exists(` | `php_local_symbol_exists [function]` | `7bcb73e7-eaed-59fb-8374-236c08833d88` | 9-16 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:9-16] | Indexed function `php_local_symbol_exists` in `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs`. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:9-16] |
| `parse_php_import_statement` | function | `pub(crate) fn parse_php_import_statement(` | `parse_php_import_statement [function]` | `0225aeb4-7bb6-5b85-b952-55e351e25a18` | 18-61 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:18-61] | Indexed function `parse_php_import_statement` in `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs`. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:18-61] |
| `PhpImportKind` | type | `enum PhpImportKind {` | `PhpImportKind [type]` | `ebe68bb0-90a5-5c94-8f98-745d79c0a81c` | 64-68 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:64-68] | Indexed type `PhpImportKind` in `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs`. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:64-68] |
| `parse_kotlin_import_statement` | function | `pub(crate) fn parse_kotlin_import_statement(` | `parse_kotlin_import_statement [function]` | `54027118-15a2-5aa6-9613-0fc66b68c61b` | 70-136 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:70-136] | Indexed function `parse_kotlin_import_statement` in `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs`. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:70-136] |
| `register_php_import_item` | function | `fn register_php_import_item(` | `register_php_import_item [function]` | `39ad1c9e-b8b5-587e-8581-92eee1187170` | 138-189 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:138-189] | Indexed function `register_php_import_item` in `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs`. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:138-189] |
| `seed_php_local_import` | function | `fn seed_php_local_import(` | `seed_php_local_import [function]` | `fbb0efc4-f84e-5b91-b868-80d1c252d06a` | 199-226 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:199-226] | Indexed function `seed_php_local_import` in `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs`. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:199-226] |
| `register_php_import_or_wildcard` | function | `fn register_php_import_or_wildcard(` | `register_php_import_or_wildcard [function]` | `4f4a5f16-d7ff-50ec-bf39-e1229f684afd` | 228-247 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:228-247] | Indexed function `register_php_import_or_wildcard` in `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs`. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:228-247] |
| `php_wildcard_module` | function | `fn php_wildcard_module(item: &str) -> Option<String> {` | `php_wildcard_module [function]` | `15993d02-9907-5488-b5c0-b52c31fd986f` | 249-262 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:249-262] | Indexed function `php_wildcard_module` in `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs`. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:249-262] |
| `split_php_use_group` | function | `fn split_php_use_group(text: &str) -> Option<(&str, &str)> {` | `split_php_use_group [function]` | `5a9aa418-d366-5ca3-b7fb-f170aad815e8` | 264-270 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:264-270] | Indexed function `split_php_use_group` in `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs`. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:264-270] |
| `php_join_use_path` | function | `fn php_join_use_path(prefix: &str, item: &str) -> Option<String> {` | `php_join_use_path [function]` | `f5470716-fd61-586e-9f39-adeecc5033a5` | 272-292 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:272-292] | Indexed function `php_join_use_path` in `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs`. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:272-292] |
