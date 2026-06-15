---
title: crates/gcode/src/graph/code_graph/write/mutation.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/write/mutation.rs
  ranges:
  - 89-96
  - 99-102
  - 105-112
  - 115-119
  - 121-128
  - 130-145
  - 147-152
  - 154-182
  - 184-197
  - 199-207
  - 209-227
  - 229-259
  - 261-295
  - 297-301
  - 303-335
  - 337-343
  - 345-364
  - 366-377
  - 379-390
  - 392-403
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/write/mutation.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/write|crates/gcode/src/graph/code_graph/write]]

## Purpose

Builds the mutation-side write path for syncing a file’s code graph into the database. It prepares stable sync tokens, filters and shapes imports, definitions, and call relations into typed parameter values, and assembles the Cypher queries that upsert the file node and write `IMPORTS`, `DEFINES`, `CALLS`, and unresolved call records.

The helper types and functions work together by normalizing raw model data into graph-ready rows: `GraphCallTarget` classifies call targets, `CallGraphItems` groups them by resolution status, `map_value` and the row builders serialize them into `TypedValue` structures, and `SyncFileMutation` carries the full per-file payload plus metadata needed by the query builders.
[crates/gcode/src/graph/code_graph/write/mutation.rs:89-96]
[crates/gcode/src/graph/code_graph/write/mutation.rs:99-102]
[crates/gcode/src/graph/code_graph/write/mutation.rs:105-112]
[crates/gcode/src/graph/code_graph/write/mutation.rs:115-119]
[crates/gcode/src/graph/code_graph/write/mutation.rs:121-128]

## API Symbols

- `new_sync_token` (function) component `new_sync_token [function]` (`a8869846-a57f-5abe-b587-24741c8f8413`) lines 89-96 [crates/gcode/src/graph/code_graph/write/mutation.rs:89-96]
  - Signature: `pub(super) fn new_sync_token(file_path: &str) -> String {`
  - Purpose: Builds a synchronization token string of the form '"<pid>:<file_path>:<unix_nanos>:<monotonic_counter>"', using the current system time in nanoseconds since the Unix epoch (or '0' if unavailable) and a relaxed atomic counter to ensure uniqueness. [crates/gcode/src/graph/code_graph/write/mutation.rs:89-96]
- `ImportGraphItem` (class) component `ImportGraphItem [class]` (`e3e21d69-34de-5bf8-ae87-3af3bb621bf4`) lines 99-102 [crates/gcode/src/graph/code_graph/write/mutation.rs:99-102]
  - Signature: `pub(in crate::graph::code_graph) struct ImportGraphItem {`
  - Purpose: 'ImportGraphItem' is a crate-internal code-graph node representing a module import relationship, storing the source file path and the imported target module as 'String' fields. [crates/gcode/src/graph/code_graph/write/mutation.rs:99-102]
- `CallGraphItem` (class) component `CallGraphItem [class]` (`8216b71e-91cc-5459-a595-ef65977a27c2`) lines 105-112 [crates/gcode/src/graph/code_graph/write/mutation.rs:105-112]
  - Signature: `pub(in crate::graph::code_graph) struct CallGraphItem {`
  - Purpose: 'CallGraphItem' is an internal code-graph record that represents a single call-site edge by storing the caller and target identifiers, callee name, source file path and line number, and an optional callee module name. [crates/gcode/src/graph/code_graph/write/mutation.rs:105-112]
- `CallGraphItems` (class) component `CallGraphItems [class]` (`ad9a643c-cae1-5944-b160-e3c7e4145c8b`) lines 115-119 [crates/gcode/src/graph/code_graph/write/mutation.rs:115-119]
  - Signature: `pub(in crate::graph::code_graph) struct CallGraphItems {`
  - Purpose: 'CallGraphItems' is an internal 'code_graph' container that groups call-graph entries into three vectors: 'symbol', 'external', and 'unresolved'. [crates/gcode/src/graph/code_graph/write/mutation.rs:115-119]
