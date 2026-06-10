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
  - 356-374
  - 376-386
  - 388-400
  - 402-447
  - 449-489
  - 491-508
  - 516-537
  - 540-547
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/visibility.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

`crates/gcode/src/visibility.rs` exposes 24 indexed API symbols.
[crates/gcode/src/visibility.rs:13-17]
[crates/gcode/src/visibility.rs:19-21]
[crates/gcode/src/visibility.rs:23-32]
[crates/gcode/src/visibility.rs:34-53]
[crates/gcode/src/visibility.rs:55-99]
[crates/gcode/src/visibility.rs:101-149]
[crates/gcode/src/visibility.rs:151-153]
[crates/gcode/src/visibility.rs:155-181]
[crates/gcode/src/visibility.rs:183-193]
[crates/gcode/src/visibility.rs:195-205]
[crates/gcode/src/visibility.rs:207-222]
[crates/gcode/src/visibility.rs:224-254]
[crates/gcode/src/visibility.rs:256-291]
[crates/gcode/src/visibility.rs:293-319]
[crates/gcode/src/visibility.rs:321-350]
[crates/gcode/src/visibility.rs:352-354]
[crates/gcode/src/visibility.rs:356-374]
[crates/gcode/src/visibility.rs:376-386]
[crates/gcode/src/visibility.rs:388-400]
[crates/gcode/src/visibility.rs:402-447]
[crates/gcode/src/visibility.rs:449-489]
[crates/gcode/src/visibility.rs:491-508]
[crates/gcode/src/visibility.rs:516-537]
[crates/gcode/src/visibility.rs:540-547]

## API Symbols

- `VisibleFile` (class) component `VisibleFile [class]` (`86045ddf-dd3e-5ee0-9edd-f7616cbfd92b`) lines 13-17 [crates/gcode/src/visibility.rs:13-17]
  - Signature: `pub struct VisibleFile {`
  - Purpose: `VisibleFile` is a plain data struct that represents a visible source file by storing its path, language, and symbol count as `String`, `String`, and `i64` fields, respectively. [crates/gcode/src/visibility.rs:13-17]
- `is_tombstone_language` (function) component `is_tombstone_language [function]` (`0135ea18-95fe-5013-9293-b327d5e0de6b`) lines 19-21 [crates/gcode/src/visibility.rs:19-21]
  - Signature: `pub fn is_tombstone_language(language: &str) -> bool {`
  - Purpose: Returns `true` exactly when `language` is equal to `TOMBSTONE_LANGUAGE`, and `false` otherwise. [crates/gcode/src/visibility.rs:19-21]
- `visible_project_ids` (function) component `visible_project_ids [function]` (`5fae9e61-67b9-5ad8-9ebb-1774b6e5c8d6`) lines 23-32 [crates/gcode/src/visibility.rs:23-32]
  - Signature: `pub fn visible_project_ids(ctx: &Context) -> Vec<String> {`
  - Purpose: Returns the set of project IDs visible in the current `Context` by yielding just `ctx.project_id` for `ProjectIndexScope::Single`, or both `overlay_project_id` and `parent_project_id` for `ProjectIndexScope::Overlay`. [crates/gcode/src/visibility.rs:23-32]
- `context_for_source_project` (function) component `context_for_source_project [function]` (`71063b35-b381-5489-a4f9-d0ca7acca366`) lines 34-53 [crates/gcode/src/visibility.rs:34-53]
  - Signature: `pub fn context_for_source_project(ctx: &Context, source_project_id: &str) -> Context {`
  - Purpose: Clones `ctx`, rewrites `project_id` to `source_project_id`, selects `project_root` from the matching overlay or parent root when `ctx.index_scope` is an `Overlay` for that project otherwise preserves the existing root, and forces `index_scope` to `ProjectIndexScope::Single`. [crates/gcode/src/visibility.rs:34-53]
