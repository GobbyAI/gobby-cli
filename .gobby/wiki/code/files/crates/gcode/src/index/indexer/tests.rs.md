---
title: crates/gcode/src/index/indexer/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/tests.rs
  ranges:
  - 24-30
  - 32-40
  - 43-62
  - 65-84
  - 87-105
  - 108-152
  - 155-164
  - 166-235
  - 238-314
  - 325-396
  - 399-405
  - 407-413
  - 415-418
  - 420-426
  - 428-459
  - 461-488
  - 490-517
  - 519-527
  - 529-539
  - 542-564
  - 567-603
  - 606-642
  - 645-675
  - 678-704
  - 707-729
  - 732-747
  - 750-799
  - 802-830
  - 833-883
  - 886-923
  - 926-952
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/tests.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

This file contains the indexer’s test suite, with small helpers for writing temp files and asserting that public indexer types remain CLI-independent, plus a `RecordingCodeFactSink` test double that tracks every code-fact write path. The tests exercise file indexing and cleanup behavior end to end: serialization contracts, PostgreSQL invalidation scoping, unsupported-file classification, parsed-file fact emission, symbol-summary preservation across reindexing, explicit file routing and gitignore handling, overlay reconciliation, and deleted/skipped file projection cleanup.
[crates/gcode/src/index/indexer/tests.rs:24-30]
[crates/gcode/src/index/indexer/tests.rs:32-40]
[crates/gcode/src/index/indexer/tests.rs:43-62]
[crates/gcode/src/index/indexer/tests.rs:65-84]
[crates/gcode/src/index/indexer/tests.rs:87-105]

## API Symbols

- `write_file` (function) component `write_file [function]` (`93b52f75-55a1-5025-a3a4-7e3d067416a6`) lines 24-30 [crates/gcode/src/index/indexer/tests.rs:24-30]
  - Signature: `fn write_file(root: &Path, rel: &str, contents: &[u8]) {`
  - Purpose: Creates the target path by joining 'rel' to 'root', ensures its parent directory exists with 'create_dir_all', and then writes 'contents' to the file, panicking on any I/O error. [crates/gcode/src/index/indexer/tests.rs:24-30]
- `assert_cli_independent_contract` (function) component `assert_cli_independent_contract [function]` (`c9ca8599-c3b6-56f5-a793-8464d6dd688a`) lines 32-40 [crates/gcode/src/index/indexer/tests.rs:32-40]
  - Signature: `fn assert_cli_independent_contract<T>()`
  - Purpose: Verifies at runtime that the generic type 'T' is not a CLI-specific type by asserting its Rust type name contains neither 'commands::', 'output::', nor 'clap', while requiring 'T: Serialize + DeserializeOwned'. [crates/gcode/src/index/indexer/tests.rs:32-40]
- `library_api_is_cli_independent` (function) component `library_api_is_cli_independent [function]` (`a75050de-6e71-506b-b6d9-97a4765ea6b7`) lines 43-62 [crates/gcode/src/index/indexer/tests.rs:43-62]
  - Signature: `fn library_api_is_cli_independent() {`
  - Purpose: Verifies that the 'IndexRequest', 'IndexOutcome', 'IndexDurations', and 'IndexDegradation' library types satisfy the CLI-independent contract and that an 'IndexRequest' serializes path fields as relative strings rather than CLI-specific values. [crates/gcode/src/index/indexer/tests.rs:43-62]
- `invalidate_postgres_deletes_are_project_scoped` (function) component `invalidate_postgres_deletes_are_project_scoped [function]` (`b35c0484-ef88-5e10-bcc0-132cc5775747`) lines 65-84 [crates/gcode/src/index/indexer/tests.rs:65-84]
  - Signature: `fn invalidate_postgres_deletes_are_project_scoped() {`
  - Purpose: Verifies that 'lifecycle.rs' uses project-scoped 'DELETE' statements for the expected PostgreSQL tables and does not contain any 'TRUNCATE' or 'DROP TABLE' operations. [crates/gcode/src/index/indexer/tests.rs:65-84]
- `current_file_state_keeps_unhashable_paths_present` (function) component `current_file_state_keeps_unhashable_paths_present [function]` (`bc26aaea-8070-5ffb-a5f3-5ffd1e0dddda`) lines 87-105 [crates/gcode/src/index/indexer/tests.rs:87-105]
  - Signature: `fn current_file_state_keeps_unhashable_paths_present() {`
  - Purpose: Verifies that 'current_file_state' records both readable and unreadable paths as present, while only computing a hash for the readable file and omitting the unhashable directory from 'hashes'. [crates/gcode/src/index/indexer/tests.rs:87-105]
