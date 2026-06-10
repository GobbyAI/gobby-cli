---
title: crates/gcode/src/graph/typed_query.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/typed_query.rs
  ranges:
  - 7-10
  - 13-21
  - 24-27
  - 30-38
  - 40-71
  - 41-46
  - 48-58
  - 60-70
  - 73-75
  - 77-98
  - 100-105
  - 107-109
  - 111-113
  - 115-120
  - 122-141
  - 143-145
  - 147-164
  - 166-178
  - 180-187
  - 181-186
  - 189-201
  - 190-200
  - '203'
  - 211-276
  - 279-284
  - 287-297
  - 300-315
  - 318-341
  - 344-350
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/typed_query.rs

Module: [[code/modules/crates/gcode/src/graph|crates/gcode/src/graph]]

## Purpose

`crates/gcode/src/graph/typed_query.rs` exposes 29 indexed API symbols.
[crates/gcode/src/graph/typed_query.rs:7-10]
[crates/gcode/src/graph/typed_query.rs:13-21]
[crates/gcode/src/graph/typed_query.rs:24-27]
[crates/gcode/src/graph/typed_query.rs:30-38]
[crates/gcode/src/graph/typed_query.rs:40-71]
[crates/gcode/src/graph/typed_query.rs:41-46]
[crates/gcode/src/graph/typed_query.rs:48-58]
[crates/gcode/src/graph/typed_query.rs:60-70]
[crates/gcode/src/graph/typed_query.rs:73-75]
[crates/gcode/src/graph/typed_query.rs:77-98]
[crates/gcode/src/graph/typed_query.rs:100-105]
[crates/gcode/src/graph/typed_query.rs:107-109]
[crates/gcode/src/graph/typed_query.rs:111-113]
[crates/gcode/src/graph/typed_query.rs:115-120]
[crates/gcode/src/graph/typed_query.rs:122-141]
[crates/gcode/src/graph/typed_query.rs:143-145]
[crates/gcode/src/graph/typed_query.rs:147-164]
[crates/gcode/src/graph/typed_query.rs:166-178]
[crates/gcode/src/graph/typed_query.rs:180-187]
[crates/gcode/src/graph/typed_query.rs:181-186]
[crates/gcode/src/graph/typed_query.rs:189-201]
[crates/gcode/src/graph/typed_query.rs:190-200]
[crates/gcode/src/graph/typed_query.rs:203]
[crates/gcode/src/graph/typed_query.rs:211-276]
[crates/gcode/src/graph/typed_query.rs:279-284]
[crates/gcode/src/graph/typed_query.rs:287-297]
[crates/gcode/src/graph/typed_query.rs:300-315]
[crates/gcode/src/graph/typed_query.rs:318-341]
[crates/gcode/src/graph/typed_query.rs:344-350]

## API Symbols

- `TypedQuery` (class) component `TypedQuery [class]` (`253b9b29-dceb-5672-a721-5d54c2418774`) lines 7-10 [crates/gcode/src/graph/typed_query.rs:7-10]
  - Signature: `pub struct TypedQuery {`
  - Purpose: TypedQuery is a struct that encapsulates a Cypher query string along with a HashMap of named string parameters for parameterized query execution. [crates/gcode/src/graph/typed_query.rs:7-10]
- `TypedValue` (type) component `TypedValue [type]` (`b8f78e98-501e-5b25-a52f-a3ae5a455b7d`) lines 13-21 [crates/gcode/src/graph/typed_query.rs:13-21]
  - Signature: `pub enum TypedValue {`
  - Purpose: Indexed type `TypedValue` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:13-21]
- `IdentifierKind` (type) component `IdentifierKind [type]` (`009bb1ad-d649-50a2-b296-8fbe9ad71ca2`) lines 24-27 [crates/gcode/src/graph/typed_query.rs:24-27]
  - Signature: `pub enum IdentifierKind {`
  - Purpose: Indexed type `IdentifierKind` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:24-27]
- `TypedQueryError` (type) component `TypedQueryError [type]` (`848f7f52-30fc-5278-8555-a6851eec679f`) lines 30-38 [crates/gcode/src/graph/typed_query.rs:30-38]
  - Signature: `pub enum TypedQueryError {`
  - Purpose: Indexed type `TypedQueryError` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:30-38]
