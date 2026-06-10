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
  - 207-236
  - 238-240
  - 242-249
  - 251-270
  - 272-281
  - 288-292
  - 296-298
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/db/queries.rs

Module: [[code/modules/crates/gcode/src/db|crates/gcode/src/db]]

## Purpose

`crates/gcode/src/db/queries.rs` exposes 21 indexed API symbols.
[crates/gcode/src/db/queries.rs:8-13]
[crates/gcode/src/db/queries.rs:15-26]
[crates/gcode/src/db/queries.rs:28-38]
[crates/gcode/src/db/queries.rs:40-55]
[crates/gcode/src/db/queries.rs:57-69]
[crates/gcode/src/db/queries.rs:71-83]
[crates/gcode/src/db/queries.rs:85-97]
[crates/gcode/src/db/queries.rs:99-109]
[crates/gcode/src/db/queries.rs:111-123]
[crates/gcode/src/db/queries.rs:125-135]
[crates/gcode/src/db/queries.rs:141-156]
[crates/gcode/src/db/queries.rs:158-168]
[crates/gcode/src/db/queries.rs:170-190]
[crates/gcode/src/db/queries.rs:192-205]
[crates/gcode/src/db/queries.rs:207-236]
[crates/gcode/src/db/queries.rs:238-240]
[crates/gcode/src/db/queries.rs:242-249]
[crates/gcode/src/db/queries.rs:251-270]
[crates/gcode/src/db/queries.rs:272-281]
[crates/gcode/src/db/queries.rs:288-292]
[crates/gcode/src/db/queries.rs:296-298]

## API Symbols

- `GraphFileFacts` (class) component `GraphFileFacts [class]` (`e246332f-4b56-54d8-9c30-d2eb0fd22317`) lines 8-13 [crates/gcode/src/db/queries.rs:8-13]
  - Signature: `pub struct GraphFileFacts {`
  - Purpose: # GraphFileFacts

**GraphFileFacts is a Rust struct that encapsulates static code analysis facts for a source file, containing its path, imported modules, defined symbols, and call relations.** [crates/gcode/src/db/queries.rs:8-13]
- `list_indexed_file_paths` (function) component `list_indexed_file_paths [function]` (`8b652c63-6d76-54dd-8d45-21ace76f373e`) lines 15-26 [crates/gcode/src/db/queries.rs:15-26]
  - Signature: `pub fn list_indexed_file_paths(`
  - Purpose: Queries the database to retrieve all indexed file paths for a given project ID and returns them as a sorted vector of strings. [crates/gcode/src/db/queries.rs:15-26]
- `indexed_project_exists` (function) component `indexed_project_exists [function]` (`7fd72311-3a27-5041-bbc1-b902a2e3befa`) lines 28-38 [crates/gcode/src/db/queries.rs:28-38]
  - Signature: `pub fn indexed_project_exists(`
  - Purpose: Queries the `code_indexed_projects` table to determine whether a project with the specified ID exists, returning a `Result<bool>`. [crates/gcode/src/db/queries.rs:28-38]
- `read_graph_file_facts` (function) component `read_graph_file_facts [function]` (`25b0349f-916e-5122-a4ff-e00a72b3e478`) lines 40-55 [crates/gcode/src/db/queries.rs:40-55]
  - Signature: `pub fn read_graph_file_facts(`
  - Purpose: Aggregates file-level graph facts (imports, symbol definitions, and function calls) from a database for a specified project file, returning them in a GraphFileFacts struct. [crates/gcode/src/db/queries.rs:40-55]
- `indexed_file_exists` (function) component `indexed_file_exists [function]` (`6524a97c-e990-53e6-a188-d713cbf6ae30`) lines 57-69 [crates/gcode/src/db/queries.rs:57-69]
  - Signature: `pub fn indexed_file_exists(`
  - Purpose: Queries the `code_indexed_files` table to check whether a file with the given path is indexed for the specified project, returning `true` if a matching record exists. [crates/gcode/src/db/queries.rs:57-69]
