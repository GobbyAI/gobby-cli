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

# crates/gcode/src/index/import_resolution/predicates.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

`crates/gcode/src/index/import_resolution/predicates.rs` exposes 20 indexed API symbols.
[crates/gcode/src/index/import_resolution/predicates.rs:8-21]
[crates/gcode/src/index/import_resolution/predicates.rs:23-53]
[crates/gcode/src/index/import_resolution/predicates.rs:55-68]
[crates/gcode/src/index/import_resolution/predicates.rs:70-77]
[crates/gcode/src/index/import_resolution/predicates.rs:79-81]
[crates/gcode/src/index/import_resolution/predicates.rs:83-88]
[crates/gcode/src/index/import_resolution/predicates.rs:94-107]
[crates/gcode/src/index/import_resolution/predicates.rs:109-179]
[crates/gcode/src/index/import_resolution/predicates.rs:185-201]
[crates/gcode/src/index/import_resolution/predicates.rs:203-210]
[crates/gcode/src/index/import_resolution/predicates.rs:212-220]
[crates/gcode/src/index/import_resolution/predicates.rs:222-231]
[crates/gcode/src/index/import_resolution/predicates.rs:233-241]
[crates/gcode/src/index/import_resolution/predicates.rs:243-251]
[crates/gcode/src/index/import_resolution/predicates.rs:258-262]
[crates/gcode/src/index/import_resolution/predicates.rs:264-276]
[crates/gcode/src/index/import_resolution/predicates.rs:284-288]
[crates/gcode/src/index/import_resolution/predicates.rs:290-302]
[crates/gcode/src/index/import_resolution/predicates.rs:304-316]
[crates/gcode/src/index/import_resolution/predicates.rs:318-328]

## API Symbols

- `is_external_python_module` (function) component `is_external_python_module [function]` (`07f657d4-9c5a-56b4-8ddc-3a5d061639d7`) lines 8-21 [crates/gcode/src/index/import_resolution/predicates.rs:8-21]
  - Signature: `pub(super) fn is_external_python_module(`
  - Purpose: Determines whether a module is external by verifying it's not a relative import and doesn't match any local module in the import context (including parent/child package relationships). [crates/gcode/src/index/import_resolution/predicates.rs:8-21]
- `is_external_js_module` (function) component `is_external_js_module [function]` (`750b41c0-111c-5111-9510-6e02889c7d9e`) lines 23-53 [crates/gcode/src/index/import_resolution/predicates.rs:23-53]
  - Signature: `pub(super) fn is_external_js_module(`
  - Purpose: Returns true if a module specifier represents an external JavaScript package (built-in or third-party), excluding relative paths, import aliases, and the current package's internal self-references. [crates/gcode/src/index/import_resolution/predicates.rs:23-53]
- `is_external_go_module` (function) component `is_external_go_module [function]` (`7e7d0299-670d-518b-bf8f-7552a45b1590`) lines 55-68 [crates/gcode/src/index/import_resolution/predicates.rs:55-68]
  - Signature: `pub(super) fn is_external_go_module(`
  - Purpose: Determines whether a Go module is external by returning `false` for relative imports and modules belonging to the current module namespace, and `true` otherwise. [crates/gcode/src/index/import_resolution/predicates.rs:55-68]
- `rust_external_roots` (function) component `rust_external_roots [function]` (`2fcf36cb-7394-5944-b6c5-8fc721bd5f25`) lines 70-77 [crates/gcode/src/index/import_resolution/predicates.rs:70-77]
  - Signature: `pub(super) fn rust_external_roots(import_context: &ImportResolutionContext) -> HashSet<String> {`
  - Purpose: Constructs a HashSet of available external Rust crate names by combining context-provided external crates with standard library crates, then removing the self-crate if defined. [crates/gcode/src/index/import_resolution/predicates.rs:70-77]
- `java_declared_types` (function) component `java_declared_types [function]` (`ff25375d-7cfd-5f19-a7a9-af1337f683f5`) lines 79-81 [crates/gcode/src/index/import_resolution/predicates.rs:79-81]
  - Signature: `pub(super) fn java_declared_types(contents: &str) -> Vec<String> {`
  - Purpose: Returns a vector of names for all declared Java types (classes, interfaces, enums, and records) found in the given source code string. [crates/gcode/src/index/import_resolution/predicates.rs:79-81]
