---
title: crates/gcode/src/index/import_resolution/predicates.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/predicates.rs
  ranges:
  - 8-21
  - 23-53
  - 55-68
  - 70-77
  - 79-81
  - 83-88
  - 94-107
  - 109-179
  - 185-201
  - 203-210
  - 212-220
  - 222-231
  - 233-241
  - 243-251
  - 258-262
  - 264-276
  - 284-288
  - 290-302
  - 304-316
  - 318-328
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/predicates.rs:8-21](crates/gcode/src/index/import_resolution/predicates.rs#L8-L21), [crates/gcode/src/index/import_resolution/predicates.rs:23-53](crates/gcode/src/index/import_resolution/predicates.rs#L23-L53), [crates/gcode/src/index/import_resolution/predicates.rs:55-68](crates/gcode/src/index/import_resolution/predicates.rs#L55-L68), [crates/gcode/src/index/import_resolution/predicates.rs:70-77](crates/gcode/src/index/import_resolution/predicates.rs#L70-L77), [crates/gcode/src/index/import_resolution/predicates.rs:79-81](crates/gcode/src/index/import_resolution/predicates.rs#L79-L81), [crates/gcode/src/index/import_resolution/predicates.rs:83-88](crates/gcode/src/index/import_resolution/predicates.rs#L83-L88), [crates/gcode/src/index/import_resolution/predicates.rs:94-107](crates/gcode/src/index/import_resolution/predicates.rs#L94-L107), [crates/gcode/src/index/import_resolution/predicates.rs:109-179](crates/gcode/src/index/import_resolution/predicates.rs#L109-L179), [crates/gcode/src/index/import_resolution/predicates.rs:185-201](crates/gcode/src/index/import_resolution/predicates.rs#L185-L201), [crates/gcode/src/index/import_resolution/predicates.rs:203-210](crates/gcode/src/index/import_resolution/predicates.rs#L203-L210), [crates/gcode/src/index/import_resolution/predicates.rs:212-220](crates/gcode/src/index/import_resolution/predicates.rs#L212-L220), [crates/gcode/src/index/import_resolution/predicates.rs:222-231](crates/gcode/src/index/import_resolution/predicates.rs#L222-L231), [crates/gcode/src/index/import_resolution/predicates.rs:233-241](crates/gcode/src/index/import_resolution/predicates.rs#L233-L241), [crates/gcode/src/index/import_resolution/predicates.rs:243-251](crates/gcode/src/index/import_resolution/predicates.rs#L243-L251), [crates/gcode/src/index/import_resolution/predicates.rs:258-262](crates/gcode/src/index/import_resolution/predicates.rs#L258-L262), [crates/gcode/src/index/import_resolution/predicates.rs:264-276](crates/gcode/src/index/import_resolution/predicates.rs#L264-L276), [crates/gcode/src/index/import_resolution/predicates.rs:284-288](crates/gcode/src/index/import_resolution/predicates.rs#L284-L288), [crates/gcode/src/index/import_resolution/predicates.rs:290-302](crates/gcode/src/index/import_resolution/predicates.rs#L290-L302), [crates/gcode/src/index/import_resolution/predicates.rs:304-316](crates/gcode/src/index/import_resolution/predicates.rs#L304-L316), [crates/gcode/src/index/import_resolution/predicates.rs:318-328](crates/gcode/src/index/import_resolution/predicates.rs#L318-L328)

</details>

# crates/gcode/src/index/import_resolution/predicates.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

This file հավաքляет language-specific predicates and helpers for import resolution. It decides whether a module or symbol is external or local for Python, JavaScript, Go, Rust, Java, C#, PHP, Dart, Ruby, and Elixir; computes known root sets such as Rust external crates, Ruby require roots, and bundled dependency roots; and provides parsing helpers like stripping comments/string literals, extracting declared types/symbols, and deriving JavaScript package names for matching imports against the current project context.
[crates/gcode/src/index/import_resolution/predicates.rs:8-21]
[crates/gcode/src/index/import_resolution/predicates.rs:23-53]
[crates/gcode/src/index/import_resolution/predicates.rs:55-68]
[crates/gcode/src/index/import_resolution/predicates.rs:70-77]
[crates/gcode/src/index/import_resolution/predicates.rs:79-81]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `is_external_python_module` | function | `pub(super) fn is_external_python_module(` | `is_external_python_module [function]` | `fbbc5ccd-520a-5fb2-a4fb-4ceae8c40cc1` | 8-21 [crates/gcode/src/index/import_resolution/predicates.rs:8-21] | Indexed function `is_external_python_module` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:8-21] |
| `is_external_js_module` | function | `pub(super) fn is_external_js_module(` | `is_external_js_module [function]` | `2319f890-edce-5c2e-9435-77d899988ae1` | 23-53 [crates/gcode/src/index/import_resolution/predicates.rs:23-53] | Indexed function `is_external_js_module` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:23-53] |
| `is_external_go_module` | function | `pub(super) fn is_external_go_module(` | `is_external_go_module [function]` | `9d383cd8-fd58-5d43-a5e7-357e263978fe` | 55-68 [crates/gcode/src/index/import_resolution/predicates.rs:55-68] | Indexed function `is_external_go_module` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:55-68] |
| `rust_external_roots` | function | `pub(super) fn rust_external_roots(import_context: &ImportResolutionContext) -> HashSet<String> {` | `rust_external_roots [function]` | `dee82bc9-faa1-578e-be45-17e36c48a96b` | 70-77 [crates/gcode/src/index/import_resolution/predicates.rs:70-77] | Indexed function `rust_external_roots` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:70-77] |
| `java_declared_types` | function | `pub(super) fn java_declared_types(contents: &str) -> Vec<String> {` | `java_declared_types [function]` | `d7fae8f4-0d16-53f8-a8a8-f558d74cc06b` | 79-81 [crates/gcode/src/index/import_resolution/predicates.rs:79-81] | Indexed function `java_declared_types` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:79-81] |
| `csharp_declared_types` | function | `pub(super) fn csharp_declared_types(contents: &str) -> Vec<String> {` | `csharp_declared_types [function]` | `f01981c0-48f2-54c8-9e40-3d182ad2e1b2` | 83-88 [crates/gcode/src/index/import_resolution/predicates.rs:83-88] | Indexed function `csharp_declared_types` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:83-88] |
| `declared_types` | function | `pub(super) fn declared_types(contents: &str, keywords: &[&str]) -> Vec<String> {` | `declared_types [function]` | `c25add13-2c25-5165-a675-a2079d9af1dc` | 94-107 [crates/gcode/src/index/import_resolution/predicates.rs:94-107] | Indexed function `declared_types` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:94-107] |
| `strip_comments_and_string_literals` | function | `fn strip_comments_and_string_literals(contents: &str) -> String {` | `strip_comments_and_string_literals [function]` | `a6a70123-43da-54b7-809e-8adade8495b8` | 109-179 [crates/gcode/src/index/import_resolution/predicates.rs:109-179] | Indexed function `strip_comments_and_string_literals` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:109-179] |
| `php_declared_symbols` | function | `pub(super) fn php_declared_symbols(contents: &str) -> Vec<String> {` | `php_declared_symbols [function]` | `7e80997d-60c8-58e0-a9aa-b3ab88d66d0d` | 185-201 [crates/gcode/src/index/import_resolution/predicates.rs:185-201] | Indexed function `php_declared_symbols` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:185-201] |
| `is_external_java_class` | function | `pub(super) fn is_external_java_class(` | `is_external_java_class [function]` | `64ee3a21-9033-55f6-8090-a87ddf5302f6` | 203-210 [crates/gcode/src/index/import_resolution/predicates.rs:203-210] | Indexed function `is_external_java_class` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:203-210] |
| `java_class_name_candidates` | function | `fn java_class_name_candidates(class_path: &str) -> impl Iterator<Item = &str> {` | `java_class_name_candidates [function]` | `7202dbb0-1eaf-5b4f-85e8-92f66ee9fa9d` | 212-220 [crates/gcode/src/index/import_resolution/predicates.rs:212-220] | Indexed function `java_class_name_candidates` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:212-220] |
| `is_external_csharp_path` | function | `pub(super) fn is_external_csharp_path(` | `is_external_csharp_path [function]` | `15c50f67-3646-5725-b3b4-9361314d60e2` | 222-231 [crates/gcode/src/index/import_resolution/predicates.rs:222-231] | Indexed function `is_external_csharp_path` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:222-231] |
| `is_external_php_symbol` | function | `pub(super) fn is_external_php_symbol(path: &str, import_context: &ImportResolutionContext) -> bool {` | `is_external_php_symbol [function]` | `dd3eb58a-807c-5cde-a6ee-90d4f0868ef5` | 233-241 [crates/gcode/src/index/import_resolution/predicates.rs:233-241] | Indexed function `is_external_php_symbol` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:233-241] |
| `is_external_rust_root` | function | `pub(super) fn is_external_rust_root(root: &str, import_context: &ImportResolutionContext) -> bool {` | `is_external_rust_root [function]` | `d9886b64-f5e1-52ae-8259-f0c7664322ef` | 243-251 [crates/gcode/src/index/import_resolution/predicates.rs:243-251] | Indexed function `is_external_rust_root` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:243-251] |
| `ruby_require_root` | function | `pub(super) fn ruby_require_root(required: &str) -> Option<&'static str> {` | `ruby_require_root [function]` | `4f9d45c2-4c18-51b9-a1b0-37b2205e87e5` | 258-262 [crates/gcode/src/index/import_resolution/predicates.rs:258-262] | Indexed function `ruby_require_root` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:258-262] |
| `is_external_dart_uri` | function | `pub(super) fn is_external_dart_uri(uri: &str, import_context: &ImportResolutionContext) -> bool {` | `is_external_dart_uri [function]` | `9f331ecd-b7b3-5b5c-8b92-fbf1baddb8b5` | 264-276 [crates/gcode/src/index/import_resolution/predicates.rs:264-276] | Indexed function `is_external_dart_uri` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:264-276] |
| `elixir_dependency_roots` | function | `pub(super) fn elixir_dependency_roots(dep: &str) -> Option<&'static [String]> {` | `elixir_dependency_roots [function]` | `9861ab57-6ed5-50dd-95da-55bb7e704639` | 284-288 [crates/gcode/src/index/import_resolution/predicates.rs:284-288] | Indexed function `elixir_dependency_roots` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:284-288] |
| `bundled_ruby_require_roots` | function | `pub(super) fn bundled_ruby_require_roots() -> &'static HashMap<String, String> {` | `bundled_ruby_require_roots [function]` | `695b0196-73f2-5797-a1f8-f951b61868c2` | 290-302 [crates/gcode/src/index/import_resolution/predicates.rs:290-302] | Indexed function `bundled_ruby_require_roots` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:290-302] |
| `bundled_elixir_dependency_roots` | function | `pub(super) fn bundled_elixir_dependency_roots() -> &'static HashMap<String, Vec<String>> {` | `bundled_elixir_dependency_roots [function]` | `8b7cfd97-1642-548e-b453-38fc109332d4` | 304-316 [crates/gcode/src/index/import_resolution/predicates.rs:304-316] | Indexed function `bundled_elixir_dependency_roots` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:304-316] |
| `js_package_name` | function | `pub(super) fn js_package_name(module: &str) -> Option<&str> {` | `js_package_name [function]` | `20869d7c-4781-5392-8754-20e32a1562ad` | 318-328 [crates/gcode/src/index/import_resolution/predicates.rs:318-328] | Indexed function `js_package_name` in `crates/gcode/src/index/import_resolution/predicates.rs`. [crates/gcode/src/index/import_resolution/predicates.rs:318-328] |
