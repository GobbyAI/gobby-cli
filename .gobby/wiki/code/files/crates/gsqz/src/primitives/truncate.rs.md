---
title: crates/gsqz/src/primitives/truncate.rs
type: code_file
provenance:
- file: crates/gsqz/src/primitives/truncate.rs
  ranges:
  - 5-27
  - 29-67
  - 74-78
  - 81-88
  - 91-106
  - 109-112
  - 115-120
  - 123-128
  - 131-136
  - 139-145
  - 148-157
  - 160-165
  - 168-178
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gsqz/src/primitives/truncate.rs

Module: [[code/modules/crates/gsqz/src/primitives|crates/gsqz/src/primitives]]

## Purpose

This file provides line-truncation utilities for `Vec<String>` output. `truncate` keeps a configurable head and tail, inserts an omission marker when content is shortened, and can switch to regex-based section truncation when `per_file_lines` and `file_marker` are set. `truncate_per_section` groups lines by section markers, truncates oversized sections independently, and preserves smaller sections unchanged; the test module exercises empty, boundary, head/tail-only, and per-section cases, plus invalid-regex fallback.
[crates/gsqz/src/primitives/truncate.rs:5-27]
[crates/gsqz/src/primitives/truncate.rs:29-67]
[crates/gsqz/src/primitives/truncate.rs:74-78]
[crates/gsqz/src/primitives/truncate.rs:81-88]
[crates/gsqz/src/primitives/truncate.rs:91-106]

## API Symbols

- `truncate` (function) component `truncate [function]` (`8cd6bb3a-58d1-5cfa-a910-f01f982a5f2a`) lines 5-27 [crates/gsqz/src/primitives/truncate.rs:5-27]
  - Signature: `pub fn truncate(`
  - Purpose: Reduces a lines vector to the first `head` and last `tail` lines with an omission count message inserted in between, or delegates to per-section truncation if `per_file_lines` and `file_marker` are specified. [crates/gsqz/src/primitives/truncate.rs:5-27]
- `truncate_per_section` (function) component `truncate_per_section [function]` (`1315000b-404f-5f00-8460-61e0b8875e86`) lines 29-67 [crates/gsqz/src/primitives/truncate.rs:29-67]
  - Signature: `fn truncate_per_section(lines: Vec<String>, max_lines: usize, marker_pattern: &str) -> Vec<String> {`
  - Purpose: Splits input lines into regex-delimited sections and truncates each section exceeding `max_lines` by preserving the top and bottom halves separated by an omission marker indicating the number of elided lines. [crates/gsqz/src/primitives/truncate.rs:29-67]
- `test_truncate_short_input` (function) component `test_truncate_short_input [function]` (`796ed8c2-2054-5086-ae8d-ee821eabf56c`) lines 74-78 [crates/gsqz/src/primitives/truncate.rs:74-78]
  - Signature: `fn test_truncate_short_input() {`
  - Purpose: This test verifies that the `truncate` function returns input lines unmodified when the input size is below the truncation threshold. [crates/gsqz/src/primitives/truncate.rs:74-78]
- `test_truncate_long_input` (function) component `test_truncate_long_input [function]` (`d244924b-b83d-5e0a-a6c0-2422fa54a112`) lines 81-88 [crates/gsqz/src/primitives/truncate.rs:81-88]
  - Signature: `fn test_truncate_long_input() {`
  - Purpose: Verifies that `truncate()` correctly retains the first 3 and last 2 lines from a 100-line input while inserting an omission marker indicating 95 lines were elided. [crates/gsqz/src/primitives/truncate.rs:81-88]
- `test_truncate_per_section` (function) component `test_truncate_per_section [function]` (`e68399f7-c7c1-5d2a-bc3d-05cc7b66a711`) lines 91-106 [crates/gsqz/src/primitives/truncate.rs:91-106]
  - Signature: `fn test_truncate_per_section() {`
  - Purpose: This test verifies that the `truncate` function correctly applies per-section line limits (3 lines maximum per section identified by the regex pattern `^@@\s`) and inserts an omission notice when truncating each section. [crates/gsqz/src/primitives/truncate.rs:91-106]
