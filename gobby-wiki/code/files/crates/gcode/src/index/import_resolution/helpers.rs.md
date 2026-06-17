---
title: crates/gcode/src/index/import_resolution/helpers.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/helpers.rs
  ranges:
  - 3-5
  - 7-13
  - 15-19
  - 21-49
  - 51-88
  - 90-99
  - 101-107
  - 109-136
  - 138-166
  - 169-174
  - 177-183
  - 189-196
  - 199-214
  - 216-305
  - 307-309
  - 311-318
  - 320-332
  - 341-362
  - 368-381
  - 383-385
  - 387-389
  - 391-403
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/helpers.rs:3-5](crates/gcode/src/index/import_resolution/helpers.rs#L3-L5), [crates/gcode/src/index/import_resolution/helpers.rs:7-13](crates/gcode/src/index/import_resolution/helpers.rs#L7-L13), [crates/gcode/src/index/import_resolution/helpers.rs:15-19](crates/gcode/src/index/import_resolution/helpers.rs#L15-L19), [crates/gcode/src/index/import_resolution/helpers.rs:21-49](crates/gcode/src/index/import_resolution/helpers.rs#L21-L49), [crates/gcode/src/index/import_resolution/helpers.rs:51-88](crates/gcode/src/index/import_resolution/helpers.rs#L51-L88), [crates/gcode/src/index/import_resolution/helpers.rs:90-99](crates/gcode/src/index/import_resolution/helpers.rs#L90-L99), [crates/gcode/src/index/import_resolution/helpers.rs:101-107](crates/gcode/src/index/import_resolution/helpers.rs#L101-L107), [crates/gcode/src/index/import_resolution/helpers.rs:109-136](crates/gcode/src/index/import_resolution/helpers.rs#L109-L136), [crates/gcode/src/index/import_resolution/helpers.rs:138-166](crates/gcode/src/index/import_resolution/helpers.rs#L138-L166), [crates/gcode/src/index/import_resolution/helpers.rs:169-174](crates/gcode/src/index/import_resolution/helpers.rs#L169-L174), [crates/gcode/src/index/import_resolution/helpers.rs:177-183](crates/gcode/src/index/import_resolution/helpers.rs#L177-L183), [crates/gcode/src/index/import_resolution/helpers.rs:189-196](crates/gcode/src/index/import_resolution/helpers.rs#L189-L196), [crates/gcode/src/index/import_resolution/helpers.rs:199-214](crates/gcode/src/index/import_resolution/helpers.rs#L199-L214), [crates/gcode/src/index/import_resolution/helpers.rs:216-305](crates/gcode/src/index/import_resolution/helpers.rs#L216-L305), [crates/gcode/src/index/import_resolution/helpers.rs:307-309](crates/gcode/src/index/import_resolution/helpers.rs#L307-L309), [crates/gcode/src/index/import_resolution/helpers.rs:311-318](crates/gcode/src/index/import_resolution/helpers.rs#L311-L318), [crates/gcode/src/index/import_resolution/helpers.rs:320-332](crates/gcode/src/index/import_resolution/helpers.rs#L320-L332), [crates/gcode/src/index/import_resolution/helpers.rs:341-362](crates/gcode/src/index/import_resolution/helpers.rs#L341-L362), [crates/gcode/src/index/import_resolution/helpers.rs:368-381](crates/gcode/src/index/import_resolution/helpers.rs#L368-L381), [crates/gcode/src/index/import_resolution/helpers.rs:383-385](crates/gcode/src/index/import_resolution/helpers.rs#L383-L385), [crates/gcode/src/index/import_resolution/helpers.rs:387-389](crates/gcode/src/index/import_resolution/helpers.rs#L387-L389), [crates/gcode/src/index/import_resolution/helpers.rs:391-403](crates/gcode/src/index/import_resolution/helpers.rs#L391-L403)

</details>

# crates/gcode/src/index/import_resolution/helpers.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

Utilities for import-resolution parsing across several languages. The file provides small string and path helpers to normalize whitespace, extract JavaScript import clauses and module specifiers, read quoted strings safely, and skip over template interpolation while scanning; it also includes language-specific helpers for Go, Rust, Dart, and Elixir alias and path handling.

The main shared parsing piece is `split_top_level`, backed by `SplitTopLevelError` and `split_error_context`, which appears to break import-like text into top-level parts while reporting structured failures. The remaining helpers build on that to recognize naming patterns, split Rust `use` groups, join Rust use paths, normalize relative Dart paths, and derive alias names for Dart and Elixir imports.
[crates/gcode/src/index/import_resolution/helpers.rs:3-5]
[crates/gcode/src/index/import_resolution/helpers.rs:7-13]
[crates/gcode/src/index/import_resolution/helpers.rs:15-19]
[crates/gcode/src/index/import_resolution/helpers.rs:21-49]
[crates/gcode/src/index/import_resolution/helpers.rs:51-88]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `collapse_whitespace` | function | `pub(super) fn collapse_whitespace(text: &str) -> String {` | `collapse_whitespace [function]` | `ec29fd76-d245-585d-924d-14ac4771e05d` | 3-5 [crates/gcode/src/index/import_resolution/helpers.rs:3-5] | Indexed function `collapse_whitespace` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:3-5] |
| `extract_js_module_specifier` | function | `pub(super) fn extract_js_module_specifier(text: &str) -> Option<String> {` | `extract_js_module_specifier [function]` | `59b14148-18b9-5465-b8ec-1cf922aa8636` | 7-13 [crates/gcode/src/index/import_resolution/helpers.rs:7-13] | Indexed function `extract_js_module_specifier` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:7-13] |
| `extract_js_import_clause` | function | `pub(super) fn extract_js_import_clause(text: &str) -> Option<&str> {` | `extract_js_import_clause [function]` | `daeef2df-7014-54fc-b3ef-767c59078fd7` | 15-19 [crates/gcode/src/index/import_resolution/helpers.rs:15-19] | Indexed function `extract_js_import_clause` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:15-19] |
| `extract_quoted_string` | function | `pub(super) fn extract_quoted_string(text: &str) -> Option<String> {` | `extract_quoted_string [function]` | `5cb7ac6e-b815-5545-86d7-a1f19b8d6062` | 21-49 [crates/gcode/src/index/import_resolution/helpers.rs:21-49] | Indexed function `extract_quoted_string` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:21-49] |
| `skip_template_interpolation` | function | `fn skip_template_interpolation(text: &str, mut idx: usize) -> Option<usize> {` | `skip_template_interpolation [function]` | `f30e7119-6ab1-5120-a624-6f4ed5b7485c` | 51-88 [crates/gcode/src/index/import_resolution/helpers.rs:51-88] | Indexed function `skip_template_interpolation` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:51-88] |
| `go_default_package_alias` | function | `pub(super) fn go_default_package_alias(module: &str) -> String {` | `go_default_package_alias [function]` | `e3123a46-a390-5bbb-8842-a1db477aa74d` | 90-99 [crates/gcode/src/index/import_resolution/helpers.rs:90-99] | Indexed function `go_default_package_alias` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:90-99] |
| `split_alias` | function | `pub(super) fn split_alias(text: &str) -> (&str, Option<&str>) {` | `split_alias [function]` | `012b2b43-086f-52fa-91d5-856defaec869` | 101-107 [crates/gcode/src/index/import_resolution/helpers.rs:101-107] | Indexed function `split_alias` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:101-107] |
| `split_rust_use_group` | function | `pub(super) fn split_rust_use_group(text: &str) -> Option<(&str, &str)> {` | `split_rust_use_group [function]` | `603d5098-0683-5fb9-abd0-d03962270a4c` | 109-136 [crates/gcode/src/index/import_resolution/helpers.rs:109-136] | Indexed function `split_rust_use_group` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:109-136] |
| `rust_join_use_path` | function | `pub(super) fn rust_join_use_path(prefix: &str, item: &str) -> Option<String> {` | `rust_join_use_path [function]` | `acbc6ce3-1acb-59b4-99d2-90c13278e3e3` | 138-166 [crates/gcode/src/index/import_resolution/helpers.rs:138-166] | Indexed function `rust_join_use_path` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:138-166] |
| `SplitTopLevelError` | class | `pub(super) struct SplitTopLevelError {` | `SplitTopLevelError [class]` | `e65745d6-0931-5624-9837-0e01889db5a1` | 169-174 [crates/gcode/src/index/import_resolution/helpers.rs:169-174] | Indexed class `SplitTopLevelError` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:169-174] |
| `SplitTopLevelError::fmt` | method | `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {` | `SplitTopLevelError::fmt [method]` | `35d1c3d5-1db7-5768-95d6-1400fc729dc3` | 177-183 [crates/gcode/src/index/import_resolution/helpers.rs:177-183] | Indexed method `SplitTopLevelError::fmt` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:177-183] |
| `SplitTopLevelError::new` | method | `fn new(text: &str, delimiter: char, position: usize, kind: &'static str) -> Self {` | `SplitTopLevelError::new [method]` | `5d3a6051-2b85-5918-b42b-a66bbe0e2655` | 189-196 [crates/gcode/src/index/import_resolution/helpers.rs:189-196] | Indexed method `SplitTopLevelError::new` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:189-196] |
| `split_error_context` | function | `fn split_error_context(text: &str, position: usize) -> String {` | `split_error_context [function]` | `62eaa4e8-ebe3-5277-ac66-6a4eedbdc1b9` | 199-214 [crates/gcode/src/index/import_resolution/helpers.rs:199-214] | Indexed function `split_error_context` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:199-214] |
| `split_top_level` | function | `pub(super) fn split_top_level(` | `split_top_level [function]` | `1e442afc-19cb-5b24-9b9b-56cfcc5f3e78` | 216-305 [crates/gcode/src/index/import_resolution/helpers.rs:216-305] | Indexed function `split_top_level` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:216-305] |
| `is_ruby_constant_name` | function | `pub(super) fn is_ruby_constant_name(name: &str) -> bool {` | `is_ruby_constant_name [function]` | `bf1a96cf-230d-5286-b52f-de5dbf1be144` | 307-309 [crates/gcode/src/index/import_resolution/helpers.rs:307-309] | Indexed function `is_ruby_constant_name` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:307-309] |
| `is_uppercase_ascii_alnum_underscore_name` | function | `fn is_uppercase_ascii_alnum_underscore_name(name: &str) -> bool {` | `is_uppercase_ascii_alnum_underscore_name [function]` | `b8ad0bac-6dd2-55aa-b726-9f551b63e641` | 311-318 [crates/gcode/src/index/import_resolution/helpers.rs:311-318] | Indexed function `is_uppercase_ascii_alnum_underscore_name` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:311-318] |
| `dart_import_alias` | function | `pub(super) fn dart_import_alias(text: &str) -> Option<String> {` | `dart_import_alias [function]` | `491b6d36-e93d-5420-b251-930a14f2c012` | 320-332 [crates/gcode/src/index/import_resolution/helpers.rs:320-332] | Indexed function `dart_import_alias` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:320-332] |
| `dart_local_import_target` | function | `pub(super) fn dart_local_import_target(` | `dart_local_import_target [function]` | `a433f6b2-28d2-59ad-9c2d-fcb5b147563a` | 341-362 [crates/gcode/src/index/import_resolution/helpers.rs:341-362] | Indexed function `dart_local_import_target` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:341-362] |
| `normalize_relative_dart_path` | function | `fn normalize_relative_dart_path(path: &Path) -> String {` | `normalize_relative_dart_path [function]` | `159f0f66-7cfe-55c7-b100-7576a0d4bdee` | 368-381 [crates/gcode/src/index/import_resolution/helpers.rs:368-381] | Indexed function `normalize_relative_dart_path` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:368-381] |
| `is_elixir_alias` | function | `pub(super) fn is_elixir_alias(name: &str) -> bool {` | `is_elixir_alias [function]` | `ed57750f-5f63-5f53-b78b-7e840c66e921` | 383-385 [crates/gcode/src/index/import_resolution/helpers.rs:383-385] | Indexed function `is_elixir_alias` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:383-385] |
| `is_elixir_alias_path` | function | `pub(super) fn is_elixir_alias_path(path: &str) -> bool {` | `is_elixir_alias_path [function]` | `f79450fc-f845-5bac-b6cc-e085cd6cdb1a` | 387-389 [crates/gcode/src/index/import_resolution/helpers.rs:387-389] | Indexed function `is_elixir_alias_path` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:387-389] |
| `elixir_alias_as` | function | `pub(super) fn elixir_alias_as(text: &str) -> Option<String> {` | `elixir_alias_as [function]` | `0e7286e5-50d1-59e2-8b3a-e8c801b59fda` | 391-403 [crates/gcode/src/index/import_resolution/helpers.rs:391-403] | Indexed function `elixir_alias_as` in `crates/gcode/src/index/import_resolution/helpers.rs`. [crates/gcode/src/index/import_resolution/helpers.rs:391-403] |
