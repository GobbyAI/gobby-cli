---
title: crates/gcode/src/index/indexer/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/tests.rs
  ranges:
  - 22-28
  - 30-38
  - 41-60
  - 63-82
  - 85-103
  - 106-150
  - 153-161
  - 163-212
  - 164-167
  - 169-173
  - 175-179
  - 181-190
  - 192-205
  - 207-211
  - 215-282
  - 285-307
  - 310-346
  - 349-385
  - 388-418
  - 421-447
  - 450-472
  - 475-490
  - 493-542
  - 545-573
  - 576-626
  - 629-666
  - 669-695
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/tests.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

`crates/gcode/src/index/indexer/tests.rs` exposes 27 indexed API symbols.
[crates/gcode/src/index/indexer/tests.rs:22-28]
[crates/gcode/src/index/indexer/tests.rs:30-38]
[crates/gcode/src/index/indexer/tests.rs:41-60]
[crates/gcode/src/index/indexer/tests.rs:63-82]
[crates/gcode/src/index/indexer/tests.rs:85-103]
[crates/gcode/src/index/indexer/tests.rs:106-150]
[crates/gcode/src/index/indexer/tests.rs:153-161]
[crates/gcode/src/index/indexer/tests.rs:163-212]
[crates/gcode/src/index/indexer/tests.rs:164-167]
[crates/gcode/src/index/indexer/tests.rs:169-173]
[crates/gcode/src/index/indexer/tests.rs:175-179]
[crates/gcode/src/index/indexer/tests.rs:181-190]
[crates/gcode/src/index/indexer/tests.rs:192-205]
[crates/gcode/src/index/indexer/tests.rs:207-211]
[crates/gcode/src/index/indexer/tests.rs:215-282]
[crates/gcode/src/index/indexer/tests.rs:285-307]
[crates/gcode/src/index/indexer/tests.rs:310-346]
[crates/gcode/src/index/indexer/tests.rs:349-385]
[crates/gcode/src/index/indexer/tests.rs:388-418]
[crates/gcode/src/index/indexer/tests.rs:421-447]
[crates/gcode/src/index/indexer/tests.rs:450-472]
[crates/gcode/src/index/indexer/tests.rs:475-490]
[crates/gcode/src/index/indexer/tests.rs:493-542]
[crates/gcode/src/index/indexer/tests.rs:545-573]
[crates/gcode/src/index/indexer/tests.rs:576-626]
[crates/gcode/src/index/indexer/tests.rs:629-666]
[crates/gcode/src/index/indexer/tests.rs:669-695]

## API Symbols

- `write_file` (function) component `write_file [function]` (`7ff9eba8-b8db-5bc6-bdb0-6efbb21c9347`) lines 22-28 [crates/gcode/src/index/indexer/tests.rs:22-28]
  - Signature: `fn write_file(root: &Path, rel: &str, contents: &[u8]) {`
  - Purpose: Joins `rel` onto `root`, creates any missing parent directories, and writes `contents` to the resulting path, panicking on any I/O failure. [crates/gcode/src/index/indexer/tests.rs:22-28]
- `assert_cli_independent_contract` (function) component `assert_cli_independent_contract [function]` (`9a555508-69c1-5909-9d69-a1fb754b3296`) lines 30-38 [crates/gcode/src/index/indexer/tests.rs:30-38]
  - Signature: `fn assert_cli_independent_contract<T>()`
  - Purpose: Asserts at runtime that a serializable/deserializable generic type `T` is CLI-independent by rejecting any type whose fully qualified name contains `commands::`, `output::`, or `clap`. [crates/gcode/src/index/indexer/tests.rs:30-38]
- `library_api_is_cli_independent` (function) component `library_api_is_cli_independent [function]` (`b1f8c304-eba0-5ff2-9f43-6400e08ce6dc`) lines 41-60 [crates/gcode/src/index/indexer/tests.rs:41-60]
  - Signature: `fn library_api_is_cli_independent() {`
  - Purpose: Verifies that the indexing library API types are CLI-independent and that `IndexRequest` serializes its `PathBuf` fields to the expected JSON string values. [crates/gcode/src/index/indexer/tests.rs:41-60]
