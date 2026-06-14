---
title: crates/gcode/src/graph/code_graph/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/tests.rs
  ranges:
  - 7-21
  - 24-33
  - 36-65
  - 68-151
  - 154-159
  - 162-189
  - 192-198
  - 201-218
  - 221-237
  - 240-245
  - 248-252
  - 255-269
  - 272-282
  - 285-324
  - 327-374
  - 377-396
  - 399-409
  - 412-439
  - 442-454
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/tests.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Purpose

This test file validates the code_graph module's core functionality through a suite of unit tests. It provides a `test_context` helper that instantiates a Context struct with test configuration values, then exercises multiple aspects of code graph operations:

The tests verify data integrity by checking that code edge metadata (provenance, confidence, source file path, line numbers) is correctly extracted and preserved through serialization and GraphPayload transformations. They validate query generation by asserting that SQL and Cypher queries use proper column aliasing to prevent shadowing, maintain distinct metadata field references, and employ correct filtering patterns.

The tests ensure safety constraints including project-scoped operations (all deletions and cleanup queries filter by project ID), label targeting (distinguishing code index labels from memory graph labels), and selective preservation (stale symbols are deleted while current symbols are retained through parameterized ID filters). They also verify graceful degradation—when FalkorDB is not configured, read guards fail strictly while public query APIs return empty responses rather than erroring.

Additional tests confirm support operations like row deduplication by node_id with distance minimization, UTF-8 boundary-aware string truncation, undirected graph traversal patterns for import relationships, and filtering of unparsed imports marked with sentinel prefixes. Together, these tests ensure the code_graph module correctly manages code structure metadata, generates safe parameterized queries, and handles edge cases without compromising data consistency.
[crates/gcode/src/graph/code_graph/tests.rs:7-21]
[crates/gcode/src/graph/code_graph/tests.rs:24-33]
[crates/gcode/src/graph/code_graph/tests.rs:36-65]
[crates/gcode/src/graph/code_graph/tests.rs:68-151]
[crates/gcode/src/graph/code_graph/tests.rs:154-159]

## API Symbols

- `test_context` (function) component `test_context [function]` (`6ada5f13-a01c-502f-a972-3217233985d9`) lines 7-21 [crates/gcode/src/graph/code_graph/tests.rs:7-21]
  - Signature: `fn test_context(falkordb: Option<crate::config::FalkorConfig>) -> Context {`
  - Purpose: Instantiates a `Context` struct with hardcoded test configuration values (nonexistent PostgreSQL URL, temporary project root, and test project ID) and an optional FalkorDB configuration parameter. [crates/gcode/src/graph/code_graph/tests.rs:7-21]
- `code_edges_carry_provenance` (function) component `code_edges_carry_provenance [function]` (`997a6ff7-0182-55be-a78f-6a99981cb933`) lines 24-33 [crates/gcode/src/graph/code_graph/tests.rs:24-33]
  - Signature: `fn code_edges_carry_provenance() {`
  - Purpose: Tests that code edge metadata extraction correctly preserves provenance information including source file path, line number, symbol identifier, confidence level, and code generation system origin. [crates/gcode/src/graph/code_graph/tests.rs:24-33]
- `read_apis_return_node_link_payloads_with_link_metadata` (function) component `read_apis_return_node_link_payloads_with_link_metadata [function]` (`db7e66a2-5c4e-51ca-9ce3-cbe0a451bada`) lines 36-65 [crates/gcode/src/graph/code_graph/tests.rs:36-65]
  - Signature: `fn read_apis_return_node_link_payloads_with_link_metadata() {`
  - Purpose: Validates that GraphPayload correctly serializes a file node and symbol-definition link while preserving metadata attributes (provenance, source_system, confidence) in a nested JSON structure. [crates/gcode/src/graph/code_graph/tests.rs:36-65]
- `graph_read_guard_stays_strict_but_public_reads_degrade_without_service` (function) component `graph_read_guard_stays_strict_but_public_reads_degrade_without_service [function]` (`b5fc4fd1-546f-5a04-a606-0290158634ec`) lines 68-151 [crates/gcode/src/graph/code_graph/tests.rs:68-151]
  - Signature: `fn graph_read_guard_stays_strict_but_public_reads_degrade_without_service() {`
  - Purpose: This test verifies that enforced graph read guards fail strictly when FalkorDB is not configured, while public graph query APIs gracefully degrade to empty or default responses without the service. [crates/gcode/src/graph/code_graph/tests.rs:68-151]
