---
title: crates/gcode/src/index/parser.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser.rs
  ranges:
  - 29-134
  - 136-235
  - 237-264
  - 266-318
  - 320-326
  - 328-389
  - 391-398
  - 400-443
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/parser.rs:29-134](crates/gcode/src/index/parser.rs#L29-L134), [crates/gcode/src/index/parser.rs:136-235](crates/gcode/src/index/parser.rs#L136-L235), [crates/gcode/src/index/parser.rs:237-264](crates/gcode/src/index/parser.rs#L237-L264), [crates/gcode/src/index/parser.rs:266-318](crates/gcode/src/index/parser.rs#L266-L318), [crates/gcode/src/index/parser.rs:320-326](crates/gcode/src/index/parser.rs#L320-L326), [crates/gcode/src/index/parser.rs:328-389](crates/gcode/src/index/parser.rs#L328-L389), [crates/gcode/src/index/parser.rs:391-398](crates/gcode/src/index/parser.rs#L391-L398), [crates/gcode/src/index/parser.rs:400-443](crates/gcode/src/index/parser.rs#L400-L443)

</details>

# crates/gcode/src/index/parser.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

Tree-sitter-based indexing for source files: it validates a candidate path, detects the language, parses the file, and builds a `ParseResult` with extracted symbols, imports, docstrings, and calls, optionally enriching call extraction with a semantic resolver. The helper functions break that work into stages: `extract_symbols` walks the AST to collect symbols, `link_parents` and `collapse_rust_impl_symbols` normalize symbol hierarchy for Rust, `extract_docstring` and `strip_quotes` attach cleaned documentation text, and `extract_imports` gathers import data for later resolution.
[crates/gcode/src/index/parser.rs:29-134]
[crates/gcode/src/index/parser.rs:136-235]
[crates/gcode/src/index/parser.rs:237-264]
[crates/gcode/src/index/parser.rs:266-318]
[crates/gcode/src/index/parser.rs:320-326]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `parse_file_with_semantic` | function | `pub(crate) fn parse_file_with_semantic(` | `parse_file_with_semantic [function]` | `c8ba7159-8e56-54fa-985a-1821e9d8d076` | 29-134 [crates/gcode/src/index/parser.rs:29-134] | Indexed function `parse_file_with_semantic` in `crates/gcode/src/index/parser.rs`. [crates/gcode/src/index/parser.rs:29-134] |
| `extract_symbols` | function | `fn extract_symbols(` | `extract_symbols [function]` | `4cd06356-ca6d-516f-926c-f21ab3dc22a4` | 136-235 [crates/gcode/src/index/parser.rs:136-235] | Indexed function `extract_symbols` in `crates/gcode/src/index/parser.rs`. [crates/gcode/src/index/parser.rs:136-235] |
| `link_parents` | function | `fn link_parents(symbols: &mut [Symbol]) {` | `link_parents [function]` | `e18c280e-b5b7-5b95-bc6d-6215ebfaec8c` | 237-264 [crates/gcode/src/index/parser.rs:237-264] | Indexed function `link_parents` in `crates/gcode/src/index/parser.rs`. [crates/gcode/src/index/parser.rs:237-264] |
| `collapse_rust_impl_symbols` | function | `fn collapse_rust_impl_symbols(symbols: &mut Vec<Symbol>) {` | `collapse_rust_impl_symbols [function]` | `0326b48a-4404-5d07-a6f9-e92bef95ec43` | 266-318 [crates/gcode/src/index/parser.rs:266-318] | Indexed function `collapse_rust_impl_symbols` in `crates/gcode/src/index/parser.rs`. [crates/gcode/src/index/parser.rs:266-318] |
| `is_rust_impl_symbol` | function | `fn is_rust_impl_symbol(symbol: &Symbol) -> bool {` | `is_rust_impl_symbol [function]` | `4c284c6c-18ce-5bdc-9761-811baac5e178` | 320-326 [crates/gcode/src/index/parser.rs:320-326] | Indexed function `is_rust_impl_symbol` in `crates/gcode/src/index/parser.rs`. [crates/gcode/src/index/parser.rs:320-326] |
| `extract_docstring` | function | `fn extract_docstring(node: &tree_sitter::Node, source: &[u8], language: &str) -> Option<String> {` | `extract_docstring [function]` | `13353f9b-16d7-5c56-9d86-979c94099192` | 328-389 [crates/gcode/src/index/parser.rs:328-389] | Indexed function `extract_docstring` in `crates/gcode/src/index/parser.rs`. [crates/gcode/src/index/parser.rs:328-389] |
| `strip_quotes` | function | `fn strip_quotes(s: &str) -> &str {` | `strip_quotes [function]` | `f35bb74f-79d8-5acb-a4f2-0404216c0404` | 391-398 [crates/gcode/src/index/parser.rs:391-398] | Indexed function `strip_quotes` in `crates/gcode/src/index/parser.rs`. [crates/gcode/src/index/parser.rs:391-398] |
| `extract_imports` | function | `fn extract_imports(` | `extract_imports [function]` | `c239baa3-e2f6-5fd8-9b64-99a2258ae9b3` | 400-443 [crates/gcode/src/index/parser.rs:400-443] | Indexed function `extract_imports` in `crates/gcode/src/index/parser.rs`. [crates/gcode/src/index/parser.rs:400-443] |