- `unsupported_file_types_group_content_only_paths` (function) component `unsupported_file_types_group_content_only_paths [function]` (`b15fe3b0-af43-55b5-a6bf-e1a7641fa3c0`) lines 108-152 [crates/gcode/src/index/indexer/tests.rs:108-152]
  - Signature: `fn unsupported_file_types_group_content_only_paths() {`
  - Purpose: Creates a temporary directory with mixed file names and verifies that 'unsupported_file_types' groups unsupported paths by normalized extension, counts files per group, and records representative examples, including case-insensitive '.txt' matching and an 'extensionless' bucket for 'Dockerfile'. [crates/gcode/src/index/indexer/tests.rs:108-152]
- `RecordingCodeFactSink` (class) component `RecordingCodeFactSink [class]` (`5227db9f-8954-5910-81bf-40152c3b2374`) lines 155-164 [crates/gcode/src/index/indexer/tests.rs:155-164]
  - Signature: `struct RecordingCodeFactSink {`
  - Purpose: 'RecordingCodeFactSink' is a simple in-memory sink that records written string entries while tracking aggregate counts for files, symbols, stale symbols, imports, calls, unresolved targets, and chunks. [crates/gcode/src/index/indexer/tests.rs:155-164]
- `RecordingCodeFactSink` (class) component `RecordingCodeFactSink [class]` (`1ca5dd93-8369-586f-90a3-1b1f414fddef`) lines 166-235 [crates/gcode/src/index/indexer/tests.rs:166-235]
  - Signature: `impl CodeFactSink for RecordingCodeFactSink {`
  - Purpose: RecordingCodeFactSink is a 'CodeFactSink' test double that records each write operation in order while tallying deletes, symbol/file/import/call/chunk upserts, stale symbol IDs processed, and unresolved call targets. [crates/gcode/src/index/indexer/tests.rs:166-235]
- `RecordingCodeFactSink.delete_file_facts` (method) component `RecordingCodeFactSink.delete_file_facts [method]` (`2cbfe908-794d-506c-927c-a073cc7bb09d`) lines 167-170 [crates/gcode/src/index/indexer/tests.rs:167-170]
  - Signature: `fn delete_file_facts(&mut self, _project_id: &str, _file_path: &str) -> anyhow::Result<()> {`
  - Purpose: Appends the string '"delete"' to 'self.writes' and returns 'Ok(())', ignoring both '_project_id' and '_file_path'. [crates/gcode/src/index/indexer/tests.rs:167-170]
- `RecordingCodeFactSink.delete_file_non_symbol_facts` (method) component `RecordingCodeFactSink.delete_file_non_symbol_facts [method]` (`57e95b23-33f2-56f1-9d50-18e93bae14a3`) lines 172-179 [crates/gcode/src/index/indexer/tests.rs:172-179]
  - Signature: `fn delete_file_non_symbol_facts(`
  - Purpose: Mutably records a 'delete_non_symbols' write marker in 'self.writes' and returns 'Ok(())', ignoring both '_project_id' and '_file_path'. [crates/gcode/src/index/indexer/tests.rs:172-179]
- `RecordingCodeFactSink.delete_stale_file_symbols` (method) component `RecordingCodeFactSink.delete_stale_file_symbols [method]` (`0b0bf71f-fe23-500b-9d8a-3c9a2afc8c62`) lines 181-190 [crates/gcode/src/index/indexer/tests.rs:181-190]
  - Signature: `fn delete_stale_file_symbols(`
  - Purpose: 'delete_stale_file_symbols' records a '"delete_stale_symbols"' write, increments 'self.stale_symbols' by 'current_symbol_ids.len()', ignores the project and file inputs, and returns 'Ok(0)'. [crates/gcode/src/index/indexer/tests.rs:181-190]
- `RecordingCodeFactSink.upsert_symbols` (method) component `RecordingCodeFactSink.upsert_symbols [method]` (`90ed7a42-9cd0-5329-96ed-d6884fc38008`) lines 192-196 [crates/gcode/src/index/indexer/tests.rs:192-196]
  - Signature: `fn upsert_symbols(&mut self, symbols: &[Symbol]) -> anyhow::Result<usize> {`
  - Purpose: Appends the '"symbols"' write marker, increments 'self.symbols' by 'symbols.len()', and returns 'Ok(symbols.len())' as the count of upserted symbols. [crates/gcode/src/index/indexer/tests.rs:192-196]
