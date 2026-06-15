---
title: crates/gcode/src/index/parser.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser.rs
  ranges:
  - 29-133
  - 135-234
  - 236-261
  - 263-324
  - 326-333
  - 335-378
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

Parses source files into indexable syntax data, but only after strict safety and size checks: it rejects unsafe, excluded, secret, binary, empty, oversized, or unsupported files, then detects the language, loads the Tree-sitter parser, and returns an optional `ParseResult` when parsing succeeds. The helper functions build the rest of the index from that tree: `extract_symbols` collects de-duplicated symbol definitions, `link_parents` assigns enclosing class/type parents and rewrites child function names as methods, `extract_docstring` pulls a leading docstring from Python/JS/TS function bodies, `strip_quotes` normalizes quoted string text, and `extract_imports` parses language-specific import statements into an `ExtractedImports` accumulator.
[crates/gcode/src/index/parser.rs:29-133]
[crates/gcode/src/index/parser.rs:135-234]
[crates/gcode/src/index/parser.rs:236-261]
[crates/gcode/src/index/parser.rs:263-324]
[crates/gcode/src/index/parser.rs:326-333]

## API Symbols

- `parse_file_with_semantic` (function) component `parse_file_with_semantic [function]` (`bc988700-71a5-5773-9ba4-992db3c7e9ab`) lines 29-133 [crates/gcode/src/index/parser.rs:29-133]
  - Signature: `pub(crate) fn parse_file_with_semantic(`
  - Purpose: Validates that 'file_path' is a safe, non-excluded, non-secret, non-binary source file under size limits, detects its language, parses it into a tree-sitter syntax tree, computes a relative path, and extracts symbols to produce an optional 'ParseResult' while returning 'Ok(None)' for any unsupported or failed step. [crates/gcode/src/index/parser.rs:29-133]
- `extract_symbols` (function) component `extract_symbols [function]` (`5812f687-c705-512d-9b61-0a67f0b75d18`) lines 135-234 [crates/gcode/src/index/parser.rs:135-234]
  - Signature: `fn extract_symbols(`
  - Purpose: 'extract_symbols' compiles the language-specific tree-sitter symbol query, walks all matches in the syntax tree, and returns a de-duplicated 'Vec<Symbol>' built from matched definition nodes and their captured names, or an empty list if no symbol query is configured. [crates/gcode/src/index/parser.rs:135-234]
- `link_parents` (function) component `link_parents [function]` (`59a940c5-8e00-5ced-9a83-db39df6bd55e`) lines 236-261 [crates/gcode/src/index/parser.rs:236-261]
  - Signature: `fn link_parents(symbols: &mut [Symbol]) {`
  - Purpose: 'link_parents' sorts symbols by source start offset, then for each symbol finds the nearest enclosing 'class' or 'type' symbol and assigns it as the parent, updates the child’s qualified name, and renames child functions to 'method'. [crates/gcode/src/index/parser.rs:236-261]
- `extract_docstring` (function) component `extract_docstring [function]` (`b606577f-1a56-573e-914a-627c786663d7`) lines 263-324 [crates/gcode/src/index/parser.rs:263-324]
  - Signature: `fn extract_docstring(node: &tree_sitter::Node, source: &[u8], language: &str) -> Option<String> {`
  - Purpose: Returns the first non-comment, non-empty leading string literal found in a Python/JavaScript/TypeScript function body as a trimmed docstring, preferring 'string_content' when available and otherwise stripping quotes, and returns 'None' for unsupported languages or if no valid body docstring exists. [crates/gcode/src/index/parser.rs:263-324]
- `strip_quotes` (function) component `strip_quotes [function]` (`8196ece1-37be-5462-a106-0d0b1f28fb78`) lines 326-333 [crates/gcode/src/index/parser.rs:326-333]
  - Signature: `fn strip_quotes(s: &str) -> &str {`
  - Purpose: Returns the input string trimmed of matching surrounding quote delimiters, preferring triple quotes ('"""' or ''''') before single quotes, and otherwise returns the original string unchanged. [crates/gcode/src/index/parser.rs:326-333]
- `extract_imports` (function) component `extract_imports [function]` (`aaa4d8ac-9b44-5cbe-8433-da23601e574b`) lines 335-378 [crates/gcode/src/index/parser.rs:335-378]
  - Signature: `fn extract_imports(`
  - Purpose: Compiles and runs a Tree-sitter import query for the given language, extracts text from captures named 'import', parses each import statement into an 'ExtractedImports' accumulator, seeds import bindings from context, and returns the result or an error if query compilation or import parsing fails. [crates/gcode/src/index/parser.rs:335-378]

