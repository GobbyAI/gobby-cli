---
title: crates/gcode/src/commands/grep/grep_matcher.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/grep/grep_matcher.rs
  ranges:
  - 6-9
  - 12-31
  - 33-43
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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/grep/grep_matcher.rs:6-9](crates/gcode/src/commands/grep/grep_matcher.rs#L6-L9), [crates/gcode/src/commands/grep/grep_matcher.rs:12-31](crates/gcode/src/commands/grep/grep_matcher.rs#L12-L31), [crates/gcode/src/commands/grep/grep_matcher.rs:33-43](crates/gcode/src/commands/grep/grep_matcher.rs#L33-L43), [crates/gcode/src/commands/grep/grep_matcher.rs:46-65](crates/gcode/src/commands/grep/grep_matcher.rs#L46-L65), [crates/gcode/src/commands/grep/grep_matcher.rs:67-75](crates/gcode/src/commands/grep/grep_matcher.rs#L67-L75), [crates/gcode/src/commands/grep/grep_matcher.rs:78-80](crates/gcode/src/commands/grep/grep_matcher.rs#L78-L80), [crates/gcode/src/commands/grep/grep_matcher.rs:86-92](crates/gcode/src/commands/grep/grep_matcher.rs#L86-L92), [crates/gcode/src/commands/grep/grep_matcher.rs:95-105](crates/gcode/src/commands/grep/grep_matcher.rs#L95-L105), [crates/gcode/src/commands/grep/grep_matcher.rs:108-116](crates/gcode/src/commands/grep/grep_matcher.rs#L108-L116), [crates/gcode/src/commands/grep/grep_matcher.rs:119-126](crates/gcode/src/commands/grep/grep_matcher.rs#L119-L126), [crates/gcode/src/commands/grep/grep_matcher.rs:129-136](crates/gcode/src/commands/grep/grep_matcher.rs#L129-L136), [crates/gcode/src/commands/grep/grep_matcher.rs:139-146](crates/gcode/src/commands/grep/grep_matcher.rs#L139-L146), [crates/gcode/src/commands/grep/grep_matcher.rs:149-156](crates/gcode/src/commands/grep/grep_matcher.rs#L149-L156), [crates/gcode/src/commands/grep/grep_matcher.rs:159-163](crates/gcode/src/commands/grep/grep_matcher.rs#L159-L163)

</details>

# crates/gcode/src/commands/grep/grep_matcher.rs

Module: [[code/modules/crates/gcode/src/commands/grep|crates/gcode/src/commands/grep]]

## Purpose

Implements `GrepMatcher`, the grep engine used by `gcode` to compile a pattern and find matching spans in a line, with support for fixed-string matching, case-insensitive matching, and optional `-w` word filtering. `new` validates and builds the regex, `find_spans` returns non-empty match ranges as `GrepSpan`s, and the helper functions enforce ASCII identifier boundary rules so word matches only accept tokens that are not attached to identifier characters, while the tests cover boundary behavior, Unicode handling, regex errors, and empty-pattern rejection.
[crates/gcode/src/commands/grep/grep_matcher.rs:6-9]
[crates/gcode/src/commands/grep/grep_matcher.rs:12-31]
[crates/gcode/src/commands/grep/grep_matcher.rs:33-43]
[crates/gcode/src/commands/grep/grep_matcher.rs:46-65]
[crates/gcode/src/commands/grep/grep_matcher.rs:67-75]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `GrepMatcher` | class | `pub(super) struct GrepMatcher {` | `GrepMatcher [class]` | `628d07b3-d008-5bd5-b330-fd328ea2e211` | 6-9 [crates/gcode/src/commands/grep/grep_matcher.rs:6-9] | Indexed class `GrepMatcher` in `crates/gcode/src/commands/grep/grep_matcher.rs`. [crates/gcode/src/commands/grep/grep_matcher.rs:6-9] |
| `GrepMatcher::new` | method | `pub(super) fn new(` | `GrepMatcher::new [method]` | `d1bd0c60-2fe5-5595-9339-d69f73a7452f` | 12-31 [crates/gcode/src/commands/grep/grep_matcher.rs:12-31] | Indexed method `GrepMatcher::new` in `crates/gcode/src/commands/grep/grep_matcher.rs`. [crates/gcode/src/commands/grep/grep_matcher.rs:12-31] |
| `GrepMatcher::find_spans` | method | `pub(super) fn find_spans(&self, line: &str) -> Vec<GrepSpan> {` | `GrepMatcher::find_spans [method]` | `6a2a20ca-13b7-57a9-84f5-bed7f3582e09` | 33-43 [crates/gcode/src/commands/grep/grep_matcher.rs:33-43] | Indexed method `GrepMatcher::find_spans` in `crates/gcode/src/commands/grep/grep_matcher.rs`. [crates/gcode/src/commands/grep/grep_matcher.rs:33-43] |
| `has_identifier_boundaries` | function | `fn has_identifier_boundaries(line: &str, span: &GrepSpan) -> bool {` | `has_identifier_boundaries [function]` | `b7c64e1e-2670-5052-831b-225b2f9a292e` | 46-65 [crates/gcode/src/commands/grep/grep_matcher.rs:46-65] | Indexed function `has_identifier_boundaries` in `crates/gcode/src/commands/grep/grep_matcher.rs`. [crates/gcode/src/commands/grep/grep_matcher.rs:46-65] |
| `has_adjacent_identifier_boundaries` | function | `fn has_adjacent_identifier_boundaries(line: &str, start: usize, end: usize) -> bool {` | `has_adjacent_identifier_boundaries [function]` | `66514ac7-12ff-5a73-a43b-5a9b52f7fac1` | 67-75 [crates/gcode/src/commands/grep/grep_matcher.rs:67-75] | Indexed function `has_adjacent_identifier_boundaries` in `crates/gcode/src/commands/grep/grep_matcher.rs`. [crates/gcode/src/commands/grep/grep_matcher.rs:67-75] |
| `is_identifier_char` | function | `fn is_identifier_char(ch: char) -> bool {` | `is_identifier_char [function]` | `d8abe9ae-62da-5d0d-9ea7-406ef25efc79` | 78-80 [crates/gcode/src/commands/grep/grep_matcher.rs:78-80] | Indexed function `is_identifier_char` in `crates/gcode/src/commands/grep/grep_matcher.rs`. [crates/gcode/src/commands/grep/grep_matcher.rs:78-80] |
| `matched_texts` | function | `fn matched_texts<'a>(matcher: &GrepMatcher, line: &'a str) -> Vec<&'a str> {` | `matched_texts [function]` | `ec6e1cd7-3f22-5b82-88eb-84fcfdcf457b` | 86-92 [crates/gcode/src/commands/grep/grep_matcher.rs:86-92] | Indexed function `matched_texts` in `crates/gcode/src/commands/grep/grep_matcher.rs`. [crates/gcode/src/commands/grep/grep_matcher.rs:86-92] |
| `word_matching_accepts_identifier_boundaries` | function | `fn word_matching_accepts_identifier_boundaries() {` | `word_matching_accepts_identifier_boundaries [function]` | `a55a9acd-0567-5e5a-98f2-a22b2aa210c2` | 95-105 [crates/gcode/src/commands/grep/grep_matcher.rs:95-105] | Indexed function `word_matching_accepts_identifier_boundaries` in `crates/gcode/src/commands/grep/grep_matcher.rs`. [crates/gcode/src/commands/grep/grep_matcher.rs:95-105] |
| `word_matching_rejects_attached_identifier_chars` | function | `fn word_matching_rejects_attached_identifier_chars() {` | `word_matching_rejects_attached_identifier_chars [function]` | `b050eb19-6a18-5775-b254-bc8e4d0e696e` | 108-116 [crates/gcode/src/commands/grep/grep_matcher.rs:108-116] | Indexed function `word_matching_rejects_attached_identifier_chars` in `crates/gcode/src/commands/grep/grep_matcher.rs`. [crates/gcode/src/commands/grep/grep_matcher.rs:108-116] |
| `word_matching_treats_unicode_as_non_identifier_chars` | function | `fn word_matching_treats_unicode_as_non_identifier_chars() {` | `word_matching_treats_unicode_as_non_identifier_chars [function]` | `d9092c4b-2a69-5609-b202-ef7e6aa45ad6` | 119-126 [crates/gcode/src/commands/grep/grep_matcher.rs:119-126] | Indexed function `word_matching_treats_unicode_as_non_identifier_chars` in `crates/gcode/src/commands/grep/grep_matcher.rs`. [crates/gcode/src/commands/grep/grep_matcher.rs:119-126] |
| `word_matching_accepts_non_identifier_literals_with_clean_adjacent_boundaries` | function | `fn word_matching_accepts_non_identifier_literals_with_clean_adjacent_boundaries() {` | `word_matching_accepts_non_identifier_literals_with_clean_adjacent_boundaries [function]` | `61b156f4-c2f7-5e1b-9c94-db8161d42e77` | 129-136 [crates/gcode/src/commands/grep/grep_matcher.rs:129-136] | Indexed function `word_matching_accepts_non_identifier_literals_with_clean_adjacent_boundaries` in `crates/gcode/src/commands/grep/grep_matcher.rs`. [crates/gcode/src/commands/grep/grep_matcher.rs:129-136] |
| `regex_word_boundaries_still_work_without_word_flag` | function | `fn regex_word_boundaries_still_work_without_word_flag() {` | `regex_word_boundaries_still_work_without_word_flag [function]` | `5137b80c-cf7d-5427-8c2f-097cb213767b` | 139-146 [crates/gcode/src/commands/grep/grep_matcher.rs:139-146] | Indexed function `regex_word_boundaries_still_work_without_word_flag` in `crates/gcode/src/commands/grep/grep_matcher.rs`. [crates/gcode/src/commands/grep/grep_matcher.rs:139-146] |
| `invalid_regex_reports_gcode_grep_pattern_error` | function | `fn invalid_regex_reports_gcode_grep_pattern_error() {` | `invalid_regex_reports_gcode_grep_pattern_error [function]` | `02637ee7-bb0a-5844-a952-69604eb7e63b` | 149-156 [crates/gcode/src/commands/grep/grep_matcher.rs:149-156] | Indexed function `invalid_regex_reports_gcode_grep_pattern_error` in `crates/gcode/src/commands/grep/grep_matcher.rs`. [crates/gcode/src/commands/grep/grep_matcher.rs:149-156] |
| `empty_pattern_reports_plain_pattern_error` | function | `fn empty_pattern_reports_plain_pattern_error() {` | `empty_pattern_reports_plain_pattern_error [function]` | `0d0f04a2-4906-5fe9-b7ab-04b7650a05b7` | 159-163 [crates/gcode/src/commands/grep/grep_matcher.rs:159-163] | Indexed function `empty_pattern_reports_plain_pattern_error` in `crates/gcode/src/commands/grep/grep_matcher.rs`. [crates/gcode/src/commands/grep/grep_matcher.rs:159-163] |