- `indexed_file_exists` (function) component `indexed_file_exists [function]` (`27c6cd4e-13ed-59e8-a82d-891201ab3a49`) lines 55-99 [crates/gcode/src/visibility.rs:55-99]
  - Signature: `pub fn indexed_file_exists(conn: &mut Client, ctx: &Context, file_path: &str) -> bool {`
  - Purpose: Returns `true` if `code_indexed_files` contains a non-`TOMBSTONE_LANGUAGE` entry for `file_path` in the current project, or in overlay mode for the overlay project or the parent project when no overlay shadow row exists for that path, and `false` on any query/error path. [crates/gcode/src/visibility.rs:55-99]
- `content_chunks_exist` (function) component `content_chunks_exist [function]` (`c673496f-2343-592d-861d-dba9cd4c4bb4`) lines 101-149 [crates/gcode/src/visibility.rs:101-149]
  - Signature: `pub fn content_chunks_exist(conn: &mut Client, ctx: &Context, file_path: &str) -> bool {`
  - Purpose: `content_chunks_exist` returns `true` if the given `file_path` has any `code_content_chunks` in the current `Context` scope, checking only the current project in `Single` mode and, in `Overlay` mode, the overlay or parent project for non-`TOMBSTONE_LANGUAGE` indexed files while suppressing parent matches when the overlay shadows the file. [crates/gcode/src/visibility.rs:101-149]
- `symbol_is_visible` (function) component `symbol_is_visible [function]` (`91f309e1-db67-530e-bbaa-6e4c37078798`) lines 151-153 [crates/gcode/src/visibility.rs:151-153]
  - Signature: `pub fn symbol_is_visible(conn: &mut Client, ctx: &Context, symbol: &Symbol) -> bool {`
  - Purpose: `symbol_is_visible` returns the visibility of a `Symbol` by delegating to `project_path_is_visible` with the symbol’s `project_id` and `file_path` in the given client/context. [crates/gcode/src/visibility.rs:151-153]
- `project_path_is_visible` (function) component `project_path_is_visible [function]` (`d1b04c3b-ab21-5118-bf3b-7a778c4f2b03`) lines 155-181 [crates/gcode/src/visibility.rs:155-181]
  - Signature: `pub fn project_path_is_visible(`
  - Purpose: `project_path_is_visible` returns `true` only when `file_path` is visible in the current `ctx.index_scope`: for `Single` scope it must belong to `ctx.project_id` and pass `project_file_is_visible`, for `Overlay` scope it is visible in the overlay project directly or in the parent project only if not shadowed by an overlay row, and otherwise it returns `false`. [crates/gcode/src/visibility.rs:155-181]
- `project_file_is_visible` (function) component `project_file_is_visible [function]` (`96fc76d2-eb72-5f5b-a9ac-ceed4c550a72`) lines 183-193 [crates/gcode/src/visibility.rs:183-193]
  - Signature: `pub fn project_file_is_visible(conn: &mut Client, project_id: &str, file_path: &str) -> bool {`
  - Purpose: Returns `true` if `code_indexed_files` contains at least one row for the given `project_id` and `file_path` whose `language` is not `TOMBSTONE_LANGUAGE`, and returns `false` on any query or decode failure. [crates/gcode/src/visibility.rs:183-193]
- `overlay_has_row` (function) component `overlay_has_row [function]` (`c81df665-fa70-5875-8174-71aaa62125be`) lines 195-205 [crates/gcode/src/visibility.rs:195-205]
  - Signature: `pub fn overlay_has_row(conn: &mut Client, overlay_project_id: &str, file_path: &str) -> bool {`
  - Purpose: Returns `true` if `code_indexed_files` contains at least one row with the given `project_id` and `file_path`, and `false` if no such row exists or the query/boolean extraction fails. [crates/gcode/src/visibility.rs:195-205]
- `visible_symbol_by_id` (function) component `visible_symbol_by_id [function]` (`887f09cb-d3e1-50fd-b959-70f088e37689`) lines 207-222 [crates/gcode/src/visibility.rs:207-222]
  - Signature: `pub fn visible_symbol_by_id(`
  - Purpose: Fetches the `code_symbols` row for the given `id`, converts it into a `Symbol`, and returns `Some(symbol)` only if `symbol_is_visible(conn, ctx, &symbol)` is true, otherwise `Ok(None)`. [crates/gcode/src/visibility.rs:207-222]
