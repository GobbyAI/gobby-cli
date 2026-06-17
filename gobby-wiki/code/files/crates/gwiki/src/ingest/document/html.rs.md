---
title: crates/gwiki/src/ingest/document/html.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/document/html.rs
  ranges:
  - 8-39
  - 41-51
  - 53-76
  - 78-96
  - 98-110
  - 112-140
  - 142-148
  - 150-199
  - 201-213
  - 215-223
  - 230-235
  - 238-242
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/document/html.rs:8-39](crates/gwiki/src/ingest/document/html.rs#L8-L39), [crates/gwiki/src/ingest/document/html.rs:41-51](crates/gwiki/src/ingest/document/html.rs#L41-L51), [crates/gwiki/src/ingest/document/html.rs:53-76](crates/gwiki/src/ingest/document/html.rs#L53-L76), [crates/gwiki/src/ingest/document/html.rs:78-96](crates/gwiki/src/ingest/document/html.rs#L78-L96), [crates/gwiki/src/ingest/document/html.rs:98-110](crates/gwiki/src/ingest/document/html.rs#L98-L110), [crates/gwiki/src/ingest/document/html.rs:112-140](crates/gwiki/src/ingest/document/html.rs#L112-L140), [crates/gwiki/src/ingest/document/html.rs:142-148](crates/gwiki/src/ingest/document/html.rs#L142-L148), [crates/gwiki/src/ingest/document/html.rs:150-199](crates/gwiki/src/ingest/document/html.rs#L150-L199), [crates/gwiki/src/ingest/document/html.rs:201-213](crates/gwiki/src/ingest/document/html.rs#L201-L213), [crates/gwiki/src/ingest/document/html.rs:215-223](crates/gwiki/src/ingest/document/html.rs#L215-L223), [crates/gwiki/src/ingest/document/html.rs:230-235](crates/gwiki/src/ingest/document/html.rs#L230-L235), [crates/gwiki/src/ingest/document/html.rs:238-242](crates/gwiki/src/ingest/document/html.rs#L238-L242)

</details>

# crates/gwiki/src/ingest/document/html.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file turns raw HTML bytes into a document extraction by parsing the HTML, pulling an optional title, collecting readable body text, and normalizing the result into markdown-like text. `extract_html_document` orchestrates the flow: it parses with `scraper`, prefers the `<body>` subtree when present, gathers visible text into parts, joins and normalizes them, and returns either a populated `DocumentExtraction` or a no-content degradation when no readable text is found.

The helper functions support that pipeline by extracting and cleaning the `<title>`, walking the DOM while skipping non-content tags like `head`, `script`, and `style`, distinguishing block elements from inline content, and managing spacing/punctuation so text reads naturally. The normalization helpers collapse markdown and Unicode whitespace, and the test symbols indicate coverage for sectioning tags and whitespace normalization behavior.
[crates/gwiki/src/ingest/document/html.rs:8-39]
[crates/gwiki/src/ingest/document/html.rs:41-51]
[crates/gwiki/src/ingest/document/html.rs:53-76]
[crates/gwiki/src/ingest/document/html.rs:78-96]
[crates/gwiki/src/ingest/document/html.rs:98-110]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `extract_html_document` | function | `pub(crate) fn extract_html_document(bytes: &[u8]) -> Result<DocumentExtraction, WikiError> {` | `extract_html_document [function]` | `1bf81aa4-071b-5672-b65a-288e5c3f154f` | 8-39 [crates/gwiki/src/ingest/document/html.rs:8-39] | Indexed function `extract_html_document` in `crates/gwiki/src/ingest/document/html.rs`. [crates/gwiki/src/ingest/document/html.rs:8-39] |
| `extract_html_title` | function | `fn extract_html_title(document: &Html) -> Option<String> {` | `extract_html_title [function]` | `c6c02a87-4cc3-542e-bbc1-446e0185e8bc` | 41-51 [crates/gwiki/src/ingest/document/html.rs:41-51] | Indexed function `extract_html_title` in `crates/gwiki/src/ingest/document/html.rs`. [crates/gwiki/src/ingest/document/html.rs:41-51] |
| `collect_visible_text` | function | `fn collect_visible_text(element: ElementRef<'_>, parts: &mut Vec<String>) {` | `collect_visible_text [function]` | `68d26b08-c2bc-5988-ac45-5cf8370577ff` | 53-76 [crates/gwiki/src/ingest/document/html.rs:53-76] | Indexed function `collect_visible_text` in `crates/gwiki/src/ingest/document/html.rs`. [crates/gwiki/src/ingest/document/html.rs:53-76] |
| `collect_inline_text` | function | `fn collect_inline_text(element: ElementRef<'_>) -> String {` | `collect_inline_text [function]` | `e46717f1-1950-5c09-b743-54cefbefbdfe` | 78-96 [crates/gwiki/src/ingest/document/html.rs:78-96] | Indexed function `collect_inline_text` in `crates/gwiki/src/ingest/document/html.rs`. [crates/gwiki/src/ingest/document/html.rs:78-96] |
| `append_inline_text` | function | `fn append_inline_text(output: &mut String, text: &str) {` | `append_inline_text [function]` | `fc2bcf43-a8e6-5407-8173-eec93e624e41` | 98-110 [crates/gwiki/src/ingest/document/html.rs:98-110] | Indexed function `append_inline_text` in `crates/gwiki/src/ingest/document/html.rs`. [crates/gwiki/src/ingest/document/html.rs:98-110] |
| `starts_with_closing_punctuation` | function | `fn starts_with_closing_punctuation(text: &str) -> bool {` | `starts_with_closing_punctuation [function]` | `3ce743fe-f6bf-5086-9d9a-b4ba0b9d9342` | 112-140 [crates/gwiki/src/ingest/document/html.rs:112-140] | Indexed function `starts_with_closing_punctuation` in `crates/gwiki/src/ingest/document/html.rs`. [crates/gwiki/src/ingest/document/html.rs:112-140] |
| `push_visible_part` | function | `fn push_visible_part(parts: &mut Vec<String>, inline: &mut String) {` | `push_visible_part [function]` | `7de0872b-a2d7-554d-931c-3e6e462b823a` | 142-148 [crates/gwiki/src/ingest/document/html.rs:142-148] | Indexed function `push_visible_part` in `crates/gwiki/src/ingest/document/html.rs`. [crates/gwiki/src/ingest/document/html.rs:142-148] |
| `is_block_element` | function | `fn is_block_element(name: &str) -> bool {` | `is_block_element [function]` | `2c2e0154-4860-55af-837e-736858f6f3f0` | 150-199 [crates/gwiki/src/ingest/document/html.rs:150-199] | Indexed function `is_block_element` in `crates/gwiki/src/ingest/document/html.rs`. [crates/gwiki/src/ingest/document/html.rs:150-199] |
| `normalize_markdown_text` | function | `fn normalize_markdown_text(text: &str) -> String {` | `normalize_markdown_text [function]` | `eefaf173-938b-5db1-a098-edfcd7f52ba7` | 201-213 [crates/gwiki/src/ingest/document/html.rs:201-213] | Indexed function `normalize_markdown_text` in `crates/gwiki/src/ingest/document/html.rs`. [crates/gwiki/src/ingest/document/html.rs:201-213] |
| `normalize_unicode_whitespace` | function | `fn normalize_unicode_whitespace(text: &str) -> String {` | `normalize_unicode_whitespace [function]` | `7c193d5d-49db-5bdd-9973-221150919cc7` | 215-223 [crates/gwiki/src/ingest/document/html.rs:215-223] | Indexed function `normalize_unicode_whitespace` in `crates/gwiki/src/ingest/document/html.rs`. [crates/gwiki/src/ingest/document/html.rs:215-223] |
| `normalize_markdown_text_normalizes_unicode_whitespace_before_lines` | function | `fn normalize_markdown_text_normalizes_unicode_whitespace_before_lines() {` | `normalize_markdown_text_normalizes_unicode_whitespace_before_lines [function]` | `0aa2ed7b-89d5-5deb-b165-da1cbd3067d4` | 230-235 [crates/gwiki/src/ingest/document/html.rs:230-235] | Indexed function `normalize_markdown_text_normalizes_unicode_whitespace_before_lines` in `crates/gwiki/src/ingest/document/html.rs`. [crates/gwiki/src/ingest/document/html.rs:230-235] |
| `html5_sectioning_tags_are_block_elements` | function | `fn html5_sectioning_tags_are_block_elements() {` | `html5_sectioning_tags_are_block_elements [function]` | `c9181c23-f1c7-5a08-8c5b-ff3c6ee9673e` | 238-242 [crates/gwiki/src/ingest/document/html.rs:238-242] | Indexed function `html5_sectioning_tags_are_block_elements` in `crates/gwiki/src/ingest/document/html.rs`. [crates/gwiki/src/ingest/document/html.rs:238-242] |