- `invalidate_postgres_deletes_are_project_scoped` (function) component `invalidate_postgres_deletes_are_project_scoped [function]` (`978e1e00-800a-57c9-9b44-25220237960b`) lines 63-82 [crates/gcode/src/index/indexer/tests.rs:63-82]
  - Signature: `fn invalidate_postgres_deletes_are_project_scoped() {`
  - Purpose: It verifies that `lifecycle.rs` performs only project-scoped `DELETE` statements for the indexed code tables and `code_indexed_projects`, and that it does not contain any `TRUNCATE` or `DROP TABLE` operations. [crates/gcode/src/index/indexer/tests.rs:63-82]
- `current_file_state_keeps_unhashable_paths_present` (function) component `current_file_state_keeps_unhashable_paths_present [function]` (`195a4b66-14f8-5543-b933-2ec31aaade71`) lines 85-103 [crates/gcode/src/index/indexer/tests.rs:85-103]
  - Signature: `fn current_file_state_keeps_unhashable_paths_present() {`
  - Purpose: Verifies that `current_file_state` records both a regular file and an unhashable directory as present, but only computes a content hash for the file path. [crates/gcode/src/index/indexer/tests.rs:85-103]
- `unsupported_file_types_group_content_only_paths` (function) component `unsupported_file_types_group_content_only_paths [function]` (`2b40a5c0-fcbb-59a1-9d4c-b51da7c521ab`) lines 106-150 [crates/gcode/src/index/indexer/tests.rs:106-150]
  - Signature: `fn unsupported_file_types_group_content_only_paths() {`
  - Purpose: This test creates a temporary directory with unsupported files of several types, then verifies that `unsupported_file_types` groups them by normalized extension (including case-insensitive `.txt` and `extensionless`) and reports the correct file counts and example paths for each group. [crates/gcode/src/index/indexer/tests.rs:106-150]
- `RecordingCodeFactSink` (class) component `RecordingCodeFactSink [class]` (`21136c8d-da12-54b0-a33d-e0a769e092b4`) lines 153-161 [crates/gcode/src/index/indexer/tests.rs:153-161]
  - Signature: `struct RecordingCodeFactSink {`
  - Purpose: A recording sink for code-fact events that stores the emitted write labels and maintains counters for files, symbols, imports, calls, unresolved targets, and chunks. [crates/gcode/src/index/indexer/tests.rs:153-161]
- `RecordingCodeFactSink` (class) component `RecordingCodeFactSink [class]` (`3d540223-37a6-583f-8847-1c21135796cf`) lines 163-212 [crates/gcode/src/index/indexer/tests.rs:163-212]
  - Signature: `impl CodeFactSink for RecordingCodeFactSink {`
  - Purpose: `RecordingCodeFactSink` is an in-memory `CodeFactSink` test double that records each write operation type and accumulates counts for files, symbols, imports, calls, unresolved call targets, and content chunks while returning the number of items processed. [crates/gcode/src/index/indexer/tests.rs:163-212]
- `RecordingCodeFactSink.delete_file_facts` (method) component `RecordingCodeFactSink.delete_file_facts [method]` (`418c8dbc-db4b-53d9-bf76-24589ec762b5`) lines 164-167 [crates/gcode/src/index/indexer/tests.rs:164-167]
  - Signature: `fn delete_file_facts(&mut self, _project_id: &str, _file_path: &str) -> anyhow::Result<()> {`
  - Purpose: Appends the string `"delete"` to `self.writes` and returns `Ok(())`, ignoring both input parameters. [crates/gcode/src/index/indexer/tests.rs:164-167]
- `RecordingCodeFactSink.upsert_symbols` (method) component `RecordingCodeFactSink.upsert_symbols [method]` (`5eca98d9-75a0-586c-8cc4-7ae6518214aa`) lines 169-173 [crates/gcode/src/index/indexer/tests.rs:169-173]
  - Signature: `fn upsert_symbols(&mut self, symbols: &[Symbol]) -> anyhow::Result<usize> {`
  - Purpose: Appends `"symbols"` to `self.writes`, increments `self.symbols` by `symbols.len()`, and returns `Ok(symbols.len())`. [crates/gcode/src/index/indexer/tests.rs:169-173]