- `map_value` (function) component `map_value [function]` (`8b3d881e-e34f-545a-9757-873171c9dc1c`) lines 121-128 [crates/gcode/src/graph/code_graph/write/mutation.rs:121-128]
  - Signature: `fn map_value(values: impl IntoIterator<Item = (&'static str, TypedValue)>) -> TypedValue {`
  - Purpose: Constructs a 'TypedValue::Map' by consuming an iterator of '(&'static str, TypedValue)' pairs, converting each key to an owned 'String', and collecting them into a 'BTreeMap'. [crates/gcode/src/graph/code_graph/write/mutation.rs:121-128]
- `import_graph_items` (function) component `import_graph_items [function]` (`fe32193e-e656-514f-a57c-f045363d9b2b`) lines 130-145 [crates/gcode/src/graph/code_graph/write/mutation.rs:130-145]
  - Signature: `pub(in crate::graph::code_graph) fn import_graph_items(`
  - Purpose: Builds a 'Vec<ImportGraphItem>' from the given 'imports' by filtering out entries with empty module names or names starting with 'UNPARSED_IMPORT_PREFIX', then mapping each remaining import to an item whose 'source_file' is 'file_path' and 'target_module' is the import’s 'module_name'. [crates/gcode/src/graph/code_graph/write/mutation.rs:130-145]
- `definition_graph_symbols` (function) component `definition_graph_symbols [function]` (`eef347a6-d2c4-5db3-bbca-9ccdbd799044`) lines 147-152 [crates/gcode/src/graph/code_graph/write/mutation.rs:147-152]
  - Signature: `pub(super) fn definition_graph_symbols(definitions: &[Symbol]) -> Vec<&Symbol> {`
  - Purpose: Returns a vector of references to the input 'Symbol' values whose 'id' and 'name' fields are both non-empty, preserving their original order. [crates/gcode/src/graph/code_graph/write/mutation.rs:147-152]
- `partition_call_graph_items` (function) component `partition_call_graph_items [function]` (`40662a74-88c2-596a-82a7-59ee84497227`) lines 154-182 [crates/gcode/src/graph/code_graph/write/mutation.rs:154-182]
  - Signature: `pub(in crate::graph::code_graph) fn partition_call_graph_items(`
  - Purpose: Partitions a slice of 'CallRelation's into a 'CallGraphItems' collection by filtering out calls without a caller symbol, converting each remaining call into a 'GraphCallTarget', building a 'CallGraphItem' with the caller, target, callee name, source file, line, and optional module, and appending it to the 'symbol', 'external', or 'unresolved' bucket based on the target variant. [crates/gcode/src/graph/code_graph/write/mutation.rs:154-182]
- `metadata_params` (function) component `metadata_params [function]` (`d728f3c4-1807-51af-b706-28a7394d375d`) lines 184-197 [crates/gcode/src/graph/code_graph/write/mutation.rs:184-197]
  - Signature: `fn metadata_params(sync_token: &str) -> Vec<(&'static str, TypedValue)> {`
  - Purpose: Constructs and returns a vector of metadata key-value pairs containing fixed 'provenance', 'confidence', and 'source_system' entries plus the dynamic 'sync_token' parameter from 'sync_token_param(sync_token)'. [crates/gcode/src/graph/code_graph/write/mutation.rs:184-197]
- `SyncFileMutation` (class) component `SyncFileMutation [class]` (`015f1eff-b334-5337-a893-bad0353001c2`) lines 199-207 [crates/gcode/src/graph/code_graph/write/mutation.rs:199-207]
  - Signature: `pub(super) struct SyncFileMutation<'a> {`
  - Purpose: 'SyncFileMutation<'a>' is a borrowed data carrier describing a file-level synchronization mutation for a project, including its project and path identifiers, symbol and import metadata, call graph items, and the associated sync token. [crates/gcode/src/graph/code_graph/write/mutation.rs:199-207]
