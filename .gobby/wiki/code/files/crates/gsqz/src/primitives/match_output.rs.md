---
title: crates/gsqz/src/primitives/match_output.rs
type: code_file
provenance:
- file: crates/gsqz/src/primitives/match_output.rs
  ranges:
  - 8-33
  - 39-45
  - 47-49
  - 52-56
  - 59-63
  - 66-70
  - 73-77
  - 80-87
  - 90-94
  - 97-101
  - 104-107
  - 110-115
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gsqz/src/primitives/match_output.rs

Module: [[code/modules/crates/gsqz/src/primitives|crates/gsqz/src/primitives]]

## Purpose

This file implements output-matching helpers for `MatchOutputRule`. `check` joins all input lines into one blob, then scans rules in order, compiling each regex and returning the first rule message whose pattern matches unless an optional `unless` regex also matches; invalid regexes are skipped. The local `rule` and `lines` helpers build test fixtures, and the tests cover basic matching, `unless` blocking, no-match behavior, first-match-wins semantics, invalid regex handling, empty-rule input, and matching across the full multi-line blob.
[crates/gsqz/src/primitives/match_output.rs:8-33]
[crates/gsqz/src/primitives/match_output.rs:39-45]
[crates/gsqz/src/primitives/match_output.rs:47-49]
[crates/gsqz/src/primitives/match_output.rs:52-56]
[crates/gsqz/src/primitives/match_output.rs:59-63]

## API Symbols

- `check` (function) component `check [function]` (`32efbce0-fa3f-56fe-bc0f-f835fc242381`) lines 8-33 [crates/gsqz/src/primitives/match_output.rs:8-33]
  - Signature: `pub fn check(lines: &[String], rules: &[MatchOutputRule]) -> Option<String> {`
  - Purpose: Concatenates input strings and returns the message of the first `MatchOutputRule` whose regex pattern matches the concatenated blob unless its optional `unless` pattern also matches, otherwise returns `None`. [crates/gsqz/src/primitives/match_output.rs:8-33]
- `rule` (function) component `rule [function]` (`c91cf302-b6ed-5dd2-bf34-22206d7b28c6`) lines 39-45 [crates/gsqz/src/primitives/match_output.rs:39-45]
  - Signature: `fn rule(pattern: &str, message: &str, unless: Option<&str>) -> MatchOutputRule {`
  - Purpose: This function constructs a `MatchOutputRule` struct by converting borrowed string references into owned `String` values for the pattern, message, and optional unless condition. [crates/gsqz/src/primitives/match_output.rs:39-45]
- `lines` (function) component `lines [function]` (`def86bb9-e734-5291-a0c0-043c8d384f39`) lines 47-49 [crates/gsqz/src/primitives/match_output.rs:47-49]
  - Signature: `fn lines(s: &str) -> Vec<String> {`
  - Purpose: This function splits a string into individual lines via `.lines()` and returns a vector of strings with a newline character appended to each line. [crates/gsqz/src/primitives/match_output.rs:47-49]
- `test_basic_match_returns_message` (function) component `test_basic_match_returns_message [function]` (`7c3d538e-60b1-5dcc-aaef-3332d2e2ae35`) lines 52-56 [crates/gsqz/src/primitives/match_output.rs:52-56]
  - Signature: `fn test_basic_match_returns_message() {`
  - Purpose: This test asserts that the `check` function correctly matches a rule pattern ("test result: ok") in the input text and returns the associated message wrapped in a `Some` variant. [crates/gsqz/src/primitives/match_output.rs:52-56]
- `test_unless_blocks_match` (function) component `test_unless_blocks_match [function]` (`8eb07c08-dccf-59ee-8776-36dd63c8dacd`) lines 59-63 [crates/gsqz/src/primitives/match_output.rs:59-63]
  - Signature: `fn test_unless_blocks_match() {`
  - Purpose: This test verifies that the `check` function returns `None` when a rule's pattern matches the input but its associated 'unless' block (negative assertion) is also present in the text. [crates/gsqz/src/primitives/match_output.rs:59-63]
- `test_unless_absent_allows_match` (function) component `test_unless_absent_allows_match [function]` (`fb441f43-6133-5423-aa9b-fde3dda81952`) lines 66-70 [crates/gsqz/src/primitives/match_output.rs:66-70]
  - Signature: `fn test_unless_absent_allows_match() {`
  - Purpose: This test verifies that a rule without absence constraints successfully matches input text containing its keyword and returns the configured message. [crates/gsqz/src/primitives/match_output.rs:66-70]
- `test_no_match_returns_none` (function) component `test_no_match_returns_none [function]` (`001e5557-abaf-5197-b5ac-897f6a6ad6bc`) lines 73-77 [crates/gsqz/src/primitives/match_output.rs:73-77]
  - Signature: `fn test_no_match_returns_none() {`
  - Purpose: This test verifies that the `check` function returns `None` when the input text contains no matches for any rule in the provided rule set. [crates/gsqz/src/primitives/match_output.rs:73-77]
- `test_first_rule_wins` (function) component `test_first_rule_wins [function]` (`28637dfe-e848-5dd1-92f9-9d8d4f738053`) lines 80-87 [crates/gsqz/src/primitives/match_output.rs:80-87]
  - Signature: `fn test_first_rule_wins() {`
  - Purpose: This test verifies that the `check` function implements first-match-wins semantics, returning the message from the first matching rule when multiple rules match the input. [crates/gsqz/src/primitives/match_output.rs:80-87]
- `test_invalid_regex_skipped` (function) component `test_invalid_regex_skipped [function]` (`f7cda631-4dec-5d05-b084-cf44fe958f6b`) lines 90-94 [crates/gsqz/src/primitives/match_output.rs:90-94]
  - Signature: `fn test_invalid_regex_skipped() {`
  - Purpose: This test verifies that rules with invalid regex patterns are skipped during evaluation, allowing subsequent valid rules to match and apply their replacements to the input. [crates/gsqz/src/primitives/match_output.rs:90-94]
- `test_invalid_unless_regex_treated_as_no_unless` (function) component `test_invalid_unless_regex_treated_as_no_unless [function]` (`fb5f4a8f-6fb2-5f7a-9a99-d2a1d67b76c9`) lines 97-101 [crates/gsqz/src/primitives/match_output.rs:97-101]
  - Signature: `fn test_invalid_unless_regex_treated_as_no_unless() {`
  - Purpose: This test verifies that an invalid regex pattern supplied as an "unless" condition is handled gracefully by treating it as an absent condition, allowing the rule to match and apply its replacement value. [crates/gsqz/src/primitives/match_output.rs:97-101]
- `test_empty_rules_returns_none` (function) component `test_empty_rules_returns_none [function]` (`fa25f392-81f2-5794-9179-aac0139089eb`) lines 104-107 [crates/gsqz/src/primitives/match_output.rs:104-107]
  - Signature: `fn test_empty_rules_returns_none() {`
  - Purpose: This test verifies that the `check` function returns `None` when invoked with output lines and an empty rules array. [crates/gsqz/src/primitives/match_output.rs:104-107]
- `test_checks_full_blob_not_per_line` (function) component `test_checks_full_blob_not_per_line [function]` (`4e69c744-2191-55fe-9fbd-9a69144fd1fd`) lines 110-115 [crates/gsqz/src/primitives/match_output.rs:110-115]
  - Signature: `fn test_checks_full_blob_not_per_line() {`
  - Purpose: This test validates that regex pattern matching with the dotall modifier (`(?s)`) correctly matches across newline boundaries when processing the complete input as a single blob rather than line-by-line. [crates/gsqz/src/primitives/match_output.rs:110-115]

