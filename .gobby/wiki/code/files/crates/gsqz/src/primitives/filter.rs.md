---
title: crates/gsqz/src/primitives/filter.rs
type: code_file
provenance:
- file: crates/gsqz/src/primitives/filter.rs
  ranges:
  - 4-15
  - 22-32
  - 35-39
  - 42-45
  - 48-52
  - 55-59
  - 62-72
  - 75-80
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gsqz/src/primitives/filter.rs

Module: [[code/modules/crates/gsqz/src/primitives|crates/gsqz/src/primitives]]

## Purpose

Provides `filter_lines`, which compiles the supplied regex patterns, skips any invalid ones, and returns only the input lines that do not match any valid pattern. The tests cover matching and non-matching filters, empty inputs and patterns, multiple patterns, removing all lines, and the invalid-regex fallback.
[crates/gsqz/src/primitives/filter.rs:4-15]
[crates/gsqz/src/primitives/filter.rs:22-32]
[crates/gsqz/src/primitives/filter.rs:35-39]
[crates/gsqz/src/primitives/filter.rs:42-45]
[crates/gsqz/src/primitives/filter.rs:48-52]

## API Symbols

- `filter_lines` (function) component `filter_lines [function]` (`8faa2138-fa37-53b4-b21b-2dc80b2babf5`) lines 4-15 [crates/gsqz/src/primitives/filter.rs:4-15]
  - Signature: `pub fn filter_lines(lines: Vec<String>, patterns: &[String]) -> Vec<String> {`
  - Purpose: Filters a vector of strings to exclude lines matching any of the provided regex patterns. [crates/gsqz/src/primitives/filter.rs:4-15]
- `test_filter_removes_matching` (function) component `test_filter_removes_matching [function]` (`eaddf723-71da-548a-b3ef-a176c019c9b5`) lines 22-32 [crates/gsqz/src/primitives/filter.rs:22-32]
  - Signature: `fn test_filter_removes_matching() {`
  - Purpose: This test verifies that `filter_lines()` removes all input lines matching any of the provided regex patterns, retaining only non-matching lines. [crates/gsqz/src/primitives/filter.rs:22-32]
- `test_filter_empty_patterns` (function) component `test_filter_empty_patterns [function]` (`08ca6a31-4880-55be-9fb6-fb381b93f51b`) lines 35-39 [crates/gsqz/src/primitives/filter.rs:35-39]
  - Signature: `fn test_filter_empty_patterns() {`
  - Purpose: Asserts that `filter_lines` with an empty patterns slice returns the input lines unmodified. [crates/gsqz/src/primitives/filter.rs:35-39]
- `test_filter_empty_lines` (function) component `test_filter_empty_lines [function]` (`75b8179f-e92b-5abd-b753-310773d5be2f`) lines 42-45 [crates/gsqz/src/primitives/filter.rs:42-45]
  - Signature: `fn test_filter_empty_lines() {`
  - Purpose: This test verifies that `filter_lines` returns an empty result when passed an empty input vector, regardless of the filter patterns provided. [crates/gsqz/src/primitives/filter.rs:42-45]
- `test_filter_removes_all` (function) component `test_filter_removes_all [function]` (`0ca60299-497e-512f-92c6-30cf0e95505d`) lines 48-52 [crates/gsqz/src/primitives/filter.rs:48-52]
  - Signature: `fn test_filter_removes_all() {`
  - Purpose: This test verifies that `filter_lines` removes all input strings when the provided regex pattern matches every element. [crates/gsqz/src/primitives/filter.rs:48-52]
- `test_filter_removes_none` (function) component `test_filter_removes_none [function]` (`0109c774-ada4-5242-9e1c-a990394e462a`) lines 55-59 [crates/gsqz/src/primitives/filter.rs:55-59]
  - Signature: `fn test_filter_removes_none() {`
  - Purpose: This test verifies that `filter_lines` returns all input lines unchanged when the provided regex pattern `^NOPE` matches none of them. [crates/gsqz/src/primitives/filter.rs:55-59]
- `test_filter_multiple_patterns` (function) component `test_filter_multiple_patterns [function]` (`45d3032d-4ceb-5a67-8300-8b7f408f9dd1`) lines 62-72 [crates/gsqz/src/primitives/filter.rs:62-72]
  - Signature: `fn test_filter_multiple_patterns() {`
  - Purpose: Tests that `filter_lines` correctly excludes lines matching any of the supplied regex patterns. [crates/gsqz/src/primitives/filter.rs:62-72]
- `test_filter_invalid_regex_skipped` (function) component `test_filter_invalid_regex_skipped [function]` (`1e9421bd-6c46-5041-ad56-06265939d31e`) lines 75-80 [crates/gsqz/src/primitives/filter.rs:75-80]
  - Signature: `fn test_filter_invalid_regex_skipped() {`
  - Purpose: Tests that `filter_lines` gracefully handles invalid regex patterns by silently skipping them and returning all input lines unfiltered. [crates/gsqz/src/primitives/filter.rs:75-80]

