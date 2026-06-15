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
  - 313-322
  - 324-328
  - 330-339
  - 341-345
  - 347-350
  - 352-358
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

# crates/gcode/src/search/fts/tests.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Purpose

This file is a test suite for `crates/gcode/src/search/fts`, covering full-text search query sanitization, glob/path pattern normalization, snippet generation, overlay visibility filtering, and graph-symbol resolution. It also defines small test helpers for generating unique IDs, connecting to the test database, seeding and cleaning up overlay fixtures, inserting projects/files/symbols/chunks, and building an overlay-scoped `Context`, so the tests can exercise the search and visibility logic against realistic PostgreSQL-backed fixtures.
[crates/gcode/src/search/fts/tests.rs:17-26]
[crates/gcode/src/search/fts/tests.rs:29-34]
[crates/gcode/src/search/fts/tests.rs:37-43]
[crates/gcode/src/search/fts/tests.rs:46-49]
[crates/gcode/src/search/fts/tests.rs:52-57]

## API Symbols

- `unique_test_id` (function) component `unique_test_id [function]` (`1622d5fc-3a81-565d-8cfe-6ffabcb12f1f`) lines 17-26 [crates/gcode/src/search/fts/tests.rs:17-26]
  - Signature: `fn unique_test_id(prefix: &str) -> String {`
  - Purpose: Generates a unique test ID string by concatenating a given prefix with the current process ID and the system time in nanoseconds since Unix epoch. [crates/gcode/src/search/fts/tests.rs:17-26]
- `sanitize_pg_search_query_matches_gobby_rules` (function) component `sanitize_pg_search_query_matches_gobby_rules [function]` (`fd54f990-1b37-5f68-8408-2d3c7269ce30`) lines 29-34 [crates/gcode/src/search/fts/tests.rs:29-34]
  - Signature: `fn sanitize_pg_search_query_matches_gobby_rules() {`
  - Purpose: This test asserts that `sanitize_pg_search_query` preserves PostgreSQL search query syntax including namespace operators (::), special characters, and quoted strings without modification. [crates/gcode/src/search/fts/tests.rs:29-34]
- `sanitize_pg_search_query_escapes_leading_minus_per_token` (function) component `sanitize_pg_search_query_escapes_leading_minus_per_token [function]` (`1f26ce71-11ec-50de-8b43-7b98692770bc`) lines 37-43 [crates/gcode/src/search/fts/tests.rs:37-43]
  - Signature: `fn sanitize_pg_search_query_escapes_leading_minus_per_token() {`
  - Purpose: A unit test verifying that `sanitize_pg_search_query` escapes leading minus signs at token boundaries with backslashes while preserving non-leading hyphens in PostgreSQL full-text search queries. [crates/gcode/src/search/fts/tests.rs:37-43]
- `sanitize_pg_search_query_preserves_dsl_punctuation` (function) component `sanitize_pg_search_query_preserves_dsl_punctuation [function]` (`fc44b822-a009-582b-b905-d5529393a1a2`) lines 46-49 [crates/gcode/src/search/fts/tests.rs:46-49]
  - Signature: `fn sanitize_pg_search_query_preserves_dsl_punctuation() {`
  - Purpose: A unit test verifying that `sanitize_pg_search_query` preserves PostgreSQL full-text search DSL operators (`::`, `+`, parentheses) while escaping unescaped minus signs. [crates/gcode/src/search/fts/tests.rs:46-49]
- `glob_to_like_prefix_escapes_like_wildcards` (function) component `glob_to_like_prefix_escapes_like_wildcards [function]` (`8689ca2e-c1bf-5808-8150-4bf0a6d9dd98`) lines 52-57 [crates/gcode/src/search/fts/tests.rs:52-57]
  - Signature: `fn glob_to_like_prefix_escapes_like_wildcards() {`
  - Purpose: This test validates that `glob_to_like_prefix` correctly converts glob patterns to SQL LIKE patterns by escaping literal underscores (SQL wildcards) as `\_` and replacing glob wildcards (`*`) with LIKE wildcards (`%`). [crates/gcode/src/search/fts/tests.rs:52-57]
