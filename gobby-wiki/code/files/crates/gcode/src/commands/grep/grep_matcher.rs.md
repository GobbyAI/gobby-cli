---
title: crates/gcode/src/commands/grep/grep_matcher.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/grep/grep_matcher.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/grep/grep_matcher.rs

Module: [[code/modules/crates/gcode/src/commands/grep|crates/gcode/src/commands/grep]]

## Overview

`crates/gcode/src/commands/grep/grep_matcher.rs` exposes 14 indexed API symbols.

## How it fits

`crates/gcode/src/commands/grep/grep_matcher.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GrepMatcher` | class | 'GrepMatcher' is an internal struct that wraps a compiled 'regex::Regex' and a 'word' flag to control whether matches are constrained to whole-word boundaries. [crates/gcode/src/commands/grep/grep_matcher.rs:6-9] |
| `GrepMatcher::new` | method | Constructs a 'Self' by rejecting empty patterns, optionally escaping the input for fixed-string matching, building a 'regex::Regex' with optional case-insensitive mode and contextualized error handling, and storing the compiled regex along with the 'word' flag. [crates/gcode/src/commands/grep/grep_matcher.rs:12-31] |
| `GrepMatcher::find_spans` | method | Returns all non-empty regex match spans in a line as 'GrepSpan { start, end }', optionally filtering them to only those with identifier word boundaries when 'self.word' is set. [crates/gcode/src/commands/grep/grep_matcher.rs:33-43] |
| `has_identifier_boundaries` | function | Returns 'true' if the first contiguous identifier-like token within 'span' in 'line' is bounded by adjacent identifier boundaries at its start and end, and falls back to checking the original span boundaries when no identifier character is present. [crates/gcode/src/commands/grep/grep_matcher.rs:46-65] |
| `has_adjacent_identifier_boundaries` | function | Returns 'true' only when the substring 'line[start..end]' is not immediately preceded or followed by an identifier character, i.e. both adjacent boundary characters are absent or non-identifier chars. [crates/gcode/src/commands/grep/grep_matcher.rs:67-75] |
| `is_identifier_char` | function | Returns 'true' if 'ch' is an ASCII letter, digit, or underscore, and 'false' otherwise. [crates/gcode/src/commands/grep/grep_matcher.rs:78-80] |
| `matched_texts` | function | Returns a vector of string slices from 'line' corresponding to each span produced by 'matcher.find_spans(line)', preserving the input lifetime by slicing 'line' at each span’s start and end indices. [crates/gcode/src/commands/grep/grep_matcher.rs:86-92] |

_Verified by 7 in-file unit tests._

