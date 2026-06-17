---
title: crates/gwiki/src/output.rs
type: code_file
provenance:
- file: crates/gwiki/src/output.rs
  ranges:
  - 10-13
  - 16-19
  - 22-27
  - 33-35
  - 39-41
  - 44-53
  - 55-61
  - 63-66
  - 68-70
  - 73-81
  - 84-101
  - 107-125
  - 131-151
  - 155-159
  - 162-168
  - 173-176
  - 181-191
  - 193-195
  - 199-209
  - 212-219
  - 222-226
  - 233-237
  - 240-244
  - 247-253
  - 256-269
  - 273-278
  - 281-287
  - 290-303
  - 306-333
  - 342-434
  - 437-476
  - 479-505
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/output.rs:10-13](crates/gwiki/src/output.rs#L10-L13), [crates/gwiki/src/output.rs:16-19](crates/gwiki/src/output.rs#L16-L19), [crates/gwiki/src/output.rs:22-27](crates/gwiki/src/output.rs#L22-L27), [crates/gwiki/src/output.rs:33-35](crates/gwiki/src/output.rs#L33-L35), [crates/gwiki/src/output.rs:39-41](crates/gwiki/src/output.rs#L39-L41), [crates/gwiki/src/output.rs:44-53](crates/gwiki/src/output.rs#L44-L53), [crates/gwiki/src/output.rs:55-61](crates/gwiki/src/output.rs#L55-L61), [crates/gwiki/src/output.rs:63-66](crates/gwiki/src/output.rs#L63-L66), [crates/gwiki/src/output.rs:68-70](crates/gwiki/src/output.rs#L68-L70), [crates/gwiki/src/output.rs:73-81](crates/gwiki/src/output.rs#L73-L81), [crates/gwiki/src/output.rs:84-101](crates/gwiki/src/output.rs#L84-L101), [crates/gwiki/src/output.rs:107-125](crates/gwiki/src/output.rs#L107-L125), [crates/gwiki/src/output.rs:131-151](crates/gwiki/src/output.rs#L131-L151), [crates/gwiki/src/output.rs:155-159](crates/gwiki/src/output.rs#L155-L159), [crates/gwiki/src/output.rs:162-168](crates/gwiki/src/output.rs#L162-L168), [crates/gwiki/src/output.rs:173-176](crates/gwiki/src/output.rs#L173-L176), [crates/gwiki/src/output.rs:181-191](crates/gwiki/src/output.rs#L181-L191), [crates/gwiki/src/output.rs:193-195](crates/gwiki/src/output.rs#L193-L195), [crates/gwiki/src/output.rs:199-209](crates/gwiki/src/output.rs#L199-L209), [crates/gwiki/src/output.rs:212-219](crates/gwiki/src/output.rs#L212-L219), [crates/gwiki/src/output.rs:222-226](crates/gwiki/src/output.rs#L222-L226), [crates/gwiki/src/output.rs:233-237](crates/gwiki/src/output.rs#L233-L237), [crates/gwiki/src/output.rs:240-244](crates/gwiki/src/output.rs#L240-L244), [crates/gwiki/src/output.rs:247-253](crates/gwiki/src/output.rs#L247-L253), [crates/gwiki/src/output.rs:256-269](crates/gwiki/src/output.rs#L256-L269), [crates/gwiki/src/output.rs:273-278](crates/gwiki/src/output.rs#L273-L278), [crates/gwiki/src/output.rs:281-287](crates/gwiki/src/output.rs#L281-L287), [crates/gwiki/src/output.rs:290-303](crates/gwiki/src/output.rs#L290-L303), [crates/gwiki/src/output.rs:306-333](crates/gwiki/src/output.rs#L306-L333), [crates/gwiki/src/output.rs:342-434](crates/gwiki/src/output.rs#L342-L434), [crates/gwiki/src/output.rs:437-476](crates/gwiki/src/output.rs#L437-L476), [crates/gwiki/src/output.rs:479-505](crates/gwiki/src/output.rs#L479-L505)

</details>

# crates/gwiki/src/output.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Formats and prints `gwiki` command results in either JSON or plain text, while providing a shared output model for search, ask, query, and audit flows. `Format`, `OutputError`, `print_result`, `print_json`, `print_text`, and `print_status` handle rendering and I/O error conversion; the various `*Output` structs package each command’s response shape, and helpers like `SearchOutput::new`, `AuditOutput::new`, `QueryOutput::answered`, `code_citations_from_results`, `render_query_text`, and `SearchResultType` derive consistent citation, result-type, and display data from underlying wiki hits. The tests at the end lock down JSON stability and verify that citations are only pulled from code hits and are included in query output.
[crates/gwiki/src/output.rs:10-13]
[crates/gwiki/src/output.rs:16-19]
[crates/gwiki/src/output.rs:22-27]
[crates/gwiki/src/output.rs:33-35]
[crates/gwiki/src/output.rs:39-41]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Format` | type | `pub enum Format {` | `Format [type]` | `d5d3dd3b-a336-5b1f-be7f-6ae6ee7afdc4` | 10-13 [crates/gwiki/src/output.rs:10-13] | Indexed type `Format` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:10-13] |
| `OutputError` | type | `pub enum OutputError {` | `OutputError [type]` | `13586740-fc38-5319-87dc-b3218979de76` | 16-19 [crates/gwiki/src/output.rs:16-19] | Indexed type `OutputError` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:16-19] |
| `OutputError::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `OutputError::fmt [method]` | `e6931e63-4653-595e-ac83-e00ef62e8bf0` | 22-27 [crates/gwiki/src/output.rs:22-27] | Indexed method `OutputError::fmt` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:22-27] |
| `OutputError::from` | method | `fn from(error: std::io::Error) -> Self {` | `OutputError::from [method]` | `83f0156d-af88-5c50-a1dd-c732d705e896` | 33-35 [crates/gwiki/src/output.rs:33-35] | Indexed method `OutputError::from` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:33-35] |
| `OutputError::from` | method | `fn from(error: serde_json::Error) -> Self {` | `OutputError::from [method]` | `3c510a50-1357-5e61-9ff7-f925d5390f98` | 39-41 [crates/gwiki/src/output.rs:39-41] | Indexed method `OutputError::from` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:39-41] |
| `print_result` | function | `pub fn print_result(` | `print_result [function]` | `ed965b4a-347d-50a6-9a8f-edef908d335e` | 44-53 [crates/gwiki/src/output.rs:44-53] | Indexed function `print_result` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:44-53] |
| `print_json` | function | `pub fn print_json<T: serde::Serialize + ?Sized>(` | `print_json [function]` | `990bf29c-71d6-5407-8fef-adc1101fcb8f` | 55-61 [crates/gwiki/src/output.rs:55-61] | Indexed function `print_json` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:55-61] |
| `print_text` | function | `pub fn print_text(writer: &mut impl Write, text: &str) -> Result<(), OutputError> {` | `print_text [function]` | `908f89c2-0e58-5d7f-8afd-6ec53611b77a` | 63-66 [crates/gwiki/src/output.rs:63-66] | Indexed function `print_text` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:63-66] |
| `print_status` | function | `pub fn print_status(message: &str) {` | `print_status [function]` | `64f93a82-188b-5c8a-a5ce-32dea3bde8b6` | 68-70 [crates/gwiki/src/output.rs:68-70] | Indexed function `print_status` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:68-70] |
| `SearchOutput` | class | `pub struct SearchOutput {` | `SearchOutput [class]` | `cbfd0ce3-f0de-57cc-9358-40d405770a4d` | 73-81 [crates/gwiki/src/output.rs:73-81] | Indexed class `SearchOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:73-81] |
| `SearchOutput::new` | method | `pub fn new(` | `SearchOutput::new [method]` | `b09db649-43b7-51e5-ad12-88fddc71aa69` | 84-101 [crates/gwiki/src/output.rs:84-101] | Indexed method `SearchOutput::new` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:84-101] |
| `code_citations_from_results` | function | `pub fn code_citations_from_results(results: &[SearchResultOutput]) -> Vec<CodeCitationOutput> {` | `code_citations_from_results [function]` | `c27e36c0-ade6-5163-8505-0cd0576fb6f9` | 107-125 [crates/gwiki/src/output.rs:107-125] | Indexed function `code_citations_from_results` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:107-125] |
| `AskOutput` | class | `pub struct AskOutput {` | `AskOutput [class]` | `578c4b1f-7d89-5d39-970f-7954da1f98fc` | 131-151 [crates/gwiki/src/output.rs:131-151] | Indexed class `AskOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:131-151] |
| `AskEvidenceOutput` | class | `pub struct AskEvidenceOutput {` | `AskEvidenceOutput [class]` | `d24c6fb4-7c6a-56d7-a802-ed9e6b5fe5a2` | 155-159 [crates/gwiki/src/output.rs:155-159] | Indexed class `AskEvidenceOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:155-159] |
| `CodeCitationOutput` | class | `pub struct CodeCitationOutput {` | `CodeCitationOutput [class]` | `d11dde81-b751-5642-81e2-e6fc83b25f65` | 162-168 [crates/gwiki/src/output.rs:162-168] | Indexed class `CodeCitationOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:162-168] |
| `SearchResultType` | type | `pub enum SearchResultType {` | `SearchResultType [type]` | `a3d31626-3533-557d-9328-c8bd13050219` | 173-176 [crates/gwiki/src/output.rs:173-176] | Indexed type `SearchResultType` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:173-176] |
| `SearchResultType::from_wiki_page` | method | `pub fn from_wiki_page(path: &Path) -> Self {` | `SearchResultType::from_wiki_page [method]` | `05cf896a-a88e-5786-9022-3d3c7bd64748` | 181-191 [crates/gwiki/src/output.rs:181-191] | Indexed method `SearchResultType::from_wiki_page` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:181-191] |
| `SearchResultType::is_code` | method | `pub fn is_code(self) -> bool {` | `SearchResultType::is_code [method]` | `4b7096c7-e7eb-55bb-be0c-f9f134bbb17d` | 193-195 [crates/gwiki/src/output.rs:193-195] | Indexed method `SearchResultType::is_code` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:193-195] |
| `SearchResultOutput` | class | `pub struct SearchResultOutput {` | `SearchResultOutput [class]` | `272db8a5-f863-539a-888d-b9fd020656be` | 199-209 [crates/gwiki/src/output.rs:199-209] | Indexed class `SearchResultOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:199-209] |
| `AskAiOutput` | class | `pub struct AskAiOutput {` | `AskAiOutput [class]` | `c7209590-baf1-5e7f-96ae-80bc5d59b0de` | 212-219 [crates/gwiki/src/output.rs:212-219] | Indexed class `AskAiOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:212-219] |
| `AskSynthesisOutput` | class | `pub struct AskSynthesisOutput {` | `AskSynthesisOutput [class]` | `be1b8eaa-0246-553b-ac9d-192b3b392692` | 222-226 [crates/gwiki/src/output.rs:222-226] | Indexed class `AskSynthesisOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:222-226] |
| `AskCitationCheckOutput` | class | `pub struct AskCitationCheckOutput {` | `AskCitationCheckOutput [class]` | `130a5e53-431c-5e3d-bed1-1a847f1a09f4` | 233-237 [crates/gwiki/src/output.rs:233-237] | Indexed class `AskCitationCheckOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:233-237] |
| `SearchSourceExplanationOutput` | class | `pub struct SearchSourceExplanationOutput {` | `SearchSourceExplanationOutput [class]` | `0625d05a-3491-5a15-a850-e321c55ea4da` | 240-244 [crates/gwiki/src/output.rs:240-244] | Indexed class `SearchSourceExplanationOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:240-244] |
| `QueryOutput` | class | `pub struct QueryOutput {` | `QueryOutput [class]` | `7c3fdc92-ed32-5fe5-b278-bb1574490453` | 247-253 [crates/gwiki/src/output.rs:247-253] | Indexed class `QueryOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:247-253] |
| `QueryOutput::answered` | method | `pub fn answered(` | `QueryOutput::answered [method]` | `96326e52-aa2c-5d38-b41d-d5e6f24218bd` | 256-269 [crates/gwiki/src/output.rs:256-269] | Indexed method `QueryOutput::answered` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:256-269] |
| `QueryCitation` | class | `pub struct QueryCitation {` | `QueryCitation [class]` | `f884f3ad-ba29-5120-9073-26a1f92094a1` | 273-278 [crates/gwiki/src/output.rs:273-278] | Indexed class `QueryCitation` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:273-278] |
| `AuditOutput` | class | `pub struct AuditOutput {` | `AuditOutput [class]` | `03c8d9fa-3f1c-56e7-ab24-9bd96a985e1f` | 281-287 [crates/gwiki/src/output.rs:281-287] | Indexed class `AuditOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:281-287] |
| `AuditOutput::new` | method | `pub fn new(` | `AuditOutput::new [method]` | `b6f17b21-3774-521e-9b21-b220d398b64c` | 290-303 [crates/gwiki/src/output.rs:290-303] | Indexed method `AuditOutput::new` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:290-303] |
| `render_query_text` | function | `pub fn render_query_text(output: &QueryOutput) -> String {` | `render_query_text [function]` | `5a22ce47-3064-5f85-bb9b-91301a64d7de` | 306-333 [crates/gwiki/src/output.rs:306-333] | Indexed function `render_query_text` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:306-333] |
| `json_output_is_stable` | function | `fn json_output_is_stable() {` | `json_output_is_stable [function]` | `3a248764-4294-59bc-92d6-c63528ecc703` | 342-434 [crates/gwiki/src/output.rs:342-434] | Indexed function `json_output_is_stable` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:342-434] |
| `search_output_derives_code_citations_from_code_hits_only` | function | `fn search_output_derives_code_citations_from_code_hits_only() {` | `search_output_derives_code_citations_from_code_hits_only [function]` | `e31aae4b-80a9-52d2-b00d-300b084bc2e0` | 437-476 [crates/gwiki/src/output.rs:437-476] | Indexed function `search_output_derives_code_citations_from_code_hits_only` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:437-476] |
| `query_output_includes_citations` | function | `fn query_output_includes_citations() {` | `query_output_includes_citations [function]` | `dcb5d888-c149-58e5-89b9-41140c53b981` | 479-505 [crates/gwiki/src/output.rs:479-505] | Indexed function `query_output_includes_citations` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:479-505] |