- `expand_paths_trims_skips_empty_and_expands_bare_paths` (function) component `expand_paths_trims_skips_empty_and_expands_bare_paths [function]` (`5f195c43-9371-5d02-ba23-e1376bfb3de3`) lines 60-72 [crates/gcode/src/search/fts/tests.rs:60-72]
  - Signature: `fn expand_paths_trims_skips_empty_and_expands_bare_paths() {`
  - Purpose: Tests that `expand_paths` trims whitespace, skips empty strings, converts directory paths with trailing slashes to `/**` glob patterns, and preserves existing glob expressions. [crates/gcode/src/search/fts/tests.rs:60-72]
- `compile_patterns_reports_invalid_glob` (function) component `compile_patterns_reports_invalid_glob [function]` (`d78afdfa-69fe-5921-a2ef-928494c47574`) lines 75-81 [crates/gcode/src/search/fts/tests.rs:75-81]
  - Signature: `fn compile_patterns_reports_invalid_glob() {`
  - Purpose: This test function verifies that `compile_patterns()` properly fails and reports an error message containing the invalid glob pattern when provided with malformed glob syntax. [crates/gcode/src/search/fts/tests.rs:75-81]
- `path_like_prefixes_escape_and_require_all_patterns` (function) component `path_like_prefixes_escape_and_require_all_patterns [function]` (`49cc3e66-1b6d-5f9e-9964-c2c54ab58b80`) lines 84-99 [crates/gcode/src/search/fts/tests.rs:84-99]
  - Signature: `fn path_like_prefixes_escape_and_require_all_patterns() {`
  - Purpose: This test function verifies that `path_like_prefixes` correctly escapes special characters in compatible path patterns, returns `None` for incompatible mixed glob patterns, and accurately determines when post-filtering is required. [crates/gcode/src/search/fts/tests.rs:84-99]
- `append_unique_symbols_respects_zero_limit` (function) component `append_unique_symbols_respects_zero_limit [function]` (`e294fe66-8239-5cc5-9153-12f7e13f587d`) lines 102-133 [crates/gcode/src/search/fts/tests.rs:102-133]
  - Signature: `fn append_unique_symbols_respects_zero_limit() {`
  - Purpose: This unit test asserts that `append_unique_symbols` respects a zero limit constraint by leaving both the output vector and seen set empty after attempting to process a symbol. [crates/gcode/src/search/fts/tests.rs:102-133]
- `snippet_centers_first_matching_token` (function) component `snippet_centers_first_matching_token [function]` (`576ff3eb-7797-5edc-ba13-7bdf39b37b5f`) lines 136-142 [crates/gcode/src/search/fts/tests.rs:136-142]
  - Signature: `fn snippet_centers_first_matching_token() {`
  - Purpose: Verifies that `make_snippet` centers a snippet around the first matching token while keeping the result within a 180-character limit. [crates/gcode/src/search/fts/tests.rs:136-142]
- `snippet_centers_earliest_matching_token_regardless_of_query_order` (function) component `snippet_centers_earliest_matching_token_regardless_of_query_order [function]` (`78da6b7c-d5ab-5449-a982-91b42784285e`) lines 145-151 [crates/gcode/src/search/fts/tests.rs:145-151]
  - Signature: `fn snippet_centers_earliest_matching_token_regardless_of_query_order() {`
  - Purpose: This test verifies that `make_snippet` centers the snippet on the earliest-occurring query match ("early match") regardless of the order in which query terms are specified ("late early"). [crates/gcode/src/search/fts/tests.rs:145-151]
- `snippet_handles_unicode_before_match` (function) component `snippet_handles_unicode_before_match [function]` (`1f5dc90a-1d58-5be8-8c77-426b53c26226`) lines 154-166 [crates/gcode/src/search/fts/tests.rs:154-166]
  - Signature: `fn snippet_handles_unicode_before_match() {`
  - Purpose: This function tests that `make_snippet` correctly extracts snippets containing a target substring while respecting a 180-character limit, even when Unicode characters precede the match in the source content. [crates/gcode/src/search/fts/tests.rs:154-166]