- `RecordingCodeFactSink.upsert_file` (method) component `RecordingCodeFactSink.upsert_file [method]` (`8ba21fb8-10fa-50ee-ac45-309ce60dcddb`) lines 175-179 [crates/gcode/src/index/indexer/tests.rs:175-179]
  - Signature: `fn upsert_file(&mut self, _file: &IndexedFile) -> anyhow::Result<()> {`
  - Purpose: `upsert_file` records a file write by pushing `"file"` onto `self.writes`, incrementing `self.files` by one, and returning `Ok(())`. [crates/gcode/src/index/indexer/tests.rs:175-179]
- `RecordingCodeFactSink.upsert_imports` (method) component `RecordingCodeFactSink.upsert_imports [method]` (`317b60d8-7ae5-5a9b-acfd-2f38f150ed09`) lines 181-190 [crates/gcode/src/index/indexer/tests.rs:181-190]
  - Signature: `fn upsert_imports(`
  - Purpose: Appends an `"imports"` write marker, increments the internal `imports` counter by `imports.len()`, and returns that count as the number of upserted import relations. [crates/gcode/src/index/indexer/tests.rs:181-190]
- `RecordingCodeFactSink.upsert_calls` (method) component `RecordingCodeFactSink.upsert_calls [method]` (`9c7a8695-2cc0-5d70-8773-f39d86f7c7a1`) lines 192-205 [crates/gcode/src/index/indexer/tests.rs:192-205]
  - Signature: `fn upsert_calls(`
  - Purpose: `upsert_calls` records a `"calls"` write marker, increments the total call count by `calls.len()` and the unresolved-target counter by the number of `CallRelation`s whose `callee_target_kind` is `Unresolved`, then returns `Ok(calls.len())`, ignoring `project_id` and `file_path`. [crates/gcode/src/index/indexer/tests.rs:192-205]
- `RecordingCodeFactSink.upsert_content_chunks` (method) component `RecordingCodeFactSink.upsert_content_chunks [method]` (`2ac82aa1-e5d8-5ee5-9451-67b51f527bf9`) lines 207-211 [crates/gcode/src/index/indexer/tests.rs:207-211]
  - Signature: `fn upsert_content_chunks(&mut self, chunks: &[ContentChunk]) -> anyhow::Result<usize> {`
  - Purpose: `upsert_content_chunks` logs a `"chunks"` write, increments the internal `chunks` counter by `chunks.len()`, and returns that count as `Ok(usize)`. [crates/gcode/src/index/indexer/tests.rs:207-211]
- `library_writes_all_code_facts` (function) component `library_writes_all_code_facts [function]` (`c8d4bb7b-1791-543c-82e7-c90f678d6fac`) lines 215-282 [crates/gcode/src/index/indexer/tests.rs:215-282]
  - Signature: `fn library_writes_all_code_facts() {`
  - Purpose: This test verifies that `write_parsed_file_facts` persists a parsed Rust file by emitting `delete`, `symbols`, `file`, `imports`, `calls`, and `chunks` writes and by returning the expected counts for one file, one symbol, one import, one call, one unresolved target, and one chunk. [crates/gcode/src/index/indexer/tests.rs:215-282]
- `call_relation_contract_uses_empty_optional_storage_values` (function) component `call_relation_contract_uses_empty_optional_storage_values [function]` (`71433a86-3291-5004-9775-de0b34753ffe`) lines 285-307 [crates/gcode/src/index/indexer/tests.rs:285-307]
  - Signature: `fn call_relation_contract_uses_empty_optional_storage_values() {`
  - Purpose: Verifies that `CallRelation` stores a symbol-targeted callee ID when set, leaves `callee_symbol_id` empty for unresolved relations, and assigns `callee_target_kind` as `Symbol` versus `Unresolved` accordingly. [crates/gcode/src/index/indexer/tests.rs:285-307]
