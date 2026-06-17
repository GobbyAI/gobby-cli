---
title: crates/gcode/src/index/parser/calls/text.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls/text.rs
  ranges:
  - 4-20
  - 22-30
  - 32-49
  - 51-53
  - 55-57
  - 59-61
  - 63-65
  - 67-153
  - 160-165
  - 168-174
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/parser/calls/text.rs:4-20](crates/gcode/src/index/parser/calls/text.rs#L4-L20), [crates/gcode/src/index/parser/calls/text.rs:22-30](crates/gcode/src/index/parser/calls/text.rs#L22-L30), [crates/gcode/src/index/parser/calls/text.rs:32-49](crates/gcode/src/index/parser/calls/text.rs#L32-L49), [crates/gcode/src/index/parser/calls/text.rs:51-53](crates/gcode/src/index/parser/calls/text.rs#L51-L53), [crates/gcode/src/index/parser/calls/text.rs:55-57](crates/gcode/src/index/parser/calls/text.rs#L55-L57), [crates/gcode/src/index/parser/calls/text.rs:59-61](crates/gcode/src/index/parser/calls/text.rs#L59-L61), [crates/gcode/src/index/parser/calls/text.rs:63-65](crates/gcode/src/index/parser/calls/text.rs#L63-L65), [crates/gcode/src/index/parser/calls/text.rs:67-153](crates/gcode/src/index/parser/calls/text.rs#L67-L153), [crates/gcode/src/index/parser/calls/text.rs:160-165](crates/gcode/src/index/parser/calls/text.rs#L160-L165), [crates/gcode/src/index/parser/calls/text.rs:168-174](crates/gcode/src/index/parser/calls/text.rs#L168-L174)

</details>

# crates/gcode/src/index/parser/calls/text.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

This file provides text and identifier utilities for the call-indexing parser. It converts byte offsets to UTF-16 columns while tolerating invalid UTF-8, measures line terminator length for test support, trims likely identifier tokens, and defines Unicode-aware start/continue checks plus a fast byte-level check for textual call names. The main `should_ignore_call_name` logic ties these helpers together by deciding when a parsed name should be skipped, and the tests confirm it ignores language keywords that resemble calls and accepts Unicode XID identifier characters.
[crates/gcode/src/index/parser/calls/text.rs:4-20]
[crates/gcode/src/index/parser/calls/text.rs:22-30]
[crates/gcode/src/index/parser/calls/text.rs:32-49]
[crates/gcode/src/index/parser/calls/text.rs:51-53]
[crates/gcode/src/index/parser/calls/text.rs:55-57]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `line_terminator_len` | function | `pub(in crate::index::parser) fn line_terminator_len(` | `line_terminator_len [function]` | `fdf5bec9-0f92-580b-ad2e-d55c1b4ab60c` | 4-20 [crates/gcode/src/index/parser/calls/text.rs:4-20] | Indexed function `line_terminator_len` in `crates/gcode/src/index/parser/calls/text.rs`. [crates/gcode/src/index/parser/calls/text.rs:4-20] |
| `utf16_column_at_byte` | function | `pub(super) fn utf16_column_at_byte(source: &[u8], byte_offset: usize) -> usize {` | `utf16_column_at_byte [function]` | `3b863457-e36d-5dad-a9b0-be2a70dadf05` | 22-30 [crates/gcode/src/index/parser/calls/text.rs:22-30] | Indexed function `utf16_column_at_byte` in `crates/gcode/src/index/parser/calls/text.rs`. [crates/gcode/src/index/parser/calls/text.rs:22-30] |
| `lossy_utf16_units` | function | `fn lossy_utf16_units(mut bytes: &[u8]) -> usize {` | `lossy_utf16_units [function]` | `e8df33ef-7361-5e81-9601-63ebdf33a38f` | 32-49 [crates/gcode/src/index/parser/calls/text.rs:32-49] | Indexed function `lossy_utf16_units` in `crates/gcode/src/index/parser/calls/text.rs`. [crates/gcode/src/index/parser/calls/text.rs:32-49] |
| `trim_identifier_token` | function | `pub(super) fn trim_identifier_token(token: &str) -> &str {` | `trim_identifier_token [function]` | `c03b08bd-256c-5124-9ad7-47206d4ca21c` | 51-53 [crates/gcode/src/index/parser/calls/text.rs:51-53] | Indexed function `trim_identifier_token` in `crates/gcode/src/index/parser/calls/text.rs`. [crates/gcode/src/index/parser/calls/text.rs:51-53] |
| `is_identifier_start` | function | `pub(super) fn is_identifier_start(ch: char) -> bool {` | `is_identifier_start [function]` | `761af537-d29e-5635-af22-70470219838a` | 55-57 [crates/gcode/src/index/parser/calls/text.rs:55-57] | Indexed function `is_identifier_start` in `crates/gcode/src/index/parser/calls/text.rs`. [crates/gcode/src/index/parser/calls/text.rs:55-57] |
| `is_identifier_continue` | function | `pub(super) fn is_identifier_continue(ch: char) -> bool {` | `is_identifier_continue [function]` | `d84b1f89-9474-5ae0-b6eb-11f06485d78b` | 59-61 [crates/gcode/src/index/parser/calls/text.rs:59-61] | Indexed function `is_identifier_continue` in `crates/gcode/src/index/parser/calls/text.rs`. [crates/gcode/src/index/parser/calls/text.rs:59-61] |
| `is_textual_call_name_byte` | function | `pub(super) fn is_textual_call_name_byte(byte: u8) -> bool {` | `is_textual_call_name_byte [function]` | `73d66dcf-5b03-5775-be09-6972894fa9a9` | 63-65 [crates/gcode/src/index/parser/calls/text.rs:63-65] | Indexed function `is_textual_call_name_byte` in `crates/gcode/src/index/parser/calls/text.rs`. [crates/gcode/src/index/parser/calls/text.rs:63-65] |
| `should_ignore_call_name` | function | `pub(super) fn should_ignore_call_name(language: &str, name: &str) -> bool {` | `should_ignore_call_name [function]` | `7c1d719b-94ea-51f9-a0d0-a3e8634e8930` | 67-153 [crates/gcode/src/index/parser/calls/text.rs:67-153] | Indexed function `should_ignore_call_name` in `crates/gcode/src/index/parser/calls/text.rs`. [crates/gcode/src/index/parser/calls/text.rs:67-153] |
| `ignores_language_keywords_that_look_like_calls` | function | `fn ignores_language_keywords_that_look_like_calls() {` | `ignores_language_keywords_that_look_like_calls [function]` | `1f52b771-0c46-5d29-b23d-58bc710bc9ff` | 160-165 [crates/gcode/src/index/parser/calls/text.rs:160-165] | Indexed function `ignores_language_keywords_that_look_like_calls` in `crates/gcode/src/index/parser/calls/text.rs`. [crates/gcode/src/index/parser/calls/text.rs:160-165] |
| `identifier_helpers_accept_unicode_xid_characters` | function | `fn identifier_helpers_accept_unicode_xid_characters() {` | `identifier_helpers_accept_unicode_xid_characters [function]` | `b5b569d3-26b9-53fc-980a-b47765407913` | 168-174 [crates/gcode/src/index/parser/calls/text.rs:168-174] | Indexed function `identifier_helpers_accept_unicode_xid_characters` in `crates/gcode/src/index/parser/calls/text.rs`. [crates/gcode/src/index/parser/calls/text.rs:168-174] |
