---
title: crates/gcode/src/commands/grep/grep_matcher.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/grep/grep_matcher.rs
  ranges:
  - 6-9
  - 11-44
  - 46-65
  - 67-75
  - 78-80
  - 86-92
  - 95-105
  - 108-116
  - 119-126
  - 129-136
  - 139-146
  - 149-156
  - 159-163
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/grep/grep_matcher.rs

Module: [[code/modules/crates/gcode/src/commands/grep|crates/gcode/src/commands/grep]]

## Purpose

This file implements GrepMatcher, a regex-based pattern matching utility for grep operations. The GrepMatcher struct wraps a compiled regex and optional word-boundary enforcement, constructed via the new() method which validates non-empty patterns, optionally escapes them for literal matching, and builds case-insensitive regex when requested. The find_spans() method locates all non-zero-width matches in a line and optionally filters them through word-boundary validation. Word-boundary checking relies on helper functions that extract identifier tokens from match spans and validate no ASCII alphanumeric characters or underscores are adjacent to the match, effectively treating only ASCII identifiers as word constituents while treating Unicode and other characters as word separators. The matched_texts() utility function extracts matched substrings from results. Comprehensive unit tests verify correct matching behavior across literal strings, case sensitivity, word boundaries with various adjacent character types (delimiters, operators, Unicode), and proper error reporting for invalid regex patterns and empty input.
[crates/gcode/src/commands/grep/grep_matcher.rs:6-9]
[crates/gcode/src/commands/grep/grep_matcher.rs:11-44]
[crates/gcode/src/commands/grep/grep_matcher.rs:12-31]
[crates/gcode/src/commands/grep/grep_matcher.rs:33-43]
[crates/gcode/src/commands/grep/grep_matcher.rs:46-65]

## API Symbols

- `GrepMatcher` (class) component `GrepMatcher [class]` (`628d07b3-d008-5bd5-b330-fd328ea2e211`) lines 6-9 [crates/gcode/src/commands/grep/grep_matcher.rs:6-9]
  - Signature: `pub(super) struct GrepMatcher {`
  - Purpose: `GrepMatcher` is a module-private struct that encapsulates a compiled regular expression and a boolean flag to optionally constrain matching to whole words. [crates/gcode/src/commands/grep/grep_matcher.rs:6-9]
- `GrepMatcher` (class) component `GrepMatcher [class]` (`e4a0bd8c-b79b-55fb-8ef1-7ad41194a5f1`) lines 11-44 [crates/gcode/src/commands/grep/grep_matcher.rs:11-44]
  - Signature: `impl GrepMatcher {`
  - Purpose: GrepMatcher constructs configurable regex patterns from string specifications with optional literal-string, case-insensitive, and word-boundary modes, then identifies match position spans within text lines. [crates/gcode/src/commands/grep/grep_matcher.rs:11-44]
- `GrepMatcher.new` (method) component `GrepMatcher.new [method]` (`d1bd0c60-2fe5-5595-9339-d69f73a7452f`) lines 12-31 [crates/gcode/src/commands/grep/grep_matcher.rs:12-31]
  - Signature: `pub(super) fn new(`
  - Purpose: Constructs a regex-based pattern matcher by conditionally escaping the input pattern string and compiling it with optional case-insensitive matching, storing the compiled regex and word-matching flag. [crates/gcode/src/commands/grep/grep_matcher.rs:12-31]
- `GrepMatcher.find_spans` (method) component `GrepMatcher.find_spans [method]` (`6a2a20ca-13b7-57a9-84f5-bed7f3582e09`) lines 33-43 [crates/gcode/src/commands/grep/grep_matcher.rs:33-43]
  - Signature: `pub(super) fn find_spans(&self, line: &str) -> Vec<GrepSpan> {`
  - Purpose: Identifies all non-zero-width regex matches in a line and returns their byte-position spans, optionally filtered to word boundaries. [crates/gcode/src/commands/grep/grep_matcher.rs:33-43]
- `has_identifier_boundaries` (function) component `has_identifier_boundaries [function]` (`b7c64e1e-2670-5052-831b-225b2f9a292e`) lines 46-65 [crates/gcode/src/commands/grep/grep_matcher.rs:46-65]
  - Signature: `fn has_identifier_boundaries(line: &str, span: &GrepSpan) -> bool {`
  - Purpose: Extracts an identifier token from within a span and validates that its boundaries are not adjacent to other identifier characters. [crates/gcode/src/commands/grep/grep_matcher.rs:46-65]
- `has_adjacent_identifier_boundaries` (function) component `has_adjacent_identifier_boundaries [function]` (`66514ac7-12ff-5a73-a43b-5a9b52f7fac1`) lines 67-75 [crates/gcode/src/commands/grep/grep_matcher.rs:67-75]
  - Signature: `fn has_adjacent_identifier_boundaries(line: &str, start: usize, end: usize) -> bool {`
  - Purpose: Returns true if the substring at the specified range is not preceded or followed by an identifier character, verifying it has proper word boundaries. [crates/gcode/src/commands/grep/grep_matcher.rs:67-75]