- `test_truncate_empty_input` (function) component `test_truncate_empty_input [function]` (`bed69c79-a5dd-5dde-a7bf-f7c7707421a6`) lines 109-112 [crates/gsqz/src/primitives/truncate.rs:109-112]
  - Signature: `fn test_truncate_empty_input() {`
  - Purpose: This test verifies that the `truncate` function returns an empty result when invoked with an empty input vector. [crates/gsqz/src/primitives/truncate.rs:109-112]
- `test_truncate_exact_boundary` (function) component `test_truncate_exact_boundary [function]` (`8c5ec8cc-2fa4-5296-a13b-436ef85984fb`) lines 115-120 [crates/gsqz/src/primitives/truncate.rs:115-120]
  - Signature: `fn test_truncate_exact_boundary() {`
  - Purpose: Tests that `truncate()` returns the complete input unmodified when head and tail line counts exactly sum to the total input size, representing the no-truncation boundary condition. [crates/gsqz/src/primitives/truncate.rs:115-120]
- `test_truncate_one_over_boundary` (function) component `test_truncate_one_over_boundary [function]` (`8f73d270-004b-548f-8b08-235210e8cb43`) lines 123-128 [crates/gsqz/src/primitives/truncate.rs:123-128]
  - Signature: `fn test_truncate_one_over_boundary() {`
  - Purpose: This test verifies that `truncate()` correctly inserts an omission marker element at the boundary when compressing an 11-line input to 5 head + 5 tail lines, producing a result with the marker containing "1 lines omitted" at index 5. [crates/gsqz/src/primitives/truncate.rs:123-128]
- `test_truncate_head_only` (function) component `test_truncate_head_only [function]` (`de708a17-35ca-5492-8cf4-42997a867b95`) lines 131-136 [crates/gsqz/src/primitives/truncate.rs:131-136]
  - Signature: `fn test_truncate_head_only() {`
  - Purpose: Tests that `truncate()` with `head=10` and `tail=0` returns the first 10 lines of input followed by a marker line indicating the number of omitted lines. [crates/gsqz/src/primitives/truncate.rs:131-136]
- `test_truncate_tail_only` (function) component `test_truncate_tail_only [function]` (`83863aa8-3901-59e1-85e5-0e40b2ca1ad7`) lines 139-145 [crates/gsqz/src/primitives/truncate.rs:139-145]
  - Signature: `fn test_truncate_tail_only() {`
  - Purpose: This test verifies that `truncate` with head=0 and tail=5 correctly keeps only the final 5 lines of a 20-line input while prepending an omission marker indicating 15 lines were removed. [crates/gsqz/src/primitives/truncate.rs:139-145]
- `test_truncate_per_section_small_sections_unchanged` (function) component `test_truncate_per_section_small_sections_unchanged [function]` (`f3070cc9-71c0-55d1-98ee-dbdf6a0165a5`) lines 148-157 [crates/gsqz/src/primitives/truncate.rs:148-157]
  - Signature: `fn test_truncate_per_section_small_sections_unchanged() {`
  - Purpose: This test verifies that the `truncate` function leaves all input sections unmodified when each section's line count remains below the maximum per-section limit of 10 lines. [crates/gsqz/src/primitives/truncate.rs:148-157]
- `test_truncate_per_section_invalid_regex` (function) component `test_truncate_per_section_invalid_regex [function]` (`6dce9471-bf26-5d9d-861e-ac39c7cbe54c`) lines 160-165 [crates/gsqz/src/primitives/truncate.rs:160-165]
  - Signature: `fn test_truncate_per_section_invalid_regex() {`
  - Purpose: Verifies that the `truncate` function returns input lines unmodified when passed an invalid regex pattern. [crates/gsqz/src/primitives/truncate.rs:160-165]
- `test_truncate_preserves_head_tail_content` (function) component `test_truncate_preserves_head_tail_content [function]` (`a6b18a74-dae8-5307-8fed-fe6870acbd8c`) lines 168-178 [crates/gsqz/src/primitives/truncate.rs:168-178]
  - Signature: `fn test_truncate_preserves_head_tail_content() {`
  - Purpose: Tests that the `truncate` function preserves the first three and last three lines of a 100-element vector while replacing the middle content with an omission marker. [crates/gsqz/src/primitives/truncate.rs:168-178]

