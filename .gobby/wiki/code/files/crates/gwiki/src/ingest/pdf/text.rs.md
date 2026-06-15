---
title: crates/gwiki/src/ingest/pdf/text.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/text.rs
  ranges:
  - 4-25
  - 32-36
  - 39-49
  - 52-54
  - 57-59
  - 62-64
  - 67-69
  - 72-74
  - 77-82
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/text.rs

Module: [[code/modules/crates/gwiki/src/ingest/pdf|crates/gwiki/src/ingest/pdf]]

## Purpose

This file normalizes extracted PDF page text into clean paragraphs. `normalize_page_text` trims each line with `single_line`, drops empty/whitespace-only lines, joins consecutive non-empty lines into a single paragraph with spaces, and uses double newlines to separate paragraphs; the tests cover paragraph preservation, whitespace trimming, collapsing multiple blank lines, removing trailing blanks, handling empty or whitespace-only input, and leaving already single-line text unchanged.
[crates/gwiki/src/ingest/pdf/text.rs:4-25]
[crates/gwiki/src/ingest/pdf/text.rs:32-36]
[crates/gwiki/src/ingest/pdf/text.rs:39-49]
[crates/gwiki/src/ingest/pdf/text.rs:52-54]
[crates/gwiki/src/ingest/pdf/text.rs:57-59]

## API Symbols

- `normalize_page_text` (function) component `normalize_page_text [function]` (`4c7760f4-07a6-539a-a8d4-c84163b931ee`) lines 4-25 [crates/gwiki/src/ingest/pdf/text.rs:4-25]
  - Signature: `pub(crate) fn normalize_page_text(text: &str) -> String {`
  - Purpose: Collapses non-empty lines into paragraphs by trimming each line with 'single_line', joining consecutive lines with spaces, and separating paragraphs with double newlines whenever blank lines are encountered. [crates/gwiki/src/ingest/pdf/text.rs:4-25]
- `normalize_page_text_preserves_paragraph_breaks` (function) component `normalize_page_text_preserves_paragraph_breaks [function]` (`41bdf075-e195-5fd6-ab33-a7552152d06a`) lines 32-36 [crates/gwiki/src/ingest/pdf/text.rs:32-36]
  - Signature: `fn normalize_page_text_preserves_paragraph_breaks() {`
  - Purpose: Verifies that 'normalize_page_text' merges single newline line wraps into spaces while preserving double-newline paragraph breaks and trimming the trailing newline. [crates/gwiki/src/ingest/pdf/text.rs:32-36]
- `normalize_page_text_handles_whitespace_edges` (function) component `normalize_page_text_handles_whitespace_edges [function]` (`ce04a893-c469-5583-8a35-fbd456b30c8a`) lines 39-49 [crates/gwiki/src/ingest/pdf/text.rs:39-49]
  - Signature: `fn normalize_page_text_handles_whitespace_edges() {`
  - Purpose: Verifies that 'normalize_page_text' trims leading/trailing whitespace, collapses intra-line whitespace, and preserves paragraph breaks as double newlines. [crates/gwiki/src/ingest/pdf/text.rs:39-49]
- `normalize_page_text_multiple_blank_lines` (function) component `normalize_page_text_multiple_blank_lines [function]` (`78c8c579-da08-566d-a140-56b096072a6a`) lines 52-54 [crates/gwiki/src/ingest/pdf/text.rs:52-54]
  - Signature: `fn normalize_page_text_multiple_blank_lines() {`
  - Purpose: Tests that 'normalize_page_text' collapses runs of three or more consecutive newline-separated blank lines into a single blank line, preserving exactly two newline characters between paragraphs. [crates/gwiki/src/ingest/pdf/text.rs:52-54]
- `normalize_page_text_trailing_blank_lines` (function) component `normalize_page_text_trailing_blank_lines [function]` (`cec6e7cb-44d8-527c-ab1c-f6f346ccd518`) lines 57-59 [crates/gwiki/src/ingest/pdf/text.rs:57-59]
  - Signature: `fn normalize_page_text_trailing_blank_lines() {`
  - Purpose: Removes trailing blank lines from page text, collapsing a '"First\n\n"' input to '"First"' without altering the substantive content. [crates/gwiki/src/ingest/pdf/text.rs:57-59]
- `normalize_page_text_whitespace_only_lines` (function) component `normalize_page_text_whitespace_only_lines [function]` (`580faa00-90fb-5bed-a4a7-2a41b7b9b9f3`) lines 62-64 [crates/gwiki/src/ingest/pdf/text.rs:62-64]
  - Signature: `fn normalize_page_text_whitespace_only_lines() {`
  - Purpose: Verifies that 'normalize_page_text' collapses input consisting only of whitespace and blank lines into an empty string. [crates/gwiki/src/ingest/pdf/text.rs:62-64]
- `normalize_page_text_empty_input` (function) component `normalize_page_text_empty_input [function]` (`ae9d61ab-19d6-5116-a47e-126ab81e7268`) lines 67-69 [crates/gwiki/src/ingest/pdf/text.rs:67-69]
  - Signature: `fn normalize_page_text_empty_input() {`
  - Purpose: Verifies that 'normalize_page_text' returns an empty string unchanged when given an empty input string. [crates/gwiki/src/ingest/pdf/text.rs:67-69]
- `normalize_page_text_single_line` (function) component `normalize_page_text_single_line [function]` (`cf4b7879-61e4-58a7-a115-4565247d9046`) lines 72-74 [crates/gwiki/src/ingest/pdf/text.rs:72-74]
  - Signature: `fn normalize_page_text_single_line() {`
  - Purpose: 'normalize_page_text_single_line' verifies that 'normalize_page_text' leaves an already single-line page text unchanged. [crates/gwiki/src/ingest/pdf/text.rs:72-74]
- `normalize_page_text_no_blank_lines` (function) component `normalize_page_text_no_blank_lines [function]` (`42d5bcb1-e10e-570f-bfa9-b0010ac3cad9`) lines 77-82 [crates/gwiki/src/ingest/pdf/text.rs:77-82]
  - Signature: `fn normalize_page_text_no_blank_lines() {`
  - Purpose: Verifies that 'normalize_page_text' converts a single wrapped multiline paragraph into one space-separated line, preserving text while removing newline breaks. [crates/gwiki/src/ingest/pdf/text.rs:77-82]

