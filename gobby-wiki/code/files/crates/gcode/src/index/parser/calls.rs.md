---
title: crates/gcode/src/index/parser/calls.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls.rs
  ranges:
  - 26-35
  - 38-45
  - 47-61
  - 63-443
  - 445-464
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/parser/calls.rs:26-35](crates/gcode/src/index/parser/calls.rs#L26-L35), [crates/gcode/src/index/parser/calls.rs:38-45](crates/gcode/src/index/parser/calls.rs#L38-L45), [crates/gcode/src/index/parser/calls.rs:47-61](crates/gcode/src/index/parser/calls.rs#L47-L61), [crates/gcode/src/index/parser/calls.rs:63-443](crates/gcode/src/index/parser/calls.rs#L63-L443), [crates/gcode/src/index/parser/calls.rs:445-464](crates/gcode/src/index/parser/calls.rs#L445-L464)

</details>

# crates/gcode/src/index/parser/calls.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

This file builds call-relation extraction for indexed source files. `extract_calls` dispatches by language to language-specific strategies: textual Dart handling, Objective-C AST handling, or the general AST path. `CallExtractionContext` carries the file, symbol, import, and language state needed during extraction, while `CallSite` is the internal representation of a discovered call before it is turned into a `CallRelation`. `materialize_call` resolves a `CallSite` into a concrete relation by finding the enclosing caller symbol, adjusting qualifiers when needed, and optionally using semantic resolution. `lua_require_qualifier_before_name` is a Lua-specific helper for recovering `require` qualifiers from source text.
[crates/gcode/src/index/parser/calls.rs:26-35]
[crates/gcode/src/index/parser/calls.rs:38-45]
[crates/gcode/src/index/parser/calls.rs:47-61]
[crates/gcode/src/index/parser/calls.rs:63-443]
[crates/gcode/src/index/parser/calls.rs:445-464]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CallExtractionContext` | class | `pub(super) struct CallExtractionContext<'a> {` | `CallExtractionContext [class]` | `d6a9337c-e91f-51f2-ab7a-3e09d9c76d54` | 26-35 [crates/gcode/src/index/parser/calls.rs:26-35] | Indexed class `CallExtractionContext` in `crates/gcode/src/index/parser/calls.rs`. [crates/gcode/src/index/parser/calls.rs:26-35] |
| `CallSite` | class | `struct CallSite {` | `CallSite [class]` | `bb7b96bd-5bc7-596e-bcdf-e71a138157c6` | 38-45 [crates/gcode/src/index/parser/calls.rs:38-45] | Indexed class `CallSite` in `crates/gcode/src/index/parser/calls.rs`. [crates/gcode/src/index/parser/calls.rs:38-45] |
| `extract_calls` | function | `pub(super) fn extract_calls(` | `extract_calls [function]` | `4fbb11be-6ade-5beb-8319-d251fa699b44` | 47-61 [crates/gcode/src/index/parser/calls.rs:47-61] | Indexed function `extract_calls` in `crates/gcode/src/index/parser/calls.rs`. [crates/gcode/src/index/parser/calls.rs:47-61] |
| `materialize_call` | function | `fn materialize_call(` | `materialize_call [function]` | `33296882-0bdf-5b08-889a-5c6ed6eef29a` | 63-443 [crates/gcode/src/index/parser/calls.rs:63-443] | Indexed function `materialize_call` in `crates/gcode/src/index/parser/calls.rs`. [crates/gcode/src/index/parser/calls.rs:63-443] |
| `lua_require_qualifier_before_name` | function | `fn lua_require_qualifier_before_name(source: &[u8], name_byte: usize) -> Option<String> {` | `lua_require_qualifier_before_name [function]` | `134c9149-8205-5fa4-9544-0f9f1f3f3881` | 445-464 [crates/gcode/src/index/parser/calls.rs:445-464] | Indexed function `lua_require_qualifier_before_name` in `crates/gcode/src/index/parser/calls.rs`. [crates/gcode/src/index/parser/calls.rs:445-464] |
