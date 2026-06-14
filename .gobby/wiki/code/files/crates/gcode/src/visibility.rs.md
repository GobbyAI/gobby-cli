---
title: crates/gcode/src/visibility.rs
type: code_file
provenance:
- file: crates/gcode/src/visibility.rs
  ranges:
  - 13-17
  - 19-21
  - 23-32
  - 34-53
  - 55-99
  - 101-149
  - 151-153
  - 155-181
  - 183-193
  - 195-205
  - 207-222
  - 224-254
  - 256-291
  - 293-319
  - 321-350
  - 352-354
  - 356-362
  - 364-383
  - 385-395
  - 397-413
  - 415-427
  - 429-450
  - 452-497
  - 499-539
  - 541-558
  - 566-587
  - 590-598
  - 601-611
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/visibility.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Implements visibility and lookup logic for indexed code data in a project context, including the tombstone-language marker, visible project scoping, and conversion of a context to the appropriate source-project view. It provides helpers to determine whether files, content chunks, symbols, symbol kinds, and the file tree are visible in either single-project or overlay mode, with overlay handling that respects shadowing by the overlay project and excludes tombstoned files. The file also builds the SQL used to fetch visible symbols from the database and includes tests that verify project ordering, query shape, and overlay shadowing behavior.
[crates/gcode/src/visibility.rs:13-17]
[crates/gcode/src/visibility.rs:19-21]
[crates/gcode/src/visibility.rs:23-32]
[crates/gcode/src/visibility.rs:34-53]
[crates/gcode/src/visibility.rs:55-99]

## API Symbols

- `VisibleFile` (class) component `VisibleFile [class]` (`86045ddf-dd3e-5ee0-9edd-f7616cbfd92b`) lines 13-17 [crates/gcode/src/visibility.rs:13-17]
  - Signature: `pub struct VisibleFile {`
  - Purpose: `VisibleFile` is a public Rust data struct that models a visible file by storing its path, language identifier, and an `i64` symbol count. [crates/gcode/src/visibility.rs:13-17]
- `is_tombstone_language` (function) component `is_tombstone_language [function]` (`0135ea18-95fe-5013-9293-b327d5e0de6b`) lines 19-21 [crates/gcode/src/visibility.rs:19-21]
  - Signature: `pub fn is_tombstone_language(language: &str) -> bool {`
  - Purpose: Returns `true` if and only if `language` is exactly equal to `TOMBSTONE_LANGUAGE`, otherwise returns `false`. [crates/gcode/src/visibility.rs:19-21]
- `visible_project_ids` (function) component `visible_project_ids [function]` (`5fae9e61-67b9-5ad8-9ebb-1774b6e5c8d6`) lines 23-32 [crates/gcode/src/visibility.rs:23-32]
  - Signature: `pub fn visible_project_ids(ctx: &Context) -> Vec<String> {`
  - Purpose: Returns the visible project ID list for a `Context`, yielding only `ctx.project_id` in `ProjectIndexScope::Single` and both `overlay_project_id` and `parent_project_id` in `ProjectIndexScope::Overlay`. [crates/gcode/src/visibility.rs:23-32]
- `context_for_source_project` (function) component `context_for_source_project [function]` (`71063b35-b381-5489-a4f9-d0ca7acca366`) lines 34-53 [crates/gcode/src/visibility.rs:34-53]
  - Signature: `pub fn context_for_source_project(ctx: &Context, source_project_id: &str) -> Context {`
  - Purpose: Creates a cloned `Context` scoped to `source_project_id` by replacing `project_id`, selecting `project_root` from the overlay child or parent root when the current `index_scope` is an `Overlay` matching that project, otherwise preserving the existing root, and then forcing `index_scope` to `ProjectIndexScope::Single`. [crates/gcode/src/visibility.rs:34-53]
- `indexed_file_exists` (function) component `indexed_file_exists [function]` (`27c6cd4e-13ed-59e8-a82d-891201ab3a49`) lines 55-99 [crates/gcode/src/visibility.rs:55-99]
  - Signature: `pub fn indexed_file_exists(conn: &mut Client, ctx: &Context, file_path: &str) -> bool {`
  - Purpose: It returns `true` if `code_indexed_files` contains a non-`TOMBSTONE_LANGUAGE` row for `file_path` in the current project, or in overlay mode either in the overlay project itself or in the parent project when the overlay has no shadowing entry for that path, and otherwise `false` on query failure. [crates/gcode/src/visibility.rs:55-99]