- `is_identifier_char` (function) component `is_identifier_char [function]` (`d8abe9ae-62da-5d0d-9ea7-406ef25efc79`) lines 78-80 [crates/gcode/src/commands/grep/grep_matcher.rs:78-80]
  - Signature: `fn is_identifier_char(ch: char) -> bool {`
  - Purpose: Returns `true` if the character is ASCII alphanumeric (0-9, a-z, A-Z) or an underscore, otherwise `false`. [crates/gcode/src/commands/grep/grep_matcher.rs:78-80]
- `matched_texts` (function) component `matched_texts [function]` (`ec6e1cd7-3f22-5b82-88eb-84fcfdcf457b`) lines 86-92 [crates/gcode/src/commands/grep/grep_matcher.rs:86-92]
  - Signature: `fn matched_texts<'a>(matcher: &GrepMatcher, line: &'a str) -> Vec<&'a str> {`
  - Purpose: Extracts all matched text substrings from a line by finding match spans with the provided GrepMatcher and returning them as a vector of string slices. [crates/gcode/src/commands/grep/grep_matcher.rs:86-92]
- `word_matching_accepts_identifier_boundaries` (function) component `word_matching_accepts_identifier_boundaries [function]` (`a55a9acd-0567-5e5a-98f2-a22b2aa210c2`) lines 95-105 [crates/gcode/src/commands/grep/grep_matcher.rs:95-105]
  - Signature: `fn word_matching_accepts_identifier_boundaries() {`
  - Purpose: Unit test verifying that GrepMatcher with identifier boundary mode correctly matches all occurrences of the identifier `note_path` across various syntactic contexts (standalone, after delimiters, with operators, and in method calls). [crates/gcode/src/commands/grep/grep_matcher.rs:95-105]
- `word_matching_rejects_attached_identifier_chars` (function) component `word_matching_rejects_attached_identifier_chars [function]` (`b050eb19-6a18-5775-b254-bc8e4d0e696e`) lines 108-116 [crates/gcode/src/commands/grep/grep_matcher.rs:108-116]
  - Signature: `fn word_matching_rejects_attached_identifier_chars() {`
  - Purpose: This test verifies that word-boundary matching rejects pattern matches when the target term is directly adjacent to identifier characters (alphanumeric or underscore). [crates/gcode/src/commands/grep/grep_matcher.rs:108-116]
- `word_matching_treats_unicode_as_non_identifier_chars` (function) component `word_matching_treats_unicode_as_non_identifier_chars [function]` (`d9092c4b-2a69-5609-b202-ef7e6aa45ad6`) lines 119-126 [crates/gcode/src/commands/grep/grep_matcher.rs:119-126]
  - Signature: `fn word_matching_treats_unicode_as_non_identifier_chars() {`
  - Purpose: Verifies that a GrepMatcher with word-boundary matching treats Unicode characters as non-identifier word separators, correctly matching only whole-word instances of "bar" while excluding matches adjacent to underscores. [crates/gcode/src/commands/grep/grep_matcher.rs:119-126]
- `word_matching_accepts_non_identifier_literals_with_clean_adjacent_boundaries` (function) component `word_matching_accepts_non_identifier_literals_with_clean_adjacent_boundaries [function]` (`61b156f4-c2f7-5e1b-9c94-db8161d42e77`) lines 129-136 [crates/gcode/src/commands/grep/grep_matcher.rs:129-136]
  - Signature: `fn word_matching_accepts_non_identifier_literals_with_clean_adjacent_boundaries() {`
  - Purpose: This test verifies that a `GrepMatcher` configured for word matching correctly identifies only `"::"` operators surrounded by whitespace on both sides, rejecting those directly adjacent to identifier characters. [crates/gcode/src/commands/grep/grep_matcher.rs:129-136]
- `regex_word_boundaries_still_work_without_word_flag` (function) component `regex_word_boundaries_still_work_without_word_flag [function]` (`5137b80c-cf7d-5427-8c2f-097cb213767b`) lines 139-146 [crates/gcode/src/commands/grep/grep_matcher.rs:139-146]
  - Signature: `fn regex_word_boundaries_still_work_without_word_flag() {`
  - Purpose: Verifies that regex word boundary anchors (`\b`) correctly isolate whole-word matches without requiring a dedicated word-matching flag. [crates/gcode/src/commands/grep/grep_matcher.rs:139-146]
- `invalid_regex_reports_gcode_grep_pattern_error` (function) component `invalid_regex_reports_gcode_grep_pattern_error [function]` (`02637ee7-bb0a-5844-a952-69604eb7e63b`) lines 149-156 [crates/gcode/src/commands/grep/grep_matcher.rs:149-156]
  - Signature: `fn invalid_regex_reports_gcode_grep_pattern_error() {`
  - Purpose: This test verifies that `GrepMatcher::new()` reports an error containing the message "invalid gcode grep pattern" when instantiated with invalid regex syntax (an unclosed parenthesis). [crates/gcode/src/commands/grep/grep_matcher.rs:149-156]
- `empty_pattern_reports_plain_pattern_error` (function) component `empty_pattern_reports_plain_pattern_error [function]` (`0d0f04a2-4906-5fe9-b7ab-04b7650a05b7`) lines 159-163 [crates/gcode/src/commands/grep/grep_matcher.rs:159-163]
  - Signature: `fn empty_pattern_reports_plain_pattern_error() {`
  - Purpose: Verifies that `GrepMatcher::new()` rejects an empty pattern string and returns an error with the message "pattern cannot be empty". [crates/gcode/src/commands/grep/grep_matcher.rs:159-163]

