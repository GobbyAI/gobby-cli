---
title: crates/gsqz/src/primitives/replace.rs
type: code_file
provenance:
- file: crates/gsqz/src/primitives/replace.rs
  ranges:
  - 7-30
  - 36-41
  - 44-48
  - 51-55
  - 58-63
  - 66-70
  - 73-77
  - 80-84
  - 87-90
  - 93-97
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gsqz/src/primitives/replace.rs

Module: [[code/modules/crates/gsqz/src/primitives|crates/gsqz/src/primitives]]

## Purpose

Provides sequential regex-based string replacement over a vector of lines. It compiles each `ReplaceRule` pattern up front, skips invalid regexes, then applies the surviving rules in order to every line so each rule can build on the previous rule’s output; the local `rule` helper and tests exercise basic substitution, backreferences, chained replacements, unchanged input cases, empty inputs, and multiple matches per line.
[crates/gsqz/src/primitives/replace.rs:7-30]
[crates/gsqz/src/primitives/replace.rs:36-41]
[crates/gsqz/src/primitives/replace.rs:44-48]
[crates/gsqz/src/primitives/replace.rs:51-55]
[crates/gsqz/src/primitives/replace.rs:58-63]

## API Symbols

- `replace` (function) component `replace [function]` (`0fd9af53-3342-5461-8496-8c5e90555988`) lines 7-30 [crates/gsqz/src/primitives/replace.rs:7-30]
  - Signature: `pub fn replace(lines: Vec<String>, rules: &[ReplaceRule]) -> Vec<String> {`
  - Purpose: This function sequentially applies multiple compiled regex pattern replacements from a rules slice to each string in a vector, discarding invalid regex patterns during compilation. [crates/gsqz/src/primitives/replace.rs:7-30]
- `rule` (function) component `rule [function]` (`51e5d958-0fc2-5f5a-99f8-d2dafac5d86a`) lines 36-41 [crates/gsqz/src/primitives/replace.rs:36-41]
  - Signature: `fn rule(pattern: &str, replacement: &str) -> ReplaceRule {`
  - Purpose: Constructs and returns a `ReplaceRule` struct by converting the provided pattern and replacement string slices into owned `String` values. [crates/gsqz/src/primitives/replace.rs:36-41]
- `test_basic_replacement` (function) component `test_basic_replacement [function]` (`3473bef7-fa16-5abe-a674-cf0d526f8f73`) lines 44-48 [crates/gsqz/src/primitives/replace.rs:44-48]
  - Signature: `fn test_basic_replacement() {`
  - Purpose: Tests that the `replace` function correctly applies a single substitution rule ("hello" → "hi") across multiple newline-terminated input lines. [crates/gsqz/src/primitives/replace.rs:44-48]
- `test_backreferences` (function) component `test_backreferences [function]` (`575d100b-e49e-5408-8760-af33dd8daf9c`) lines 51-55 [crates/gsqz/src/primitives/replace.rs:51-55]
  - Signature: `fn test_backreferences() {`
  - Purpose: Tests that the `replace` function correctly interprets regex backreferences by swapping the order of two captured word groups in colon-delimited pairs. [crates/gsqz/src/primitives/replace.rs:51-55]
- `test_chained_rules` (function) component `test_chained_rules [function]` (`d77cf346-4371-5c0d-aa94-30607d7f03f7`) lines 58-63 [crates/gsqz/src/primitives/replace.rs:58-63]
  - Signature: `fn test_chained_rules() {`
  - Purpose: This test verifies that multiple regex-based replacement rules are applied sequentially to transform an input string, replacing version patterns and literal strings in a single pass. [crates/gsqz/src/primitives/replace.rs:58-63]
- `test_invalid_regex_skipped` (function) component `test_invalid_regex_skipped [function]` (`d1b449c5-6dde-52b1-a309-72f407a5d747`) lines 66-70 [crates/gsqz/src/primitives/replace.rs:66-70]
  - Signature: `fn test_invalid_regex_skipped() {`
  - Purpose: Asserts that the `replace` function skips invalid regex patterns and returns input lines unchanged. [crates/gsqz/src/primitives/replace.rs:66-70]
- `test_empty_rules` (function) component `test_empty_rules [function]` (`67cf9a86-71d0-5ff3-bff5-8db96daac94a`) lines 73-77 [crates/gsqz/src/primitives/replace.rs:73-77]
  - Signature: `fn test_empty_rules() {`
  - Purpose: Tests that the `replace` function returns input lines unchanged when invoked with an empty rules array. [crates/gsqz/src/primitives/replace.rs:73-77]
- `test_no_match_unchanged` (function) component `test_no_match_unchanged [function]` (`c9e220eb-1b65-54f4-9ba6-7966d620f19c`) lines 80-84 [crates/gsqz/src/primitives/replace.rs:80-84]
  - Signature: `fn test_no_match_unchanged() {`
  - Purpose: Tests that the `replace` function returns input lines unchanged when the provided rule pattern does not match any content. [crates/gsqz/src/primitives/replace.rs:80-84]
- `test_empty_lines` (function) component `test_empty_lines [function]` (`10e633e0-a676-5e67-9492-70f800426bca`) lines 87-90 [crates/gsqz/src/primitives/replace.rs:87-90]
  - Signature: `fn test_empty_lines() {`
  - Purpose: Asserts that the `replace` function returns an empty collection when passed an empty input vector, regardless of the substitution rules provided. [crates/gsqz/src/primitives/replace.rs:87-90]
- `test_multiple_matches_per_line` (function) component `test_multiple_matches_per_line [function]` (`09f3939e-f6f8-5881-841b-e008c8f8a527`) lines 93-97 [crates/gsqz/src/primitives/replace.rs:93-97]
  - Signature: `fn test_multiple_matches_per_line() {`
  - Purpose: Tests that the `replace` function correctly applies pattern substitution to all occurrences of a substring within a single input line. [crates/gsqz/src/primitives/replace.rs:93-97]

