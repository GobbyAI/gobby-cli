---
title: crates/gcode/src/index/parser
type: code_module
provenance:
- file: crates/gcode/src/index/parser/calls.rs
- file: crates/gcode/src/index/parser/calls/ast.rs
- file: crates/gcode/src/index/parser/calls/dart_textual.rs
- file: crates/gcode/src/index/parser/calls/objc_ast.rs
- file: crates/gcode/src/index/parser/calls/resolution.rs
- file: crates/gcode/src/index/parser/calls/shadowing.rs
- file: crates/gcode/src/index/parser/calls/text.rs
- file: crates/gcode/src/index/parser/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser

Parent: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

## Module: `crates/gcode/src/index/parser`

This module is the call-extraction layer of the gcode indexing pipeline. Its central responsibility is walking a parsed syntax tree (or raw source text, for special-case languages) and producing a flat list of `CallRelation` values that record which symbol invokes which other symbol at a given source location. The module owns the language-dispatch logic: Dart is handled via a bespoke textual pass, Objective-C through a dedicated AST visitor, and all other languages through the generic `ast` sub-module — each specialisation living in a named sub-module under `calls` (`ast`, `dart_textual`, `objc_ast`, `resolution`, `shadowing`, `text`) calls.rs:11–17.

The public entry-point is `extract_calls`, which accepts a Tree-sitter parse tree, raw source bytes, a `LanguageSpec`, a `CallExtractionContext`, and an optional `SemanticCallResolver`. After dispatching to the correct language backend it calls the private `materialize_call` helper to resolve each raw `CallSite` into a typed `CallRelation` — looking up the enclosing `Symbol` by byte offset, handling Lua's `require`-based qualifier path as a special case, and delegating cross-file name resolution to `ImportBindings` and `ImportResolutionContext` calls.rs:47–80.

### Public / package-visible API

| Symbol | Kind | Notes |
|---|---|---|
| `CallExtractionContext<'a>` | struct | Bundles language id, Tree-sitter language, relative path, symbol slice, import context/bindings, and file/root paths for one extraction run calls.rs:24–33 |
| `extract_calls(…)` | fn | Top-level entry; dispatches to `dart_textual`, `objc_ast`, or `ast` backends calls.rs:43–57 |
| `call_qualifier_path` | fn (test re-export) | Re-exported from `resolution` for unit tests calls.rs:20 |
| `split_qualified_callee` | fn (test re-export) | Re-exported from `resolution` for unit tests calls.rs:21 |
| `line_terminator_len` | fn (test re-export) | Re-exported from `text` for unit tests calls.rs:23 |

### Collaboration points

`CallExtractionContext` holds references to types from several sibling modules: `ImportBindings` and `import_resolution` supply import-aware name binding calls.rs:3–4; `languages::LanguageSpec` carries grammar metadata calls.rs:5; `SemanticCallResolver` / `SemanticCallTarget` / `SemanticCallRequest` drive optional semantic-layer resolution calls.rs:6–9; and `CallRelation` / `Symbol` are the output and lookup types from `crate::models` calls.rs:8. The `tests.rs` file gathers integration test sub-modules spanning bash, Go, Rust, Java, C#, Kotlin, Swift, Lua, Objective-C, PHP, Ruby, Dart, Elixir, Python, JavaScript, TypeScript, Scala, and a cross-cutting semantic suite tests.rs:1–11, giving broad language coverage to the dispatch logic in `extract_calls`.
[crates/gcode/src/index/parser/calls/dart_textual.rs:8-55]
[crates/gcode/src/index/parser/calls/objc_ast.rs:16-119]
[crates/gcode/src/index/parser/calls/ast.rs:17-103]
[crates/gcode/src/index/parser/calls/resolution.rs:6-10]
[crates/gcode/src/index/parser/calls/shadowing.rs:6-23]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/index/parser/calls\|crates/gcode/src/index/parser/calls]] | ## Module: `crates/gcode/src/index/parser/calls` |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/index/parser/calls.rs\|crates/gcode/src/index/parser/calls.rs]] | `crates/gcode/src/index/parser/calls.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/tests.rs\|crates/gcode/src/index/parser/tests.rs]] | `crates/gcode/src/index/parser/tests.rs` has no indexed API symbols. |

