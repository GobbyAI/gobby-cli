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
  - 67-151
  - 158-163
  - 166-172
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser/calls/text.rs

Module: [[code/modules/crates/gcode/src/index/parser/calls|crates/gcode/src/index/parser/calls]]

## Purpose

`crates/gcode/src/index/parser/calls/text.rs` exposes 10 indexed API symbols.
[crates/gcode/src/index/parser/calls/text.rs:4-20]
[crates/gcode/src/index/parser/calls/text.rs:22-30]
[crates/gcode/src/index/parser/calls/text.rs:32-49]
[crates/gcode/src/index/parser/calls/text.rs:51-53]
[crates/gcode/src/index/parser/calls/text.rs:55-57]
[crates/gcode/src/index/parser/calls/text.rs:59-61]
[crates/gcode/src/index/parser/calls/text.rs:63-65]
[crates/gcode/src/index/parser/calls/text.rs:67-151]
[crates/gcode/src/index/parser/calls/text.rs:158-163]
[crates/gcode/src/index/parser/calls/text.rs:166-172]

## API Symbols

- `line_terminator_len` (function) component `line_terminator_len [function]` (`fdf5bec9-0f92-580b-ad2e-d55c1b4ab60c`) lines 4-20 [crates/gcode/src/index/parser/calls/text.rs:4-20]
  - Signature: `pub(in crate::index::parser) fn line_terminator_len(`
  - Purpose: Returns the byte length of the line terminator (CRLF=2, LF=1, or none=0) immediately following a line at the position indicated by `line_start_byte + line_len`. [crates/gcode/src/index/parser/calls/text.rs:4-20]
- `utf16_column_at_byte` (function) component `utf16_column_at_byte [function]` (`3b863457-e36d-5dad-a9b0-be2a70dadf05`) lines 22-30 [crates/gcode/src/index/parser/calls/text.rs:22-30]
  - Signature: `pub(super) fn utf16_column_at_byte(source: &[u8], byte_offset: usize) -> usize {`
  - Purpose: Computes the UTF-16 code unit count from the beginning of the current line to a specified byte offset in the source. [crates/gcode/src/index/parser/calls/text.rs:22-30]
- `lossy_utf16_units` (function) component `lossy_utf16_units [function]` (`e8df33ef-7361-5e81-9601-63ebdf33a38f`) lines 32-49 [crates/gcode/src/index/parser/calls/text.rs:32-49]
  - Signature: `fn lossy_utf16_units(mut bytes: &[u8]) -> usize {`
  - Purpose: Computes the number of UTF-16 code units required to encode a byte slice, treating invalid UTF-8 sequences as replacement characters (U+FFFD). [crates/gcode/src/index/parser/calls/text.rs:32-49]
- `trim_identifier_token` (function) component `trim_identifier_token [function]` (`c03b08bd-256c-5124-9ad7-47206d4ca21c`) lines 51-53 [crates/gcode/src/index/parser/calls/text.rs:51-53]
  - Signature: `pub(super) fn trim_identifier_token(token: &str) -> &str {`
  - Purpose: This function removes leading and trailing non-identifier characters from a string by trimming all characters that fail the `is_identifier_continue` predicate. [crates/gcode/src/index/parser/calls/text.rs:51-53]
- `is_identifier_start` (function) component `is_identifier_start [function]` (`761af537-d29e-5635-af22-70470219838a`) lines 55-57 [crates/gcode/src/index/parser/calls/text.rs:55-57]
  - Signature: `pub(super) fn is_identifier_start(ch: char) -> bool {`
  - Purpose: Returns `true` if the character satisfies the Unicode XID_Start property or is an underscore or dollar sign, determining whether it can begin an identifier. [crates/gcode/src/index/parser/calls/text.rs:55-57]
- `is_identifier_continue` (function) component `is_identifier_continue [function]` (`d84b1f89-9474-5ae0-b6eb-11f06485d78b`) lines 59-61 [crates/gcode/src/index/parser/calls/text.rs:59-61]
  - Signature: `pub(super) fn is_identifier_continue(ch: char) -> bool {`
  - Purpose: This function returns `true` if a character is valid for continuing an identifier, which includes Unicode XID_Continue characters plus underscore and dollar sign. [crates/gcode/src/index/parser/calls/text.rs:59-61]
- `is_textual_call_name_byte` (function) component `is_textual_call_name_byte [function]` (`73d66dcf-5b03-5775-be09-6972894fa9a9`) lines 63-65 [crates/gcode/src/index/parser/calls/text.rs:63-65]
  - Signature: `pub(super) fn is_textual_call_name_byte(byte: u8) -> bool {`
  - Purpose: Returns `true` if the byte is a valid character for a textual call name: alphanumeric or one of `_`, `$`, `!`, `?`. [crates/gcode/src/index/parser/calls/text.rs:63-65]
- `should_ignore_call_name` (function) component `should_ignore_call_name [function]` (`7c1d719b-94ea-51f9-a0d0-a3e8634e8930`) lines 67-151 [crates/gcode/src/index/parser/calls/text.rs:67-151]
  - Signature: `pub(super) fn should_ignore_call_name(language: &str, name: &str) -> bool {`
  - Purpose: Returns `true` if the given name is a reserved keyword or language-specific special form for the specified programming language (Dart, Elixir, or Kotlin). [crates/gcode/src/index/parser/calls/text.rs:67-151]
- `ignores_language_keywords_that_look_like_calls` (function) component `ignores_language_keywords_that_look_like_calls [function]` (`c93f116e-886b-57d7-9591-c47dab4c5380`) lines 158-163 [crates/gcode/src/index/parser/calls/text.rs:158-163]
  - Signature: `fn ignores_language_keywords_that_look_like_calls() {`
  - Purpose: This test function verifies that `should_ignore_call_name` correctly identifies and excludes language-specific keywords (await, object, with) that syntactically resemble function calls while preserving actual function identifiers. [crates/gcode/src/index/parser/calls/text.rs:158-163]
- `identifier_helpers_accept_unicode_xid_characters` (function) component `identifier_helpers_accept_unicode_xid_characters [function]` (`652e44d5-64b2-5fd4-bd27-4d0381e2b588`) lines 166-172 [crates/gcode/src/index/parser/calls/text.rs:166-172]
  - Signature: `fn identifier_helpers_accept_unicode_xid_characters() {`
  - Purpose: This test asserts that the `is_identifier_start()` and `is_identifier_continue()` functions correctly recognize Unicode XID characters (including combining marks) and ASCII symbols as valid identifier components. [crates/gcode/src/index/parser/calls/text.rs:166-172]