- `ensure_file_node_query` (function) component `ensure_file_node_query [function]` (`d596eb39-fdeb-594f-9cc0-ec5a6e6a740f`) lines 209-227 [crates/gcode/src/graph/code_graph/write/mutation.rs:209-227]
  - Signature: `pub(super) fn ensure_file_node_query(`
  - Purpose: Builds a typed Cypher 'MERGE' query that upserts a 'CodeFile' node keyed by 'path' and 'project', then updates its 'updated_at', 'symbol_count', and 'sync_token' fields using the provided parameters. [crates/gcode/src/graph/code_graph/write/mutation.rs:209-227]
- `add_imports_query` (function) component `add_imports_query [function]` (`49f95909-a463-50da-9751-9357d42e4a2f`) lines 229-259 [crates/gcode/src/graph/code_graph/write/mutation.rs:229-259]
  - Signature: `pub(super) fn add_imports_query(`
  - Purpose: Builds a 'TypedQuery' for the 'ADD_IMPORTS_CYPHER' statement by packaging 'project_id', a list of import records mapped to 'source_file' and 'target_module', and sync metadata derived from 'sync_token'. [crates/gcode/src/graph/code_graph/write/mutation.rs:229-259]
- `add_definitions_query` (function) component `add_definitions_query [function]` (`9562a0f8-11b8-5d5e-b3bb-b654cbd0572f`) lines 261-295 [crates/gcode/src/graph/code_graph/write/mutation.rs:261-295]
  - Signature: `pub(super) fn add_definitions_query(`
  - Purpose: Builds a 'TypedQuery' for the 'ADD_DEFINITIONS_CYPHER' Cypher statement by serializing the given project, file path, symbol list, and sync token into typed parameters, returning an error if any symbol field conversion fails. [crates/gcode/src/graph/code_graph/write/mutation.rs:261-295]
- `GraphCallTarget` (type) component `GraphCallTarget [type]` (`a9c5b35c-0d08-53bc-a4a5-99529cc5ef5d`) lines 297-301 [crates/gcode/src/graph/code_graph/write/mutation.rs:297-301]
  - Signature: `enum GraphCallTarget {`
  - Purpose: Indexed type `GraphCallTarget` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:297-301]
- `GraphCallTarget` (class) component `GraphCallTarget [class]` (`5748128b-81eb-52f2-8b31-5bc97e6152c8`) lines 303-335 [crates/gcode/src/graph/code_graph/write/mutation.rs:303-335]
  - Signature: `impl GraphCallTarget {`
  - Purpose: 'GraphCallTarget' is an enum-like wrapper that derives a call target from a 'CallRelation' as a resolved symbol, external symbol, or unresolved identifier, and exposes its stable 'id' plus optional external 'module'. [crates/gcode/src/graph/code_graph/write/mutation.rs:303-335]
- `GraphCallTarget.from_call` (method) component `GraphCallTarget.from_call [method]` (`f301e8b4-d050-5e98-98c3-a2e160c9bdef`) lines 304-321 [crates/gcode/src/graph/code_graph/write/mutation.rs:304-321]
  - Signature: `fn from_call(project_id: &str, call: &CallRelation) -> Option<Self> {`
  - Purpose: Constructs an optional callee reference by preferring a non-empty symbol ID as 'Symbol', otherwise returning 'None' for empty names, mapping external callees to an 'External' identifier via 'project_id' and module, and falling back to an 'Unresolved' identifier for all other named callees. [crates/gcode/src/graph/code_graph/write/mutation.rs:304-321]
- `GraphCallTarget.id` (method) component `GraphCallTarget.id [method]` (`1dc09ea5-212b-5bf0-a7f1-5f2eef72080a`) lines 323-327 [crates/gcode/src/graph/code_graph/write/mutation.rs:323-327]
  - Signature: `fn id(&self) -> &str {`
  - Purpose: Returns the 'id' string slice from the enum variant, matching 'Symbol', 'External', or 'Unresolved' and borrowing the stored 'id' field. [crates/gcode/src/graph/code_graph/write/mutation.rs:323-327]
