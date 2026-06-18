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

`crates/gcode/src/index/semantic.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SemanticCallRequest` | class | Indexed class `SemanticCallRequest` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:15-23] |
| `SemanticCallTarget` | class | Indexed class `SemanticCallTarget` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:26-29] |
| `SemanticTargetKind` | type | Indexed type `SemanticTargetKind` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:33-43] |
| `SemanticCallResolver` | type | Indexed type `SemanticCallResolver` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:45-50] |
| `DefinitionLocation` | class | Indexed class `DefinitionLocation` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:53-55] |
| `create_cpp_semantic_resolver` | function | Indexed function `create_cpp_semantic_resolver` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:57-85] |
| `discover_compile_commands_dir` | function | Indexed function `discover_compile_commands_dir` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:87-105] |
| `classify_definition` | function | Indexed function `classify_definition` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:107-122] |
| `locations_from_lsp_response` | function | Indexed function `locations_from_lsp_response` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:124-135] |
| `location_from_lsp_value` | function | Indexed function `location_from_lsp_value` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:137-145] |
| `source_defines_macro` | function | Indexed function `source_defines_macro` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:147-153] |
| `logical_source_lines` | function | Indexed function `logical_source_lines` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:155-175] |
| `macro_definition_name` | function | Indexed function `macro_definition_name` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:177-210] |
| `definition_target_kind` | function | Indexed function `definition_target_kind` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:215-231] |
| `resolve_clangd_command` | function | Indexed function `resolve_clangd_command` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:233-240] |
| `parse_clangd_command` | function | Indexed function `parse_clangd_command` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:242-248] |
| `find_executable_in_path` | function | Indexed function `find_executable_in_path` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:251-256] |
| `find_executable_in_path` | function | Indexed function `find_executable_in_path` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:259-271] |
| `executable_name_candidates` | function | Indexed function `executable_name_candidates` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:274-295] |
| `env_flag` | function | Indexed function `env_flag` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:297-302] |
| `path_to_uri` | function | Indexed function `path_to_uri` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:304-330] |
| `is_windows_drive_prefix` | function | Indexed function `is_windows_drive_prefix` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:332-335] |
| `is_windows_drive_path` | function | Indexed function `is_windows_drive_path` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:337-339] |
| `file_uri_to_path` | function | Indexed function `file_uri_to_path` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:341-356] |
| `ClangdResolver` | class | Indexed class `ClangdResolver` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:358-366] |
| `ClangdResolver::start` | method | Indexed method `ClangdResolver::start` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:369-399] |
| `ClangdResolver::initialize` | method | Indexed method `ClangdResolver::initialize` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:401-413] |
| `ClangdResolver::ensure_open` | method | Indexed method `ClangdResolver::ensure_open` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:415-433] |
| `ClangdResolver::close_open_files` | method | Indexed method `ClangdResolver::close_open_files` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:435-463] |
| `ClangdResolver::send_request` | method | Indexed method `ClangdResolver::send_request` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:465-475] |
| `ClangdResolver::send_notification` | method | Indexed method `ClangdResolver::send_notification` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:477-483] |
| `ClangdResolver::write_message` | method | Indexed method `ClangdResolver::write_message` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:485-490] |
| `ClangdResolver::read_response` | method | Indexed method `ClangdResolver::read_response` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:492-494] |
| `ClangdResolver::drop` | method | Indexed method `ClangdResolver::drop` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:498-504] |
| `ClangdResolver::resolve` | method | Indexed method `ClangdResolver::resolve` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:508-543] |
| `spawn_clangd_stdout_reader` | function | Indexed function `spawn_clangd_stdout_reader` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:546-552] |
| `read_clangd_stdout` | function | Indexed function `read_clangd_stdout` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:554-572] |
| `read_json_rpc_message` | function | Indexed function `read_json_rpc_message` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:574-596] |
| `read_response_from_channel` | function | Indexed function `read_response_from_channel` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:598-630] |
| `format_clangd_timeout` | function | Indexed function `format_clangd_timeout` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:632-640] |
| `discovers_compile_commands_in_root_and_build_dirs` | function | Indexed function `discovers_compile_commands_in_root_and_build_dirs` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:651-658] |
| `parses_lsp_location_and_location_link_results` | function | Indexed function `parses_lsp_location_and_location_link_results` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:661-673] |
| `parses_quoted_clangd_command_arguments` | function | Indexed function `parses_quoted_clangd_command_arguments` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:676-685] |
| `rejects_empty_and_invalid_clangd_commands` | function | Indexed function `rejects_empty_and_invalid_clangd_commands` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:688-693] |
| `channel_response_wait_times_out` | function | Indexed function `channel_response_wait_times_out` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:696-702] |
| `classifies_single_definition_outside_project_as_external` | function | Indexed function `classifies_single_definition_outside_project_as_external` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:705-723] |
| `classifies_single_definition_inside_project_as_local_candidate` | function | Indexed function `classifies_single_definition_inside_project_as_local_candidate` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:726-746] |
| `drops_single_definition_when_canonicalization_fails` | function | Indexed function `drops_single_definition_when_canonicalization_fails` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:749-762] |
| `leaves_empty_multiple_and_macro_definitions_unresolved` | function | Indexed function `leaves_empty_multiple_and_macro_definitions_unresolved` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:765-798] |
| `detects_function_like_and_backslash_continued_macros` | function | Indexed function `detects_function_like_and_backslash_continued_macros` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:801-819] |
| `path_to_uri_encodes_absolute_path_components` | function | Indexed function `path_to_uri_encodes_absolute_path_components` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:823-827] |
| `path_to_uri_preserves_windows_drive_prefix` | function | Indexed function `path_to_uri_preserves_windows_drive_prefix` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:831-835] |
| `file_uri_to_path_strips_windows_drive_leading_slash` | function | Indexed function `file_uri_to_path_strips_windows_drive_leading_slash` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:839-844] |
| `file_uri_to_path_keeps_decoded_path_on_non_windows` | function | Indexed function `file_uri_to_path_keeps_decoded_path_on_non_windows` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:848-853] |
| `find_executable_in_path_honors_pathext_on_windows` | function | Indexed function `find_executable_in_path_honors_pathext_on_windows` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:858-882] |
| `optional_clangd_integration_resolves_external_definition` | function | Indexed function `optional_clangd_integration_resolves_external_definition` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:885-920] |

