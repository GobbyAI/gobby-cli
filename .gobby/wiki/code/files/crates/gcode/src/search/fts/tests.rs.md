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
  - 173-207
  - 211-239
  - 242-257
  - 260-269
  - 272-281
  - 283-302
  - 304-308
  - 310-319
  - 311-318
  - 321-325
  - 327-336
  - 328-335
  - 338-342
  - 339-341
  - 344-347
  - 349-355
  - 350-354
  - 357-360
  - 362-364
  - 366-380
  - 382-470
  - 472-480
  - 482-499
  - 501-514
  - 516-533
  - 535-554
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/search/fts/tests.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Purpose

`crates/gcode/src/search/fts/tests.rs` exposes 38 indexed API symbols.
[crates/gcode/src/search/fts/tests.rs:17-26]
[crates/gcode/src/search/fts/tests.rs:29-34]
[crates/gcode/src/search/fts/tests.rs:37-43]
[crates/gcode/src/search/fts/tests.rs:46-49]
[crates/gcode/src/search/fts/tests.rs:52-57]
[crates/gcode/src/search/fts/tests.rs:60-72]
[crates/gcode/src/search/fts/tests.rs:75-81]
[crates/gcode/src/search/fts/tests.rs:84-99]
[crates/gcode/src/search/fts/tests.rs:102-133]
[crates/gcode/src/search/fts/tests.rs:136-142]
[crates/gcode/src/search/fts/tests.rs:145-151]
[crates/gcode/src/search/fts/tests.rs:154-166]
[crates/gcode/src/search/fts/tests.rs:173-207]
[crates/gcode/src/search/fts/tests.rs:211-239]
[crates/gcode/src/search/fts/tests.rs:242-257]
[crates/gcode/src/search/fts/tests.rs:260-269]
[crates/gcode/src/search/fts/tests.rs:272-281]
[crates/gcode/src/search/fts/tests.rs:283-302]
[crates/gcode/src/search/fts/tests.rs:304-308]
[crates/gcode/src/search/fts/tests.rs:310-319]
[crates/gcode/src/search/fts/tests.rs:311-318]
[crates/gcode/src/search/fts/tests.rs:321-325]
[crates/gcode/src/search/fts/tests.rs:327-336]
[crates/gcode/src/search/fts/tests.rs:328-335]
[crates/gcode/src/search/fts/tests.rs:338-342]
[crates/gcode/src/search/fts/tests.rs:339-341]
[crates/gcode/src/search/fts/tests.rs:344-347]
[crates/gcode/src/search/fts/tests.rs:349-355]
[crates/gcode/src/search/fts/tests.rs:350-354]
[crates/gcode/src/search/fts/tests.rs:357-360]
[crates/gcode/src/search/fts/tests.rs:362-364]
[crates/gcode/src/search/fts/tests.rs:366-380]
[crates/gcode/src/search/fts/tests.rs:382-470]
[crates/gcode/src/search/fts/tests.rs:472-480]
[crates/gcode/src/search/fts/tests.rs:482-499]
[crates/gcode/src/search/fts/tests.rs:501-514]
[crates/gcode/src/search/fts/tests.rs:516-533]
[crates/gcode/src/search/fts/tests.rs:535-554]

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
- `overlay_visibility_counts_and_kinds_use_database_predicates` (function) component `overlay_visibility_counts_and_kinds_use_database_predicates [function]` (`e7a89329-186a-50f7-9f45-834cf3f5d189`) lines 173-207 [crates/gcode/src/search/fts/tests.rs:173-207]
  - Signature: `fn overlay_visibility_counts_and_kinds_use_database_predicates() {`
  - Purpose: Tests overlay visibility database predicates by asserting correct visible kinds and text/content visibility counts across parent and overlay projects. [crates/gcode/src/search/fts/tests.rs:173-207]
- `resolve_graph_symbol_by_id_resolves_exact_symbol` (function) component `resolve_graph_symbol_by_id_resolves_exact_symbol [function]` (`70ea9540-7e9c-556b-9125-c0d00efa1945`) lines 211-239 [crates/gcode/src/search/fts/tests.rs:211-239]
  - Signature: `fn resolve_graph_symbol_by_id_resolves_exact_symbol() {`
  - Purpose: This unit test verifies that `resolve_graph_symbol_by_id` correctly retrieves a symbol from the database when queried by its fully-qualified identifier (project:file:name). [crates/gcode/src/search/fts/tests.rs:211-239]
