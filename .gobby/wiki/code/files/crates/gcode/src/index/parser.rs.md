---
title: crates/gcode/src/index/parser.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser.rs
  ranges:
  - 31-135
  - 137-236
  - 238-263
  - 265-326
  - 328-335
  - 337-380
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

`crates/gcode/src/index/parser.rs` exposes 6 indexed API symbols.
[crates/gcode/src/index/parser.rs:31-135]
[crates/gcode/src/index/parser.rs:137-236]
[crates/gcode/src/index/parser.rs:238-263]
[crates/gcode/src/index/parser.rs:265-326]
[crates/gcode/src/index/parser.rs:328-335]

## API Symbols

- `parse_file_with_semantic` (function) component `parse_file_with_semantic [function]` (`1e272241-b68f-5b19-9dcf-fe9d75387827`) lines 31-135 [crates/gcode/src/index/parser.rs:31-135]
  - Signature: `pub(crate) fn parse_file_with_semantic(`
  - Purpose: Securely parses a validated source file using language detection and Tree-sitter to extract semantic symbols with AST analysis. [crates/gcode/src/index/parser.rs:31-135]
- `extract_symbols` (function) component `extract_symbols [function]` (`33397c78-993c-5c89-80c9-9e3c93b7960c`) lines 137-236 [crates/gcode/src/index/parser.rs:137-236]
  - Signature: `fn extract_symbols(`
  - Purpose: Executes a language-specific tree-sitter query on a syntax tree to extract symbol definitions with their names, kinds, and source locations. [crates/gcode/src/index/parser.rs:137-236]
- `link_parents` (function) component `link_parents [function]` (`e377f306-1706-5a6b-83c8-2dd54e55b132`) lines 238-263 [crates/gcode/src/index/parser.rs:238-263]
  - Signature: `fn link_parents(symbols: &mut [Symbol]) {`
  - Purpose: # Summary

Assigns parent class/type symbols to child symbols by identifying byte-range containment relationships and updates their qualified names and function classifications accordingly. [crates/gcode/src/index/parser.rs:238-263]
- `extract_docstring` (function) component `extract_docstring [function]` (`923b7149-b4bc-57ed-8c19-85c4c1f6032b`) lines 265-326 [crates/gcode/src/index/parser.rs:265-326]
  - Signature: `fn extract_docstring(node: &tree_sitter::Node, source: &[u8], language: &str) -> Option<String> {`
  - Purpose: Extracts and returns the trimmed content of the first string literal encountered in a function or class body within a tree-sitter syntax tree for Python, JavaScript, or TypeScript, or None if not found. [crates/gcode/src/index/parser.rs:265-326]
- `strip_quotes` (function) component `strip_quotes [function]` (`37441e30-5c58-553c-a8ef-343372893121`) lines 328-335 [crates/gcode/src/index/parser.rs:328-335]
  - Signature: `fn strip_quotes(s: &str) -> &str {`
  - Purpose: Strips matching leading and trailing quote delimiters (prioritizing triple-quoted strings over single quotes) from a string and returns the trimmed interior, or the original string if no matching quotes are found. [crates/gcode/src/index/parser.rs:328-335]
- `extract_imports` (function) component `extract_imports [function]` (`ef7d4f8c-9f0f-5a72-be3d-82629913ef00`) lines 337-380 [crates/gcode/src/index/parser.rs:337-380]
  - Signature: `fn extract_imports(`
  - Purpose: Extracts language-specific import statements from source code via tree-sitter pattern matching and populates import resolution bindings. [crates/gcode/src/index/parser.rs:337-380]

