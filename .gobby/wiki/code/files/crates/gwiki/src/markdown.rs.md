---
title: crates/gwiki/src/markdown.rs
type: code_file
provenance:
- file: crates/gwiki/src/markdown.rs
  ranges:
  - 11-19
  - 22-29
  - 32-35
  - 38-41
  - 43-55
  - 57-68
  - 70-77
  - 71-76
  - '79'
  - 81-85
  - 82-84
  - 87-91
  - 88-90
  - 93-116
  - 118-129
  - 131-184
  - 186-205
  - 207-229
  - 231-273
  - 275-295
  - 303-352
  - 355-367
  - 370-386
  - 389-398
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/markdown.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/markdown.rs` exposes 24 indexed API symbols.
[crates/gwiki/src/markdown.rs:11-19]
[crates/gwiki/src/markdown.rs:22-29]
[crates/gwiki/src/markdown.rs:32-35]
[crates/gwiki/src/markdown.rs:38-41]
[crates/gwiki/src/markdown.rs:43-55]

## API Symbols

- `MarkdownHeading` (class) component `MarkdownHeading [class]` (`f8871d89-a4b9-577d-b70c-8fe152ce549d`) lines 11-19 [crates/gwiki/src/markdown.rs:11-19]
  - Signature: `pub struct MarkdownHeading {`
  - Purpose: Indexed class `MarkdownHeading` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:11-19]
- `MarkdownDomainRecord` (class) component `MarkdownDomainRecord [class]` (`fd0bda02-0120-5a4f-a4fe-ca4ee8bf1e32`) lines 22-29 [crates/gwiki/src/markdown.rs:22-29]
  - Signature: `pub struct MarkdownDomainRecord {`
  - Purpose: Indexed class `MarkdownDomainRecord` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:22-29]
- `MarkdownParseError` (type) component `MarkdownParseError [type]` (`e71121cc-2253-570c-977e-c9f8ab9a36fe`) lines 32-35 [crates/gwiki/src/markdown.rs:32-35]
  - Signature: `pub enum MarkdownParseError {`
  - Purpose: Indexed type `MarkdownParseError` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:32-35]
- `MarkdownFence` (class) component `MarkdownFence [class]` (`44f0fa0a-726c-5afe-9ed9-dff0a0513b9e`) lines 38-41 [crates/gwiki/src/markdown.rs:38-41]
  - Signature: `pub(crate) struct MarkdownFence {`
  - Purpose: Indexed class `MarkdownFence` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:38-41]
- `markdown_fence_start` (function) component `markdown_fence_start [function]` (`ac9abea2-aa28-59ee-b26d-f4bc83caad23`) lines 43-55 [crates/gwiki/src/markdown.rs:43-55]
  - Signature: `pub(crate) fn markdown_fence_start(line: &str) -> Option<MarkdownFence> {`
  - Purpose: Indexed function `markdown_fence_start` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:43-55]
- `markdown_fence_closes` (function) component `markdown_fence_closes [function]` (`36b7d1c7-2be0-57f7-8bbb-dda7e4ca991f`) lines 57-68 [crates/gwiki/src/markdown.rs:57-68]
  - Signature: `pub(crate) fn markdown_fence_closes(line: &str, fence: MarkdownFence) -> bool {`
  - Purpose: Indexed function `markdown_fence_closes` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:57-68]
- `MarkdownParseError` (class) component `MarkdownParseError [class]` (`f110c3de-5abe-5005-927a-a25828000900`) lines 70-77 [crates/gwiki/src/markdown.rs:70-77]
  - Signature: `impl fmt::Display for MarkdownParseError {`
  - Purpose: Indexed class `MarkdownParseError` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:70-77]
- `MarkdownParseError.fmt` (method) component `MarkdownParseError.fmt [method]` (`fbdd7c9b-0485-59c4-ad45-779dccba74bf`) lines 71-76 [crates/gwiki/src/markdown.rs:71-76]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Indexed method `MarkdownParseError.fmt` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:71-76]
- `MarkdownParseError` (class) component `MarkdownParseError [class]` (`17c4eb02-c42f-5c57-893c-de6501d35db9`) lines 79-79 [crates/gwiki/src/markdown.rs:79]
  - Signature: `impl std::error::Error for MarkdownParseError {}`
  - Purpose: Indexed class `MarkdownParseError` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:79]
- `MarkdownParseError` (class) component `MarkdownParseError [class]` (`387e1030-9be5-5144-abb2-d4bd012c202f`) lines 81-85 [crates/gwiki/src/markdown.rs:81-85]
  - Signature: `impl From<FrontmatterError> for MarkdownParseError {`
  - Purpose: Indexed class `MarkdownParseError` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:81-85]
- `MarkdownParseError.from` (method) component `MarkdownParseError.from [method]` (`b090e9f3-d9a4-5b31-beca-ddca92450e72`) lines 82-84 [crates/gwiki/src/markdown.rs:82-84]
  - Signature: `fn from(error: FrontmatterError) -> Self {`
  - Purpose: Indexed method `MarkdownParseError.from` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:82-84]
- `MarkdownParseError` (class) component `MarkdownParseError [class]` (`b500fc9a-73d0-5357-a1e5-e688dd0bc450`) lines 87-91 [crates/gwiki/src/markdown.rs:87-91]
  - Signature: `impl From<std::io::Error> for MarkdownParseError {`
  - Purpose: Indexed class `MarkdownParseError` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:87-91]
- `MarkdownParseError.from` (method) component `MarkdownParseError.from [method]` (`223e0c06-2ba8-55b5-a787-9901c110f662`) lines 88-90 [crates/gwiki/src/markdown.rs:88-90]
  - Signature: `fn from(error: std::io::Error) -> Self {`
  - Purpose: Indexed method `MarkdownParseError.from` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:88-90]
- `parse_markdown` (function) component `parse_markdown [function]` (`ce5e52b0-f295-5da1-beb1-9d46fc7a1081`) lines 93-116 [crates/gwiki/src/markdown.rs:93-116]
  - Signature: `pub fn parse_markdown<I, S>(`
  - Purpose: Indexed function `parse_markdown` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:93-116]
- `parse_index_file` (function) component `parse_index_file [function]` (`73a39aaf-02e4-5d01-9f18-45c88668f498`) lines 118-129 [crates/gwiki/src/markdown.rs:118-129]
  - Signature: `pub fn parse_index_file<I, S>(`
  - Purpose: Indexed function `parse_index_file` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:118-129]
- `extract_headings` (function) component `extract_headings [function]` (`9f2375db-4a63-5a4b-b212-c8f7a6953a24`) lines 131-184 [crates/gwiki/src/markdown.rs:131-184]
  - Signature: `fn extract_headings(markdown: &str, body_start: usize) -> Vec<MarkdownHeading> {`
  - Purpose: Indexed function `extract_headings` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:131-184]
- `parse_atx_heading` (function) component `parse_atx_heading [function]` (`6bde9974-ea37-5288-b15f-c277ee9d4d87`) lines 186-205 [crates/gwiki/src/markdown.rs:186-205]
  - Signature: `pub(crate) fn parse_atx_heading(line: &str) -> Option<(u8, String)> {`
  - Purpose: Indexed function `parse_atx_heading` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:186-205]
- `strip_atx_closing_sequence` (function) component `strip_atx_closing_sequence [function]` (`d60505c4-c824-5f88-b768-f1f7cb82e650`) lines 207-229 [crates/gwiki/src/markdown.rs:207-229]
  - Signature: `fn strip_atx_closing_sequence(title: &str) -> &str {`
  - Purpose: Indexed function `strip_atx_closing_sequence` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:207-229]
- `build_chunks` (function) component `build_chunks [function]` (`730493d7-b08b-565a-ac81-ac8321eca24c`) lines 231-273 [crates/gwiki/src/markdown.rs:231-273]
  - Signature: `fn build_chunks(`
  - Purpose: Indexed function `build_chunks` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:231-273]
- `push_chunk` (function) component `push_chunk [function]` (`ed3c7b9b-b91e-58e1-8d10-0735550f9bce`) lines 275-295 [crates/gwiki/src/markdown.rs:275-295]
  - Signature: `fn push_chunk(`
  - Purpose: Indexed function `push_chunk` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:275-295]
- `extracts_heading_ranges` (function) component `extracts_heading_ranges [function]` (`fec924a0-9926-5c64-bca2-b65a05c858b7`) lines 303-352 [crates/gwiki/src/markdown.rs:303-352]
  - Signature: `fn extracts_heading_ranges() {`
  - Purpose: Indexed function `extracts_heading_ranges` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:303-352]
- `headings_ignore_code_until_matching_fence_length_closes` (function) component `headings_ignore_code_until_matching_fence_length_closes [function]` (`0f1b2c4b-c5ad-5d66-a3e3-40ea5a4195a8`) lines 355-367 [crates/gwiki/src/markdown.rs:355-367]
  - Signature: `fn headings_ignore_code_until_matching_fence_length_closes() {`
  - Purpose: Indexed function `headings_ignore_code_until_matching_fence_length_closes` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:355-367]
- `index_parse_is_read_only` (function) component `index_parse_is_read_only [function]` (`1f420a8f-ec7e-5454-9229-93efd88dbef6`) lines 370-386 [crates/gwiki/src/markdown.rs:370-386]
  - Signature: `fn index_parse_is_read_only() {`
  - Purpose: Indexed function `index_parse_is_read_only` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:370-386]
- `atx_heading_keeps_hash_without_preceding_space` (function) component `atx_heading_keeps_hash_without_preceding_space [function]` (`a2e56fd1-7b84-5114-b17c-e9bdcaf2d666`) lines 389-398 [crates/gwiki/src/markdown.rs:389-398]
  - Signature: `fn atx_heading_keeps_hash_without_preceding_space() {`
  - Purpose: Indexed function `atx_heading_keeps_hash_without_preceding_space` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:389-398]

