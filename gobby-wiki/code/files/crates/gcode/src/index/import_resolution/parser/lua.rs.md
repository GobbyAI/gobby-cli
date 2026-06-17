---
title: crates/gcode/src/index/import_resolution/parser/lua.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/lua.rs
  ranges:
  - 6-44
  - 46-68
  - 70-85
  - 87-111
  - 113-128
  - 130-137
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/parser/lua.rs:6-44](crates/gcode/src/index/import_resolution/parser/lua.rs#L6-L44), [crates/gcode/src/index/import_resolution/parser/lua.rs:46-68](crates/gcode/src/index/import_resolution/parser/lua.rs#L46-L68), [crates/gcode/src/index/import_resolution/parser/lua.rs:70-85](crates/gcode/src/index/import_resolution/parser/lua.rs#L70-L85), [crates/gcode/src/index/import_resolution/parser/lua.rs:87-111](crates/gcode/src/index/import_resolution/parser/lua.rs#L87-L111), [crates/gcode/src/index/import_resolution/parser/lua.rs:113-128](crates/gcode/src/index/import_resolution/parser/lua.rs#L113-L128), [crates/gcode/src/index/import_resolution/parser/lua.rs:130-137](crates/gcode/src/index/import_resolution/parser/lua.rs#L130-L137)

</details>

# crates/gcode/src/index/import_resolution/parser/lua.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

This file extracts Lua import relationships and callable bindings from source text. `parse_lua_import_statement` normalizes a statement, finds `require` and its quoted module path, records the import, and, when it sees a valid `local` assignment, binds either the whole required module or a specific member to matching module files; `resolve_lua_require_member_callee` performs the same module lookup for member-style calls on `require(...)`, while the helper functions parse assignment structure, locate text after the first quoted string, detect member access after `require`, and validate Lua identifiers.
[crates/gcode/src/index/import_resolution/parser/lua.rs:6-44]
[crates/gcode/src/index/import_resolution/parser/lua.rs:46-68]
[crates/gcode/src/index/import_resolution/parser/lua.rs:70-85]
[crates/gcode/src/index/import_resolution/parser/lua.rs:87-111]
[crates/gcode/src/index/import_resolution/parser/lua.rs:113-128]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `parse_lua_import_statement` | function | `pub(crate) fn parse_lua_import_statement(` | `parse_lua_import_statement [function]` | `3e1957e4-ed67-566b-bcbe-eaa6451a06c8` | 6-44 [crates/gcode/src/index/import_resolution/parser/lua.rs:6-44] | Indexed function `parse_lua_import_statement` in `crates/gcode/src/index/import_resolution/parser/lua.rs`. [crates/gcode/src/index/import_resolution/parser/lua.rs:6-44] |
| `resolve_lua_require_member_callee` | function | `pub(crate) fn resolve_lua_require_member_callee(` | `resolve_lua_require_member_callee [function]` | `38a34874-ccac-532b-ad3a-d5197d39f2e5` | 46-68 [crates/gcode/src/index/import_resolution/parser/lua.rs:46-68] | Indexed function `resolve_lua_require_member_callee` in `crates/gcode/src/index/import_resolution/parser/lua.rs`. [crates/gcode/src/index/import_resolution/parser/lua.rs:46-68] |
| `lua_require_assignment` | function | `fn lua_require_assignment(text: &str) -> Option<(String, Option<String>)> {` | `lua_require_assignment [function]` | `1bcda28c-5e7e-58ca-b1da-ea2f099d0795` | 70-85 [crates/gcode/src/index/import_resolution/parser/lua.rs:70-85] | Indexed function `lua_require_assignment` in `crates/gcode/src/index/import_resolution/parser/lua.rs`. [crates/gcode/src/index/import_resolution/parser/lua.rs:70-85] |
| `after_first_quoted_string` | function | `fn after_first_quoted_string(text: &str) -> Option<&str> {` | `after_first_quoted_string [function]` | `33339e4a-3cb4-55b1-968a-c5528dcc91e6` | 87-111 [crates/gcode/src/index/import_resolution/parser/lua.rs:87-111] | Indexed function `after_first_quoted_string` in `crates/gcode/src/index/import_resolution/parser/lua.rs`. [crates/gcode/src/index/import_resolution/parser/lua.rs:87-111] |
| `lua_member_after_require` | function | `fn lua_member_after_require(text: &str) -> Option<String> {` | `lua_member_after_require [function]` | `1ee7d248-f3a4-52e5-b0bc-40bd5e06ca75` | 113-128 [crates/gcode/src/index/import_resolution/parser/lua.rs:113-128] | Indexed function `lua_member_after_require` in `crates/gcode/src/index/import_resolution/parser/lua.rs`. [crates/gcode/src/index/import_resolution/parser/lua.rs:113-128] |
| `is_lua_identifier` | function | `fn is_lua_identifier(name: &str) -> bool {` | `is_lua_identifier [function]` | `64ed031c-38d0-5f4c-92aa-4c877fb6cf37` | 130-137 [crates/gcode/src/index/import_resolution/parser/lua.rs:130-137] | Indexed function `is_lua_identifier` in `crates/gcode/src/index/import_resolution/parser/lua.rs`. [crates/gcode/src/index/import_resolution/parser/lua.rs:130-137] |
