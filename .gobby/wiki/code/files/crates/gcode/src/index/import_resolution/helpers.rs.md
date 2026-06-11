---
title: crates/gcode/src/index/import_resolution/helpers.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/helpers.rs
  ranges:
  - 1-3
  - 5-11
  - 13-17
  - 19-47
  - 49-86
  - 88-97
  - 99-105
  - 107-134
  - 136-164
  - 167-172
  - 174-182
  - 175-181
  - '184'
  - 186-195
  - 187-194
  - 197-212
  - 214-303
  - 305-307
  - 309-316
  - 318-330
  - 332-334
  - 336-338
  - 340-352
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/helpers.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

`crates/gcode/src/index/import_resolution/helpers.rs` exposes 23 indexed API symbols.
[crates/gcode/src/index/import_resolution/helpers.rs:1-3]
[crates/gcode/src/index/import_resolution/helpers.rs:5-11]
[crates/gcode/src/index/import_resolution/helpers.rs:13-17]
[crates/gcode/src/index/import_resolution/helpers.rs:19-47]
[crates/gcode/src/index/import_resolution/helpers.rs:49-86]

## API Symbols

- `collapse_whitespace` (function) component `collapse_whitespace [function]` (`a4c2ee4b-65fd-51c9-8c66-d768b267e4a0`) lines 1-3 [crates/gcode/src/index/import_resolution/helpers.rs:1-3]
  - Signature: `pub(super) fn collapse_whitespace(text: &str) -> String {`
  - Purpose: Collapses all consecutive whitespace sequences into single spaces by splitting on whitespace boundaries and rejoining with space delimiters. [crates/gcode/src/index/import_resolution/helpers.rs:1-3]
- `extract_js_module_specifier` (function) component `extract_js_module_specifier [function]` (`437c13ac-dca4-5091-9085-e26c94422ce8`) lines 5-11 [crates/gcode/src/index/import_resolution/helpers.rs:5-11]
  - Signature: `pub(super) fn extract_js_module_specifier(text: &str) -> Option<String> {`
  - Purpose: Extracts a quoted module specifier string from JavaScript import statements by parsing the substring following either a ' from ' keyword (right-split) or the 'import ' prefix. [crates/gcode/src/index/import_resolution/helpers.rs:5-11]
- `extract_js_import_clause` (function) component `extract_js_import_clause [function]` (`634bbbde-7bc3-56c9-b682-ad6dd5427803`) lines 13-17 [crates/gcode/src/index/import_resolution/helpers.rs:13-17]
  - Signature: `pub(super) fn extract_js_import_clause(text: &str) -> Option<&str> {`
  - Purpose: Extracts the import specifier clause from a JavaScript import statement by removing the "import " prefix and splitting at the rightmost " from " delimiter, returning None if either operation fails. [crates/gcode/src/index/import_resolution/helpers.rs:13-17]
- `extract_quoted_string` (function) component `extract_quoted_string [function]` (`8fa24ae8-c68a-5743-863d-d43aa8f63f29`) lines 19-47 [crates/gcode/src/index/import_resolution/helpers.rs:19-47]
  - Signature: `pub(super) fn extract_quoted_string(text: &str) -> Option<String> {`
  - Purpose: Extracts and returns the unquoted content of the first quoted string in the input, handling escape sequences and backtick template variable interpolation (${...}). [crates/gcode/src/index/import_resolution/helpers.rs:19-47]
- `skip_template_interpolation` (function) component `skip_template_interpolation [function]` (`05e1ba4b-7a24-5803-9402-9dd07845d243`) lines 49-86 [crates/gcode/src/index/import_resolution/helpers.rs:49-86]
  - Signature: `fn skip_template_interpolation(text: &str, mut idx: usize) -> Option<usize> {`
  - Purpose: Finds the byte position immediately after the closing brace that matches an opening brace at the given index, while excluding braces within string literals and respecting escape sequences. [crates/gcode/src/index/import_resolution/helpers.rs:49-86]
- `go_default_package_alias` (function) component `go_default_package_alias [function]` (`022febc3-6f22-5f26-9403-1b53a66466d1`) lines 88-97 [crates/gcode/src/index/import_resolution/helpers.rs:88-97]
  - Signature: `pub(super) fn go_default_package_alias(module: &str) -> String {`
  - Purpose: Generates a Go package alias from a module path by extracting the final segment, stripping semantic version suffixes (`.vN`), and replacing hyphens with underscores. [crates/gcode/src/index/import_resolution/helpers.rs:88-97]
