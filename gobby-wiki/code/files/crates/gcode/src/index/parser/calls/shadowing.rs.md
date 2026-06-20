---
title: crates/gcode/src/index/parser/calls/shadowing.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls/shadowing.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser/calls/shadowing.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

`crates/gcode/src/index/parser/calls/shadowing.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gcode/src/index/parser/calls/shadowing.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `external_call_is_shadowed` | function | Returns 'true' when the call’s resolved shadow name is a non-empty bare callee name or member root alias that is already locally in scope before 'call_byte', and 'false' otherwise. [crates/gcode/src/index/parser/calls/shadowing.rs:6-23] |
| `local_name_in_scope_before_call` | function | Returns 'true' if, between the caller symbol’s start byte and the call site, the source prefix contains either a matching parameter name in the function’s parameter list or a local binding line that defines 'name', after stripping block comments, and 'false' otherwise. [crates/gcode/src/index/parser/calls/shadowing.rs:25-43] |
| `remove_block_comments` | function | Removes nested C-style block comments delimited by '/*' and '*/' from a string by scanning left to right, preserving non-comment text, and returning the partially cleaned prefix if an unterminated block comment is encountered. [crates/gcode/src/index/parser/calls/shadowing.rs:45-84] |
| `parameter_list_contains_name` | function | Returns 'true' if 'prefix' contains a balanced parenthesized parameter list whose comma-separated segments include a parameter name equal to 'name', and 'false' otherwise. [crates/gcode/src/index/parser/calls/shadowing.rs:86-96] |
| `matching_paren_in_str` | function | Scans 'text' from the given byte offset 'open', tracks nested '(' and ')' with a depth counter, and returns the byte index of the first ')' that brings depth back to zero, or 'None' if no such closing parenthesis is found. [crates/gcode/src/index/parser/calls/shadowing.rs:98-113] |
| `parameter_segment_name` | function | Returns the first non-empty, trimmed identifier-like token in 'segment' before any '=' or ':' delimiter, after stripping surrounding whitespace and trimming identifier token punctuation, or 'None' if no such token exists. [crates/gcode/src/index/parser/calls/shadowing.rs:115-129] |
| `local_binding_line_defines` | function | Returns 'true' if the trimmed line is a non-empty, non-comment, non-import/use statement that defines 'name' via a ':=' binding, a standard assignment, or a declaration without assignment, and 'false' otherwise. [crates/gcode/src/index/parser/calls/shadowing.rs:131-153] |
| `split_assignment` | function | 'split_assignment' scans a line while tracking single/double quotes and escapes, ignores '//' and '#' comments, and returns the first unquoted standalone '=' as a '(left, right)' split only when it is not part of a comparison, compound, or arrow/operator sequence. [crates/gcode/src/index/parser/calls/shadowing.rs:155-218] |
| `binding_left_side_contains` | function | Returns 'true' if any comma-separated binding name parsed from 'left' exactly matches 'name', otherwise 'false'. [crates/gcode/src/index/parser/calls/shadowing.rs:220-224] |
| `binding_name_from_left_part` | function | Returns the last whitespace-delimited token from the left side of a ':'-separated string, after trimming and rejecting any segment containing '.', '[', or ']', then normalizing it with 'trim_identifier_token' and returning 'None' if the result is empty. [crates/gcode/src/index/parser/calls/shadowing.rs:226-235] |
| `declaration_without_assignment_contains` | function | It returns 'true' if 'line' is a variable declaration without an assignment whose comma- or semicolon-separated bindings contain 'name', handling 'let'/'const'/'var'/'val' via 'binding_name_from_name_first_part' and 'final'/'late'/'auto' via 'binding_name_from_left_part'. [crates/gcode/src/index/parser/calls/shadowing.rs:237-260] |
| `binding_name_from_name_first_part` | function | Trims the input, takes its first whitespace-delimited token, rejects it if it contains '.', '[', or ']', then returns the first ':'-delimited segment after trimming identifier whitespace, provided it is non-empty, otherwise 'None'. [crates/gcode/src/index/parser/calls/shadowing.rs:262-273] |

_Verified by 6 in-file unit tests._

