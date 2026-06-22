---
title: crates/gcode/src/index/semantic.rs
type: code_file
provenance:
- file: crates/gcode/src/index/semantic.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/semantic.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

`crates/gcode/src/index/semantic.rs` exposes 56 indexed API symbols.

## How it fits

`crates/gcode/src/index/semantic.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SemanticCallRequest` | class | 'SemanticCallRequest<'a>' is an internal borrowed request object that packages the target language, file and root paths, source bytes, callee name, and 1-based line/column position needed to perform a semantic call lookup. [crates/gcode/src/index/semantic.rs:15-23] |
| `SemanticCallTarget` | class | 'SemanticCallTarget' is an internal struct that represents a semantic call target by storing the callee’s name as a 'String' and its classification in a 'SemanticTargetKind'. [crates/gcode/src/index/semantic.rs:26-29] |
| `SemanticTargetKind` | type | Indexed type `SemanticTargetKind` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:33-43] |
| `SemanticCallResolver` | type | Indexed type `SemanticCallResolver` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:45-50] |
| `DefinitionLocation` | class | 'DefinitionLocation' is a crate-visible struct that stores a single 'PathBuf' identifying the filesystem path of a definition. [crates/gcode/src/index/semantic.rs:53-55] |
| `create_cpp_semantic_resolver` | function | Creates and returns a 'ClangdResolver' boxed as a 'SemanticCallResolver' when a compile commands directory and 'clangd' are available, otherwise returns 'Ok(None)' unless C/C++ semantics are required, in which case it fails with an error. [crates/gcode/src/index/semantic.rs:57-85] |
| `discover_compile_commands_dir` | function | Returns the first directory, either from the 'GCODE_COMPILE_COMMANDS_DIR' override or from a fixed set of candidate build paths under 'root_path', that contains a 'compile_commands.json' file, otherwise 'None'. [crates/gcode/src/index/semantic.rs:87-105] |
| `classify_definition` | function | Returns 'Some(SemanticCallTarget)' for a uniquely located definition whose declaration path resolves to a target kind and whose source does not define a macro, otherwise returns 'None'. [crates/gcode/src/index/semantic.rs:107-122] |
| `locations_from_lsp_response` | function | Parses an LSP JSON response’s 'result' field into a 'Vec<DefinitionLocation>', returning an empty vector when 'result' is missing or null, mapping each array element through 'location_from_lsp_value' when 'result' is an array, and otherwise converting a single location value into a one-element vector. [crates/gcode/src/index/semantic.rs:124-135] |
| `location_from_lsp_value` | function | Extracts a file URI from the 'uri' or 'targetUri' field of an LSP JSON value, converts it to a local path, and returns it wrapped in 'DefinitionLocation', or 'None' if any step fails. [crates/gcode/src/index/semantic.rs:137-145] |
| `source_defines_macro` | function | Returns 'true' if any logical line in the UTF-8 lossy decoded source yields a macro definition whose name exactly matches 'callee_name'. [crates/gcode/src/index/semantic.rs:147-153] |
| `logical_source_lines` | function | Splits 'text' into logical lines by concatenating physical lines ending in a trailing backslash ('\') onto the next line, preserving each completed line as a 'String' and appending any final unterminated fragment if present. [crates/gcode/src/index/semantic.rs:155-175] |
| `macro_definition_name` | function | Returns 'Some(name)' when 'line' is a preprocessor '#define' directive whose macro identifier starts with an ASCII letter or '_', continues with ASCII alphanumerics or '_', and is followed by '(', whitespace, or end-of-string; otherwise returns 'None'. [crates/gcode/src/index/semantic.rs:177-210] |
| `definition_target_kind` | function | Canonicalizes 'path' and 'root_path', returns 'None' if 'path' resolves exactly to 'root_path', returns 'SemanticTargetKind::LocalCandidate' with the root-relative path when 'path' is under 'root_path', and otherwise returns 'SemanticTargetKind::External' containing the original path string. [crates/gcode/src/index/semantic.rs:215-231] |
| `resolve_clangd_command` | function | Returns the 'GCODE_CLANGD' environment variable when it is set to a non-empty trimmed string, otherwise searches 'PATH' for 'clangd' and returns its resolved executable path as a string, or 'None' if neither is available. [crates/gcode/src/index/semantic.rs:233-240] |
| `parse_clangd_command` | function | Parses a clangd command string into shell-like arguments with 'shlex::split', returning an error if the input is empty or yields no tokens. [crates/gcode/src/index/semantic.rs:242-248] |
| `find_executable_in_path` | function | Searches the directories listed in 'PATH' for the first regular file named 'name' and returns its full 'PathBuf', or 'None' if 'PATH' is unset or no matching file exists. [crates/gcode/src/index/semantic.rs:251-256] |
| `find_executable_in_path` | function | Searches each directory in 'PATH' for the first file matching any platform-specific executable-name candidate derived from 'name', and returns its 'PathBuf' if found. [crates/gcode/src/index/semantic.rs:259-271] |
| `executable_name_candidates` | function | Returns a vector of executable path candidates for 'name', returning 'name' unchanged if it already has an extension, otherwise including 'name' plus 'name' with each non-empty 'PATHEXT' extension appended in normalized dot-prefixed form. [crates/gcode/src/index/semantic.rs:274-295] |
| `env_flag` | function | Returns 'true' if the named environment variable exists and its value is exactly one of '"1"', '"true"', '"TRUE"', '"yes"', or '"on"', otherwise returns 'false'. [crates/gcode/src/index/semantic.rs:297-302] |
| `path_to_uri` | function | Converts a filesystem 'Path' into a 'file:' URI by lossily stringifying it, normalizing Windows backslashes to forward slashes, percent-encoding each path segment except an initial Windows drive prefix, and choosing the correct 'file://' or 'file:///' form based on whether the path is UNC-like or drive-letter-based. [crates/gcode/src/index/semantic.rs:304-330] |
| `is_windows_drive_prefix` | function | Returns 'true' only when 'part' is exactly two bytes long, starts with an ASCII alphabetic character, and ends with ':', matching a Windows drive prefix like 'C:'. [crates/gcode/src/index/semantic.rs:332-335] |
| `is_windows_drive_path` | function | Returns 'true' when 'path' has at least two characters and its leading two-character slice satisfies 'is_windows_drive_prefix', indicating a Windows drive-prefixed path. [crates/gcode/src/index/semantic.rs:337-339] |
| `file_uri_to_path` | function | Parses a 'file://' URI by stripping the scheme, percent-decoding the remainder, removing a leading slash before a Windows drive letter when applicable, and returning the result as a 'PathBuf' or 'None' on invalid input. [crates/gcode/src/index/semantic.rs:341-356] |

_16 more symbol(s) not shown — run `gcode outline crates/gcode/src/index/semantic.rs` for the full list._

_Verified by 16 in-file unit tests._

