---
title: crates/gcode/src/index/languages.rs
type: code_file
provenance:
- file: crates/gcode/src/index/languages.rs
  ranges:
  - 7-12
  - 326-338
  - 341-346
  - 349-371
  - 374-385
  - 392-396
  - 399-404
  - 407-410
  - 413-419
  - 422-428
  - 430-435
  - 437-442
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/languages.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

`crates/gcode/src/index/languages.rs` exposes 12 indexed API symbols.
[crates/gcode/src/index/languages.rs:7-12]
[crates/gcode/src/index/languages.rs:326-338]
[crates/gcode/src/index/languages.rs:341-346]
[crates/gcode/src/index/languages.rs:349-371]
[crates/gcode/src/index/languages.rs:374-385]
[crates/gcode/src/index/languages.rs:392-396]
[crates/gcode/src/index/languages.rs:399-404]
[crates/gcode/src/index/languages.rs:407-410]
[crates/gcode/src/index/languages.rs:413-419]
[crates/gcode/src/index/languages.rs:422-428]
[crates/gcode/src/index/languages.rs:430-435]
[crates/gcode/src/index/languages.rs:437-442]

## API Symbols

- `LanguageSpec` (class) component `LanguageSpec [class]` (`45cbe260-2ed9-563d-9e08-950506b427fa`) lines 7-12 [crates/gcode/src/index/languages.rs:7-12]
  - Signature: `pub struct LanguageSpec {`
  - Purpose: `LanguageSpec` is a stateless struct that associates file extensions with static query strings for extracting symbols, imports, and calls from a given programming language. [crates/gcode/src/index/languages.rs:7-12]
- `detect_language` (function) component `detect_language [function]` (`010132ff-e730-54ef-a005-f15a8a1ce9c8`) lines 326-338 [crates/gcode/src/index/languages.rs:326-338]
  - Signature: `pub fn detect_language(file_path: &str) -> Option<&'static str> {`
  - Purpose: Determines the programming language of a file by matching its lowercase extension against a static specification map, returning the language name or `None` if no match is found. [crates/gcode/src/index/languages.rs:326-338]
- `get_spec` (function) component `get_spec [function]` (`f82e8aa9-4d3d-508d-9a91-81662aa61460`) lines 341-346 [crates/gcode/src/index/languages.rs:341-346]
  - Signature: `pub fn get_spec(lang: &str) -> Option<&'static LanguageSpec> {`
  - Purpose: Returns an optional reference to a static LanguageSpec by linearly searching an internal SPECS collection for a matching language name. [crates/gcode/src/index/languages.rs:341-346]
- `get_ts_language` (function) component `get_ts_language [function]` (`c63491bd-6e5a-5dab-adeb-5049e67503b5`) lines 349-371 [crates/gcode/src/index/languages.rs:349-371]
  - Signature: `pub fn get_ts_language(lang: &str) -> Option<Language> {`
  - Purpose: Maps a language identifier string to its corresponding tree-sitter Language parser, returning None if the language is unsupported. [crates/gcode/src/index/languages.rs:349-371]
- `get_ts_language_for_path` (function) component `get_ts_language_for_path [function]` (`9d568e28-9d31-598c-b189-1750a40d5ac2`) lines 374-385 [crates/gcode/src/index/languages.rs:374-385]
  - Signature: `pub fn get_ts_language_for_path(lang: &str, file_path: &str) -> Option<Language> {`
  - Purpose: Returns the Tree-sitter TSX language if the language parameter is "typescript" and the file extension is ".tsx", otherwise delegates to `get_ts_language` for standard TypeScript processing. [crates/gcode/src/index/languages.rs:374-385]
- `markdown_extensions_are_not_detected` (function) component `markdown_extensions_are_not_detected [function]` (`a020d84d-57c1-56fc-a4a8-6cfd1bfe29f1`) lines 392-396 [crates/gcode/src/index/languages.rs:392-396]
  - Signature: `fn markdown_extensions_are_not_detected() {`
  - Purpose: This unit test asserts that the `detect_language` function returns `None` for markdown file extensions (.md, .markdown), confirming that markdown files are intentionally handled as plain text content rather than parsed into an AST. [crates/gcode/src/index/languages.rs:392-396]
- `javascript_extensions_still_detect` (function) component `javascript_extensions_still_detect [function]` (`e8a63554-9bc6-5b69-9e77-8493f05d2479`) lines 399-404 [crates/gcode/src/index/languages.rs:399-404]
  - Signature: `fn javascript_extensions_still_detect() {`
  - Purpose: Unit test asserting that `detect_language` correctly identifies .js, .jsx, .cjs, and .mjs file extensions as `Some("javascript")`. [crates/gcode/src/index/languages.rs:399-404]
- `typescript_extensions_still_detect` (function) component `typescript_extensions_still_detect [function]` (`75e296d5-1992-5a58-85a0-2472b4a4aff0`) lines 407-410 [crates/gcode/src/index/languages.rs:407-410]
  - Signature: `fn typescript_extensions_still_detect() {`
  - Purpose: Unit test asserting that `detect_language` returns `Some("typescript")` for both `.ts` and `.tsx` file extensions. [crates/gcode/src/index/languages.rs:407-410]
- `tsx_paths_use_tsx_grammar` (function) component `tsx_paths_use_tsx_grammar [function]` (`469316ad-457d-5d65-9541-1a724765b4bc`) lines 413-419 [crates/gcode/src/index/languages.rs:413-419]
  - Signature: `fn tsx_paths_use_tsx_grammar() {`
  - Purpose: This test verifies that the TypeScript language grammar correctly parses JSX syntax when configured for `.tsx` file paths. [crates/gcode/src/index/languages.rs:413-419]
- `ts_paths_keep_typescript_grammar` (function) component `ts_paths_keep_typescript_grammar [function]` (`a5014def-f98c-5923-abaa-216d22db3a22`) lines 422-428 [crates/gcode/src/index/languages.rs:422-428]
  - Signature: `fn ts_paths_keep_typescript_grammar() {`
  - Purpose: Asserts that the TypeScript language parser configured for a specified file path correctly detects parsing errors in JSX syntax. [crates/gcode/src/index/languages.rs:422-428]
- `parses_without_error` (function) component `parses_without_error [function]` (`c4562978-6c37-5d1d-a1f3-93509666db9e`) lines 430-435 [crates/gcode/src/index/languages.rs:430-435]
  - Signature: `fn parses_without_error(language: Language, source: &str) -> bool {`
  - Purpose: This function checks whether the given source code parses without syntax errors in the specified tree-sitter language. [crates/gcode/src/index/languages.rs:430-435]
- `parses_with_error` (function) component `parses_with_error [function]` (`f864e9eb-ef9a-53cc-bc50-d64e949447db`) lines 437-442 [crates/gcode/src/index/languages.rs:437-442]
  - Signature: `fn parses_with_error(language: Language, source: &str) -> bool {`
  - Purpose: Parses source code using tree-sitter for a specified language and returns true if the resulting abstract syntax tree contains error nodes. [crates/gcode/src/index/languages.rs:437-442]

