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

## Module: `crates/gcode/src/index/parser/calls`

This module is responsible for discovering, classifying, and materializing call-site relations from source files during the gcode indexing pass. It operates at two distinct levels of fidelity: an AST-guided path (backed by tree-sitter) used for most languages via `ast.rs` and `objc_ast.rs`, and a line-oriented textual fallback path implemented in `dart_textual.rs` for Dart. Across both paths the module emits `CallRelation` model values that are consumed by upstream indexing stages, optionally enriched by a `SemanticCallResolver` injected at call time (`dart_textual.rs:1-10`).

The central classification concept is the `CallSyntaxKind` discriminant defined in `resolution.rs:9-12`. Every candidate call site is tagged as `Bare` (a direct identifier call), `Member` (a method or field access chain), or `Other` (any other syntactic form). The AST-based path determines the kind by walking tree-sitter node ancestry through a set of recognised "memberish" node kinds — `member_expression`, `selector_expression`, `navigation_expression`, `scoped_identifier`, and others — until the enclosing call node is reached (`resolution.rs:24-54`). The textual Dart path uses `.` as the member separator and applies its own heuristics to skip import/export/class/enum declarations and other non-call contexts (`dart_textual.rs:18-49`).

Before a candidate call is accepted, the `shadowing` submodule checks whether the callee name or its root alias is already bound as a local variable or parameter within the enclosing `Symbol`'s byte range, using byte-precise prefix scanning (`shadowing.rs:3-23`). Block comments are stripped from the prefix before the scan to avoid false matches inside comment text (`shadowing.rs:34-57`). The `text.rs` utility layer underpins both the shadowing and extraction passes: it provides Unicode-XID identifier boundary predicates, a UTF-16 column calculator needed for LSP-compatible position reporting, and language-aware call-name ignore lists aligned with Dart, Elixir, and Kotlin keyword specifications (`text.rs:55-100`).

Externally, this module imports `crate::models::{Symbol, CallRelation}` for its data types and `crate::index::semantic::SemanticCallResolver` for optional semantic enrichment. The parent parser module (`crates/gcode/src/index/parser`) drives extraction by supplying a `CallExtractionContext` and a `materialize_call` helper re-exported through `super`. Tree-sitter `Node` references flow into `resolution.rs` from the AST parsing layer (`resolution.rs:24-26`).

### Key Public/Internal Types

| Symbol | File | Role |
|---|---|---|
| `CallSyntaxKind` | `resolution.rs:9` | Discriminates `Bare` / `Member` / `Other` call forms |
| `enclosing_symbol` | `resolution.rs:17` | Finds the innermost `Symbol` containing a byte offset |
| `call_syntax_kind` | `resolution.rs:23` | Classifies a call node via tree-sitter ancestry walk |
| `external_call_is_shadowed` | `shadowing.rs:5` | Returns `true` when a local binding hides the callee |
| `extract_textual_dart_calls` | `dart_textual.rs:8` | Line-scan call extractor for Dart source |
| `utf16_column_at_byte` | `text.rs:22` | Computes LSP-compatible UTF-16 column from a byte offset |
| `is_textual_call_name_byte` | `text.rs:66` | Byte-level predicate for valid call-name characters |
| `should_ignore_call_name` | `text.rs:69` | Filters language keywords from candidate callee names |
| `trim_identifier_token` | `text.rs:54` | Strips non-identifier boundary characters from a token |

### Memberish Node Kinds Recognised by `call_syntax_kind`

| Tree-sitter Kind | Language context |
|---|---|
| `attribute` | General attribute syntax |
| `member_expression` | JS / TS |
| `selector_expression` | Go |
| `field_expression` | Rust / C++ |
| `member_access_expression` | C# / Swift |
| `member_call_expression` | Swift |
| `navigation_expression` | Kotlin |
| `scoped_identifier` | Rust / C++ |
| `scoped_call_expression` | Rust |
| `dot` | Generic dot separator |

(`resolution.rs:45-57`)
[crates/gcode/src/index/parser/calls/dart_textual.rs:8-55]
[crates/gcode/src/index/parser/calls/objc_ast.rs:16-119]
[crates/gcode/src/index/parser/calls/ast.rs:17-103]
[crates/gcode/src/index/parser/calls/resolution.rs:6-10]
[crates/gcode/src/index/parser/calls/shadowing.rs:6-23]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/index/parser/calls/ast.rs\|crates/gcode/src/index/parser/calls/ast.rs]] | `crates/gcode/src/index/parser/calls/ast.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/dart_textual.rs\|crates/gcode/src/index/parser/calls/dart_textual.rs]] | `crates/gcode/src/index/parser/calls/dart_textual.rs` exposes 21 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/objc_ast.rs\|crates/gcode/src/index/parser/calls/objc_ast.rs]] | `crates/gcode/src/index/parser/calls/objc_ast.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/resolution.rs\|crates/gcode/src/index/parser/calls/resolution.rs]] | `crates/gcode/src/index/parser/calls/resolution.rs` exposes 14 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/shadowing.rs\|crates/gcode/src/index/parser/calls/shadowing.rs]] | `crates/gcode/src/index/parser/calls/shadowing.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/text.rs\|crates/gcode/src/index/parser/calls/text.rs]] | `crates/gcode/src/index/parser/calls/text.rs` exposes 10 indexed API symbols. |