- `overlay_visibility_counts_and_kinds_use_database_predicates` (function) component `overlay_visibility_counts_and_kinds_use_database_predicates [function]` (`95a18355-c18b-5c69-a394-23e780c4de6e`) lines 177-209 [crates/gcode/src/search/fts/tests.rs:177-209]
  - Signature: `fn overlay_visibility_counts_and_kinds_use_database_predicates() {`
  - Purpose: It verifies that overlay visibility queries use database-level predicates by asserting the visible kinds and text/content match counts for a seeded overlay fixture are exactly the expected values. [crates/gcode/src/search/fts/tests.rs:177-209]
- `resolve_graph_symbol_by_id_resolves_exact_symbol` (function) component `resolve_graph_symbol_by_id_resolves_exact_symbol [function]` (`bc44041c-8be3-5fb7-a9d2-d3ec818abf0d`) lines 217-243 [crates/gcode/src/search/fts/tests.rs:217-243]
  - Signature: `fn resolve_graph_symbol_by_id_resolves_exact_symbol() {`
  - Purpose: Verifies that 'resolve_graph_symbol_by_id' returns the exact symbol for a fully qualified symbol ID within a project, preserving the ID and resolving the expected display name. [crates/gcode/src/search/fts/tests.rs:217-243]
- `resolve_graph_symbol_by_id_returns_none_for_missing_uuid` (function) component `resolve_graph_symbol_by_id_returns_none_for_missing_uuid [function]` (`896f406b-7be4-5da6-85a8-4085cc42dc40`) lines 251-264 [crates/gcode/src/search/fts/tests.rs:251-264]
  - Signature: `fn resolve_graph_symbol_by_id_returns_none_for_missing_uuid() {`
  - Purpose: Verifies that 'resolve_graph_symbol_by_id' returns 'None' when called with a UUID that does not correspond to any graph symbol in the given project. [crates/gcode/src/search/fts/tests.rs:251-264]
- `resolve_graph_symbol_by_id_returns_none_for_empty_id` (function) component `resolve_graph_symbol_by_id_returns_none_for_empty_id [function]` (`30d84ae4-7c0c-5f47-a008-8f41fb85f29c`) lines 272-279 [crates/gcode/src/search/fts/tests.rs:272-279]
  - Signature: `fn resolve_graph_symbol_by_id_returns_none_for_empty_id() {`
  - Purpose: Verifies that 'resolve_graph_symbol_by_id' returns 'None' when called with an empty symbol ID, even though the database lookup itself succeeds. [crates/gcode/src/search/fts/tests.rs:272-279]
- `resolve_graph_symbol_by_id_returns_none_for_malformed_id` (function) component `resolve_graph_symbol_by_id_returns_none_for_malformed_id [function]` (`abdac773-0971-5e6d-b3fc-40716f61a397`) lines 287-295 [crates/gcode/src/search/fts/tests.rs:287-295]
  - Signature: `fn resolve_graph_symbol_by_id_returns_none_for_malformed_id() {`
  - Purpose: Verifies that 'resolve_graph_symbol_by_id' returns 'None' when given a malformed symbol ID, even though the call itself succeeds. [crates/gcode/src/search/fts/tests.rs:287-295]
- `connect_overlay_visibility_test_db` (function) component `connect_overlay_visibility_test_db [function]` (`2b93fd1b-cb44-5f9c-80ff-ccaf43295cba`) lines 298-305 [crates/gcode/src/search/fts/tests.rs:298-305]
  - Signature: `fn connect_overlay_visibility_test_db() -> (Client, String) {`
  - Purpose: Reads 'GCODE_POSTGRES_TEST_DATABASE_URL', opens a read-write PostgreSQL client, validates the runtime schema, and returns the client together with the database URL. [crates/gcode/src/search/fts/tests.rs:298-305]
