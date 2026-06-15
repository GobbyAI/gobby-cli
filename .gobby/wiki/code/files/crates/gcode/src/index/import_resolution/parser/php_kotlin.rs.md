---
title: crates/gcode/src/index/import_resolution/parser/php_kotlin.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/php_kotlin.rs
  ranges:
  - 7-14
  - 16-59
  - 62-66
  - 68-104
  - 106-147
  - 149-168
  - 170-183
  - 185-191
  - 193-213
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/php_kotlin.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution/parser|crates/gcode/src/index/import_resolution/parser]]

## Purpose

This file contains import-resolution parsers for PHP and Kotlin. It provides helpers to check whether a PHP local symbol exists case-insensitively, parse PHP `use` statements into class/function/const imports, and parse Kotlin `import` statements into extracted bindings. The PHP side handles grouped and ungrouped forms, wildcard imports, aliasing, and namespace path joining, while the Kotlin side records import targets and aliases and creates symbol-to-module bindings for external Java classes.
[crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:7-14]
[crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:16-59]
[crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:62-66]
[crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:68-104]
[crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:106-147]

## API Symbols

- `php_local_symbol_exists` (function) component `php_local_symbol_exists [function]` (`9d0cf291-80b8-561b-89b5-e1c1cf992098`) lines 7-14 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:7-14]
  - Signature: `pub(crate) fn php_local_symbol_exists(`
  - Purpose: Checks whether a PHP symbol exists in the import context's local symbols collection using case-insensitive comparison. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:7-14]
- `parse_php_import_statement` (function) component `parse_php_import_statement [function]` (`8a4fb0c6-b6c9-514c-a9b2-35d6261ffd1d`) lines 16-59 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:16-59]
  - Signature: `pub(crate) fn parse_php_import_statement(`
  - Purpose: Parses a PHP `use` statement, extracts individual imports categorized by kind (function/const/class-like), handles grouped and ungrouped import forms, and registers them in the provided extraction context. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:16-59]
- `PhpImportKind` (type) component `PhpImportKind [type]` (`d0eb6e1f-cacc-536d-8ad3-65e661acaedb`) lines 62-66 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:62-66]
  - Signature: `enum PhpImportKind {`
  - Purpose: Indexed type `PhpImportKind` in `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs`. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:62-66]
- `parse_kotlin_import_statement` (function) component `parse_kotlin_import_statement [function]` (`344a756e-ef65-554e-adda-c6414e768359`) lines 68-104 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:68-104]
  - Signature: `pub(crate) fn parse_kotlin_import_statement(`
  - Purpose: Extracts and records Kotlin import statements while creating symbol-to-module bindings for non-wildcard external Java classes, handling import aliases in the process. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:68-104]
- `register_php_import_item` (function) component `register_php_import_item [function]` (`d14f20b1-7d41-5049-bc5d-16e27d701598`) lines 106-147 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:106-147]
  - Signature: `fn register_php_import_item(`
  - Purpose: Registers a PHP import item by parsing its namespace-qualified target and optional alias, then stores the appropriate binding (either a namespaced function or qualified class/constant) in the extracted imports structure. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:106-147]
- `register_php_import_or_wildcard` (function) component `register_php_import_or_wildcard [function]` (`8a75b2a5-d532-5828-87f4-f1af978fc6e7`) lines 149-168 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:149-168]
  - Signature: `fn register_php_import_or_wildcard(`
  - Purpose: Registers a PHP import by extracting wildcard modules and tracking external symbols separately, or delegates to standard item import registration for non-wildcard imports. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:149-168]
- `php_wildcard_module` (function) component `php_wildcard_module [function]` (`352830db-1cc4-54fc-95dd-37c91592e63e`) lines 170-183 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:170-183]
  - Signature: `fn php_wildcard_module(item: &str) -> Option<String> {`
  - Purpose: Extracts the PHP namespace module path (segments before a wildcard character) from a use statement alias, returning None if no wildcard or valid module exists. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:170-183]
- `split_php_use_group` (function) component `split_php_use_group [function]` (`9b01598a-a9e4-59a8-a095-a5633f8ee2cb`) lines 185-191 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:185-191]
  - Signature: `fn split_php_use_group(text: &str) -> Option<(&str, &str)> {`
  - Purpose: Splits a PHP use group string into base and group components via `split_rust_use_group`, returning `Some((base, group))` only if both components are non-empty. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:185-191]
- `php_join_use_path` (function) component `php_join_use_path [function]` (`46e6ba59-99c4-5804-aedc-4c1a39955cc5`) lines 193-213 [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:193-213]
  - Signature: `fn php_join_use_path(prefix: &str, item: &str) -> Option<String> {`
  - Purpose: Joins a PHP namespace prefix with an item path (with optional alias), normalizing backslash delimiters and returning None if the path is empty. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:193-213]

