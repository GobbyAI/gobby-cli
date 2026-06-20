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

`grep_matcher.rs` implements the internal matcher behind `gcode grep`: it owns a compiled `regex::Regex` plus the `word` matching mode, validates non-empty patterns, optionally escapes fixed-string input, applies case-insensitive compilation, and wraps regex build failures as “invalid gcode grep pattern” errors (`crates/gcode/src/commands/grep/grep_matcher.rs:6-30`). It collaborates with the parent grep command module through `super::GrepSpan`, returning byte spans for matches instead of text so callers can render or process matches consistently (`crates/gcode/src/commands/grep/grep_matcher.rs:3`, `crates/gcode/src/commands/grep/grep_matcher.rs:33-42`).

The main flow is `GrepMatcher::new` followed by `find_spans`: `find_spans` iterates regex matches, drops zero-length matches, converts each match into `GrepSpan { start, end }`, and conditionally applies word-boundary filtering (`crates/gcode/src/commands/grep/grep_matcher.rs:33-42`). Word matching is token-oriented rather than regex `\b`-oriented: it finds the first ASCII identifier character inside the matched span, expands through adjacent ASCII identifier characters, and accepts the match only when the surrounding characters are not ASCII alphanumeric or underscore (`crates/gcode/src/commands/grep/grep_matcher.rs:46-79`). The source comment ties this behavior specifically to `gcode grep -w` and indexed source tokens (`crates/gcode/src/commands/grep/grep_matcher.rs:77-79`).

| Symbol | Role | Evidence |
| --- | --- | --- |
| `GrepMatcher` | Internal matcher state: compiled regex plus word mode | `crates/gcode/src/commands/grep/grep_matcher.rs:6-9` |
| `GrepMatcher::new` | Builds and validates matcher configuration | `crates/gcode/src/commands/grep/grep_matcher.rs:12-30` |
| `GrepMatcher::find_spans` | Returns filtered match spans for one line | `crates/gcode/src/commands/grep/grep_matcher.rs:33-42` |
| `has_identifier_boundaries` | Applies token-aware word matching to spans | `crates/gcode/src/commands/grep/grep_matcher.rs:46-64` |
| `has_adjacent_identifier_boundaries` | Checks immediate characters around a token | `crates/gcode/src/commands/grep/grep_matcher.rs:67-74` |
| `is_identifier_char` | Defines ASCII identifier characters | `crates/gcode/src/commands/grep/grep_matcher.rs:77-79` |

| Option/Input | Effect |
| --- | --- |
| `pattern` | Empty patterns error; otherwise compiled into regex |
| `fixed_strings` | Escapes the pattern before regex compilation |
| `ignore_case` | Enables case-insensitive regex matching |
| `word` | Requires ASCII identifier boundaries around matched source tokens |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/grep/grep_matcher.rs\|crates/gcode/src/commands/grep/grep_matcher.rs]] | `crates/gcode/src/commands/grep/grep_matcher.rs` exposes 14 indexed API symbols. |