- `content_chunks_exist` (function) component `content_chunks_exist [function]` (`c673496f-2343-592d-861d-dba9cd4c4bb4`) lines 101-149 [crates/gcode/src/visibility.rs:101-149]
  - Signature: `pub fn content_chunks_exist(conn: &mut Client, ctx: &Context, file_path: &str) -> bool {`
  - Purpose: Returns whether `file_path` has any matching rows in `code_content_chunks` for the active `Context`, querying `ctx.project_id` directly in `Single` scope and, in `Overlay` scope, treating overlay or parent-project chunks as present only when the indexed file is not `TOMBSTONE_LANGUAGE` and the parent path is not shadowed in the overlay, with any query failure yielding `false`. [crates/gcode/src/visibility.rs:101-149]
- `symbol_is_visible` (function) component `symbol_is_visible [function]` (`91f309e1-db67-530e-bbaa-6e4c37078798`) lines 151-153 [crates/gcode/src/visibility.rs:151-153]
  - Signature: `pub fn symbol_is_visible(conn: &mut Client, ctx: &Context, symbol: &Symbol) -> bool {`
  - Purpose: Returns `true` exactly when `project_path_is_visible(conn, ctx, &symbol.project_id, &symbol.file_path)` says the symbol’s project/file path is visible to the given client context. [crates/gcode/src/visibility.rs:151-153]
- `project_path_is_visible` (function) component `project_path_is_visible [function]` (`d1b04c3b-ab21-5118-bf3b-7a778c4f2b03`) lines 155-181 [crates/gcode/src/visibility.rs:155-181]
  - Signature: `pub fn project_path_is_visible(`
  - Purpose: Returns `true` only when `file_path` is visible for `project_id` under `ctx.index_scope` by enforcing single-project matching, allowing the overlay project directly, allowing the overlay parent only when the path is visible there and not shadowed by an overlay row, and rejecting all other project IDs. [crates/gcode/src/visibility.rs:155-181]
- `project_file_is_visible` (function) component `project_file_is_visible [function]` (`96fc76d2-eb72-5f5b-a9ac-ceed4c550a72`) lines 183-193 [crates/gcode/src/visibility.rs:183-193]
  - Signature: `pub fn project_file_is_visible(conn: &mut Client, project_id: &str, file_path: &str) -> bool {`
  - Purpose: Returns `true` when `code_indexed_files` contains at least one row matching the given `project_id` and `file_path` whose `language` is not `TOMBSTONE_LANGUAGE`, and returns `false` on no match or any query/decoding error. [crates/gcode/src/visibility.rs:183-193]
- `overlay_has_row` (function) component `overlay_has_row [function]` (`c81df665-fa70-5875-8174-71aaa62125be`) lines 195-205 [crates/gcode/src/visibility.rs:195-205]
  - Signature: `pub fn overlay_has_row(conn: &mut Client, overlay_project_id: &str, file_path: &str) -> bool {`
  - Purpose: Returns `true` if `code_indexed_files` contains a row whose `project_id` equals `overlay_project_id` and whose `file_path` equals `file_path`, and `false` if the lookup or boolean extraction fails. [crates/gcode/src/visibility.rs:195-205]
- `visible_symbol_by_id` (function) component `visible_symbol_by_id [function]` (`887f09cb-d3e1-50fd-b959-70f088e37689`) lines 207-222 [crates/gcode/src/visibility.rs:207-222]
  - Signature: `pub fn visible_symbol_by_id(`
  - Purpose: Queries `code_symbols` for the row with the given `id`, converts it to a `Symbol`, and returns `Some(symbol)` only if `symbol_is_visible(conn, ctx, &symbol)` is true, otherwise `None` (propagating any database or parsing errors). [crates/gcode/src/visibility.rs:207-222]
- `visible_symbols_by_ids` (function) component `visible_symbols_by_ids [function]` (`ec279f15-db31-5e75-8a59-3d686a30edc4`) lines 224-254 [crates/gcode/src/visibility.rs:224-254]
  - Signature: `pub fn visible_symbols_by_ids(`
  - Purpose: Fetches `code_symbols` rows for the given IDs with a parameterized `IN` query ordered by `file_path` and `line_start`, deduplicates them by `symbol.id`, and returns only the symbols visible under `ctx` via `filter_visible_symbols` (or an empty vector if `ids` is empty). [crates/gcode/src/visibility.rs:224-254]
- `filter_visible_symbols` (function) component `filter_visible_symbols [function]` (`b01e50cb-daea-5b7d-873a-906cbe3203fa`) lines 256-291 [crates/gcode/src/visibility.rs:256-291]
  - Signature: `pub(crate) fn filter_visible_symbols(`
  - Purpose: It returns the input unchanged when empty, otherwise deduplicates the symbols’ project IDs and file paths, fetches the indexed file languages for those projects and paths, and filters the `Symbol` list to only those visible according to `symbol_visible_from_file_languages(ctx, ...)`. [crates/gcode/src/visibility.rs:256-291]