- `csharp_declared_types` (function) component `csharp_declared_types [function]` (`4e36e015-f9be-5008-a6b3-33a07a2d9313`) lines 83-88 [crates/gcode/src/index/import_resolution/predicates.rs:83-88]
  - Signature: `pub(super) fn csharp_declared_types(contents: &str) -> Vec<String> {`
  - Purpose: Extracts all declared C# type identifiers (classes, interfaces, enums, records, and structs) from the provided source code string and returns them as a vector. [crates/gcode/src/index/import_resolution/predicates.rs:83-88]
- `declared_types` (function) component `declared_types [function]` (`c4799ccd-275b-599c-9f4d-dadc9b681fb5`) lines 94-107 [crates/gcode/src/index/import_resolution/predicates.rs:94-107]
  - Signature: `pub(super) fn declared_types(contents: &str, keywords: &[&str]) -> Vec<String> {`
  - Purpose: Extracts and returns identifiers that immediately follow occurrences of specified keywords in source code after removing comments and string literals. [crates/gcode/src/index/import_resolution/predicates.rs:94-107]
- `strip_comments_and_string_literals` (function) component `strip_comments_and_string_literals [function]` (`6e2c4a70-1c80-5eca-ab8a-56e9c94e6dab`) lines 109-179 [crates/gcode/src/index/import_resolution/predicates.rs:109-179]
  - Signature: `fn strip_comments_and_string_literals(contents: &str) -> String {`
  - Purpose: Removes single-line (`//`) and multi-line (`/* */`) comments and string literals (quoted with `"`, `'`, or `` ` ``) from source code by replacing them with spaces while preserving newlines and character positions. [crates/gcode/src/index/import_resolution/predicates.rs:109-179]
- `php_declared_symbols` (function) component `php_declared_symbols [function]` (`6c0ea49d-bd2c-51c6-96cc-0dd4ebe026ae`) lines 185-201 [crates/gcode/src/index/import_resolution/predicates.rs:185-201]
  - Signature: `pub(super) fn php_declared_symbols(contents: &str) -> Vec<String> {`
  - Purpose: Extracts declared PHP symbol names by identifying identifiers that immediately follow class, interface, trait, enum, or function keywords in tokenized, comment-stripped source code. [crates/gcode/src/index/import_resolution/predicates.rs:185-201]
- `is_external_java_class` (function) component `is_external_java_class [function]` (`99b6bbce-7221-5f71-8963-9dd01758aa13`) lines 203-210 [crates/gcode/src/index/import_resolution/predicates.rs:203-210]
  - Signature: `pub(super) fn is_external_java_class(`
  - Purpose: Determines whether a class path represents an external Java class by verifying that none of its derived class name candidates exist in the import context's local classes set. [crates/gcode/src/index/import_resolution/predicates.rs:203-210]
- `java_class_name_candidates` (function) component `java_class_name_candidates [function]` (`123db214-0e01-5bce-8144-449c656c5774`) lines 212-220 [crates/gcode/src/index/import_resolution/predicates.rs:212-220]
  - Signature: `fn java_class_name_candidates(class_path: &str) -> impl Iterator<Item = &str> {`
  - Purpose: Returns an iterator yielding three candidate Java class name strings extracted from a qualified class path: the full path, the simple name (after the rightmost dot), and the outer class name (before the first dollar sign indicating inner classes). [crates/gcode/src/index/import_resolution/predicates.rs:212-220]
- `is_external_csharp_path` (function) component `is_external_csharp_path [function]` (`b2c7ec54-187d-5f46-b143-782a3d5ca89a`) lines 222-231 [crates/gcode/src/index/import_resolution/predicates.rs:222-231]
  - Signature: `pub(super) fn is_external_csharp_path(`
  - Purpose: Determines if a C# path is external by verifying that its root namespace (following optional `global::` prefix) is not present in the ImportResolutionContext's local roots collection. [crates/gcode/src/index/import_resolution/predicates.rs:222-231]
- `is_external_php_symbol` (function) component `is_external_php_symbol [function]` (`c33bb23c-e5dc-5404-8622-17a2208734f5`) lines 233-241 [crates/gcode/src/index/import_resolution/predicates.rs:233-241]
  - Signature: `pub(super) fn is_external_php_symbol(path: &str, import_context: &ImportResolutionContext) -> bool {`
  - Purpose: Determines whether a PHP symbol is external by confirming that neither its fully-qualified path nor its simple name (after the final backslash separator) exists in the local symbols set. [crates/gcode/src/index/import_resolution/predicates.rs:233-241]
- `is_external_rust_root` (function) component `is_external_rust_root [function]` (`51404e43-9190-5595-8d38-40cedb7ec16e`) lines 243-251 [crates/gcode/src/index/import_resolution/predicates.rs:243-251]
  - Signature: `pub(super) fn is_external_rust_root(root: &str, import_context: &ImportResolutionContext) -> bool {`
  - Purpose: Identifies whether a root identifier references an external Rust crate by excluding relative module keywords ("crate", "self", "super"), the current crate name, and checking against external and standard crate registries. [crates/gcode/src/index/import_resolution/predicates.rs:243-251]
- `ruby_require_root` (function) component `ruby_require_root [function]` (`e833a0ae-52f6-58ab-b0bc-d6b283957351`) lines 258-262 [crates/gcode/src/index/import_resolution/predicates.rs:258-262]
  - Signature: `pub(super) fn ruby_require_root(required: &str) -> Option<&'static str> {`
  - Purpose: This function retrieves a static string reference from an internal mapping of bundled Ruby require roots by key, returning `None` if the key is not found. [crates/gcode/src/index/import_resolution/predicates.rs:258-262]
- `is_external_dart_uri` (function) component `is_external_dart_uri [function]` (`db874d10-b95c-5912-be49-f94fb150216e`) lines 264-276 [crates/gcode/src/index/import_resolution/predicates.rs:264-276]
  - Signature: `pub(super) fn is_external_dart_uri(uri: &str, import_context: &ImportResolutionContext) -> bool {`
  - Purpose: Determines whether a URI references an external Dart dependency by identifying `dart:` standard library imports or `package:` imports that are registered as external packages and differ from the current package. [crates/gcode/src/index/import_resolution/predicates.rs:264-276]
- `elixir_dependency_roots` (function) component `elixir_dependency_roots [function]` (`478268b0-31a0-52da-8f3d-eeac9f9cdd6c`) lines 284-288 [crates/gcode/src/index/import_resolution/predicates.rs:284-288]
  - Signature: `pub(super) fn elixir_dependency_roots(dep: &str) -> Option<&'static [String]> {`
  - Purpose: Returns a static slice of root path strings for a given Elixir dependency from a bundled collection, or None if the dependency is not found. [crates/gcode/src/index/import_resolution/predicates.rs:284-288]
- `bundled_ruby_require_roots` (function) component `bundled_ruby_require_roots [function]` (`8c11cbd1-1bfe-5a02-ad63-8d6b216ddd2e`) lines 290-302 [crates/gcode/src/index/import_resolution/predicates.rs:290-302]
  - Signature: `pub(super) fn bundled_ruby_require_roots() -> &'static HashMap<String, String> {`
  - Purpose: Returns a static reference to a lazily-initialized `HashMap<String, String>` of Ruby require root mappings deserialized from an embedded JSON asset file. [crates/gcode/src/index/import_resolution/predicates.rs:290-302]
- `bundled_elixir_dependency_roots` (function) component `bundled_elixir_dependency_roots [function]` (`543980d7-b8a9-598c-8a0a-d384b1a0c564`) lines 304-316 [crates/gcode/src/index/import_resolution/predicates.rs:304-316]
  - Signature: `pub(super) fn bundled_elixir_dependency_roots() -> &'static HashMap<String, Vec<String>> {`
  - Purpose: Returns a static reference to a lazily-initialized HashMap mapping Elixir dependency names to their root import paths, deserialized from a bundled JSON asset file. [crates/gcode/src/index/import_resolution/predicates.rs:304-316]
- `js_package_name` (function) component `js_package_name [function]` (`5752de2e-6213-5500-9719-fc467a640117`) lines 318-328 [crates/gcode/src/index/import_resolution/predicates.rs:318-328]
  - Signature: `pub(super) fn js_package_name(module: &str) -> Option<&str> {`
  - Purpose: Extracts the JavaScript package name from a module path, including the `@scope/` prefix for scoped packages or the first path segment for unscoped packages. [crates/gcode/src/index/import_resolution/predicates.rs:318-328]

