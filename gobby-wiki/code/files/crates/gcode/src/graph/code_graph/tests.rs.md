---
title: crates/gcode/src/graph/code_graph/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/tests.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Overview

`crates/gcode/src/graph/code_graph/tests.rs` exposes 22 indexed API symbols.

## How it fits

`crates/gcode/src/graph/code_graph/tests.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `test_context` | function | Indexed function `test_context` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:7-21] |
| `code_edges_carry_provenance` | function | Indexed function `code_edges_carry_provenance` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:24-33] |
| `read_apis_return_node_link_payloads_with_link_metadata` | function | Indexed function `read_apis_return_node_link_payloads_with_link_metadata` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:36-65] |
| `graph_read_guard_stays_strict_but_public_reads_degrade_without_service` | function | Indexed function `graph_read_guard_stays_strict_but_public_reads_degrade_without_service` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:68-156] |
| `compact_detail_truncates_on_char_boundaries` | function | Indexed function `compact_detail_truncates_on_char_boundaries` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:159-164] |
| `file_blast_rows_are_deduped_and_limited_after_merge` | function | Indexed function `file_blast_rows_are_deduped_and_limited_after_merge` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:167-194] |
| `file_calls_query_keeps_node_and_metadata_source_paths_distinct` | function | Indexed function `file_calls_query_keeps_node_and_metadata_source_paths_distinct` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:197-203] |
| `graph_write_uses_synced_file_path_for_import_and_call_sources` | function | Indexed function `graph_write_uses_synced_file_path_for_import_and_call_sources` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:206-223] |
| `graph_write_skips_unparsed_import_sentinel_modules` | function | Indexed function `graph_write_skips_unparsed_import_sentinel_modules` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:226-242] |
| `imports_query_returns_stable_id` | function | Indexed function `imports_query_returns_stable_id` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:245-250] |
| `external_call_target_resolution_matches_id_name_or_module_member` | function | Indexed function `external_call_target_resolution_matches_id_name_or_module_member` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:253-276] |
| `symbol_path_queries_stay_project_scoped_and_symbol_only` | function | Indexed function `symbol_path_queries_stay_project_scoped_and_symbol_only` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:279-320] |
| `file_import_blast_radius_traverses_import_edges_undirected` | function | Indexed function `file_import_blast_radius_traverses_import_edges_undirected` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:323-327] |
| `projection_metadata_uses_only_metadata_source_file_path` | function | Indexed function `projection_metadata_uses_only_metadata_source_file_path` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:330-344] |
| `projection_metadata_does_not_fallback_to_node_source_file_path` | function | Indexed function `projection_metadata_does_not_fallback_to_node_source_file_path` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:347-357] |
| `delete_preserves_current_symbols` | function | Indexed function `delete_preserves_current_symbols` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:360-399] |
| `cleanup_orphans_is_project_scoped` | function | Indexed function `cleanup_orphans_is_project_scoped` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:402-449] |
| `deleted_file_cleanup_queries_are_project_scoped_and_count_file_nodes` | function | Indexed function `deleted_file_cleanup_queries_are_project_scoped_and_count_file_nodes` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:452-499] |
| `delete_file_node_is_project_and_path_scoped` | function | Indexed function `delete_file_node_is_project_and_path_scoped` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:502-521] |
| `clear_project_is_project_scoped` | function | Indexed function `clear_project_is_project_scoped` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:524-534] |
| `clear_project_targets_only_code_index_labels` | function | Indexed function `clear_project_targets_only_code_index_labels` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:537-564] |
| `clear_all_code_index_targets_only_code_index_labels` | function | Indexed function `clear_all_code_index_targets_only_code_index_labels` in `crates/gcode/src/graph/code_graph/tests.rs`. [crates/gcode/src/graph/code_graph/tests.rs:567-579] |

