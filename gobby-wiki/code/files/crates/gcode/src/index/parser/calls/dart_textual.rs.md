---
title: crates/gcode/src/index/parser/calls/dart_textual.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls/dart_textual.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser/calls/dart_textual.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

`crates/gcode/src/index/parser/calls/dart_textual.rs` exposes 21 indexed API symbols.

## How it fits

`crates/gcode/src/index/parser/calls/dart_textual.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `extract_textual_dart_calls` | function | Scans a Dart source buffer line by line, skips import/export/type/class declarations and other ignored textual contexts, filters out disallowed call names, and materializes a 'CallRelation' for each remaining textual '.'-based call candidate using the optional semantic resolver. [crates/gcode/src/index/parser/calls/dart_textual.rs:8-55] |
| `source_line_spans` | function | Returns a vector of '(byte_offset, line_slice)' pairs for each line in 'source', splitting on '\n' and stripping a trailing '\r' from each line slice while preserving the original start index. [crates/gcode/src/index/parser/calls/dart_textual.rs:57-77] |
| `textual_call_candidates` | function | Scans a single source line for '('-terminated textual call expressions, backtracks to extract the callee name and optional qualified path (including generic type arguments), skips likely function declarations, and returns corresponding 'CallSite' candidates with byte-range/line metadata. [crates/gcode/src/index/parser/calls/dart_textual.rs:79-168] |
| `is_textual_qualifier_byte` | function | Returns 'true' if the byte is an ASCII alphanumeric character or one of the qualifier characters '_' or '$', otherwise 'false'. [crates/gcode/src/index/parser/calls/dart_textual.rs:170-172] |
| `matching_angle_start` | function | Scans backward from 'close_idx' through 'bytes', tracking nested generic angle delimiters, and returns the index of the matching opening '<' for the closing '>' at 'close_idx' if one is found, otherwise 'None'. [crates/gcode/src/index/parser/calls/dart_textual.rs:174-189] |
| `angle_looks_like_generic_delimiter` | function | Returns 'true' when the byte at 'idx' is a '<' or '>' that does not appear to be part of a shift/comparison/operator sequence, based on its immediate neighbors, and 'false' otherwise. [crates/gcode/src/index/parser/calls/dart_textual.rs:191-216] |
| `is_angle_operator_neighbor` | function | Returns 'true' if the byte is one of '=', '<', '>', '!', '&', '\|', '+', '-', '*', '/', '^', or '%', indicating an operator character that can neighbor angle brackets. [crates/gcode/src/index/parser/calls/dart_textual.rs:218-223] |
| `DartScanState` | class | 'DartScanState' tracks the current lexical scanning context for Dart code, including whether the scanner is inside a block comment or string, the current brace nesting depth, whether a class body is pending, and a stack of class-body brace depths. [crates/gcode/src/index/parser/calls/dart_textual.rs:226-232] |
| `DartScanState::is_code` | method | Returns 'true' when the current token is not inside a block comment and not inside a string literal ('self.string.is_none()'), otherwise 'false'. [crates/gcode/src/index/parser/calls/dart_textual.rs:235-237] |
| `DartScanState::in_class_member_scope` | method | Returns 'true' when there is a recorded innermost class body depth and the current 'brace_depth' exactly matches that depth, meaning the parser is at class member scope. [crates/gcode/src/index/parser/calls/dart_textual.rs:239-243] |
| `DartStringState` | class | 'DartStringState' is a small state record for parsing Dart string literals, tracking the quote delimiter, whether the string is triple-quoted or raw, and whether the parser is currently in an escaped state. [crates/gcode/src/index/parser/calls/dart_textual.rs:247-252] |
| `DartLineScan` | class | 'DartLineScan' is a scan summary for a line of Dart source containing the per-byte lexer states, the starting byte offset of any line comment, and the final lexer state after scanning the line. [crates/gcode/src/index/parser/calls/dart_textual.rs:255-259] |
| `DartLineScan::new` | method | Scans a Dart source line byte by byte to update and record lexical state transitions for block comments and string literals, while also flagging a pending class body when a type declaration starts in code. [crates/gcode/src/index/parser/calls/dart_textual.rs:262-362] |
| `DartLineScan::state_at` | method | Returns a reference to the 'DartScanState' stored at the given byte index, clamping the index to the last valid entry if 'byte' exceeds the bounds of 'states_at_byte'. [crates/gcode/src/index/parser/calls/dart_textual.rs:364-366] |
| `DartLineScan::in_line_comment` | method | Returns 'true' when 'line_comment_start' is set and the given byte offset is greater than or equal to that start position, indicating the byte lies within an in-line comment. [crates/gcode/src/index/parser/calls/dart_textual.rs:368-370] |
| `record_scan_state` | function | 'record_scan_state' appends 'count' cloned copies of 'state' to the end of 'states'. [crates/gcode/src/index/parser/calls/dart_textual.rs:373-375] |
| `dart_textual_candidate_in_ignored_context` | function | Returns 'true' when the candidate byte lies inside a line comment or at a position whose scan state is not code, indicating the textual candidate is in an ignored context. [crates/gcode/src/index/parser/calls/dart_textual.rs:377-379] |
| `dart_line_starts_type_declaration` | function | Returns 'true' if the line, after left-trimming whitespace, begins with a Dart type declaration keyword such as 'class', 'abstract class', 'base class', 'final class', 'interface class', 'enum', 'mixin', or 'extension'. [crates/gcode/src/index/parser/calls/dart_textual.rs:381-391] |
| `empty_prefix_semicolon_declaration_in_class` | function | Returns 'true' only for a class-member declaration whose prefix before 'name_start' is blank, is immediately followed by a parenthesized parameter list and a trailing semicolon, and is not inside a line comment according to 'scan'. [crates/gcode/src/index/parser/calls/dart_textual.rs:393-417] |
| `dart_string_start` | function | Parses the start of a Dart string literal at 'idx', recognizing optional raw prefixes ('r'), single vs. triple quoting, and returns the initial 'DartStringState' plus the number of bytes consumed, or 'None' if no string start is present. [crates/gcode/src/index/parser/calls/dart_textual.rs:419-441] |
| `looks_like_textual_function_declaration` | function | Returns 'true' when a line syntactically resembles a textual function declaration by requiring a declaration-like suffix after the parameter list and a plausible type/identifier prefix before the name, while rejecting expressions or calls with disallowed preceding tokens. [crates/gcode/src/index/parser/calls/dart_textual.rs:443-492] |

