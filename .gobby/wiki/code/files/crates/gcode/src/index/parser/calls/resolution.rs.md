---
title: crates/gcode/src/index/parser/calls/resolution.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls/resolution.rs
  ranges:
  - 6-10
  - 17-21
  - 23-46
  - 48-61
  - 63-65
  - 67-90
  - 92-105
  - 107-115
  - 117-155
  - 157-162
  - 164-175
  - 177-182
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser/calls/resolution.rs

Module: [[code/modules/crates/gcode/src/index/parser/calls|crates/gcode/src/index/parser/calls]]

## Purpose

`crates/gcode/src/index/parser/calls/resolution.rs` exposes 12 indexed API symbols.
[crates/gcode/src/index/parser/calls/resolution.rs:6-10]
[crates/gcode/src/index/parser/calls/resolution.rs:17-21]
[crates/gcode/src/index/parser/calls/resolution.rs:23-46]
[crates/gcode/src/index/parser/calls/resolution.rs:48-61]
[crates/gcode/src/index/parser/calls/resolution.rs:63-65]

## API Symbols

- `CallSyntaxKind` (type) component `CallSyntaxKind [type]` (`05532d20-0797-5f98-b19e-15a7f431a888`) lines 6-10 [crates/gcode/src/index/parser/calls/resolution.rs:6-10]
  - Signature: `pub(super) enum CallSyntaxKind {`
  - Purpose: Indexed type `CallSyntaxKind` in `crates/gcode/src/index/parser/calls/resolution.rs`. [crates/gcode/src/index/parser/calls/resolution.rs:6-10]
- `enclosing_symbol` (function) component `enclosing_symbol [function]` (`9c30b856-c855-5c26-aa73-bdd164c437a1`) lines 17-21 [crates/gcode/src/index/parser/calls/resolution.rs:17-21]
  - Signature: `pub(super) fn enclosing_symbol(symbols: &[Symbol], byte_offset: usize) -> Option<&Symbol> {`
  - Purpose: Finds the rightmost symbol whose byte range encloses the given offset, returning a reference to that symbol or None if no enclosing symbol exists. [crates/gcode/src/index/parser/calls/resolution.rs:17-21]
- `call_syntax_kind` (function) component `call_syntax_kind [function]` (`53222c78-5e39-5e45-a035-c9b48740a4d6`) lines 23-46 [crates/gcode/src/index/parser/calls/resolution.rs:23-46]
  - Signature: `pub(super) fn call_syntax_kind(`
  - Purpose: Classifies a name node's call syntax as bare (direct), member (method), or other by traversing its ancestor chain to detect member access patterns before reaching the enclosing call node. [crates/gcode/src/index/parser/calls/resolution.rs:23-46]
- `is_memberish_kind` (function) component `is_memberish_kind [function]` (`6eca919c-11ec-5425-a720-90a47399bf04`) lines 48-61 [crates/gcode/src/index/parser/calls/resolution.rs:48-61]
  - Signature: `fn is_memberish_kind(kind: &str) -> bool {`
  - Purpose: Returns `true` if the given syntax kind string represents a member-related construct, such as member access, field expression, selector expression, or member call expression. [crates/gcode/src/index/parser/calls/resolution.rs:48-61]
- `is_callable_kind` (function) component `is_callable_kind [function]` (`28c9ff78-6b41-50f6-a96d-e43acc99fb8f`) lines 63-65 [crates/gcode/src/index/parser/calls/resolution.rs:63-65]
  - Signature: `fn is_callable_kind(kind: &str) -> bool {`
  - Purpose: Returns `true` if the input string is either "function" or "method", otherwise returns `false`. [crates/gcode/src/index/parser/calls/resolution.rs:63-65]
- `resolve_same_file_callee` (function) component `resolve_same_file_callee [function]` (`5124f9d4-2259-5d16-a479-3131f6cb9b16`) lines 67-90 [crates/gcode/src/index/parser/calls/resolution.rs:67-90]
  - Signature: `fn resolve_same_file_callee(`
  - Purpose: Resolves a same-file callee by finding a unique symbol ID matching the callee name, filtered by call syntax type (bare callable, parent-scoped method, or none). [crates/gcode/src/index/parser/calls/resolution.rs:67-90]
- `resolve_same_file_callee_for_language` (function) component `resolve_same_file_callee_for_language [function]` (`719a45ba-540c-509e-974f-23109a634cfb`) lines 92-105 [crates/gcode/src/index/parser/calls/resolution.rs:92-105]
  - Signature: `pub(super) fn resolve_same_file_callee_for_language(`
  - Purpose: Resolves same-file callee references for a given language, filtering out Ruby bare-call syntax to prevent false positive edges from dynamic dispatch. [crates/gcode/src/index/parser/calls/resolution.rs:92-105]
- `unique_symbol_id` (function) component `unique_symbol_id [function]` (`9d0c7948-4a09-5532-a9a1-d9c3c4bcb0dd`) lines 107-115 [crates/gcode/src/index/parser/calls/resolution.rs:107-115]
  - Signature: `fn unique_symbol_id<'a>(symbols: impl Iterator<Item = &'a Symbol>) -> Option<String> {`
  - Purpose: Returns the ID of the first symbol if the iterator contains exactly one element, otherwise returns `None`. [crates/gcode/src/index/parser/calls/resolution.rs:107-115]
- `member_qualifier_path` (function) component `member_qualifier_path [function]` (`720986cd-dadd-56a2-ad70-5fdc2a966923`) lines 117-155 [crates/gcode/src/index/parser/calls/resolution.rs:117-155]
  - Signature: `pub(super) fn member_qualifier_path(`
  - Purpose: Extracts and normalizes a qualified namespace/member path from source code between two tree-sitter nodes, filtering out variable dereferences and arrow operators while handling both absolute and relative namespaces. [crates/gcode/src/index/parser/calls/resolution.rs:117-155]
- `call_qualifier_path` (function) component `call_qualifier_path [function]` (`88a242ea-d394-5089-b65f-fcb57556954f`) lines 157-162 [crates/gcode/src/index/parser/calls/resolution.rs:157-162]
  - Signature: `pub(in crate::index::parser) fn call_qualifier_path(`
  - Purpose: Returns an optional qualifier string, deferring to a lazily-evaluated member-derived qualifier only if the name-based qualifier is `None`. [crates/gcode/src/index/parser/calls/resolution.rs:157-162]
- `split_qualified_callee` (function) component `split_qualified_callee [function]` (`1ad174c0-0cae-569e-a964-41e540ed90c0`) lines 164-175 [crates/gcode/src/index/parser/calls/resolution.rs:164-175]
  - Signature: `pub(in crate::index::parser) fn split_qualified_callee(raw: &str) -> (String, Option<String>) {`
  - Purpose: Splits a qualified identifier on the rightmost occurrence of `::`, `\`, or `.`, returning the unqualified name and optional qualifier prefix as a tuple. [crates/gcode/src/index/parser/calls/resolution.rs:164-175]
- `qualifier_root_alias` (function) component `qualifier_root_alias [function]` (`de130dfa-ced4-5096-aa07-d865ac254172`) lines 177-182 [crates/gcode/src/index/parser/calls/resolution.rs:177-182]
  - Signature: `pub(super) fn qualifier_root_alias(qualifier: &str) -> Option<&str> {`
  - Purpose: Extracts the first non-empty component of a qualified identifier by removing leading backslashes and splitting on `.`, `:`, or `\\` delimiters. [crates/gcode/src/index/parser/calls/resolution.rs:177-182]

