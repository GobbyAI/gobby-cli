---
title: crates/gwiki/src/code_graph.rs
type: code_file
provenance:
- file: crates/gwiki/src/code_graph.rs
  ranges:
  - 15-18
  - 21-28
  - 31-34
  - 37-40
  - 43-47
  - 49-68
  - 70-79
  - 81-124
  - 126-132
  - 134-162
  - 164-167
  - 169-172
  - 174-181
  - 183-194
  - 196-208
  - 210-220
  - 222-243
  - 245-249
  - 251-253
  - 255-260
  - 262-275
  - 277-291
  - 299-301
  - 304-315
  - 318-331
  - 334-345
  - 348-356
  - 359-424
  - 427-466
  - 469-492
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/code_graph.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file provides the code-graph layer for gwiki: it queries a Falkor-backed graph for file or symbol relationships, converts raw rows into structured `CodeGraphEdge` records, and wraps service availability into degradation signals. It also defines change-set and affected-page models, then uses them to map modified files and symbols through the code graph and a provenance graph to the pages that should be refreshed. Helper functions handle query construction, row extraction, path/source normalization, and graceful fallback when graph data is unavailable or malformed.
[crates/gwiki/src/code_graph.rs:15-18]
[crates/gwiki/src/code_graph.rs:21-28]
[crates/gwiki/src/code_graph.rs:31-34]
[crates/gwiki/src/code_graph.rs:37-40]
[crates/gwiki/src/code_graph.rs:43-47]

## API Symbols

- `CodeGraphQuery` (type) component `CodeGraphQuery [type]` (`02a6dda9-f7e6-5f66-b0e9-16f966ef7fca`) lines 15-18 [crates/gwiki/src/code_graph.rs:15-18]
  - Signature: `pub(crate) enum CodeGraphQuery<'a> {`
  - Purpose: Indexed type `CodeGraphQuery` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:15-18]
- `CodeGraphEdge` (class) component `CodeGraphEdge [class]` (`b19ec23b-3628-55b6-851e-330115b9126f`) lines 21-28 [crates/gwiki/src/code_graph.rs:21-28]
  - Signature: `pub(crate) struct CodeGraphEdge {`
  - Purpose: Indexed class `CodeGraphEdge` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:21-28]
- `CodeChangeSet` (class) component `CodeChangeSet [class]` (`8dd5edc0-cf47-5129-bf9c-6c56da291135`) lines 31-34 [crates/gwiki/src/code_graph.rs:31-34]
  - Signature: `pub(crate) struct CodeChangeSet {`
  - Purpose: Indexed class `CodeChangeSet` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:31-34]
- `AffectedPages` (class) component `AffectedPages [class]` (`88869721-4a0d-53cc-8bf0-544fd9d69b2a`) lines 37-40 [crates/gwiki/src/code_graph.rs:37-40]
  - Signature: `pub(crate) struct AffectedPages {`
  - Purpose: Indexed class `AffectedPages` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:37-40]
- `AffectedPage` (class) component `AffectedPage [class]` (`4f132b0e-12ae-5ddd-b114-dca2fa47d5c2`) lines 43-47 [crates/gwiki/src/code_graph.rs:43-47]
  - Signature: `pub(crate) struct AffectedPage {`
  - Purpose: Indexed class `AffectedPage` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:43-47]
- `code_edges` (function) component `code_edges [function]` (`f71a3e0b-10e4-5a6e-91f0-039ee8971b85`) lines 49-68 [crates/gwiki/src/code_graph.rs:49-68]
  - Signature: `pub(crate) fn code_edges(`
  - Purpose: Indexed function `code_edges` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:49-68]
- `affected_pages_for_changes` (function) component `affected_pages_for_changes [function]` (`efef1146-2082-5d21-bc79-cff80f079c3e`) lines 70-79 [crates/gwiki/src/code_graph.rs:70-79]
  - Signature: `pub(crate) fn affected_pages_for_changes(`
  - Purpose: Indexed function `affected_pages_for_changes` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:70-79]
- `affected_pages_for_changes_with_edges` (function) component `affected_pages_for_changes_with_edges [function]` (`05db4a51-6183-5b68-b2d6-c28abf484348`) lines 81-124 [crates/gwiki/src/code_graph.rs:81-124]
  - Signature: `fn affected_pages_for_changes_with_edges(`
  - Purpose: Indexed function `affected_pages_for_changes_with_edges` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:81-124]
