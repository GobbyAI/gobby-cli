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

`crates/gcode/src/index/parser/calls/shadowing.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

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
| `split_assignment_ignores_bitwise_compound_operators` | function | Ensures 'split_assignment' returns 'None' for compound assignment operators ('&=', '\|=', '^=', '+=', '@=', '??=', '&&=', '\|\|=', '**=', '<<=', '>>=') and still splits a plain '=' assignment such as 'flags = READ \| WRITE'. [crates/gcode/src/index/parser/calls/shadowing.rs:283-299] |
| `name_first_declarations_use_declared_name` | function | Tests that 'declaration_without_assignment_contains' matches the declared identifier in uninitialized declarations like 'var client http.Client' and 'val owner: User', and does not match the type name 'Client'. [crates/gcode/src/index/parser/calls/shadowing.rs:302-315] |
| `typed_assignment_bindings_use_name_before_colon` | function | Verifies that 'binding_left_side_contains' matches the identifier before the type annotation in a typed 'let' binding, returning true for 'owner' and false for 'User'. [crates/gcode/src/index/parser/calls/shadowing.rs:318-327] |
| `block_comments_do_not_define_shadowing_bindings` | function | It verifies that a 'const fetch = ...' declaration inside a block comment is ignored by comment stripping and does not create a shadowing 'fetch' binding before the later 'fetch()' call. [crates/gcode/src/index/parser/calls/shadowing.rs:330-339] |
| `nested_block_comments_do_not_leak_inner_tail` | function | Verifies that nested block comments are fully removed without exposing the inner comment tail, leaving 'fetch()' intact and not treating 'fetch' as in scope before the call. [crates/gcode/src/index/parser/calls/shadowing.rs:342-351] |
| `unclosed_block_comments_are_treated_as_eof_terminated` | function | Verifies that an unclosed '/* ...' block comment is treated as terminating at EOF, so 'remove_block_comments' strips the trailing commented code and 'local_name_in_scope_before_call' does not see names declared only inside that comment. [crates/gcode/src/index/parser/calls/shadowing.rs:354-363] |

