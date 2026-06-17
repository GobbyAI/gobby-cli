---
title: crates/gcode/src/graph/code_graph/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/tests.rs
  ranges:
  - 7-21
  - 24-33
  - 36-65
  - 68-156
  - 159-164
  - 167-194
  - 197-203
  - 206-223
  - 226-242
  - 245-250
  - 253-276
  - 279-320
  - 323-327
  - 330-344
  - 347-357
  - 360-399
  - 402-449
  - 452-499
  - 502-521
  - 524-534
  - 537-564
  - 567-579
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/tests.rs:7-21](crates/gcode/src/graph/code_graph/tests.rs#L7-L21), [crates/gcode/src/graph/code_graph/tests.rs:24-33](crates/gcode/src/graph/code_graph/tests.rs#L24-L33), [crates/gcode/src/graph/code_graph/tests.rs:36-65](crates/gcode/src/graph/code_graph/tests.rs#L36-L65), [crates/gcode/src/graph/code_graph/tests.rs:68-156](crates/gcode/src/graph/code_graph/tests.rs#L68-L156), [crates/gcode/src/graph/code_graph/tests.rs:159-164](crates/gcode/src/graph/code_graph/tests.rs#L159-L164), [crates/gcode/src/graph/code_graph/tests.rs:167-194](crates/gcode/src/graph/code_graph/tests.rs#L167-L194), [crates/gcode/src/graph/code_graph/tests.rs:197-203](crates/gcode/src/graph/code_graph/tests.rs#L197-L203), [crates/gcode/src/graph/code_graph/tests.rs:206-223](crates/gcode/src/graph/code_graph/tests.rs#L206-L223), [crates/gcode/src/graph/code_graph/tests.rs:226-242](crates/gcode/src/graph/code_graph/tests.rs#L226-L242), [crates/gcode/src/graph/code_graph/tests.rs:245-250](crates/gcode/src/graph/code_graph/tests.rs#L245-L250), [crates/gcode/src/graph/code_graph/tests.rs:253-276](crates/gcode/src/graph/code_graph/tests.rs#L253-L276), [crates/gcode/src/graph/code_graph/tests.rs:279-320](crates/gcode/src/graph/code_graph/tests.rs#L279-L320), [crates/gcode/src/graph/code_graph/tests.rs:323-327](crates/gcode/src/graph/code_graph/tests.rs#L323-L327), [crates/gcode/src/graph/code_graph/tests.rs:330-344](crates/gcode/src/graph/code_graph/tests.rs#L330-L344), [crates/gcode/src/graph/code_graph/tests.rs:347-357](crates/gcode/src/graph/code_graph/tests.rs#L347-L357), [crates/gcode/src/graph/code_graph/tests.rs:360-399](crates/gcode/src/graph/code_graph/tests.rs#L360-L399), [crates/gcode/src/graph/code_graph/tests.rs:402-449](crates/gcode/src/graph/code_graph/tests.rs#L402-L449), [crates/gcode/src/graph/code_graph/tests.rs:452-499](crates/gcode/src/graph/code_graph/tests.rs#L452-L499), [crates/gcode/src/graph/code_graph/tests.rs:502-521](crates/gcode/src/graph/code_graph/tests.rs#L502-L521), [crates/gcode/src/graph/code_graph/tests.rs:524-534](crates/gcode/src/graph/code_graph/tests.rs#L524-L534), [crates/gcode/src/graph/code_graph/tests.rs:537-564](crates/gcode/src/graph/code_graph/tests.rs#L537-L564), [crates/gcode/src/graph/code_graph/tests.rs:567-579](crates/gcode/src/graph/code_graph/tests.rs#L567-L579)

</details>

# crates/gcode/src/graph/code_graph/tests.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Purpose

This file is a test suite for the code graph layer, checking that graph payloads, edges, and query results preserve the right provenance and metadata and that read/write helpers behave correctly under project scoping. The tests cover edge cases such as truncation, deduping and limiting merged file-blast rows, stable import and symbol IDs, external call target resolution, and keeping node source paths separate from metadata source paths. It also verifies graph mutation and cleanup operations, including delete, orphan cleanup, file-node deletion, and project/global clear operations, only affect the intended project and code-index labels.
[crates/gcode/src/graph/code_graph/tests.rs:7-21]
[crates/gcode/src/graph/code_graph/tests.rs:24-33]
[crates/gcode/src/graph/code_graph/tests.rs:36-65]
[crates/gcode/src/graph/code_graph/tests.rs:68-156]
[crates/gcode/src/graph/code_graph/tests.rs:159-164]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `test_context` | function | `fn test_context(falkordb: Option<crate::config::FalkorConfig>) -> Context {` | `test_context [function]` | `6ada5f13-a01c-502f-a972-3217233985d9` | 7-21 [crates/gcode/src/graph/code_graph/tests.rs:7-21] | Indexed function `test_context` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:7-21] |
| `code_edges_carry_provenance` | function | `fn code_edges_carry_provenance() {` | `code_edges_carry_provenance [function]` | `997a6ff7-0182-55be-a78f-6a99981cb933` | 24-33 [crates/gcode/src/graph/code_graph/tests.rs:24-33] | Indexed function `code_edges_carry_provenance` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:24-33] |
| `read_apis_return_node_link_payloads_with_link_metadata` | function | `fn read_apis_return_node_link_payloads_with_link_metadata() {` | `read_apis_return_node_link_payloads_with_link_metadata [function]` | `db7e66a2-5c4e-51ca-9ce3-cbe0a451bada` | 36-65 [crates/gcode/src/graph/code_graph/tests.rs:36-65] | Indexed function `read_apis_return_node_link_payloads_with_link_metadata` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:36-65] |
| `graph_read_guard_stays_strict_but_public_reads_degrade_without_service` | function | `fn graph_read_guard_stays_strict_but_public_reads_degrade_without_service() {` | `graph_read_guard_stays_strict_but_public_reads_degrade_without_service [function]` | `b5fc4fd1-546f-5a04-a606-0290158634ec` | 68-156 [crates/gcode/src/graph/code_graph/tests.rs:68-156] | Indexed function `graph_read_guard_stays_strict_but_public_reads_degrade_without_service` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:68-156] |
| `compact_detail_truncates_on_char_boundaries` | function | `fn compact_detail_truncates_on_char_boundaries() {` | `compact_detail_truncates_on_char_boundaries [function]` | `13feec5e-b5ad-5c8f-b551-28c14accc9e3` | 159-164 [crates/gcode/src/graph/code_graph/tests.rs:159-164] | Indexed function `compact_detail_truncates_on_char_boundaries` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:159-164] |
| `file_blast_rows_are_deduped_and_limited_after_merge` | function | `fn file_blast_rows_are_deduped_and_limited_after_merge() {` | `file_blast_rows_are_deduped_and_limited_after_merge [function]` | `98609cd7-2726-5ba9-9d2a-879617577762` | 167-194 [crates/gcode/src/graph/code_graph/tests.rs:167-194] | Indexed function `file_blast_rows_are_deduped_and_limited_after_merge` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:167-194] |
| `file_calls_query_keeps_node_and_metadata_source_paths_distinct` | function | `fn file_calls_query_keeps_node_and_metadata_source_paths_distinct() {` | `file_calls_query_keeps_node_and_metadata_source_paths_distinct [function]` | `f202a3ac-b987-57e0-ac7e-60ce154c6962` | 197-203 [crates/gcode/src/graph/code_graph/tests.rs:197-203] | Indexed function `file_calls_query_keeps_node_and_metadata_source_paths_distinct` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:197-203] |
| `graph_write_uses_synced_file_path_for_import_and_call_sources` | function | `fn graph_write_uses_synced_file_path_for_import_and_call_sources() {` | `graph_write_uses_synced_file_path_for_import_and_call_sources [function]` | `a39277f9-1c47-5226-9b16-c0f842530a0d` | 206-223 [crates/gcode/src/graph/code_graph/tests.rs:206-223] | Indexed function `graph_write_uses_synced_file_path_for_import_and_call_sources` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:206-223] |
| `graph_write_skips_unparsed_import_sentinel_modules` | function | `fn graph_write_skips_unparsed_import_sentinel_modules() {` | `graph_write_skips_unparsed_import_sentinel_modules [function]` | `29ee42aa-3f2b-5b6b-aae8-57503e538b5e` | 226-242 [crates/gcode/src/graph/code_graph/tests.rs:226-242] | Indexed function `graph_write_skips_unparsed_import_sentinel_modules` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:226-242] |
| `imports_query_returns_stable_id` | function | `fn imports_query_returns_stable_id() {` | `imports_query_returns_stable_id [function]` | `c251aaa9-38b5-5364-bc63-e6a819ce5bc7` | 245-250 [crates/gcode/src/graph/code_graph/tests.rs:245-250] | Indexed function `imports_query_returns_stable_id` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:245-250] |
| `external_call_target_resolution_matches_id_name_or_module_member` | function | `fn external_call_target_resolution_matches_id_name_or_module_member() {` | `external_call_target_resolution_matches_id_name_or_module_member [function]` | `c2cad773-3e9a-5d00-90f8-e4ef0db77dcf` | 253-276 [crates/gcode/src/graph/code_graph/tests.rs:253-276] | Indexed function `external_call_target_resolution_matches_id_name_or_module_member` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:253-276] |
| `symbol_path_queries_stay_project_scoped_and_symbol_only` | function | `fn symbol_path_queries_stay_project_scoped_and_symbol_only() {` | `symbol_path_queries_stay_project_scoped_and_symbol_only [function]` | `ab50ae77-1a54-5bd8-9840-a987ebe7659c` | 279-320 [crates/gcode/src/graph/code_graph/tests.rs:279-320] | Indexed function `symbol_path_queries_stay_project_scoped_and_symbol_only` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:279-320] |
| `file_import_blast_radius_traverses_import_edges_undirected` | function | `fn file_import_blast_radius_traverses_import_edges_undirected() {` | `file_import_blast_radius_traverses_import_edges_undirected [function]` | `783d7c77-d149-5fb1-9a1c-0a971a92814c` | 323-327 [crates/gcode/src/graph/code_graph/tests.rs:323-327] | Indexed function `file_import_blast_radius_traverses_import_edges_undirected` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:323-327] |
| `projection_metadata_uses_only_metadata_source_file_path` | function | `fn projection_metadata_uses_only_metadata_source_file_path() {` | `projection_metadata_uses_only_metadata_source_file_path [function]` | `847f2ae2-f90c-54b3-98fa-f6491edb542b` | 330-344 [crates/gcode/src/graph/code_graph/tests.rs:330-344] | Indexed function `projection_metadata_uses_only_metadata_source_file_path` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:330-344] |
| `projection_metadata_does_not_fallback_to_node_source_file_path` | function | `fn projection_metadata_does_not_fallback_to_node_source_file_path() {` | `projection_metadata_does_not_fallback_to_node_source_file_path [function]` | `d1fa0e8e-43c3-5fa2-9516-c4e78115a629` | 347-357 [crates/gcode/src/graph/code_graph/tests.rs:347-357] | Indexed function `projection_metadata_does_not_fallback_to_node_source_file_path` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:347-357] |
| `delete_preserves_current_symbols` | function | `fn delete_preserves_current_symbols() {` | `delete_preserves_current_symbols [function]` | `2d0f639f-0085-5e18-b23d-8b1bb0a42ec6` | 360-399 [crates/gcode/src/graph/code_graph/tests.rs:360-399] | Indexed function `delete_preserves_current_symbols` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:360-399] |
| `cleanup_orphans_is_project_scoped` | function | `fn cleanup_orphans_is_project_scoped() {` | `cleanup_orphans_is_project_scoped [function]` | `9f9a5884-fe96-5999-9d8e-00e97c4c615c` | 402-449 [crates/gcode/src/graph/code_graph/tests.rs:402-449] | Indexed function `cleanup_orphans_is_project_scoped` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:402-449] |
| `deleted_file_cleanup_queries_are_project_scoped_and_count_file_nodes` | function | `fn deleted_file_cleanup_queries_are_project_scoped_and_count_file_nodes() {` | `deleted_file_cleanup_queries_are_project_scoped_and_count_file_nodes [function]` | `f71e97e6-0282-5d0a-9568-0314814948c3` | 452-499 [crates/gcode/src/graph/code_graph/tests.rs:452-499] | Indexed function `deleted_file_cleanup_queries_are_project_scoped_and_count_file_nodes` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:452-499] |
| `delete_file_node_is_project_and_path_scoped` | function | `fn delete_file_node_is_project_and_path_scoped() {` | `delete_file_node_is_project_and_path_scoped [function]` | `14a52fd8-aeca-5a12-8146-7e354d6ed9a8` | 502-521 [crates/gcode/src/graph/code_graph/tests.rs:502-521] | Indexed function `delete_file_node_is_project_and_path_scoped` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:502-521] |
| `clear_project_is_project_scoped` | function | `fn clear_project_is_project_scoped() {` | `clear_project_is_project_scoped [function]` | `2893d8f5-c57d-5b53-a42f-5fede7228985` | 524-534 [crates/gcode/src/graph/code_graph/tests.rs:524-534] | Indexed function `clear_project_is_project_scoped` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:524-534] |
| `clear_project_targets_only_code_index_labels` | function | `fn clear_project_targets_only_code_index_labels() {` | `clear_project_targets_only_code_index_labels [function]` | `7fd7c976-4bbc-533e-b09c-571c613b7012` | 537-564 [crates/gcode/src/graph/code_graph/tests.rs:537-564] | Indexed function `clear_project_targets_only_code_index_labels` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:537-564] |
| `clear_all_code_index_targets_only_code_index_labels` | function | `fn clear_all_code_index_targets_only_code_index_labels() {` | `clear_all_code_index_targets_only_code_index_labels [function]` | `2ef2d434-b593-5526-96cf-94f471ec212a` | 567-579 [crates/gcode/src/graph/code_graph/tests.rs:567-579] | Indexed function `clear_all_code_index_targets_only_code_index_labels` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:567-579] |