- `visible_symbols_by_ids` (function) component `visible_symbols_by_ids [function]` (`ec279f15-db31-5e75-8a59-3d686a30edc4`) lines 224-254 [crates/gcode/src/visibility.rs:224-254]
  - Signature: `pub fn visible_symbols_by_ids(`
  - Purpose: Queries `code_symbols` for the supplied IDs with a parameterized `IN` clause, deduplicates results by symbol ID while preserving `file_path`/`line_start` ordering, and then filters the set through `filter_visible_symbols` for the given context, returning an empty vector when `ids` is empty. [crates/gcode/src/visibility.rs:224-254]
- `filter_visible_symbols` (function) component `filter_visible_symbols [function]` (`b01e50cb-daea-5b7d-873a-906cbe3203fa`) lines 256-291 [crates/gcode/src/visibility.rs:256-291]
  - Signature: `pub(crate) fn filter_visible_symbols(`
  - Purpose: `filter_visible_symbols` deduplicates the input symbols’ project IDs and file paths, fetches indexed file-language metadata for those projects/files (including overlay and parent projects when applicable), and returns only the symbols that `symbol_visible_from_file_languages` deems visible in the current `Context`. [crates/gcode/src/visibility.rs:256-291]
- `indexed_file_languages` (function) component `indexed_file_languages [function]` (`53c83206-a0f4-53d2-961c-5b01975bf8ea`) lines 293-319 [crates/gcode/src/visibility.rs:293-319]
  - Signature: `fn indexed_file_languages(`
  - Purpose: It returns a `HashMap<(project_id, file_path), language>` for the requested projects and paths by querying `code_indexed_files` with `ANY($1)`/`ANY($2)`, and yields an empty map immediately if either input slice is empty. [crates/gcode/src/visibility.rs:293-319]
- `symbol_visible_from_file_languages` (function) component `symbol_visible_from_file_languages [function]` (`c2fca560-7d45-58ba-b549-bdfd8edb41f0`) lines 321-350 [crates/gcode/src/visibility.rs:321-350]
  - Signature: `fn symbol_visible_from_file_languages(`
  - Purpose: Returns `true` only if the symbol belongs to the current index scope and its file’s indexed language is visible in `file_languages`: in `Single` scope it must come from `ctx.project_id`, in `Overlay` scope it is visible directly from the overlay project, or from the parent project only when the overlay does not shadow that file and the parent file’s language passes `indexed_language_is_visible`. [crates/gcode/src/visibility.rs:321-350]
- `indexed_language_is_visible` (function) component `indexed_language_is_visible [function]` (`bd298967-47f0-50aa-b422-f2828444f9a6`) lines 352-354 [crates/gcode/src/visibility.rs:352-354]
  - Signature: `fn indexed_language_is_visible(language: Option<&String>) -> bool {`
  - Purpose: Returns `true` only when `language` is `Some` and the contained string is not a tombstone language, otherwise `false`. [crates/gcode/src/visibility.rs:352-354]
- `visible_symbols_for_file` (function) component `visible_symbols_for_file [function]` (`9980aaeb-426d-5fe5-baaf-a0ec4b60ad67`) lines 356-374 [crates/gcode/src/visibility.rs:356-374]
  - Signature: `pub fn visible_symbols_for_file(`
  - Purpose: Returns the `Symbol` list for `file_path` from the current index scope, querying the single project directly or, in overlay mode, using the overlay project’s symbols when that file exists there and otherwise falling back to the parent project. [crates/gcode/src/visibility.rs:356-374]
- `query_symbols_for_file` (function) component `query_symbols_for_file [function]` (`3b59160a-421f-5d1b-aa52-f55d883e040c`) lines 376-386 [crates/gcode/src/visibility.rs:376-386]
  - Signature: `fn query_symbols_for_file(`
  - Purpose: Executes `symbols_for_file_sql()` with `project_id`, `file_path`, and `TOMBSTONE_LANGUAGE`, then converts the returned rows into a `Vec<Symbol>`. [crates/gcode/src/visibility.rs:376-386]