- `TypedQuery` (class) component `TypedQuery [class]` (`36f544e9-d6e4-5cf3-80fb-4bfae81d48f4`) lines 40-71 [crates/gcode/src/graph/typed_query.rs:40-71]
  - Signature: `impl TypedQuery {`
  - Purpose: TypedQuery constructs Cypher database queries with validated parameters by rendering typed values to Cypher syntax. [crates/gcode/src/graph/typed_query.rs:40-71]
- `TypedQuery.new` (method) component `TypedQuery.new [method]` (`033311ce-5853-5eb3-85f7-86b1ec16fe6c`) lines 41-46 [crates/gcode/src/graph/typed_query.rs:41-46]
  - Signature: `pub fn new(cypher: impl Into<String>) -> Self {`
  - Purpose: Constructs a new instance by converting the provided generic input into a String for the cypher field and initializing an empty HashMap for parameters. [crates/gcode/src/graph/typed_query.rs:41-46]
- `TypedQuery.with_params` (method) component `TypedQuery.with_params [method]` (`7bf33194-8dd4-5dd7-a601-63b8863c5fd1`) lines 48-58 [crates/gcode/src/graph/typed_query.rs:48-58]
  - Signature: `pub fn with_params<I, K>(cypher: impl Into<String>, params: I) -> Result<Self, TypedQueryError>`
  - Purpose: Constructs a new query from a Cypher string and populates it with an iterable collection of typed parameters, returning the query or a TypedQueryError if parameter insertion fails. [crates/gcode/src/graph/typed_query.rs:48-58]
- `TypedQuery.insert_param` (method) component `TypedQuery.insert_param [method]` (`01643f1a-bc6d-5aa0-b1c7-e24709829aa6`) lines 60-70 [crates/gcode/src/graph/typed_query.rs:60-70]
  - Signature: `pub fn insert_param(`
  - Purpose: Inserts a parameterized query value by validating the identifier name, rendering the TypedValue as Cypher syntax, and storing it in an internal parameters map. [crates/gcode/src/graph/typed_query.rs:60-70]
- `cypher_string_literal` (function) component `cypher_string_literal [function]` (`5725568d-6530-58ba-ae4a-9438c76a7ab6`) lines 73-75 [crates/gcode/src/graph/typed_query.rs:73-75]
  - Signature: `pub fn cypher_string_literal(s: &str) -> String {`
  - Purpose: Produces a Cypher string literal by escaping the input string's contents and enclosing it in single quotes. [crates/gcode/src/graph/typed_query.rs:73-75]
- `render_cypher_value` (function) component `render_cypher_value [function]` (`74c91864-ce73-5e7a-bf1c-749773eb62dd`) lines 77-98 [crates/gcode/src/graph/typed_query.rs:77-98]
  - Signature: `pub fn render_cypher_value(value: &TypedValue) -> Result<String, TypedQueryError> {`
  - Purpose: Recursively converts a `TypedValue` into its formatted Cypher literal string representation, validating map key identifiers during serialization. [crates/gcode/src/graph/typed_query.rs:77-98]
- `string_params` (function) component `string_params [function]` (`d2ced456-93df-58dd-9459-c67535715451`) lines 100-105 [crates/gcode/src/graph/typed_query.rs:100-105]
  - Signature: `pub fn string_params(values: &[(&str, &str)]) -> HashMap<String, String> {`
  - Purpose: Transforms a slice of string key-value pairs into a `HashMap` with `String` keys and Cypher-escaped `String` values. [crates/gcode/src/graph/typed_query.rs:100-105]
- `clamp_limit` (function) component `clamp_limit [function]` (`f9fb6abe-6731-56c4-8dd6-43418f0edf10`) lines 107-109 [crates/gcode/src/graph/typed_query.rs:107-109]
  - Signature: `pub fn clamp_limit(limit: usize, max: usize) -> usize {`
  - Purpose: Clamps the `limit` parameter to the closed interval [1, `max`]. [crates/gcode/src/graph/typed_query.rs:107-109]
- `clamp_offset` (function) component `clamp_offset [function]` (`ef1c3970-bc91-5dd1-863e-6fdc606915a8`) lines 111-113 [crates/gcode/src/graph/typed_query.rs:111-113]
  - Signature: `pub fn clamp_offset(offset: usize, max: usize) -> usize {`
  - Purpose: Returns the minimum of `offset` and `max`, effectively clamping the offset to not exceed the specified maximum value. [crates/gcode/src/graph/typed_query.rs:111-113]