- `GraphCallTarget.module` (method) component `GraphCallTarget.module [method]` (`fb33098b-c1b2-5dc2-b9a4-3cbd8c6bc2ff`) lines 329-334 [crates/gcode/src/graph/code_graph/write/mutation.rs:329-334]
  - Signature: `fn module(&self) -> Option<&str> {`
  - Purpose: Returns the module name for 'External' variants and 'None' for 'Symbol' and 'Unresolved' variants. [crates/gcode/src/graph/code_graph/write/mutation.rs:329-334]
- `call_target_id` (function) component `call_target_id [function]` (`ce402677-421b-5686-b1eb-4949c37daeff`) lines 337-343 [crates/gcode/src/graph/code_graph/write/mutation.rs:337-343]
  - Signature: `pub fn call_target_id(project_id: &str, call: &CallRelation) -> Option<String> {`
  - Purpose: Returns the target identifier from a 'CallRelation' by converting it to a 'GraphCallTarget' for the given 'project_id' and extracting the 'id' from symbol, external, or unresolved targets, otherwise yielding 'None'. [crates/gcode/src/graph/code_graph/write/mutation.rs:337-343]
- `call_rows` (function) component `call_rows [function]` (`ad187869-a667-5a5e-9799-d546b2844cb5`) lines 345-364 [crates/gcode/src/graph/code_graph/write/mutation.rs:345-364]
  - Signature: `fn call_rows(calls: &[CallGraphItem]) -> anyhow::Result<TypedValue> {`
  - Purpose: Builds a 'TypedValue::List' of mapped row objects from 'calls', where each row contains 'caller_id', 'target_id', 'callee_name', 'file_path', 'line', and 'callee_module' fields cloned from each 'CallGraphItem', returning any conversion error encountered. [crates/gcode/src/graph/code_graph/write/mutation.rs:345-364]
- `add_symbol_calls_query` (function) component `add_symbol_calls_query [function]` (`4e2fbd55-4044-59e2-9786-dde50ef49b0c`) lines 366-377 [crates/gcode/src/graph/code_graph/write/mutation.rs:366-377]
  - Signature: `pub(super) fn add_symbol_calls_query(`
  - Purpose: Builds a typed Cypher query for inserting symbol-call rows by packaging the 'project_id', serialized 'calls', and sync-token metadata into parameter values and passing them to 'typed_query' with 'ADD_SYMBOL_CALLS_CYPHER'. [crates/gcode/src/graph/code_graph/write/mutation.rs:366-377]
- `add_external_calls_query` (function) component `add_external_calls_query [function]` (`725a13c0-675c-5b80-9cc9-dc1245885fa9`) lines 379-390 [crates/gcode/src/graph/code_graph/write/mutation.rs:379-390]
  - Signature: `pub(super) fn add_external_calls_query(`
  - Purpose: Builds a typed Cypher query for inserting external call graph rows by packaging the 'project_id', serialized 'calls', and sync-token metadata into parameters and passing them to 'typed_query'. [crates/gcode/src/graph/code_graph/write/mutation.rs:379-390]
- `add_unresolved_calls_query` (function) component `add_unresolved_calls_query [function]` (`9d5c3fe6-de55-5101-a01d-48284fc003ee`) lines 392-403 [crates/gcode/src/graph/code_graph/write/mutation.rs:392-403]
  - Signature: `pub(super) fn add_unresolved_calls_query(`
  - Purpose: Builds a 'TypedQuery' for the 'ADD_UNRESOLVED_CALLS_CYPHER' Cypher statement by packaging the 'project_id', serialized unresolved call rows from 'calls', and sync-token metadata into typed parameters, propagating any error from 'call_rows(calls)'. [crates/gcode/src/graph/code_graph/write/mutation.rs:392-403]

