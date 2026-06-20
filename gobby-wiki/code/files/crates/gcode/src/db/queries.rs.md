---
title: crates/gcode/src/db/queries.rs
type: code_file
provenance:
- file: crates/gcode/src/db/queries.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/db/queries.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/db/queries.rs` exposes 36 indexed API symbols.

## How it fits

`crates/gcode/src/db/queries.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GraphFileFacts` | class | 'GraphFileFacts' is a file-level fact record that stores a source file path along with its imported relations, declared symbols, and call relations. [crates/gcode/src/db/queries.rs:8-13] |
| `list_indexed_file_paths` | function | Queries 'code_indexed_files' for the given 'project_id', orders results by 'file_path', and returns the indexed file paths as a 'Vec<String>' propagated through 'anyhow::Result'. [crates/gcode/src/db/queries.rs:15-26] |
| `indexed_project_exists` | function | Returns 'true' if a row with the given 'project_id' exists in 'code_indexed_projects', otherwise 'false', by executing a parameterized 'SELECT 1' lookup and checking whether the query returns a row. [crates/gcode/src/db/queries.rs:28-38] |
| `read_graph_file_facts` | function | Reads a file’s graph-related facts from the database by fetching its imports, symbol definitions, and calls for a given project, then returns them bundled into a 'GraphFileFacts' with the file path. [crates/gcode/src/db/queries.rs:40-55] |
| `indexed_file_exists` | function | Returns 'true' if 'code_indexed_files' contains a row matching the given 'project_id' and 'file_path', otherwise 'false', propagating any database error via 'anyhow::Result<bool>'. [crates/gcode/src/db/queries.rs:57-69] |
| `mark_graph_sync_attempted` | function | Updates the 'code_indexed_files' row for the given 'project_id' and 'file_path' to set 'graph_synced = false' and 'graph_sync_attempted_at = NOW()', returning 'true' if any row was modified. [crates/gcode/src/db/queries.rs:71-83] |
| `mark_graph_synced` | function | Updates 'code_indexed_files' to set 'graph_synced = true' and 'graph_sync_attempted_at = NOW()' for the given 'project_id' and 'file_path', returning 'true' if at least one row was modified. [crates/gcode/src/db/queries.rs:85-97] |
| `reset_graph_sync_for_project` | function | Resets graph sync state for all 'code_indexed_files' rows in the specified project by setting 'graph_synced = false' and clearing 'graph_sync_attempted_at', returning the number of updated rows. [crates/gcode/src/db/queries.rs:99-109] |
| `mark_vectors_synced` | function | Sets 'vectors_synced = true' for the 'code_indexed_files' row matching the given 'project_id' and 'file_path', and returns 'true' if at least one row was updated. [crates/gcode/src/db/queries.rs:111-123] |
| `mark_project_vectors_synced` | function | Updates all 'code_indexed_files' rows for the given 'project_id' to set 'vectors_synced = true' and returns the number of affected rows as a 'u64' wrapped in 'anyhow::Result'. [crates/gcode/src/db/queries.rs:125-135] |
| `file_vectors_synced` | function | Queries 'code_indexed_files' for the given 'project_id' and 'file_path' and returns 'Ok(Some(vectors_synced))' if a matching row exists, otherwise 'Ok(None)'. [crates/gcode/src/db/queries.rs:141-156] |
| `reset_vectors_sync_for_project` | function | Marks all rows in 'code_indexed_files' for the given 'project_id' as unsynced by setting 'vectors_synced = false', and returns the number of updated rows. [crates/gcode/src/db/queries.rs:158-168] |
| `read_imports_for_file` | function | Queries 'code_imports' for the given 'project_id' and 'file_path', orders by 'target_module', and returns the rows mapped into 'ImportRelation' values containing the source file path and imported module name. [crates/gcode/src/db/queries.rs:170-190] |
| `read_symbols_for_file` | function | Queries 'code_symbols' for the given 'project_id' and 'file_path', orders results by 'line_start' and 'byte_start', and returns the rows converted into a 'Vec<Symbol>' or propagates any database/row-mapping error. [crates/gcode/src/db/queries.rs:192-205] |
| `read_calls_for_file` | function | Queries the 'code_calls' table for all call records in a given 'project_id' and 'file_path', orders them by line, caller, and callee name, and converts the result rows into a 'Vec<CallRelation>'. [crates/gcode/src/db/queries.rs:207-221] |
| `call_relation_from_row` | function | Converts a 'postgres::Row' into a 'CallRelation' by extracting the required columns, validating and normalizing string fields, parsing 'callee_target_kind', and converting 'line' from 'i64' to 'usize', returning an error on any missing or invalid value. [crates/gcode/src/db/queries.rs:223-236] |
| `read_local_import_calls` | function | Queries 'code_calls' for the given 'project_id' and file paths, filtered to 'callee_target_kind = 'local_import'', orders the results deterministically by file and location, and converts each row into a 'CallRelation', returning an empty vector when no paths are provided. [crates/gcode/src/db/queries.rs:241-259] |
| `read_project_local_import_calls` | function | Queries 'code_calls' for a given 'project_id' to fetch and return all 'CallRelation' records whose 'callee_target_kind' is 'local_import', ordered by file path, line, caller symbol, and callee name. [crates/gcode/src/db/queries.rs:261-274] |
| `resolve_local_callee_symbol_id` | function | Queries 'code_symbols' for symbols in the given project and target files with the specified name, converts the matching rows into 'LocalCalleeCandidate's, and returns the ID selected by 'select_local_callee_candidate_id', or 'None' if the inputs are empty or no candidate is chosen. [crates/gcode/src/db/queries.rs:289-321] |
| `resolve_default_import_symbol_id` | function | Queries top-level 'function'/'class'/'type' symbols for the given project files, converts them into 'LocalCalleeCandidate's, and returns the ID selected by 'select_default_import_candidate_id', or 'None' if no target files are provided. [crates/gcode/src/db/queries.rs:323-357] |
| `LocalCalleeCandidate` | class | 'LocalCalleeCandidate' is a data structure representing a potential locally resolved callee, identified by 'id', classified by 'kind', and optionally linked to a parent symbol via 'parent_symbol_id'. [crates/gcode/src/db/queries.rs:360-364] |
| `select_local_callee_candidate_id` | function | Selects a unique candidate ID by priority order: top-level functions/classes, then methods, then module-scoped functions, then top-level types, returning 'None' when no unambiguous match exists. [crates/gcode/src/db/queries.rs:366-413] |
| `select_default_import_candidate_id` | function | Returns the unique 'id' of the only top-level candidate whose 'parent_symbol_id' is 'None' and whose 'kind' is 'function', 'class', or 'type', or 'None' if no unique such candidate exists. [crates/gcode/src/db/queries.rs:415-425] |
| `unique_id` | function | Returns the sole 'String' cloned from 'ids' when the slice contains exactly one element, otherwise returns 'None'. [crates/gcode/src/db/queries.rs:427-432] |

_5 more symbol(s) not shown — run `gcode outline crates/gcode/src/db/queries.rs` for the full list._

_Verified by 7 in-file unit tests._

