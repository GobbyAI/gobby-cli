---
title: crates/gwiki/src/output.rs
type: code_file
provenance:
- file: crates/gwiki/src/output.rs
  ranges:
  - 10-13
  - 16-19
  - 21-28
  - '30'
  - 32-36
  - 38-42
  - 44-53
  - 55-61
  - 63-66
  - 68-70
  - 73-80
  - 82-99
  - 102-124
  - 127-135
  - 138-144
  - 149-152
  - 154-172
  - 175-185
  - 188-192
  - 195-202
  - 205-209
  - 216-220
  - 223-227
  - 230-236
  - 238-253
  - 256-261
  - 264-270
  - 272-287
  - 289-316
  - 325-416
  - 419-445
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/output.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/output.rs` exposes 39 indexed API symbols.
[crates/gwiki/src/output.rs:10-13]
[crates/gwiki/src/output.rs:16-19]
[crates/gwiki/src/output.rs:21-28]
[crates/gwiki/src/output.rs:22-27]
[crates/gwiki/src/output.rs:30]

## API Symbols

- `Format` (type) component `Format [type]` (`d5d3dd3b-a336-5b1f-be7f-6ae6ee7afdc4`) lines 10-13 [crates/gwiki/src/output.rs:10-13]
  - Signature: `pub enum Format {`
  - Purpose: Indexed type `Format` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:10-13]
- `OutputError` (type) component `OutputError [type]` (`13586740-fc38-5319-87dc-b3218979de76`) lines 16-19 [crates/gwiki/src/output.rs:16-19]
  - Signature: `pub enum OutputError {`
  - Purpose: Indexed type `OutputError` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:16-19]
- `OutputError` (class) component `OutputError [class]` (`fba419c8-3db0-51f2-960d-1fc61da1abc2`) lines 21-28 [crates/gwiki/src/output.rs:21-28]
  - Signature: `impl fmt::Display for OutputError {`
  - Purpose: Implements `fmt::Display` for `OutputError`, formatting its `Io` and `Json` error variants as human-readable error messages prefixed with contextual descriptions. [crates/gwiki/src/output.rs:21-28]
- `OutputError.fmt` (method) component `OutputError.fmt [method]` (`e6931e63-4653-595e-ac83-e00ef62e8bf0`) lines 22-27 [crates/gwiki/src/output.rs:22-27]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: This method implements the `Display` trait to format an error enum's two variants (`Io` and `Json`) with contextual error descriptions. [crates/gwiki/src/output.rs:22-27]
- `OutputError` (class) component `OutputError [class]` (`c106b6ed-b048-5652-9f1d-7ce9f21943bc`) lines 30-30 [crates/gwiki/src/output.rs:30]
  - Signature: `impl std::error::Error for OutputError {}`
  - Purpose: `OutputError` implements Rust's standard `Error` trait with default trait method implementations. [crates/gwiki/src/output.rs:30]
- `OutputError` (class) component `OutputError [class]` (`18149cda-931c-5c80-8de6-87278a3466b9`) lines 32-36 [crates/gwiki/src/output.rs:32-36]
  - Signature: `impl From<std::io::Error> for OutputError {`
  - Purpose: This `From` trait implementation enables implicit conversion of `std::io::Error` to `OutputError` by wrapping it in the `Io` variant. [crates/gwiki/src/output.rs:32-36]
- `OutputError.from` (method) component `OutputError.from [method]` (`83f0156d-af88-5c50-a1dd-c732d705e896`) lines 33-35 [crates/gwiki/src/output.rs:33-35]
  - Signature: `fn from(error: std::io::Error) -> Self {`
  - Purpose: Converts a `std::io::Error` into the implementing enum type by wrapping it in the `Io` variant, implementing the `From` trait for automatic error conversion. [crates/gwiki/src/output.rs:33-35]
- `OutputError` (class) component `OutputError [class]` (`638ca648-517f-5c59-aa91-1ce42232078d`) lines 38-42 [crates/gwiki/src/output.rs:38-42]
  - Signature: `impl From<serde_json::Error> for OutputError {`
  - Purpose: This implements the `From` trait to enable automatic conversion of `serde_json::Error` into the `OutputError::Json` enum variant. [crates/gwiki/src/output.rs:38-42]
- `OutputError.from` (method) component `OutputError.from [method]` (`3c510a50-1357-5e61-9ff7-f925d5390f98`) lines 39-41 [crates/gwiki/src/output.rs:39-41]
  - Signature: `fn from(error: serde_json::Error) -> Self {`
  - Purpose: This `From` trait implementation converts a `serde_json::Error` into the target type by wrapping it in the `Json` enum variant. [crates/gwiki/src/output.rs:39-41]
- `print_result` (function) component `print_result [function]` (`ed965b4a-347d-50a6-9a8f-edef908d335e`) lines 44-53 [crates/gwiki/src/output.rs:44-53]
  - Signature: `pub fn print_result(`
  - Purpose: Serializes a `CommandResult` to either JSON or plain text format and writes it to the provided writer based on the `Format` enum variant. [crates/gwiki/src/output.rs:44-53]
- `print_json` (function) component `print_json [function]` (`990bf29c-71d6-5407-8fef-adc1101fcb8f`) lines 55-61 [crates/gwiki/src/output.rs:55-61]
  - Signature: `pub fn print_json<T: serde::Serialize + ?Sized>(`
  - Purpose: Writes a pretty-printed JSON serialization of a generic serde-serializable value to the provided writer. [crates/gwiki/src/output.rs:55-61]
- `print_text` (function) component `print_text [function]` (`908f89c2-0e58-5d7f-8afd-6ec53611b77a`) lines 63-66 [crates/gwiki/src/output.rs:63-66]
  - Signature: `pub fn print_text(writer: &mut impl Write, text: &str) -> Result<(), OutputError> {`
  - Purpose: This function writes a line of text to any type implementing the `Write` trait and returns a `Result` that propagates any `OutputError`. [crates/gwiki/src/output.rs:63-66]
- `print_status` (function) component `print_status [function]` (`64f93a82-188b-5c8a-a5ce-32dea3bde8b6`) lines 68-70 [crates/gwiki/src/output.rs:68-70]
  - Signature: `pub fn print_status(message: &str) {`
  - Purpose: `print_status` writes a message to standard error (stderr) with the "gwiki: " prefix. [crates/gwiki/src/output.rs:68-70]
- `SearchOutput` (class) component `SearchOutput [class]` (`cbfd0ce3-f0de-57cc-9358-40d405770a4d`) lines 73-80 [crates/gwiki/src/output.rs:73-80]
  - Signature: `pub struct SearchOutput {`
  - Purpose: SearchOutput is a struct aggregating search command metadata, scope, query parameters, the returned results, and any quality degradations encountered during execution. [crates/gwiki/src/output.rs:73-80]
- `SearchOutput` (class) component `SearchOutput [class]` (`7c61b245-13df-5635-9d50-a4d55aa1e6e4`) lines 82-99 [crates/gwiki/src/output.rs:82-99]
  - Signature: `impl SearchOutput {`
  - Purpose: `SearchOutput` is a constructor that instantiates a new search command output with a given scope, query string, result limit, result collection, and degradation messages. [crates/gwiki/src/output.rs:82-99]
- `SearchOutput.new` (method) component `SearchOutput.new [method]` (`f4a4ca49-cb4b-5f75-9401-52950f96bcd2`) lines 83-98 [crates/gwiki/src/output.rs:83-98]
  - Signature: `pub fn new(`
  - Purpose: Constructs a new search instance with the provided scope, query string, result limit, search results vector, and degradations list, while hardcoding the command field to "search". [crates/gwiki/src/output.rs:83-98]
- `AskOutput` (class) component `AskOutput [class]` (`9a65ff4b-3e08-5689-a255-8f9b629e8c3d`) lines 102-124 [crates/gwiki/src/output.rs:102-124]
  - Signature: `pub struct AskOutput {`
  - Purpose: `AskOutput` is a struct that encapsulates the complete response to a search query, including results, execution metadata (status, degradation, truncation), source citations, code relationships, and optional AI-synthesized analysis. [crates/gwiki/src/output.rs:102-124]
- `AskCodeEdgeOutput` (class) component `AskCodeEdgeOutput [class]` (`a9934a7c-27d9-5fbc-a67e-e6a339706c7e`) lines 127-135 [crates/gwiki/src/output.rs:127-135]
  - Signature: `pub struct AskCodeEdgeOutput {`
  - Purpose: `AskCodeEdgeOutput` is a serializable struct representing a directed edge in a code dependency graph, containing source and target identifiers, edge classification metadata (kind and direction), an optional line number, and provenance information. [crates/gwiki/src/output.rs:127-135]
- `AskCodeCitationOutput` (class) component `AskCodeCitationOutput [class]` (`abda8ed8-ac86-5484-88a6-f3b55a849b1b`) lines 138-144 [crates/gwiki/src/output.rs:138-144]
  - Signature: `pub struct AskCodeCitationOutput {`
  - Purpose: `AskCodeCitationOutput` is a serializable struct that represents a code citation with a required file path and optional line number and symbol identifier, conditionally omitting None values during serialization. [crates/gwiki/src/output.rs:138-144]
- `SearchResultType` (type) component `SearchResultType [type]` (`ff38e03a-1a0d-5e43-9e86-1d1910739bbb`) lines 149-152 [crates/gwiki/src/output.rs:149-152]
  - Signature: `pub enum SearchResultType {`
  - Purpose: Indexed type `SearchResultType` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:149-152]
- `SearchResultType` (class) component `SearchResultType [class]` (`95e11036-1a71-5c89-8e8a-b54f90e4186d`) lines 154-172 [crates/gwiki/src/output.rs:154-172]
  - Signature: `impl SearchResultType {`
  - Purpose: This implementation classifies vault-relative wiki page paths as either code (if located under `code/files/`) or wiki content, with a predicate method to test the code classification. [crates/gwiki/src/output.rs:154-172]
- `SearchResultType.from_wiki_page` (method) component `SearchResultType.from_wiki_page [method]` (`7d05c4dc-3b0f-5638-98ec-c3bb7246c857`) lines 157-167 [crates/gwiki/src/output.rs:157-167]
  - Signature: `pub fn from_wiki_page(path: &Path) -> Self {`
  - Purpose: Returns `Self::Code` if the normalized path (with backslashes converted to forward slashes) starts with `"code/files/"`, otherwise returns `Self::Wiki`. [crates/gwiki/src/output.rs:157-167]
- `SearchResultType.is_code` (method) component `SearchResultType.is_code [method]` (`0a38d7a3-7c89-5990-a589-0fdebc958ea8`) lines 169-171 [crates/gwiki/src/output.rs:169-171]
  - Signature: `pub fn is_code(self) -> bool {`
  - Purpose: The `is_code` method returns `true` if the enum variant is `Code`, otherwise `false`. [crates/gwiki/src/output.rs:169-171]
- `SearchResultOutput` (class) component `SearchResultOutput [class]` (`cdd9f244-d679-522c-b389-e2334ea9b9a8`) lines 175-185 [crates/gwiki/src/output.rs:175-185]
  - Signature: `pub struct SearchResultOutput {`
  - Purpose: Encapsulates a ranked search result with title, snippet, relevance score, source paths, and explanatory metadata. [crates/gwiki/src/output.rs:175-185]
- `AskRelatedPageOutput` (class) component `AskRelatedPageOutput [class]` (`9f21297d-24f7-5a98-9914-10c790180afa`) lines 188-192 [crates/gwiki/src/output.rs:188-192]
  - Signature: `pub struct AskRelatedPageOutput {`
  - Purpose: A struct representing a ranked page search result containing an optional title, filesystem path, and floating-point relevance score. [crates/gwiki/src/output.rs:188-192]
- `AskAiOutput` (class) component `AskAiOutput [class]` (`59dfbeff-2c1c-5c9e-b54b-239ca0beca26`) lines 195-202 [crates/gwiki/src/output.rs:195-202]
  - Signature: `pub struct AskAiOutput {`
  - Purpose: `AskAiOutput` is a struct that encapsulates the result metadata of an AI request, containing a boolean request flag, static string references for mode, route, and status, and optional fields for the model identifier and error information. [crates/gwiki/src/output.rs:195-202]
- `AskSynthesisOutput` (class) component `AskSynthesisOutput [class]` (`5b8a0128-128d-5c63-8656-37b08698a4d0`) lines 205-209 [crates/gwiki/src/output.rs:205-209]
  - Signature: `pub struct AskSynthesisOutput {`
  - Purpose: `AskSynthesisOutput` is a struct that encapsulates the result of a synthesis operation, containing a synthesized answer string, an optional model identifier, and citation verification results. [crates/gwiki/src/output.rs:205-209]
- `AskCitationCheckOutput` (class) component `AskCitationCheckOutput [class]` (`f980369e-6343-524f-85b9-a6587109be7b`) lines 216-220 [crates/gwiki/src/output.rs:216-220]
  - Signature: `pub struct AskCitationCheckOutput {`
  - Purpose: `AskCitationCheckOutput` is a struct that encapsulates the results of a citation verification operation, containing a static status indicator, a count of claims checked, and a vector of unsupported claim strings. [crates/gwiki/src/output.rs:216-220]
- `SearchSourceExplanationOutput` (class) component `SearchSourceExplanationOutput [class]` (`9cb0deea-94eb-5f40-b86a-c7cf1cc571a2`) lines 223-227 [crates/gwiki/src/output.rs:223-227]
  - Signature: `pub struct SearchSourceExplanationOutput {`
  - Purpose: `SearchSourceExplanationOutput` is a struct that encapsulates search result metadata, containing a source identifier string, its ranking position (usize), and a floating-point relevance score (f64). [crates/gwiki/src/output.rs:223-227]
- `QueryOutput` (class) component `QueryOutput [class]` (`78109ee2-b945-5ba3-b7b7-c084a1666b2b`) lines 230-236 [crates/gwiki/src/output.rs:230-236]
  - Signature: `pub struct QueryOutput {`
  - Purpose: `QueryOutput` is a Rust struct that encapsulates a query response, containing a static command identifier, scope context, input query string, generated answer string, and a vector of citation references. [crates/gwiki/src/output.rs:230-236]
- `QueryOutput` (class) component `QueryOutput [class]` (`64461ad0-e6fe-5f66-acf3-a765ae8f48cc`) lines 238-253 [crates/gwiki/src/output.rs:238-253]
  - Signature: `impl QueryOutput {`
  - Purpose: `QueryOutput::answered` is a constructor method that instantiates a query response struct with a scope identity, query and answer strings (via the `Into` trait for flexible input types), and a vector of citations. [crates/gwiki/src/output.rs:238-253]
- `QueryOutput.answered` (method) component `QueryOutput.answered [method]` (`267ff829-fda3-5916-ab51-97725675e03a`) lines 239-252 [crates/gwiki/src/output.rs:239-252]
  - Signature: `pub fn answered(`
  - Purpose: Constructs and returns a Self instance configured with command="query" and the provided scope, query string, answer string, and citations. [crates/gwiki/src/output.rs:239-252]
- `QueryCitation` (class) component `QueryCitation [class]` (`deebcb1c-d4a2-5d4b-b170-c5c6249b01cb`) lines 256-261 [crates/gwiki/src/output.rs:256-261]
  - Signature: `pub struct QueryCitation {`
  - Purpose: `QueryCitation` is a struct that pairs a source file path with a wiki page reference, optionally including a title and line information for citation tracking. [crates/gwiki/src/output.rs:256-261]
- `AuditOutput` (class) component `AuditOutput [class]` (`ea2b6aff-c07d-5788-887c-a8c569ff7cf7`) lines 264-270 [crates/gwiki/src/output.rs:264-270]
  - Signature: `pub struct AuditOutput {`
  - Purpose: AuditOutput is a struct that encapsulates the results of an audit operation, containing the executed command, scope context, count of unsupported claims detected, an optional report output path, and the source file paths that were audited. [crates/gwiki/src/output.rs:264-270]
- `AuditOutput` (class) component `AuditOutput [class]` (`8e09801a-d01d-551d-935b-74c5a61cf257`) lines 272-287 [crates/gwiki/src/output.rs:272-287]
  - Signature: `impl AuditOutput {`
  - Purpose: `AuditOutput::new()` is a constructor that initializes an `AuditOutput` instance with a scope identity, unsupported claim count, optional report path, and source paths, setting the command field to "audit". [crates/gwiki/src/output.rs:272-287]
- `AuditOutput.new` (method) component `AuditOutput.new [method]` (`0af68c17-d456-56d7-bf34-7182de782081`) lines 273-286 [crates/gwiki/src/output.rs:273-286]
  - Signature: `pub fn new(`
  - Purpose: Instantiates an audit command struct with the provided scope identity, unsupported claim count, optional report path, and source paths. [crates/gwiki/src/output.rs:273-286]
- `render_query_text` (function) component `render_query_text [function]` (`94927022-d299-5b3b-977c-e67abf37b9c8`) lines 289-316 [crates/gwiki/src/output.rs:289-316]
  - Signature: `pub fn render_query_text(output: &QueryOutput) -> String {`
  - Purpose: Converts a `QueryOutput` struct into a formatted text string representation containing the query scope, question, answer, and citations with their source paths, wiki pages, and optional metadata. [crates/gwiki/src/output.rs:289-316]
- `json_output_is_stable` (function) component `json_output_is_stable [function]` (`db6d6c87-95ee-5002-9b5b-4d849a7d6bbe`) lines 325-416 [crates/gwiki/src/output.rs:325-416]
  - Signature: `fn json_output_is_stable() {`
  - Purpose: This function asserts that a `SearchOutput` struct serializes to a deterministic JSON representation matching its expected schema via `serde_json::to_value()`. [crates/gwiki/src/output.rs:325-416]
- `query_output_includes_citations` (function) component `query_output_includes_citations [function]` (`e395a29f-c131-5747-9f43-e0f0bb4e9d03`) lines 419-445 [crates/gwiki/src/output.rs:419-445]
  - Signature: `fn query_output_includes_citations() {`
  - Purpose: # Summary

A unit test that verifies `QueryOutput` correctly initializes with `QueryCitation` metadata and that `render_query_text` properly formats source and wiki page paths in the rendered query output. [crates/gwiki/src/output.rs:419-445]

