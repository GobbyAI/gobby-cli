---
title: crates/gcode/src/index/parser/calls.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls.rs
  ranges:
  - 23-32
  - 35-42
  - 44-55
  - 57-132
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser/calls.rs

Module: [[code/modules/crates/gcode/src/index/parser|crates/gcode/src/index/parser]]

## Purpose

`crates/gcode/src/index/parser/calls.rs` exposes 4 indexed API symbols.
[crates/gcode/src/index/parser/calls.rs:23-32]
[crates/gcode/src/index/parser/calls.rs:35-42]
[crates/gcode/src/index/parser/calls.rs:44-55]
[crates/gcode/src/index/parser/calls.rs:57-132]

## API Symbols

- `CallExtractionContext` (class) component `CallExtractionContext [class]` (`3948f226-4674-5fc9-ab77-faa8cbcded2e`) lines 23-32 [crates/gcode/src/index/parser/calls.rs:23-32]
  - Signature: `pub(super) struct CallExtractionContext<'a> {`
  - Purpose: A generic context struct containing borrowed references to a tree-sitter language parser, file paths, symbols, and import resolution bindings required for extracting function call information from source code. [crates/gcode/src/index/parser/calls.rs:23-32]
- `CallSite` (class) component `CallSite [class]` (`52986442-3c6c-5b74-8b49-4b78638db497`) lines 35-42 [crates/gcode/src/index/parser/calls.rs:35-42]
  - Signature: `struct CallSite {`
  - Purpose: A struct that records metadata for a function call site, including the callee name, optional qualifier path, byte offsets within source, line number, and the syntactic form of the call. [crates/gcode/src/index/parser/calls.rs:35-42]
- `extract_calls` (function) component `extract_calls [function]` (`e903b8d9-6b22-5ad3-a5aa-330b94923a9e`) lines 44-55 [crates/gcode/src/index/parser/calls.rs:44-55]
  - Signature: `pub(super) fn extract_calls(`
  - Purpose: Extracts call relations from source code by dispatching to either a Dart-specific textual analyzer or a language-agnostic AST-based analyzer. [crates/gcode/src/index/parser/calls.rs:44-55]
- `materialize_call` (function) component `materialize_call [function]` (`0d374fc6-9cf4-539f-9c71-7ad4d398aa09`) lines 57-132 [crates/gcode/src/index/parser/calls.rs:57-132]
  - Signature: `fn materialize_call(`
  - Purpose: Resolves a function call's target through hierarchical strategies—local scope lookup, external import resolution (with shadowing detection), and semantic analysis as fallback—returning the materialized CallRelation. [crates/gcode/src/index/parser/calls.rs:57-132]

