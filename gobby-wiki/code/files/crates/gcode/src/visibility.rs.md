---
title: crates/gcode/src/visibility.rs
type: code_file
provenance:
- file: crates/gcode/src/visibility.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/visibility.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/visibility.rs` exposes 28 indexed API symbols.

## How it fits

`crates/gcode/src/visibility.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `VisibleFile` | class | 'VisibleFile' is a public Rust struct that models a file visible in the UI or index, storing its path, detected language, and an 'i64' symbol count. [crates/gcode/src/visibility.rs:13-17] |
| `is_tombstone_language` | function | Returns 'true' when 'language' exactly matches the 'TOMBSTONE_LANGUAGE' constant, and 'false' otherwise. [crates/gcode/src/visibility.rs:19-21] |
| `visible_project_ids` | function | Returns the list of project IDs visible in the current context, yielding either the single current project ID or, for an overlay scope, the overlay project ID followed by its parent project ID. [crates/gcode/src/visibility.rs:23-32] |
| `context_for_source_project` | function | Creates a cloned 'Context' scoped to a specified 'source_project_id' by replacing 'project_id', resolving 'project_root' to the matching overlay or parent root when the current 'index_scope' is an overlay, and then forcing 'index_scope' to 'ProjectIndexScope::Single'. [crates/gcode/src/visibility.rs:34-53] |
| `indexed_file_exists` | function | Returns 'true' if 'file_path' has a non-'TOMBSTONE_LANGUAGE' row in 'code_indexed_files' for the current project scope, using the overlay project and falling back to the parent only when the overlay does not shadow that path, and 'false' on any query or decode failure. [crates/gcode/src/visibility.rs:55-99] |
| `content_chunks_exist` | function | Returns 'true' if the database contains any 'code_content_chunks' for 'file_path' in the current index scope, using a simple project/file existence check for 'Single' scopes and an overlay-aware query that excludes tombstoned/shadowed files and non-tombstone-language chunks for 'Overlay' scopes, otherwise 'false' on query or decoding failure. [crates/gcode/src/visibility.rs:101-149] |
| `symbol_is_visible` | function | Returns whether the given 'Symbol' is visible in the current 'Context' by delegating to 'project_path_is_visible' with the symbol’s 'project_id' and 'file_path'. [crates/gcode/src/visibility.rs:151-153] |
| `project_path_is_visible` | function | Returns 'true' only if the given 'project_id'/'file_path' is visible under the current 'Context' index scope: in 'Single' scope it must match 'ctx.project_id' and be visible via 'project_file_is_visible', in 'Overlay' scope it is visible for the overlay project itself, visible for the parent project only when no overlay row exists for that path and the parent file is visible, and 'false' for all other projects. [crates/gcode/src/visibility.rs:155-181] |
| `project_file_is_visible` | function | Returns 'true' if 'code_indexed_files' contains a row for the given 'project_id' and 'file_path' whose 'language' is not 'TOMBSTONE_LANGUAGE', and 'false' on no match or any query/decoding error. [crates/gcode/src/visibility.rs:183-193] |
| `overlay_has_row` | function | Returns 'true' if the 'code_indexed_files' table contains at least one row matching the given 'overlay_project_id' and 'file_path', and returns 'false' if the query fails or the result cannot be read. [crates/gcode/src/visibility.rs:195-205] |
| `visible_symbol_by_id` | function | Fetches a 'code_symbols' row by 'id', converts it to 'Symbol', and returns 'Some(symbol)' only if 'symbol_is_visible(conn, ctx, &symbol)' is true, otherwise 'None'. [crates/gcode/src/visibility.rs:207-222] |
| `visible_symbols_by_ids` | function | Queries 'code_symbols' for the given IDs, de-duplicates returned symbols by 'id', preserves 'file_path'/'line_start' ordering, and then filters the results through 'filter_visible_symbols' before returning them. [crates/gcode/src/visibility.rs:224-254] |
| `filter_visible_symbols` | function | 'filter_visible_symbols' collects the relevant project IDs and file paths from the input symbols, fetches indexed file-language metadata for them, and returns only the symbols that 'symbol_visible_from_file_languages' deems visible in the current 'Context'. [crates/gcode/src/visibility.rs:256-291] |
| `indexed_file_languages` | function | Returns a 'HashMap<(project_id, file_path), language>' for the requested projects and paths by querying 'code_indexed_files', or an empty map if either input slice is empty. [crates/gcode/src/visibility.rs:293-319] |
| `symbol_visible_from_file_languages` | function | Returns 'true' only when a symbol is in the currently indexed scope and its file’s indexed language is visible: in 'Single' scope it must belong to the current project, in 'Overlay' scope overlay symbols are checked directly, parent-project symbols are visible only if the overlay lacks that file and the parent file’s language is visible, and all other symbols are hidden. [crates/gcode/src/visibility.rs:321-350] |
| `indexed_language_is_visible` | function | Returns 'true' only when 'language' is 'Some' and the contained string is not a tombstone language, otherwise 'false'. [crates/gcode/src/visibility.rs:352-354] |
| `visible_symbols_for_file` | function | Returns the visible symbols for a single file path by delegating to 'visible_symbols_for_files' with a one-element file list and propagating its 'anyhow::Result<Vec<Symbol>>'. [crates/gcode/src/visibility.rs:356-362] |
| `visible_symbols_for_files` | function | Returns an empty vector when 'file_paths' is empty, otherwise dispatches to either 'query_symbols_for_files' for 'ProjectIndexScope::Single' or 'query_overlay_symbols_for_files' for 'ProjectIndexScope::Overlay', using the appropriate project IDs to fetch visible 'Symbol's from the database. [crates/gcode/src/visibility.rs:364-383] |
| `query_symbols_for_files` | function | Queries the database for symbol rows associated with the given 'project_id' and list of 'file_paths', filtered by 'TOMBSTONE_LANGUAGE', and converts the returned rows into a 'Vec<Symbol>'. [crates/gcode/src/visibility.rs:385-395] |
| `query_overlay_symbols_for_files` | function | Queries the database for symbols associated with the given file paths in an overlay project and its parent project, using a tombstone-language filter, then converts the resulting rows into 'Symbol' values. [crates/gcode/src/visibility.rs:397-413] |
| `symbols_for_files_sql` | function | Builds a parameterized SQL query that selects symbol columns from 'code_symbols', joins 'code_indexed_files' on project and file path, filters by project ID, a file-path array, and excluded language, and orders results by file path, line start, and byte start. [crates/gcode/src/visibility.rs:415-427] |
| `overlay_symbols_for_files_sql` | function | Builds and returns a SQL query that selects symbol columns from 'code_symbols' joined to 'code_indexed_files', filtering by a file-path list, excluding a specified language, and overlaying symbols from a secondary project only when the primary project lacks the file, ordered by file path and source position. [crates/gcode/src/visibility.rs:429-450] |
| `visible_kinds` | function | Returns the sorted list of distinct symbol kinds visible in the current index scope by querying 'code_symbols' joined with 'code_indexed_files', excluding tombstoned-language files and, for overlays, unioning overlay and unshadowed parent kinds. [crates/gcode/src/visibility.rs:452-497] |
| `visible_tree` | function | 'visible_tree' queries 'code_indexed_files' for all non-tombstone files visible in the current project scope, using either the single project or an overlay-plus-parent fallback merge ordered by 'file_path', and converts the result rows into a 'Vec<VisibleFile>' with 'file_path', 'language', and 'symbol_count'. [crates/gcode/src/visibility.rs:499-539] |

_1 more symbol(s) not shown — run `gcode outline crates/gcode/src/visibility.rs` for the full list._

_Verified by 3 in-file unit tests._

