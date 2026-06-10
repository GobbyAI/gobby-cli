---
title: crates/gcode/src/index/parser/calls/ast.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls/ast.rs
  ranges:
  - 17-96
  - 109-140
  - 142-154
  - 157-166
  - 169-178
  - 181-196
  - 199-213
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser/calls/ast.rs

Module: [[code/modules/crates/gcode/src/index/parser/calls|crates/gcode/src/index/parser/calls]]

## Purpose

`crates/gcode/src/index/parser/calls/ast.rs` exposes 7 indexed API symbols.
[crates/gcode/src/index/parser/calls/ast.rs:17-96]
[crates/gcode/src/index/parser/calls/ast.rs:109-140]
[crates/gcode/src/index/parser/calls/ast.rs:142-154]
[crates/gcode/src/index/parser/calls/ast.rs:157-166]
[crates/gcode/src/index/parser/calls/ast.rs:169-178]
[crates/gcode/src/index/parser/calls/ast.rs:181-196]
[crates/gcode/src/index/parser/calls/ast.rs:199-213]

## API Symbols

- `extract_ast_calls` (function) component `extract_ast_calls [function]` (`01939a5b-e090-5540-8d47-89bb67ced83d`) lines 17-96 [crates/gcode/src/index/parser/calls/ast.rs:17-96]
  - Signature: `pub(super) fn extract_ast_calls(`
  - Purpose: # Summary

Extracts function call relations from a syntax tree by executing a language-specific tree-sitter query to identify, qualify, and semantically resolve callee names. [crates/gcode/src/index/parser/calls/ast.rs:17-96]
- `extract_js_calls` (function) component `extract_js_calls [function]` (`b3483c06-ebea-51c2-af6f-d117e03e0e14`) lines 109-140 [crates/gcode/src/index/parser/calls/ast.rs:109-140]
  - Signature: `fn extract_js_calls(`
  - Purpose: Parses JavaScript source code into an abstract syntax tree using Tree-sitter and extracts function call relations matching the provided query pattern. [crates/gcode/src/index/parser/calls/ast.rs:109-140]
- `js_bindings` (function) component `js_bindings [function]` (`e07e10e4-1d48-574d-8dc2-afdc044556eb`) lines 142-154 [crates/gcode/src/index/parser/calls/ast.rs:142-154]
  - Signature: `fn js_bindings(import_text: &str) -> ImportBindings {`
  - Purpose: Parses a JavaScript import statement string and returns the extracted `ImportBindings`. [crates/gcode/src/index/parser/calls/ast.rs:142-154]
- `skips_matches_without_name_capture` (function) component `skips_matches_without_name_capture [function]` (`4285af00-ea06-5e6e-9bb4-a124b63b67fa`) lines 157-166 [crates/gcode/src/index/parser/calls/ast.rs:157-166]
  - Signature: `fn skips_matches_without_name_capture() {`
  - Purpose: This unit test verifies that `extract_js_calls` ignores matches from tree-sitter query patterns that lack the required named capture group for function names. [crates/gcode/src/index/parser/calls/ast.rs:157-166]
- `ignores_qualified_keyword_callee_after_split` (function) component `ignores_qualified_keyword_callee_after_split [function]` (`70058089-d832-5fb3-821e-00c47d79f8d2`) lines 169-178 [crates/gcode/src/index/parser/calls/ast.rs:169-178]
  - Signature: `fn ignores_qualified_keyword_callee_after_split() {`
  - Purpose: This test verifies that `extract_js_calls` ignores function calls where the callee is a reserved keyword accessed via member expression (e.g., `obj.await()`). [crates/gcode/src/index/parser/calls/ast.rs:169-178]
- `member_call_uses_qualifier_path_from_call_node` (function) component `member_call_uses_qualifier_path_from_call_node [function]` (`4369cc1b-3d2f-5e06-b490-edb9cdd35100`) lines 181-196 [crates/gcode/src/index/parser/calls/ast.rs:181-196]
  - Signature: `fn member_call_uses_qualifier_path_from_call_node() {`
  - Purpose: This test verifies that member expression function calls are correctly extracted with accurate callee identifiers, line numbers, and external module qualifier resolution. [crates/gcode/src/index/parser/calls/ast.rs:181-196]
- `bare_detected_syntax_upgrades_to_member_when_qualified_name_is_captured` (function) component `bare_detected_syntax_upgrades_to_member_when_qualified_name_is_captured [function]` (`a85b31c9-4048-5e10-85e0-98f46229b40d`) lines 199-213 [crates/gcode/src/index/parser/calls/ast.rs:199-213]
  - Signature: `fn bare_detected_syntax_upgrades_to_member_when_qualified_name_is_captured() {`
  - Purpose: Tests that member expression calls on imported qualified names (e.g., `fs.readFile()`) are correctly identified as external module calls through tree-sitter pattern matching and binding resolution. [crates/gcode/src/index/parser/calls/ast.rs:199-213]