- `resolve_graph_symbol_by_id_returns_none_for_missing_uuid` (function) component `resolve_graph_symbol_by_id_returns_none_for_missing_uuid [function]` (`ac13df70-4a1b-5715-a138-bdff7efaae89`) lines 242-257 [crates/gcode/src/search/fts/tests.rs:242-257]
  - Signature: `fn resolve_graph_symbol_by_id_returns_none_for_missing_uuid() {`
  - Purpose: This test verifies that `resolve_graph_symbol_by_id` returns `None` when querying with a non-existent UUID. [crates/gcode/src/search/fts/tests.rs:242-257]
- `resolve_graph_symbol_by_id_returns_none_for_empty_id` (function) component `resolve_graph_symbol_by_id_returns_none_for_empty_id [function]` (`6ce78df0-8b75-58cb-bff6-3a7a8d5c00c2`) lines 260-269 [crates/gcode/src/search/fts/tests.rs:260-269]
  - Signature: `fn resolve_graph_symbol_by_id_returns_none_for_empty_id() {`
  - Purpose: This is a unit test that asserts `resolve_graph_symbol_by_id()` returns `None` when invoked with an empty string as the symbol identifier. [crates/gcode/src/search/fts/tests.rs:260-269]
- `resolve_graph_symbol_by_id_returns_none_for_malformed_id` (function) component `resolve_graph_symbol_by_id_returns_none_for_malformed_id [function]` (`adece121-7c6d-5c41-b9b1-559f2a896ed3`) lines 272-281 [crates/gcode/src/search/fts/tests.rs:272-281]
  - Signature: `fn resolve_graph_symbol_by_id_returns_none_for_malformed_id() {`
  - Purpose: Unit test that asserts `resolve_graph_symbol_by_id` returns `None` when provided with malformed symbol identifiers. [crates/gcode/src/search/fts/tests.rs:272-281]
- `connect_overlay_visibility_test_db` (function) component `connect_overlay_visibility_test_db [function]` (`0e326739-88d8-5971-8ddf-6a59511de529`) lines 283-302 [crates/gcode/src/search/fts/tests.rs:283-302]
  - Signature: `fn connect_overlay_visibility_test_db() -> Option<(Client, String)> {`
  - Purpose: Connects to a PostgreSQL test database from an environment variable, validates the runtime schema, and returns the connection client paired with the database URL, or None if connection or schema validation fails. [crates/gcode/src/search/fts/tests.rs:283-302]
- `OverlayFixtureIds` (class) component `OverlayFixtureIds [class]` (`c2edb10a-2bc8-5649-8aa9-099f0aa14504`) lines 304-308 [crates/gcode/src/search/fts/tests.rs:304-308]
  - Signature: `struct OverlayFixtureIds {`
  - Purpose: `OverlayFixtureIds` is a struct that bundles a database URL with parent and overlay project identifiers for managing fixture relationships between projects. [crates/gcode/src/search/fts/tests.rs:304-308]
- `OverlayFixtureIds` (class) component `OverlayFixtureIds [class]` (`b0b511f1-9935-55ea-b891-a5baf8be77f4`) lines 310-319 [crates/gcode/src/search/fts/tests.rs:310-319]
  - Signature: `impl OverlayFixtureIds {`
  - Purpose: OverlayFixtureIds initializes a test fixture that generates unique parent and overlay project identifiers derived from a common test suffix for overlay functionality testing. [crates/gcode/src/search/fts/tests.rs:310-319]
- `OverlayFixtureIds.new` (method) component `OverlayFixtureIds.new [method]` (`f64b55f9-c0e7-5456-ac7e-0ae5d3bc289e`) lines 311-318 [crates/gcode/src/search/fts/tests.rs:311-318]
  - Signature: `fn new(database_url: String) -> Self {`
  - Purpose: Constructs an instance with the provided database_url while generating unique parent and overlay project IDs derived from a test-specific suffix. [crates/gcode/src/search/fts/tests.rs:311-318]
- `OverlayFixtureCleanup` (class) component `OverlayFixtureCleanup [class]` (`2c07fc55-be3f-569c-91a0-83656dbb6696`) lines 321-325 [crates/gcode/src/search/fts/tests.rs:321-325]
  - Signature: `struct OverlayFixtureCleanup {`
  - Purpose: OverlayFixtureCleanup is a struct that encapsulates a database URL and parent/overlay project identifiers required to perform fixture cleanup operations. [crates/gcode/src/search/fts/tests.rs:321-325]