- `add_edge_paths` (function) component `add_edge_paths [function]` (`f726c6d8-3d1a-578b-8830-07bc25776d33`) lines 126-132 [crates/gwiki/src/code_graph.rs:126-132]
  - Signature: `fn add_edge_paths(target_paths: &mut BTreeSet<PathBuf>, edges: Vec<CodeGraphEdge>) {`
  - Purpose: Indexed function `add_edge_paths` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:126-132]
- `affected_pages_for_targets` (function) component `affected_pages_for_targets [function]` (`18d1ad64-f2b2-5d96-a3e8-288b4403183e`) lines 134-162 [crates/gwiki/src/code_graph.rs:134-162]
  - Signature: `fn affected_pages_for_targets(`
  - Purpose: Indexed function `affected_pages_for_targets` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:134-162]
- `normalized_path` (function) component `normalized_path [function]` (`014e0680-4a8e-5f2d-88da-3e53a9d29133`) lines 164-167 [crates/gwiki/src/code_graph.rs:164-167]
  - Signature: `fn normalized_path(path: &str) -> Option<PathBuf> {`
  - Purpose: Indexed function `normalized_path` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:164-167]
- `normalized_source_id` (function) component `normalized_source_id [function]` (`283bbe06-5f04-5762-8e5d-9e0d8acc2aa9`) lines 169-172 [crates/gwiki/src/code_graph.rs:169-172]
  - Signature: `fn normalized_source_id(source_id: &str) -> Option<String> {`
  - Purpose: Indexed function `normalized_source_id` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:169-172]
- `query_edges` (function) component `query_edges [function]` (`ee9c8d25-f29b-5867-9f4e-affeedec2d32`) lines 174-181 [crates/gwiki/src/code_graph.rs:174-181]
  - Signature: `fn query_edges(`
  - Purpose: Indexed function `query_edges` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:174-181]
- `query_params` (function) component `query_params [function]` (`a8186e8d-9368-571a-ad01-7cff32689680`) lines 183-194 [crates/gwiki/src/code_graph.rs:183-194]
  - Signature: `fn query_params(project: &str, target: CodeGraphQuery<'_>) -> HashMap<String, String> {`
  - Purpose: Indexed function `query_params` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:183-194]
- `edge_from_row` (function) component `edge_from_row [function]` (`f987f790-3c88-508b-b3b0-34dd6577ee60`) lines 196-208 [crates/gwiki/src/code_graph.rs:196-208]
  - Signature: `fn edge_from_row(row: Row) -> Option<CodeGraphEdge> {`
  - Purpose: Indexed function `edge_from_row` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:196-208]
- `required_row_string` (function) component `required_row_string [function]` (`1c9c3a79-cd98-59e7-9624-82bbf8cb14c3`) lines 210-220 [crates/gwiki/src/code_graph.rs:210-220]
  - Signature: `fn required_row_string(row: &Row, key: &str) -> Option<String> {`
  - Purpose: Indexed function `required_row_string` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:210-220]
- `degradation_key` (function) component `degradation_key [function]` (`8e670478-f729-5c3e-8d95-e065bcf5a778`) lines 222-243 [crates/gwiki/src/code_graph.rs:222-243]
  - Signature: `fn degradation_key(degradation: &DegradationKind) -> String {`
  - Purpose: Indexed function `degradation_key` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:222-243]
- `row_string` (function) component `row_string [function]` (`6b0715d0-803a-5c96-bc16-1fbd9d02fcbf`) lines 245-249 [crates/gwiki/src/code_graph.rs:245-249]
  - Signature: `fn row_string(row: &Row, key: &str) -> Option<String> {`
  - Purpose: Indexed function `row_string` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:245-249]
- `row_i64` (function) component `row_i64 [function]` (`e82715a1-6afc-5c3e-a93f-2a1adef13485`) lines 251-253 [crates/gwiki/src/code_graph.rs:251-253]
  - Signature: `fn row_i64(row: &Row, key: &str) -> Option<i64> {`
  - Purpose: Indexed function `row_i64` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:251-253]
- `graph_query` (function) component `graph_query [function]` (`e3c96ea3-b66a-5435-b263-9a48e62fa723`) lines 255-260 [crates/gwiki/src/code_graph.rs:255-260]
  - Signature: `fn graph_query(target: CodeGraphQuery<'_>) -> String {`
  - Purpose: Indexed function `graph_query` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:255-260]
