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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/pdf/text.rs:4-25](crates/gwiki/src/ingest/pdf/text.rs#L4-L25), [crates/gwiki/src/ingest/pdf/text.rs:32-36](crates/gwiki/src/ingest/pdf/text.rs#L32-L36), [crates/gwiki/src/ingest/pdf/text.rs:39-49](crates/gwiki/src/ingest/pdf/text.rs#L39-L49), [crates/gwiki/src/ingest/pdf/text.rs:52-54](crates/gwiki/src/ingest/pdf/text.rs#L52-L54), [crates/gwiki/src/ingest/pdf/text.rs:57-59](crates/gwiki/src/ingest/pdf/text.rs#L57-L59), [crates/gwiki/src/ingest/pdf/text.rs:62-64](crates/gwiki/src/ingest/pdf/text.rs#L62-L64), [crates/gwiki/src/ingest/pdf/text.rs:67-69](crates/gwiki/src/ingest/pdf/text.rs#L67-L69), [crates/gwiki/src/ingest/pdf/text.rs:72-74](crates/gwiki/src/ingest/pdf/text.rs#L72-L74), [crates/gwiki/src/ingest/pdf/text.rs:77-82](crates/gwiki/src/ingest/pdf/text.rs#L77-L82)

</details>

# crates/gwiki/src/ingest/pdf/text.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Provides PDF page-text normalization for ingestion. `normalize_page_text` runs each input line through `single_line`, drops empty or whitespace-only lines, groups consecutive nonblank lines into paragraphs joined with spaces, and emits those paragraphs separated by double newlines. The test module verifies the behavior across paragraph breaks, edge whitespace, multiple blank lines, trailing blanks, empty input, single-line input, and fully unbroken text.
[crates/gwiki/src/ingest/pdf/text.rs:4-25]
[crates/gwiki/src/ingest/pdf/text.rs:32-36]
[crates/gwiki/src/ingest/pdf/text.rs:39-49]
[crates/gwiki/src/ingest/pdf/text.rs:52-54]
[crates/gwiki/src/ingest/pdf/text.rs:57-59]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `normalize_page_text` | function | `pub(crate) fn normalize_page_text(text: &str) -> String {` | `normalize_page_text [function]` | `4c7760f4-07a6-539a-a8d4-c84163b931ee` | 4-25 [crates/gwiki/src/ingest/pdf/text.rs:4-25] | Indexed function `normalize_page_text` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:4-25] |
| `normalize_page_text_preserves_paragraph_breaks` | function | `fn normalize_page_text_preserves_paragraph_breaks() {` | `normalize_page_text_preserves_paragraph_breaks [function]` | `41bdf075-e195-5fd6-ab33-a7552152d06a` | 32-36 [crates/gwiki/src/ingest/pdf/text.rs:32-36] | Indexed function `normalize_page_text_preserves_paragraph_breaks` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:32-36] |
| `normalize_page_text_handles_whitespace_edges` | function | `fn normalize_page_text_handles_whitespace_edges() {` | `normalize_page_text_handles_whitespace_edges [function]` | `ce04a893-c469-5583-8a35-fbd456b30c8a` | 39-49 [crates/gwiki/src/ingest/pdf/text.rs:39-49] | Indexed function `normalize_page_text_handles_whitespace_edges` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:39-49] |
| `normalize_page_text_multiple_blank_lines` | function | `fn normalize_page_text_multiple_blank_lines() {` | `normalize_page_text_multiple_blank_lines [function]` | `78c8c579-da08-566d-a140-56b096072a6a` | 52-54 [crates/gwiki/src/ingest/pdf/text.rs:52-54] | Indexed function `normalize_page_text_multiple_blank_lines` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:52-54] |
| `normalize_page_text_trailing_blank_lines` | function | `fn normalize_page_text_trailing_blank_lines() {` | `normalize_page_text_trailing_blank_lines [function]` | `cec6e7cb-44d8-527c-ab1c-f6f346ccd518` | 57-59 [crates/gwiki/src/ingest/pdf/text.rs:57-59] | Indexed function `normalize_page_text_trailing_blank_lines` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:57-59] |
| `normalize_page_text_whitespace_only_lines` | function | `fn normalize_page_text_whitespace_only_lines() {` | `normalize_page_text_whitespace_only_lines [function]` | `580faa00-90fb-5bed-a4a7-2a41b7b9b9f3` | 62-64 [crates/gwiki/src/ingest/pdf/text.rs:62-64] | Indexed function `normalize_page_text_whitespace_only_lines` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:62-64] |
| `normalize_page_text_empty_input` | function | `fn normalize_page_text_empty_input() {` | `normalize_page_text_empty_input [function]` | `ae9d61ab-19d6-5116-a47e-126ab81e7268` | 67-69 [crates/gwiki/src/ingest/pdf/text.rs:67-69] | Indexed function `normalize_page_text_empty_input` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:67-69] |
| `normalize_page_text_single_line` | function | `fn normalize_page_text_single_line() {` | `normalize_page_text_single_line [function]` | `cf4b7879-61e4-58a7-a115-4565247d9046` | 72-74 [crates/gwiki/src/ingest/pdf/text.rs:72-74] | Indexed function `normalize_page_text_single_line` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:72-74] |
| `normalize_page_text_no_blank_lines` | function | `fn normalize_page_text_no_blank_lines() {` | `normalize_page_text_no_blank_lines [function]` | `42d5bcb1-e10e-570f-bfa9-b0010ac3cad9` | 77-82 [crates/gwiki/src/ingest/pdf/text.rs:77-82] | Indexed function `normalize_page_text_no_blank_lines` in `crates/gwiki/src/ingest/pdf/text.rs`. [crates/gwiki/src/ingest/pdf/text.rs:77-82] |