- `explicit_file_route_sends_unsupported_text_to_content_only` (function) component `explicit_file_route_sends_unsupported_text_to_content_only [function]` (`c3f8ea7c-3223-52ae-9c2b-bad4d837a14d`) lines 310-346 [crates/gcode/src/index/indexer/tests.rs:310-346]
  - Signature: `fn explicit_file_route_sends_unsupported_text_to_content_only() {`
  - Purpose: Verifies that `explicit_file_route` returns `Ast` for a Rust source file, `ContentOnly` for supported plain-text files like `notes.txt` and `Dockerfile`, and `Skip` for excluded, secret-like, generated, or binary files under `DEFAULT_EXCLUDES`. [crates/gcode/src/index/indexer/tests.rs:310-346]
- `explicit_file_routes_follow_respect_gitignore_setting` (function) component `explicit_file_routes_follow_respect_gitignore_setting [function]` (`89f71fe7-84ef-535c-94c8-5c133c4cca52`) lines 349-385 [crates/gcode/src/index/indexer/tests.rs:349-385]
  - Signature: `fn explicit_file_routes_follow_respect_gitignore_setting() {`
  - Purpose: This test verifies that `explicit_route_with_discovery_options` returns `ExplicitFileRoute::Skip` for a gitignored file and `ExplicitFileRoute::Ast` for a non-ignored file when `respect_gitignore` is `true`, but returns `ExplicitFileRoute::Ast` for the ignored file when `respect_gitignore` is `false`. [crates/gcode/src/index/indexer/tests.rs:349-385]
- `explicit_file_route_applies_parent_gitignore_without_full_discovery` (function) component `explicit_file_route_applies_parent_gitignore_without_full_discovery [function]` (`8b64e2de-681b-5327-a65c-a6bf97ad0b68`) lines 388-418 [crates/gcode/src/index/indexer/tests.rs:388-418]
  - Signature: `fn explicit_file_route_applies_parent_gitignore_without_full_discovery() {`
  - Purpose: Verifies that `explicit_route_with_discovery_options` honors a parent `src/.gitignore` when evaluating explicit files, returning `ExplicitFileRoute::Skip` for `src/ignored.rs` and `ExplicitFileRoute::Ast` for `src/visible.rs` without requiring full directory discovery. [crates/gcode/src/index/indexer/tests.rs:388-418]
- `explicit_file_route_indexes_mjs_and_routes_markdown_to_content_only` (function) component `explicit_file_route_indexes_mjs_and_routes_markdown_to_content_only [function]` (`7cd4e722-01fb-5699-b7db-3395adfd8335`) lines 421-447 [crates/gcode/src/index/indexer/tests.rs:421-447]
  - Signature: `fn explicit_file_route_indexes_mjs_and_routes_markdown_to_content_only() {`
  - Purpose: Creates a temporary project tree and asserts that `explicit_file_route` classifies `.mjs` files as `Ast` while routing `.md`, `.markdown`, and `.yml` files to `ContentOnly` under `DEFAULT_EXCLUDES`. [crates/gcode/src/index/indexer/tests.rs:421-447]
- `discovered_hidden_workflows_survive_index_path_filter` (function) component `discovered_hidden_workflows_survive_index_path_filter [function]` (`5f2c8897-001b-5abc-8729-35fbd8cafb32`) lines 450-472 [crates/gcode/src/index/indexer/tests.rs:450-472]
  - Signature: `fn discovered_hidden_workflows_survive_index_path_filter() {`
  - Purpose: This test verifies that `filter_discovered_paths` preserves discovered files under `.github/workflows` when filtering by that index path, while excluding other hidden paths such as `.gobby/plans/plan.md`. [crates/gcode/src/index/indexer/tests.rs:450-472]
- `explicit_file_route_skips_generated_mjs` (function) component `explicit_file_route_skips_generated_mjs [function]` (`7d1e2cf0-4955-5953-bf5e-e477404bf78e`) lines 475-490 [crates/gcode/src/index/indexer/tests.rs:475-490]
  - Signature: `fn explicit_file_route_skips_generated_mjs() {`
  - Purpose: This test verifies that `explicit_file_route` returns `ExplicitFileRoute::Skip` for an explicit `src/setup.mjs` path containing the generated-file banner when checked against `DEFAULT_EXCLUDES`. [crates/gcode/src/index/indexer/tests.rs:475-490]