- `compact_detail_truncates_on_char_boundaries` (function) component `compact_detail_truncates_on_char_boundaries [function]` (`7df349e3-8ec9-53dc-ace2-652737365365`) lines 154-159 [crates/gcode/src/graph/code_graph/tests.rs:154-159]
  - Signature: `fn compact_detail_truncates_on_char_boundaries() {`
  - Purpose: This unit test verifies that `compact_detail` truncates strings to exactly 240 characters at UTF-8 character boundaries and appends a three-dot ellipsis. [crates/gcode/src/graph/code_graph/tests.rs:154-159]
- `file_blast_rows_are_deduped_and_limited_after_merge` (function) component `file_blast_rows_are_deduped_and_limited_after_merge [function]` (`66e16705-8139-5a2d-b892-6e7d34f414b5`) lines 162-189 [crates/gcode/src/graph/code_graph/tests.rs:162-189]
  - Signature: `fn file_blast_rows_are_deduped_and_limited_after_merge() {`
  - Purpose: Tests that `dedupe_limited_blast_rows` deduplicates rows by `node_id`, preserves the record with minimum distance, and enforces a row count limit. [crates/gcode/src/graph/code_graph/tests.rs:162-189]
- `file_calls_query_keeps_node_and_metadata_source_paths_distinct` (function) component `file_calls_query_keeps_node_and_metadata_source_paths_distinct [function]` (`a521573d-8d55-570d-bc21-368c25abba02`) lines 192-198 [crates/gcode/src/graph/code_graph/tests.rs:192-198]
  - Signature: `fn file_calls_query_keeps_node_and_metadata_source_paths_distinct() {`
  - Purpose: This test verifies that `file_calls_query` generates SQL with distinct column aliases (`source_file_path` for the node table and `metadata_source_file_path` for the metadata reference) to prevent column name shadowing. [crates/gcode/src/graph/code_graph/tests.rs:192-198]
- `graph_write_uses_synced_file_path_for_import_and_call_sources` (function) component `graph_write_uses_synced_file_path_for_import_and_call_sources [function]` (`2912145e-d9eb-5a79-8bd7-116fc512d610`) lines 201-218 [crates/gcode/src/graph/code_graph/tests.rs:201-218]
  - Signature: `fn graph_write_uses_synced_file_path_for_import_and_call_sources() {`
  - Purpose: Verifies that `import_graph_items` and `partition_call_graph_items` synchronize stale file paths in import and call relations to the canonical source file path. [crates/gcode/src/graph/code_graph/tests.rs:201-218]
- `graph_write_skips_unparsed_import_sentinel_modules` (function) component `graph_write_skips_unparsed_import_sentinel_modules [function]` (`a49206b3-922c-5c1f-a829-b6452876945a`) lines 221-237 [crates/gcode/src/graph/code_graph/tests.rs:221-237]
  - Signature: `fn graph_write_skips_unparsed_import_sentinel_modules() {`
  - Purpose: This test verifies that the `import_graph_items` function correctly filters out import relations marked with the `UNPARSED:` sentinel prefix, returning only successfully parsed imports. [crates/gcode/src/graph/code_graph/tests.rs:221-237]
- `imports_query_returns_stable_id` (function) component `imports_query_returns_stable_id [function]` (`974418c2-f1ef-5226-bda4-a998c74f85f4`) lines 240-245 [crates/gcode/src/graph/code_graph/tests.rs:240-245]
  - Signature: `fn imports_query_returns_stable_id() {`
  - Purpose: This test function verifies that the imports query for a given project and source file contains the expected SQL column aliases (`m.name AS id` and `m.name AS module_name`) for stable module identification. [crates/gcode/src/graph/code_graph/tests.rs:240-245]
- `file_import_blast_radius_traverses_import_edges_undirected` (function) component `file_import_blast_radius_traverses_import_edges_undirected [function]` (`9a65f915-0ea0-531a-98e0-1c8fa1c53b51`) lines 248-252 [crates/gcode/src/graph/code_graph/tests.rs:248-252]
  - Signature: `fn file_import_blast_radius_traverses_import_edges_undirected() {`
  - Purpose: Verifies that the file import blast radius query generates an undirected, variable-length (1-2 hops) Cypher-style graph traversal pattern for IMPORTS relationships. [crates/gcode/src/graph/code_graph/tests.rs:248-252]
- `projection_metadata_uses_only_metadata_source_file_path` (function) component `projection_metadata_uses_only_metadata_source_file_path [function]` (`3e5b0ee6-479a-51de-abd5-127139799e87`) lines 255-269 [crates/gcode/src/graph/code_graph/tests.rs:255-269]
  - Signature: `fn projection_metadata_uses_only_metadata_source_file_path() {`
  - Purpose: This function tests that `row_to_projection_metadata()` prioritizes the `metadata_source_file_path` field over `source_file_path` when constructing projection metadata. [crates/gcode/src/graph/code_graph/tests.rs:255-269]