- `id_list_literal` (function) component `id_list_literal [function]` (`7601d6f1-139b-57ed-818b-9d66f37e9a28`) lines 115-120 [crates/gcode/src/graph/typed_query.rs:115-120]
  - Signature: `pub fn id_list_literal(ids: &[String]) -> String {`
  - Purpose: Converts a slice of strings into a comma-separated Cypher string literal list by applying `cypher_string_literal()` to each ID and joining them with `", "`. [crates/gcode/src/graph/typed_query.rs:115-120]
- `validate_identifier` (function) component `validate_identifier [function]` (`653f5cff-90ae-52e9-9bfb-ba0d78c31172`) lines 122-141 [crates/gcode/src/graph/typed_query.rs:122-141]
  - Signature: `pub fn validate_identifier(identifier: &str, kind: IdentifierKind) -> Result<(), TypedQueryError> {`
  - Purpose: Validates that an identifier starts with an underscore or ASCII letter and contains only underscores or ASCII alphanumeric characters, returning a `TypedQueryError` on failure. [crates/gcode/src/graph/typed_query.rs:122-141]
- `render_string_literal` (function) component `render_string_literal [function]` (`d3f2d5f1-8cc2-555b-bf13-b6390bc2a13e`) lines 143-145 [crates/gcode/src/graph/typed_query.rs:143-145]
  - Signature: `fn render_string_literal(value: &str) -> Result<String, TypedQueryError> {`
  - Purpose: Renders a string value as a Cypher string literal by delegating to `cypher_string_literal()` and wrapping the result in a `Result<String, TypedQueryError>`. [crates/gcode/src/graph/typed_query.rs:143-145]
- `escape_string_contents` (function) component `escape_string_contents [function]` (`8010a20e-f99a-5801-bf8d-ebe8d737ab53`) lines 147-164 [crates/gcode/src/graph/typed_query.rs:147-164]
  - Signature: `fn escape_string_contents(value: &str) -> String {`
  - Purpose: Escapes special characters (quotes, backslash, whitespace) and control characters in a string by replacing them with their backslash escape sequences or Unicode hex escape codes. [crates/gcode/src/graph/typed_query.rs:147-164]
- `render_float` (function) component `render_float [function]` (`564814c2-501e-52e4-9095-bcb8ef6bcd5d`) lines 166-178 [crates/gcode/src/graph/typed_query.rs:166-178]
  - Signature: `fn render_float(value: f64) -> Result<String, TypedQueryError> {`
  - Purpose: Converts a finite f64 to a string representation with guaranteed decimal-point or exponential notation (appending ".0" if absent), or returns a TypedQueryError for non-finite values. [crates/gcode/src/graph/typed_query.rs:166-178]
- `IdentifierKind` (class) component `IdentifierKind [class]` (`8f4324a8-a5f5-5652-9c57-073442fd22be`) lines 180-187 [crates/gcode/src/graph/typed_query.rs:180-187]
  - Signature: `impl fmt::Display for IdentifierKind {`
  - Purpose: This Display trait implementation enables IdentifierKind enum variants to be formatted as human-readable strings, mapping `ParameterName` to "parameter name" and `MapKey` to "map key". [crates/gcode/src/graph/typed_query.rs:180-187]
- `IdentifierKind.fmt` (method) component `IdentifierKind.fmt [method]` (`8fdd0d1f-da86-5c54-a9af-cf309f441f88`) lines 181-186 [crates/gcode/src/graph/typed_query.rs:181-186]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Implements the Display trait by pattern-matching each enum variant and writing its corresponding string representation to the formatter. [crates/gcode/src/graph/typed_query.rs:181-186]
- `TypedQueryError` (class) component `TypedQueryError [class]` (`c6671deb-6d92-59d7-880e-c6683bbfed77`) lines 189-201 [crates/gcode/src/graph/typed_query.rs:189-201]
  - Signature: `impl fmt::Display for TypedQueryError {`
  - Purpose: The `fmt::Display` implementation for `TypedQueryError` formats two error variants—`InvalidIdentifier` (with regex pattern validation) and `NonFiniteFloat`—into human-readable error messages. [crates/gcode/src/graph/typed_query.rs:189-201]
