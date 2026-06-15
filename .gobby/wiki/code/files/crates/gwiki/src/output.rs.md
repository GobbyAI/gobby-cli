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
  - 73-81
  - 83-102
  - 107-125
  - 131-151
  - 155-159
  - 162-168
  - 173-176
  - 178-196
  - 199-209
  - 212-219
  - 222-226
  - 233-237
  - 240-244
  - 247-253
  - 255-270
  - 273-278
  - 281-287
  - 289-304
  - 306-333
  - 342-434
  - 437-476
  - 479-505
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/output.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines gwiki’s output layer: a `Format` switch, a unified `OutputError`, and helpers for printing results as JSON, plain text, or status messages. It also contains the serializable response structs for `search`, `ask`, `query`, and `audit` commands, along with citation and search-hit metadata types used to shape stable CLI output. The pieces work together by building command-specific output records, deriving citations from search hits where needed, and rendering those records through the shared print functions and text formatter.
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
- `SearchOutput` (class) component `SearchOutput [class]` (`cbfd0ce3-f0de-57cc-9358-40d405770a4d`) lines 73-81 [crates/gwiki/src/output.rs:73-81]
  - Signature: `pub struct SearchOutput {`
  - Purpose: 'SearchOutput' is a search response struct that records the invoked command, target scope, query string, result limit, returned 'SearchResultOutput' items, associated 'CodeCitationOutput' entries, and any degradation messages. [crates/gwiki/src/output.rs:73-81]
- `SearchOutput` (class) component `SearchOutput [class]` (`22d8af39-7b95-5bc4-aeab-db890619de25`) lines 83-102 [crates/gwiki/src/output.rs:83-102]
  - Signature: `impl SearchOutput {`
  - Purpose: 'SearchOutput::new' constructs a 'SearchOutput' for a search command by storing the scope, query, limit, results, and degradations, while deriving 'code_citations' from the provided results and hardcoding 'command' to '"search"'. [crates/gwiki/src/output.rs:83-102]
- `SearchOutput.new` (method) component `SearchOutput.new [method]` (`b09db649-43b7-51e5-ad12-88fddc71aa69`) lines 84-101 [crates/gwiki/src/output.rs:84-101]
  - Signature: `pub fn new(`
  - Purpose: Creates a 'Self' for a search operation by converting 'query' into a 'String', copying 'scope', 'limit', 'results', and 'degradations', deriving 'code_citations' from 'results', and setting 'command' to '"search"'. [crates/gwiki/src/output.rs:84-101]
- `code_citations_from_results` (function) component `code_citations_from_results [function]` (`c27e36c0-ade6-5163-8505-0cd0576fb6f9`) lines 107-125 [crates/gwiki/src/output.rs:107-125]
  - Signature: `pub fn code_citations_from_results(results: &[SearchResultOutput]) -> Vec<CodeCitationOutput> {`
  - Purpose: It filters the input search results to code hits, deduplicates them by '(file path, title)' using a 'BTreeSet', and returns one 'CodeCitationOutput' per unique file-symbol pair with 'line' set to 'None'. [crates/gwiki/src/output.rs:107-125]
- `AskOutput` (class) component `AskOutput [class]` (`578c4b1f-7d89-5d39-970f-7954da1f98fc`) lines 131-151 [crates/gwiki/src/output.rs:131-151]
  - Signature: `pub struct AskOutput {`
  - Purpose: 'AskOutput' is a structured result envelope for an 'ask' operation that packages the command metadata, scope, query, status, search hits, source and citation evidence, token-budget/truncation diagnostics, warnings, and optional AI synthesis output. [crates/gwiki/src/output.rs:131-151]
- `AskEvidenceOutput` (class) component `AskEvidenceOutput [class]` (`d24c6fb4-7c6a-56d7-a802-ed9e6b5fe5a2`) lines 155-159 [crates/gwiki/src/output.rs:155-159]
  - Signature: `pub struct AskEvidenceOutput {`
  - Purpose: 'AskEvidenceOutput' is a Rust output struct that records the generated wiki page path, the originating source file path, and the number of characters included in the excerpt. [crates/gwiki/src/output.rs:155-159]
- `CodeCitationOutput` (class) component `CodeCitationOutput [class]` (`d11dde81-b751-5642-81e2-e6fc83b25f65`) lines 162-168 [crates/gwiki/src/output.rs:162-168]
  - Signature: `pub struct CodeCitationOutput {`
  - Purpose: 'CodeCitationOutput' is a serializable citation record that identifies a source 'file' and optionally includes a 'line' number and 'symbol' name, omitting unset optional fields during serialization. [crates/gwiki/src/output.rs:162-168]
- `SearchResultType` (type) component `SearchResultType [type]` (`a3d31626-3533-557d-9328-c8bd13050219`) lines 173-176 [crates/gwiki/src/output.rs:173-176]
  - Signature: `pub enum SearchResultType {`
  - Purpose: Indexed type `SearchResultType` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:173-176]
