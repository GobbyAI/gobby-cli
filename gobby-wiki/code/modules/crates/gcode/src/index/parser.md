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

The `crates/gcode/src/index/parser` module focuses on extracting call relationships for the gcode indexer. Its `calls` child module owns call parsing and resolution, producing `CallRelation` records from source, symbols, import context, and optional semantic resolution inputs (`crates/gcode/src/index/parser/calls.rs:1-100`).

The main flow is routed through `extract_calls`: Dart uses a textual scanner, Objective-C uses an Objective-C AST extractor, and all other languages fall back to the generic AST extractor (`crates/gcode/src/index/parser/calls.rs:1-100`). Dart’s scanner explicitly skips non-call contexts such as imports, exports, class declarations, enums, and typedefs, then resolves candidates into call relations; shared text helpers handle byte/UTF-16 positions, Unicode identifiers, call-name checks, and ignore lists (`crates/gcode/src/index/parser/calls/dart_textual.rs:1-100`, `crates/gcode/src/index/parser/calls/text.rs:1-100`).

This module collaborates with the wider indexer through imports from import resolution, language specs, semantic call resolution, and model types (`crates/gcode/src/index/parser/calls.rs:1-100`). Internally, call materialization finds the enclosing symbol, assigns the caller symbol id, and handles language-specific details such as Lua `require` qualifier recovery before producing a `CallRelation` (`crates/gcode/src/index/parser/calls.rs:1-100`). Parser test coverage is organized by language and behavior-focused submodules such as `objc`, `lua`, `semantic`, and `resolution` (`crates/gcode/src/index/parser/tests.rs:1-12`).

| Symbol | Kind | Role |
| --- | --- | --- |
| `CallExtractionContext` | `pub(super)` struct | Carries language, tree-sitter language, paths, symbols, import context, and bindings for extraction (`crates/gcode/src/index/parser/calls.rs:1-100`). |
| `extract_calls` | `pub(super)` function | Dispatches call extraction by language and returns `Vec<CallRelation>` (`crates/gcode/src/index/parser/calls.rs:1-100`). |
| `call_qualifier_path` | test re-export | Resolution helper exposed to tests (`crates/gcode/src/index/parser/calls.rs:1-100`). |
| `split_qualified_callee` | test re-export | Resolution helper exposed to tests (`crates/gcode/src/index/parser/calls.rs:1-100`). |
| `line_terminator_len` | test re-export | Text helper exposed to tests (`crates/gcode/src/index/parser/calls.rs:1-100`). |

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/index/parser/calls\|crates/gcode/src/index/parser/calls]] | The `calls` parser module extracts and resolves call relationships for the indexer. Its Dart textual scanner walks source line spans, skips non-call contexts such as imports, exports, class declarations, enums, and typedefs, filters ignored names, and materializes candidates into `CallRelation` records with optional semantic resolution support (`crates/gcode/src/index/parser/calls/dart_textual.rs:1-100`). Shared text helpers provide byte/UTF-16 positioning, Unicode-aware identifier handling, call-name byte tests, and language-specific ignore lists… |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/index/parser/calls.rs\|crates/gcode/src/index/parser/calls.rs]] | `crates/gcode/src/index/parser/calls.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/tests.rs\|crates/gcode/src/index/parser/tests.rs]] | `crates/gcode/src/index/parser/tests.rs` has no indexed API symbols. |

