---
title: crates/gcode/src/index/parser/calls/text.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls/text.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser/calls/text.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

`crates/gcode/src/index/parser/calls/text.rs` exposes 10 indexed API symbols.

## How it fits

`crates/gcode/src/index/parser/calls/text.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `line_terminator_len` | function | Returns the byte length of the line terminator immediately following a line segment in 'text' given its starting byte and length, returning '2' for '\r\n', '1' for '\n', and '0' when no terminator is present or the slice is out of bounds. [crates/gcode/src/index/parser/calls/text.rs:4-20] |
| `utf16_column_at_byte` | function | Clamps 'byte_offset' to 'source.len()', finds the start of the current line by scanning backward for the last '\n', and returns the number of UTF-16 code units in the bytes between that line start and the clamped offset via 'lossy_utf16_units'. [crates/gcode/src/index/parser/calls/text.rs:22-30] |
| `lossy_utf16_units` | function | It computes the number of UTF-16 code units that would result from lossily decoding the byte slice as UTF-8, counting each invalid UTF-8 sequence as one replacement character ('U+FFFD') and each valid character by its UTF-16 length. [crates/gcode/src/index/parser/calls/text.rs:32-49] |
| `trim_identifier_token` | function | Returns the input 'token' with all leading and trailing characters removed that do not satisfy 'is_identifier_continue', yielding the longest contiguous identifier-continuation substring. [crates/gcode/src/index/parser/calls/text.rs:51-53] |
| `is_identifier_start` | function | Returns 'true' if 'ch' is a valid Unicode identifier start character per 'UnicodeXID::is_xid_start', or if it is '_' or '$', and 'false' otherwise. [crates/gcode/src/index/parser/calls/text.rs:55-57] |
| `is_identifier_continue` | function | Returns 'true' when 'ch' is a valid Unicode identifier continuation character according to 'UnicodeXID::is_xid_continue', or when it is '_' or '$'. [crates/gcode/src/index/parser/calls/text.rs:59-61] |
| `is_textual_call_name_byte` | function | Returns 'true' if the byte is an ASCII alphanumeric character or one of '_', '$', '!', or '?', indicating it is valid within a textual call name. [crates/gcode/src/index/parser/calls/text.rs:63-65] |
| `should_ignore_call_name` | function | Returns 'true' when 'name' is a language-specific reserved keyword or special form that should be ignored as a call name for the given 'language' ('dart', 'elixir', or 'kotlin'), and 'false' otherwise. [crates/gcode/src/index/parser/calls/text.rs:67-153] |
| `ignores_language_keywords_that_look_like_calls` | function | Verifies that 'should_ignore_call_name' returns 'true' for reserved language keywords that resemble call names in Dart, Kotlin, and Elixir, and 'false' for a normal identifier like 'fetchUser'. [crates/gcode/src/index/parser/calls/text.rs:160-165] |
| `identifier_helpers_accept_unicode_xid_characters` | function | Verifies that the identifier helper predicates accept Unicode XID-start and XID-continue characters, including 'λ', 'é', a combining acute accent, '_' as a valid start, and '$' as a valid continuation. [crates/gcode/src/index/parser/calls/text.rs:168-174] |