- `TypedQueryError.fmt` (method) component `TypedQueryError.fmt [method]` (`948ed2fd-0b7f-53e4-a6c4-745c0c6b7a70`) lines 190-200 [crates/gcode/src/graph/typed_query.rs:190-200]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: This method implements the `Display` trait to format an error enum, rendering `InvalidIdentifier` and `NonFiniteFloat` variants as human-readable validation error messages with their respective constraints. [crates/gcode/src/graph/typed_query.rs:190-200]
- `TypedQueryError` (class) component `TypedQueryError [class]` (`1eaec93d-71d3-5d47-8e7c-e603e34e5173`) lines 203-203 [crates/gcode/src/graph/typed_query.rs:203]
  - Signature: `impl std::error::Error for TypedQueryError {}`
  - Purpose: TypedQueryError implements the `std::error::Error` trait, enabling it to be used as a standard error type in Rust's error handling system. [crates/gcode/src/graph/typed_query.rs:203]
- `typed_params_render_nested_safe_cypher_literals` (function) component `typed_params_render_nested_safe_cypher_literals [function]` (`e5dcf98b-a6d6-5dd2-8408-b7234acf5e20`) lines 211-276 [crates/gcode/src/graph/typed_query.rs:211-276]
  - Signature: `fn typed_params_render_nested_safe_cypher_literals() {`
  - Purpose: This function tests that `TypedQuery::with_params` correctly renders and escapes nested typed parameter values (strings with special characters, numbers, booleans, lists, and maps) into properly formatted Cypher literal strings. [crates/gcode/src/graph/typed_query.rs:211-276]
- `string_literals_escape_both_quote_delimiters` (function) component `string_literals_escape_both_quote_delimiters [function]` (`cf901af5-c937-5526-aada-187139f6d0f2`) lines 279-284 [crates/gcode/src/graph/typed_query.rs:279-284]
  - Signature: `fn string_literals_escape_both_quote_delimiters() {`
  - Purpose: Tests that `render_cypher_value()` correctly escapes both single and double quotes within Cypher string literals using backslash delimiters. [crates/gcode/src/graph/typed_query.rs:279-284]
- `string_literals_escape_control_characters` (function) component `string_literals_escape_control_characters [function]` (`09dd73ce-4ab9-5002-95a7-5dde362c9bfb`) lines 287-297 [crates/gcode/src/graph/typed_query.rs:287-297]
  - Signature: `fn string_literals_escape_control_characters() {`
  - Purpose: This test verifies that `render_cypher_value` correctly escapes control characters (newline, carriage return, tab, backspace, form feed, escape) in strings to their corresponding Cypher literal escape sequences. [crates/gcode/src/graph/typed_query.rs:287-297]
- `nested_string_values_escape_control_characters` (function) component `nested_string_values_escape_control_characters [function]` (`971887e9-0c6e-545a-842b-1ee5105969e6`) lines 300-315 [crates/gcode/src/graph/typed_query.rs:300-315]
  - Signature: `fn nested_string_values_escape_control_characters() {`
  - Purpose: This function tests that `render_cypher_value` correctly escapes control characters (newline and tab) in nested string values when rendering Cypher map syntax. [crates/gcode/src/graph/typed_query.rs:300-315]
- `invalid_identifiers_return_typed_errors` (function) component `invalid_identifiers_return_typed_errors [function]` (`4b0dd5f0-5186-5324-be9c-d73284c11d8b`) lines 318-341 [crates/gcode/src/graph/typed_query.rs:318-341]
  - Signature: `fn invalid_identifiers_return_typed_errors() {`
  - Purpose: Tests that invalid identifiers in parameter names and map keys return appropriately typed `TypedQueryError::InvalidIdentifier` errors with the correct identifier kind. [crates/gcode/src/graph/typed_query.rs:318-341]
- `unsafe_values_return_typed_errors` (function) component `unsafe_values_return_typed_errors [function]` (`3ed62b10-a62b-54cc-b7de-6834c141e46c`) lines 344-350 [crates/gcode/src/graph/typed_query.rs:344-350]
  - Signature: `fn unsafe_values_return_typed_errors() {`
  - Purpose: This test function validates that rendering non-finite f64 values (NaN, ±∞) as TypedValue::Float consistently produces TypedQueryError::NonFiniteFloat errors. [crates/gcode/src/graph/typed_query.rs:344-350]

