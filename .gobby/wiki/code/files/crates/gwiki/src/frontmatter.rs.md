---
title: crates/gwiki/src/frontmatter.rs
type: code_file
provenance:
- file: crates/gwiki/src/frontmatter.rs
  ranges:
  - 10-13
  - 16-30
  - 32-115
  - 33-48
  - 50-114
  - 118-124
  - 127-129
  - 131-135
  - 132-134
  - '137'
  - 139-169
  - 171-189
  - 191-197
  - 192-196
  - 199-203
  - 205-219
  - 221-230
  - 232-262
  - 264-284
  - 286-300
  - 302-310
  - 312-325
  - 327-340
  - 342-388
  - 390-392
  - 394-400
  - 402-409
  - 413-428
  - 430-444
  - 451-518
  - 521-540
  - 543-572
  - 575-605
  - 608-637
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/frontmatter.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/frontmatter.rs` exposes 34 indexed API symbols.
[crates/gwiki/src/frontmatter.rs:10-13]
[crates/gwiki/src/frontmatter.rs:16-30]
[crates/gwiki/src/frontmatter.rs:32-115]
[crates/gwiki/src/frontmatter.rs:33-48]
[crates/gwiki/src/frontmatter.rs:50-114]

## API Symbols

- `FrontmatterFormat` (type) component `FrontmatterFormat [type]` (`7d7d2878-4616-50b7-b364-5d25d085c2ff`) lines 10-13 [crates/gwiki/src/frontmatter.rs:10-13]
  - Signature: `pub enum FrontmatterFormat {`
  - Purpose: Indexed type `FrontmatterFormat` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:10-13]
- `WikiFrontmatter` (class) component `WikiFrontmatter [class]` (`862372eb-ec1d-56e0-9087-7b29b27353b9`) lines 16-30 [crates/gwiki/src/frontmatter.rs:16-30]
  - Signature: `pub struct WikiFrontmatter {`
  - Purpose: WikiFrontmatter is a struct representing wiki document metadata with optional fields for title, source attribution, provenance, trust/freshness indicators, and a BTreeMap to preserve unrecognized/legacy frontmatter keys for extensibility. [crates/gwiki/src/frontmatter.rs:16-30]
- `WikiFrontmatter` (class) component `WikiFrontmatter [class]` (`23ca6438-a0eb-5b47-93a0-09260ef6a965`) lines 32-115 [crates/gwiki/src/frontmatter.rs:32-115]
  - Signature: `impl WikiFrontmatter {`
  - Purpose: # Summary

`WikiFrontmatter` implementation provides factory construction and JSON serialization methods for a metadata structure that stores optional document properties (title, aliases, tags, source provenance, etc.) and unknown arbitrary fields. [crates/gwiki/src/frontmatter.rs:32-115]
- `WikiFrontmatter.empty` (method) component `WikiFrontmatter.empty [method]` (`cfca94a5-346a-517d-97f5-45935c604b86`) lines 33-48 [crates/gwiki/src/frontmatter.rs:33-48]
  - Signature: `pub fn empty() -> Self {`
  - Purpose: Creates a new instance with all optional fields set to `None` and collection fields initialized to empty. [crates/gwiki/src/frontmatter.rs:33-48]
- `WikiFrontmatter.as_json` (method) component `WikiFrontmatter.as_json [method]` (`c2fa0519-10cb-5740-aaeb-d99ceabf2f2f`) lines 50-114 [crates/gwiki/src/frontmatter.rs:50-114]
  - Signature: `pub fn as_json(&self) -> Value {`
  - Purpose: # Summary

Converts the struct instance to a JSON `Value` object by merging all preserved unknown fields with conditionally-inserted optional metadata fields (title, aliases, tags, source_kind, captured_from, source, provenance, generated_by, trust, and others). [crates/gwiki/src/frontmatter.rs:50-114]
- `ParsedFrontmatter` (class) component `ParsedFrontmatter [class]` (`a16841af-047d-57ae-b5b8-46e3d0f1afb0`) lines 118-124 [crates/gwiki/src/frontmatter.rs:118-124]
  - Signature: `pub struct ParsedFrontmatter<'a> {`
  - Purpose: `ParsedFrontmatter` is a borrowed-lifetime struct that encapsulates parsed frontmatter with its optional format and source range, body start offset, body content slice, and extracted metadata. [crates/gwiki/src/frontmatter.rs:118-124]
- `FrontmatterError` (class) component `FrontmatterError [class]` (`8cbc77b1-2afd-52ee-8479-dfe3371b9584`) lines 127-129 [crates/gwiki/src/frontmatter.rs:127-129]
  - Signature: `pub struct FrontmatterError {`
  - Purpose: `FrontmatterError` is a custom error type that encapsulates frontmatter parsing or processing failures with a string-based detail message. [crates/gwiki/src/frontmatter.rs:127-129]
- `FrontmatterError` (class) component `FrontmatterError [class]` (`a8667634-c897-51a5-b84a-3b01a56fb2c3`) lines 131-135 [crates/gwiki/src/frontmatter.rs:131-135]
  - Signature: `impl fmt::Display for FrontmatterError {`
  - Purpose: Implements the `fmt::Display` trait for `FrontmatterError`, enabling string representation by delegating to its `detail` field. [crates/gwiki/src/frontmatter.rs:131-135]
- `FrontmatterError.fmt` (method) component `FrontmatterError.fmt [method]` (`e054f9c1-d277-51d8-889d-791ec65e5b90`) lines 132-134 [crates/gwiki/src/frontmatter.rs:132-134]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: This method implements the `Display` trait to format the struct by writing its `detail` field to the provided `Formatter`. [crates/gwiki/src/frontmatter.rs:132-134]
- `FrontmatterError` (class) component `FrontmatterError [class]` (`735815a8-31a0-5b8b-a9f6-8ac9dd68f8c4`) lines 137-137 [crates/gwiki/src/frontmatter.rs:137]
  - Signature: `impl std::error::Error for FrontmatterError {}`
  - Purpose: FrontmatterError implements the `std::error::Error` trait to enable it as a standard error type in Rust's error handling infrastructure. [crates/gwiki/src/frontmatter.rs:137]
- `parse_frontmatter` (function) component `parse_frontmatter [function]` (`798ccde8-ecb7-5b29-b654-00cdb939a3ed`) lines 139-169 [crates/gwiki/src/frontmatter.rs:139-169]
  - Signature: `pub fn parse_frontmatter(markdown: &str) -> Result<ParsedFrontmatter<'_>, FrontmatterError> {`
  - Purpose: Parses frontmatter metadata from a markdown string by locating and extracting delimited blocks, then returns the parsed metadata along with the remaining body content, or an error if delimiters are unmatched. [crates/gwiki/src/frontmatter.rs:139-169]
- `mark_stale_markdown` (function) component `mark_stale_markdown [function]` (`2cbe7774-2850-5c8a-a1ef-a68bc4c694e0`) lines 171-189 [crates/gwiki/src/frontmatter.rs:171-189]
  - Signature: `pub fn mark_stale_markdown(markdown: &str, reason: &str) -> Result<String, FrontmatterError> {`
  - Purpose: Parses markdown frontmatter, injects a `stale` boolean flag and `stale_reason` string into its metadata, serializes the metadata back to its original format (YAML or TOML), and returns the reconstructed markdown document. [crates/gwiki/src/frontmatter.rs:171-189]
- `FrontmatterError` (class) component `FrontmatterError [class]` (`fc81c73c-b3d1-5557-a2cd-0499bcc7d0cc`) lines 191-197 [crates/gwiki/src/frontmatter.rs:191-197]
  - Signature: `impl FrontmatterError {`
  - Purpose: A constructor method that instantiates `FrontmatterError` by converting a generic type implementing `Into<String>` into its `detail` field. [crates/gwiki/src/frontmatter.rs:191-197]
- `FrontmatterError.new` (method) component `FrontmatterError.new [method]` (`a4c5832d-124e-5286-a936-e2729f3dd05b`) lines 192-196 [crates/gwiki/src/frontmatter.rs:192-196]
  - Signature: `fn new(detail: impl Into<String>) -> Self {`
  - Purpose: Creates a new instance by accepting any type implementing `Into<String>` and initializing the `detail` field with the converted value. [crates/gwiki/src/frontmatter.rs:192-196]
- `OpeningDelimiter` (class) component `OpeningDelimiter [class]` (`586a186e-3254-5a62-b3f4-e1b9686b4080`) lines 199-203 [crates/gwiki/src/frontmatter.rs:199-203]
  - Signature: `struct OpeningDelimiter {`
  - Purpose: OpeningDelimiter is a struct that encodes the frontmatter format type, delimiter marker string, and the byte offset where content begins following the opening delimiter. [crates/gwiki/src/frontmatter.rs:199-203]
- `opening_delimiter` (function) component `opening_delimiter [function]` (`8654b39c-4fc1-5e2c-9444-e0e76080f811`) lines 205-219 [crates/gwiki/src/frontmatter.rs:205-219]
  - Signature: `fn opening_delimiter(markdown: &str) -> Option<OpeningDelimiter> {`
  - Purpose: Identifies and returns the opening frontmatter delimiter from a markdown string, returning an `OpeningDelimiter` with either YAML ("---") or TOML ("+++") format, or `None` if neither is found. [crates/gwiki/src/frontmatter.rs:205-219]
- `delimiter_content_start` (function) component `delimiter_content_start [function]` (`65d38dfd-8890-5161-ab3c-fa6a4d4b6f0b`) lines 221-230 [crates/gwiki/src/frontmatter.rs:221-230]
  - Signature: `fn delimiter_content_start(markdown: &str, marker: &str) -> Option<usize> {`
  - Purpose: Returns the byte offset immediately after a delimiter marker in markdown if followed by a line ending (CRLF or LF), or None if the marker lacks a valid line terminator. [crates/gwiki/src/frontmatter.rs:221-230]
- `find_closing_delimiter` (function) component `find_closing_delimiter [function]` (`7689b51b-1048-5b40-bc0d-ecde0d14e7d5`) lines 232-262 [crates/gwiki/src/frontmatter.rs:232-262]
  - Signature: `fn find_closing_delimiter(`
  - Purpose: Searches a markdown string starting from a given offset for a line containing only the marker string (when trimmed), returning the marker's position and the start of the following content if found, or None otherwise. [crates/gwiki/src/frontmatter.rs:232-262]
- `parse_metadata` (function) component `parse_metadata [function]` (`80652ef4-fc46-53e1-a2a6-7aa9f7edb633`) lines 264-284 [crates/gwiki/src/frontmatter.rs:264-284]
  - Signature: `fn parse_metadata(`
  - Purpose: Parses YAML or TOML formatted frontmatter into a WikiFrontmatter object, validating that the parsed root value is a table/object or null. [crates/gwiki/src/frontmatter.rs:264-284]
- `serialize_yaml_frontmatter` (function) component `serialize_yaml_frontmatter [function]` (`14dea53f-c250-5940-b3ee-7efd4994acaa`) lines 286-300 [crates/gwiki/src/frontmatter.rs:286-300]
  - Signature: `fn serialize_yaml_frontmatter(metadata: &WikiFrontmatter) -> Result<String, FrontmatterError> {`
  - Purpose: Converts a `WikiFrontmatter` struct to YAML format, removing document delimiters (`---` prefix and `...` suffix) and ensuring the output ends with a newline. [crates/gwiki/src/frontmatter.rs:286-300]
- `serialize_toml_frontmatter` (function) component `serialize_toml_frontmatter [function]` (`202bd631-d36c-5760-9205-a7d5f55bae23`) lines 302-310 [crates/gwiki/src/frontmatter.rs:302-310]
  - Signature: `fn serialize_toml_frontmatter(metadata: &WikiFrontmatter) -> Result<String, FrontmatterError> {`
  - Purpose: Serializes a `WikiFrontmatter` struct to a TOML-formatted `String` with a mandatory trailing newline, mapping serialization errors to `FrontmatterError`. [crates/gwiki/src/frontmatter.rs:302-310]
- `parse_yaml` (function) component `parse_yaml [function]` (`35ef6c28-3382-5d1e-8181-3c8f54d2154b`) lines 312-325 [crates/gwiki/src/frontmatter.rs:312-325]
  - Signature: `fn parse_yaml(raw: &str) -> Result<Value, FrontmatterError> {`
  - Purpose: Parses a YAML string into a serde_json::Value, returning an empty JSON object for empty input and mapping YAML parsing or JSON conversion errors to FrontmatterError. [crates/gwiki/src/frontmatter.rs:312-325]
- `parse_toml` (function) component `parse_toml [function]` (`a052d7ec-549d-55e5-aeea-6ff1071eafca`) lines 327-340 [crates/gwiki/src/frontmatter.rs:327-340]
  - Signature: `fn parse_toml(raw: &str) -> Result<Value, FrontmatterError> {`
  - Purpose: Parses a TOML frontmatter string into a `serde_json::Value`, returning an empty object for empty input and propagating parse/serialization errors as `FrontmatterError`. [crates/gwiki/src/frontmatter.rs:327-340]
- `frontmatter_from_object` (function) component `frontmatter_from_object [function]` (`24c3afe7-2271-5451-981f-162e69c019e7`) lines 342-388 [crates/gwiki/src/frontmatter.rs:342-388]
  - Signature: `fn frontmatter_from_object(mut object: Map<String, Value>) -> WikiFrontmatter {`
  - Purpose: Deserializes a JSON object map into a typed `WikiFrontmatter` struct by extracting and type-converting specific metadata fields (title, aliases, tags, source_kind, etc.) with default fallbacks for missing values, while collecting unmapped entries into an `unknown` field. [crates/gwiki/src/frontmatter.rs:342-388]
- `string_value` (function) component `string_value [function]` (`09bea6d6-e92b-5d14-908f-4c5e4bca1c47`) lines 390-392 [crates/gwiki/src/frontmatter.rs:390-392]
  - Signature: `fn string_value(value: &Value) -> Option<String> {`
  - Purpose: Extracts an optional `String` from a `Value` by converting it to a string reference and chaining it through the `string_value_str` function using `and_then`. [crates/gwiki/src/frontmatter.rs:390-392]
- `string_list` (function) component `string_list [function]` (`e2004dbb-c0b2-5b6a-a749-9c4520283f3a`) lines 394-400 [crates/gwiki/src/frontmatter.rs:394-400]
  - Signature: `fn string_list(value: &Value) -> Vec<String> {`
  - Purpose: Converts a `Value` enum to a `Vec<String>` by extracting strings from `String` variants directly or filter-mapping `Array` elements through the `string_value` function, returning an empty vector for other types. [crates/gwiki/src/frontmatter.rs:394-400]
- `string_value_str` (function) component `string_value_str [function]` (`fa063a16-969b-50a0-b36d-654116f40ed1`) lines 402-409 [crates/gwiki/src/frontmatter.rs:402-409]
  - Signature: `fn string_value_str(value: &str) -> Option<String> {`
  - Purpose: Returns an `Option<String>` containing the trimmed input string if non-empty, or `None` if empty after trimming. [crates/gwiki/src/frontmatter.rs:402-409]
- `tag_list` (function) component `tag_list [function]` (`51b4a09a-7a85-5909-8481-bfe0837e11c3`) lines 413-428 [crates/gwiki/src/frontmatter.rs:413-428]
  - Signature: `fn tag_list(value: &Value) -> Vec<String> {`
  - Purpose: Converts a `Value` into a normalized `Vec<String>` of tags by splitting comma/whitespace-delimited strings or parsing array elements, with leading `#` characters and empty entries removed. [crates/gwiki/src/frontmatter.rs:413-428]
- `parse_source_kind` (function) component `parse_source_kind [function]` (`38e2faf6-af9c-538f-9689-43d1cefbc277`) lines 430-444 [crates/gwiki/src/frontmatter.rs:430-444]
  - Signature: `fn parse_source_kind(value: &str) -> Option<WikiSourceKind> {`
  - Purpose: Converts a normalized string (trimmed, lowercased, with hyphens and spaces replaced by underscores) into a corresponding `WikiSourceKind` enum variant, or returns `None` if the input doesn't match any recognized variant. [crates/gwiki/src/frontmatter.rs:430-444]
- `preserves_unknown_frontmatter` (function) component `preserves_unknown_frontmatter [function]` (`f1940e4a-de16-59b9-b1e6-732c09adff9c`) lines 451-518 [crates/gwiki/src/frontmatter.rs:451-518]
  - Signature: `fn preserves_unknown_frontmatter() {`
  - Purpose: Unit test verifying that `parse_frontmatter()` correctly extracts known metadata fields while preserving unrecognized fields in an `unknown` map for both YAML and TOML frontmatter formats. [crates/gwiki/src/frontmatter.rs:451-518]
- `legacy_source_files_remain_unknown_metadata` (function) component `legacy_source_files_remain_unknown_metadata [function]` (`e0f37fe1-d9bf-53e0-867e-bacb65979bde`) lines 521-540 [crates/gwiki/src/frontmatter.rs:521-540]
  - Signature: `fn legacy_source_files_remain_unknown_metadata() {`
  - Purpose: This test verifies that a `source_files` field in frontmatter is categorized as unknown metadata rather than being parsed into the recognized `source` or `provenance` metadata fields. [crates/gwiki/src/frontmatter.rs:521-540]
- `frontmatter_migration_parses_shared_contract_keys` (function) component `frontmatter_migration_parses_shared_contract_keys [function]` (`c146b671-51c9-5cd5-8ccc-da0904e186db`) lines 543-572 [crates/gwiki/src/frontmatter.rs:543-572]
  - Signature: `fn frontmatter_migration_parses_shared_contract_keys() {`
  - Purpose: Tests that the frontmatter parser correctly parses shared contract metadata keys (source, provenance, generated_by, trust, freshness) into their designated typed fields while excluding them from the unknown fields collection. [crates/gwiki/src/frontmatter.rs:543-572]
- `change_triggered_refresh_marks_page_stale_with_reason` (function) component `change_triggered_refresh_marks_page_stale_with_reason [function]` (`81b5a9ee-4f68-5ab1-abd6-06cda4f92418`) lines 575-605 [crates/gwiki/src/frontmatter.rs:575-605]
  - Signature: `fn change_triggered_refresh_marks_page_stale_with_reason() {`
  - Purpose: Tests that `mark_stale_markdown()` correctly adds `stale: true` and `stale_reason` metadata fields to markdown frontmatter when provided with a change reason. [crates/gwiki/src/frontmatter.rs:575-605]
- `change_triggered_refresh_preserves_toml_frontmatter` (function) component `change_triggered_refresh_preserves_toml_frontmatter [function]` (`7bf58d00-1dd8-5b47-a541-3ad72921d8c6`) lines 608-637 [crates/gwiki/src/frontmatter.rs:608-637]
  - Signature: `fn change_triggered_refresh_preserves_toml_frontmatter() {`
  - Purpose: This test verifies that `mark_stale_markdown` preserves TOML frontmatter structure and existing metadata fields while injecting stale status information in response to a source file change. [crates/gwiki/src/frontmatter.rs:608-637]

