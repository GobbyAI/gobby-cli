---
title: crates/gcode/src/index/parser/calls/dart_textual.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls/dart_textual.rs
  ranges:
  - 8-55
  - 57-77
  - 79-168
  - 170-172
  - 174-189
  - 191-216
  - 218-223
  - 226-232
  - 234-244
  - 247-252
  - 255-259
  - 261-371
  - 373-375
  - 377-379
  - 381-391
  - 393-417
  - 419-441
  - 443-492
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser/calls/dart_textual.rs

Module: [[code/modules/crates/gcode/src/index/parser/calls|crates/gcode/src/index/parser/calls]]

## Purpose

This file implements a text-based Dart call extractor that scans source line by line, tracks lexical state for comments, strings, class scope, and line boundaries, then finds dot-notation call candidates and filters out false positives from declarations, comments, strings, imports/exports, and other ignored names before materializing `CallRelation` records with optional semantic resolution. The helper routines support that pipeline by splitting source into line spans, recognizing textual call syntax, handling generic angle brackets, detecting Dart string starts, and distinguishing function or type declarations from real call sites.
[crates/gcode/src/index/parser/calls/dart_textual.rs:8-55]
[crates/gcode/src/index/parser/calls/dart_textual.rs:57-77]
[crates/gcode/src/index/parser/calls/dart_textual.rs:79-168]
[crates/gcode/src/index/parser/calls/dart_textual.rs:170-172]
[crates/gcode/src/index/parser/calls/dart_textual.rs:174-189]

## API Symbols

- `extract_textual_dart_calls` (function) component `extract_textual_dart_calls [function]` (`e61b2a21-72d5-5d34-8e75-b367e3ad76ba`) lines 8-55 [crates/gcode/src/index/parser/calls/dart_textual.rs:8-55]
  - Signature: `pub(super) fn extract_textual_dart_calls(`
  - Purpose: # Summary

Extracts Dart method call relations from source code by scanning each line for dot-notation call candidates, filtering out false positives via syntactic context and declaration type checks, and materializing valid calls with optional semantic resolution. [crates/gcode/src/index/parser/calls/dart_textual.rs:8-55]
- `source_line_spans` (function) component `source_line_spans [function]` (`2738a422-f288-534e-a366-5e9e46974efe`) lines 57-77 [crates/gcode/src/index/parser/calls/dart_textual.rs:57-77]
  - Signature: `fn source_line_spans(source: &[u8]) -> Vec<(usize, &[u8])> {`
  - Purpose: Returns a vector of tuples pairing each line's starting byte offset with its content (excluding line terminators) for a byte slice. [crates/gcode/src/index/parser/calls/dart_textual.rs:57-77]
- `textual_call_candidates` (function) component `textual_call_candidates [function]` (`3159fb65-0a43-5df8-b392-1bc39ff422a6`) lines 79-168 [crates/gcode/src/index/parser/calls/dart_textual.rs:79-168]
  - Signature: `fn textual_call_candidates(`
  - Purpose: # Summary

`textual_call_candidates` parses a source code line to extract potential function call sites by identifying identifiers (optionally with generic parameters and path qualifiers) that precede opening parentheses, while filtering out function declarations. [crates/gcode/src/index/parser/calls/dart_textual.rs:79-168]
- `is_textual_qualifier_byte` (function) component `is_textual_qualifier_byte [function]` (`044945e8-53b2-5a84-abe4-a18304877a11`) lines 170-172 [crates/gcode/src/index/parser/calls/dart_textual.rs:170-172]
  - Signature: `fn is_textual_qualifier_byte(byte: u8) -> bool {`
  - Purpose: Returns `true` if the byte is an ASCII alphanumeric character, underscore, or dollar sign; `false` otherwise. [crates/gcode/src/index/parser/calls/dart_textual.rs:170-172]
- `matching_angle_start` (function) component `matching_angle_start [function]` (`75250a72-74e8-5862-ad9b-51b8a6da1a65`) lines 174-189 [crates/gcode/src/index/parser/calls/dart_textual.rs:174-189]
  - Signature: `fn matching_angle_start(bytes: &[u8], close_idx: usize) -> Option<usize> {`
  - Purpose: # Summary

This function performs a reverse linear scan from `close_idx` to locate the matching opening angle bracket (`<`) for a closing angle bracket (`>`) at the given index, accounting for nested generic angle brackets through depth tracking. [crates/gcode/src/index/parser/calls/dart_textual.rs:174-189]
- `angle_looks_like_generic_delimiter` (function) component `angle_looks_like_generic_delimiter [function]` (`647ac655-f5a8-5f0d-a60f-33c8ea2c9ce2`) lines 191-216 [crates/gcode/src/index/parser/calls/dart_textual.rs:191-216]
  - Signature: `fn angle_looks_like_generic_delimiter(bytes: &[u8], idx: usize) -> bool {`
  - Purpose: Determines whether a `<` or `>` byte at the specified position is a generic type delimiter rather than a comparison or bitwise operator by rejecting cases where it's part of multi-character operators (`<<`, `<=`, `>=`) or is adjacent to angle operator neighbor characters. [crates/gcode/src/index/parser/calls/dart_textual.rs:191-216]