- `indexed_file_languages` (function) component `indexed_file_languages [function]` (`53c83206-a0f4-53d2-961c-5b01975bf8ea`) lines 293-319 [crates/gcode/src/visibility.rs:293-319]
  - Signature: `fn indexed_file_languages(`
  - Purpose: Returns a `HashMap<(project_id, file_path), language>` by querying `code_indexed_files` for rows matching any of the given `project_ids` and `file_paths`, or returns an empty map immediately if either input slice is empty. [crates/gcode/src/visibility.rs:293-319]
- `symbol_visible_from_file_languages` (function) component `symbol_visible_from_file_languages [function]` (`c2fca560-7d45-58ba-b549-bdfd8edb41f0`) lines 321-350 [crates/gcode/src/visibility.rs:321-350]
  - Signature: `fn symbol_visible_from_file_languages(`
  - Purpose: Returns `true` only if the symbol is in the active project scope and its file’s indexed language is visible: in `Single` scope it must belong to `ctx.project_id`, in `Overlay` scope overlay-project symbols are visible when their overlay file language is visible, parent-project symbols are visible only when the overlay has no file for that path and the parent file language is visible, and all other overlay cases return `false`. [crates/gcode/src/visibility.rs:321-350]
- `indexed_language_is_visible` (function) component `indexed_language_is_visible [function]` (`bd298967-47f0-50aa-b422-f2828444f9a6`) lines 352-354 [crates/gcode/src/visibility.rs:352-354]
  - Signature: `fn indexed_language_is_visible(language: Option<&String>) -> bool {`
  - Purpose: Returns `true` only when `language` is `Some` and the referenced language string is not a tombstone language; otherwise it returns `false`. [crates/gcode/src/visibility.rs:352-354]
- `visible_symbols_for_file` (function) component `visible_symbols_for_file [function]` (`9980aaeb-426d-5fe5-baaf-a0ec4b60ad67`) lines 356-362 [crates/gcode/src/visibility.rs:356-362]
  - Signature: `pub fn visible_symbols_for_file(`
  - Purpose: Returns the visible symbols for the given `file_path` by wrapping it in a single-element path list and delegating to `visible_symbols_for_files`, propagating the resulting `anyhow::Result<Vec<Symbol>>`. [crates/gcode/src/visibility.rs:356-362]
- `visible_symbols_for_files` (function) component `visible_symbols_for_files [function]` (`85594023-9138-5b6f-9e35-a7f830cf11de`) lines 364-383 [crates/gcode/src/visibility.rs:364-383]
  - Signature: `pub fn visible_symbols_for_files(`
  - Purpose: Returns an empty list for no input paths, otherwise dispatches to the appropriate symbol lookup query for the current `ctx.index_scope` (`Single` project or `Overlay`) and returns the resulting `Vec<Symbol>` or propagated error. [crates/gcode/src/visibility.rs:364-383]
- `query_symbols_for_files` (function) component `query_symbols_for_files [function]` (`ab0800fd-3780-5f87-b3c5-ef20c052c9e5`) lines 385-395 [crates/gcode/src/visibility.rs:385-395]
  - Signature: `fn query_symbols_for_files(`
  - Purpose: Executes the `symbols_for_files_sql()` query against the database for the given `project_id` and `file_paths` with `TOMBSTONE_LANGUAGE` as a filter, then converts the returned rows into a `Vec<Symbol>`. [crates/gcode/src/visibility.rs:385-395]
- `query_overlay_symbols_for_files` (function) component `query_overlay_symbols_for_files [function]` (`9d15f8ef-5ed1-5a1f-8fe0-4be4c2f4060c`) lines 397-413 [crates/gcode/src/visibility.rs:397-413]
  - Signature: `fn query_overlay_symbols_for_files(`
  - Purpose: Executes `overlay_symbols_for_files_sql()` on `conn` with the overlay project ID, parent project ID, file paths, and `TOMBSTONE_LANGUAGE`, then maps each returned row into a `Symbol` and returns `anyhow::Result<Vec<Symbol>>`. [crates/gcode/src/visibility.rs:397-413]
- `symbols_for_files_sql` (function) component `symbols_for_files_sql [function]` (`af95f309-122c-53a9-be0f-c9283769c407`) lines 415-427 [crates/gcode/src/visibility.rs:415-427]
  - Signature: `fn symbols_for_files_sql() -> String {`
  - Purpose: Builds a parameterized SQL `SELECT` that fetches symbol rows for a project from `code_symbols` joined to `code_indexed_files`, filters by `project_id`, a file-path array, and a language exclusion, then orders by `file_path`, `line_start`, and `byte_start`. [crates/gcode/src/visibility.rs:415-427]
