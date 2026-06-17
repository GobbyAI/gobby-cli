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
  - 71-76
  - 82-84
  - 88-90
  - 93-116
  - 119-130
  - 132-185
  - 187-206
  - 208-230
  - 232-274
  - 276-296
  - 304-353
  - 356-368
  - 371-387
  - 390-399
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/markdown.rs:11-19](crates/gwiki/src/markdown.rs#L11-L19), [crates/gwiki/src/markdown.rs:22-29](crates/gwiki/src/markdown.rs#L22-L29), [crates/gwiki/src/markdown.rs:32-35](crates/gwiki/src/markdown.rs#L32-L35), [crates/gwiki/src/markdown.rs:38-41](crates/gwiki/src/markdown.rs#L38-L41), [crates/gwiki/src/markdown.rs:43-55](crates/gwiki/src/markdown.rs#L43-L55), [crates/gwiki/src/markdown.rs:57-68](crates/gwiki/src/markdown.rs#L57-L68), [crates/gwiki/src/markdown.rs:71-76](crates/gwiki/src/markdown.rs#L71-L76), [crates/gwiki/src/markdown.rs:82-84](crates/gwiki/src/markdown.rs#L82-L84), [crates/gwiki/src/markdown.rs:88-90](crates/gwiki/src/markdown.rs#L88-L90), [crates/gwiki/src/markdown.rs:93-116](crates/gwiki/src/markdown.rs#L93-L116), [crates/gwiki/src/markdown.rs:119-130](crates/gwiki/src/markdown.rs#L119-L130), [crates/gwiki/src/markdown.rs:132-185](crates/gwiki/src/markdown.rs#L132-L185), [crates/gwiki/src/markdown.rs:187-206](crates/gwiki/src/markdown.rs#L187-L206), [crates/gwiki/src/markdown.rs:208-230](crates/gwiki/src/markdown.rs#L208-L230), [crates/gwiki/src/markdown.rs:232-274](crates/gwiki/src/markdown.rs#L232-L274), [crates/gwiki/src/markdown.rs:276-296](crates/gwiki/src/markdown.rs#L276-L296), [crates/gwiki/src/markdown.rs:304-353](crates/gwiki/src/markdown.rs#L304-L353), [crates/gwiki/src/markdown.rs:356-368](crates/gwiki/src/markdown.rs#L356-L368), [crates/gwiki/src/markdown.rs:371-387](crates/gwiki/src/markdown.rs#L371-L387), [crates/gwiki/src/markdown.rs:390-399](crates/gwiki/src/markdown.rs#L390-L399)

</details>

# crates/gwiki/src/markdown.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements Markdown parsing for wiki content. It defines `MarkdownHeading` to record heading metadata and byte ranges, and `MarkdownDomainRecord` to bundle a page’s path, parsed frontmatter, body offset, extracted headings, links, and index chunks. The parser is centered around `parse_markdown` and `parse_index_file`, which read content, parse frontmatter, extract links, and build chunk/index data. Supporting helpers detect fenced code blocks, parse ATX headings, strip closing `#` sequences, and compute heading ranges while ignoring headings inside matching fences. `MarkdownParseError` wraps frontmatter and I/O failures and provides display/error conversions for the parsing flow.
[crates/gwiki/src/markdown.rs:11-19]
[crates/gwiki/src/markdown.rs:22-29]
[crates/gwiki/src/markdown.rs:32-35]
[crates/gwiki/src/markdown.rs:38-41]
[crates/gwiki/src/markdown.rs:43-55]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `MarkdownHeading` | class | `pub struct MarkdownHeading {` | `MarkdownHeading [class]` | `f8871d89-a4b9-577d-b70c-8fe152ce549d` | 11-19 [crates/gwiki/src/markdown.rs:11-19] | Indexed class `MarkdownHeading` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:11-19] |
| `MarkdownDomainRecord` | class | `pub struct MarkdownDomainRecord {` | `MarkdownDomainRecord [class]` | `fd0bda02-0120-5a4f-a4fe-ca4ee8bf1e32` | 22-29 [crates/gwiki/src/markdown.rs:22-29] | Indexed class `MarkdownDomainRecord` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:22-29] |
| `MarkdownParseError` | type | `pub enum MarkdownParseError {` | `MarkdownParseError [type]` | `e71121cc-2253-570c-977e-c9f8ab9a36fe` | 32-35 [crates/gwiki/src/markdown.rs:32-35] | Indexed type `MarkdownParseError` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:32-35] |
| `MarkdownFence` | class | `pub(crate) struct MarkdownFence {` | `MarkdownFence [class]` | `44f0fa0a-726c-5afe-9ed9-dff0a0513b9e` | 38-41 [crates/gwiki/src/markdown.rs:38-41] | Indexed class `MarkdownFence` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:38-41] |
| `markdown_fence_start` | function | `pub(crate) fn markdown_fence_start(line: &str) -> Option<MarkdownFence> {` | `markdown_fence_start [function]` | `ac9abea2-aa28-59ee-b26d-f4bc83caad23` | 43-55 [crates/gwiki/src/markdown.rs:43-55] | Indexed function `markdown_fence_start` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:43-55] |
| `markdown_fence_closes` | function | `pub(crate) fn markdown_fence_closes(line: &str, fence: MarkdownFence) -> bool {` | `markdown_fence_closes [function]` | `36b7d1c7-2be0-57f7-8bbb-dda7e4ca991f` | 57-68 [crates/gwiki/src/markdown.rs:57-68] | Indexed function `markdown_fence_closes` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:57-68] |
| `MarkdownParseError::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `MarkdownParseError::fmt [method]` | `fbdd7c9b-0485-59c4-ad45-779dccba74bf` | 71-76 [crates/gwiki/src/markdown.rs:71-76] | Indexed method `MarkdownParseError::fmt` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:71-76] |
| `MarkdownParseError::from` | method | `fn from(error: FrontmatterError) -> Self {` | `MarkdownParseError::from [method]` | `b090e9f3-d9a4-5b31-beca-ddca92450e72` | 82-84 [crates/gwiki/src/markdown.rs:82-84] | Indexed method `MarkdownParseError::from` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:82-84] |
| `MarkdownParseError::from` | method | `fn from(error: std::io::Error) -> Self {` | `MarkdownParseError::from [method]` | `223e0c06-2ba8-55b5-a787-9901c110f662` | 88-90 [crates/gwiki/src/markdown.rs:88-90] | Indexed method `MarkdownParseError::from` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:88-90] |
| `parse_markdown` | function | `pub fn parse_markdown<I, S>(` | `parse_markdown [function]` | `ce5e52b0-f295-5da1-beb1-9d46fc7a1081` | 93-116 [crates/gwiki/src/markdown.rs:93-116] | Indexed function `parse_markdown` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:93-116] |
| `parse_index_file` | function | `pub fn parse_index_file<I, S>(` | `parse_index_file [function]` | `89afdf74-873c-5f78-82e9-b5faea06790a` | 119-130 [crates/gwiki/src/markdown.rs:119-130] | Indexed function `parse_index_file` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:119-130] |
| `extract_headings` | function | `fn extract_headings(markdown: &str, body_start: usize) -> Vec<MarkdownHeading> {` | `extract_headings [function]` | `4acb5620-41a1-5f51-ab93-f13c5a216413` | 132-185 [crates/gwiki/src/markdown.rs:132-185] | Indexed function `extract_headings` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:132-185] |
| `parse_atx_heading` | function | `pub(crate) fn parse_atx_heading(line: &str) -> Option<(u8, String)> {` | `parse_atx_heading [function]` | `195e7aee-5dd7-5119-ab53-98bcb2308cd6` | 187-206 [crates/gwiki/src/markdown.rs:187-206] | Indexed function `parse_atx_heading` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:187-206] |
| `strip_atx_closing_sequence` | function | `fn strip_atx_closing_sequence(title: &str) -> &str {` | `strip_atx_closing_sequence [function]` | `47a5d906-49ab-5666-9385-6fa127651597` | 208-230 [crates/gwiki/src/markdown.rs:208-230] | Indexed function `strip_atx_closing_sequence` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:208-230] |
| `build_chunks` | function | `fn build_chunks(` | `build_chunks [function]` | `8565bca7-06f4-5c44-bc35-1f329d7fc187` | 232-274 [crates/gwiki/src/markdown.rs:232-274] | Indexed function `build_chunks` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:232-274] |
| `push_chunk` | function | `fn push_chunk(` | `push_chunk [function]` | `06baa7e2-2f66-58f7-a8e4-877dcbe4f073` | 276-296 [crates/gwiki/src/markdown.rs:276-296] | Indexed function `push_chunk` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:276-296] |
| `extracts_heading_ranges` | function | `fn extracts_heading_ranges() {` | `extracts_heading_ranges [function]` | `0ecf31b1-78e8-5228-8eb2-3e22ee84b756` | 304-353 [crates/gwiki/src/markdown.rs:304-353] | Indexed function `extracts_heading_ranges` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:304-353] |
| `headings_ignore_code_until_matching_fence_length_closes` | function | `fn headings_ignore_code_until_matching_fence_length_closes() {` | `headings_ignore_code_until_matching_fence_length_closes [function]` | `78b65cdb-2809-552b-9389-ece8288d51d1` | 356-368 [crates/gwiki/src/markdown.rs:356-368] | Indexed function `headings_ignore_code_until_matching_fence_length_closes` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:356-368] |
| `index_parse_is_read_only` | function | `fn index_parse_is_read_only() {` | `index_parse_is_read_only [function]` | `f39f917b-e02b-546c-b33a-1ba6b3842c7d` | 371-387 [crates/gwiki/src/markdown.rs:371-387] | Indexed function `index_parse_is_read_only` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:371-387] |
| `atx_heading_keeps_hash_without_preceding_space` | function | `fn atx_heading_keeps_hash_without_preceding_space() {` | `atx_heading_keeps_hash_without_preceding_space [function]` | `90226c7c-0678-5af3-92c8-70f2cb9bc096` | 390-399 [crates/gwiki/src/markdown.rs:390-399] | Indexed function `atx_heading_keeps_hash_without_preceding_space` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:390-399] |
