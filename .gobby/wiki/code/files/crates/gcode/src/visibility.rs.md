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

`crates/gcode/src/visibility.rs` exposes 28 indexed API symbols.
[crates/gcode/src/visibility.rs:13-17]
[crates/gcode/src/visibility.rs:19-21]
[crates/gcode/src/visibility.rs:23-32]
[crates/gcode/src/visibility.rs:34-53]
[crates/gcode/src/visibility.rs:55-99]

## API Symbols

- `VisibleFile` (class) component `VisibleFile [class]` (`86045ddf-dd3e-5ee0-9edd-f7616cbfd92b`) lines 13-17 [crates/gcode/src/visibility.rs:13-17]
  - Signature: `pub struct VisibleFile {`
  - Purpose: Indexed class `VisibleFile` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:13-17]
- `is_tombstone_language` (function) component `is_tombstone_language [function]` (`0135ea18-95fe-5013-9293-b327d5e0de6b`) lines 19-21 [crates/gcode/src/visibility.rs:19-21]
  - Signature: `pub fn is_tombstone_language(language: &str) -> bool {`
  - Purpose: Indexed function `is_tombstone_language` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:19-21]
- `visible_project_ids` (function) component `visible_project_ids [function]` (`5fae9e61-67b9-5ad8-9ebb-1774b6e5c8d6`) lines 23-32 [crates/gcode/src/visibility.rs:23-32]
  - Signature: `pub fn visible_project_ids(ctx: &Context) -> Vec<String> {`
  - Purpose: Indexed function `visible_project_ids` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:23-32]
- `context_for_source_project` (function) component `context_for_source_project [function]` (`71063b35-b381-5489-a4f9-d0ca7acca366`) lines 34-53 [crates/gcode/src/visibility.rs:34-53]
  - Signature: `pub fn context_for_source_project(ctx: &Context, source_project_id: &str) -> Context {`
  - Purpose: Indexed function `context_for_source_project` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:34-53]
- `indexed_file_exists` (function) component `indexed_file_exists [function]` (`27c6cd4e-13ed-59e8-a82d-891201ab3a49`) lines 55-99 [crates/gcode/src/visibility.rs:55-99]
  - Signature: `pub fn indexed_file_exists(conn: &mut Client, ctx: &Context, file_path: &str) -> bool {`
  - Purpose: Indexed function `indexed_file_exists` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:55-99]
- `content_chunks_exist` (function) component `content_chunks_exist [function]` (`c673496f-2343-592d-861d-dba9cd4c4bb4`) lines 101-149 [crates/gcode/src/visibility.rs:101-149]
  - Signature: `pub fn content_chunks_exist(conn: &mut Client, ctx: &Context, file_path: &str) -> bool {`
  - Purpose: Indexed function `content_chunks_exist` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:101-149]
- `symbol_is_visible` (function) component `symbol_is_visible [function]` (`91f309e1-db67-530e-bbaa-6e4c37078798`) lines 151-153 [crates/gcode/src/visibility.rs:151-153]
  - Signature: `pub fn symbol_is_visible(conn: &mut Client, ctx: &Context, symbol: &Symbol) -> bool {`
  - Purpose: Indexed function `symbol_is_visible` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:151-153]
- `project_path_is_visible` (function) component `project_path_is_visible [function]` (`d1b04c3b-ab21-5118-bf3b-7a778c4f2b03`) lines 155-181 [crates/gcode/src/visibility.rs:155-181]
  - Signature: `pub fn project_path_is_visible(`
  - Purpose: Indexed function `project_path_is_visible` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:155-181]
- `project_file_is_visible` (function) component `project_file_is_visible [function]` (`96fc76d2-eb72-5f5b-a9ac-ceed4c550a72`) lines 183-193 [crates/gcode/src/visibility.rs:183-193]
  - Signature: `pub fn project_file_is_visible(conn: &mut Client, project_id: &str, file_path: &str) -> bool {`
  - Purpose: Indexed function `project_file_is_visible` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:183-193]
