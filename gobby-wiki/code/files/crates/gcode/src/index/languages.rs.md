---
title: crates/gcode/src/index/languages.rs
type: code_file
provenance:
- file: crates/gcode/src/index/languages.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/languages.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

`crates/gcode/src/index/languages.rs` exposes 33 indexed API symbols.

## How it fits

`crates/gcode/src/index/languages.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `LanguageSpec` | class | 'LanguageSpec' is a static configuration struct that associates a language with its file extensions and three Tree-sitter query strings for symbols, imports, and calls. [crates/gcode/src/index/languages.rs:9-14] |
| `detect_language` | function | Returns the language name for a file path by lowercasing and matching its extension against 'SPECS', with '.h' files delegated to 'detect_header_language', and 'None' if no extension mapping exists. [crates/gcode/src/index/languages.rs:443-459] |
| `detect_header_language` | function | Returns '"objc"' for a header if it has a sibling implementation file or Objective-C header signals, '"cpp"' if it instead contains C++ header signals, and '"c"' when the file cannot be read or no such signals are found. [crates/gcode/src/index/languages.rs:461-480] |
| `objc_header_has_sibling_implementation` | function | Returns 'true' if the given Objective-C header path has a sibling implementation file with the same stem and either '.m' or '.mm' extension, otherwise 'false'. [crates/gcode/src/index/languages.rs:482-484] |
| `source_contains_objc_header_signal` | function | Returns 'true' if the source contains an Objective-C header-like directive at a candidate header position, specifically '@interface', '@protocol', or '@import', as detected via 'source_contains_header_signal'. [crates/gcode/src/index/languages.rs:486-492] |
| `source_contains_cpp_header_signal` | function | Returns 'true' if 'source_contains_header_signal' finds a header-like pattern in 'source' where the callback detects a C++ keyword token at the given position: 'class', 'namespace', or 'template'. [crates/gcode/src/index/languages.rs:494-500] |
| `source_contains_header_signal` | function | Returns 'true' if 'signal_at' reports a match at any byte offset in the source outside line comments, block comments, and quoted strings, otherwise returns 'false'. [crates/gcode/src/index/languages.rs:502-533] |
| `skip_quoted` | function | Returns the index just past the matching closing quote for the quoted byte sequence starting at 'start', skipping over escaped bytes introduced by '\\', or 'bytes.len()' if no closing quote is found. [crates/gcode/src/index/languages.rs:535-548] |
| `objc_directive_at` | function | Returns 'true' when 'directive' matches exactly at 'idx' in 'bytes' and is not immediately followed by an ASCII identifier byte, so the match is delimited or at end of input. [crates/gcode/src/index/languages.rs:550-555] |
| `c_like_keyword_at` | function | Returns 'true' when 'keyword' matches exactly at 'idx' and is not adjacent to ASCII identifier bytes, with the extra rule that the preceding byte must also not be '@'. [crates/gcode/src/index/languages.rs:557-566] |
| `literal_at` | function | Returns 'true' if the slice 'bytes' contains 'literal' exactly at offset 'idx' with no out-of-bounds access, otherwise 'false'. [crates/gcode/src/index/languages.rs:568-570] |
| `is_ascii_identifier_byte` | function | Returns 'true' if the byte is an ASCII alphanumeric character or an underscore, and 'false' otherwise. [crates/gcode/src/index/languages.rs:572-574] |
| `get_spec` | function | Returns the 'LanguageSpec' associated with 'lang' by searching 'SPECS' for a matching name and mapping the found tuple to its spec, or 'None' if no match exists. [crates/gcode/src/index/languages.rs:577-582] |
| `is_data_language` | function | Returns 'true' if 'lang' resolves to a spec whose 'import_query' and 'call_query' are both empty, and 'false' otherwise. [crates/gcode/src/index/languages.rs:591-595] |
| `get_ts_language` | function | Returns 'Some(Language)' for a fixed set of supported language strings by mapping each name to the corresponding Tree-sitter language constant, and returns 'None' for any unsupported input. [crates/gcode/src/index/languages.rs:598-624] |
| `get_ts_language_for_path` | function | Returns the TypeScript TSX Tree-sitter 'Language' for '.tsx' files when 'lang == "typescript"', otherwise delegates to 'get_ts_language(lang)' and returns its result. [crates/gcode/src/index/languages.rs:627-638] |
| `markdown_extensions_are_not_detected` | function | Verifies that Markdown files are not classified as a language by 'detect_language', returning 'None' for both '.md' and '.markdown' paths because Markdown is treated as content-only text rather than AST. [crates/gcode/src/index/languages.rs:645-649] |
| `javascript_extensions_still_detect` | function | Verifies that 'detect_language' returns 'Some("javascript")' for '.js', '.jsx', '.cjs', and '.mjs' file paths. [crates/gcode/src/index/languages.rs:652-657] |
| `typescript_extensions_still_detect` | function | Verifies that 'detect_language' classifies both '.ts' and '.tsx' file paths as 'Some("typescript")'. [crates/gcode/src/index/languages.rs:660-663] |
| `bash_extensions_detect` | function | Verifies that 'detect_language' classifies 'scripts/deploy.sh' and 'scripts/env.bash' as 'Some("bash")'. [crates/gcode/src/index/languages.rs:666-669] |
| `scala_extensions_detect` | function | Verifies that 'detect_language' classifies '.scala' and '.sc' source paths as 'Some("scala")'. [crates/gcode/src/index/languages.rs:672-675] |
| `lua_extensions_detect` | function | Asserts that 'detect_language("lua/app/init.lua")' correctly returns 'Some("lua")', verifying Lua language detection for a Lua file path. [crates/gcode/src/index/languages.rs:678-680] |
| `objc_extensions_detect` | function | Verifies that 'detect_language' classifies both '.m' and '.mm' source files as Objective-C by asserting it returns 'Some("objc")' for each path. [crates/gcode/src/index/languages.rs:683-686] |
| `c_header_detects_without_objc_or_cpp_signal` | function | Verifies that 'detect_language("Sources/App/Widget.h")' returns 'Some("c")' for a '.h' header path when no Objective-C or C++ indicators are present. [crates/gcode/src/index/languages.rs:689-691] |
| `objc_header_detects_declaration_signal` | function | Creates a temporary Objective-C header file containing an '@interface' declaration and verifies that 'detect_language' classifies it as 'Some("objc")'. [crates/gcode/src/index/languages.rs:694-708] |
| `objc_header_detects_sibling_implementation_signal` | function | Creates a temporary Objective-C header and sibling '.m' implementation file, then asserts that 'detect_language' classifies the header as 'Some("objc")'. [crates/gcode/src/index/languages.rs:711-722] |
| `cpp_header_detects_cpp_signal` | function | Creates a temporary '.h' file containing C++-specific syntax and verifies that 'detect_language' classifies it as 'Some("cpp")'. [crates/gcode/src/index/languages.rs:725-740] |
| `objcxx_paths_use_objc_grammar` | function | Verifies that 'get_ts_language_for_path("objc", "Sources/App/Widget.mm")' returns a language that parses an Objective-C interface/implementation snippet without errors. [crates/gcode/src/index/languages.rs:743-757] |
| `tsx_paths_use_tsx_grammar` | function | Verifies that the TypeScript grammar selected for a '.tsx' path can successfully parse TSX syntax without errors. [crates/gcode/src/index/languages.rs:760-766] |
| `ts_paths_keep_typescript_grammar` | function | Verifies that the TypeScript grammar selected for a '.ts' file does not accept JSX syntax by asserting that 'export const View = () => <section />;' in 'src/app.ts' parses with an error. [crates/gcode/src/index/languages.rs:769-775] |
| `parses_without_error` | function | Creates a Tree-sitter parser for the given 'Language', parses 'source', and returns 'true' only if the resulting syntax tree’s root node has no parse errors. [crates/gcode/src/index/languages.rs:777-782] |
| `parses_with_error` | function | Returns 'true' if parsing 'source' with a new 'tree_sitter::Parser' configured for 'language' produces a syntax tree whose root node reports an error, and 'false' otherwise. [crates/gcode/src/index/languages.rs:784-789] |
| `is_data_language_matches_only_json_and_yaml` | function | Verifies that 'is_data_language' returns 'true' only for 'json' and 'yaml', and 'false' for AST/query-bearing languages ('rust', 'python', 'dart') as well as unknown languages. [crates/gcode/src/index/languages.rs:792-802] |