- `explicit_skip_cleanup_deletes_stale_facts_and_projections` (function) component `explicit_skip_cleanup_deletes_stale_facts_and_projections [function]` (`34d856bd-9b99-5236-a485-b2e84f9ce053`) lines 493-542 [crates/gcode/src/index/indexer/tests.rs:493-542]
  - Signature: `fn explicit_skip_cleanup_deletes_stale_facts_and_projections() {`
  - Purpose: This test verifies that `cleanup_skipped_explicit_file_if_indexed` invokes the deletion callback for an explicitly skipped indexed file, increments `outcome.skipped_files`, and records two `IndexDegradation::ProjectionCleanupFailed` entries for the graph and vector targets. [crates/gcode/src/index/indexer/tests.rs:493-542]
- `explicit_skip_cleanup_ignores_never_indexed_files` (function) component `explicit_skip_cleanup_ignores_never_indexed_files [function]` (`bf0534e8-aa11-5a70-b062-993812c9bfef`) lines 545-573 [crates/gcode/src/index/indexer/tests.rs:545-573]
  - Signature: `fn explicit_skip_cleanup_ignores_never_indexed_files() {`
  - Purpose: Verifies that `cleanup_skipped_explicit_file_if_indexed` treats an explicitly skipped file marked as never indexed (`Some(false)`) as a no-op, does not invoke the delete callback, increments `outcome.skipped_files`, and leaves `outcome.degraded` empty. [crates/gcode/src/index/indexer/tests.rs:545-573]
- `overlay_reconciliation_actions_cover_inherit_shadow_add_delete` (function) component `overlay_reconciliation_actions_cover_inherit_shadow_add_delete [function]` (`e7bad465-74e8-5d60-b4bd-ece2ef2aa94b`) lines 576-626 [crates/gcode/src/index/indexer/tests.rs:576-626]
  - Signature: `fn overlay_reconciliation_actions_cover_inherit_shadow_add_delete() {`
  - Purpose: This test verifies that `overlay_reconcile_action` returns the correct `OverlayReconcileAction` for overlay reconciliation scenarios spanning inherited unchanged content, re-indexing edited or newly added files, tombstoning missing parent entries, skipping already tombstoned entries, and deleting stray overlay-only entries. [crates/gcode/src/index/indexer/tests.rs:576-626]
- `deleted_file_projection_cleanup_degrades_without_services` (function) component `deleted_file_projection_cleanup_degrades_without_services [function]` (`670ef2f6-c6c5-5e05-bb96-bdc788727c6d`) lines 629-666 [crates/gcode/src/index/indexer/tests.rs:629-666]
  - Signature: `fn deleted_file_projection_cleanup_degrades_without_services() {`
  - Purpose: Verifies that `cleanup_deleted_file_projections` degrades gracefully when graph and vector services are unconfigured by recording two `ProjectionCleanupFailed` degradations for the deleted file, one for `ProjectionTarget::Graph` and one for `ProjectionTarget::Vectors`, with the expected configuration error messages. [crates/gcode/src/index/indexer/tests.rs:629-666]
- `deleted_file_projection_cleanup_skips_vectors_when_not_previously_synced` (function) component `deleted_file_projection_cleanup_skips_vectors_when_not_previously_synced [function]` (`8321812f-69ec-586f-a357-9db2017403ec`) lines 669-695 [crates/gcode/src/index/indexer/tests.rs:669-695]
  - Signature: `fn deleted_file_projection_cleanup_skips_vectors_when_not_previously_synced() {`
  - Purpose: Verifies that `cleanup_deleted_file_projections` treats a deleted file marked as not previously synced (`Some(false)`) as graph-only cleanup, recording exactly one `IndexDegradation::ProjectionCleanupFailed` for `ProjectionTarget::Graph` and not emitting any vector cleanup degradation. [crates/gcode/src/index/indexer/tests.rs:669-695]

