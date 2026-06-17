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
  - 181-186
  - 190-200
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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/typed_query.rs:7-10](crates/gcode/src/graph/typed_query.rs#L7-L10), [crates/gcode/src/graph/typed_query.rs:13-21](crates/gcode/src/graph/typed_query.rs#L13-L21), [crates/gcode/src/graph/typed_query.rs:24-27](crates/gcode/src/graph/typed_query.rs#L24-L27), [crates/gcode/src/graph/typed_query.rs:30-38](crates/gcode/src/graph/typed_query.rs#L30-L38), [crates/gcode/src/graph/typed_query.rs:41-46](crates/gcode/src/graph/typed_query.rs#L41-L46), [crates/gcode/src/graph/typed_query.rs:48-58](crates/gcode/src/graph/typed_query.rs#L48-L58), [crates/gcode/src/graph/typed_query.rs:60-70](crates/gcode/src/graph/typed_query.rs#L60-L70), [crates/gcode/src/graph/typed_query.rs:73-75](crates/gcode/src/graph/typed_query.rs#L73-L75), [crates/gcode/src/graph/typed_query.rs:77-98](crates/gcode/src/graph/typed_query.rs#L77-L98), [crates/gcode/src/graph/typed_query.rs:100-105](crates/gcode/src/graph/typed_query.rs#L100-L105), [crates/gcode/src/graph/typed_query.rs:107-109](crates/gcode/src/graph/typed_query.rs#L107-L109), [crates/gcode/src/graph/typed_query.rs:111-113](crates/gcode/src/graph/typed_query.rs#L111-L113), [crates/gcode/src/graph/typed_query.rs:115-120](crates/gcode/src/graph/typed_query.rs#L115-L120), [crates/gcode/src/graph/typed_query.rs:122-141](crates/gcode/src/graph/typed_query.rs#L122-L141), [crates/gcode/src/graph/typed_query.rs:143-145](crates/gcode/src/graph/typed_query.rs#L143-L145), [crates/gcode/src/graph/typed_query.rs:147-164](crates/gcode/src/graph/typed_query.rs#L147-L164), [crates/gcode/src/graph/typed_query.rs:166-178](crates/gcode/src/graph/typed_query.rs#L166-L178), [crates/gcode/src/graph/typed_query.rs:181-186](crates/gcode/src/graph/typed_query.rs#L181-L186), [crates/gcode/src/graph/typed_query.rs:190-200](crates/gcode/src/graph/typed_query.rs#L190-L200), [crates/gcode/src/graph/typed_query.rs:211-276](crates/gcode/src/graph/typed_query.rs#L211-L276), [crates/gcode/src/graph/typed_query.rs:279-284](crates/gcode/src/graph/typed_query.rs#L279-L284), [crates/gcode/src/graph/typed_query.rs:287-297](crates/gcode/src/graph/typed_query.rs#L287-L297), [crates/gcode/src/graph/typed_query.rs:300-315](crates/gcode/src/graph/typed_query.rs#L300-L315), [crates/gcode/src/graph/typed_query.rs:318-341](crates/gcode/src/graph/typed_query.rs#L318-L341), [crates/gcode/src/graph/typed_query.rs:344-350](crates/gcode/src/graph/typed_query.rs#L344-L350)

</details>

# crates/gcode/src/graph/typed_query.rs

Module: [[code/modules/crates/gcode/src/graph|crates/gcode/src/graph]]

## Purpose

This file defines a typed Cypher query builder and renderer. `TypedQuery` holds the query text plus a stringified parameter map, while `TypedValue` models the allowed parameter value shapes and `TypedQueryError` reports invalid identifiers or non-finite floats. The helper functions validate parameter names and map keys, escape and format strings, numbers, lists, and maps into safe Cypher literals, and `TypedQuery::new`, `with_params`, and `insert_param` compose those pieces to build a query with rendered parameters.
[crates/gcode/src/graph/typed_query.rs:7-10]
[crates/gcode/src/graph/typed_query.rs:13-21]
[crates/gcode/src/graph/typed_query.rs:24-27]
[crates/gcode/src/graph/typed_query.rs:30-38]
[crates/gcode/src/graph/typed_query.rs:41-46]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `TypedQuery` | class | `pub struct TypedQuery {` | `TypedQuery [class]` | `253b9b29-dceb-5672-a721-5d54c2418774` | 7-10 [crates/gcode/src/graph/typed_query.rs:7-10] | Indexed class `TypedQuery` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:7-10] |
| `TypedValue` | type | `pub enum TypedValue {` | `TypedValue [type]` | `b8f78e98-501e-5b25-a52f-a3ae5a455b7d` | 13-21 [crates/gcode/src/graph/typed_query.rs:13-21] | Indexed type `TypedValue` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:13-21] |
| `IdentifierKind` | type | `pub enum IdentifierKind {` | `IdentifierKind [type]` | `009bb1ad-d649-50a2-b296-8fbe9ad71ca2` | 24-27 [crates/gcode/src/graph/typed_query.rs:24-27] | Indexed type `IdentifierKind` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:24-27] |
| `TypedQueryError` | type | `pub enum TypedQueryError {` | `TypedQueryError [type]` | `848f7f52-30fc-5278-8555-a6851eec679f` | 30-38 [crates/gcode/src/graph/typed_query.rs:30-38] | Indexed type `TypedQueryError` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:30-38] |
| `TypedQuery::new` | method | `pub fn new(cypher: impl Into<String>) -> Self {` | `TypedQuery::new [method]` | `033311ce-5853-5eb3-85f7-86b1ec16fe6c` | 41-46 [crates/gcode/src/graph/typed_query.rs:41-46] | Indexed method `TypedQuery::new` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:41-46] |
| `TypedQuery::with_params` | method | `pub fn with_params<I, K>(cypher: impl Into<String>, params: I) -> Result<Self, TypedQueryError>` | `TypedQuery::with_params [method]` | `7bf33194-8dd4-5dd7-a601-63b8863c5fd1` | 48-58 [crates/gcode/src/graph/typed_query.rs:48-58] | Indexed method `TypedQuery::with_params` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:48-58] |
| `TypedQuery::insert_param` | method | `pub fn insert_param(` | `TypedQuery::insert_param [method]` | `01643f1a-bc6d-5aa0-b1c7-e24709829aa6` | 60-70 [crates/gcode/src/graph/typed_query.rs:60-70] | Indexed method `TypedQuery::insert_param` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:60-70] |
| `cypher_string_literal` | function | `pub fn cypher_string_literal(s: &str) -> String {` | `cypher_string_literal [function]` | `5725568d-6530-58ba-ae4a-9438c76a7ab6` | 73-75 [crates/gcode/src/graph/typed_query.rs:73-75] | Indexed function `cypher_string_literal` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:73-75] |
| `render_cypher_value` | function | `pub fn render_cypher_value(value: &TypedValue) -> Result<String, TypedQueryError> {` | `render_cypher_value [function]` | `74c91864-ce73-5e7a-bf1c-749773eb62dd` | 77-98 [crates/gcode/src/graph/typed_query.rs:77-98] | Indexed function `render_cypher_value` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:77-98] |
| `string_params` | function | `pub fn string_params(values: &[(&str, &str)]) -> HashMap<String, String> {` | `string_params [function]` | `d2ced456-93df-58dd-9459-c67535715451` | 100-105 [crates/gcode/src/graph/typed_query.rs:100-105] | Indexed function `string_params` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:100-105] |
| `clamp_limit` | function | `pub fn clamp_limit(limit: usize, max: usize) -> usize {` | `clamp_limit [function]` | `f9fb6abe-6731-56c4-8dd6-43418f0edf10` | 107-109 [crates/gcode/src/graph/typed_query.rs:107-109] | Indexed function `clamp_limit` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:107-109] |
| `clamp_offset` | function | `pub fn clamp_offset(offset: usize, max: usize) -> usize {` | `clamp_offset [function]` | `ef1c3970-bc91-5dd1-863e-6fdc606915a8` | 111-113 [crates/gcode/src/graph/typed_query.rs:111-113] | Indexed function `clamp_offset` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:111-113] |
| `id_list_literal` | function | `pub fn id_list_literal(ids: &[String]) -> String {` | `id_list_literal [function]` | `7601d6f1-139b-57ed-818b-9d66f37e9a28` | 115-120 [crates/gcode/src/graph/typed_query.rs:115-120] | Indexed function `id_list_literal` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:115-120] |
| `validate_identifier` | function | `pub fn validate_identifier(identifier: &str, kind: IdentifierKind) -> Result<(), TypedQueryError> {` | `validate_identifier [function]` | `653f5cff-90ae-52e9-9bfb-ba0d78c31172` | 122-141 [crates/gcode/src/graph/typed_query.rs:122-141] | Indexed function `validate_identifier` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:122-141] |
| `render_string_literal` | function | `fn render_string_literal(value: &str) -> Result<String, TypedQueryError> {` | `render_string_literal [function]` | `d3f2d5f1-8cc2-555b-bf13-b6390bc2a13e` | 143-145 [crates/gcode/src/graph/typed_query.rs:143-145] | Indexed function `render_string_literal` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:143-145] |
| `escape_string_contents` | function | `fn escape_string_contents(value: &str) -> String {` | `escape_string_contents [function]` | `8010a20e-f99a-5801-bf8d-ebe8d737ab53` | 147-164 [crates/gcode/src/graph/typed_query.rs:147-164] | Indexed function `escape_string_contents` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:147-164] |
| `render_float` | function | `fn render_float(value: f64) -> Result<String, TypedQueryError> {` | `render_float [function]` | `564814c2-501e-52e4-9095-bcb8ef6bcd5d` | 166-178 [crates/gcode/src/graph/typed_query.rs:166-178] | Indexed function `render_float` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:166-178] |
| `IdentifierKind::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `IdentifierKind::fmt [method]` | `8fdd0d1f-da86-5c54-a9af-cf309f441f88` | 181-186 [crates/gcode/src/graph/typed_query.rs:181-186] | Indexed method `IdentifierKind::fmt` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:181-186] |
| `TypedQueryError::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `TypedQueryError::fmt [method]` | `948ed2fd-0b7f-53e4-a6c4-745c0c6b7a70` | 190-200 [crates/gcode/src/graph/typed_query.rs:190-200] | Indexed method `TypedQueryError::fmt` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:190-200] |
| `typed_params_render_nested_safe_cypher_literals` | function | `fn typed_params_render_nested_safe_cypher_literals() {` | `typed_params_render_nested_safe_cypher_literals [function]` | `e5dcf98b-a6d6-5dd2-8408-b7234acf5e20` | 211-276 [crates/gcode/src/graph/typed_query.rs:211-276] | Indexed function `typed_params_render_nested_safe_cypher_literals` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:211-276] |
| `string_literals_escape_both_quote_delimiters` | function | `fn string_literals_escape_both_quote_delimiters() {` | `string_literals_escape_both_quote_delimiters [function]` | `cf901af5-c937-5526-aada-187139f6d0f2` | 279-284 [crates/gcode/src/graph/typed_query.rs:279-284] | Indexed function `string_literals_escape_both_quote_delimiters` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:279-284] |
| `string_literals_escape_control_characters` | function | `fn string_literals_escape_control_characters() {` | `string_literals_escape_control_characters [function]` | `09dd73ce-4ab9-5002-95a7-5dde362c9bfb` | 287-297 [crates/gcode/src/graph/typed_query.rs:287-297] | Indexed function `string_literals_escape_control_characters` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:287-297] |
| `nested_string_values_escape_control_characters` | function | `fn nested_string_values_escape_control_characters() {` | `nested_string_values_escape_control_characters [function]` | `971887e9-0c6e-545a-842b-1ee5105969e6` | 300-315 [crates/gcode/src/graph/typed_query.rs:300-315] | Indexed function `nested_string_values_escape_control_characters` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:300-315] |
| `invalid_identifiers_return_typed_errors` | function | `fn invalid_identifiers_return_typed_errors() {` | `invalid_identifiers_return_typed_errors [function]` | `4b0dd5f0-5186-5324-be9c-d73284c11d8b` | 318-341 [crates/gcode/src/graph/typed_query.rs:318-341] | Indexed function `invalid_identifiers_return_typed_errors` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:318-341] |
| `unsafe_values_return_typed_errors` | function | `fn unsafe_values_return_typed_errors() {` | `unsafe_values_return_typed_errors [function]` | `3ed62b10-a62b-54cc-b7de-6834c141e46c` | 344-350 [crates/gcode/src/graph/typed_query.rs:344-350] | Indexed function `unsafe_values_return_typed_errors` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:344-350] |
