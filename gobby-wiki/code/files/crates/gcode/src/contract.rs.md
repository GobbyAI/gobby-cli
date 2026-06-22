---
title: crates/gcode/src/contract.rs
type: code_file
provenance:
- file: crates/gcode/src/contract.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/contract.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/contract.rs` exposes 28 indexed API symbols.

## How it fits

`crates/gcode/src/contract.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `contract` | function | The 'contract' function defines and returns a 'CliContract' struct specifying the CLI schema, global flags, project scoping, and available subcommands for the 'gcode' tool. [crates/gcode/src/contract.rs:5-542] |
| `format_flag` | function | The 'format_flag' function constructs and returns a 'FlagContract' for a '--format' command-line option, restricting its allowed values to either '"json"' or '"text"'. [crates/gcode/src/contract.rs:544-546] |
| `ai_flag` | function | The 'ai_flag' function constructs and returns a 'FlagContract' representing a command-line flag named '--ai' that restricts its value to one of the following allowed options: "auto", "daemon", "direct", or "off". [crates/gcode/src/contract.rs:548-551] |
| `ai_depth_flag` | function | The 'ai_depth_flag' function returns a 'FlagContract' configuration for the '--ai-depth' command-line argument, restricting its accepted values to "sections", "files", or "symbols". [crates/gcode/src/contract.rs:553-556] |
| `ai_prose_depth_flag` | function | The 'ai_prose_depth_flag' function returns a 'FlagContract' configuration for the '--ai-prose-depth' command-line flag, restricting its accepted values to "brief", "standard", or "deep". [crates/gcode/src/contract.rs:558-561] |
| `ai_register_flag` | function | The 'ai_register_flag' function constructs and returns a 'FlagContract' for the '--ai-register' command-line flag, restricting its acceptable values to "newcomer", "maintainer", or "agent". [crates/gcode/src/contract.rs:563-569] |
| `token_budget_flag` | function | The 'token_budget_flag' function constructs and returns a 'FlagContract' defining a command-line option named '"--token-budget"' that accepts an argument value represented by '"N"'. [crates/gcode/src/contract.rs:571-573] |
| `search_flags` | function | The 'search_flags' function returns a vector of 'FlagContract' instances representing the command-line search options '--limit', '--offset', '--kind', and '--language' with their expected value types. [crates/gcode/src/contract.rs:575-582] |
| `grep_flags` | function | The 'grep_flags' function constructs and returns a vector of 'FlagContract' objects defining standard pattern-matching, context-filtering, and formatting command-line flags. [crates/gcode/src/contract.rs:584-596] |
| `graph_read_flags` | function | The 'graph_read_flags' function constructs and returns a vector of 'FlagContract' instances representing command-line flags for a limit, an offset, and a format option. [crates/gcode/src/contract.rs:598-604] |
| `outline_keys` | function | The function 'outline_keys' returns a vector containing the static string slice keys '"id"', '"name"', '"kind"', '"line_start"', '"line_end"', and '"signature"'. [crates/gcode/src/contract.rs:606-608] |
| `tree_keys` | function | The 'tree_keys' function returns a vector containing the static string slices '"file_path"', '"language"', and '"symbol_count"'. [crates/gcode/src/contract.rs:610-612] |
| `symbol_record_keys` | function | The function 'symbol_record_keys' returns a vector of static string slices containing the identifier and metadata field keys associated with a symbol record. [crates/gcode/src/contract.rs:618-637] |
| `symbol_keys` | function | The 'symbol_keys' function retrieves a vector of static string slices from 'symbol_record_keys', appends the string slice '"source"' to it, and returns the modified vector. [crates/gcode/src/contract.rs:640-644] |
| `symbol_at_keys` | function | The 'symbol_at_keys' function returns a vector of static string slices retrieved from 'symbol_keys' with the string literal '"lookup"' appended to the end. [crates/gcode/src/contract.rs:647-651] |
| `paged_graph_keys` | function | The 'paged_graph_keys' function returns a vector of static string slices containing predefined keys used for paginating and querying graph-related data. [crates/gcode/src/contract.rs:656-673] |
| `search_keys` | function | The 'search_keys' function returns a vector of static string slices containing a predefined set of search parameters, pagination control names, and schema metadata fields. [crates/gcode/src/contract.rs:675-693] |
| `grep_keys` | function | The 'grep_keys' function returns a vector of static string slices containing key names representing configuration parameters and response fields for a grep search operation. [crates/gcode/src/contract.rs:695-718] |
| `graph_read_keys` | function | The 'graph_read_keys' function returns a vector of static string slices containing a predefined list of keys representing graph metadata, pagination parameters, and entity attributes. [crates/gcode/src/contract.rs:720-737] |
| `graph_path_keys` | function | The 'graph_path_keys' function returns a vector of static string slices representing predefined property and parameter keys for graph path queries and metadata. [crates/gcode/src/contract.rs:739-756] |
| `contract_keys` | function | The 'contract_keys' function returns a vector of static string slices containing the keys "tool", "contract_version", "summary", "global_flags", "scope", "commands", and "error_codes". [crates/gcode/src/contract.rs:758-768] |
| `graph_payload_keys` | function | The 'graph_payload_keys' function returns a vector of static string slices containing '"nodes"', '"links"', and '"summary"'. [crates/gcode/src/contract.rs:770-772] |
| `graph_lifecycle_keys` | function | The 'graph_lifecycle_keys' function returns a 'Vec<&'static str>' containing predefined string literal keys representing graph lifecycle status, synchronization metrics, and summary metadata. [crates/gcode/src/contract.rs:774-788] |
| `graph_cleanup_keys` | function | The 'graph_cleanup_keys' function returns a vector of static string slices containing the keys used for tracking and reporting graph cleanup operations, specifically 'status', 'action', 'project_id', 'stale_graph_files_deleted', and 'graph_nodes_deleted'. [crates/gcode/src/contract.rs:790-798] |

_4 more symbol(s) not shown — run `gcode outline crates/gcode/src/contract.rs` for the full list._