- `mark_graph_sync_attempted` (function) component `mark_graph_sync_attempted [function]` (`b7f0438b-913e-530e-b42b-c3282f6d89a8`) lines 71-83 [crates/gcode/src/db/queries.rs:71-83]
  - Signature: `pub fn mark_graph_sync_attempted(`
  - Purpose: Updates a file's `code_indexed_files` database record to mark a graph sync attempt by setting `graph_synced = false` and timestamping `graph_sync_attempted_at`, returning true if any rows were modified. [crates/gcode/src/db/queries.rs:71-83]
- `mark_graph_synced` (function) component `mark_graph_synced [function]` (`f1deb79d-f478-5d9e-af41-e7a81efd5d5b`) lines 85-97 [crates/gcode/src/db/queries.rs:85-97]
  - Signature: `pub fn mark_graph_synced(`
  - Purpose: Sets the `graph_synced` flag to true and records the current timestamp for a specified project file, returning whether the update affected any rows. [crates/gcode/src/db/queries.rs:85-97]
- `reset_graph_sync_for_project` (function) component `reset_graph_sync_for_project [function]` (`4bd59611-25f4-5318-ba4c-57af36eb8a78`) lines 99-109 [crates/gcode/src/db/queries.rs:99-109]
  - Signature: `pub fn reset_graph_sync_for_project(`
  - Purpose: Resets the graph synchronization state for all indexed files in a specified project by setting `graph_synced` to false and clearing the `graph_sync_attempted_at` timestamp, returning the count of affected rows. [crates/gcode/src/db/queries.rs:99-109]
- `mark_vectors_synced` (function) component `mark_vectors_synced [function]` (`7a15e279-5b5a-5f51-81f8-33e683f23c84`) lines 111-123 [crates/gcode/src/db/queries.rs:111-123]
  - Signature: `pub fn mark_vectors_synced(`
  - Purpose: Updates the `vectors_synced` column to true for a specified project file in the `code_indexed_files` table and returns whether any rows were affected by the update. [crates/gcode/src/db/queries.rs:111-123]
- `mark_project_vectors_synced` (function) component `mark_project_vectors_synced [function]` (`a215d167-f5c3-5d85-90b6-3ea69d369f88`) lines 125-135 [crates/gcode/src/db/queries.rs:125-135]
  - Signature: `pub fn mark_project_vectors_synced(`
  - Purpose: Sets `vectors_synced` to true for all code-indexed files matching the given project ID and returns the number of affected rows. [crates/gcode/src/db/queries.rs:125-135]
- `file_vectors_synced` (function) component `file_vectors_synced [function]` (`7e1cb395-59ff-5822-b355-89eca4bd5804`) lines 141-156 [crates/gcode/src/db/queries.rs:141-156]
  - Signature: `pub fn file_vectors_synced(`
  - Purpose: Retrieves the `vectors_synced` boolean status from the `code_indexed_files` table for a specified project and file path, returning `Option<bool>` or an error. [crates/gcode/src/db/queries.rs:141-156]
- `reset_vectors_sync_for_project` (function) component `reset_vectors_sync_for_project [function]` (`9cb523e6-341e-5a59-ae9a-9bdc4fa503b3`) lines 158-168 [crates/gcode/src/db/queries.rs:158-168]
  - Signature: `pub fn reset_vectors_sync_for_project(`
  - Purpose: Resets the `vectors_synced` flag to false for all code-indexed files in a project, returning the count of affected rows. [crates/gcode/src/db/queries.rs:158-168]
- `read_imports_for_file` (function) component `read_imports_for_file [function]` (`0b9c0618-cf65-5bf0-9e0f-a2ea3e01e057`) lines 170-190 [crates/gcode/src/db/queries.rs:170-190]
  - Signature: `fn read_imports_for_file(`
  - Purpose: # Summary

