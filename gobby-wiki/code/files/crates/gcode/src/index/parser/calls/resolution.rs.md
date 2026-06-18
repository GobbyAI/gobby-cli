---
title: crates/gcode/src/index/parser/calls/resolution.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls/resolution.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser/calls/resolution.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

`crates/gcode/src/index/parser/calls/resolution.rs` exposes 14 indexed API symbols.

## How it fits

`crates/gcode/src/index/parser/calls/resolution.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CallSyntaxKind` | type | Indexed type `CallSyntaxKind` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:6-10] |
| `enclosing_symbol` | function | Returns the last 'Symbol' in 'symbols' whose byte range contains 'byte_offset' ('byte_start <= byte_offset < byte_end'), or 'None' if no such symbol exists. [crates/gcode/src/index/parser/calls/resolution.rs:17-21] |
| `call_syntax_kind` | function | 'call_syntax_kind' walks upward from 'name_node' to 'call_node' and classifies the call as 'Bare' if the name is the direct child of the call node, 'Member' if any ancestor on the path is member-like, and 'Other' if it reaches the call node or root without matching either case. [crates/gcode/src/index/parser/calls/resolution.rs:23-46] |
| `is_memberish_kind` | function | Returns 'true' if 'kind' is one of the member-like syntax kinds ('attribute', 'member_expression', 'selector_expression', 'field_expression', 'member_access_expression', 'member_call_expression', 'navigation_expression', 'scoped_identifier', 'scoped_call_expression', or 'dot'), and 'false' otherwise. [crates/gcode/src/index/parser/calls/resolution.rs:48-62] |
| `is_callable_kind` | function | Returns 'true' if 'kind' is exactly '"function"', '"method"', or '"class"', and 'false' otherwise. [crates/gcode/src/index/parser/calls/resolution.rs:64-66] |
| `resolve_same_file_callee` | function | Resolves a call site within the same file to a unique callee symbol ID by matching bare calls against callable symbols named 'callee_name', matching member calls first via associated/qualified resolution then by same-parent method lookup, and returning 'None' for unsupported syntax kinds. [crates/gcode/src/index/parser/calls/resolution.rs:68-96] |
| `resolve_same_file_callee_for_language` | function | Returns 'None' for bare Ruby calls to avoid spurious same-file matches from dynamic dispatch, otherwise delegates to 'resolve_same_file_callee' with the provided symbols, caller, callee name, qualifier path, and call syntax. [crates/gcode/src/index/parser/calls/resolution.rs:98-112] |
| `unique_symbol_id` | function | Returns 'Some(first.id.clone())' only when the iterator contains exactly one 'Symbol', and returns 'None' for an empty iterator or any iterator with more than one item. [crates/gcode/src/index/parser/calls/resolution.rs:114-122] |
| `resolve_same_file_associated_callee` | function | Returns the unique symbol ID of a method named 'callee_name' whose 'parent_symbol_id' matches a class/type symbol identified by 'qualifier_path', or 'None' if the qualifier is absent or no unique match exists. [crates/gcode/src/index/parser/calls/resolution.rs:124-145] |
| `member_qualifier_path` | function | Extracts and normalizes the member/callee qualifier text preceding 'name_node' from 'source' for a call expression, rejecting bare calls, '$'/'->' prefixes, and non-separator suffixes, preserving absolute namespaces and Lua 'require' string qualifiers, and returning the parsed qualifier as 'Option<String>'. [crates/gcode/src/index/parser/calls/resolution.rs:147-202] |
| `call_qualifier_path` | function | Returns the first available qualifier by preferring 'qualifier_from_name' and otherwise invoking 'qualifier_from_member', yielding an 'Option<String>'. [crates/gcode/src/index/parser/calls/resolution.rs:204-209] |
| `split_qualified_callee` | function | Trims the input and returns '(callee_name, Some(qualifier))' by splitting on the last valid '::', '\', or '.' separator when both sides are non-empty, otherwise returns '(raw, None)'. [crates/gcode/src/index/parser/calls/resolution.rs:211-222] |
| `qualifier_root_alias` | function | Returns the first non-empty root segment of a 'qualifier' after trimming leading backslashes and splitting on '.', ':', or '\', or 'None' if no such segment exists. [crates/gcode/src/index/parser/calls/resolution.rs:224-229] |
| `quoted_require_member_qualifier_is_lua_only` | function | Parses a JavaScript 'require("./utils").helper()' call with tree-sitter, extracts the member qualifier path for the call and property identifier, and asserts that 'member_qualifier_path' returns the full quoted 'require("./utils")' only for Lua mode while returning just 'require' for JavaScript mode. [crates/gcode/src/index/parser/calls/resolution.rs:239-285] |

