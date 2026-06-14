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

This file normalizes extracted PDF page text into clean paragraphs. `normalize_page_text` walks each input line, passes it through `single_line` to trim and flatten wrapping, groups non-empty lines into paragraphs, and joins paragraphs with blank lines so original paragraph breaks are preserved while extra whitespace and repeated blank lines are removed. The test module verifies the behavior across edge cases such as leading/trailing whitespace, multiple blank lines, whitespace-only input, empty input, single lines, and multi-line text with and without paragraph breaks.
[crates/gwiki/src/ingest/pdf/text.rs:4-25]
[crates/gwiki/src/ingest/pdf/text.rs:32-36]
[crates/gwiki/src/ingest/pdf/text.rs:39-49]
[crates/gwiki/src/ingest/pdf/text.rs:52-54]
[crates/gwiki/src/ingest/pdf/text.rs:57-59]

## API Symbols

- `normalize_page_text` (function) component `normalize_page_text [function]` (`4c7760f4-07a6-539a-a8d4-c84163b931ee`) lines 4-25 [crates/gwiki/src/ingest/pdf/text.rs:4-25]
  - Signature: `pub(crate) fn normalize_page_text(text: &str) -> String {`
  - Purpose: Indexed function `normalize_page_text` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:4-25]
- `normalize_page_text_preserves_paragraph_breaks` (function) component `normalize_page_text_preserves_paragraph_breaks [function]` (`41bdf075-e195-5fd6-ab33-a7552152d06a`) lines 32-36 [crates/gwiki/src/ingest/pdf/text.rs:32-36]
  - Signature: `fn normalize_page_text_preserves_paragraph_breaks() {`
  - Purpose: Indexed function `normalize_page_text_preserves_paragraph_breaks` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:32-36]
- `normalize_page_text_handles_whitespace_edges` (function) component `normalize_page_text_handles_whitespace_edges [function]` (`ce04a893-c469-5583-8a35-fbd456b30c8a`) lines 39-49 [crates/gwiki/src/ingest/pdf/text.rs:39-49]
  - Signature: `fn normalize_page_text_handles_whitespace_edges() {`
  - Purpose: Indexed function `normalize_page_text_handles_whitespace_edges` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:39-49]
- `normalize_page_text_multiple_blank_lines` (function) component `normalize_page_text_multiple_blank_lines [function]` (`78c8c579-da08-566d-a140-56b096072a6a`) lines 52-54 [crates/gwiki/src/ingest/pdf/text.rs:52-54]
  - Signature: `fn normalize_page_text_multiple_blank_lines() {`
  - Purpose: Indexed function `normalize_page_text_multiple_blank_lines` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:52-54]
- `normalize_page_text_trailing_blank_lines` (function) component `normalize_page_text_trailing_blank_lines [function]` (`cec6e7cb-44d8-527c-ab1c-f6f346ccd518`) lines 57-59 [crates/gwiki/src/ingest/pdf/text.rs:57-59]
  - Signature: `fn normalize_page_text_trailing_blank_lines() {`
  - Purpose: Indexed function `normalize_page_text_trailing_blank_lines` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:57-59]
- `normalize_page_text_whitespace_only_lines` (function) component `normalize_page_text_whitespace_only_lines [function]` (`580faa00-90fb-5bed-a4a7-2a41b7b9b9f3`) lines 62-64 [crates/gwiki/src/ingest/pdf/text.rs:62-64]
  - Signature: `fn normalize_page_text_whitespace_only_lines() {`
  - Purpose: Indexed function `normalize_page_text_whitespace_only_lines` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:62-64]
- `normalize_page_text_empty_input` (function) component `normalize_page_text_empty_input [function]` (`ae9d61ab-19d6-5116-a47e-126ab81e7268`) lines 67-69 [crates/gwiki/src/ingest/pdf/text.rs:67-69]
  - Signature: `fn normalize_page_text_empty_input() {`
  - Purpose: Indexed function `normalize_page_text_empty_input` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:67-69]
- `normalize_page_text_single_line` (function) component `normalize_page_text_single_line [function]` (`cf4b7879-61e4-58a7-a115-4565247d9046`) lines 72-74 [crates/gwiki/src/ingest/pdf/text.rs:72-74]
  - Signature: `fn normalize_page_text_single_line() {`
  - Purpose: Indexed function `normalize_page_text_single_line` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:72-74]
- `normalize_page_text_no_blank_lines` (function) component `normalize_page_text_no_blank_lines [function]` (`42d5bcb1-e10e-570f-bfa9-b0010ac3cad9`) lines 77-82 [crates/gwiki/src/ingest/pdf/text.rs:77-82]
  - Signature: `fn normalize_page_text_no_blank_lines() {`
  - Purpose: Indexed function `normalize_page_text_no_blank_lines` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:77-82]