- `symbols_for_file_sql` (function) component `symbols_for_file_sql [function]` (`6dd33fb8-73ad-5f1a-aeaf-e0e237aba34f`) lines 388-400 [crates/gcode/src/visibility.rs:388-400]
  - Signature: `fn symbols_for_file_sql() -> String {`
  - Purpose: Constructs a parameterized SQL query that selects symbol columns for a given project and file from `code_symbols` joined with `code_indexed_files`, filters out a specified language, and orders results by `line_start` then `byte_start`. [crates/gcode/src/visibility.rs:388-400]
- `visible_kinds` (function) component `visible_kinds [function]` (`a6c4debc-7f3c-5c81-b024-58655e6be3bc`) lines 402-447 [crates/gcode/src/visibility.rs:402-447]
  - Signature: `pub fn visible_kinds(conn: &mut Client, ctx: &Context) -> anyhow::Result<Vec<String>> {`
  - Purpose: `visible_kinds` queries the database for the distinct `code_symbols.kind` values visible in the current `Context` scope, excluding tombstoned files, and in overlay mode merges overlay-project kinds with parent-project kinds that are not shadowed by overlay files, returning the sorted kinds as a `Vec<String>`. [crates/gcode/src/visibility.rs:402-447]
- `visible_tree` (function) component `visible_tree [function]` (`a0b6f4ba-f679-5480-953b-2075acf3e0ee`) lines 449-489 [crates/gcode/src/visibility.rs:449-489]
  - Signature: `pub fn visible_tree(conn: &mut Client, ctx: &Context) -> anyhow::Result<Vec<VisibleFile>> {`
  - Purpose: `visible_tree` queries `code_indexed_files` for the current project scope, excluding rows in `TOMBSTONE_LANGUAGE`, merging overlay and parent-project files without duplicates when `ctx.index_scope` is `Overlay`, ordering by `file_path`, and converting each row into a `VisibleFile` containing `file_path`, `language`, and `symbol_count`. [crates/gcode/src/visibility.rs:449-489]
- `tombstone_count` (function) component `tombstone_count [function]` (`4ead8e5e-8265-5c1e-9853-9d49fa1338f5`) lines 491-508 [crates/gcode/src/visibility.rs:491-508]
  - Signature: `pub fn tombstone_count(conn: &mut Client, ctx: &Context) -> usize {`
  - Purpose: Returns the number of `code_indexed_files` rows for the current overlay project whose `language` equals `TOMBSTONE_LANGUAGE`, or `0` if the context is not an overlay scope or the query/count conversion fails. [crates/gcode/src/visibility.rs:491-508]
- `visible_project_ids_include_overlay_before_parent` (function) component `visible_project_ids_include_overlay_before_parent [function]` (`162a38d5-758b-58f7-990c-c1174639197d`) lines 516-537 [crates/gcode/src/visibility.rs:516-537]
  - Signature: `fn visible_project_ids_include_overlay_before_parent() {`
  - Purpose: Verifies that `visible_project_ids(&ctx)` returns the overlay project ID before the parent project ID when `Context.index_scope` is `ProjectIndexScope::Overlay`. [crates/gcode/src/visibility.rs:516-537]
- `symbols_for_file_sql_qualifies_joined_symbol_columns` (function) component `symbols_for_file_sql_qualifies_joined_symbol_columns [function]` (`33991afd-8dd0-5894-b7a6-ecb1781b1ad7`) lines 540-547 [crates/gcode/src/visibility.rs:540-547]
  - Signature: `fn symbols_for_file_sql_qualifies_joined_symbol_columns() {`
  - Purpose: Verifies that `symbols_for_file_sql()` produces SQL selecting `code_symbols` columns with the `cs` table alias, includes a join to `code_indexed_files cf`, and does not emit an unqualified `SELECT id, project_id, file_path` projection. [crates/gcode/src/visibility.rs:540-547]