- `SearchResultType` (class) component `SearchResultType [class]` (`2d21d509-53bd-523b-a138-c3ba4ee3a196`) lines 178-196 [crates/gwiki/src/output.rs:178-196]
  - Signature: `impl SearchResultType {`
  - Purpose: 'SearchResultType' classifies a vault-relative wiki page path as 'Code' when its normalized string form starts with 'code/files/', otherwise 'Wiki', and exposes 'is_code()' as a predicate for the 'Code' variant. [crates/gwiki/src/output.rs:178-196]
- `SearchResultType.from_wiki_page` (method) component `SearchResultType.from_wiki_page [method]` (`05cf896a-a88e-5786-9022-3d3c7bd64748`) lines 181-191 [crates/gwiki/src/output.rs:181-191]
  - Signature: `pub fn from_wiki_page(path: &Path) -> Self {`
  - Purpose: Returns 'Self::Code' when the provided path, after lossy UTF-8 conversion and '\' to '/' normalization, starts with 'code/files/'; otherwise it returns 'Self::Wiki'. [crates/gwiki/src/output.rs:181-191]
- `SearchResultType.is_code` (method) component `SearchResultType.is_code [method]` (`4b7096c7-e7eb-55bb-be0c-f9f134bbb17d`) lines 193-195 [crates/gwiki/src/output.rs:193-195]
  - Signature: `pub fn is_code(self) -> bool {`
  - Purpose: Returns 'true' if 'self' is the 'Self::Code' variant, and 'false' for all other variants. [crates/gwiki/src/output.rs:193-195]
- `SearchResultOutput` (class) component `SearchResultOutput [class]` (`272db8a5-f863-539a-888d-b9fd020656be`) lines 199-209 [crates/gwiki/src/output.rs:199-209]
  - Signature: `pub struct SearchResultOutput {`
  - Purpose: 'SearchResultOutput' is a search-hit record that carries the result’s optional title, fusion key, wiki and source paths, result type, snippet, relevance score, contributing source identifiers, and per-source explanation data. [crates/gwiki/src/output.rs:199-209]
- `AskAiOutput` (class) component `AskAiOutput [class]` (`c7209590-baf1-5e7f-96ae-80bc5d59b0de`) lines 212-219 [crates/gwiki/src/output.rs:212-219]
  - Signature: `pub struct AskAiOutput {`
  - Purpose: 'AskAiOutput' is a Rust output record that captures whether an AI request was issued, the requested mode and route, the resulting status, and optional model and error information. [crates/gwiki/src/output.rs:212-219]
- `AskSynthesisOutput` (class) component `AskSynthesisOutput [class]` (`be1b8eaa-0246-553b-ac9d-192b3b392692`) lines 222-226 [crates/gwiki/src/output.rs:222-226]
  - Signature: `pub struct AskSynthesisOutput {`
  - Purpose: 'AskSynthesisOutput' is a Rust struct representing a synthesized response payload, with the answer text, an optional model identifier, and a 'AskCitationCheckOutput' citation-check result. [crates/gwiki/src/output.rs:222-226]
- `AskCitationCheckOutput` (class) component `AskCitationCheckOutput [class]` (`130a5e53-431c-5e3d-bed1-1a847f1a09f4`) lines 233-237 [crates/gwiki/src/output.rs:233-237]
  - Signature: `pub struct AskCitationCheckOutput {`
  - Purpose: 'AskCitationCheckOutput' is a result struct that reports the citation-check 'status', the number of claims evaluated in 'checked_claims', and the unsupported claim texts in 'unsupported_claims'. [crates/gwiki/src/output.rs:233-237]
- `SearchSourceExplanationOutput` (class) component `SearchSourceExplanationOutput [class]` (`0625d05a-3491-5a15-a850-e321c55ea4da`) lines 240-244 [crates/gwiki/src/output.rs:240-244]
  - Signature: `pub struct SearchSourceExplanationOutput {`
  - Purpose: 'SearchSourceExplanationOutput' is a Rust struct that captures a search source identifier plus its 'rank' and 'score' for explaining or reporting search result ordering. [crates/gwiki/src/output.rs:240-244]
- `QueryOutput` (class) component `QueryOutput [class]` (`7c3fdc92-ed32-5fe5-b278-bb1574490453`) lines 247-253 [crates/gwiki/src/output.rs:247-253]
  - Signature: `pub struct QueryOutput {`
  - Purpose: 'QueryOutput' is a data struct that captures the result of a scoped query operation, including the fixed command name, the 'ScopeIdentity', the original query string, the generated answer, and a list of supporting 'QueryCitation's. [crates/gwiki/src/output.rs:247-253]
