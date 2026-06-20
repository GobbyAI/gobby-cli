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

`crates/gcode/src/index/languages.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

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
| `parses_without_error` | function | Creates a Tree-sitter parser for the given 'Language', parses 'source', and returns 'true' only if the resulting syntax tree’s root node has no parse errors. [crates/gcode/src/index/languages.rs:777-782] |
| `parses_with_error` | function | Returns 'true' if parsing 'source' with a new 'tree_sitter::Parser' configured for 'language' produces a syntax tree whose root node reports an error, and 'false' otherwise. [crates/gcode/src/index/languages.rs:784-789] |

_Verified by 15 in-file unit tests._