- `RecordingCodeFactSink.upsert_file` (method) component `RecordingCodeFactSink.upsert_file [method]` (`4b97fd8d-91c4-5de4-ba7c-1f29360ca45b`) lines 198-202 [crates/gcode/src/index/indexer/tests.rs:198-202]
  - Signature: `fn upsert_file(&mut self, _file: &IndexedFile) -> anyhow::Result<()> {`
  - Purpose: Appends '"file"' to 'writes', increments 'files' by 1, and returns 'Ok(())' without otherwise using the provided 'IndexedFile' argument. [crates/gcode/src/index/indexer/tests.rs:198-202]
- `RecordingCodeFactSink.upsert_imports` (method) component `RecordingCodeFactSink.upsert_imports [method]` (`d9cfd64d-fc55-5dfa-a38b-362fbc1f3114`) lines 204-213 [crates/gcode/src/index/indexer/tests.rs:204-213]
  - Signature: `fn upsert_imports(`
  - Purpose: 'upsert_imports' records an '"imports"' write marker, increments the internal 'imports' counter by the number of 'ImportRelation' items provided, and returns that count as 'Ok(usize)', ignoring '_project_id' and '_file_path'. [crates/gcode/src/index/indexer/tests.rs:204-213]
- `RecordingCodeFactSink.upsert_calls` (method) component `RecordingCodeFactSink.upsert_calls [method]` (`1f23c1ce-dc5f-5a3a-b7d7-6d0460aa821a`) lines 215-228 [crates/gcode/src/index/indexer/tests.rs:215-228]
  - Signature: `fn upsert_calls(`
  - Purpose: 'upsert_calls' records a calls write, increments the stored call count by the number of 'CallRelation' entries, increments 'unresolved_targets' by the number whose 'callee_target_kind' is 'CallTargetKind::Unresolved', and returns the number of calls processed. [crates/gcode/src/index/indexer/tests.rs:215-228]
- `RecordingCodeFactSink.upsert_content_chunks` (method) component `RecordingCodeFactSink.upsert_content_chunks [method]` (`337e0088-4236-5a84-956d-8ef4e82ed3a6`) lines 230-234 [crates/gcode/src/index/indexer/tests.rs:230-234]
  - Signature: `fn upsert_content_chunks(&mut self, chunks: &[ContentChunk]) -> anyhow::Result<usize> {`
  - Purpose: Appends the '"chunks"' write marker, increments the internal chunk count by the number of input 'ContentChunk's, and returns that count as 'Ok(len)'. [crates/gcode/src/index/indexer/tests.rs:230-234]
- `library_writes_all_code_facts` (function) component `library_writes_all_code_facts [function]` (`d345608e-3d2e-57d3-b30d-2559654276aa`) lines 238-314 [crates/gcode/src/index/indexer/tests.rs:238-314]
  - Signature: `fn library_writes_all_code_facts() {`
  - Purpose: Tests that 'write_parsed_file_facts' emits the full expected write sequence for a parsed Rust file and records one file, one symbol, one stale symbol deletion, one import, and one call. [crates/gcode/src/index/indexer/tests.rs:238-314]
- `parsed_reindex_preserves_unchanged_symbol_summaries_and_clears_changed_symbols` (function) component `parsed_reindex_preserves_unchanged_symbol_summaries_and_clears_changed_symbols [function]` (`cb1ede0d-30e3-5627-8743-224b367e3577`) lines 325-396 [crates/gcode/src/index/indexer/tests.rs:325-396]
  - Signature: `fn parsed_reindex_preserves_unchanged_symbol_summaries_and_clears_changed_symbols() {`
  - Purpose: Indexed function `parsed_reindex_preserves_unchanged_symbol_summaries_and_clears_changed_symbols` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:325-396]
- `connect_summary_preservation_test_db` (function) component `connect_summary_preservation_test_db [function]` (`87c041ff-313d-5b8b-bb4d-e29c2ace6c8d`) lines 399-405 [crates/gcode/src/index/indexer/tests.rs:399-405]
  - Signature: `fn connect_summary_preservation_test_db() -> (postgres::Client, String) {`
  - Purpose: Indexed function `connect_summary_preservation_test_db` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:399-405]
- `unique_test_project_id` (function) component `unique_test_project_id [function]` (`84dd1f64-5bb5-5824-9019-da5dfea477fe`) lines 407-413 [crates/gcode/src/index/indexer/tests.rs:407-413]
  - Signature: `fn unique_test_project_id(prefix: &str) -> String {`
  - Purpose: Indexed function `unique_test_project_id` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:407-413]
- `SummaryPreservationCleanup` (class) component `SummaryPreservationCleanup [class]` (`77d099ec-1720-50d5-a7f4-d1a439102ba6`) lines 415-418 [crates/gcode/src/index/indexer/tests.rs:415-418]
  - Signature: `struct SummaryPreservationCleanup {`
  - Purpose: Indexed class `SummaryPreservationCleanup` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:415-418]