- `overlay_has_row` (function) component `overlay_has_row [function]` (`c81df665-fa70-5875-8174-71aaa62125be`) lines 195-205 [crates/gcode/src/visibility.rs:195-205]
  - Signature: `pub fn overlay_has_row(conn: &mut Client, overlay_project_id: &str, file_path: &str) -> bool {`
  - Purpose: Indexed function `overlay_has_row` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:195-205]
- `visible_symbol_by_id` (function) component `visible_symbol_by_id [function]` (`887f09cb-d3e1-50fd-b959-70f088e37689`) lines 207-222 [crates/gcode/src/visibility.rs:207-222]
  - Signature: `pub fn visible_symbol_by_id(`
  - Purpose: Indexed function `visible_symbol_by_id` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:207-222]
- `visible_symbols_by_ids` (function) component `visible_symbols_by_ids [function]` (`ec279f15-db31-5e75-8a59-3d686a30edc4`) lines 224-254 [crates/gcode/src/visibility.rs:224-254]
  - Signature: `pub fn visible_symbols_by_ids(`
  - Purpose: Indexed function `visible_symbols_by_ids` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:224-254]
- `filter_visible_symbols` (function) component `filter_visible_symbols [function]` (`b01e50cb-daea-5b7d-873a-906cbe3203fa`) lines 256-291 [crates/gcode/src/visibility.rs:256-291]
  - Signature: `pub(crate) fn filter_visible_symbols(`
  - Purpose: Indexed function `filter_visible_symbols` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:256-291]
- `indexed_file_languages` (function) component `indexed_file_languages [function]` (`53c83206-a0f4-53d2-961c-5b01975bf8ea`) lines 293-319 [crates/gcode/src/visibility.rs:293-319]
  - Signature: `fn indexed_file_languages(`
  - Purpose: Indexed function `indexed_file_languages` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:293-319]
- `symbol_visible_from_file_languages` (function) component `symbol_visible_from_file_languages [function]` (`c2fca560-7d45-58ba-b549-bdfd8edb41f0`) lines 321-350 [crates/gcode/src/visibility.rs:321-350]
  - Signature: `fn symbol_visible_from_file_languages(`
  - Purpose: Indexed function `symbol_visible_from_file_languages` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:321-350]
- `indexed_language_is_visible` (function) component `indexed_language_is_visible [function]` (`bd298967-47f0-50aa-b422-f2828444f9a6`) lines 352-354 [crates/gcode/src/visibility.rs:352-354]
  - Signature: `fn indexed_language_is_visible(language: Option<&String>) -> bool {`
  - Purpose: Indexed function `indexed_language_is_visible` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:352-354]
- `visible_symbols_for_file` (function) component `visible_symbols_for_file [function]` (`9980aaeb-426d-5fe5-baaf-a0ec4b60ad67`) lines 356-362 [crates/gcode/src/visibility.rs:356-362]
  - Signature: `pub fn visible_symbols_for_file(`
  - Purpose: Indexed function `visible_symbols_for_file` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:356-362]
- `visible_symbols_for_files` (function) component `visible_symbols_for_files [function]` (`85594023-9138-5b6f-9e35-a7f830cf11de`) lines 364-383 [crates/gcode/src/visibility.rs:364-383]
  - Signature: `pub fn visible_symbols_for_files(`
  - Purpose: Indexed function `visible_symbols_for_files` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:364-383]
- `query_symbols_for_files` (function) component `query_symbols_for_files [function]` (`ab0800fd-3780-5f87-b3c5-ef20c052c9e5`) lines 385-395 [crates/gcode/src/visibility.rs:385-395]
  - Signature: `fn query_symbols_for_files(`
  - Purpose: Indexed function `query_symbols_for_files` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:385-395]
