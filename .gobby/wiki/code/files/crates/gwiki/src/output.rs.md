---
title: crates/gwiki/src/output.rs
type: code_file
provenance:
- file: crates/gwiki/src/output.rs
  ranges:
  - 10-13
  - 16-19
  - 21-28
  - 22-27
  - '30'
  - 32-36
  - 33-35
  - 38-42
  - 39-41
  - 44-53
  - 55-61
  - 63-66
  - 68-70
  - 73-80
  - 82-99
  - 83-98
  - 102-124
  - 127-135
  - 138-144
  - 149-152
  - 154-172
  - 157-167
  - 169-171
  - 175-185
  - 188-192
  - 195-202
  - 205-208
  - 211-215
  - 218-224
  - 226-241
  - 227-240
  - 244-249
  - 252-258
  - 260-275
  - 261-274
  - 277-304
  - 313-404
  - 407-433
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/output.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/output.rs` exposes 38 indexed API symbols.
[crates/gwiki/src/output.rs:10-13]
[crates/gwiki/src/output.rs:16-19]
[crates/gwiki/src/output.rs:21-28]
[crates/gwiki/src/output.rs:22-27]
[crates/gwiki/src/output.rs:30]
[crates/gwiki/src/output.rs:32-36]
[crates/gwiki/src/output.rs:33-35]
[crates/gwiki/src/output.rs:38-42]
[crates/gwiki/src/output.rs:39-41]
[crates/gwiki/src/output.rs:44-53]
[crates/gwiki/src/output.rs:55-61]
[crates/gwiki/src/output.rs:63-66]
[crates/gwiki/src/output.rs:68-70]
[crates/gwiki/src/output.rs:73-80]
[crates/gwiki/src/output.rs:82-99]
[crates/gwiki/src/output.rs:83-98]
[crates/gwiki/src/output.rs:102-124]
[crates/gwiki/src/output.rs:127-135]
[crates/gwiki/src/output.rs:138-144]
[crates/gwiki/src/output.rs:149-152]
[crates/gwiki/src/output.rs:154-172]
[crates/gwiki/src/output.rs:157-167]
[crates/gwiki/src/output.rs:169-171]
[crates/gwiki/src/output.rs:175-185]
[crates/gwiki/src/output.rs:188-192]
[crates/gwiki/src/output.rs:195-202]
[crates/gwiki/src/output.rs:205-208]
[crates/gwiki/src/output.rs:211-215]
[crates/gwiki/src/output.rs:218-224]
[crates/gwiki/src/output.rs:226-241]
[crates/gwiki/src/output.rs:227-240]
[crates/gwiki/src/output.rs:244-249]
[crates/gwiki/src/output.rs:252-258]
[crates/gwiki/src/output.rs:260-275]
[crates/gwiki/src/output.rs:261-274]
[crates/gwiki/src/output.rs:277-304]
[crates/gwiki/src/output.rs:313-404]
[crates/gwiki/src/output.rs:407-433]

## API Symbols

- `Format` (type) component `Format [type]` (`d5d3dd3b-a336-5b1f-be7f-6ae6ee7afdc4`) lines 10-13 [crates/gwiki/src/output.rs:10-13]
  - Signature: `pub enum Format {`
  - Purpose: Indexed type `Format` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:10-13]
- `OutputError` (type) component `OutputError [type]` (`13586740-fc38-5319-87dc-b3218979de76`) lines 16-19 [crates/gwiki/src/output.rs:16-19]
  - Signature: `pub enum OutputError {`
  - Purpose: Indexed type `OutputError` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:16-19]
- `OutputError` (class) component `OutputError [class]` (`fba419c8-3db0-51f2-960d-1fc61da1abc2`) lines 21-28 [crates/gwiki/src/output.rs:21-28]
  - Signature: `impl fmt::Display for OutputError {`
  - Purpose: Indexed class `OutputError` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:21-28]
- `OutputError.fmt` (method) component `OutputError.fmt [method]` (`e6931e63-4653-595e-ac83-e00ef62e8bf0`) lines 22-27 [crates/gwiki/src/output.rs:22-27]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Indexed method `OutputError.fmt` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:22-27]
- `OutputError` (class) component `OutputError [class]` (`c106b6ed-b048-5652-9f1d-7ce9f21943bc`) lines 30-30 [crates/gwiki/src/output.rs:30]
  - Signature: `impl std::error::Error for OutputError {}`
  - Purpose: Indexed class `OutputError` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:30]
- `OutputError` (class) component `OutputError [class]` (`18149cda-931c-5c80-8de6-87278a3466b9`) lines 32-36 [crates/gwiki/src/output.rs:32-36]
  - Signature: `impl From<std::io::Error> for OutputError {`
  - Purpose: Indexed class `OutputError` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:32-36]
- `OutputError.from` (method) component `OutputError.from [method]` (`83f0156d-af88-5c50-a1dd-c732d705e896`) lines 33-35 [crates/gwiki/src/output.rs:33-35]
  - Signature: `fn from(error: std::io::Error) -> Self {`
  - Purpose: Indexed method `OutputError.from` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:33-35]
- `OutputError` (class) component `OutputError [class]` (`638ca648-517f-5c59-aa91-1ce42232078d`) lines 38-42 [crates/gwiki/src/output.rs:38-42]
  - Signature: `impl From<serde_json::Error> for OutputError {`
  - Purpose: Indexed class `OutputError` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:38-42]
- `OutputError.from` (method) component `OutputError.from [method]` (`3c510a50-1357-5e61-9ff7-f925d5390f98`) lines 39-41 [crates/gwiki/src/output.rs:39-41]
  - Signature: `fn from(error: serde_json::Error) -> Self {`
  - Purpose: Indexed method `OutputError.from` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:39-41]
- `print_result` (function) component `print_result [function]` (`ed965b4a-347d-50a6-9a8f-edef908d335e`) lines 44-53 [crates/gwiki/src/output.rs:44-53]
  - Signature: `pub fn print_result(`
  - Purpose: Indexed function `print_result` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:44-53]
- `print_json` (function) component `print_json [function]` (`990bf29c-71d6-5407-8fef-adc1101fcb8f`) lines 55-61 [crates/gwiki/src/output.rs:55-61]
  - Signature: `pub fn print_json<T: serde::Serialize + ?Sized>(`
  - Purpose: Indexed function `print_json` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:55-61]
- `print_text` (function) component `print_text [function]` (`908f89c2-0e58-5d7f-8afd-6ec53611b77a`) lines 63-66 [crates/gwiki/src/output.rs:63-66]
  - Signature: `pub fn print_text(writer: &mut impl Write, text: &str) -> Result<(), OutputError> {`
  - Purpose: Indexed function `print_text` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:63-66]
- `print_status` (function) component `print_status [function]` (`64f93a82-188b-5c8a-a5ce-32dea3bde8b6`) lines 68-70 [crates/gwiki/src/output.rs:68-70]
  - Signature: `pub fn print_status(message: &str) {`
  - Purpose: Indexed function `print_status` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:68-70]
- `SearchOutput` (class) component `SearchOutput [class]` (`cbfd0ce3-f0de-57cc-9358-40d405770a4d`) lines 73-80 [crates/gwiki/src/output.rs:73-80]
  - Signature: `pub struct SearchOutput {`
  - Purpose: Indexed class `SearchOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:73-80]
- `SearchOutput` (class) component `SearchOutput [class]` (`7c61b245-13df-5635-9d50-a4d55aa1e6e4`) lines 82-99 [crates/gwiki/src/output.rs:82-99]
  - Signature: `impl SearchOutput {`
  - Purpose: Indexed class `SearchOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:82-99]
- `SearchOutput.new` (method) component `SearchOutput.new [method]` (`f4a4ca49-cb4b-5f75-9401-52950f96bcd2`) lines 83-98 [crates/gwiki/src/output.rs:83-98]
  - Signature: `pub fn new(`
  - Purpose: Indexed method `SearchOutput.new` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:83-98]
- `AskOutput` (class) component `AskOutput [class]` (`9a65ff4b-3e08-5689-a255-8f9b629e8c3d`) lines 102-124 [crates/gwiki/src/output.rs:102-124]
  - Signature: `pub struct AskOutput {`
  - Purpose: Indexed class `AskOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:102-124]
- `AskCodeEdgeOutput` (class) component `AskCodeEdgeOutput [class]` (`a9934a7c-27d9-5fbc-a67e-e6a339706c7e`) lines 127-135 [crates/gwiki/src/output.rs:127-135]
  - Signature: `pub struct AskCodeEdgeOutput {`
  - Purpose: Indexed class `AskCodeEdgeOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:127-135]
- `AskCodeCitationOutput` (class) component `AskCodeCitationOutput [class]` (`abda8ed8-ac86-5484-88a6-f3b55a849b1b`) lines 138-144 [crates/gwiki/src/output.rs:138-144]
  - Signature: `pub struct AskCodeCitationOutput {`
  - Purpose: Indexed class `AskCodeCitationOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:138-144]
- `SearchResultType` (type) component `SearchResultType [type]` (`ff38e03a-1a0d-5e43-9e86-1d1910739bbb`) lines 149-152 [crates/gwiki/src/output.rs:149-152]
  - Signature: `pub enum SearchResultType {`
  - Purpose: Indexed type `SearchResultType` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:149-152]
- `SearchResultType` (class) component `SearchResultType [class]` (`95e11036-1a71-5c89-8e8a-b54f90e4186d`) lines 154-172 [crates/gwiki/src/output.rs:154-172]
  - Signature: `impl SearchResultType {`
  - Purpose: Indexed class `SearchResultType` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:154-172]
- `SearchResultType.from_wiki_page` (method) component `SearchResultType.from_wiki_page [method]` (`7d05c4dc-3b0f-5638-98ec-c3bb7246c857`) lines 157-167 [crates/gwiki/src/output.rs:157-167]
  - Signature: `pub fn from_wiki_page(path: &Path) -> Self {`
  - Purpose: Indexed method `SearchResultType.from_wiki_page` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:157-167]
- `SearchResultType.is_code` (method) component `SearchResultType.is_code [method]` (`0a38d7a3-7c89-5990-a589-0fdebc958ea8`) lines 169-171 [crates/gwiki/src/output.rs:169-171]
  - Signature: `pub fn is_code(self) -> bool {`
  - Purpose: Indexed method `SearchResultType.is_code` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:169-171]
- `SearchResultOutput` (class) component `SearchResultOutput [class]` (`cdd9f244-d679-522c-b389-e2334ea9b9a8`) lines 175-185 [crates/gwiki/src/output.rs:175-185]
  - Signature: `pub struct SearchResultOutput {`
  - Purpose: Indexed class `SearchResultOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:175-185]
- `AskRelatedPageOutput` (class) component `AskRelatedPageOutput [class]` (`9f21297d-24f7-5a98-9914-10c790180afa`) lines 188-192 [crates/gwiki/src/output.rs:188-192]
  - Signature: `pub struct AskRelatedPageOutput {`
  - Purpose: Indexed class `AskRelatedPageOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:188-192]
- `AskAiOutput` (class) component `AskAiOutput [class]` (`59dfbeff-2c1c-5c9e-b54b-239ca0beca26`) lines 195-202 [crates/gwiki/src/output.rs:195-202]
  - Signature: `pub struct AskAiOutput {`
  - Purpose: Indexed class `AskAiOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:195-202]
- `AskSynthesisOutput` (class) component `AskSynthesisOutput [class]` (`5b8a0128-128d-5c63-8656-37b08698a4d0`) lines 205-208 [crates/gwiki/src/output.rs:205-208]
  - Signature: `pub struct AskSynthesisOutput {`
  - Purpose: Indexed class `AskSynthesisOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:205-208]
- `SearchSourceExplanationOutput` (class) component `SearchSourceExplanationOutput [class]` (`fe2f3ca2-6b6b-5efd-a547-82fea8569ac8`) lines 211-215 [crates/gwiki/src/output.rs:211-215]
  - Signature: `pub struct SearchSourceExplanationOutput {`
  - Purpose: Indexed class `SearchSourceExplanationOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:211-215]
- `QueryOutput` (class) component `QueryOutput [class]` (`4d8ac4c8-9545-5cfd-ae9e-519ddf37da1d`) lines 218-224 [crates/gwiki/src/output.rs:218-224]
  - Signature: `pub struct QueryOutput {`
  - Purpose: Indexed class `QueryOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:218-224]
- `QueryOutput` (class) component `QueryOutput [class]` (`7ab4dbb9-698b-503a-9980-8d1076f32076`) lines 226-241 [crates/gwiki/src/output.rs:226-241]
  - Signature: `impl QueryOutput {`
  - Purpose: Indexed class `QueryOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:226-241]
- `QueryOutput.answered` (method) component `QueryOutput.answered [method]` (`a4f85b17-5979-59f0-8749-6791acd2deaa`) lines 227-240 [crates/gwiki/src/output.rs:227-240]
  - Signature: `pub fn answered(`
  - Purpose: Indexed method `QueryOutput.answered` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:227-240]
- `QueryCitation` (class) component `QueryCitation [class]` (`bb79c867-01ce-56cc-a399-e524253b9e5a`) lines 244-249 [crates/gwiki/src/output.rs:244-249]
  - Signature: `pub struct QueryCitation {`
  - Purpose: Indexed class `QueryCitation` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:244-249]
- `AuditOutput` (class) component `AuditOutput [class]` (`fc0b2783-087d-5355-92c1-60c5ac6f0272`) lines 252-258 [crates/gwiki/src/output.rs:252-258]
  - Signature: `pub struct AuditOutput {`
  - Purpose: Indexed class `AuditOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:252-258]
- `AuditOutput` (class) component `AuditOutput [class]` (`e4ddb036-789e-58cd-8a4e-0cee12f01dd1`) lines 260-275 [crates/gwiki/src/output.rs:260-275]
  - Signature: `impl AuditOutput {`
  - Purpose: Indexed class `AuditOutput` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:260-275]
- `AuditOutput.new` (method) component `AuditOutput.new [method]` (`e272b6bd-4dae-5d79-9986-81271e4b94ae`) lines 261-274 [crates/gwiki/src/output.rs:261-274]
  - Signature: `pub fn new(`
  - Purpose: Indexed method `AuditOutput.new` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:261-274]
- `render_query_text` (function) component `render_query_text [function]` (`ffd39b42-922d-5222-ab08-7e9bee94f988`) lines 277-304 [crates/gwiki/src/output.rs:277-304]
  - Signature: `pub fn render_query_text(output: &QueryOutput) -> String {`
  - Purpose: Indexed function `render_query_text` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:277-304]
- `json_output_is_stable` (function) component `json_output_is_stable [function]` (`56111543-346c-50d5-98e5-e5bcb28e2792`) lines 313-404 [crates/gwiki/src/output.rs:313-404]
  - Signature: `fn json_output_is_stable() {`
  - Purpose: Indexed function `json_output_is_stable` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:313-404]
- `query_output_includes_citations` (function) component `query_output_includes_citations [function]` (`6fab457d-0f7e-579a-a597-99c8437c79d9`) lines 407-433 [crates/gwiki/src/output.rs:407-433]
  - Signature: `fn query_output_includes_citations() {`
  - Purpose: Indexed function `query_output_includes_citations` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:407-433]

