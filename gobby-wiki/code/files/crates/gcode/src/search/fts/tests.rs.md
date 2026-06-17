---
title: crates/gcode/src/search/fts/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/search/fts/tests.rs
  ranges:
  - 17-26
  - 29-34
  - 37-43
  - 46-49
  - 52-57
  - 60-72
  - 75-81
  - 84-99
  - 102-133
  - 136-142
  - 145-151
  - 154-166
  - 177-209
  - 217-243
  - 251-264
  - 272-279
  - 287-295
  - 298-305
  - 307-311
  - 314-321
  - 324-328
  - 331-338
  - 342-344
  - 347-350
  - 353-357
  - 360-363
  - 365-367
  - 369-383
  - 385-473
  - 475-483
  - 485-502
  - 504-517
  - 519-536
  - 538-557
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/search/fts/tests.rs:17-26](crates/gcode/src/search/fts/tests.rs#L17-L26), [crates/gcode/src/search/fts/tests.rs:29-34](crates/gcode/src/search/fts/tests.rs#L29-L34), [crates/gcode/src/search/fts/tests.rs:37-43](crates/gcode/src/search/fts/tests.rs#L37-L43), [crates/gcode/src/search/fts/tests.rs:46-49](crates/gcode/src/search/fts/tests.rs#L46-L49), [crates/gcode/src/search/fts/tests.rs:52-57](crates/gcode/src/search/fts/tests.rs#L52-L57), [crates/gcode/src/search/fts/tests.rs:60-72](crates/gcode/src/search/fts/tests.rs#L60-L72), [crates/gcode/src/search/fts/tests.rs:75-81](crates/gcode/src/search/fts/tests.rs#L75-L81), [crates/gcode/src/search/fts/tests.rs:84-99](crates/gcode/src/search/fts/tests.rs#L84-L99), [crates/gcode/src/search/fts/tests.rs:102-133](crates/gcode/src/search/fts/tests.rs#L102-L133), [crates/gcode/src/search/fts/tests.rs:136-142](crates/gcode/src/search/fts/tests.rs#L136-L142), [crates/gcode/src/search/fts/tests.rs:145-151](crates/gcode/src/search/fts/tests.rs#L145-L151), [crates/gcode/src/search/fts/tests.rs:154-166](crates/gcode/src/search/fts/tests.rs#L154-L166), [crates/gcode/src/search/fts/tests.rs:177-209](crates/gcode/src/search/fts/tests.rs#L177-L209), [crates/gcode/src/search/fts/tests.rs:217-243](crates/gcode/src/search/fts/tests.rs#L217-L243), [crates/gcode/src/search/fts/tests.rs:251-264](crates/gcode/src/search/fts/tests.rs#L251-L264), [crates/gcode/src/search/fts/tests.rs:272-279](crates/gcode/src/search/fts/tests.rs#L272-L279), [crates/gcode/src/search/fts/tests.rs:287-295](crates/gcode/src/search/fts/tests.rs#L287-L295), [crates/gcode/src/search/fts/tests.rs:298-305](crates/gcode/src/search/fts/tests.rs#L298-L305), [crates/gcode/src/search/fts/tests.rs:307-311](crates/gcode/src/search/fts/tests.rs#L307-L311), [crates/gcode/src/search/fts/tests.rs:314-321](crates/gcode/src/search/fts/tests.rs#L314-L321), [crates/gcode/src/search/fts/tests.rs:324-328](crates/gcode/src/search/fts/tests.rs#L324-L328), [crates/gcode/src/search/fts/tests.rs:331-338](crates/gcode/src/search/fts/tests.rs#L331-L338), [crates/gcode/src/search/fts/tests.rs:342-344](crates/gcode/src/search/fts/tests.rs#L342-L344), [crates/gcode/src/search/fts/tests.rs:347-350](crates/gcode/src/search/fts/tests.rs#L347-L350), [crates/gcode/src/search/fts/tests.rs:353-357](crates/gcode/src/search/fts/tests.rs#L353-L357), [crates/gcode/src/search/fts/tests.rs:360-363](crates/gcode/src/search/fts/tests.rs#L360-L363), [crates/gcode/src/search/fts/tests.rs:365-367](crates/gcode/src/search/fts/tests.rs#L365-L367), [crates/gcode/src/search/fts/tests.rs:369-383](crates/gcode/src/search/fts/tests.rs#L369-L383), [crates/gcode/src/search/fts/tests.rs:385-473](crates/gcode/src/search/fts/tests.rs#L385-L473), [crates/gcode/src/search/fts/tests.rs:475-483](crates/gcode/src/search/fts/tests.rs#L475-L483), [crates/gcode/src/search/fts/tests.rs:485-502](crates/gcode/src/search/fts/tests.rs#L485-L502), [crates/gcode/src/search/fts/tests.rs:504-517](crates/gcode/src/search/fts/tests.rs#L504-L517), [crates/gcode/src/search/fts/tests.rs:519-536](crates/gcode/src/search/fts/tests.rs#L519-L536), [crates/gcode/src/search/fts/tests.rs:538-557](crates/gcode/src/search/fts/tests.rs#L538-L557)

</details>

# crates/gcode/src/search/fts/tests.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This file is the test suite for the full-text-search and overlay-visibility helpers in `crates/gcode/src/search/fts`. It verifies query sanitization, glob/path expansion and pattern compilation, snippet selection, symbol lookup by UUID, and the database-backed overlay visibility logic, while the fixture and cleanup helpers build and tear down temporary projects, files, symbols, and chunks used by those tests.
[crates/gcode/src/search/fts/tests.rs:17-26]
[crates/gcode/src/search/fts/tests.rs:29-34]
[crates/gcode/src/search/fts/tests.rs:37-43]
[crates/gcode/src/search/fts/tests.rs:46-49]
[crates/gcode/src/search/fts/tests.rs:52-57]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `unique_test_id` | function | `fn unique_test_id(prefix: &str) -> String {` | `unique_test_id [function]` | `1622d5fc-3a81-565d-8cfe-6ffabcb12f1f` | 17-26 [crates/gcode/src/search/fts/tests.rs:17-26] | Indexed function `unique_test_id` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:17-26] |
| `sanitize_pg_search_query_matches_gobby_rules` | function | `fn sanitize_pg_search_query_matches_gobby_rules() {` | `sanitize_pg_search_query_matches_gobby_rules [function]` | `fd54f990-1b37-5f68-8408-2d3c7269ce30` | 29-34 [crates/gcode/src/search/fts/tests.rs:29-34] | Indexed function `sanitize_pg_search_query_matches_gobby_rules` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:29-34] |
| `sanitize_pg_search_query_escapes_leading_minus_per_token` | function | `fn sanitize_pg_search_query_escapes_leading_minus_per_token() {` | `sanitize_pg_search_query_escapes_leading_minus_per_token [function]` | `1f26ce71-11ec-50de-8b43-7b98692770bc` | 37-43 [crates/gcode/src/search/fts/tests.rs:37-43] | Indexed function `sanitize_pg_search_query_escapes_leading_minus_per_token` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:37-43] |
| `sanitize_pg_search_query_preserves_dsl_punctuation` | function | `fn sanitize_pg_search_query_preserves_dsl_punctuation() {` | `sanitize_pg_search_query_preserves_dsl_punctuation [function]` | `fc44b822-a009-582b-b905-d5529393a1a2` | 46-49 [crates/gcode/src/search/fts/tests.rs:46-49] | Indexed function `sanitize_pg_search_query_preserves_dsl_punctuation` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:46-49] |
| `glob_to_like_prefix_escapes_like_wildcards` | function | `fn glob_to_like_prefix_escapes_like_wildcards() {` | `glob_to_like_prefix_escapes_like_wildcards [function]` | `8689ca2e-c1bf-5808-8150-4bf0a6d9dd98` | 52-57 [crates/gcode/src/search/fts/tests.rs:52-57] | Indexed function `glob_to_like_prefix_escapes_like_wildcards` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:52-57] |
| `expand_paths_trims_skips_empty_and_expands_bare_paths` | function | `fn expand_paths_trims_skips_empty_and_expands_bare_paths() {` | `expand_paths_trims_skips_empty_and_expands_bare_paths [function]` | `5f195c43-9371-5d02-ba23-e1376bfb3de3` | 60-72 [crates/gcode/src/search/fts/tests.rs:60-72] | Indexed function `expand_paths_trims_skips_empty_and_expands_bare_paths` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:60-72] |
| `compile_patterns_reports_invalid_glob` | function | `fn compile_patterns_reports_invalid_glob() {` | `compile_patterns_reports_invalid_glob [function]` | `d78afdfa-69fe-5921-a2ef-928494c47574` | 75-81 [crates/gcode/src/search/fts/tests.rs:75-81] | Indexed function `compile_patterns_reports_invalid_glob` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:75-81] |
| `path_like_prefixes_escape_and_require_all_patterns` | function | `fn path_like_prefixes_escape_and_require_all_patterns() {` | `path_like_prefixes_escape_and_require_all_patterns [function]` | `49cc3e66-1b6d-5f9e-9964-c2c54ab58b80` | 84-99 [crates/gcode/src/search/fts/tests.rs:84-99] | Indexed function `path_like_prefixes_escape_and_require_all_patterns` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:84-99] |
| `append_unique_symbols_respects_zero_limit` | function | `fn append_unique_symbols_respects_zero_limit() {` | `append_unique_symbols_respects_zero_limit [function]` | `e294fe66-8239-5cc5-9153-12f7e13f587d` | 102-133 [crates/gcode/src/search/fts/tests.rs:102-133] | Indexed function `append_unique_symbols_respects_zero_limit` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:102-133] |
| `snippet_centers_first_matching_token` | function | `fn snippet_centers_first_matching_token() {` | `snippet_centers_first_matching_token [function]` | `576ff3eb-7797-5edc-ba13-7bdf39b37b5f` | 136-142 [crates/gcode/src/search/fts/tests.rs:136-142] | Indexed function `snippet_centers_first_matching_token` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:136-142] |
| `snippet_centers_earliest_matching_token_regardless_of_query_order` | function | `fn snippet_centers_earliest_matching_token_regardless_of_query_order() {` | `snippet_centers_earliest_matching_token_regardless_of_query_order [function]` | `78da6b7c-d5ab-5449-a982-91b42784285e` | 145-151 [crates/gcode/src/search/fts/tests.rs:145-151] | Indexed function `snippet_centers_earliest_matching_token_regardless_of_query_order` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:145-151] |
| `snippet_handles_unicode_before_match` | function | `fn snippet_handles_unicode_before_match() {` | `snippet_handles_unicode_before_match [function]` | `1f5dc90a-1d58-5be8-8c77-426b53c26226` | 154-166 [crates/gcode/src/search/fts/tests.rs:154-166] | Indexed function `snippet_handles_unicode_before_match` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:154-166] |
| `overlay_visibility_counts_and_kinds_use_database_predicates` | function | `fn overlay_visibility_counts_and_kinds_use_database_predicates() {` | `overlay_visibility_counts_and_kinds_use_database_predicates [function]` | `95a18355-c18b-5c69-a394-23e780c4de6e` | 177-209 [crates/gcode/src/search/fts/tests.rs:177-209] | Indexed function `overlay_visibility_counts_and_kinds_use_database_predicates` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:177-209] |
| `resolve_graph_symbol_by_id_resolves_exact_symbol` | function | `fn resolve_graph_symbol_by_id_resolves_exact_symbol() {` | `resolve_graph_symbol_by_id_resolves_exact_symbol [function]` | `bc44041c-8be3-5fb7-a9d2-d3ec818abf0d` | 217-243 [crates/gcode/src/search/fts/tests.rs:217-243] | Indexed function `resolve_graph_symbol_by_id_resolves_exact_symbol` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:217-243] |
| `resolve_graph_symbol_by_id_returns_none_for_missing_uuid` | function | `fn resolve_graph_symbol_by_id_returns_none_for_missing_uuid() {` | `resolve_graph_symbol_by_id_returns_none_for_missing_uuid [function]` | `896f406b-7be4-5da6-85a8-4085cc42dc40` | 251-264 [crates/gcode/src/search/fts/tests.rs:251-264] | Indexed function `resolve_graph_symbol_by_id_returns_none_for_missing_uuid` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:251-264] |
| `resolve_graph_symbol_by_id_returns_none_for_empty_id` | function | `fn resolve_graph_symbol_by_id_returns_none_for_empty_id() {` | `resolve_graph_symbol_by_id_returns_none_for_empty_id [function]` | `30d84ae4-7c0c-5f47-a008-8f41fb85f29c` | 272-279 [crates/gcode/src/search/fts/tests.rs:272-279] | Indexed function `resolve_graph_symbol_by_id_returns_none_for_empty_id` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:272-279] |
| `resolve_graph_symbol_by_id_returns_none_for_malformed_id` | function | `fn resolve_graph_symbol_by_id_returns_none_for_malformed_id() {` | `resolve_graph_symbol_by_id_returns_none_for_malformed_id [function]` | `abdac773-0971-5e6d-b3fc-40716f61a397` | 287-295 [crates/gcode/src/search/fts/tests.rs:287-295] | Indexed function `resolve_graph_symbol_by_id_returns_none_for_malformed_id` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:287-295] |
| `connect_overlay_visibility_test_db` | function | `fn connect_overlay_visibility_test_db() -> (Client, String) {` | `connect_overlay_visibility_test_db [function]` | `2b93fd1b-cb44-5f9c-80ff-ccaf43295cba` | 298-305 [crates/gcode/src/search/fts/tests.rs:298-305] | Indexed function `connect_overlay_visibility_test_db` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:298-305] |
| `OverlayFixtureIds` | class | `struct OverlayFixtureIds {` | `OverlayFixtureIds [class]` | `f1d2919b-f385-5236-abce-442b1c16ae92` | 307-311 [crates/gcode/src/search/fts/tests.rs:307-311] | Indexed class `OverlayFixtureIds` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:307-311] |
| `OverlayFixtureIds::new` | method | `fn new(database_url: String) -> Self {` | `OverlayFixtureIds::new [method]` | `1ef9fbbf-bd96-512c-a476-ec5aafe30e6c` | 314-321 [crates/gcode/src/search/fts/tests.rs:314-321] | Indexed method `OverlayFixtureIds::new` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:314-321] |
| `OverlayFixtureCleanup` | class | `struct OverlayFixtureCleanup {` | `OverlayFixtureCleanup [class]` | `50604e3e-f024-5af9-a127-2c0ead9ef20d` | 324-328 [crates/gcode/src/search/fts/tests.rs:324-328] | Indexed class `OverlayFixtureCleanup` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:324-328] |
| `OverlayFixtureCleanup::cleanup` | method | `fn cleanup(&self) -> anyhow::Result<()> {` | `OverlayFixtureCleanup::cleanup [method]` | `46e6cb58-9078-5398-8946-6ac2285c6879` | 331-338 [crates/gcode/src/search/fts/tests.rs:331-338] | Indexed method `OverlayFixtureCleanup::cleanup` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:331-338] |
| `OverlayFixtureCleanup::drop` | method | `fn drop(&mut self) {` | `OverlayFixtureCleanup::drop [method]` | `fcfc117f-effc-5cf1-becf-3f2e75903b65` | 342-344 [crates/gcode/src/search/fts/tests.rs:342-344] | Indexed method `OverlayFixtureCleanup::drop` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:342-344] |
| `SingleProjectCleanup` | class | `struct SingleProjectCleanup {` | `SingleProjectCleanup [class]` | `9c551ca8-6d1f-55a7-892a-3262b1c428e2` | 347-350 [crates/gcode/src/search/fts/tests.rs:347-350] | Indexed class `SingleProjectCleanup` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:347-350] |
| `SingleProjectCleanup::drop` | method | `fn drop(&mut self) {` | `SingleProjectCleanup::drop [method]` | `a3ac8493-2afd-57e2-bbd0-110b93040a3a` | 353-357 [crates/gcode/src/search/fts/tests.rs:353-357] | Indexed method `SingleProjectCleanup::drop` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:353-357] |
| `cleanup_overlay_visibility_fixture` | function | `fn cleanup_overlay_visibility_fixture(conn: &mut Client, ids: &OverlayFixtureIds) {` | `cleanup_overlay_visibility_fixture [function]` | `217b7e05-09d4-5acc-b8b3-459b8dcbde29` | 360-363 [crates/gcode/src/search/fts/tests.rs:360-363] | Indexed function `cleanup_overlay_visibility_fixture` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:360-363] |
| `cleanup_single_project` | function | `fn cleanup_single_project(conn: &mut Client, project_id: &str) {` | `cleanup_single_project [function]` | `20a648c9-6128-5fe2-b489-05e1171388f2` | 365-367 [crates/gcode/src/search/fts/tests.rs:365-367] | Indexed function `cleanup_single_project` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:365-367] |
| `cleanup_overlay_visibility_projects` | function | `fn cleanup_overlay_visibility_projects(` | `cleanup_overlay_visibility_projects [function]` | `41bebba3-96fa-5b65-bc0c-3f65881e72cf` | 369-383 [crates/gcode/src/search/fts/tests.rs:369-383] | Indexed function `cleanup_overlay_visibility_projects` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:369-383] |
| `seed_overlay_visibility_fixture` | function | `fn seed_overlay_visibility_fixture(conn: &mut Client, ids: &OverlayFixtureIds) {` | `seed_overlay_visibility_fixture [function]` | `ad84a5d9-b175-5bc3-a1f8-4daec0cc72f5` | 385-473 [crates/gcode/src/search/fts/tests.rs:385-473] | Indexed function `seed_overlay_visibility_fixture` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:385-473] |
| `insert_project` | function | `fn insert_project(conn: &mut Client, project_id: &str, root_path: &str) {` | `insert_project [function]` | `3ed4b212-bb18-5901-8827-8aa5dfdbe854` | 475-483 [crates/gcode/src/search/fts/tests.rs:475-483] | Indexed function `insert_project` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:475-483] |
| `insert_file` | function | `fn insert_file(` | `insert_file [function]` | `9862aa3f-335c-5433-a314-938b02cc821d` | 485-502 [crates/gcode/src/search/fts/tests.rs:485-502] | Indexed function `insert_file` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:485-502] |
| `insert_symbol` | function | `fn insert_symbol(conn: &mut Client, project_id: &str, file_path: &str, name: &str, kind: &str) {` | `insert_symbol [function]` | `1c8fb530-721e-5290-a7c8-66f7feebd56a` | 504-517 [crates/gcode/src/search/fts/tests.rs:504-517] | Indexed function `insert_symbol` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:504-517] |
| `insert_chunk` | function | `fn insert_chunk(` | `insert_chunk [function]` | `3913a027-5b01-5cab-8046-309dd90b2606` | 519-536 [crates/gcode/src/search/fts/tests.rs:519-536] | Indexed function `insert_chunk` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:519-536] |
| `overlay_visibility_context` | function | `fn overlay_visibility_context(ids: &OverlayFixtureIds) -> Context {` | `overlay_visibility_context [function]` | `01c42c68-8644-50f6-a2cb-96c57ad72f29` | 538-557 [crates/gcode/src/search/fts/tests.rs:538-557] | Indexed function `overlay_visibility_context` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:538-557] |
