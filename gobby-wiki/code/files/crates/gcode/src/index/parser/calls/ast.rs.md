---
title: crates/gcode/src/index/parser/calls/ast.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls/ast.rs
  ranges:
  - 17-103
  - 105-135
  - 148-179
  - 181-193
  - 196-205
  - 208-217
  - 220-235
  - 238-252
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/parser/calls/ast.rs:17-103](crates/gcode/src/index/parser/calls/ast.rs#L17-L103), [crates/gcode/src/index/parser/calls/ast.rs:105-135](crates/gcode/src/index/parser/calls/ast.rs#L105-L135), [crates/gcode/src/index/parser/calls/ast.rs:148-179](crates/gcode/src/index/parser/calls/ast.rs#L148-L179), [crates/gcode/src/index/parser/calls/ast.rs:181-193](crates/gcode/src/index/parser/calls/ast.rs#L181-L193), [crates/gcode/src/index/parser/calls/ast.rs:196-205](crates/gcode/src/index/parser/calls/ast.rs#L196-L205), [crates/gcode/src/index/parser/calls/ast.rs:208-217](crates/gcode/src/index/parser/calls/ast.rs#L208-L217), [crates/gcode/src/index/parser/calls/ast.rs:220-235](crates/gcode/src/index/parser/calls/ast.rs#L220-L235), [crates/gcode/src/index/parser/calls/ast.rs:238-252](crates/gcode/src/index/parser/calls/ast.rs#L238-L252)

</details>

# crates/gcode/src/index/parser/calls/ast.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

This file extracts call relations from Tree-sitter AST queries for multiple languages and turns matched call sites into `CallRelation` records. `extract_ast_calls` is the main entry point: it compiles the language’s call query, walks query matches, finds the `name` and optional `call` captures, filters ignored names, handles language-specific special cases like Elixir definition heads, and then materializes each call with qualifier-path and semantic-resolution helpers; the JS-specific helpers and the small test cases exercise capture handling, qualifier splitting, and when bare or qualified names should be treated as member calls.
[crates/gcode/src/index/parser/calls/ast.rs:17-103]
[crates/gcode/src/index/parser/calls/ast.rs:105-135]
[crates/gcode/src/index/parser/calls/ast.rs:148-179]
[crates/gcode/src/index/parser/calls/ast.rs:181-193]
[crates/gcode/src/index/parser/calls/ast.rs:196-205]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `extract_ast_calls` | function | `pub(super) fn extract_ast_calls(` | `extract_ast_calls [function]` | `bcaf8341-d7e2-526b-af67-326be6b04220` | 17-103 [crates/gcode/src/index/parser/calls/ast.rs:17-103] | Indexed function `extract_ast_calls` in `crates/gcode/src/index/parser/calls/ast.rs`. [crates/gcode/src/index/parser/calls/ast.rs:17-103] |
| `is_elixir_definition_head_call` | function | `fn is_elixir_definition_head_call(language: &str, call_node: Node<'_>, source: &[u8]) -> bool {` | `is_elixir_definition_head_call [function]` | `586efd45-7dd8-5f7d-ade3-f785c9d9d9c8` | 105-135 [crates/gcode/src/index/parser/calls/ast.rs:105-135] | Indexed function `is_elixir_definition_head_call` in `crates/gcode/src/index/parser/calls/ast.rs`. [crates/gcode/src/index/parser/calls/ast.rs:105-135] |
| `extract_js_calls` | function | `fn extract_js_calls(` | `extract_js_calls [function]` | `425ba4ef-1a13-5762-bac0-07e57d1d2709` | 148-179 [crates/gcode/src/index/parser/calls/ast.rs:148-179] | Indexed function `extract_js_calls` in `crates/gcode/src/index/parser/calls/ast.rs`. [crates/gcode/src/index/parser/calls/ast.rs:148-179] |
| `js_bindings` | function | `fn js_bindings(import_text: &str) -> ImportBindings {` | `js_bindings [function]` | `4560361a-df66-5092-969a-7592746703a4` | 181-193 [crates/gcode/src/index/parser/calls/ast.rs:181-193] | Indexed function `js_bindings` in `crates/gcode/src/index/parser/calls/ast.rs`. [crates/gcode/src/index/parser/calls/ast.rs:181-193] |
| `skips_matches_without_name_capture` | function | `fn skips_matches_without_name_capture() {` | `skips_matches_without_name_capture [function]` | `9e398a6c-c654-5983-a963-06daa7a9169c` | 196-205 [crates/gcode/src/index/parser/calls/ast.rs:196-205] | Indexed function `skips_matches_without_name_capture` in `crates/gcode/src/index/parser/calls/ast.rs`. [crates/gcode/src/index/parser/calls/ast.rs:196-205] |
| `ignores_qualified_keyword_callee_after_split` | function | `fn ignores_qualified_keyword_callee_after_split() {` | `ignores_qualified_keyword_callee_after_split [function]` | `2146e6ac-ac69-5c87-8f97-04c4fb67ed5c` | 208-217 [crates/gcode/src/index/parser/calls/ast.rs:208-217] | Indexed function `ignores_qualified_keyword_callee_after_split` in `crates/gcode/src/index/parser/calls/ast.rs`. [crates/gcode/src/index/parser/calls/ast.rs:208-217] |
| `member_call_uses_qualifier_path_from_call_node` | function | `fn member_call_uses_qualifier_path_from_call_node() {` | `member_call_uses_qualifier_path_from_call_node [function]` | `79b25384-0aab-5efe-b355-3dd11e8de21a` | 220-235 [crates/gcode/src/index/parser/calls/ast.rs:220-235] | Indexed function `member_call_uses_qualifier_path_from_call_node` in `crates/gcode/src/index/parser/calls/ast.rs`. [crates/gcode/src/index/parser/calls/ast.rs:220-235] |
| `bare_detected_syntax_upgrades_to_member_when_qualified_name_is_captured` | function | `fn bare_detected_syntax_upgrades_to_member_when_qualified_name_is_captured() {` | `bare_detected_syntax_upgrades_to_member_when_qualified_name_is_captured [function]` | `aa7ddaad-72e7-5d12-a15e-7b8996db3fe8` | 238-252 [crates/gcode/src/index/parser/calls/ast.rs:238-252] | Indexed function `bare_detected_syntax_upgrades_to_member_when_qualified_name_is_captured` in `crates/gcode/src/index/parser/calls/ast.rs`. [crates/gcode/src/index/parser/calls/ast.rs:238-252] |
