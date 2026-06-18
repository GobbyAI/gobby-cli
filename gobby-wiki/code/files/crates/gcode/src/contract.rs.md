---
title: crates/gcode/src/contract.rs
type: code_file
provenance:
- file: crates/gcode/src/contract.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/contract.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The `crates/gcode/src/contract.rs` file defines the schema contract for the `gcode` CLI tool, which serves as a fast code index CLI for Gobby. Its primary entry point is the `contract` function crates/gcode/src/contract.rs:5-535. This function constructs and returns a `CliContract` describing the CLI's version (version 2), its global flags (such as formatting, quietness, verbosity, and freshness), and the available subcommand contracts.

## How it fits
[crates/gcode/src/contract.rs:5-535]
[crates/gcode/src/contract.rs:537-539]
[crates/gcode/src/contract.rs:541-544]
[crates/gcode/src/contract.rs:546-548]
[crates/gcode/src/contract.rs:550-557]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `contract` | function | Constructs and returns a 'CliContract' describing the 'gcode' CLI: version 2, global project/format/verbosity flags, project-scoped identity defaults, and the available commands and their contracts. [crates/gcode/src/contract.rs:5-535] |
| `format_flag` | function | Creates a 'FlagContract' for the '--format' option with the value specifier '"json\|text"' and restricts it to the allowed values 'json' and 'text'. [crates/gcode/src/contract.rs:537-539] |
| `ai_flag` | function | Defines a 'FlagContract' for the '--ai' CLI flag with the value pattern 'auto\|daemon\|direct\|off' and restricts accepted values to 'auto', 'daemon', 'direct', and 'off'. [crates/gcode/src/contract.rs:541-544] |
| `token_budget_flag` | function | Returns a 'FlagContract' representing the '--token-budget' CLI flag with the value placeholder 'N'. [crates/gcode/src/contract.rs:546-548] |
| `search_flags` | function | Returns a vector of 'FlagContract' values defining the supported search CLI flags: '--limit', '--offset', '--kind', and '--language', each with its expected placeholder. [crates/gcode/src/contract.rs:550-557] |
| `grep_flags` | function | Returns a 'Vec<FlagContract>' describing supported 'grep' CLI options: switches for '--fixed-strings', '--ignore-case', and '--word', value flags for '--before-context', '--after-context', '--context', and '--max-count', a repeatable '--glob' value flag, and the 'format_flag()' entry. [crates/gcode/src/contract.rs:559-571] |
| `graph_read_flags` | function | Returns a 'Vec<FlagContract>' describing the readable graph flags '--limit', '--offset', and the format flag. [crates/gcode/src/contract.rs:573-579] |
| `outline_keys` | function | Returns a vector of six static string keys representing an outline schema: 'id', 'name', 'kind', 'line_start', 'line_end', and 'signature'. [crates/gcode/src/contract.rs:581-583] |
| `tree_keys` | function | Returns a vector of three static string keys: '"file_path"', '"language"', and '"symbol_count"'. [crates/gcode/src/contract.rs:585-587] |
| `symbol_record_keys` | function | Returns a 'Vec<&'static str>' listing the fixed database record field keys for a symbol, including identifiers, location ranges, metadata, timestamps, and content fields. [crates/gcode/src/contract.rs:593-612] |
| `symbol_keys` | function | Returns the list of symbol record keys with '"source"' appended to the end. [crates/gcode/src/contract.rs:615-619] |
| `symbol_at_keys` | function | Returns the list of symbol keys from 'symbol_keys()' with the string '"lookup"' appended. [crates/gcode/src/contract.rs:622-626] |
| `paged_graph_keys` | function | Returns a static vector of string slice field names used for paged graph data structures: 'project_id', 'total', 'offset', 'limit', 'results', 'id', 'name', 'file_path', 'line', 'confidence', 'relation', 'distance', 'metadata', and 'hint'. [crates/gcode/src/contract.rs:631-648] |
| `search_keys` | function | Returns a fixed vector of string keys used for search result metadata and pagination, including project, result, location, and scoring fields. [crates/gcode/src/contract.rs:650-668] |
| `grep_keys` | function | Returns a static 'Vec<&'static str>' listing the grep result and query field names used by the function, including search parameters, match metadata, and span coordinates. [crates/gcode/src/contract.rs:670-693] |
| `graph_read_keys` | function | Returns a static vector of string keys used for graph-reading results and pagination metadata: 'project_id', 'total', 'offset', 'limit', 'results', 'id', 'name', 'file_path', 'line', 'confidence', 'relation', 'distance', 'metadata', and 'hint'. [crates/gcode/src/contract.rs:695-712] |
| `graph_path_keys` | function | Returns a static vector of string keys used to describe graph path data fields: 'project_id', 'found', 'from', 'to', 'max_depth', 'hops', 'path', 'position', 'id', 'display_name', 'name', 'file_path', 'line', and 'hint'. [crates/gcode/src/contract.rs:714-731] |
| `contract_keys` | function | Returns a vector of seven static string keys identifying the contract fields: 'tool', 'contract_version', 'summary', 'global_flags', 'scope', 'commands', and 'error_codes'. [crates/gcode/src/contract.rs:733-743] |
| `graph_payload_keys` | function | Returns a vector of the three static payload key names: '"nodes"', '"links"', and '"summary"'. [crates/gcode/src/contract.rs:745-747] |
| `graph_lifecycle_keys` | function | Returns the fixed list of lifecycle field keys used for graph synchronization and cleanup state tracking: 'status', 'action', 'project_id', 'synced_files', 'synced_symbols', 'skipped_files', 'failed_files', 'synced_relationships', 'deleted_nodes', 'deleted_relationships', and 'summary'. [crates/gcode/src/contract.rs:749-763] |
| `graph_cleanup_keys` | function | Returns a vector of five static string keys used for graph cleanup metadata: 'status', 'action', 'project_id', 'stale_graph_files_deleted', and 'graph_nodes_deleted'. [crates/gcode/src/contract.rs:765-773] |
| `graph_report_keys` | function | Returns a vector of the five static report field keys: 'project_id', 'summary', 'hotspots', 'bridges', and 'degraded'. [crates/gcode/src/contract.rs:775-777] |
| `vector_lifecycle_keys` | function | Returns a static vector of lifecycle metric and status field names used to report vector processing outcomes, including success, errors, sync counts, deletions, and summary data. [crates/gcode/src/contract.rs:779-799] |
| `vector_cleanup_keys` | function | Returns a 'Vec<&'static str>' listing the cleanup-related field keys: 'project_id', 'projection', 'action', 'collection', 'status', 'vector_files_scanned', 'orphan_files_deleted', 'vectors_deleted', and 'summary'. [crates/gcode/src/contract.rs:801-813] |
| `embeddings_doctor_keys` | function | Returns a static vector of the embeddings doctor field names: 'status', 'project_id', 'source', 'model', 'vector_dim', 'peer', and 'drift'. [crates/gcode/src/contract.rs:815-825] |