- `split_alias` (function) component `split_alias [function]` (`a20aece7-d14b-51d5-90a0-0c4824050740`) lines 99-105 [crates/gcode/src/index/import_resolution/helpers.rs:99-105]
  - Signature: `pub(super) fn split_alias(text: &str) -> (&str, Option<&str>) {`
  - Purpose: Parses a name and optional alias from a string separated by " as ", returning the name and alias as trimmed string slices. [crates/gcode/src/index/import_resolution/helpers.rs:99-105]
- `split_rust_use_group` (function) component `split_rust_use_group [function]` (`43652486-e9ef-57cc-abd5-b5e489b0618c`) lines 107-134 [crates/gcode/src/index/import_resolution/helpers.rs:107-134]
  - Signature: `pub(super) fn split_rust_use_group(text: &str) -> Option<(&str, &str)> {`
  - Purpose: Splits a string at a balanced top-level brace pair, returning the trimmed prefix and body only if no non-whitespace content follows the closing brace. [crates/gcode/src/index/import_resolution/helpers.rs:107-134]
- `rust_join_use_path` (function) component `rust_join_use_path [function]` (`42af5f2c-a5fa-5f91-94ff-c8550303c22e`) lines 136-164 [crates/gcode/src/index/import_resolution/helpers.rs:136-164]
  - Signature: `pub(super) fn rust_join_use_path(prefix: &str, item: &str) -> Option<String> {`
  - Purpose: Joins a namespace prefix with a Rust use item, handling the special `self` reference and preserving optional aliases in the format `path as alias`, returning `None` for invalid inputs. [crates/gcode/src/index/import_resolution/helpers.rs:136-164]
- `SplitTopLevelError` (class) component `SplitTopLevelError [class]` (`17a0206d-acd4-5707-b678-831791ccb76f`) lines 167-172 [crates/gcode/src/index/import_resolution/helpers.rs:167-172]
  - Signature: `pub(super) struct SplitTopLevelError {`
  - Purpose: `SplitTopLevelError` is an error struct that captures parsing failures when splitting top-level constructs by a delimiter, containing the problematic delimiter character, its position, error type classification, and contextual information. [crates/gcode/src/index/import_resolution/helpers.rs:167-172]
- `SplitTopLevelError` (class) component `SplitTopLevelError [class]` (`3fd8c6a7-ac3d-56d2-b3cd-a74f7e7d0c22`) lines 174-182 [crates/gcode/src/index/import_resolution/helpers.rs:174-182]
  - Signature: `impl std::fmt::Display for SplitTopLevelError {`
  - Purpose: Implements the `Display` trait for `SplitTopLevelError` to format an error message containing the failure kind, delimiter, byte position, and surrounding context. [crates/gcode/src/index/import_resolution/helpers.rs:174-182]