- `OverlayFixtureIds` (class) component `OverlayFixtureIds [class]` (`f1d2919b-f385-5236-abce-442b1c16ae92`) lines 307-311 [crates/gcode/src/search/fts/tests.rs:307-311]
  - Signature: `struct OverlayFixtureIds {`
  - Purpose: 'OverlayFixtureIds' is a data struct that holds the database URL plus the parent and overlay project identifiers needed to associate an overlay fixture with its source project and derived project. [crates/gcode/src/search/fts/tests.rs:307-311]
- `OverlayFixtureIds` (class) component `OverlayFixtureIds [class]` (`87e24284-9839-52c2-8e5a-37921d934fb4`) lines 313-322 [crates/gcode/src/search/fts/tests.rs:313-322]
  - Signature: `impl OverlayFixtureIds {`
  - Purpose: 'OverlayFixtureIds' is a test-fixture ID generator that stores a 'database_url' and derives unique 'parent_project_id' and 'overlay_project_id' values from a 'gcode-overlay-test'-prefixed suffix. [crates/gcode/src/search/fts/tests.rs:313-322]
- `OverlayFixtureIds.new` (method) component `OverlayFixtureIds.new [method]` (`1ef9fbbf-bd96-512c-a476-ec5aafe30e6c`) lines 314-321 [crates/gcode/src/search/fts/tests.rs:314-321]
  - Signature: `fn new(database_url: String) -> Self {`
  - Purpose: Constructs a new instance by generating a unique test suffix and using it to derive distinct 'parent_project_id' and 'overlay_project_id' values while storing the provided 'database_url'. [crates/gcode/src/search/fts/tests.rs:314-321]
- `OverlayFixtureCleanup` (class) component `OverlayFixtureCleanup [class]` (`50604e3e-f024-5af9-a127-2c0ead9ef20d`) lines 324-328 [crates/gcode/src/search/fts/tests.rs:324-328]
  - Signature: `struct OverlayFixtureCleanup {`
  - Purpose: 'OverlayFixtureCleanup' is a cleanup record that stores the database URL and the parent and overlay project IDs needed to remove or reconcile an overlay test fixture. [crates/gcode/src/search/fts/tests.rs:324-328]
- `OverlayFixtureCleanup` (class) component `OverlayFixtureCleanup [class]` (`e883fdff-942e-5381-a8f5-46d1a711aede`) lines 330-339 [crates/gcode/src/search/fts/tests.rs:330-339]
  - Signature: `impl OverlayFixtureCleanup {`
  - Purpose: 'OverlayFixtureCleanup' is a helper that opens a read-write PostgreSQL connection and invokes 'cleanup_overlay_visibility_projects' to remove overlay visibility state for a specific parent/overlay project pair. [crates/gcode/src/search/fts/tests.rs:330-339]
- `OverlayFixtureCleanup.cleanup` (method) component `OverlayFixtureCleanup.cleanup [method]` (`46e6cb58-9078-5398-8946-6ac2285c6879`) lines 331-338 [crates/gcode/src/search/fts/tests.rs:331-338]
  - Signature: `fn cleanup(&self) -> anyhow::Result<()> {`
  - Purpose: Opens a read-write PostgreSQL connection using 'database_url' and delegates cleanup of overlay visibility state for the parent and overlay project IDs to 'cleanup_overlay_visibility_projects', returning any resulting error. [crates/gcode/src/search/fts/tests.rs:331-338]
- `OverlayFixtureCleanup` (class) component `OverlayFixtureCleanup [class]` (`31e2fc31-c40c-5bf1-9bf9-fcfe75b4496d`) lines 341-345 [crates/gcode/src/search/fts/tests.rs:341-345]
  - Signature: `impl Drop for OverlayFixtureCleanup {`
  - Purpose: 'OverlayFixtureCleanup' is a RAII cleanup guard whose 'Drop' implementation invokes 'cleanup()' on destruction and deliberately discards any resulting error. [crates/gcode/src/search/fts/tests.rs:341-345]