- `is_angle_operator_neighbor` (function) component `is_angle_operator_neighbor [function]` (`18b2b0c1-9d75-540c-945d-d4927534fe86`) lines 218-223 [crates/gcode/src/index/parser/calls/dart_textual.rs:218-223]
  - Signature: `fn is_angle_operator_neighbor(byte: u8) -> bool {`
  - Purpose: Returns true if the byte is one of the binary operators (`=`, `<`, `>`, `!`, `&`, `|`, `+`, `-`, `*`, `/`, `^`, `%`) that can appear adjacent to angle bracket operators. [crates/gcode/src/index/parser/calls/dart_textual.rs:218-223]
- `DartScanState` (class) component `DartScanState [class]` (`a0546f1a-f17f-57c6-b2ff-422ba208d0c1`) lines 226-232 [crates/gcode/src/index/parser/calls/dart_textual.rs:226-232]
  - Signature: `struct DartScanState {`
  - Purpose: `DartScanState` maintains lexical scanner state for Dart code by tracking block comment and string parsing contexts, brace nesting depth, and class body declaration scopes. [crates/gcode/src/index/parser/calls/dart_textual.rs:226-232]
- `DartScanState` (class) component `DartScanState [class]` (`6baf9d3f-da3f-5253-b8b2-51b1f14b40bf`) lines 234-244 [crates/gcode/src/index/parser/calls/dart_textual.rs:234-244]
  - Signature: `impl DartScanState {`
  - Purpose: DartScanState provides context-aware predicates for Dart source scanning, determining whether the current position represents executable code and whether it resides within a class member scope. [crates/gcode/src/index/parser/calls/dart_textual.rs:234-244]
- `DartScanState.is_code` (method) component `DartScanState.is_code [method]` (`1f8978c2-802f-5f74-bade-eb9b8c282f14`) lines 235-237 [crates/gcode/src/index/parser/calls/dart_textual.rs:235-237]
  - Signature: `fn is_code(&self) -> bool {`
  - Purpose: Returns `true` if the current parser position is in code, i.e., not inside a block comment and not inside a string literal. [crates/gcode/src/index/parser/calls/dart_textual.rs:235-237]
- `DartScanState.in_class_member_scope` (method) component `DartScanState.in_class_member_scope [method]` (`c1a66187-3bcc-5091-b205-1883d9e3935b`) lines 239-243 [crates/gcode/src/index/parser/calls/dart_textual.rs:239-243]
  - Signature: `fn in_class_member_scope(&self) -> bool {`
  - Purpose: Returns `true` if the current brace depth matches the most recent class body depth, indicating the parser is currently within a class member scope. [crates/gcode/src/index/parser/calls/dart_textual.rs:239-243]
- `DartStringState` (class) component `DartStringState [class]` (`c94c5b27-366d-50be-b9e8-f8f2e7af1dc8`) lines 247-252 [crates/gcode/src/index/parser/calls/dart_textual.rs:247-252]
  - Signature: `struct DartStringState {`
  - Purpose: `DartStringState` is a struct that tracks the parsing state of a Dart string literal, maintaining the quote character type, triple-quote flag, raw string flag, and escape character status. [crates/gcode/src/index/parser/calls/dart_textual.rs:247-252]
- `DartLineScan` (class) component `DartLineScan [class]` (`826e8df3-be70-5ac4-ada1-55a31359f6ff`) lines 255-259 [crates/gcode/src/index/parser/calls/dart_textual.rs:255-259]
  - Signature: `struct DartLineScan {`
  - Purpose: `DartLineScan` is a structure that stores the byte-by-byte parsing state progression for a Dart source line, including state transitions at each byte position, the starting position of any line comment, and the final scanning state. [crates/gcode/src/index/parser/calls/dart_textual.rs:255-259]
- `DartLineScan` (class) component `DartLineScan [class]` (`b7006ee4-fd09-55a8-b408-ca7ca1e92081`) lines 261-371 [crates/gcode/src/index/parser/calls/dart_textual.rs:261-371]
  - Signature: `impl DartLineScan {`
  - Purpose: # DartLineScan::new Summary

A byte-by-byte lexical scanner for Dart source code that constructs a state vector recording parser state at each byte offset, handling block comments, string literals (including raw and triple-quoted variants), escape sequences, and type declarations. [crates/gcode/src/index/parser/calls/dart_textual.rs:261-371]
- `DartLineScan.new` (method) component `DartLineScan.new [method]` (`f3fb79da-43d4-545c-b031-131b84dca8a2`) lines 262-362 [crates/gcode/src/index/parser/calls/dart_textual.rs:262-362]
  - Signature: `fn new(line: &str, mut state: DartScanState) -> Self {`
  - Purpose: # Summary

