---
title: crates/gcode/src/index/import_resolution/helpers.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/helpers.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/helpers.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/helpers.rs` exposes 22 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/helpers.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `collapse_whitespace` | function | Returns a new 'String' that normalizes all runs of Unicode whitespace in 'text' into single ASCII spaces, removing leading and trailing whitespace. [crates/gcode/src/index/import_resolution/helpers.rs:3-5] |
| `extract_js_module_specifier` | function | Returns the quoted module specifier from a JavaScript 'import' statement by first parsing the substring after the last '" from "' and, if absent, parsing the string after an 'import ' prefix, yielding 'None' when no quoted specifier is found. [crates/gcode/src/index/import_resolution/helpers.rs:7-13] |
| `extract_js_import_clause` | function | Returns the substring between the leading '"import "' prefix and the last '" from "' separator in 'text', or 'None' if either delimiter is missing. [crates/gcode/src/index/import_resolution/helpers.rs:15-19] |
| `extract_quoted_string` | function | Returns the contents of the first quoted substring in 'text' delimited by '"', ''', or '' ' '', stopping at the matching closing quote while honoring backslash escapes and skipping '${...}' interpolation, or 'None' if no terminator is found. [crates/gcode/src/index/import_resolution/helpers.rs:21-49] |
| `skip_template_interpolation` | function | Scans forward from 'idx' through a template interpolation, tracking nested '{}' and quoted/escaped substrings, and returns the byte index just after the matching closing '}' when the brace depth reaches zero, or 'None' if no terminator is found. [crates/gcode/src/index/import_resolution/helpers.rs:51-88] |
| `go_default_package_alias` | function | Returns a default Go package alias by trimming trailing slashes, taking the last path segment, stripping a valid '.vN...' version suffix if present, and replacing hyphens with underscores. [crates/gcode/src/index/import_resolution/helpers.rs:90-99] |
| `split_alias` | function | Trims the input string and, if it contains the substring ' as ', returns the trimmed text before it as the name and the trimmed text after it as 'Some(alias)', otherwise returns the trimmed input and 'None'. [crates/gcode/src/index/import_resolution/helpers.rs:101-107] |
| `split_rust_use_group` | function | Scans a Rust 'use' statement for a top-level brace-delimited group and, if the braces are balanced and nothing but whitespace follows the closing brace, returns the trimmed prefix before '{' and the trimmed contents inside the group; otherwise returns 'None'. [crates/gcode/src/index/import_resolution/helpers.rs:109-136] |
| `rust_join_use_path` | function | Trims 'prefix' and 'item', rejects empty inputs, resolves 'self' to the non-empty prefix or concatenates 'prefix::item_path', and returns the resulting Rust 'use' path optionally suffixed with 'as alias' when an alias is present. [crates/gcode/src/index/import_resolution/helpers.rs:138-166] |
| `SplitTopLevelError` | class | 'SplitTopLevelError' is a private error type that records the delimiter, byte position, error kind, and surrounding context for a failure encountered while splitting a top-level string. [crates/gcode/src/index/import_resolution/helpers.rs:169-174] |
| `SplitTopLevelError::fmt` | method | Formats the value as a human-readable error string of the form '"{kind} while splitting on '{delimiter}' at byte {position} near '{context}'"' using the provided formatter. [crates/gcode/src/index/import_resolution/helpers.rs:177-183] |
| `SplitTopLevelError::new` | method | Constructs a new instance by storing the provided 'delimiter', 'position', and 'kind', and computing 'context' from 'text' and 'position' via 'split_error_context'. [crates/gcode/src/index/import_resolution/helpers.rs:189-196] |
| `split_error_context` | function | Returns a UTF-8-safe error snippet centered on 'position' by clamping it to 'text.len()', expanding to at most 24 characters on each side on character boundaries, and escaping newline characters as '\\n'. [crates/gcode/src/index/import_resolution/helpers.rs:199-214] |
| `split_top_level` | function | Splits 'text' on the specified 'delimiter' only when it appears at top level outside quotes, escapes, and any nested '()', '{}', or '[]', and returns a 'SplitTopLevelError' if it encounters an unbalanced closing delimiter. [crates/gcode/src/index/import_resolution/helpers.rs:216-305] |
| `is_ruby_constant_name` | function | Returns 'true' if 'name' satisfies the 'is_uppercase_ascii_alnum_underscore_name' predicate, i.e. it is a Ruby constant-style identifier using only uppercase ASCII letters, digits, and underscores. [crates/gcode/src/index/import_resolution/helpers.rs:307-309] |
| `is_uppercase_ascii_alnum_underscore_name` | function | Returns 'true' iff 'name' is non-empty, starts with an ASCII uppercase letter, and every character is an ASCII alphanumeric or underscore. [crates/gcode/src/index/import_resolution/helpers.rs:311-318] |
| `dart_import_alias` | function | Extracts the first whitespace-delimited token following '" as "' in a Dart import string, strips any trailing semicolon, and returns it as 'Some(alias)' unless no nonempty alias is present, in which case it returns 'None'. [crates/gcode/src/index/import_resolution/helpers.rs:320-332] |
| `dart_local_import_target` | function | Returns a normalized project-local Dart import path only for same-package 'package:' URIs or non-empty relative paths resolved against 'rel_path', and returns 'None' for other packages, SDK/other schemes, or empty resolutions. [crates/gcode/src/index/import_resolution/helpers.rs:341-362] |
| `normalize_relative_dart_path` | function | Returns a slash-separated relative path string by discarding '.' and root/prefix components, resolving '..' by popping the previous segment, and concatenating the remaining normal components. [crates/gcode/src/index/import_resolution/helpers.rs:368-381] |
| `is_elixir_alias` | function | Returns 'true' if 'name' satisfies 'is_uppercase_ascii_alnum_underscore_name', meaning it is an uppercase ASCII identifier composed of alphanumeric characters and underscores. [crates/gcode/src/index/import_resolution/helpers.rs:383-385] |
| `is_elixir_alias_path` | function | Returns 'true' if every '.'-separated segment of 'path' satisfies 'is_elixir_alias', and 'false' otherwise. [crates/gcode/src/index/import_resolution/helpers.rs:387-389] |
| `elixir_alias_as` | function | Extracts the first candidate token following the literal substring '" as: "' up to the next comma, space, ')', or ']', and returns it as 'Some(String)' only if it passes 'is_elixir_alias', otherwise 'None'. [crates/gcode/src/index/import_resolution/helpers.rs:391-403] |

