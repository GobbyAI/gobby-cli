---
title: crates/gcode/src/graph/code_graph/write/mutation.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/write/mutation.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/write/mutation.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/graph/code_graph/write/mutation.rs` exposes 24 indexed API symbols.

## How it fits

`crates/gcode/src/graph/code_graph/write/mutation.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `new_sync_token` | function | Generates a synchronization token string by combining the current process ID, the provided file path, the current UNIX timestamp in nanoseconds, and a monotonically incrementing atomic counter. [crates/gcode/src/graph/code_graph/write/mutation.rs:89-96] |
| `ImportGraphItem` | class | 'ImportGraphItem' is a crate-internal code-graph record that stores the importing source file path and the imported target module as 'String' values. [crates/gcode/src/graph/code_graph/write/mutation.rs:99-102] |
| `CallGraphItem` | class | 'CallGraphItem' is a crate-internal code-graph record that identifies a call-site by caller and target IDs, callee name, source file path and line number, with an optional callee module. [crates/gcode/src/graph/code_graph/write/mutation.rs:105-112] |
| `CallGraphItems` | class | 'CallGraphItems' is an internal code-graph container that partitions 'CallGraphItem' values into three vectors: 'symbol' for resolved symbols, 'external' for external targets, and 'unresolved' for calls that could not be resolved. [crates/gcode/src/graph/code_graph/write/mutation.rs:115-119] |
| `map_value` | function | Constructs a 'TypedValue::Map' by consuming an iterator of '(&'static str, TypedValue)' pairs, converting each key to an owned 'String', and collecting the entries into a 'BTreeMap'. [crates/gcode/src/graph/code_graph/write/mutation.rs:121-128] |
| `import_graph_items` | function | Builds a 'Vec<ImportGraphItem>' from the given 'imports' by keeping only relations whose 'module_name' is nonempty and does not start with 'UNPARSED_IMPORT_PREFIX', then mapping each to an item with 'source_file' set to 'file_path' and 'target_module' cloned from the import. [crates/gcode/src/graph/code_graph/write/mutation.rs:130-145] |
| `definition_graph_symbols` | function | Returns references to the subset of 'definitions' whose 'id' and 'name' fields are both non-empty, preserving the original order. [crates/gcode/src/graph/code_graph/write/mutation.rs:147-152] |
| `partition_call_graph_items` | function | Partitions a slice of 'CallRelation' records into a 'CallGraphItems' collection by skipping entries without a caller symbol, deriving a 'GraphCallTarget' for each remaining call, constructing a 'CallGraphItem' with caller/target metadata and source location, and grouping the items into 'symbol', 'external', or 'unresolved' buckets based on the target variant. [crates/gcode/src/graph/code_graph/write/mutation.rs:154-182] |
| `metadata_params` | function | Constructs and returns a 'Vec' of metadata key-value pairs containing fixed provenance, confidence, and source system entries plus the 'sync_token' parameter produced by 'sync_token_param(sync_token)'. [crates/gcode/src/graph/code_graph/write/mutation.rs:184-197] |
| `SyncFileMutation` | class | 'SyncFileMutation<'a>' is a borrowed data carrier describing a project file synchronization mutation, including the target project and file path, symbol count, import and symbol references, call-graph items, and a sync token. [crates/gcode/src/graph/code_graph/write/mutation.rs:199-207] |
| `ensure_file_node_query` | function | Builds a parameterized Cypher 'MERGE' query that upserts a 'CodeFile' node keyed by 'path' and 'project', then updates its 'updated_at', 'symbol_count', and 'sync_token' fields. [crates/gcode/src/graph/code_graph/write/mutation.rs:209-227] |
| `add_imports_query` | function | Builds a 'TypedQuery' for the 'ADD_IMPORTS_CYPHER' Cypher statement by assembling 'project', a list of 'imports' mapped to 'source_file'/'target_module' values, appending metadata from 'sync_token', and returning the typed query result. [crates/gcode/src/graph/code_graph/write/mutation.rs:229-259] |
| `add_definitions_query` | function | Builds a 'TypedQuery' for the 'ADD_DEFINITIONS_CYPHER' Cypher statement by serializing the project ID, file path, a list of symbol records, and sync-token metadata into typed parameters. [crates/gcode/src/graph/code_graph/write/mutation.rs:261-295] |
| `GraphCallTarget` | type | Indexed type `GraphCallTarget` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:297-301] |
| `GraphCallTarget::from_call` | method | 'from_call' converts a 'CallRelation' into an 'Option<Self>' by preferring a non-empty 'callee_symbol_id' as 'Symbol', returning 'None' when 'callee_name' is empty, mapping external callees to 'External' using a generated external symbol ID and module name, and otherwise producing an 'Unresolved' callee ID. [crates/gcode/src/graph/code_graph/write/mutation.rs:304-321] |
| `GraphCallTarget::id` | method | Returns a shared '&str' reference to the 'id' field of the enum, regardless of whether the variant is 'Symbol', 'External', or 'Unresolved'. [crates/gcode/src/graph/code_graph/write/mutation.rs:323-327] |
| `GraphCallTarget::module` | method | Returns the external module name as 'Some(&str)' when 'self' is 'External', and 'None' for 'Symbol' or 'Unresolved' variants. [crates/gcode/src/graph/code_graph/write/mutation.rs:329-334] |
| `call_target_id` | function | Returns the target identifier from a 'CallRelation' for the given 'project_id' by converting it to a 'GraphCallTarget' and extracting the 'id' for symbol, external, or unresolved targets, otherwise yielding 'None'. [crates/gcode/src/graph/code_graph/write/mutation.rs:337-343] |
| `call_rows` | function | Converts a slice of 'CallGraphItem' records into a 'TypedValue::List' of mapped row objects containing 'caller_id', 'target_id', 'callee_name', 'file_path', 'line', and 'callee_module', propagating any conversion error via 'anyhow::Result'. [crates/gcode/src/graph/code_graph/write/mutation.rs:345-364] |
| `add_symbol_calls_query` | function | Builds and returns a 'TypedQuery' for the 'ADD_SYMBOL_CALLS_CYPHER' Cypher statement by packaging the 'project_id', serialized 'calls' rows, and sync-token metadata into typed parameters. [crates/gcode/src/graph/code_graph/write/mutation.rs:366-377] |
| `add_external_calls_query` | function | Builds a typed Cypher query for adding external call graph rows by packaging the project ID, serialized call rows, and sync-token metadata into parameters and passing them to 'typed_query'. [crates/gcode/src/graph/code_graph/write/mutation.rs:379-390] |
| `add_unresolved_calls_query` | function | Builds a typed Cypher query for 'ADD_UNRESOLVED_CALLS_CYPHER' by packaging the project ID, serialized unresolved call rows, and sync-token metadata into query parameters. [crates/gcode/src/graph/code_graph/write/mutation.rs:392-403] |

_Verified by 2 in-file unit tests._

