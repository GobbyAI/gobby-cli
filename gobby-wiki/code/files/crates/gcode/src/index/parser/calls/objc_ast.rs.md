---
title: crates/gcode/src/index/parser/calls/objc_ast.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls/objc_ast.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser/calls/objc_ast.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

`crates/gcode/src/index/parser/calls/objc_ast.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gcode/src/index/parser/calls/objc_ast.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `extract_objc_calls` | function | Parses the given Tree-sitter AST with the language-specific call query, selects the best 'name'/'call'/'receiver' captures for each match, and returns a 'Vec<CallRelation>' representing extracted Objective-C call sites, or an empty vector if no call query is configured. [crates/gcode/src/index/parser/calls/objc_ast.rs:16-119] |
| `objc_message_receiver_qualifier` | function | It extracts the receiver text for an Objective-C message send, returns 'None' for non-identifiers or 'self'/'super', returns the text unchanged if it starts with an ASCII uppercase letter, and otherwise infers the receiver’s type qualifier via 'objc_variable_type_before(source, call_start, receiver_text)'. [crates/gcode/src/index/parser/calls/objc_ast.rs:121-140] |
| `objc_variable_type_before` | function | Scans up to the 80 most recent lines before 'call_start' in 'source' and returns the first Objective-C variable type string found for 'variable' via 'objc_variable_type_from_line', or 'None' if no match is found. [crates/gcode/src/index/parser/calls/objc_ast.rs:142-150] |
| `objc_variable_type_from_line` | function | Returns the nearest preceding Objective-C type identifier for 'variable' on a line, ignoring comments and enforcing identifier boundaries, or 'None' if no valid type token is found. [crates/gcode/src/index/parser/calls/objc_ast.rs:152-169] |
| `is_identifier_boundary` | function | Returns 'true' when the substring 'text[start..start + len]' is bounded on both sides by either the string edges or non-identifier-continuation characters, making it a whole identifier token. [crates/gcode/src/index/parser/calls/objc_ast.rs:171-181] |
| `is_objc_type_identifier` | function | Returns 'true' only if 'name' is a valid Objective-C identifier and its first character is an ASCII uppercase letter. [crates/gcode/src/index/parser/calls/objc_ast.rs:183-189] |
| `is_objc_identifier` | function | Returns 'true' if 'name' is non-empty and its first character is either a valid identifier start or '_', and all remaining characters satisfy 'is_identifier_continue'. [crates/gcode/src/index/parser/calls/objc_ast.rs:191-197] |