- `SummaryPreservationCleanup` (class) component `SummaryPreservationCleanup [class]` (`b7c10ebd-c6ef-5d11-a2d5-1372b9f04a33`) lines 420-426 [crates/gcode/src/index/indexer/tests.rs:420-426]
  - Signature: `impl Drop for SummaryPreservationCleanup {`
  - Purpose: Indexed class `SummaryPreservationCleanup` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:420-426]
- `SummaryPreservationCleanup.drop` (method) component `SummaryPreservationCleanup.drop [method]` (`57789680-12c3-5318-8c9c-ed63b0e3633b`) lines 421-425 [crates/gcode/src/index/indexer/tests.rs:421-425]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Indexed method `SummaryPreservationCleanup.drop` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:421-425]
- `cleanup_summary_preservation_project` (function) component `cleanup_summary_preservation_project [function]` (`b49025b8-8136-5397-9b30-34934448342f`) lines 428-459 [crates/gcode/src/index/indexer/tests.rs:428-459]
  - Signature: `fn cleanup_summary_preservation_project(`
  - Purpose: Indexed function `cleanup_summary_preservation_project` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:428-459]
- `write_postgres_parsed_file_facts` (function) component `write_postgres_parsed_file_facts [function]` (`03fbf907-efa9-5dbc-91be-9a3212521556`) lines 461-488 [crates/gcode/src/index/indexer/tests.rs:461-488]
  - Signature: `fn write_postgres_parsed_file_facts(`
  - Purpose: Indexed function `write_postgres_parsed_file_facts` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:461-488]
- `test_symbol` (function) component `test_symbol [function]` (`becd65c3-2f32-5c62-a38d-24eaed34ad41`) lines 490-517 [crates/gcode/src/index/indexer/tests.rs:490-517]
  - Signature: `fn test_symbol(`
  - Purpose: Indexed function `test_symbol` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:490-517]
- `symbol_summary` (function) component `symbol_summary [function]` (`699f9adc-4821-5420-aa6f-4ed543e7752d`) lines 519-527 [crates/gcode/src/index/indexer/tests.rs:519-527]
  - Signature: `fn symbol_summary(conn: &mut postgres::Client, symbol_id: &str) -> Option<String> {`
  - Purpose: Indexed function `symbol_summary` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:519-527]
- `symbol_count` (function) component `symbol_count [function]` (`012f264d-5fb8-5cf7-839e-9bc77ef8925a`) lines 529-539 [crates/gcode/src/index/indexer/tests.rs:529-539]
  - Signature: `fn symbol_count(conn: &mut postgres::Client, project_id: &str, rel: &str, symbol_id: &str) -> i64 {`
  - Purpose: Indexed function `symbol_count` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:529-539]
- `call_relation_contract_uses_empty_optional_storage_values` (function) component `call_relation_contract_uses_empty_optional_storage_values [function]` (`29f2ec76-fe0f-56e0-9cce-d5df71c04dd9`) lines 542-564 [crates/gcode/src/index/indexer/tests.rs:542-564]
  - Signature: `fn call_relation_contract_uses_empty_optional_storage_values() {`
  - Purpose: Indexed function `call_relation_contract_uses_empty_optional_storage_values` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:542-564]
- `explicit_file_route_sends_unsupported_text_to_content_only` (function) component `explicit_file_route_sends_unsupported_text_to_content_only [function]` (`f9c0921d-74ab-5d46-a979-209eef3c5e22`) lines 567-603 [crates/gcode/src/index/indexer/tests.rs:567-603]
  - Signature: `fn explicit_file_route_sends_unsupported_text_to_content_only() {`
  - Purpose: Indexed function `explicit_file_route_sends_unsupported_text_to_content_only` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:567-603]
- `explicit_file_routes_follow_respect_gitignore_setting` (function) component `explicit_file_routes_follow_respect_gitignore_setting [function]` (`c41bf724-242e-5152-b00e-6813dc2214cb`) lines 606-642 [crates/gcode/src/index/indexer/tests.rs:606-642]
  - Signature: `fn explicit_file_routes_follow_respect_gitignore_setting() {`
  - Purpose: Indexed function `explicit_file_routes_follow_respect_gitignore_setting` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:606-642]