- `OverlayFixtureCleanup.drop` (method) component `OverlayFixtureCleanup.drop [method]` (`fcfc117f-effc-5cf1-becf-3f2e75903b65`) lines 342-344 [crates/gcode/src/search/fts/tests.rs:342-344]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Calls 'self.cleanup()' during drop and ignores its result, ensuring best-effort cleanup without propagating errors. [crates/gcode/src/search/fts/tests.rs:342-344]
- `SingleProjectCleanup` (class) component `SingleProjectCleanup [class]` (`9c551ca8-6d1f-55a7-892a-3262b1c428e2`) lines 347-350 [crates/gcode/src/search/fts/tests.rs:347-350]
  - Signature: `struct SingleProjectCleanup {`
  - Purpose: 'SingleProjectCleanup' is a data container holding a 'database_url' and a 'project_id' for cleanup operations scoped to a single project. [crates/gcode/src/search/fts/tests.rs:347-350]
- `SingleProjectCleanup` (class) component `SingleProjectCleanup [class]` (`7057c908-bfc5-538d-9f58-449e1520909d`) lines 352-358 [crates/gcode/src/search/fts/tests.rs:352-358]
  - Signature: `impl Drop for SingleProjectCleanup {`
  - Purpose: 'SingleProjectCleanup' is a 'Drop' guard that, on destruction, attempts a read-write PostgreSQL connection using its 'database_url' and invokes 'cleanup_single_project' for its 'project_id' if the connection succeeds. [crates/gcode/src/search/fts/tests.rs:352-358]
- `SingleProjectCleanup.drop` (method) component `SingleProjectCleanup.drop [method]` (`a3ac8493-2afd-57e2-bbd0-110b93040a3a`) lines 353-357 [crates/gcode/src/search/fts/tests.rs:353-357]
  - Signature: `fn drop(&mut self) {`
  - Purpose: On drop, it attempts to open a read-write PostgreSQL connection using 'self.database_url' and, if successful, calls 'cleanup_single_project' with that connection and 'self.project_id', otherwise it does nothing. [crates/gcode/src/search/fts/tests.rs:353-357]
- `cleanup_overlay_visibility_fixture` (function) component `cleanup_overlay_visibility_fixture [function]` (`217b7e05-09d4-5acc-b8b3-459b8dcbde29`) lines 360-363 [crates/gcode/src/search/fts/tests.rs:360-363]
  - Signature: `fn cleanup_overlay_visibility_fixture(conn: &mut Client, ids: &OverlayFixtureIds) {`
  - Purpose: Removes the overlay visibility fixture by calling 'cleanup_overlay_visibility_projects' for the parent and overlay project IDs, discarding the result. [crates/gcode/src/search/fts/tests.rs:360-363]
- `cleanup_single_project` (function) component `cleanup_single_project [function]` (`20a648c9-6128-5fe2-b489-05e1171388f2`) lines 365-367 [crates/gcode/src/search/fts/tests.rs:365-367]
  - Signature: `fn cleanup_single_project(conn: &mut Client, project_id: &str) {`
  - Purpose: Calls 'cleanup_overlay_visibility_projects(conn, project_id, project_id)' to clean up overlay visibility state for the given project, discarding any returned result. [crates/gcode/src/search/fts/tests.rs:365-367]
- `cleanup_overlay_visibility_projects` (function) component `cleanup_overlay_visibility_projects [function]` (`41bebba3-96fa-5b65-bc0c-3f65881e72cf`) lines 369-383 [crates/gcode/src/search/fts/tests.rs:369-383]
  - Signature: `fn cleanup_overlay_visibility_projects(`
  - Purpose: Within a transaction, this function deletes rows for both the parent and overlay project IDs from every 'OVERLAY_VISIBILITY_CHILD_TABLES' table and from 'OVERLAY_VISIBILITY_PROJECT_TABLE', then commits the transaction. [crates/gcode/src/search/fts/tests.rs:369-383]
