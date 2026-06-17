---
title: crates/gcode/src/db/queries.rs
type: code_file
provenance:
- file: crates/gcode/src/db/queries.rs
  ranges:
  - 8-13
  - 15-26
  - 28-38
  - 40-55
  - 57-69
  - 71-83
  - 85-97
  - 99-109
  - 111-123
  - 125-135
  - 141-156
  - 158-168
  - 170-190
  - 192-205
  - 207-221
  - 223-236
  - 241-259
  - 261-274
  - 289-321
  - 323-357
  - 360-364
  - 366-413
  - 415-425
  - 427-432
  - 434-436
  - 438-449
  - 451-470
  - 472-481
  - 487-497
  - 500-507
  - 510-520
  - 523-530
  - 533-544
  - 547-554
  - 557-561
  - 565-567
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/db/queries.rs:8-13](crates/gcode/src/db/queries.rs#L8-L13), [crates/gcode/src/db/queries.rs:15-26](crates/gcode/src/db/queries.rs#L15-L26), [crates/gcode/src/db/queries.rs:28-38](crates/gcode/src/db/queries.rs#L28-L38), [crates/gcode/src/db/queries.rs:40-55](crates/gcode/src/db/queries.rs#L40-L55), [crates/gcode/src/db/queries.rs:57-69](crates/gcode/src/db/queries.rs#L57-L69), [crates/gcode/src/db/queries.rs:71-83](crates/gcode/src/db/queries.rs#L71-L83), [crates/gcode/src/db/queries.rs:85-97](crates/gcode/src/db/queries.rs#L85-L97), [crates/gcode/src/db/queries.rs:99-109](crates/gcode/src/db/queries.rs#L99-L109), [crates/gcode/src/db/queries.rs:111-123](crates/gcode/src/db/queries.rs#L111-L123), [crates/gcode/src/db/queries.rs:125-135](crates/gcode/src/db/queries.rs#L125-L135), [crates/gcode/src/db/queries.rs:141-156](crates/gcode/src/db/queries.rs#L141-L156), [crates/gcode/src/db/queries.rs:158-168](crates/gcode/src/db/queries.rs#L158-L168), [crates/gcode/src/db/queries.rs:170-190](crates/gcode/src/db/queries.rs#L170-L190), [crates/gcode/src/db/queries.rs:192-205](crates/gcode/src/db/queries.rs#L192-L205), [crates/gcode/src/db/queries.rs:207-221](crates/gcode/src/db/queries.rs#L207-L221), [crates/gcode/src/db/queries.rs:223-236](crates/gcode/src/db/queries.rs#L223-L236), [crates/gcode/src/db/queries.rs:241-259](crates/gcode/src/db/queries.rs#L241-L259), [crates/gcode/src/db/queries.rs:261-274](crates/gcode/src/db/queries.rs#L261-L274), [crates/gcode/src/db/queries.rs:289-321](crates/gcode/src/db/queries.rs#L289-L321), [crates/gcode/src/db/queries.rs:323-357](crates/gcode/src/db/queries.rs#L323-L357), [crates/gcode/src/db/queries.rs:360-364](crates/gcode/src/db/queries.rs#L360-L364), [crates/gcode/src/db/queries.rs:366-413](crates/gcode/src/db/queries.rs#L366-L413), [crates/gcode/src/db/queries.rs:415-425](crates/gcode/src/db/queries.rs#L415-L425), [crates/gcode/src/db/queries.rs:427-432](crates/gcode/src/db/queries.rs#L427-L432), [crates/gcode/src/db/queries.rs:434-436](crates/gcode/src/db/queries.rs#L434-L436), [crates/gcode/src/db/queries.rs:438-449](crates/gcode/src/db/queries.rs#L438-L449), [crates/gcode/src/db/queries.rs:451-470](crates/gcode/src/db/queries.rs#L451-L470), [crates/gcode/src/db/queries.rs:472-481](crates/gcode/src/db/queries.rs#L472-L481), [crates/gcode/src/db/queries.rs:487-497](crates/gcode/src/db/queries.rs#L487-L497), [crates/gcode/src/db/queries.rs:500-507](crates/gcode/src/db/queries.rs#L500-L507), [crates/gcode/src/db/queries.rs:510-520](crates/gcode/src/db/queries.rs#L510-L520), [crates/gcode/src/db/queries.rs:523-530](crates/gcode/src/db/queries.rs#L523-L530), [crates/gcode/src/db/queries.rs:533-544](crates/gcode/src/db/queries.rs#L533-L544), [crates/gcode/src/db/queries.rs:547-554](crates/gcode/src/db/queries.rs#L547-L554), [crates/gcode/src/db/queries.rs:557-561](crates/gcode/src/db/queries.rs#L557-L561), [crates/gcode/src/db/queries.rs:565-567](crates/gcode/src/db/queries.rs#L565-L567)

</details>

# crates/gcode/src/db/queries.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This file defines database query helpers for the code index. It checks whether projects and files are indexed, lists indexed file paths, reads a file’s graph facts by aggregating imports, symbol definitions, and calls, and updates sync state for graph and vector indexing; the later helpers resolve local and default-import call targets, build symbol-select SQL fragments, and enforce safe aliasing and candidate selection rules so the query logic stays consistent and unambiguous.
[crates/gcode/src/db/queries.rs:8-13]
[crates/gcode/src/db/queries.rs:15-26]
[crates/gcode/src/db/queries.rs:28-38]
[crates/gcode/src/db/queries.rs:40-55]
[crates/gcode/src/db/queries.rs:57-69]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `GraphFileFacts` | class | `pub struct GraphFileFacts {` | `GraphFileFacts [class]` | `e246332f-4b56-54d8-9c30-d2eb0fd22317` | 8-13 [crates/gcode/src/db/queries.rs:8-13] | Indexed class `GraphFileFacts` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:8-13] |
| `list_indexed_file_paths` | function | `pub fn list_indexed_file_paths(` | `list_indexed_file_paths [function]` | `8b652c63-6d76-54dd-8d45-21ace76f373e` | 15-26 [crates/gcode/src/db/queries.rs:15-26] | Indexed function `list_indexed_file_paths` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:15-26] |
| `indexed_project_exists` | function | `pub fn indexed_project_exists(` | `indexed_project_exists [function]` | `7fd72311-3a27-5041-bbc1-b902a2e3befa` | 28-38 [crates/gcode/src/db/queries.rs:28-38] | Indexed function `indexed_project_exists` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:28-38] |
| `read_graph_file_facts` | function | `pub fn read_graph_file_facts(` | `read_graph_file_facts [function]` | `25b0349f-916e-5122-a4ff-e00a72b3e478` | 40-55 [crates/gcode/src/db/queries.rs:40-55] | Indexed function `read_graph_file_facts` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:40-55] |
| `indexed_file_exists` | function | `pub fn indexed_file_exists(` | `indexed_file_exists [function]` | `6524a97c-e990-53e6-a188-d713cbf6ae30` | 57-69 [crates/gcode/src/db/queries.rs:57-69] | Indexed function `indexed_file_exists` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:57-69] |
| `mark_graph_sync_attempted` | function | `pub fn mark_graph_sync_attempted(` | `mark_graph_sync_attempted [function]` | `b7f0438b-913e-530e-b42b-c3282f6d89a8` | 71-83 [crates/gcode/src/db/queries.rs:71-83] | Indexed function `mark_graph_sync_attempted` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:71-83] |
| `mark_graph_synced` | function | `pub fn mark_graph_synced(` | `mark_graph_synced [function]` | `f1deb79d-f478-5d9e-af41-e7a81efd5d5b` | 85-97 [crates/gcode/src/db/queries.rs:85-97] | Indexed function `mark_graph_synced` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:85-97] |
| `reset_graph_sync_for_project` | function | `pub fn reset_graph_sync_for_project(` | `reset_graph_sync_for_project [function]` | `4bd59611-25f4-5318-ba4c-57af36eb8a78` | 99-109 [crates/gcode/src/db/queries.rs:99-109] | Indexed function `reset_graph_sync_for_project` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:99-109] |
| `mark_vectors_synced` | function | `pub fn mark_vectors_synced(` | `mark_vectors_synced [function]` | `7a15e279-5b5a-5f51-81f8-33e683f23c84` | 111-123 [crates/gcode/src/db/queries.rs:111-123] | Indexed function `mark_vectors_synced` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:111-123] |
| `mark_project_vectors_synced` | function | `pub fn mark_project_vectors_synced(` | `mark_project_vectors_synced [function]` | `a215d167-f5c3-5d85-90b6-3ea69d369f88` | 125-135 [crates/gcode/src/db/queries.rs:125-135] | Indexed function `mark_project_vectors_synced` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:125-135] |
| `file_vectors_synced` | function | `pub fn file_vectors_synced(` | `file_vectors_synced [function]` | `7e1cb395-59ff-5822-b355-89eca4bd5804` | 141-156 [crates/gcode/src/db/queries.rs:141-156] | Indexed function `file_vectors_synced` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:141-156] |
| `reset_vectors_sync_for_project` | function | `pub fn reset_vectors_sync_for_project(` | `reset_vectors_sync_for_project [function]` | `9cb523e6-341e-5a59-ae9a-9bdc4fa503b3` | 158-168 [crates/gcode/src/db/queries.rs:158-168] | Indexed function `reset_vectors_sync_for_project` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:158-168] |
| `read_imports_for_file` | function | `fn read_imports_for_file(` | `read_imports_for_file [function]` | `0b9c0618-cf65-5bf0-9e0f-a2ea3e01e057` | 170-190 [crates/gcode/src/db/queries.rs:170-190] | Indexed function `read_imports_for_file` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:170-190] |
| `read_symbols_for_file` | function | `fn read_symbols_for_file(` | `read_symbols_for_file [function]` | `10d7b27b-d830-50e7-8dab-20cf950c1f40` | 192-205 [crates/gcode/src/db/queries.rs:192-205] | Indexed function `read_symbols_for_file` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:192-205] |
| `read_calls_for_file` | function | `fn read_calls_for_file(` | `read_calls_for_file [function]` | `ee16f0b6-e143-57c6-8af2-bb834b4c98b5` | 207-221 [crates/gcode/src/db/queries.rs:207-221] | Indexed function `read_calls_for_file` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:207-221] |
| `call_relation_from_row` | function | `fn call_relation_from_row(row: &postgres::Row) -> anyhow::Result<CallRelation> {` | `call_relation_from_row [function]` | `b0e67fef-4cc5-5c0f-9f56-1ddf88f5ba6a` | 223-236 [crates/gcode/src/db/queries.rs:223-236] | Indexed function `call_relation_from_row` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:223-236] |
| `read_local_import_calls` | function | `pub fn read_local_import_calls(` | `read_local_import_calls [function]` | `873d65e7-3a6e-54fb-9a8c-cb9388fa3b3c` | 241-259 [crates/gcode/src/db/queries.rs:241-259] | Indexed function `read_local_import_calls` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:241-259] |
| `read_project_local_import_calls` | function | `pub fn read_project_local_import_calls(` | `read_project_local_import_calls [function]` | `715e1d86-965c-5844-870f-d6e68eec8a7f` | 261-274 [crates/gcode/src/db/queries.rs:261-274] | Indexed function `read_project_local_import_calls` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:261-274] |
| `resolve_local_callee_symbol_id` | function | `pub fn resolve_local_callee_symbol_id(` | `resolve_local_callee_symbol_id [function]` | `3d6bfe8c-f2f4-59db-b9ad-0e274d7a1e17` | 289-321 [crates/gcode/src/db/queries.rs:289-321] | Indexed function `resolve_local_callee_symbol_id` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:289-321] |
| `resolve_default_import_symbol_id` | function | `pub fn resolve_default_import_symbol_id(` | `resolve_default_import_symbol_id [function]` | `ab2e821a-bda9-5ea8-9c47-ba274364986c` | 323-357 [crates/gcode/src/db/queries.rs:323-357] | Indexed function `resolve_default_import_symbol_id` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:323-357] |
| `LocalCalleeCandidate` | class | `struct LocalCalleeCandidate {` | `LocalCalleeCandidate [class]` | `0beb86ea-b5a8-5b9b-a4c0-f276726599e5` | 360-364 [crates/gcode/src/db/queries.rs:360-364] | Indexed class `LocalCalleeCandidate` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:360-364] |
| `select_local_callee_candidate_id` | function | `fn select_local_callee_candidate_id(candidates: &[LocalCalleeCandidate]) -> Option<String> {` | `select_local_callee_candidate_id [function]` | `6c77cfcb-4eb1-5529-abd2-0959a3397b2c` | 366-413 [crates/gcode/src/db/queries.rs:366-413] | Indexed function `select_local_callee_candidate_id` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:366-413] |
| `select_default_import_candidate_id` | function | `fn select_default_import_candidate_id(candidates: &[LocalCalleeCandidate]) -> Option<String> {` | `select_default_import_candidate_id [function]` | `cd99d411-2209-57e4-8732-d03e3cd48bbf` | 415-425 [crates/gcode/src/db/queries.rs:415-425] | Indexed function `select_default_import_candidate_id` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:415-425] |
| `unique_id` | function | `fn unique_id(ids: &[&String]) -> Option<String> {` | `unique_id [function]` | `38399a73-da62-51be-9115-1e8c0a0f5654` | 427-432 [crates/gcode/src/db/queries.rs:427-432] | Indexed function `unique_id` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:427-432] |
| `non_empty` | function | `fn non_empty(value: String) -> Option<String> {` | `non_empty [function]` | `1fa2a784-67af-56cd-9d5b-71fbaaf2508f` | 434-436 [crates/gcode/src/db/queries.rs:434-436] | Indexed function `non_empty` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:434-436] |
| `call_target_kind_from_str` | function | `fn call_target_kind_from_str(value: &str) -> anyhow::Result<CallTargetKind> {` | `call_target_kind_from_str [function]` | `183e5248-f106-5785-91d8-171b587c486b` | 438-449 [crates/gcode/src/db/queries.rs:438-449] | Indexed function `call_target_kind_from_str` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:438-449] |
| `symbol_select_columns` | function | `pub fn symbol_select_columns(alias: &str) -> String {` | `symbol_select_columns [function]` | `8ebe6b22-52ed-5b94-be53-76a46c385506` | 451-470 [crates/gcode/src/db/queries.rs:451-470] | Indexed function `symbol_select_columns` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:451-470] |
| `safe_symbol_select_alias` | function | `fn safe_symbol_select_alias(alias: &str) -> bool {` | `safe_symbol_select_alias [function]` | `64564600-d01c-5c6b-92f0-4fe9a10f05ec` | 472-481 [crates/gcode/src/db/queries.rs:472-481] | Indexed function `safe_symbol_select_alias` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:472-481] |
| `code_symbol_row` | function | `fn code_symbol_row(` | `code_symbol_row [function]` | `ca9b7027-0b71-527b-8171-007b4871ba81` | 487-497 [crates/gcode/src/db/queries.rs:487-497] | Indexed function `code_symbol_row` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:487-497] |
| `resolves_unique_module_scoped_function_candidate` | function | `fn resolves_unique_module_scoped_function_candidate() {` | `resolves_unique_module_scoped_function_candidate [function]` | `ce3c2c86-f3d7-57e2-b709-524593d695f3` | 500-507 [crates/gcode/src/db/queries.rs:500-507] | Indexed function `resolves_unique_module_scoped_function_candidate` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:500-507] |
| `method_tier_precedes_module_scoped_function_candidates` | function | `fn method_tier_precedes_module_scoped_function_candidates() {` | `method_tier_precedes_module_scoped_function_candidates [function]` | `79d3fe53-7fdd-5e06-b54d-576da04e7f88` | 510-520 [crates/gcode/src/db/queries.rs:510-520] | Indexed function `method_tier_precedes_module_scoped_function_candidates` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:510-520] |
| `leaves_ambiguous_module_scoped_function_candidates_unresolved` | function | `fn leaves_ambiguous_module_scoped_function_candidates_unresolved() {` | `leaves_ambiguous_module_scoped_function_candidates_unresolved [function]` | `2cdde4e8-2c95-5c12-8d26-86b4cb7c0be3` | 523-530 [crates/gcode/src/db/queries.rs:523-530] | Indexed function `leaves_ambiguous_module_scoped_function_candidates_unresolved` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:523-530] |
| `default_import_selector_resolves_unique_top_level_candidate` | function | `fn default_import_selector_resolves_unique_top_level_candidate() {` | `default_import_selector_resolves_unique_top_level_candidate [function]` | `4ccf2f23-5f4d-53df-b8d3-1a38f6224a10` | 533-544 [crates/gcode/src/db/queries.rs:533-544] | Indexed function `default_import_selector_resolves_unique_top_level_candidate` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:533-544] |
| `default_import_selector_leaves_ambiguous_top_level_candidates_unresolved` | function | `fn default_import_selector_leaves_ambiguous_top_level_candidates_unresolved() {` | `default_import_selector_leaves_ambiguous_top_level_candidates_unresolved [function]` | `bbe38c19-e95f-5948-9742-8d98592e7bb4` | 547-554 [crates/gcode/src/db/queries.rs:547-554] | Indexed function `default_import_selector_leaves_ambiguous_top_level_candidates_unresolved` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:547-554] |
| `symbol_select_columns_accepts_empty_or_safe_alias` | function | `fn symbol_select_columns_accepts_empty_or_safe_alias() {` | `symbol_select_columns_accepts_empty_or_safe_alias [function]` | `992b5ec6-fa1c-5de1-803b-ef5452ba431c` | 557-561 [crates/gcode/src/db/queries.rs:557-561] | Indexed function `symbol_select_columns_accepts_empty_or_safe_alias` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:557-561] |
| `symbol_select_columns_rejects_unsafe_alias` | function | `fn symbol_select_columns_rejects_unsafe_alias() {` | `symbol_select_columns_rejects_unsafe_alias [function]` | `6faaa92a-fea3-5acf-bc45-29934f691242` | 565-567 [crates/gcode/src/db/queries.rs:565-567] | Indexed function `symbol_select_columns_rejects_unsafe_alias` in `crates/gcode/src/db/queries.rs`. [crates/gcode/src/db/queries.rs:565-567] |