- `query_overlay_symbols_for_files` (function) component `query_overlay_symbols_for_files [function]` (`9d15f8ef-5ed1-5a1f-8fe0-4be4c2f4060c`) lines 397-413 [crates/gcode/src/visibility.rs:397-413]
  - Signature: `fn query_overlay_symbols_for_files(`
  - Purpose: Indexed function `query_overlay_symbols_for_files` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:397-413]
- `symbols_for_files_sql` (function) component `symbols_for_files_sql [function]` (`af95f309-122c-53a9-be0f-c9283769c407`) lines 415-427 [crates/gcode/src/visibility.rs:415-427]
  - Signature: `fn symbols_for_files_sql() -> String {`
  - Purpose: Indexed function `symbols_for_files_sql` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:415-427]
- `overlay_symbols_for_files_sql` (function) component `overlay_symbols_for_files_sql [function]` (`0a7779c0-e57f-5686-bc51-c8731d6cd7f8`) lines 429-450 [crates/gcode/src/visibility.rs:429-450]
  - Signature: `fn overlay_symbols_for_files_sql() -> String {`
  - Purpose: Indexed function `overlay_symbols_for_files_sql` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:429-450]
- `visible_kinds` (function) component `visible_kinds [function]` (`ce6d4fbc-ca1d-5bb3-9f6b-09a4dc5e08f8`) lines 452-497 [crates/gcode/src/visibility.rs:452-497]
  - Signature: `pub fn visible_kinds(conn: &mut Client, ctx: &Context) -> anyhow::Result<Vec<String>> {`
  - Purpose: Indexed function `visible_kinds` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:452-497]
- `visible_tree` (function) component `visible_tree [function]` (`3f983b55-9fe7-5d82-b47e-059f94972071`) lines 499-539 [crates/gcode/src/visibility.rs:499-539]
  - Signature: `pub fn visible_tree(conn: &mut Client, ctx: &Context) -> anyhow::Result<Vec<VisibleFile>> {`
  - Purpose: Indexed function `visible_tree` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:499-539]
- `tombstone_count` (function) component `tombstone_count [function]` (`342a8eab-150d-572d-b5e8-bac043bb8d40`) lines 541-558 [crates/gcode/src/visibility.rs:541-558]
  - Signature: `pub fn tombstone_count(conn: &mut Client, ctx: &Context) -> usize {`
  - Purpose: Indexed function `tombstone_count` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:541-558]
- `visible_project_ids_include_overlay_before_parent` (function) component `visible_project_ids_include_overlay_before_parent [function]` (`cbcb1617-93ce-5767-b79f-efe7b4e92f41`) lines 566-587 [crates/gcode/src/visibility.rs:566-587]
  - Signature: `fn visible_project_ids_include_overlay_before_parent() {`
  - Purpose: Indexed function `visible_project_ids_include_overlay_before_parent` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:566-587]
- `symbols_for_file_sql_qualifies_joined_symbol_columns` (function) component `symbols_for_file_sql_qualifies_joined_symbol_columns [function]` (`9ffef222-e02b-53b6-b5fc-c62968218301`) lines 590-598 [crates/gcode/src/visibility.rs:590-598]
  - Signature: `fn symbols_for_file_sql_qualifies_joined_symbol_columns() {`
  - Purpose: Indexed function `symbols_for_file_sql_qualifies_joined_symbol_columns` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:590-598]
- `overlay_symbols_for_files_sql_batches_paths_and_preserves_overlay_shadowing` (function) component `overlay_symbols_for_files_sql_batches_paths_and_preserves_overlay_shadowing [function]` (`084373a5-89ac-5b0e-9de2-b797ec84980d`) lines 601-611 [crates/gcode/src/visibility.rs:601-611]
  - Signature: `fn overlay_symbols_for_files_sql_batches_paths_and_preserves_overlay_shadowing() {`
  - Purpose: Indexed function `overlay_symbols_for_files_sql_batches_paths_and_preserves_overlay_shadowing` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:601-611]

