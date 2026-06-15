---
title: crates/gcode/src/index/languages.rs
type: code_file
provenance:
- file: crates/gcode/src/index/languages.rs
  ranges:
  - 7-12
  - 326-338
  - 341-346
  - 355-359
  - 362-384
  - 387-398
  - 405-409
  - 412-417
  - 420-423
  - 426-432
  - 435-441
  - 443-448
  - 450-455
  - 458-468
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/languages.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

Registry of language-specific Tree-sitter query specs used by the indexer. It defines static `LanguageSpec` entries that map file extensions to symbol, import, and call queries, then provides helpers to detect a file’s language, look up a spec, classify data-only languages like JSON/YAML, and choose the correct Tree-sitter grammar, including TSX handling for `.tsx` paths. The test helpers and cases verify extension detection, parser selection, Markdown exclusion, and that only JSON/YAML are treated as data languages.
[crates/gcode/src/index/languages.rs:7-12]
[crates/gcode/src/index/languages.rs:326-338]
[crates/gcode/src/index/languages.rs:341-346]
[crates/gcode/src/index/languages.rs:355-359]
[crates/gcode/src/index/languages.rs:362-384]

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
- `is_data_language` (function) component `is_data_language [function]` (`de1fed24-e69f-5440-9cd1-7ef2467c9a64`) lines 355-359 [crates/gcode/src/index/languages.rs:355-359]
  - Signature: `pub fn is_data_language(lang: &str) -> bool {`
  - Purpose: Returns 'true' when 'get_spec(lang)' finds a language whose 'import_query' and 'call_query' are both empty, and 'false' otherwise. [crates/gcode/src/index/languages.rs:355-359]
- `get_ts_language` (function) component `get_ts_language [function]` (`a352da09-909e-5589-a05b-55a457160324`) lines 362-384 [crates/gcode/src/index/languages.rs:362-384]
  - Signature: `pub fn get_ts_language(lang: &str) -> Option<Language> {`
  - Purpose: Returns 'Some(Language)' by mapping a supported language name string to the corresponding Tree-sitter language constant, or 'None' if the input is not one of the recognized languages. [crates/gcode/src/index/languages.rs:362-384]
- `get_ts_language_for_path` (function) component `get_ts_language_for_path [function]` (`a19f009e-52da-58a3-b1cb-39e6460e52d0`) lines 387-398 [crates/gcode/src/index/languages.rs:387-398]
  - Signature: `pub fn get_ts_language_for_path(lang: &str, file_path: &str) -> Option<Language> {`
  - Purpose: Returns the TSX tree-sitter language for '.tsx' files when 'lang' is '"typescript"', otherwise delegates to 'get_ts_language(lang)' and returns its result. [crates/gcode/src/index/languages.rs:387-398]
- `markdown_extensions_are_not_detected` (function) component `markdown_extensions_are_not_detected [function]` (`97fb135c-6a68-5912-a7e9-0aa66b98b4a8`) lines 405-409 [crates/gcode/src/index/languages.rs:405-409]
  - Signature: `fn markdown_extensions_are_not_detected() {`
  - Purpose: Verifies that Markdown files with '.md' and '.markdown' extensions are not assigned a detected language, since Markdown is treated as content-only text rather than an AST-backed language. [crates/gcode/src/index/languages.rs:405-409]
- `javascript_extensions_still_detect` (function) component `javascript_extensions_still_detect [function]` (`04eca584-270a-52c3-bb74-d229935f2cf0`) lines 412-417 [crates/gcode/src/index/languages.rs:412-417]
  - Signature: `fn javascript_extensions_still_detect() {`
  - Purpose: Verifies that 'detect_language' returns 'Some("javascript")' for '.js', '.jsx', '.cjs', and '.mjs' file paths. [crates/gcode/src/index/languages.rs:412-417]
- `typescript_extensions_still_detect` (function) component `typescript_extensions_still_detect [function]` (`3e65dc2a-6b89-5bd0-8fbc-514f60a3183a`) lines 420-423 [crates/gcode/src/index/languages.rs:420-423]
  - Signature: `fn typescript_extensions_still_detect() {`
  - Purpose: Verifies that 'detect_language' returns 'Some("typescript")' for both '.ts' and '.tsx' file paths. [crates/gcode/src/index/languages.rs:420-423]
- `tsx_paths_use_tsx_grammar` (function) component `tsx_paths_use_tsx_grammar [function]` (`9da8762f-e2aa-5293-a07c-adf715368e5b`) lines 426-432 [crates/gcode/src/index/languages.rs:426-432]
  - Signature: `fn tsx_paths_use_tsx_grammar() {`
  - Purpose: Verifies that the TypeScript parser selected for a '.tsx' file can successfully parse JSX syntax without errors. [crates/gcode/src/index/languages.rs:426-432]
- `ts_paths_keep_typescript_grammar` (function) component `ts_paths_keep_typescript_grammar [function]` (`168734ef-e080-5a59-ad13-fc034d74f44e`) lines 435-441 [crates/gcode/src/index/languages.rs:435-441]
  - Signature: `fn ts_paths_keep_typescript_grammar() {`
  - Purpose: Verifies that the TypeScript grammar for '.ts' paths is preserved by asserting that a TS file containing JSX syntax ('<section />') parses with an error instead of being treated as TSX. [crates/gcode/src/index/languages.rs:435-441]
- `parses_without_error` (function) component `parses_without_error [function]` (`dc2ae90b-488c-5b30-8ee8-3a1de563a92e`) lines 443-448 [crates/gcode/src/index/languages.rs:443-448]
  - Signature: `fn parses_without_error(language: Language, source: &str) -> bool {`
  - Purpose: Creates a Tree-sitter parser for the given 'Language', parses the provided 'source', and returns 'true' only if the resulting syntax tree’s root node contains no parse errors. [crates/gcode/src/index/languages.rs:443-448]
- `parses_with_error` (function) component `parses_with_error [function]` (`6d79c8a1-1d74-5a85-97c7-5519eee8459a`) lines 450-455 [crates/gcode/src/index/languages.rs:450-455]
  - Signature: `fn parses_with_error(language: Language, source: &str) -> bool {`
  - Purpose: Returns 'true' if parsing 'source' with a Tree-sitter parser configured for 'language' produces a syntax tree whose root node reports an error, and 'false' otherwise. [crates/gcode/src/index/languages.rs:450-455]
- `is_data_language_matches_only_json_and_yaml` (function) component `is_data_language_matches_only_json_and_yaml [function]` (`14bc4b1f-8719-51b2-91c4-0ff446dd439e`) lines 458-468 [crates/gcode/src/index/languages.rs:458-468]
  - Signature: `fn is_data_language_matches_only_json_and_yaml() {`
  - Purpose: Verifies that 'is_data_language' returns 'true' only for 'json' and 'yaml', and 'false' for AST languages like 'rust', 'python', 'dart', and unknown language names. [crates/gcode/src/index/languages.rs:458-468]

