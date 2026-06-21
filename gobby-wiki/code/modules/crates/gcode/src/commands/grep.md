---
title: crates/gcode/src/commands/grep
type: code_module
provenance:
- file: crates/gcode/src/commands/grep/grep_matcher.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/grep

Parent: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

## crates/gcode/src/commands/grep

This module implements the pattern-matching core for a `gcode grep` command. Its single public-facing abstraction is `GrepMatcher`, a compiled regular-expression wrapper that translates user-supplied search options into a reusable matcher and then applies it line-by-line to produce byte-offset spans. The module is declared `pub(super)`, meaning it is encapsulated within the parent `commands::grep` namespace and is not exposed as part of the crate's public surface.

`GrepMatcher::new` (grep_matcher.rs:11-32) accepts four construction parameters and builds an internal `regex::Regex` value. When `fixed_strings` is true the pattern is escaped with `regex::escape` before compilation, preventing regex metacharacters from being interpreted. `ignore_case` is forwarded directly to `regex::RegexBuilder::case_insensitive`. An empty pattern is rejected early with a plain error, and a regex compilation failure is annotated with the context string `"invalid gcode grep pattern"` via `anyhow::Context` (grep_matcher.rs:1, 26-28).

`GrepMatcher::find_spans` (grep_matcher.rs:34-44) drives the actual search. It calls `regex::Regex::find_iter` on a line of text, discards zero-length matches, converts each match into a `GrepSpan` (imported from the parent module via `super::GrepSpan`), and optionally filters through word-boundary logic when `self.word` is true. Word-boundary enforcement is intentionally ASCII-only: `is_identifier_char` (grep_matcher.rs:78-80) recognises only `[A-Za-z0-9_]`, so Unicode letters adjacent to a match do not block it. The two helpers `has_identifier_boundaries` and `has_adjacent_identifier_boundaries` implement this by locating the first identifier-char run inside the matched span and verifying that neither the byte immediately before nor the byte immediately after the run is itself an identifier character (grep_matcher.rs:46-74). The test suite (components `word_matching_accepts_identifier_boundaries` through `empty_pattern_reports_plain_pattern_error`) exercises all branches of this logic, including edge cases for Unicode, non-identifier literals, and embedded `\b` regex anchors.

### Public API

| Symbol | Kind | Visibility | Notes |
|---|---|---|---|
| `GrepMatcher` | struct | `pub(super)` | Holds compiled `regex::Regex` and `word` flag |
| `GrepMatcher::new` | method | `pub(super)` | Compiles pattern; see construction flags below |
| `GrepMatcher::find_spans` | method | `pub(super)` | Returns `Vec<GrepSpan>` of byte-offset matches for a single line |
| `has_identifier_boundaries` | fn | private | Locates first identifier run in span, delegates to adjacent check |
| `has_adjacent_identifier_boundaries` | fn | private | Checks chars immediately before/after a byte range |
| `is_identifier_char` | fn | private | `[A-Za-z0-9_]` — ASCII only, by design |

### `GrepMatcher::new` construction flags

| Parameter | Type | Effect |
|---|---|---|
| `pattern` | `&str` | Search expression; empty value is rejected (grep_matcher.rs:17-19) |
| `fixed_strings` | `bool` | When true, escapes pattern as a literal string (grep_matcher.rs:20-23) |
| `ignore_case` | `bool` | Passed to `RegexBuilder::case_insensitive` (grep_matcher.rs:25-26) |
| `word` | `bool` | Enables ASCII word-boundary filtering in `find_spans` (grep_matcher.rs:40-41) |

### Cross-module collaboration

The module imports `GrepSpan` from its parent via `use super::GrepSpan` (grep_matcher.rs:3), indicating the parent `commands::grep` module owns the span type and this module is responsible only for producing instances of it. External dependencies are limited to `anyhow` (error context, grep_matcher.rs:1) and `regex` (grep_matcher.rs:24-27); no other crate-internal modules are called.
[crates/gcode/src/commands/grep/grep_matcher.rs:6-9]
[crates/gcode/src/commands/grep/grep_matcher.rs:12-31]
[crates/gcode/src/commands/grep/grep_matcher.rs:33-43]
[crates/gcode/src/commands/grep/grep_matcher.rs:46-65]
[crates/gcode/src/commands/grep/grep_matcher.rs:67-75]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/grep/grep_matcher.rs\|crates/gcode/src/commands/grep/grep_matcher.rs]] | `crates/gcode/src/commands/grep/grep_matcher.rs` exposes 14 indexed API symbols. |

