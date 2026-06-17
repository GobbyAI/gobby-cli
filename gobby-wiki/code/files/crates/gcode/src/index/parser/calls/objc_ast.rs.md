---
title: crates/gcode/src/index/parser/calls/objc_ast.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls/objc_ast.rs
  ranges:
  - 16-119
  - 121-140
  - 142-150
  - 152-169
  - 171-181
  - 183-189
  - 191-197
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/parser/calls/objc_ast.rs:16-119](crates/gcode/src/index/parser/calls/objc_ast.rs#L16-L119), [crates/gcode/src/index/parser/calls/objc_ast.rs:121-140](crates/gcode/src/index/parser/calls/objc_ast.rs#L121-L140), [crates/gcode/src/index/parser/calls/objc_ast.rs:142-150](crates/gcode/src/index/parser/calls/objc_ast.rs#L142-L150), [crates/gcode/src/index/parser/calls/objc_ast.rs:152-169](crates/gcode/src/index/parser/calls/objc_ast.rs#L152-L169), [crates/gcode/src/index/parser/calls/objc_ast.rs:171-181](crates/gcode/src/index/parser/calls/objc_ast.rs#L171-L181), [crates/gcode/src/index/parser/calls/objc_ast.rs:183-189](crates/gcode/src/index/parser/calls/objc_ast.rs#L183-L189), [crates/gcode/src/index/parser/calls/objc_ast.rs:191-197](crates/gcode/src/index/parser/calls/objc_ast.rs#L191-L197)

</details>

# crates/gcode/src/index/parser/calls/objc_ast.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

Extracts Objective-C call relations from a parsed tree-sitter AST by running the language’s call query, collecting `name`/`call`/`receiver` captures, and turning matched call sites into `CallRelation` records, optionally using a semantic resolver. The helper functions support that extraction by determining message receiver qualifiers, inferring a variable’s Objective-C type from surrounding text or lines, and checking identifier and type-identifier boundaries so call names and receivers are recognized correctly.
[crates/gcode/src/index/parser/calls/objc_ast.rs:16-119]
[crates/gcode/src/index/parser/calls/objc_ast.rs:121-140]
[crates/gcode/src/index/parser/calls/objc_ast.rs:142-150]
[crates/gcode/src/index/parser/calls/objc_ast.rs:152-169]
[crates/gcode/src/index/parser/calls/objc_ast.rs:171-181]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `extract_objc_calls` | function | `pub(super) fn extract_objc_calls(` | `extract_objc_calls [function]` | `bfd38d24-7867-52b9-9937-c35acd474a4d` | 16-119 [crates/gcode/src/index/parser/calls/objc_ast.rs:16-119] | Indexed function `extract_objc_calls` in `crates/gcode/src/index/parser/calls/objc_ast.rs`. [crates/gcode/src/index/parser/calls/objc_ast.rs:16-119] |
| `objc_message_receiver_qualifier` | function | `fn objc_message_receiver_qualifier(` | `objc_message_receiver_qualifier [function]` | `67ee4404-02e3-5c9a-aa55-0afb3133d10e` | 121-140 [crates/gcode/src/index/parser/calls/objc_ast.rs:121-140] | Indexed function `objc_message_receiver_qualifier` in `crates/gcode/src/index/parser/calls/objc_ast.rs`. [crates/gcode/src/index/parser/calls/objc_ast.rs:121-140] |
| `objc_variable_type_before` | function | `fn objc_variable_type_before(source: &[u8], call_start: usize, variable: &str) -> Option<String> {` | `objc_variable_type_before [function]` | `85b0a29d-b63e-50f4-ab41-458f8661945e` | 142-150 [crates/gcode/src/index/parser/calls/objc_ast.rs:142-150] | Indexed function `objc_variable_type_before` in `crates/gcode/src/index/parser/calls/objc_ast.rs`. [crates/gcode/src/index/parser/calls/objc_ast.rs:142-150] |
| `objc_variable_type_from_line` | function | `fn objc_variable_type_from_line(line: &str, variable: &str) -> Option<String> {` | `objc_variable_type_from_line [function]` | `48c54247-5677-5c3d-9359-2637cc182fd9` | 152-169 [crates/gcode/src/index/parser/calls/objc_ast.rs:152-169] | Indexed function `objc_variable_type_from_line` in `crates/gcode/src/index/parser/calls/objc_ast.rs`. [crates/gcode/src/index/parser/calls/objc_ast.rs:152-169] |
| `is_identifier_boundary` | function | `fn is_identifier_boundary(text: &str, start: usize, len: usize) -> bool {` | `is_identifier_boundary [function]` | `1f92b56e-539a-53bb-8cbc-db53d0bc474a` | 171-181 [crates/gcode/src/index/parser/calls/objc_ast.rs:171-181] | Indexed function `is_identifier_boundary` in `crates/gcode/src/index/parser/calls/objc_ast.rs`. [crates/gcode/src/index/parser/calls/objc_ast.rs:171-181] |
| `is_objc_type_identifier` | function | `fn is_objc_type_identifier(name: &str) -> bool {` | `is_objc_type_identifier [function]` | `a61fb040-84db-50dc-93b0-0f2c69b8a936` | 183-189 [crates/gcode/src/index/parser/calls/objc_ast.rs:183-189] | Indexed function `is_objc_type_identifier` in `crates/gcode/src/index/parser/calls/objc_ast.rs`. [crates/gcode/src/index/parser/calls/objc_ast.rs:183-189] |
| `is_objc_identifier` | function | `fn is_objc_identifier(name: &str) -> bool {` | `is_objc_identifier [function]` | `d302155e-627e-5b31-bf5d-2751242abbd2` | 191-197 [crates/gcode/src/index/parser/calls/objc_ast.rs:191-197] | Indexed function `is_objc_identifier` in `crates/gcode/src/index/parser/calls/objc_ast.rs`. [crates/gcode/src/index/parser/calls/objc_ast.rs:191-197] |
