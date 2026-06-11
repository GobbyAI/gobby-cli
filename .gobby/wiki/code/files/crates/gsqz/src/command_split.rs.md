---
title: crates/gsqz/src/command_split.rs
type: code_file
provenance:
- file: crates/gsqz/src/command_split.rs
  ranges:
  - 5-85
  - 92-94
  - 97-102
  - 105-107
  - 110-112
  - 115-120
  - 123-128
  - 131-136
  - 139-144
  - 147-152
  - 155-157
  - 160-162
  - 165-167
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gsqz/src/command_split.rs

Module: [[code/modules/crates/gsqz/src|crates/gsqz/src]]

## Purpose

`crates/gsqz/src/command_split.rs` exposes 13 indexed API symbols.
[crates/gsqz/src/command_split.rs:5-85]
[crates/gsqz/src/command_split.rs:92-94]
[crates/gsqz/src/command_split.rs:97-102]
[crates/gsqz/src/command_split.rs:105-107]
[crates/gsqz/src/command_split.rs:110-112]

## API Symbols

- `split_compound` (function) component `split_compound [function]` (`b05a5755-3822-5184-a05f-511f79a33790`) lines 5-85 [crates/gsqz/src/command_split.rs:5-85]
  - Signature: `pub fn split_compound(cmd: &str) -> Vec<&str> {`
  - Purpose: Splits a shell command string into segments at top-level logical operators (`&&`, `||`, `;`) while respecting quoted strings and parenthesis nesting. [crates/gsqz/src/command_split.rs:5-85]
- `test_single_command` (function) component `test_single_command [function]` (`45ba74bd-50f6-57a2-a576-1b3170eb97c3`) lines 92-94 [crates/gsqz/src/command_split.rs:92-94]
  - Signature: `fn test_single_command() {`
  - Purpose: This unit test asserts that `split_compound()` returns a single-element vector containing the input string unchanged when given a non-compound command. [crates/gsqz/src/command_split.rs:92-94]
- `test_and_split` (function) component `test_and_split [function]` (`656178ad-02d7-5b7c-b1f0-8f943bf97c38`) lines 97-102 [crates/gsqz/src/command_split.rs:97-102]
  - Signature: `fn test_and_split() {`
  - Purpose: # Summary

This test function verifies that `split_compound` correctly tokenizes a shell command string joined with the `&&` operator into a vector of individual command strings. [crates/gsqz/src/command_split.rs:97-102]
- `test_or_split` (function) component `test_or_split [function]` (`d1136450-588e-5d0f-b375-4e045bb4afe1`) lines 105-107 [crates/gsqz/src/command_split.rs:105-107]
  - Signature: `fn test_or_split() {`
  - Purpose: This unit test verifies that `split_compound()` correctly parses a compound command string delimited by the logical OR operator (`||`) into separate command tokens. [crates/gsqz/src/command_split.rs:105-107]
- `test_semicolon_split` (function) component `test_semicolon_split [function]` (`c53d27cd-c4a3-56bc-9469-f247439d596b`) lines 110-112 [crates/gsqz/src/command_split.rs:110-112]
  - Signature: `fn test_semicolon_split() {`
  - Purpose: This test verifies that `split_compound()` correctly tokenizes a semicolon-delimited command string into individual command substrings. [crates/gsqz/src/command_split.rs:110-112]
- `test_mixed_operators` (function) component `test_mixed_operators [function]` (`6d44fdde-e21b-5d31-80a6-305aae293a20`) lines 115-120 [crates/gsqz/src/command_split.rs:115-120]
  - Signature: `fn test_mixed_operators() {`
  - Purpose: `test_mixed_operators` verifies that `split_compound` correctly parses a shell command string containing mixed control operators (&&, ||, ;) and returns a vector of individual commands. [crates/gsqz/src/command_split.rs:115-120]
- `test_pipe_not_split` (function) component `test_pipe_not_split [function]` (`fe8a10ef-6fc3-5e42-a152-493c66bbac0e`) lines 123-128 [crates/gsqz/src/command_split.rs:123-128]
  - Signature: `fn test_pipe_not_split() {`
  - Purpose: Tests that `split_compound` splits commands on the `&&` operator while treating the pipe operator `|` as a non-splitting delimiter within a single unit. [crates/gsqz/src/command_split.rs:123-128]
- `test_single_quoted_operators_preserved` (function) component `test_single_quoted_operators_preserved [function]` (`3ed46273-d30f-5730-a29c-b963fc40f853`) lines 131-136 [crates/gsqz/src/command_split.rs:131-136]
  - Signature: `fn test_single_quoted_operators_preserved() {`
  - Purpose: This test verifies that the `split_compound` function preserves operators within single-quoted strings as literal characters rather than interpreting them as command separators. [crates/gsqz/src/command_split.rs:131-136]
- `test_double_quoted_operators_preserved` (function) component `test_double_quoted_operators_preserved [function]` (`1fe14273-a3f1-5af3-98a7-3be5d6777bf5`) lines 139-144 [crates/gsqz/src/command_split.rs:139-144]
  - Signature: `fn test_double_quoted_operators_preserved() {`
  - Purpose: This test verifies that `split_compound` correctly splits shell commands on the unquoted `&&` operator while preserving `&&` operators inside double-quoted strings as literal content. [crates/gsqz/src/command_split.rs:139-144]
- `test_parenthesized_operators_preserved` (function) component `test_parenthesized_operators_preserved [function]` (`6789a3b7-180d-5c2e-b576-777993cb1662`) lines 147-152 [crates/gsqz/src/command_split.rs:147-152]
  - Signature: `fn test_parenthesized_operators_preserved() {`
  - Purpose: Tests that `split_compound` splits compound shell commands on `&&` operators while preserving parenthesized subexpressions as atomic units. [crates/gsqz/src/command_split.rs:147-152]
- `test_empty_string` (function) component `test_empty_string [function]` (`d485a5b9-8ddf-557c-8e41-1099affcb842`) lines 155-157 [crates/gsqz/src/command_split.rs:155-157]
  - Signature: `fn test_empty_string() {`
  - Purpose: This unit test verifies that `split_compound("")` returns a vector containing a single empty string when given an empty input. [crates/gsqz/src/command_split.rs:155-157]
- `test_trailing_operator` (function) component `test_trailing_operator [function]` (`7dca957d-80d4-543a-9b89-8ceaf07fa5a1`) lines 160-162 [crates/gsqz/src/command_split.rs:160-162]
  - Signature: `fn test_trailing_operator() {`
  - Purpose: This test verifies that `split_compound()` correctly discards trailing `&&` operators, returning only the valid command portion when parsing "cmd1 &&". [crates/gsqz/src/command_split.rs:160-162]
- `test_whitespace_trimming` (function) component `test_whitespace_trimming [function]` (`7d2016c1-ff23-50fd-905a-9cd16d8f98c5`) lines 165-167 [crates/gsqz/src/command_split.rs:165-167]
  - Signature: `fn test_whitespace_trimming() {`
  - Purpose: This test verifies that `split_compound` correctly strips leading and trailing whitespace from commands when parsing a compound command string delimited by `&&` operators. [crates/gsqz/src/command_split.rs:165-167]

