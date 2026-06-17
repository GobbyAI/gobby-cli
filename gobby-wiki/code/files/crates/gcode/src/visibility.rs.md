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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/visibility.rs:13-17](crates/gcode/src/visibility.rs#L13-L17), [crates/gcode/src/visibility.rs:19-21](crates/gcode/src/visibility.rs#L19-L21), [crates/gcode/src/visibility.rs:23-32](crates/gcode/src/visibility.rs#L23-L32), [crates/gcode/src/visibility.rs:34-53](crates/gcode/src/visibility.rs#L34-L53), [crates/gcode/src/visibility.rs:55-99](crates/gcode/src/visibility.rs#L55-L99), [crates/gcode/src/visibility.rs:101-149](crates/gcode/src/visibility.rs#L101-L149), [crates/gcode/src/visibility.rs:151-153](crates/gcode/src/visibility.rs#L151-L153), [crates/gcode/src/visibility.rs:155-181](crates/gcode/src/visibility.rs#L155-L181), [crates/gcode/src/visibility.rs:183-193](crates/gcode/src/visibility.rs#L183-L193), [crates/gcode/src/visibility.rs:195-205](crates/gcode/src/visibility.rs#L195-L205), [crates/gcode/src/visibility.rs:207-222](crates/gcode/src/visibility.rs#L207-L222), [crates/gcode/src/visibility.rs:224-254](crates/gcode/src/visibility.rs#L224-L254), [crates/gcode/src/visibility.rs:256-291](crates/gcode/src/visibility.rs#L256-L291), [crates/gcode/src/visibility.rs:293-319](crates/gcode/src/visibility.rs#L293-L319), [crates/gcode/src/visibility.rs:321-350](crates/gcode/src/visibility.rs#L321-L350), [crates/gcode/src/visibility.rs:352-354](crates/gcode/src/visibility.rs#L352-L354), [crates/gcode/src/visibility.rs:356-362](crates/gcode/src/visibility.rs#L356-L362), [crates/gcode/src/visibility.rs:364-383](crates/gcode/src/visibility.rs#L364-L383), [crates/gcode/src/visibility.rs:385-395](crates/gcode/src/visibility.rs#L385-L395), [crates/gcode/src/visibility.rs:397-413](crates/gcode/src/visibility.rs#L397-L413), [crates/gcode/src/visibility.rs:415-427](crates/gcode/src/visibility.rs#L415-L427), [crates/gcode/src/visibility.rs:429-450](crates/gcode/src/visibility.rs#L429-L450), [crates/gcode/src/visibility.rs:452-497](crates/gcode/src/visibility.rs#L452-L497), [crates/gcode/src/visibility.rs:499-539](crates/gcode/src/visibility.rs#L499-L539), [crates/gcode/src/visibility.rs:541-558](crates/gcode/src/visibility.rs#L541-L558), [crates/gcode/src/visibility.rs:566-587](crates/gcode/src/visibility.rs#L566-L587), [crates/gcode/src/visibility.rs:590-598](crates/gcode/src/visibility.rs#L590-L598), [crates/gcode/src/visibility.rs:601-611](crates/gcode/src/visibility.rs#L601-L611)

</details>

# crates/gcode/src/visibility.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Provides visibility and lookup helpers for the gcode index, deciding which projects, files, languages, symbols, kinds, and trees should be exposed under single-project and overlay index scopes. It defines tombstone markers and a `VisibleFile` record, then builds the core checks and SQL queries that verify indexed file/content presence, filter symbols by file and language visibility, and batch symbol retrieval while preserving overlay shadowing and parent/overlay ordering.
[crates/gcode/src/visibility.rs:13-17]
[crates/gcode/src/visibility.rs:19-21]
[crates/gcode/src/visibility.rs:23-32]
[crates/gcode/src/visibility.rs:34-53]
[crates/gcode/src/visibility.rs:55-99]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `VisibleFile` | class | `pub struct VisibleFile {` | `VisibleFile [class]` | `86045ddf-dd3e-5ee0-9edd-f7616cbfd92b` | 13-17 [crates/gcode/src/visibility.rs:13-17] | Indexed class `VisibleFile` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:13-17] |
| `is_tombstone_language` | function | `pub fn is_tombstone_language(language: &str) -> bool {` | `is_tombstone_language [function]` | `0135ea18-95fe-5013-9293-b327d5e0de6b` | 19-21 [crates/gcode/src/visibility.rs:19-21] | Indexed function `is_tombstone_language` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:19-21] |
| `visible_project_ids` | function | `pub fn visible_project_ids(ctx: &Context) -> Vec<String> {` | `visible_project_ids [function]` | `5fae9e61-67b9-5ad8-9ebb-1774b6e5c8d6` | 23-32 [crates/gcode/src/visibility.rs:23-32] | Indexed function `visible_project_ids` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:23-32] |
| `context_for_source_project` | function | `pub fn context_for_source_project(ctx: &Context, source_project_id: &str) -> Context {` | `context_for_source_project [function]` | `71063b35-b381-5489-a4f9-d0ca7acca366` | 34-53 [crates/gcode/src/visibility.rs:34-53] | Indexed function `context_for_source_project` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:34-53] |
| `indexed_file_exists` | function | `pub fn indexed_file_exists(conn: &mut Client, ctx: &Context, file_path: &str) -> bool {` | `indexed_file_exists [function]` | `27c6cd4e-13ed-59e8-a82d-891201ab3a49` | 55-99 [crates/gcode/src/visibility.rs:55-99] | Indexed function `indexed_file_exists` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:55-99] |
| `content_chunks_exist` | function | `pub fn content_chunks_exist(conn: &mut Client, ctx: &Context, file_path: &str) -> bool {` | `content_chunks_exist [function]` | `c673496f-2343-592d-861d-dba9cd4c4bb4` | 101-149 [crates/gcode/src/visibility.rs:101-149] | Indexed function `content_chunks_exist` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:101-149] |
| `symbol_is_visible` | function | `pub fn symbol_is_visible(conn: &mut Client, ctx: &Context, symbol: &Symbol) -> bool {` | `symbol_is_visible [function]` | `91f309e1-db67-530e-bbaa-6e4c37078798` | 151-153 [crates/gcode/src/visibility.rs:151-153] | Indexed function `symbol_is_visible` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:151-153] |
| `project_path_is_visible` | function | `pub fn project_path_is_visible(` | `project_path_is_visible [function]` | `d1b04c3b-ab21-5118-bf3b-7a778c4f2b03` | 155-181 [crates/gcode/src/visibility.rs:155-181] | Indexed function `project_path_is_visible` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:155-181] |
| `project_file_is_visible` | function | `pub fn project_file_is_visible(conn: &mut Client, project_id: &str, file_path: &str) -> bool {` | `project_file_is_visible [function]` | `96fc76d2-eb72-5f5b-a9ac-ceed4c550a72` | 183-193 [crates/gcode/src/visibility.rs:183-193] | Indexed function `project_file_is_visible` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:183-193] |
| `overlay_has_row` | function | `pub fn overlay_has_row(conn: &mut Client, overlay_project_id: &str, file_path: &str) -> bool {` | `overlay_has_row [function]` | `c81df665-fa70-5875-8174-71aaa62125be` | 195-205 [crates/gcode/src/visibility.rs:195-205] | Indexed function `overlay_has_row` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:195-205] |
| `visible_symbol_by_id` | function | `pub fn visible_symbol_by_id(` | `visible_symbol_by_id [function]` | `887f09cb-d3e1-50fd-b959-70f088e37689` | 207-222 [crates/gcode/src/visibility.rs:207-222] | Indexed function `visible_symbol_by_id` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:207-222] |
| `visible_symbols_by_ids` | function | `pub fn visible_symbols_by_ids(` | `visible_symbols_by_ids [function]` | `ec279f15-db31-5e75-8a59-3d686a30edc4` | 224-254 [crates/gcode/src/visibility.rs:224-254] | Indexed function `visible_symbols_by_ids` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:224-254] |
| `filter_visible_symbols` | function | `pub(crate) fn filter_visible_symbols(` | `filter_visible_symbols [function]` | `b01e50cb-daea-5b7d-873a-906cbe3203fa` | 256-291 [crates/gcode/src/visibility.rs:256-291] | Indexed function `filter_visible_symbols` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:256-291] |
| `indexed_file_languages` | function | `fn indexed_file_languages(` | `indexed_file_languages [function]` | `53c83206-a0f4-53d2-961c-5b01975bf8ea` | 293-319 [crates/gcode/src/visibility.rs:293-319] | Indexed function `indexed_file_languages` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:293-319] |
| `symbol_visible_from_file_languages` | function | `fn symbol_visible_from_file_languages(` | `symbol_visible_from_file_languages [function]` | `c2fca560-7d45-58ba-b549-bdfd8edb41f0` | 321-350 [crates/gcode/src/visibility.rs:321-350] | Indexed function `symbol_visible_from_file_languages` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:321-350] |
| `indexed_language_is_visible` | function | `fn indexed_language_is_visible(language: Option<&String>) -> bool {` | `indexed_language_is_visible [function]` | `bd298967-47f0-50aa-b422-f2828444f9a6` | 352-354 [crates/gcode/src/visibility.rs:352-354] | Indexed function `indexed_language_is_visible` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:352-354] |
| `visible_symbols_for_file` | function | `pub fn visible_symbols_for_file(` | `visible_symbols_for_file [function]` | `9980aaeb-426d-5fe5-baaf-a0ec4b60ad67` | 356-362 [crates/gcode/src/visibility.rs:356-362] | Indexed function `visible_symbols_for_file` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:356-362] |
| `visible_symbols_for_files` | function | `pub fn visible_symbols_for_files(` | `visible_symbols_for_files [function]` | `85594023-9138-5b6f-9e35-a7f830cf11de` | 364-383 [crates/gcode/src/visibility.rs:364-383] | Indexed function `visible_symbols_for_files` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:364-383] |
| `query_symbols_for_files` | function | `fn query_symbols_for_files(` | `query_symbols_for_files [function]` | `ab0800fd-3780-5f87-b3c5-ef20c052c9e5` | 385-395 [crates/gcode/src/visibility.rs:385-395] | Indexed function `query_symbols_for_files` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:385-395] |
| `query_overlay_symbols_for_files` | function | `fn query_overlay_symbols_for_files(` | `query_overlay_symbols_for_files [function]` | `9d15f8ef-5ed1-5a1f-8fe0-4be4c2f4060c` | 397-413 [crates/gcode/src/visibility.rs:397-413] | Indexed function `query_overlay_symbols_for_files` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:397-413] |
| `symbols_for_files_sql` | function | `fn symbols_for_files_sql() -> String {` | `symbols_for_files_sql [function]` | `af95f309-122c-53a9-be0f-c9283769c407` | 415-427 [crates/gcode/src/visibility.rs:415-427] | Indexed function `symbols_for_files_sql` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:415-427] |
| `overlay_symbols_for_files_sql` | function | `fn overlay_symbols_for_files_sql() -> String {` | `overlay_symbols_for_files_sql [function]` | `0a7779c0-e57f-5686-bc51-c8731d6cd7f8` | 429-450 [crates/gcode/src/visibility.rs:429-450] | Indexed function `overlay_symbols_for_files_sql` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:429-450] |
| `visible_kinds` | function | `pub fn visible_kinds(conn: &mut Client, ctx: &Context) -> anyhow::Result<Vec<String>> {` | `visible_kinds [function]` | `ce6d4fbc-ca1d-5bb3-9f6b-09a4dc5e08f8` | 452-497 [crates/gcode/src/visibility.rs:452-497] | Indexed function `visible_kinds` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:452-497] |
| `visible_tree` | function | `pub fn visible_tree(conn: &mut Client, ctx: &Context) -> anyhow::Result<Vec<VisibleFile>> {` | `visible_tree [function]` | `3f983b55-9fe7-5d82-b47e-059f94972071` | 499-539 [crates/gcode/src/visibility.rs:499-539] | Indexed function `visible_tree` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:499-539] |
| `tombstone_count` | function | `pub fn tombstone_count(conn: &mut Client, ctx: &Context) -> usize {` | `tombstone_count [function]` | `342a8eab-150d-572d-b5e8-bac043bb8d40` | 541-558 [crates/gcode/src/visibility.rs:541-558] | Indexed function `tombstone_count` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:541-558] |
| `visible_project_ids_include_overlay_before_parent` | function | `fn visible_project_ids_include_overlay_before_parent() {` | `visible_project_ids_include_overlay_before_parent [function]` | `cbcb1617-93ce-5767-b79f-efe7b4e92f41` | 566-587 [crates/gcode/src/visibility.rs:566-587] | Indexed function `visible_project_ids_include_overlay_before_parent` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:566-587] |
| `symbols_for_file_sql_qualifies_joined_symbol_columns` | function | `fn symbols_for_file_sql_qualifies_joined_symbol_columns() {` | `symbols_for_file_sql_qualifies_joined_symbol_columns [function]` | `9ffef222-e02b-53b6-b5fc-c62968218301` | 590-598 [crates/gcode/src/visibility.rs:590-598] | Indexed function `symbols_for_file_sql_qualifies_joined_symbol_columns` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:590-598] |
| `overlay_symbols_for_files_sql_batches_paths_and_preserves_overlay_shadowing` | function | `fn overlay_symbols_for_files_sql_batches_paths_and_preserves_overlay_shadowing() {` | `overlay_symbols_for_files_sql_batches_paths_and_preserves_overlay_shadowing [function]` | `084373a5-89ac-5b0e-9de2-b797ec84980d` | 601-611 [crates/gcode/src/visibility.rs:601-611] | Indexed function `overlay_symbols_for_files_sql_batches_paths_and_preserves_overlay_shadowing` in `crates/gcode/src/visibility.rs`. [crates/gcode/src/visibility.rs:601-611] |