- `OverlayFixtureCleanup` (class) component `OverlayFixtureCleanup [class]` (`673b9448-55d0-5859-a47c-78489448e643`) lines 327-336 [crates/gcode/src/search/fts/tests.rs:327-336]
  - Signature: `impl OverlayFixtureCleanup {`
  - Purpose: OverlayFixtureCleanup establishes a read-write PostgreSQL connection and removes visibility relationships between parent and overlay projects during cleanup operations. [crates/gcode/src/search/fts/tests.rs:327-336]
- `OverlayFixtureCleanup.cleanup` (method) component `OverlayFixtureCleanup.cleanup [method]` (`26e8ab31-86ed-5ca5-b570-56b44149663c`) lines 328-335 [crates/gcode/src/search/fts/tests.rs:328-335]
  - Signature: `fn cleanup(&self) -> anyhow::Result<()> {`
  - Purpose: Establishes a read-write PostgreSQL connection and invokes cleanup_overlay_visibility_projects to remove visibility relationships between a parent and overlay project. [crates/gcode/src/search/fts/tests.rs:328-335]
- `OverlayFixtureCleanup` (class) component `OverlayFixtureCleanup [class]` (`7d3cefe4-8506-50e3-8415-87819a836943`) lines 338-342 [crates/gcode/src/search/fts/tests.rs:338-342]
  - Signature: `impl Drop for OverlayFixtureCleanup {`
  - Purpose: `OverlayFixtureCleanup` implements the `Drop` trait to invoke its `cleanup()` method when the value is deallocated. [crates/gcode/src/search/fts/tests.rs:338-342]
- `OverlayFixtureCleanup.drop` (method) component `OverlayFixtureCleanup.drop [method]` (`069c92e4-0653-554c-96ec-e138369841ac`) lines 339-341 [crates/gcode/src/search/fts/tests.rs:339-341]
  - Signature: `fn drop(&mut self) {`
  - Purpose: The `drop` method implements Rust's `Drop` trait to invoke a cleanup operation when the value is deallocated, discarding any return value. [crates/gcode/src/search/fts/tests.rs:339-341]
- `SingleProjectCleanup` (class) component `SingleProjectCleanup [class]` (`f8f6acf9-c230-59e0-a228-5dfbc798e605`) lines 344-347 [crates/gcode/src/search/fts/tests.rs:344-347]
  - Signature: `struct SingleProjectCleanup {`
  - Purpose: `SingleProjectCleanup` is a struct that encapsulates a database URL and project ID required to perform cleanup operations on a single project. [crates/gcode/src/search/fts/tests.rs:344-347]
- `SingleProjectCleanup` (class) component `SingleProjectCleanup [class]` (`d4232e2f-aebe-52fb-ac05-20a32531a353`) lines 349-355 [crates/gcode/src/search/fts/tests.rs:349-355]
  - Signature: `impl Drop for SingleProjectCleanup {`
  - Purpose: `SingleProjectCleanup` implements the `Drop` trait to execute project-specific PostgreSQL cleanup via a read-write database connection upon value deallocation. [crates/gcode/src/search/fts/tests.rs:349-355]
- `SingleProjectCleanup.drop` (method) component `SingleProjectCleanup.drop [method]` (`ff80a57a-18f8-59af-b135-0efb3fe1dd44`) lines 350-354 [crates/gcode/src/search/fts/tests.rs:350-354]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Drops the associated project from the PostgreSQL database by establishing a read-write connection and calling `cleanup_single_project` when the value is deallocated. [crates/gcode/src/search/fts/tests.rs:350-354]
- `cleanup_overlay_visibility_fixture` (function) component `cleanup_overlay_visibility_fixture [function]` (`21f764c8-ccab-5311-975a-c3499cd9be81`) lines 357-360 [crates/gcode/src/search/fts/tests.rs:357-360]
  - Signature: `fn cleanup_overlay_visibility_fixture(conn: &mut Client, ids: &OverlayFixtureIds) {`
  - Purpose: Removes overlay visibility relationships between parent and overlay projects by delegating to `cleanup_overlay_visibility_projects` with the extracted project identifiers. [crates/gcode/src/search/fts/tests.rs:357-360]