Queries the `code_imports` database table to retrieve all module imports for a specified file within a project, returning them as a `Vec<ImportRelation>` mapping source files to target modules. [crates/gcode/src/db/queries.rs:170-190]
- `read_symbols_for_file` (function) component `read_symbols_for_file [function]` (`10d7b27b-d830-50e7-8dab-20cf950c1f40`) lines 192-205 [crates/gcode/src/db/queries.rs:192-205]
  - Signature: `fn read_symbols_for_file(`
  - Purpose: Queries the `code_symbols` table to retrieve all Symbol records for a specified project and file path, ordered by line and byte start positions. [crates/gcode/src/db/queries.rs:192-205]
- `read_calls_for_file` (function) component `read_calls_for_file [function]` (`ee16f0b6-e143-57c6-8af2-bb834b4c98b5`) lines 207-236 [crates/gcode/src/db/queries.rs:207-236]
  - Signature: `fn read_calls_for_file(`
  - Purpose: Queries the `code_calls` table to retrieve all function call relations for a specified project file, mapping database rows into a vector of `CallRelation` structs with type conversions and validation, ordered by line number. [crates/gcode/src/db/queries.rs:207-236]
- `non_empty` (function) component `non_empty [function]` (`4df2a72f-8c27-55ff-b0ce-df1c24fe4397`) lines 238-240 [crates/gcode/src/db/queries.rs:238-240]
  - Signature: `fn non_empty(value: String) -> Option<String> {`
  - Purpose: Returns `Some(value)` if the string is non-empty, otherwise returns `None`. [crates/gcode/src/db/queries.rs:238-240]
- `call_target_kind_from_str` (function) component `call_target_kind_from_str [function]` (`4cd2adae-7e54-50db-b297-2bdeee0c434a`) lines 242-249 [crates/gcode/src/db/queries.rs:242-249]
  - Signature: `fn call_target_kind_from_str(value: &str) -> anyhow::Result<CallTargetKind> {`
  - Purpose: Parses a string slice into a `CallTargetKind` enum variant via pattern matching, returning `anyhow::Result` with an error for unrecognized input. [crates/gcode/src/db/queries.rs:242-249]
- `symbol_select_columns` (function) component `symbol_select_columns [function]` (`2f2b38e7-762a-5aed-824e-ba3e1ecf385b`) lines 251-270 [crates/gcode/src/db/queries.rs:251-270]
  - Signature: `pub fn symbol_select_columns(alias: &str) -> String {`
  - Purpose: Returns a SQL SELECT clause enumerating symbol table columns with optional table aliasing and explicit BIGINT/TEXT type casts. [crates/gcode/src/db/queries.rs:251-270]
- `safe_symbol_select_alias` (function) component `safe_symbol_select_alias [function]` (`ddc3e953-a356-526e-8081-733019a6b8b8`) lines 272-281 [crates/gcode/src/db/queries.rs:272-281]
  - Signature: `fn safe_symbol_select_alias(alias: &str) -> bool {`
  - Purpose: Returns `true` if the alias is empty or matches a valid C-style identifier pattern: starting with an underscore or ASCII letter, followed only by underscores and ASCII alphanumeric characters. [crates/gcode/src/db/queries.rs:272-281]
- `symbol_select_columns_accepts_empty_or_safe_alias` (function) component `symbol_select_columns_accepts_empty_or_safe_alias [function]` (`9180db5c-1def-506b-bb9a-7cd4a1cc5915`) lines 288-292 [crates/gcode/src/db/queries.rs:288-292]
  - Signature: `fn symbol_select_columns_accepts_empty_or_safe_alias() {`
  - Purpose: Tests that `symbol_select_columns` correctly generates SQL column select clauses with or without table alias qualification based on empty or safe alias inputs. [crates/gcode/src/db/queries.rs:288-292]
- `symbol_select_columns_rejects_unsafe_alias` (function) component `symbol_select_columns_rejects_unsafe_alias [function]` (`0fc60be7-0559-58bc-8ace-2da15c4a3200`) lines 296-298 [crates/gcode/src/db/queries.rs:296-298]
  - Signature: `fn symbol_select_columns_rejects_unsafe_alias() {`
  - Purpose: Unit test verifying that `symbol_select_columns` safely rejects SQL injection attempts embedded in column alias parameters. [crates/gcode/src/db/queries.rs:296-298]