- `QueryOutput` (class) component `QueryOutput [class]` (`a60b07e1-181f-53f4-a33c-e06b8afff1f2`) lines 255-270 [crates/gwiki/src/output.rs:255-270]
  - Signature: `impl QueryOutput {`
  - Purpose: 'QueryOutput' is a Rust constructor/response type that produces a 'query' command output containing the scope, query string, answer string, and associated citations. [crates/gwiki/src/output.rs:255-270]
- `QueryOutput.answered` (method) component `QueryOutput.answered [method]` (`96326e52-aa2c-5d38-b41d-d5e6f24218bd`) lines 256-269 [crates/gwiki/src/output.rs:256-269]
  - Signature: `pub fn answered(`
  - Purpose: Constructs and returns a 'Self' value for a '"query"' command by storing the provided 'scope', converting 'query' and 'answer' into 'String's, and attaching the given 'citations' vector. [crates/gwiki/src/output.rs:256-269]
- `QueryCitation` (class) component `QueryCitation [class]` (`f884f3ad-ba29-5120-9073-26a1f92094a1`) lines 273-278 [crates/gwiki/src/output.rs:273-278]
  - Signature: `pub struct QueryCitation {`
  - Purpose: 'QueryCitation' is a Rust struct that stores a citation’s source file path, associated wiki page path, and optional title and line-reference metadata. [crates/gwiki/src/output.rs:273-278]
- `AuditOutput` (class) component `AuditOutput [class]` (`03c8d9fa-3f1c-56e7-ab24-9bd96a985e1f`) lines 281-287 [crates/gwiki/src/output.rs:281-287]
  - Signature: `pub struct AuditOutput {`
  - Purpose: 'AuditOutput' is a Rust struct that captures an audit command identifier, the scoped target being audited, the count of unsupported claims found, an optional report file path, and the list of source paths examined. [crates/gwiki/src/output.rs:281-287]
- `AuditOutput` (class) component `AuditOutput [class]` (`60039241-e50a-5696-ae80-258f161cdea2`) lines 289-304 [crates/gwiki/src/output.rs:289-304]
  - Signature: `impl AuditOutput {`
  - Purpose: 'AuditOutput' is a constructor-only Rust wrapper that builds an audit command output value with a fixed 'command' of '"audit"' and stores the provided 'scope', 'unsupported_claim_count', optional 'report_path', and 'source_paths' into the returned struct. [crates/gwiki/src/output.rs:289-304]
- `AuditOutput.new` (method) component `AuditOutput.new [method]` (`b6f17b21-3774-521e-9b21-b220d398b64c`) lines 290-303 [crates/gwiki/src/output.rs:290-303]
  - Signature: `pub fn new(`
  - Purpose: Constructs and returns a new instance with 'command' fixed to '"audit"' and the provided 'scope', 'unsupported_claim_count', 'report_path', and 'source_paths' fields. [crates/gwiki/src/output.rs:290-303]
- `render_query_text` (function) component `render_query_text [function]` (`5a22ce47-3064-5f85-bb9b-91301a64d7de`) lines 306-333 [crates/gwiki/src/output.rs:306-333]
  - Signature: `pub fn render_query_text(output: &QueryOutput) -> String {`
  - Purpose: Formats a 'QueryOutput' into a plain-text report containing the scope, question, answer, and either 'Citations: none' or a per-citation list with source path, wiki page, optional title, and optional lines. [crates/gwiki/src/output.rs:306-333]
- `json_output_is_stable` (function) component `json_output_is_stable [function]` (`3a248764-4294-59bc-92d6-c63528ecc703`) lines 342-434 [crates/gwiki/src/output.rs:342-434]
  - Signature: `fn json_output_is_stable() {`
  - Purpose: Verifies that 'SearchOutput', 'QueryOutput', and 'AuditOutput' serialize to the expected stable JSON shape and field values using 'serde_json::to_value' equality assertions. [crates/gwiki/src/output.rs:342-434]
- `search_output_derives_code_citations_from_code_hits_only` (function) component `search_output_derives_code_citations_from_code_hits_only [function]` (`e31aae4b-80a9-52d2-b00d-300b084bc2e0`) lines 437-476 [crates/gwiki/src/output.rs:437-476]
  - Signature: `fn search_output_derives_code_citations_from_code_hits_only() {`
  - Purpose: Verifies that 'SearchOutput::new' derives 'code_citations' exclusively from code search hits, deduplicating duplicate code hits and ignoring wiki hits. [crates/gwiki/src/output.rs:437-476]
- `query_output_includes_citations` (function) component `query_output_includes_citations [function]` (`dcb5d888-c149-58e5-89b9-41140c53b981`) lines 479-505 [crates/gwiki/src/output.rs:479-505]
  - Signature: `fn query_output_includes_citations() {`
  - Purpose: Verifies that an answered 'QueryOutput' preserves citation paths and that 'render_query_text' includes both the source and wiki citation references in its output. [crates/gwiki/src/output.rs:479-505]

