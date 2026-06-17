---
title: crates/gcode/src/index/parser/calls/resolution.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls/resolution.rs
  ranges:
  - 6-10
  - 17-21
  - 23-46
  - 48-62
  - 64-66
  - 68-96
  - 98-112
  - 114-122
  - 124-145
  - 147-202
  - 204-209
  - 211-222
  - 224-229
  - 239-285
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/parser/calls/resolution.rs:6-10](crates/gcode/src/index/parser/calls/resolution.rs#L6-L10), [crates/gcode/src/index/parser/calls/resolution.rs:17-21](crates/gcode/src/index/parser/calls/resolution.rs#L17-L21), [crates/gcode/src/index/parser/calls/resolution.rs:23-46](crates/gcode/src/index/parser/calls/resolution.rs#L23-L46), [crates/gcode/src/index/parser/calls/resolution.rs:48-62](crates/gcode/src/index/parser/calls/resolution.rs#L48-L62), [crates/gcode/src/index/parser/calls/resolution.rs:64-66](crates/gcode/src/index/parser/calls/resolution.rs#L64-L66), [crates/gcode/src/index/parser/calls/resolution.rs:68-96](crates/gcode/src/index/parser/calls/resolution.rs#L68-L96), [crates/gcode/src/index/parser/calls/resolution.rs:98-112](crates/gcode/src/index/parser/calls/resolution.rs#L98-L112), [crates/gcode/src/index/parser/calls/resolution.rs:114-122](crates/gcode/src/index/parser/calls/resolution.rs#L114-L122), [crates/gcode/src/index/parser/calls/resolution.rs:124-145](crates/gcode/src/index/parser/calls/resolution.rs#L124-L145), [crates/gcode/src/index/parser/calls/resolution.rs:147-202](crates/gcode/src/index/parser/calls/resolution.rs#L147-L202), [crates/gcode/src/index/parser/calls/resolution.rs:204-209](crates/gcode/src/index/parser/calls/resolution.rs#L204-L209), [crates/gcode/src/index/parser/calls/resolution.rs:211-222](crates/gcode/src/index/parser/calls/resolution.rs#L211-L222), [crates/gcode/src/index/parser/calls/resolution.rs:224-229](crates/gcode/src/index/parser/calls/resolution.rs#L224-L229), [crates/gcode/src/index/parser/calls/resolution.rs:239-285](crates/gcode/src/index/parser/calls/resolution.rs#L239-L285)

</details>

# crates/gcode/src/index/parser/calls/resolution.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

This file resolves call targets within the current file by combining tree-sitter syntax inspection with the file’s indexed symbols. It first classifies a call as `Bare`, `Member`, or `Other` via `CallSyntaxKind`, using `enclosing_symbol` to find the innermost symbol at a byte offset and `call_syntax_kind` plus syntax-kind predicates to detect whether the callee sits in a member-like expression. The resolution helpers then map a callee name and optional qualifier path to a same-file symbol ID: bare calls search for callable symbols by name, member calls try associated/member resolution, and qualified calls are split into root alias and path pieces before lookup. The remaining helpers support this pipeline by identifying unique symbols, extracting qualifier paths, and handling Lua-specific quoted `require` member qualifiers.
[crates/gcode/src/index/parser/calls/resolution.rs:6-10]
[crates/gcode/src/index/parser/calls/resolution.rs:17-21]
[crates/gcode/src/index/parser/calls/resolution.rs:23-46]
[crates/gcode/src/index/parser/calls/resolution.rs:48-62]
[crates/gcode/src/index/parser/calls/resolution.rs:64-66]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CallSyntaxKind` | type | `pub(super) enum CallSyntaxKind {` | `CallSyntaxKind [type]` | `05532d20-0797-5f98-b19e-15a7f431a888` | 6-10 [crates/gcode/src/index/parser/calls/resolution.rs:6-10] | Indexed type `CallSyntaxKind` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:6-10] |
| `enclosing_symbol` | function | `pub(super) fn enclosing_symbol(symbols: &[Symbol], byte_offset: usize) -> Option<&Symbol> {` | `enclosing_symbol [function]` | `9c30b856-c855-5c26-aa73-bdd164c437a1` | 17-21 [crates/gcode/src/index/parser/calls/resolution.rs:17-21] | Indexed function `enclosing_symbol` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:17-21] |
| `call_syntax_kind` | function | `pub(super) fn call_syntax_kind(` | `call_syntax_kind [function]` | `53222c78-5e39-5e45-a035-c9b48740a4d6` | 23-46 [crates/gcode/src/index/parser/calls/resolution.rs:23-46] | Indexed function `call_syntax_kind` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:23-46] |
| `is_memberish_kind` | function | `fn is_memberish_kind(kind: &str) -> bool {` | `is_memberish_kind [function]` | `6eca919c-11ec-5425-a720-90a47399bf04` | 48-62 [crates/gcode/src/index/parser/calls/resolution.rs:48-62] | Indexed function `is_memberish_kind` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:48-62] |
| `is_callable_kind` | function | `fn is_callable_kind(kind: &str) -> bool {` | `is_callable_kind [function]` | `2aa8732c-83b8-518b-b0a5-843da210d4b7` | 64-66 [crates/gcode/src/index/parser/calls/resolution.rs:64-66] | Indexed function `is_callable_kind` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:64-66] |
| `resolve_same_file_callee` | function | `fn resolve_same_file_callee(` | `resolve_same_file_callee [function]` | `f596569d-20cc-55b0-94fc-08854f353fac` | 68-96 [crates/gcode/src/index/parser/calls/resolution.rs:68-96] | Indexed function `resolve_same_file_callee` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:68-96] |
| `resolve_same_file_callee_for_language` | function | `pub(super) fn resolve_same_file_callee_for_language(` | `resolve_same_file_callee_for_language [function]` | `46568845-3c46-5115-ae60-d4d46c3a1e10` | 98-112 [crates/gcode/src/index/parser/calls/resolution.rs:98-112] | Indexed function `resolve_same_file_callee_for_language` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:98-112] |
| `unique_symbol_id` | function | `fn unique_symbol_id<'a>(symbols: impl Iterator<Item = &'a Symbol>) -> Option<String> {` | `unique_symbol_id [function]` | `1c703af1-47ef-5303-88a2-e47e55a8cb8b` | 114-122 [crates/gcode/src/index/parser/calls/resolution.rs:114-122] | Indexed function `unique_symbol_id` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:114-122] |
| `resolve_same_file_associated_callee` | function | `fn resolve_same_file_associated_callee(` | `resolve_same_file_associated_callee [function]` | `fdba7de9-f10d-58be-96c6-0d80689eecbf` | 124-145 [crates/gcode/src/index/parser/calls/resolution.rs:124-145] | Indexed function `resolve_same_file_associated_callee` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:124-145] |
| `member_qualifier_path` | function | `pub(super) fn member_qualifier_path(` | `member_qualifier_path [function]` | `ab9858ab-0b86-5a51-ab49-596b31f73e44` | 147-202 [crates/gcode/src/index/parser/calls/resolution.rs:147-202] | Indexed function `member_qualifier_path` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:147-202] |
| `call_qualifier_path` | function | `pub(in crate::index::parser) fn call_qualifier_path(` | `call_qualifier_path [function]` | `b2822686-5f91-5b6f-bd1c-5864535c80e3` | 204-209 [crates/gcode/src/index/parser/calls/resolution.rs:204-209] | Indexed function `call_qualifier_path` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:204-209] |
| `split_qualified_callee` | function | `pub(in crate::index::parser) fn split_qualified_callee(raw: &str) -> (String, Option<String>) {` | `split_qualified_callee [function]` | `1e7faef2-7c39-5488-a964-e922ebf42bdb` | 211-222 [crates/gcode/src/index/parser/calls/resolution.rs:211-222] | Indexed function `split_qualified_callee` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:211-222] |
| `qualifier_root_alias` | function | `pub(super) fn qualifier_root_alias(qualifier: &str) -> Option<&str> {` | `qualifier_root_alias [function]` | `2d7d0f18-dae7-5ea0-9ba1-98eb48cfb3c3` | 224-229 [crates/gcode/src/index/parser/calls/resolution.rs:224-229] | Indexed function `qualifier_root_alias` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:224-229] |
| `quoted_require_member_qualifier_is_lua_only` | function | `fn quoted_require_member_qualifier_is_lua_only() {` | `quoted_require_member_qualifier_is_lua_only [function]` | `e962f81d-c93c-5637-9fa7-a95893a9f737` | 239-285 [crates/gcode/src/index/parser/calls/resolution.rs:239-285] | Indexed function `quoted_require_member_qualifier_is_lua_only` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:239-285] |