- `projection_metadata_does_not_fallback_to_node_source_file_path` (function) component `projection_metadata_does_not_fallback_to_node_source_file_path [function]` (`e08e8955-4908-52b8-8c51-37b8262ad4db`) lines 272-282 [crates/gcode/src/graph/code_graph/tests.rs:272-282]
  - Signature: `fn projection_metadata_does_not_fallback_to_node_source_file_path() {`
  - Purpose: This test verifies that `row_to_projection_metadata` discards the `source_file_path` field when converting a row with `provenance="EXTRACTED"` and `source_system="gcode"`, resulting in `None` rather than falling back to the node source file path. [crates/gcode/src/graph/code_graph/tests.rs:272-282]
- `delete_preserves_current_symbols` (function) component `delete_preserves_current_symbols [function]` (`6f57dbfe-ec7a-5dc2-9a7d-240d117f6dfa`) lines 285-324 [crates/gcode/src/graph/code_graph/tests.rs:285-324]
  - Signature: `fn delete_preserves_current_symbols() {`
  - Purpose: This function asserts that `delete_file_graph_queries` generates Cypher queries that selectively delete stale CodeSymbol nodes while preserving specified symbol IDs through a `WHERE NOT s.id IN $symbol_ids` filter clause. [crates/gcode/src/graph/code_graph/tests.rs:285-324]
- `cleanup_orphans_is_project_scoped` (function) component `cleanup_orphans_is_project_scoped [function]` (`ce7ca738-08aa-5842-9990-a7ca372ce079`) lines 327-374 [crates/gcode/src/graph/code_graph/tests.rs:327-374]
  - Signature: `fn cleanup_orphans_is_project_scoped() {`
  - Purpose: Verifies that `cleanup_orphans_queries` generates exactly three Cypher deletion queries, each correctly scoped to a specified project via parameterized project ID filters on CodeModule and CodeSymbol nodes and their relationships. [crates/gcode/src/graph/code_graph/tests.rs:327-374]
- `delete_file_node_is_project_and_path_scoped` (function) component `delete_file_node_is_project_and_path_scoped [function]` (`857fdb88-cc01-5819-8aab-af2d64f54df1`) lines 377-396 [crates/gcode/src/graph/code_graph/tests.rs:377-396]
  - Signature: `fn delete_file_node_is_project_and_path_scoped() {`
  - Purpose: Verifies that `delete_file_node_query` generates a parameterized Cypher deletion query scoped to a specific project and file path, ensuring the MATCH clause filters by both properties and the query uses DETACH DELETE. [crates/gcode/src/graph/code_graph/tests.rs:377-396]
- `clear_project_is_project_scoped` (function) component `clear_project_is_project_scoped [function]` (`804f63f1-5045-51c2-9265-d3ca6260aac1`) lines 399-409 [crates/gcode/src/graph/code_graph/tests.rs:399-409]
  - Signature: `fn clear_project_is_project_scoped() {`
  - Purpose: This test verifies that `clear_project_query` generates a project-scoped Cypher query that targets both CodeFile and CodeSymbol nodes with correct parameterization of the project identifier. [crates/gcode/src/graph/code_graph/tests.rs:399-409]
- `clear_project_targets_only_code_index_labels` (function) component `clear_project_targets_only_code_index_labels [function]` (`481f99d7-57e7-5aea-85d4-59608b548f84`) lines 412-439 [crates/gcode/src/graph/code_graph/tests.rs:412-439]
  - Signature: `fn clear_project_targets_only_code_index_labels() {`
  - Purpose: This function validates that a project clear query targets all code index labels (CodeFile, CodeSymbol, CodeModule, UnresolvedCallee, ExternalSymbol) while excluding all memory graph labels. [crates/gcode/src/graph/code_graph/tests.rs:412-439]
- `clear_all_code_index_targets_only_code_index_labels` (function) component `clear_all_code_index_targets_only_code_index_labels [function]` (`dfeb388c-a61b-5d1e-b8c7-5b7657895be1`) lines 442-454 [crates/gcode/src/graph/code_graph/tests.rs:442-454]
  - Signature: `fn clear_all_code_index_targets_only_code_index_labels() {`
  - Purpose: Asserts that `clear_all_code_index_query()` generates an unparameterized Cypher query matching all code index node types (CodeFile, CodeSymbol, CodeModule, UnresolvedCallee, ExternalSymbol) without project-scoped filtering or config store references. [crates/gcode/src/graph/code_graph/tests.rs:442-454]

