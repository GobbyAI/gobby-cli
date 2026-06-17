---
title: crates/gcode/src/commands/grep
type: code_module
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

# crates/gcode/src/commands/grep

Parent: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

The `grep` module is responsible for compiling search patterns and finding matching text spans within source lines, serving as the core query engine for grep operations [crates/gcode/src/commands/grep/grep_matcher.rs:6-9]. It compiles query patterns into regular expressions with configurable parameters for fixed-string (literal) matching and case insensitivity, raising an error for invalid regex configurations or empty patterns [crates/gcode/src/commands/grep/grep_matcher.rs:12-31]. During search operations, the module supports filtering matches using whole-word boundary logic based on ASCII identifiers (alphanumeric characters and underscores), ensuring that matches are not attached to adjacent identifier characters when word-matching is active [crates/gcode/src/commands/grep/grep_matcher.rs:33-43, crates/gcode/src/commands/grep/grep_matcher.rs:67-75].

The main workflow begins with the instantiation of `GrepMatcher` via its `new` method, which processes the pattern and constructs a `regex::Regex` instance [crates/gcode/src/commands/grep/grep_matcher.rs:12-31]. Consumers of this module execute searches on individual text lines by calling `find_spans`, which returns a vector of matched byte ranges in the form of `GrepSpan` objects [crates/gcode/src/commands/grep/grep_matcher.rs:3-3, crates/gcode/src/commands/grep/grep_matcher.rs:33-43]. If word-boundary filtering is requested, matching ranges are validated through identifier boundaries, checking adjacent characters before and after the matched span to ensure correctness .

### Public & Internal Module API Symbols

| Symbol | Type | Description | Reference |
| --- | --- | --- | --- |
| `GrepMatcher` | struct | The grep compilation and line-matching engine. |  |
| `GrepMatcher::new` | method | Validates, compiles, and configures the search pattern. | [crates/gcode/src/commands/grep/grep_matcher.rs:12-31] |
| `GrepMatcher::find_spans` | method | Scans a line and returns matching spans, applying word filtering if enabled. | [crates/gcode/src/commands/grep/grep_matcher.rs:33-43] |
| `GrepSpan` | struct | Contains start and end byte offsets of a matching text segment. |  |

### Search Configuration Mapping

| Parameter | Type | CLI / Query Flag Context | Description | Reference |
| --- | --- | --- | --- | --- |
| `fixed_strings` | bool | Literal search mode | Disables regex features by escaping pattern special characters. | [crates/gcode/src/commands/grep/grep_matcher.rs:14-14, crates/gcode/src/commands/grep/grep_matcher.rs:20-24] |
| `ignore_case` | bool | Case-insensitive option | Directs the RegexBuilder to perform case-insensitive evaluation. | [crates/gcode/src/commands/grep/grep_matcher.rs:15-15, crates/gcode/src/commands/grep/grep_matcher.rs:26-26] |
| `word` | bool | Word match flag (`-w`) | Filters matches using ASCII identifier boundaries. | [crates/gcode/src/commands/grep/grep_matcher.rs:16-16, crates/gcode/src/commands/grep/grep_matcher.rs:72-72] |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/grep/grep_matcher.rs\|crates/gcode/src/commands/grep/grep_matcher.rs]] | Implements `GrepMatcher`, the grep engine used by `gcode` to compile a pattern and find matching spans in a line, with support for fixed-string matching, case-insensitive matching, and optional `-w` word filtering. `new` validates and builds the regex, `find_spans` returns non-empty match ranges as `GrepSpan`s, and the helper functions enforce ASCII identifier boundary rules so word matches only accept tokens that are not attached to identifier characters, while the tests cover boundary behavior, Unicode handling, regex errors, and empty-pattern rejection. [crates/gcode/src/commands/grep/grep_matcher.rs:6-9] [crates/gcode/src/commands/grep/grep_matcher.rs:12-31] [crates/gcode/src/commands/grep/grep_matcher.rs:33-43] [crates/gcode/src/commands/grep/grep_matcher.rs:46-65] [crates/gcode/src/commands/grep/grep_matcher.rs:67-75] |

## Components

| Component ID |
| --- |
| `628d07b3-d008-5bd5-b330-fd328ea2e211` |
| `d1bd0c60-2fe5-5595-9339-d69f73a7452f` |
| `6a2a20ca-13b7-57a9-84f5-bed7f3582e09` |
| `b7c64e1e-2670-5052-831b-225b2f9a292e` |
| `66514ac7-12ff-5a73-a43b-5a9b52f7fac1` |
| `d8abe9ae-62da-5d0d-9ea7-406ef25efc79` |
| `ec6e1cd7-3f22-5b82-88eb-84fcfdcf457b` |
| `a55a9acd-0567-5e5a-98f2-a22b2aa210c2` |
| `b050eb19-6a18-5775-b254-bc8e4d0e696e` |
| `d9092c4b-2a69-5609-b202-ef7e6aa45ad6` |
| `61b156f4-c2f7-5e1b-9c94-db8161d42e77` |
| `5137b80c-cf7d-5427-8c2f-097cb213767b` |
| `02637ee7-bb0a-5844-a952-69604eb7e63b` |
| `0d0f04a2-4906-5fe9-b7ab-04b7650a05b7` |