- `cleanup_single_project` (function) component `cleanup_single_project [function]` (`4254b793-3d52-581a-8a61-5f0134ac7d20`) lines 362-364 [crates/gcode/src/search/fts/tests.rs:362-364]
  - Signature: `fn cleanup_single_project(conn: &mut Client, project_id: &str) {`
  - Purpose: Delegates overlay visibility cleanup for a single project to `cleanup_overlay_visibility_projects`, passing the project ID as both source and target identifiers. [crates/gcode/src/search/fts/tests.rs:362-364]
- `cleanup_overlay_visibility_projects` (function) component `cleanup_overlay_visibility_projects [function]` (`8d662aa4-aad8-52aa-b186-0cd53d1ddc13`) lines 366-380 [crates/gcode/src/search/fts/tests.rs:366-380]
  - Signature: `fn cleanup_overlay_visibility_projects(`
  - Purpose: Transactionally deletes overlay visibility project records and their child table entries for two specified project IDs. [crates/gcode/src/search/fts/tests.rs:366-380]
- `seed_overlay_visibility_fixture` (function) component `seed_overlay_visibility_fixture [function]` (`e7450bd9-79a8-5dc2-b73f-4e01dc4cbf3a`) lines 382-470 [crates/gcode/src/search/fts/tests.rs:382-470]
  - Signature: `fn seed_overlay_visibility_fixture(conn: &mut Client, ids: &OverlayFixtureIds) {`
  - Purpose: This function seeds a database with test fixtures comprising parent and overlay projects containing files, symbols, and chunks to validate visibility behavior when an overlay project shadows and deletes resources from a parent project. [crates/gcode/src/search/fts/tests.rs:382-470]
- `insert_project` (function) component `insert_project [function]` (`9a5ed7b9-87d8-55c9-952f-9be23dd54838`) lines 472-480 [crates/gcode/src/search/fts/tests.rs:472-480]
  - Signature: `fn insert_project(conn: &mut Client, project_id: &str, root_path: &str) {`
  - Purpose: Inserts a new project record into the `code_indexed_projects` table with the given project ID and root path, initializing file and symbol counts to zero and setting the last indexed timestamp to the current time. [crates/gcode/src/search/fts/tests.rs:472-480]
- `insert_file` (function) component `insert_file [function]` (`c8eadff2-15a4-5099-b73d-9941c7866c77`) lines 482-499 [crates/gcode/src/search/fts/tests.rs:482-499]
  - Signature: `fn insert_file(`
  - Purpose: Inserts a code-indexed file metadata record into the database with provided language and symbol count, initializing both graph and vector sync status fields to false and setting the indexed timestamp to the current time. [crates/gcode/src/search/fts/tests.rs:482-499]
- `insert_symbol` (function) component `insert_symbol [function]` (`0bf71dd4-c8a5-53ab-a576-33893c11c841`) lines 501-514 [crates/gcode/src/search/fts/tests.rs:501-514]
  - Signature: `fn insert_symbol(conn: &mut Client, project_id: &str, file_path: &str, name: &str, kind: &str) {`
  - Purpose: Inserts a code symbol record into the `code_symbols` table with a composite ID key (project_id:file_path:name), hardcoded Rust language, and default placeholder values for parsing metadata (byte/line positions, signature, and docstring fields). [crates/gcode/src/search/fts/tests.rs:501-514]
- `insert_chunk` (function) component `insert_chunk [function]` (`1983b58d-145c-5e2a-9bbf-85bdc4b3ddef`) lines 516-533 [crates/gcode/src/search/fts/tests.rs:516-533]
  - Signature: `fn insert_chunk(`
  - Purpose: Inserts a code chunk record into the `code_content_chunks` table with a composite ID derived from project_id:file_path:chunk_index, storing the content with hard-coded language ('rust') and fixed line boundaries. [crates/gcode/src/search/fts/tests.rs:516-533]
- `overlay_visibility_context` (function) component `overlay_visibility_context [function]` (`ace6cf3e-47ec-5e0f-ba94-e00bc5fabbbb`) lines 535-554 [crates/gcode/src/search/fts/tests.rs:535-554]
  - Signature: `fn overlay_visibility_context(ids: &OverlayFixtureIds) -> Context {`
  - Purpose: Constructs a Context struct configured for overlay project indexing, initialized with provided fixture IDs and hardcoded temporary project paths, with external services disabled. [crates/gcode/src/search/fts/tests.rs:535-554]