Constructs a lexical scanner that parses a Dart source line byte-by-byte, recording the parser state at each position while tracking block comments, string literals, and escape sequences. [crates/gcode/src/index/parser/calls/dart_textual.rs:262-362]
- `DartLineScan.state_at` (method) component `DartLineScan.state_at [method]` (`ddf1d64c-873e-530c-8e50-7993d3724101`) lines 364-366 [crates/gcode/src/index/parser/calls/dart_textual.rs:364-366]
  - Signature: `fn state_at(&self, byte: usize) -> &DartScanState {`
  - Purpose: Returns a reference to the `DartScanState` at the specified byte index, clamped to the last valid state if the index exceeds the array bounds. [crates/gcode/src/index/parser/calls/dart_textual.rs:364-366]
- `DartLineScan.in_line_comment` (method) component `DartLineScan.in_line_comment [method]` (`8a1a9ca2-9049-55c1-b8f6-bc61d1c51cab`) lines 368-370 [crates/gcode/src/index/parser/calls/dart_textual.rs:368-370]
  - Signature: `fn in_line_comment(&self, byte: usize) -> bool {`
  - Purpose: Returns true if the given byte offset is at or beyond the stored line comment start position, indicating the byte lies within an active line comment. [crates/gcode/src/index/parser/calls/dart_textual.rs:368-370]
- `record_scan_state` (function) component `record_scan_state [function]` (`c3e16433-934e-5dfc-a56a-f42893a6a5b1`) lines 373-375 [crates/gcode/src/index/parser/calls/dart_textual.rs:373-375]
  - Signature: `fn record_scan_state(states: &mut Vec<DartScanState>, count: usize, state: &DartScanState) {`
  - Purpose: Appends `count` clones of the provided `DartScanState` to the mutable vector. [crates/gcode/src/index/parser/calls/dart_textual.rs:373-375]
- `dart_textual_candidate_in_ignored_context` (function) component `dart_textual_candidate_in_ignored_context [function]` (`dcc92820-a198-56bc-bbad-0abad5c21c36`) lines 377-379 [crates/gcode/src/index/parser/calls/dart_textual.rs:377-379]
  - Signature: `fn dart_textual_candidate_in_ignored_context(scan: &DartLineScan, candidate_byte: usize) -> bool {`
  - Purpose: Returns true if the candidate byte position is located within a line comment or a non-code language state context. [crates/gcode/src/index/parser/calls/dart_textual.rs:377-379]
- `dart_line_starts_type_declaration` (function) component `dart_line_starts_type_declaration [function]` (`3efdcaae-3db8-5670-b839-7d379eb7a396`) lines 381-391 [crates/gcode/src/index/parser/calls/dart_textual.rs:381-391]
  - Signature: `fn dart_line_starts_type_declaration(line: &str) -> bool {`
  - Purpose: This function returns `true` if the input line, after trimming leading whitespace, begins with any Dart type declaration keyword (class variants, enum, mixin, or extension). [crates/gcode/src/index/parser/calls/dart_textual.rs:381-391]
- `empty_prefix_semicolon_declaration_in_class` (function) component `empty_prefix_semicolon_declaration_in_class [function]` (`c99e04de-c6b8-5a5a-90af-0d60d1bc23f3`) lines 393-417 [crates/gcode/src/index/parser/calls/dart_textual.rs:393-417]
  - Signature: `fn empty_prefix_semicolon_declaration_in_class(`
  - Purpose: Determines if a position marks an abstract method declaration in a Dart class scope, identified by an empty prefix, parenthesized parameter list, and semicolon terminator outside comments. [crates/gcode/src/index/parser/calls/dart_textual.rs:393-417]
- `dart_string_start` (function) component `dart_string_start [function]` (`0467e7e4-5fdd-570e-9d33-c53d9783c68f`) lines 419-441 [crates/gcode/src/index/parser/calls/dart_textual.rs:419-441]
  - Signature: `fn dart_string_start(bytes: &[u8], idx: usize) -> Option<(DartStringState, usize)> {`
  - Purpose: Detects and parses the opening of a Dart string literal at the given index, returning the string state (quote character, raw prefix, triple-quote flag) and bytes consumed, or None if no valid string opening is found. [crates/gcode/src/index/parser/calls/dart_textual.rs:419-441]
- `looks_like_textual_function_declaration` (function) component `looks_like_textual_function_declaration [function]` (`9ed7304a-528a-586b-adb5-856d6b59e102`) lines 443-492 [crates/gcode/src/index/parser/calls/dart_textual.rs:443-492]
  - Signature: `fn looks_like_textual_function_declaration(`
  - Purpose: # Summary

This function validates whether a line segment at a given position represents a function declaration by checking for a valid declaration tail (e.g., `{`, `=>`, `;`) and confirming the preceding context contains a recognized type keyword, generic annotation, or type-like identifier. [crates/gcode/src/index/parser/calls/dart_textual.rs:443-492]

