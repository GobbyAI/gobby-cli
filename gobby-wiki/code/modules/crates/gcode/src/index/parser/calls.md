---
title: crates/gcode/src/index/parser/calls
type: code_module
provenance:
- file: crates/gcode/src/index/parser/calls/ast.rs
- file: crates/gcode/src/index/parser/calls/dart_textual.rs
- file: crates/gcode/src/index/parser/calls/objc_ast.rs
- file: crates/gcode/src/index/parser/calls/resolution.rs
- file: crates/gcode/src/index/parser/calls/shadowing.rs
- file: crates/gcode/src/index/parser/calls/text.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser/calls

Parent: [[code/modules/crates/gcode/src/index/parser|crates/gcode/src/index/parser]]

## Overview

The `calls` parser module extracts and resolves call relationships for the indexer. Its Dart textual scanner walks source line spans, skips non-call contexts such as imports, exports, class declarations, enums, and typedefs, filters ignored names, and materializes candidates into `CallRelation` records with optional semantic resolution support (`crates/gcode/src/index/parser/calls/dart_textual.rs:1-100`). Shared text helpers provide byte/UTF-16 positioning, Unicode-aware identifier handling, call-name byte tests, and language-specific ignore lists (`crates/gcode/src/index/parser/calls/text.rs:1-100`).

Resolution code classifies call syntax as bare, member, or other, finds the deepest enclosing symbol by byte range, and resolves same-file callees against callable symbols such as functions, methods, and classes (`crates/gcode/src/index/parser/calls/resolution.rs:1-100`). Shadowing checks prevent external call links when a local binding, parameter, or member root alias would mask the callee before the call site (`crates/gcode/src/index/parser/calls/shadowing.rs:1-100`).

This module collaborates with the wider indexer through model and semantic boundaries: Dart extraction returns `crate::models::CallRelation`, accepts `crate::index::semantic::SemanticCallResolver`, and uses shared `CallExtractionContext`, `CallSite`, and `materialize_call` from the parent calls module (`crates/gcode/src/index/parser/calls/dart_textual.rs:1-12`). Resolution and shadowing both depend on `crate::models::Symbol`, while text parsing depends on `unicode_xid::UnicodeXID` for identifier classification (`crates/gcode/src/index/parser/calls/resolution.rs:1-20`, `crates/gcode/src/index/parser/calls/shadowing.rs:1-18`, `crates/gcode/src/index/parser/calls/text.rs:1-47`).

| Symbol | Kind | Responsibility |
| --- | --- | --- |
| `extract_textual_dart_calls` | function | Scan Dart text and emit `CallRelation` values (`dart_textual.rs:8-16`) |
| `CallSyntaxKind` | enum | Classify calls as `Bare`, `Member`, or `Other` (`resolution.rs:5-10`) |
| `enclosing_symbol` | function | Find the innermost symbol containing a byte offset (`resolution.rs:12-21`) |
| `call_syntax_kind` | function | Derive syntax kind from tree-sitter nodes (`resolution.rs:23-45`) |
| `external_call_is_shadowed` | function | Detect local shadowing before linking external calls (`shadowing.rs:5-22`) |
| `utf16_column_at_byte` | function | Convert byte offsets to UTF-16 columns (`text.rs:20-28`) |
| `is_identifier_start` / `is_identifier_continue` | functions | Unicode-aware identifier classification (`text.rs:47-55`) |
| `should_ignore_call_name` | function | Filter language keywords and special forms (`text.rs:61-100`) |
[crates/gcode/src/index/parser/calls/dart_textual.rs:8-55]
[crates/gcode/src/index/parser/calls/resolution.rs:6-10]
[crates/gcode/src/index/parser/calls/shadowing.rs:6-23]
[crates/gcode/src/index/parser/calls/text.rs:4-20]
[crates/gcode/src/index/parser/calls/ast.rs:17-103]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/index/parser/calls/ast.rs\|crates/gcode/src/index/parser/calls/ast.rs]] | `crates/gcode/src/index/parser/calls/ast.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/dart_textual.rs\|crates/gcode/src/index/parser/calls/dart_textual.rs]] | `crates/gcode/src/index/parser/calls/dart_textual.rs` exposes 21 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/objc_ast.rs\|crates/gcode/src/index/parser/calls/objc_ast.rs]] | `crates/gcode/src/index/parser/calls/objc_ast.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/resolution.rs\|crates/gcode/src/index/parser/calls/resolution.rs]] | `crates/gcode/src/index/parser/calls/resolution.rs` exposes 14 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/shadowing.rs\|crates/gcode/src/index/parser/calls/shadowing.rs]] | `crates/gcode/src/index/parser/calls/shadowing.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/text.rs\|crates/gcode/src/index/parser/calls/text.rs]] | `crates/gcode/src/index/parser/calls/text.rs` exposes 10 indexed API symbols. |

