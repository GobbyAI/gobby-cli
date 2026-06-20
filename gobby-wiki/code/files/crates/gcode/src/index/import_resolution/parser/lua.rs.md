---
title: crates/gcode/src/index/import_resolution/parser/lua.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/lua.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/lua.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/parser/lua.rs` exposes 6 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/parser/lua.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `parse_lua_import_statement` | function | Parses a Lua 'require' import statement by normalizing whitespace, extracting the quoted module name, recording an 'ImportRelation', resolving candidate module files, and, when the statement is an assignment, registering either a bare or member local binding for the alias. [crates/gcode/src/index/import_resolution/parser/lua.rs:6-44] |
| `resolve_lua_require_member_callee` | function | Returns a 'LocalCallBinding' for a Lua member-call target only when 'is_member_call' is true and the qualifier is a 'require(...)' expression that yields at least one module file, otherwise 'None'. [crates/gcode/src/index/import_resolution/parser/lua.rs:46-68] |
| `lua_require_assignment` | function | Parses a Lua assignment of the form 'local? <identifier> = ...require...' and, if the left-hand side is a single valid Lua identifier, returns that variable name plus any member path extracted from the expression following 'require', otherwise 'None'. [crates/gcode/src/index/import_resolution/parser/lua.rs:70-85] |
| `after_first_quoted_string` | function | Returns the substring immediately following the first matching closing quote (''' or '"') that terminates the first quoted section in 'text', while correctly skipping escaped characters, or 'None' if no complete quoted string is found. [crates/gcode/src/index/import_resolution/parser/lua.rs:87-111] |
| `lua_member_after_require` | function | Parses and returns the first Lua member identifier immediately following an optional leading ')' and then a '.' or ':' separator, accepting only ASCII alphanumerics and underscores when the identifier satisfies 'is_lua_identifier'. [crates/gcode/src/index/import_resolution/parser/lua.rs:113-128] |
| `is_lua_identifier` | function | Returns 'true' iff 'name' is non-empty and consists of an ASCII letter or '_' as the first character followed only by ASCII alphanumeric characters or '_'. [crates/gcode/src/index/import_resolution/parser/lua.rs:130-137] |