- `SplitTopLevelError.fmt` (method) component `SplitTopLevelError.fmt [method]` (`f8548d08-2736-5c7b-b989-d2b3eaa4db17`) lines 175-181 [crates/gcode/src/index/import_resolution/helpers.rs:175-181]
  - Signature: `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
  - Purpose: Implements the `Display` trait's `fmt` method to write a formatted error message containing the error kind, delimiter character, byte position, and surrounding context of a split operation failure. [crates/gcode/src/index/import_resolution/helpers.rs:175-181]
- `SplitTopLevelError` (class) component `SplitTopLevelError [class]` (`6e952616-a9b0-5d9f-9e69-418f7b9cf2de`) lines 184-184 [crates/gcode/src/index/import_resolution/helpers.rs:184]
  - Signature: `impl std::error::Error for SplitTopLevelError {}`
  - Purpose: SplitTopLevelError implements the `std::error::Error` trait, making it a valid Rust error type that can be propagated and handled in standard error contexts. [crates/gcode/src/index/import_resolution/helpers.rs:184]
- `SplitTopLevelError` (class) component `SplitTopLevelError [class]` (`0734158f-7eea-527d-bbfe-3fcae4c92be7`) lines 186-195 [crates/gcode/src/index/import_resolution/helpers.rs:186-195]
  - Signature: `impl SplitTopLevelError {`
  - Purpose: `SplitTopLevelError::new` is a constructor that instantiates the error type with a delimiter character, error position, error kind, and contextual information extracted from the source text. [crates/gcode/src/index/import_resolution/helpers.rs:186-195]
- `SplitTopLevelError.new` (method) component `SplitTopLevelError.new [method]` (`745f167d-b99d-5f7e-8283-06aa2aebf242`) lines 187-194 [crates/gcode/src/index/import_resolution/helpers.rs:187-194]
  - Signature: `fn new(text: &str, delimiter: char, position: usize, kind: &'static str) -> Self {`
  - Purpose: Initializes a new instance with the supplied delimiter, position, and kind, while extracting contextual information from the input text at the specified position via `split_error_context`. [crates/gcode/src/index/import_resolution/helpers.rs:187-194]
- `split_error_context` (function) component `split_error_context [function]` (`bf446b9c-cded-5cc5-b70c-0e878b1494d1`) lines 197-212 [crates/gcode/src/index/import_resolution/helpers.rs:197-212]
  - Signature: `fn split_error_context(text: &str, position: usize) -> String {`
  - Purpose: Extracts a context window of up to 24 Unicode characters before and after a given error position, returning the substring with newlines escaped as literal `\n`. [crates/gcode/src/index/import_resolution/helpers.rs:197-212]
- `split_top_level` (function) component `split_top_level [function]` (`1d87edf1-aab1-5e72-a7ae-fb20b5490da2`) lines 214-303 [crates/gcode/src/index/import_resolution/helpers.rs:214-303]
  - Signature: `pub(super) fn split_top_level(`
  - Purpose: Splits a string at a delimiter character only at top-level positions (outside nested parentheses, braces, brackets, and quoted strings) while validating balanced delimiters. [crates/gcode/src/index/import_resolution/helpers.rs:214-303]
- `is_ruby_constant_name` (function) component `is_ruby_constant_name [function]` (`f201e538-e01b-59ec-ae7c-78109ca78f43`) lines 305-307 [crates/gcode/src/index/import_resolution/helpers.rs:305-307]
  - Signature: `pub(super) fn is_ruby_constant_name(name: &str) -> bool {`
  - Purpose: This function validates whether a string conforms to Ruby constant naming conventions by checking if it contains only uppercase ASCII alphanumeric characters and underscores. [crates/gcode/src/index/import_resolution/helpers.rs:305-307]
- `is_uppercase_ascii_alnum_underscore_name` (function) component `is_uppercase_ascii_alnum_underscore_name [function]` (`fc9f79bc-ed88-5926-b897-e76e0c08081d`) lines 309-316 [crates/gcode/src/index/import_resolution/helpers.rs:309-316]
  - Signature: `fn is_uppercase_ascii_alnum_underscore_name(name: &str) -> bool {`
  - Purpose: Returns `true` if the input string begins with an uppercase ASCII letter and contains only ASCII alphanumeric characters or underscores. [crates/gcode/src/index/import_resolution/helpers.rs:309-316]
- `dart_import_alias` (function) component `dart_import_alias [function]` (`f550cc37-008b-5fb3-a35e-37559d5ca490`) lines 318-330 [crates/gcode/src/index/import_resolution/helpers.rs:318-330]
  - Signature: `pub(super) fn dart_import_alias(text: &str) -> Option<String> {`
  - Purpose: Extracts the alias identifier from a Dart import statement by parsing the text after the " as " keyword, trimming whitespace and trailing semicolons, and returning `None` if no alias is present. [crates/gcode/src/index/import_resolution/helpers.rs:318-330]
- `is_elixir_alias` (function) component `is_elixir_alias [function]` (`1458f6f6-a1e9-50b3-92b7-ff0e333b20d0`) lines 332-334 [crates/gcode/src/index/import_resolution/helpers.rs:332-334]
  - Signature: `pub(super) fn is_elixir_alias(name: &str) -> bool {`
  - Purpose: Determines whether a string is a valid Elixir alias by verifying it contains only uppercase ASCII alphanumeric characters and underscores. [crates/gcode/src/index/import_resolution/helpers.rs:332-334]
- `is_elixir_alias_path` (function) component `is_elixir_alias_path [function]` (`a4479e3d-fc7f-5c19-8df0-c3c3a9b81d5a`) lines 336-338 [crates/gcode/src/index/import_resolution/helpers.rs:336-338]
  - Signature: `pub(super) fn is_elixir_alias_path(path: &str) -> bool {`
  - Purpose: Returns true if and only if every dot-separated segment of the input path is a valid Elixir alias. [crates/gcode/src/index/import_resolution/helpers.rs:336-338]
- `elixir_alias_as` (function) component `elixir_alias_as [function]` (`298a796f-3b71-57de-91e3-92ee6f7bd0f2`) lines 340-352 [crates/gcode/src/index/import_resolution/helpers.rs:340-352]
  - Signature: `pub(super) fn elixir_alias_as(text: &str) -> Option<String> {`
  - Purpose: Extracts and validates the Elixir alias name immediately following the `" as: "` delimiter, returning `Some(String)` if the extracted token is a valid Elixir alias, or `None` if not found or invalid. [crates/gcode/src/index/import_resolution/helpers.rs:340-352]