- `overlay_symbols_for_files_sql` (function) component `overlay_symbols_for_files_sql [function]` (`0a7779c0-e57f-5686-bc51-c8731d6cd7f8`) lines 429-450 [crates/gcode/src/visibility.rs:429-450]
  - Signature: `fn overlay_symbols_for_files_sql() -> String {`
  - Purpose: Returns a parameterized SQL query that selects symbol rows for the requested file paths, joins `code_indexed_files` to filter out a language, and overlays symbols from a secondary project only when the primary project has no symbol entry for the same file, ordered by file path and source position. [crates/gcode/src/visibility.rs:429-450]
- `visible_kinds` (function) component `visible_kinds [function]` (`ce6d4fbc-ca1d-5bb3-9f6b-09a4dc5e08f8`) lines 452-497 [crates/gcode/src/visibility.rs:452-497]
  - Signature: `pub fn visible_kinds(conn: &mut Client, ctx: &Context) -> anyhow::Result<Vec<String>> {`
  - Purpose: Returns the sorted list of distinct `code_symbols.kind` values visible in the current `Context`’s index scope, querying the project alone for `Single` scope or unioning overlay and unshadowed parent symbols for `Overlay` scope while excluding tombstoned files. [crates/gcode/src/visibility.rs:452-497]
- `visible_tree` (function) component `visible_tree [function]` (`3f983b55-9fe7-5d82-b47e-059f94972071`) lines 499-539 [crates/gcode/src/visibility.rs:499-539]
  - Signature: `pub fn visible_tree(conn: &mut Client, ctx: &Context) -> anyhow::Result<Vec<VisibleFile>> {`
  - Purpose: Fetches all non-`TOMBSTONE_LANGUAGE` rows from `code_indexed_files` visible under `ctx.index_scope` (project-only for `Single`, or overlay files plus parent files not shadowed by the overlay for `Overlay`) and maps each row into a `VisibleFile`. [crates/gcode/src/visibility.rs:499-539]
- `tombstone_count` (function) component `tombstone_count [function]` (`342a8eab-150d-572d-b5e8-bac043bb8d40`) lines 541-558 [crates/gcode/src/visibility.rs:541-558]
  - Signature: `pub fn tombstone_count(conn: &mut Client, ctx: &Context) -> usize {`
  - Purpose: `tombstone_count` returns `0` unless `ctx.index_scope` is an `Overlay`, in which case it queries `code_indexed_files` for the overlay project’s rows with `language = TOMBSTONE_LANGUAGE`, converts the `COUNT(*)` result to `usize`, and falls back to `0` on any query, row-read, or conversion failure. [crates/gcode/src/visibility.rs:541-558]
- `visible_project_ids_include_overlay_before_parent` (function) component `visible_project_ids_include_overlay_before_parent [function]` (`cbcb1617-93ce-5767-b79f-efe7b4e92f41`) lines 566-587 [crates/gcode/src/visibility.rs:566-587]
  - Signature: `fn visible_project_ids_include_overlay_before_parent() {`
  - Purpose: Tests that `visible_project_ids(&ctx)` returns the overlay project ID first and the parent project ID second when the index scope is `ProjectIndexScope::Overlay`. [crates/gcode/src/visibility.rs:566-587]
- `symbols_for_file_sql_qualifies_joined_symbol_columns` (function) component `symbols_for_file_sql_qualifies_joined_symbol_columns [function]` (`9ffef222-e02b-53b6-b5fc-c62968218301`) lines 590-598 [crates/gcode/src/visibility.rs:590-598]
  - Signature: `fn symbols_for_file_sql_qualifies_joined_symbol_columns() {`
  - Purpose: Asserts that `symbols_for_files_sql()` generates a SQL query that uses `cs`-qualified `code_symbols` columns, joins `code_indexed_files`, filters with `cs.file_path = ANY($2)`, and does not fall back to unqualified `SELECT id, project_id, file_path`. [crates/gcode/src/visibility.rs:590-598]
- `overlay_symbols_for_files_sql_batches_paths_and_preserves_overlay_shadowing` (function) component `overlay_symbols_for_files_sql_batches_paths_and_preserves_overlay_shadowing [function]` (`084373a5-89ac-5b0e-9de2-b797ec84980d`) lines 601-611 [crates/gcode/src/visibility.rs:601-611]
  - Signature: `fn overlay_symbols_for_files_sql_batches_paths_and_preserves_overlay_shadowing() {`
  - Purpose: This test verifies that `overlay_symbols_for_files_sql()` generates a query that batches file paths with `cs.file_path = ANY($3)`, binds project IDs to `$1` and `$2`, enforces overlay shadowing via a `NOT EXISTS` clause keyed on `shadow.project_id = $1 AND shadow.file_path = cs.file_path`, and does not incorrectly parameterize `cs.file_path` as `$3`. [crates/gcode/src/visibility.rs:601-611]

