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

# crates/gwiki/src/ingest/document/html.rs

Module: [[code/modules/crates/gwiki/src/ingest/document|crates/gwiki/src/ingest/document]]

## Purpose

`crates/gwiki/src/ingest/document/html.rs` exposes 12 indexed API symbols.
[crates/gwiki/src/ingest/document/html.rs:8-39]
[crates/gwiki/src/ingest/document/html.rs:41-51]
[crates/gwiki/src/ingest/document/html.rs:53-76]
[crates/gwiki/src/ingest/document/html.rs:78-96]
[crates/gwiki/src/ingest/document/html.rs:98-110]

## API Symbols

- `extract_html_document` (function) component `extract_html_document [function]` (`1bf81aa4-071b-5672-b65a-288e5c3f154f`) lines 8-39 [crates/gwiki/src/ingest/document/html.rs:8-39]
  - Signature: `pub(crate) fn extract_html_document(bytes: &[u8]) -> Result<DocumentExtraction, WikiError> {`
  - Purpose: Parses HTML bytes to extract visible text content as normalized markdown with the document title, returning a `DocumentExtraction` with degradation metadata if no readable content is found. [crates/gwiki/src/ingest/document/html.rs:8-39]
- `extract_html_title` (function) component `extract_html_title [function]` (`c6c02a87-4cc3-542e-bbc1-446e0185e8bc`) lines 41-51 [crates/gwiki/src/ingest/document/html.rs:41-51]
  - Signature: `fn extract_html_title(document: &Html) -> Option<String> {`
  - Purpose: Extracts the HTML document's title element, decodes XML entities, applies markdown formatting, and returns the non-empty result as `Option<String>`. [crates/gwiki/src/ingest/document/html.rs:41-51]
- `collect_visible_text` (function) component `collect_visible_text [function]` (`68d26b08-c2bc-5988-ac45-5cf8370577ff`) lines 53-76 [crates/gwiki/src/ingest/document/html.rs:53-76]
  - Signature: `fn collect_visible_text(element: ElementRef<'_>, parts: &mut Vec<String>) {`
  - Purpose: Recursively traverses an HTML element tree, extracting visible text content into a vector of strings segmented by block-level elements while excluding head, script, and style nodes. [crates/gwiki/src/ingest/document/html.rs:53-76]
- `collect_inline_text` (function) component `collect_inline_text [function]` (`e46717f1-1950-5c09-b743-54cefbefbdfe`) lines 78-96 [crates/gwiki/src/ingest/document/html.rs:78-96]
  - Signature: `fn collect_inline_text(element: ElementRef<'_>) -> String {`
  - Purpose: Recursively extracts all text nodes from an HTML element's DOM tree while excluding head, script, and style elements. [crates/gwiki/src/ingest/document/html.rs:78-96]
- `append_inline_text` (function) component `append_inline_text [function]` (`fc2bcf43-a8e6-5407-8173-eec93e624e41`) lines 98-110 [crates/gwiki/src/ingest/document/html.rs:98-110]
  - Signature: `fn append_inline_text(output: &mut String, text: &str) {`
  - Purpose: Appends trimmed text to a mutable string with conditional spacing, inserting a space before the text only if the output is non-empty, ends with a non-whitespace character, and the text does not start with closing punctuation. [crates/gwiki/src/ingest/document/html.rs:98-110]
- `starts_with_closing_punctuation` (function) component `starts_with_closing_punctuation [function]` (`3ce743fe-f6bf-5086-9d9a-b4ba0b9d9342`) lines 112-140 [crates/gwiki/src/ingest/document/html.rs:112-140]
  - Signature: `fn starts_with_closing_punctuation(text: &str) -> bool {`
  - Purpose: Returns true if the first character of the input string is a closing or terminal punctuation mark, including ASCII variants (`.`, `,`, `;`, `:`, `!`, `?`, `)`, `]`, `}`, quotes) and Unicode equivalents for CJK and European punctuation. [crates/gwiki/src/ingest/document/html.rs:112-140]
- `push_visible_part` (function) component `push_visible_part [function]` (`7de0872b-a2d7-554d-931c-3e6e462b823a`) lines 142-148 [crates/gwiki/src/ingest/document/html.rs:142-148]
  - Signature: `fn push_visible_part(parts: &mut Vec<String>, inline: &mut String) {`
  - Purpose: Converts the inline string to a single-line format via `single_line()`, appends it to the parts vector if non-empty, and clears the input string. [crates/gwiki/src/ingest/document/html.rs:142-148]
- `is_block_element` (function) component `is_block_element [function]` (`2c2e0154-4860-55af-837e-736858f6f3f0`) lines 150-199 [crates/gwiki/src/ingest/document/html.rs:150-199]
  - Signature: `fn is_block_element(name: &str) -> bool {`
  - Purpose: Determines whether a given HTML tag name is a block-level element by pattern matching against a hardcoded set of 44 semantic and structural HTML block elements. [crates/gwiki/src/ingest/document/html.rs:150-199]
- `normalize_markdown_text` (function) component `normalize_markdown_text [function]` (`eefaf173-938b-5db1-a098-edfcd7f52ba7`) lines 201-213 [crates/gwiki/src/ingest/document/html.rs:201-213]
  - Signature: `fn normalize_markdown_text(text: &str) -> String {`
  - Purpose: Normalizes markdown text by decoding XML entities, normalizing Unicode whitespace, filtering empty lines, deduplicating consecutive identical lines, and joining the result with double-newline paragraph separators. [crates/gwiki/src/ingest/document/html.rs:201-213]
- `normalize_unicode_whitespace` (function) component `normalize_unicode_whitespace [function]` (`7c193d5d-49db-5bdd-9973-221150919cc7`) lines 215-223 [crates/gwiki/src/ingest/document/html.rs:215-223]
  - Signature: `fn normalize_unicode_whitespace(text: &str) -> String {`
  - Purpose: Normalizes Unicode whitespace by converting line and paragraph separators (`U+2028`, `U+2029`) and carriage returns to newlines, replacing all other whitespace characters with spaces, and preserving all non-whitespace characters. [crates/gwiki/src/ingest/document/html.rs:215-223]
- `normalize_markdown_text_normalizes_unicode_whitespace_before_lines` (function) component `normalize_markdown_text_normalizes_unicode_whitespace_before_lines [function]` (`0aa2ed7b-89d5-5deb-b165-da1cbd3067d4`) lines 230-235 [crates/gwiki/src/ingest/document/html.rs:230-235]
  - Signature: `fn normalize_markdown_text_normalizes_unicode_whitespace_before_lines() {`
  - Purpose: This test function verifies that `normalize_markdown_text` converts Unicode non-breaking spaces (U+00A0) to regular spaces and line separators (U+2028) to paragraph breaks (double newlines). [crates/gwiki/src/ingest/document/html.rs:230-235]
- `html5_sectioning_tags_are_block_elements` (function) component `html5_sectioning_tags_are_block_elements [function]` (`c9181c23-f1c7-5a08-8c5b-ff3c6ee9673e`) lines 238-242 [crates/gwiki/src/ingest/document/html.rs:238-242]
  - Signature: `fn html5_sectioning_tags_are_block_elements() {`
  - Purpose: This test function verifies that the HTML5 tags `details`, `summary`, and `thead` are correctly classified as block-level elements by the `is_block_element()` function. [crates/gwiki/src/ingest/document/html.rs:238-242]