- `file_graph_query` (function) component `file_graph_query [function]` (`d8580b0d-3507-5afa-b39f-81a89cbd8458`) lines 262-275 [crates/gwiki/src/code_graph.rs:262-275]
  - Signature: `fn file_graph_query() -> String {`
  - Purpose: Indexed function `file_graph_query` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:262-275]
- `symbol_graph_query` (function) component `symbol_graph_query [function]` (`92570571-540b-538d-b91f-5f0c5857e7f4`) lines 277-291 [crates/gwiki/src/code_graph.rs:277-291]
  - Signature: `fn symbol_graph_query() -> String {`
  - Purpose: Indexed function `symbol_graph_query` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:277-291]
- `code_graph_name_matches_gcode_projection` (function) component `code_graph_name_matches_gcode_projection [function]` (`d298db94-7ff4-540a-8a10-1ea8fbbbb2ba`) lines 299-301 [crates/gwiki/src/code_graph.rs:299-301]
  - Signature: `fn code_graph_name_matches_gcode_projection() {`
  - Purpose: Indexed function `code_graph_name_matches_gcode_projection` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:299-301]
- `malformed_graph_rows_are_skipped` (function) component `malformed_graph_rows_are_skipped [function]` (`4e44503d-2fee-59fe-b203-24217a786996`) lines 304-315 [crates/gwiki/src/code_graph.rs:304-315]
  - Signature: `fn malformed_graph_rows_are_skipped() {`
  - Purpose: Indexed function `malformed_graph_rows_are_skipped` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:304-315]
- `unavailable_graph_degrades_to_empty_edges` (function) component `unavailable_graph_degrades_to_empty_edges [function]` (`4eff1e86-ac27-5f66-8f78-4b0dd64676bf`) lines 318-331 [crates/gwiki/src/code_graph.rs:318-331]
  - Signature: `fn unavailable_graph_degrades_to_empty_edges() {`
  - Purpose: Indexed function `unavailable_graph_degrades_to_empty_edges` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:318-331]
- `file_query_reads_imports_definitions_calls_and_callers` (function) component `file_query_reads_imports_definitions_calls_and_callers [function]` (`40a67e09-999c-5571-8697-e2acc393005f`) lines 334-345 [crates/gwiki/src/code_graph.rs:334-345]
  - Signature: `fn file_query_reads_imports_definitions_calls_and_callers() {`
  - Purpose: Indexed function `file_query_reads_imports_definitions_calls_and_callers` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:334-345]
- `symbol_query_reads_calls_and_callers` (function) component `symbol_query_reads_calls_and_callers [function]` (`7194d89d-2cc3-5ee2-8832-1fc009e0d4d3`) lines 348-356 [crates/gwiki/src/code_graph.rs:348-356]
  - Signature: `fn symbol_query_reads_calls_and_callers() {`
  - Purpose: Indexed function `symbol_query_reads_calls_and_callers` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:348-356]
- `change_triggered_refresh_maps_changed_files_through_graph_and_provenance` (function) component `change_triggered_refresh_maps_changed_files_through_graph_and_provenance [function]` (`67c1e400-bf17-5b6b-95cf-4d0a80c54eb3`) lines 359-424 [crates/gwiki/src/code_graph.rs:359-424]
  - Signature: `fn change_triggered_refresh_maps_changed_files_through_graph_and_provenance() {`
  - Purpose: Indexed function `change_triggered_refresh_maps_changed_files_through_graph_and_provenance` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:359-424]
- `change_triggered_refresh_degrades_to_provenance_only_mapping` (function) component `change_triggered_refresh_degrades_to_provenance_only_mapping [function]` (`1512a28d-f7e5-5060-a178-d4f66cc88327`) lines 427-466 [crates/gwiki/src/code_graph.rs:427-466]
  - Signature: `fn change_triggered_refresh_degrades_to_provenance_only_mapping() {`
  - Purpose: Indexed function `change_triggered_refresh_degrades_to_provenance_only_mapping` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:427-466]
- `duplicate_degradations_are_deduped_after_all_queries_run` (function) component `duplicate_degradations_are_deduped_after_all_queries_run [function]` (`2b4c6820-40bf-5e2c-8872-ad648f825a8b`) lines 469-492 [crates/gwiki/src/code_graph.rs:469-492]
  - Signature: `fn duplicate_degradations_are_deduped_after_all_queries_run() {`
  - Purpose: Indexed function `duplicate_degradations_are_deduped_after_all_queries_run` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:469-492]