- `seed_overlay_visibility_fixture` (function) component `seed_overlay_visibility_fixture [function]` (`ad84a5d9-b175-5bc3-a1f8-4daec0cc72f5`) lines 385-473 [crates/gcode/src/search/fts/tests.rs:385-473]
  - Signature: `fn seed_overlay_visibility_fixture(conn: &mut Client, ids: &OverlayFixtureIds) {`
  - Purpose: Seeds a test fixture for overlay visibility by creating parent and overlay projects with files, symbols, and chunks that represent visible, shadowed, and tombstoned/deleted content. [crates/gcode/src/search/fts/tests.rs:385-473]
- `insert_project` (function) component `insert_project [function]` (`3ed4b212-bb18-5901-8827-8aa5dfdbe854`) lines 475-483 [crates/gcode/src/search/fts/tests.rs:475-483]
  - Signature: `fn insert_project(conn: &mut Client, project_id: &str, root_path: &str) {`
  - Purpose: 'insert_project' inserts a new row into 'code_indexed_projects' with the given 'id' and 'root_path', initializes file and symbol counts to '0', sets 'last_indexed_at' to 'NOW()', sets 'index_duration_ms' to '0', and panics if the database insert fails. [crates/gcode/src/search/fts/tests.rs:475-483]
- `insert_file` (function) component `insert_file [function]` (`9862aa3f-335c-5433-a314-938b02cc821d`) lines 485-502 [crates/gcode/src/search/fts/tests.rs:485-502]
  - Signature: `fn insert_file(`
  - Purpose: Inserts a new 'code_indexed_files' row for the given project file, using 'project_id:file_path' as the primary 'id', a fixed placeholder content hash and byte size '1', 'symbol_count' from the caller, 'graph_synced'/'vectors_synced' set to 'false', 'graph_sync_attempted_at' as 'NULL', and 'indexed_at' as 'NOW()', panicking if the database write fails. [crates/gcode/src/search/fts/tests.rs:485-502]
- `insert_symbol` (function) component `insert_symbol [function]` (`1c8fb530-721e-5290-a7c8-66f7feebd56a`) lines 504-517 [crates/gcode/src/search/fts/tests.rs:504-517]
  - Signature: `fn insert_symbol(conn: &mut Client, project_id: &str, file_path: &str, name: &str, kind: &str) {`
  - Purpose: Inserts a 'code_symbols' row for the given Rust symbol using an ID derived from 'project_id:file_path:name', populating the key metadata fields with defaults and 'NOW()' timestamps, and panicking if the database insert fails. [crates/gcode/src/search/fts/tests.rs:504-517]
- `insert_chunk` (function) component `insert_chunk [function]` (`3913a027-5b01-5cab-8046-309dd90b2606`) lines 519-536 [crates/gcode/src/search/fts/tests.rs:519-536]
  - Signature: `fn insert_chunk(`
  - Purpose: Inserts a Rust code content chunk row into 'code_content_chunks' for the given project, file, and chunk index using a synthetic 'id', fixed 'line_start'/'line_end' of '1', 'language' set to ''rust'', and the current timestamp, failing on execution error. [crates/gcode/src/search/fts/tests.rs:519-536]
- `overlay_visibility_context` (function) component `overlay_visibility_context [function]` (`01c42c68-8644-50f6-a2cb-96c57ad72f29`) lines 538-557 [crates/gcode/src/search/fts/tests.rs:538-557]
  - Signature: `fn overlay_visibility_context(ids: &OverlayFixtureIds) -> Context {`
  - Purpose: Constructs and returns a 'Context' configured for an overlay project rooted at '/tmp/gcode-overlay', cloning the provided database and project IDs, disabling quiet-related services and daemon connection fields, and setting 'index_scope' to an 'Overlay' scope that includes both overlay and parent project/root paths. [crates/gcode/src/search/fts/tests.rs:538-557]

