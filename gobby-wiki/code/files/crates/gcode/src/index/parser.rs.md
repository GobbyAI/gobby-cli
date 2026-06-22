---
title: crates/gcode/src/index/parser.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

`crates/gcode/src/index/parser.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gcode/src/index/parser.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `parse_file_with_semantic` | function | Validates that 'file_path' is a safe, non-excluded, non-secret, non-binary, size-bounded file under 'root_path', detects its language and Tree-sitter parser, reads and parses the source into an AST, computes a relative path, and then extracts symbols to produce an optional 'ParseResult' or 'None' on any failure. [crates/gcode/src/index/parser.rs:29-134] |
| `extract_symbols` | function | 'extract_symbols' compiles the language-specific Tree-sitter symbol query, scans the syntax tree for matching definition/name captures, deduplicates results by ID, and returns a 'Vec<Symbol>' built from each symbol’s name, definition node, and first-line signature. [crates/gcode/src/index/parser.rs:136-235] |
| `link_parents` | function | Assigns each symbol the nearest enclosing 'class' or 'type' as its parent based on byte-span containment, updates its 'parent_symbol_id' and dotted 'qualified_name', and promotes non-Elixir nested functions to 'method' kind. [crates/gcode/src/index/parser.rs:237-264] |
| `collapse_rust_impl_symbols` | function | Rewrites Rust symbols nested under 'impl' blocks so their 'qualified_name' becomes 'Type::member', reparenting them to the canonical type declaration in the same file when available, and then removes the 'impl' symbols themselves from the vector. [crates/gcode/src/index/parser.rs:266-318] |
| `is_rust_impl_symbol` | function | Returns 'true' only for Rust class symbols whose signature begins with 'impl ' or 'unsafe impl ', indicating a Rust implementation block. [crates/gcode/src/index/parser.rs:320-326] |
| `extract_docstring` | function | Returns the first non-empty docstring-like string literal from the start of a Python/JavaScript/TypeScript node’s block body, preferring 'string_content' when present and otherwise stripping quotes, and yields 'None' for unsupported languages or if no valid string is found. [crates/gcode/src/index/parser.rs:328-389] |
| `strip_quotes` | function | Returns the trimmed inner slice of 's' if it is enclosed by matching triple or single quotes ('"""', ''''', '"' or ''') on both ends with sufficient length, otherwise returns 's' unchanged. [crates/gcode/src/index/parser.rs:391-398] |
| `extract_imports` | function | Compiles and executes the language’s tree-sitter import query over the parsed source, extracts each '"import"' capture as text, parses it into an 'ExtractedImports' via import-resolution helpers, seeds import bindings from context, and returns the accumulated result or an error if query compilation or parsing fails. [crates/gcode/src/index/parser.rs:400-443] |

