---
title: crates/gcode/src/commands/grep
type: code_module
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

# crates/gcode/src/commands/grep

Parent: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

The grep command module centers on `GrepMatcher`, a small regex-backed matcher that turns user grep options into reusable line-matching behavior. It owns a compiled `regex::Regex` plus the `word` flag, rejects empty patterns, escapes patterns for fixed-string mode, applies optional case-insensitive matching, and wraps regex build failures with the “invalid gcode grep pattern” context before returning the matcher .

At match time, `find_spans` scans each line with `find_iter`, drops zero-width matches, converts results into `GrepSpan` start/end byte ranges, and conditionally filters matches through word-boundary logic when `-w` behavior is enabled [crates/gcode/src/commands/grep/grep_matcher.rs:33-43]. That boundary flow first finds the identifier-like token inside the matched span, falls back to checking the whole span when no identifier characters are present, and then verifies the characters immediately before and after are not identifier characters [crates/gcode/src/commands/grep/grep_matcher.rs:46-65].

The module’s collaboration boundary is intentionally narrow: it imports `GrepSpan` from the parent grep command module and returns only those spans, leaving presentation and command orchestration outside this file . Its word matching is tuned for indexed source tokens by treating only ASCII alphanumerics and underscores as identifier characters, so Unicode and punctuation behave as separators while source-style names remain protected from partial matches [crates/gcode/src/commands/grep/grep_matcher.rs:67-70].

## Call Diagram

```mermaid
sequenceDiagram
    participant m_66514ac7_12ff_5a73_a43b_5a9b52f7fac1 as has_adjacent_identifier_boundaries &#91;function&#93;
    participant m_6a2a20ca_13b7_57a9_84f5_bed7f3582e09 as GrepMatcher.find_spans &#91;method&#93;
    participant m_b7c64e1e_2670_5052_831b_225b2f9a292e as has_identifier_boundaries &#91;function&#93;
    participant m_d8abe9ae_62da_5d0d_9ea7_406ef25efc79 as is_identifier_char &#91;function&#93;
    m_6a2a20ca_13b7_57a9_84f5_bed7f3582e09->>m_b7c64e1e_2670_5052_831b_225b2f9a292e: calls
    m_b7c64e1e_2670_5052_831b_225b2f9a292e->>m_66514ac7_12ff_5a73_a43b_5a9b52f7fac1: calls
    m_b7c64e1e_2670_5052_831b_225b2f9a292e->>m_d8abe9ae_62da_5d0d_9ea7_406ef25efc79: calls
```

## Files

- [[code/files/crates/gcode/src/commands/grep/grep_matcher.rs|crates/gcode/src/commands/grep/grep_matcher.rs]] - This file implements GrepMatcher, a regex-based pattern matching utility for grep operations. The GrepMatcher struct wraps a compiled regex and optional word-boundary enforcement, constructed via the new() method which validates non-empty patterns, optionally escapes them for literal matching, and builds case-insensitive regex when requested. The find_spans() method locates all non-zero-width matches in a line and optionally filters them through word-boundary validation. Word-boundary checking relies on helper functions that extract identifier tokens from match spans and validate no ASCII alphanumeric characters or underscores are adjacent to the match, effectively treating only ASCII identifiers as word constituents while treating Unicode and other characters as word separators. The matched_texts() utility function extracts matched substrings from results. Comprehensive unit tests verify correct matching behavior across literal strings, case sensitivity, word boundaries with various adjacent character types (delimiters, operators, Unicode), and proper error reporting for invalid regex patterns and empty input.
[crates/gcode/src/commands/grep/grep_matcher.rs:6-9]
[crates/gcode/src/commands/grep/grep_matcher.rs:11-44]
[crates/gcode/src/commands/grep/grep_matcher.rs:12-31]
[crates/gcode/src/commands/grep/grep_matcher.rs:33-43]
[crates/gcode/src/commands/grep/grep_matcher.rs:46-65]

## Components

- `628d07b3-d008-5bd5-b330-fd328ea2e211`
- `e4a0bd8c-b79b-55fb-8ef1-7ad41194a5f1`
- `d1bd0c60-2fe5-5595-9339-d69f73a7452f`
- `6a2a20ca-13b7-57a9-84f5-bed7f3582e09`
- `b7c64e1e-2670-5052-831b-225b2f9a292e`
- `66514ac7-12ff-5a73-a43b-5a9b52f7fac1`
- `d8abe9ae-62da-5d0d-9ea7-406ef25efc79`
- `ec6e1cd7-3f22-5b82-88eb-84fcfdcf457b`
- `a55a9acd-0567-5e5a-98f2-a22b2aa210c2`
- `b050eb19-6a18-5775-b254-bc8e4d0e696e`
- `d9092c4b-2a69-5609-b202-ef7e6aa45ad6`
- `61b156f4-c2f7-5e1b-9c94-db8161d42e77`
- `5137b80c-cf7d-5427-8c2f-097cb213767b`
- `02637ee7-bb0a-5844-a952-69604eb7e63b`
- `0d0f04a2-4906-5fe9-b7ab-04b7650a05b7`