- `explicit_file_route_applies_parent_gitignore_without_full_discovery` (function) component `explicit_file_route_applies_parent_gitignore_without_full_discovery [function]` (`a76fbbc7-9566-5df4-a262-5f5bf40e3bd3`) lines 645-675 [crates/gcode/src/index/indexer/tests.rs:645-675]
  - Signature: `fn explicit_file_route_applies_parent_gitignore_without_full_discovery() {`
  - Purpose: Indexed function `explicit_file_route_applies_parent_gitignore_without_full_discovery` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:645-675]
- `explicit_file_route_indexes_mjs_and_routes_markdown_to_content_only` (function) component `explicit_file_route_indexes_mjs_and_routes_markdown_to_content_only [function]` (`e3478d38-ed2e-5998-8c7d-b4c49345fa5d`) lines 678-704 [crates/gcode/src/index/indexer/tests.rs:678-704]
  - Signature: `fn explicit_file_route_indexes_mjs_and_routes_markdown_to_content_only() {`
  - Purpose: Indexed function `explicit_file_route_indexes_mjs_and_routes_markdown_to_content_only` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:678-704]
- `discovered_hidden_workflows_survive_index_path_filter` (function) component `discovered_hidden_workflows_survive_index_path_filter [function]` (`b96ef10b-f433-5ae6-b922-f34a171f4db3`) lines 707-729 [crates/gcode/src/index/indexer/tests.rs:707-729]
  - Signature: `fn discovered_hidden_workflows_survive_index_path_filter() {`
  - Purpose: Indexed function `discovered_hidden_workflows_survive_index_path_filter` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:707-729]
- `explicit_file_route_skips_generated_mjs` (function) component `explicit_file_route_skips_generated_mjs [function]` (`ebae9ab4-f5cf-52a3-9b5d-4b91b993cd84`) lines 732-747 [crates/gcode/src/index/indexer/tests.rs:732-747]
  - Signature: `fn explicit_file_route_skips_generated_mjs() {`
  - Purpose: Indexed function `explicit_file_route_skips_generated_mjs` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:732-747]
- `explicit_skip_cleanup_deletes_stale_facts_and_projections` (function) component `explicit_skip_cleanup_deletes_stale_facts_and_projections [function]` (`10b84684-b35a-55d8-baa8-eb3f75fa9b06`) lines 750-799 [crates/gcode/src/index/indexer/tests.rs:750-799]
  - Signature: `fn explicit_skip_cleanup_deletes_stale_facts_and_projections() {`
  - Purpose: Indexed function `explicit_skip_cleanup_deletes_stale_facts_and_projections` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:750-799]
- `explicit_skip_cleanup_ignores_never_indexed_files` (function) component `explicit_skip_cleanup_ignores_never_indexed_files [function]` (`b2a865aa-5da0-5c97-bcaa-2eaef5e55fc9`) lines 802-830 [crates/gcode/src/index/indexer/tests.rs:802-830]
  - Signature: `fn explicit_skip_cleanup_ignores_never_indexed_files() {`
  - Purpose: Indexed function `explicit_skip_cleanup_ignores_never_indexed_files` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:802-830]
- `overlay_reconciliation_actions_cover_inherit_shadow_add_delete` (function) component `overlay_reconciliation_actions_cover_inherit_shadow_add_delete [function]` (`b71c3bb5-a673-50df-86e1-ab79dc0b3486`) lines 833-883 [crates/gcode/src/index/indexer/tests.rs:833-883]
  - Signature: `fn overlay_reconciliation_actions_cover_inherit_shadow_add_delete() {`
  - Purpose: Indexed function `overlay_reconciliation_actions_cover_inherit_shadow_add_delete` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:833-883]
- `deleted_file_projection_cleanup_degrades_without_services` (function) component `deleted_file_projection_cleanup_degrades_without_services [function]` (`d11a636b-dde1-5ab0-8019-c2b16e41ece7`) lines 886-923 [crates/gcode/src/index/indexer/tests.rs:886-923]
  - Signature: `fn deleted_file_projection_cleanup_degrades_without_services() {`
  - Purpose: Indexed function `deleted_file_projection_cleanup_degrades_without_services` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:886-923]
- `deleted_file_projection_cleanup_skips_vectors_when_not_previously_synced` (function) component `deleted_file_projection_cleanup_skips_vectors_when_not_previously_synced [function]` (`44a9a3fb-2628-5d1f-867e-7a2fdd841c26`) lines 926-952 [crates/gcode/src/index/indexer/tests.rs:926-952]
  - Signature: `fn deleted_file_projection_cleanup_skips_vectors_when_not_previously_synced() {`
  - Purpose: Indexed function `deleted_file_projection_cleanup_skips_vectors_when_not_previously_synced` in `crates/gcode/src/index/indexer/tests.rs`. [crates/gcode/src/index/indexer/tests.rs:926-952]

