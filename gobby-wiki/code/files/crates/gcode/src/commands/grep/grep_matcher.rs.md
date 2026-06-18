---
title: crates/gcode/src/commands/grep/grep_matcher.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/grep/grep_matcher.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/grep/grep_matcher.rs

Module: [[code/modules/crates/gcode/src/commands/grep|crates/gcode/src/commands/grep]]

## Overview

This file defines the pattern-matching logic used during grep search operations. It contains the GrepMatcher struct, which compiles search patterns and scans input text to locate matching spans crates/gcode/src/commands/grep/grep_matcher.rs:6-9. The matcher supports standard regular expressions, fixed-string escaping, case-insensitive options, and specialized word-boundary matching rules crates/gcode/src/commands/grep/grep_matcher.rs:12-31.

Through its word-boundary implementation, the matcher provides precise matching capabilities designed for source code analysis. When word-boundary matching is enabled, it ensures that matches are not part of larger, attached alphanumeric identifiers, avoiding false positives during token searches crates/gcode/src/commands/grep/grep_matcher.rs:33-43.

## How it fits
[crates/gcode/src/commands/grep/grep_matcher.rs:6-9]
[crates/gcode/src/commands/grep/grep_matcher.rs:12-31]
[crates/gcode/src/commands/grep/grep_matcher.rs:33-43]
[crates/gcode/src/commands/grep/grep_matcher.rs:46-65]
[crates/gcode/src/commands/grep/grep_matcher.rs:67-75]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GrepMatcher` | class | 'GrepMatcher' is an internal struct that wraps a compiled 'regex::Regex' and a 'word' flag to control whether matches are constrained to whole-word boundaries. [crates/gcode/src/commands/grep/grep_matcher.rs:6-9] |
| `GrepMatcher::new` | method | Constructs a 'Self' by rejecting empty patterns, optionally escaping the input for fixed-string matching, building a 'regex::Regex' with optional case-insensitive mode and contextualized error handling, and storing the compiled regex along with the 'word' flag. [crates/gcode/src/commands/grep/grep_matcher.rs:12-31] |
| `GrepMatcher::find_spans` | method | Returns all non-empty regex match spans in a line as 'GrepSpan { start, end }', optionally filtering them to only those with identifier word boundaries when 'self.word' is set. [crates/gcode/src/commands/grep/grep_matcher.rs:33-43] |
| `has_identifier_boundaries` | function | Returns 'true' if the first contiguous identifier-like token within 'span' in 'line' is bounded by adjacent identifier boundaries at its start and end, and falls back to checking the original span boundaries when no identifier character is present. [crates/gcode/src/commands/grep/grep_matcher.rs:46-65] |
| `has_adjacent_identifier_boundaries` | function | Returns 'true' only when the substring 'line[start..end]' is not immediately preceded or followed by an identifier character, i.e. both adjacent boundary characters are absent or non-identifier chars. [crates/gcode/src/commands/grep/grep_matcher.rs:67-75] |
| `is_identifier_char` | function | Returns 'true' if 'ch' is an ASCII letter, digit, or underscore, and 'false' otherwise. [crates/gcode/src/commands/grep/grep_matcher.rs:78-80] |
| `matched_texts` | function | Returns a vector of string slices from 'line' corresponding to each span produced by 'matcher.find_spans(line)', preserving the input lifetime by slicing 'line' at each span’s start and end indices. [crates/gcode/src/commands/grep/grep_matcher.rs:86-92] |
| `word_matching_accepts_identifier_boundaries` | function | Verifies that a 'GrepMatcher' configured for word matching treats identifier characters as valid boundaries, matching 'note_path' in plain, colon-delimited, borrowed, and member-access contexts and returning four matches. [crates/gcode/src/commands/grep/grep_matcher.rs:95-105] |
| `word_matching_rejects_attached_identifier_chars` | function | Verifies that a 'GrepMatcher' for 'note_path' does not match occurrences where the term is attached to surrounding identifier characters, returning no spans for 'selected_note_paths note_paths xnote_path'. [crates/gcode/src/commands/grep/grep_matcher.rs:108-116] |
| `word_matching_treats_unicode_as_non_identifier_chars` | function | Verifies that 'GrepMatcher' word matching treats Unicode letters as non-identifier characters, so '"bar"' is matched at boundaries against strings like 'føøbar', 'barβ', and 'β bar' but not inside ASCII identifier forms like '_bar' or 'bar_'. [crates/gcode/src/commands/grep/grep_matcher.rs:119-126] |
| `word_matching_accepts_non_identifier_literals_with_clean_adjacent_boundaries` | function | Verifies that a 'GrepMatcher' configured for word matching recognizes the non-identifier literal '::' only when it appears at clean token boundaries, yielding two matches in the sample text. [crates/gcode/src/commands/grep/grep_matcher.rs:129-136] |
| `regex_word_boundaries_still_work_without_word_flag` | function | Verifies that 'GrepMatcher' correctly matches '\bnote_path\b' as a whole-word regex even when the word flag is disabled, by asserting it extracts only 'note_path' from 'selected_note_paths note_path.parent()'. [crates/gcode/src/commands/grep/grep_matcher.rs:139-146] |
| `invalid_regex_reports_gcode_grep_pattern_error` | function | Verifies that constructing a 'GrepMatcher' with an invalid regex pattern ('"("') returns an error whose formatted message contains 'invalid gcode grep pattern'. [crates/gcode/src/commands/grep/grep_matcher.rs:149-156] |
| `empty_pattern_reports_plain_pattern_error` | function | Verifies that constructing a 'GrepMatcher' with an empty pattern returns an error whose string representation is exactly '"pattern cannot be empty"'. [crates/gcode/src/commands/grep/grep_matcher.rs:159-163] |

