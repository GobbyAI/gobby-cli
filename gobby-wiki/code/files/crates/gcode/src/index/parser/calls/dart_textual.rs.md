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
  - 235-237
  - 239-243
  - 247-252
  - 255-259
  - 262-362
  - 364-366
  - 368-370
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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/parser/calls/dart_textual.rs:8-55](crates/gcode/src/index/parser/calls/dart_textual.rs#L8-L55), [crates/gcode/src/index/parser/calls/dart_textual.rs:57-77](crates/gcode/src/index/parser/calls/dart_textual.rs#L57-L77), [crates/gcode/src/index/parser/calls/dart_textual.rs:79-168](crates/gcode/src/index/parser/calls/dart_textual.rs#L79-L168), [crates/gcode/src/index/parser/calls/dart_textual.rs:170-172](crates/gcode/src/index/parser/calls/dart_textual.rs#L170-L172), [crates/gcode/src/index/parser/calls/dart_textual.rs:174-189](crates/gcode/src/index/parser/calls/dart_textual.rs#L174-L189), [crates/gcode/src/index/parser/calls/dart_textual.rs:191-216](crates/gcode/src/index/parser/calls/dart_textual.rs#L191-L216), [crates/gcode/src/index/parser/calls/dart_textual.rs:218-223](crates/gcode/src/index/parser/calls/dart_textual.rs#L218-L223), [crates/gcode/src/index/parser/calls/dart_textual.rs:226-232](crates/gcode/src/index/parser/calls/dart_textual.rs#L226-L232), [crates/gcode/src/index/parser/calls/dart_textual.rs:235-237](crates/gcode/src/index/parser/calls/dart_textual.rs#L235-L237), [crates/gcode/src/index/parser/calls/dart_textual.rs:239-243](crates/gcode/src/index/parser/calls/dart_textual.rs#L239-L243), [crates/gcode/src/index/parser/calls/dart_textual.rs:247-252](crates/gcode/src/index/parser/calls/dart_textual.rs#L247-L252), [crates/gcode/src/index/parser/calls/dart_textual.rs:255-259](crates/gcode/src/index/parser/calls/dart_textual.rs#L255-L259), [crates/gcode/src/index/parser/calls/dart_textual.rs:262-362](crates/gcode/src/index/parser/calls/dart_textual.rs#L262-L362), [crates/gcode/src/index/parser/calls/dart_textual.rs:364-366](crates/gcode/src/index/parser/calls/dart_textual.rs#L364-L366), [crates/gcode/src/index/parser/calls/dart_textual.rs:368-370](crates/gcode/src/index/parser/calls/dart_textual.rs#L368-L370), [crates/gcode/src/index/parser/calls/dart_textual.rs:373-375](crates/gcode/src/index/parser/calls/dart_textual.rs#L373-L375), [crates/gcode/src/index/parser/calls/dart_textual.rs:377-379](crates/gcode/src/index/parser/calls/dart_textual.rs#L377-L379), [crates/gcode/src/index/parser/calls/dart_textual.rs:381-391](crates/gcode/src/index/parser/calls/dart_textual.rs#L381-L391), [crates/gcode/src/index/parser/calls/dart_textual.rs:393-417](crates/gcode/src/index/parser/calls/dart_textual.rs#L393-L417), [crates/gcode/src/index/parser/calls/dart_textual.rs:419-441](crates/gcode/src/index/parser/calls/dart_textual.rs#L419-L441), [crates/gcode/src/index/parser/calls/dart_textual.rs:443-492](crates/gcode/src/index/parser/calls/dart_textual.rs#L443-L492)

</details>

# crates/gcode/src/index/parser/calls/dart_textual.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

Implements a textual Dart call extractor for the call indexer. It walks the source line by line, maintains lightweight scan state for code, strings, comments, and class-member context, and uses that state to find call-like candidates, filter out declarations and other ignored contexts, and materialize `CallRelation` entries with optional semantic resolution.

The helper functions and small state structs work together to support the heuristics: line-span splitting, candidate detection, qualifier and angle-bracket checks, declaration and string-start detection, and per-line scan bookkeeping that suppresses false positives before a call is recorded.
[crates/gcode/src/index/parser/calls/dart_textual.rs:8-55]
[crates/gcode/src/index/parser/calls/dart_textual.rs:57-77]
[crates/gcode/src/index/parser/calls/dart_textual.rs:79-168]
[crates/gcode/src/index/parser/calls/dart_textual.rs:170-172]
[crates/gcode/src/index/parser/calls/dart_textual.rs:174-189]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `extract_textual_dart_calls` | function | `pub(super) fn extract_textual_dart_calls(` | `extract_textual_dart_calls [function]` | `e61b2a21-72d5-5d34-8e75-b367e3ad76ba` | 8-55 [crates/gcode/src/index/parser/calls/dart_textual.rs:8-55] | Indexed function `extract_textual_dart_calls` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:8-55] |
| `source_line_spans` | function | `fn source_line_spans(source: &[u8]) -> Vec<(usize, &[u8])> {` | `source_line_spans [function]` | `2738a422-f288-534e-a366-5e9e46974efe` | 57-77 [crates/gcode/src/index/parser/calls/dart_textual.rs:57-77] | Indexed function `source_line_spans` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:57-77] |
| `textual_call_candidates` | function | `fn textual_call_candidates(` | `textual_call_candidates [function]` | `3159fb65-0a43-5df8-b392-1bc39ff422a6` | 79-168 [crates/gcode/src/index/parser/calls/dart_textual.rs:79-168] | Indexed function `textual_call_candidates` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:79-168] |
| `is_textual_qualifier_byte` | function | `fn is_textual_qualifier_byte(byte: u8) -> bool {` | `is_textual_qualifier_byte [function]` | `044945e8-53b2-5a84-abe4-a18304877a11` | 170-172 [crates/gcode/src/index/parser/calls/dart_textual.rs:170-172] | Indexed function `is_textual_qualifier_byte` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:170-172] |
| `matching_angle_start` | function | `fn matching_angle_start(bytes: &[u8], close_idx: usize) -> Option<usize> {` | `matching_angle_start [function]` | `75250a72-74e8-5862-ad9b-51b8a6da1a65` | 174-189 [crates/gcode/src/index/parser/calls/dart_textual.rs:174-189] | Indexed function `matching_angle_start` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:174-189] |
| `angle_looks_like_generic_delimiter` | function | `fn angle_looks_like_generic_delimiter(bytes: &[u8], idx: usize) -> bool {` | `angle_looks_like_generic_delimiter [function]` | `647ac655-f5a8-5f0d-a60f-33c8ea2c9ce2` | 191-216 [crates/gcode/src/index/parser/calls/dart_textual.rs:191-216] | Indexed function `angle_looks_like_generic_delimiter` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:191-216] |
| `is_angle_operator_neighbor` | function | `fn is_angle_operator_neighbor(byte: u8) -> bool {` | `is_angle_operator_neighbor [function]` | `18b2b0c1-9d75-540c-945d-d4927534fe86` | 218-223 [crates/gcode/src/index/parser/calls/dart_textual.rs:218-223] | Indexed function `is_angle_operator_neighbor` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:218-223] |
| `DartScanState` | class | `struct DartScanState {` | `DartScanState [class]` | `a0546f1a-f17f-57c6-b2ff-422ba208d0c1` | 226-232 [crates/gcode/src/index/parser/calls/dart_textual.rs:226-232] | Indexed class `DartScanState` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:226-232] |
| `DartScanState::is_code` | method | `fn is_code(&self) -> bool {` | `DartScanState::is_code [method]` | `1f8978c2-802f-5f74-bade-eb9b8c282f14` | 235-237 [crates/gcode/src/index/parser/calls/dart_textual.rs:235-237] | Indexed method `DartScanState::is_code` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:235-237] |
| `DartScanState::in_class_member_scope` | method | `fn in_class_member_scope(&self) -> bool {` | `DartScanState::in_class_member_scope [method]` | `c1a66187-3bcc-5091-b205-1883d9e3935b` | 239-243 [crates/gcode/src/index/parser/calls/dart_textual.rs:239-243] | Indexed method `DartScanState::in_class_member_scope` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:239-243] |
| `DartStringState` | class | `struct DartStringState {` | `DartStringState [class]` | `c94c5b27-366d-50be-b9e8-f8f2e7af1dc8` | 247-252 [crates/gcode/src/index/parser/calls/dart_textual.rs:247-252] | Indexed class `DartStringState` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:247-252] |
| `DartLineScan` | class | `struct DartLineScan {` | `DartLineScan [class]` | `826e8df3-be70-5ac4-ada1-55a31359f6ff` | 255-259 [crates/gcode/src/index/parser/calls/dart_textual.rs:255-259] | Indexed class `DartLineScan` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:255-259] |
| `DartLineScan::new` | method | `fn new(line: &str, mut state: DartScanState) -> Self {` | `DartLineScan::new [method]` | `f3fb79da-43d4-545c-b031-131b84dca8a2` | 262-362 [crates/gcode/src/index/parser/calls/dart_textual.rs:262-362] | Indexed method `DartLineScan::new` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:262-362] |
| `DartLineScan::state_at` | method | `fn state_at(&self, byte: usize) -> &DartScanState {` | `DartLineScan::state_at [method]` | `ddf1d64c-873e-530c-8e50-7993d3724101` | 364-366 [crates/gcode/src/index/parser/calls/dart_textual.rs:364-366] | Indexed method `DartLineScan::state_at` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:364-366] |
| `DartLineScan::in_line_comment` | method | `fn in_line_comment(&self, byte: usize) -> bool {` | `DartLineScan::in_line_comment [method]` | `8a1a9ca2-9049-55c1-b8f6-bc61d1c51cab` | 368-370 [crates/gcode/src/index/parser/calls/dart_textual.rs:368-370] | Indexed method `DartLineScan::in_line_comment` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:368-370] |
| `record_scan_state` | function | `fn record_scan_state(states: &mut Vec<DartScanState>, count: usize, state: &DartScanState) {` | `record_scan_state [function]` | `c3e16433-934e-5dfc-a56a-f42893a6a5b1` | 373-375 [crates/gcode/src/index/parser/calls/dart_textual.rs:373-375] | Indexed function `record_scan_state` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:373-375] |
| `dart_textual_candidate_in_ignored_context` | function | `fn dart_textual_candidate_in_ignored_context(scan: &DartLineScan, candidate_byte: usize) -> bool {` | `dart_textual_candidate_in_ignored_context [function]` | `dcc92820-a198-56bc-bbad-0abad5c21c36` | 377-379 [crates/gcode/src/index/parser/calls/dart_textual.rs:377-379] | Indexed function `dart_textual_candidate_in_ignored_context` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:377-379] |
| `dart_line_starts_type_declaration` | function | `fn dart_line_starts_type_declaration(line: &str) -> bool {` | `dart_line_starts_type_declaration [function]` | `3efdcaae-3db8-5670-b839-7d379eb7a396` | 381-391 [crates/gcode/src/index/parser/calls/dart_textual.rs:381-391] | Indexed function `dart_line_starts_type_declaration` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:381-391] |
| `empty_prefix_semicolon_declaration_in_class` | function | `fn empty_prefix_semicolon_declaration_in_class(` | `empty_prefix_semicolon_declaration_in_class [function]` | `c99e04de-c6b8-5a5a-90af-0d60d1bc23f3` | 393-417 [crates/gcode/src/index/parser/calls/dart_textual.rs:393-417] | Indexed function `empty_prefix_semicolon_declaration_in_class` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:393-417] |
| `dart_string_start` | function | `fn dart_string_start(bytes: &[u8], idx: usize) -> Option<(DartStringState, usize)> {` | `dart_string_start [function]` | `0467e7e4-5fdd-570e-9d33-c53d9783c68f` | 419-441 [crates/gcode/src/index/parser/calls/dart_textual.rs:419-441] | Indexed function `dart_string_start` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:419-441] |
| `looks_like_textual_function_declaration` | function | `fn looks_like_textual_function_declaration(` | `looks_like_textual_function_declaration [function]` | `9ed7304a-528a-586b-adb5-856d6b59e102` | 443-492 [crates/gcode/src/index/parser/calls/dart_textual.rs:443-492] | Indexed function `looks_like_textual_function_declaration` in `crates/gcode/src/index/parser/calls/dart_textual.rs`. [crates/gcode/src/index/parser/calls/dart_textual.rs:443-492] |
