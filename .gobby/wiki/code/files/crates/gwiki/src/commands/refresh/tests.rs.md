---
title: crates/gwiki/src/commands/refresh/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/refresh/tests.rs
  ranges:
  - 7-13
  - 15-31
  - 33-49
  - 51-103
  - 105-121
  - 123-131
  - 134-160
  - 163-185
  - 188-214
  - 217-250
  - 253-316
  - 319-342
  - 345-362
  - 365-370
  - 373-386
  - 389-406
  - 409-420
  - 423-434
  - 437-445
  - 448-464
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh/tests.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Purpose

Test module for the refresh command. It defines small seeding helpers for building a `ResolvedScope`, registering URL/file source records, and constructing snapshots, then uses them to exercise refresh behavior across dry runs, unchanged and changed content, local-file replay, unsupported or missing sources, source-id/path validation, URL scheme handling, and full-source refresh skipping unsupported records.
[crates/gwiki/src/commands/refresh/tests.rs:7-13]
[crates/gwiki/src/commands/refresh/tests.rs:15-31]
[crates/gwiki/src/commands/refresh/tests.rs:33-49]
[crates/gwiki/src/commands/refresh/tests.rs:51-103]
[crates/gwiki/src/commands/refresh/tests.rs:105-121]

## API Symbols

- `test_scope` (function) component `test_scope [function]` (`f0c37b2c-e586-5edd-83aa-ecf554126398`) lines 7-13 [crates/gwiki/src/commands/refresh/tests.rs:7-13]
  - Signature: `fn test_scope(root: &Path) -> ResolvedScope {`
  - Purpose: Constructs and returns a 'ResolvedScope' for the '"refresh-test"' topic using the provided 'root' path, with the root directory as the scope base and 'root/registry.toml' as the registry file. [crates/gwiki/src/commands/refresh/tests.rs:7-13]
- `seed_url` (function) component `seed_url [function]` (`89d5ac91-7ebb-524b-afcd-aef82ff7e4bd`) lines 15-31 [crates/gwiki/src/commands/refresh/tests.rs:15-31]
  - Signature: `fn seed_url(root: &Path, location: &str, fetched_at: &str, body: &[u8]) -> SourceRecord {`
  - Purpose: Registers a new 'SourceRecord' in 'SourceManifest' for the given URL by constructing a 'SourceDraft' with the provided location, fetched timestamp, and body bytes, fixed title '"Example"', manual ingestion, pending compile status, and then panicking if registration fails. [crates/gwiki/src/commands/refresh/tests.rs:15-31]
- `seed_file_without_replay` (function) component `seed_file_without_replay [function]` (`3ad695f4-9565-51ea-9256-24cdf83998ea`) lines 33-49 [crates/gwiki/src/commands/refresh/tests.rs:33-49]
  - Signature: `fn seed_file_without_replay(root: &Path) -> SourceRecord {`
  - Purpose: Registers a new file source at '"/tmp/source.txt"' in the given 'root' via 'SourceManifest::register' using fixed metadata and content, then unwraps the result with 'expect("register source")' to return a 'SourceRecord'. [crates/gwiki/src/commands/refresh/tests.rs:33-49]
- `seed_local_file` (function) component `seed_local_file [function]` (`84002a94-24c5-5225-8eae-3d954ae5f21f`) lines 51-103 [crates/gwiki/src/commands/refresh/tests.rs:51-103]
  - Signature: `fn seed_local_file(root: &Path, relative_path: &str, body: &[u8]) -> SourceRecord {`
  - Purpose: Creates a local file under 'root', registers it as a manual pending source record in the manifest with a kind inferred from its extension, attaches local-file replay metadata, and returns the updated manifest entry. [crates/gwiki/src/commands/refresh/tests.rs:51-103]
- `seed_unsupported_connector` (function) component `seed_unsupported_connector [function]` (`5a5a8b89-8f80-5e29-911d-0e57b4729095`) lines 105-121 [crates/gwiki/src/commands/refresh/tests.rs:105-121]
  - Signature: `fn seed_unsupported_connector(root: &Path) -> SourceRecord {`
  - Purpose: Registers a 'SourceDraft' for a manually ingested stdin-backed source with pending compile status in 'SourceManifest' at the given root, then unwraps the resulting 'SourceRecord' with an 'expect' if registration fails. [crates/gwiki/src/commands/refresh/tests.rs:105-121]
- `snapshot` (function) component `snapshot [function]` (`a40abd46-665f-5ed9-bf15-40147ac6ba9f`) lines 123-131 [crates/gwiki/src/commands/refresh/tests.rs:123-131]
  - Signature: `fn snapshot(url: &str, body: &str) -> UrlSnapshot {`
  - Purpose: Creates a 'UrlSnapshot' by copying the input URL into both 'requested_url' and 'final_url', stamping a fixed 'fetched_at' timestamp, storing the body as raw bytes, and setting 'content_type' to 'Some("text/html")'. [crates/gwiki/src/commands/refresh/tests.rs:123-131]
- `dry_run_plans_without_fetching_or_writing` (function) component `dry_run_plans_without_fetching_or_writing [function]` (`d6fb63c9-a2d7-5932-b6eb-71439d96a961`) lines 134-160 [crates/gwiki/src/commands/refresh/tests.rs:134-160]
  - Signature: `fn dry_run_plans_without_fetching_or_writing() {`
  - Purpose: Verifies that a dry-run refresh plan marks the result as '"dry_run"', includes the target record in the planned output, does not invoke the fetcher, and leaves the source manifest unchanged. [crates/gwiki/src/commands/refresh/tests.rs:134-160]
- `unchanged_content_does_not_rewrite_or_index` (function) component `unchanged_content_does_not_rewrite_or_index [function]` (`5e442ff7-e6d7-5623-aa92-6f39de454509`) lines 163-185 [crates/gwiki/src/commands/refresh/tests.rs:163-185]
  - Signature: `fn unchanged_content_does_not_rewrite_or_index() {`
  - Purpose: Verifies that when a fetched snapshot is byte-for-byte identical to the existing record, the refresh reports 'unchanged', preserves the record ID, skips indexing with 'index_status.status == "not_run"', and leaves the source manifest entry count unchanged. [crates/gwiki/src/commands/refresh/tests.rs:163-185]
- `unchanged_local_file_does_not_replay_or_index` (function) component `unchanged_local_file_does_not_replay_or_index [function]` (`ca67f7fa-b319-5b17-8ab5-4262fe13b736`) lines 188-214 [crates/gwiki/src/commands/refresh/tests.rs:188-214]
  - Signature: `fn unchanged_local_file_does_not_replay_or_index() {`
  - Purpose: Verifies that refreshing an unchanged seeded local file returns 'status: "unchanged"' with 'replay_kind: "local_file"', does not run indexing, and leaves the source manifest with exactly one entry. [crates/gwiki/src/commands/refresh/tests.rs:188-214]
- `changed_content_replaces_manifest_and_removes_old_raw` (function) component `changed_content_replaces_manifest_and_removes_old_raw [function]` (`72a0b3b7-9571-5c41-a72d-81e1dcfaa1ca`) lines 217-250 [crates/gwiki/src/commands/refresh/tests.rs:217-250]
  - Signature: `fn changed_content_replaces_manifest_and_removes_old_raw() {`
  - Purpose: Verifies that refreshing a record with changed fetched content generates a new source ID, deletes the old raw content file, and updates the manifest to contain only the new entry. [crates/gwiki/src/commands/refresh/tests.rs:217-250]
- `changed_local_file_replays_and_removes_old_raw_assets` (function) component `changed_local_file_replays_and_removes_old_raw_assets [function]` (`7caa4d04-5754-51a6-b0fa-50d48cdfc3c3`) lines 253-316 [crates/gwiki/src/commands/refresh/tests.rs:253-316]
  - Signature: `fn changed_local_file_replays_and_removes_old_raw_assets() {`
  - Purpose: This test validates that modifying a locally-stored file source triggers a replay operation generating a new identifier, while removing the obsolete raw source and asset files and creating new ones with the updated ID before reindexing. [crates/gwiki/src/commands/refresh/tests.rs:253-316]
- `explicit_unsupported_and_missing_sources_fail_structurally` (function) component `explicit_unsupported_and_missing_sources_fail_structurally [function]` (`6ad1cf88-5527-56ac-8fee-0a7b0e5337da`) lines 319-342 [crates/gwiki/src/commands/refresh/tests.rs:319-342]
  - Signature: `fn explicit_unsupported_and_missing_sources_fail_structurally() {`
  - Purpose: Verifies that refreshing a resolved set containing one source lacking replay metadata and one nonexistent source fails with exit code '1' and a structured payload whose 'failed' array contains exactly 'missing_replay_metadata' followed by 'not_found'. [crates/gwiki/src/commands/refresh/tests.rs:319-342]
- `explicit_selection_reports_malformed_raw_source_ids` (function) component `explicit_selection_reports_malformed_raw_source_ids [function]` (`bb82ea79-87de-595c-b6a5-29a7060493ae`) lines 345-362 [crates/gwiki/src/commands/refresh/tests.rs:345-362]
  - Signature: `fn explicit_selection_reports_malformed_raw_source_ids() {`
  - Purpose: Verifies that 'select_sources' rejects an explicitly requested source ID containing path-traversal characters, returns no planned selections, and records a single 'invalid_source_id' failure whose message mentions an unsafe source id. [crates/gwiki/src/commands/refresh/tests.rs:345-362]
- `raw_source_path_trims_source_ids` (function) component `raw_source_path_trims_source_ids [function]` (`15891dbb-a94f-557e-a2a8-58e41edc447b`) lines 365-370 [crates/gwiki/src/commands/refresh/tests.rs:365-370]
  - Signature: `fn raw_source_path_trims_source_ids() {`
  - Purpose: Verifies that 'raw_source_path' trims surrounding whitespace from a source ID string and maps '" src-abc "' to 'raw/src-abc.md'. [crates/gwiki/src/commands/refresh/tests.rs:365-370]
- `source_asset_paths_for_id_accepts_only_single_extension_assets` (function) component `source_asset_paths_for_id_accepts_only_single_extension_assets [function]` (`6435efb4-6a3a-59ea-beca-f03f22b17bc9`) lines 373-386 [crates/gwiki/src/commands/refresh/tests.rs:373-386]
  - Signature: `fn source_asset_paths_for_id_accepts_only_single_extension_assets() {`
  - Purpose: Verifies that 'source_asset_paths_for_id' returns only the exact single-extension asset path for a given source ID, excluding derived multi-extension files, other IDs, and empty-extension names. [crates/gwiki/src/commands/refresh/tests.rs:373-386]
- `remove_relative_file_rejects_unsafe_paths_before_join` (function) component `remove_relative_file_rejects_unsafe_paths_before_join [function]` (`b40cd965-6aba-5110-ae2d-a7836be41da6`) lines 389-406 [crates/gwiki/src/commands/refresh/tests.rs:389-406]
  - Signature: `fn remove_relative_file_rejects_unsafe_paths_before_join() {`
  - Purpose: Verifies that 'remove_relative_file' rejects empty, current-directory, parent-directory traversal, and absolute paths by returning 'WikiError::InvalidInput' before attempting to join them to the base directory. [crates/gwiki/src/commands/refresh/tests.rs:389-406]
- `remove_relative_file_normalizes_current_dir_components` (function) component `remove_relative_file_normalizes_current_dir_components [function]` (`86663790-f95c-5160-b1e0-d687141387f3`) lines 409-420 [crates/gwiki/src/commands/refresh/tests.rs:409-420]
  - Signature: `fn remove_relative_file_normalizes_current_dir_components() {`
  - Purpose: Verifies that 'remove_relative_file' correctly normalizes '.' path components in a relative file path, removes the resolved file under the given root directory, and reports success. [crates/gwiki/src/commands/refresh/tests.rs:409-420]
- `refresh_url_accepts_case_insensitive_http_scheme` (function) component `refresh_url_accepts_case_insensitive_http_scheme [function]` (`ee373694-2e3b-52b7-b803-38861eb67d49`) lines 423-434 [crates/gwiki/src/commands/refresh/tests.rs:423-434]
  - Signature: `fn refresh_url_accepts_case_insensitive_http_scheme() {`
  - Purpose: Verifies that 'refresh_url' preserves and returns an 'HTTPS://' URL with an uppercase HTTP scheme unchanged, demonstrating case-insensitive handling of the scheme when refreshing a URL. [crates/gwiki/src/commands/refresh/tests.rs:423-434]
- `invalid_http_like_locations_are_not_url_sources` (function) component `invalid_http_like_locations_are_not_url_sources [function]` (`43829ce6-08fa-5a08-997b-2a8d28afae4d`) lines 437-445 [crates/gwiki/src/commands/refresh/tests.rs:437-445]
  - Signature: `fn invalid_http_like_locations_are_not_url_sources() {`
  - Purpose: Verifies that a record seeded with an HTTP-like but invalid location ('"https://"') is classified by 'replay_kind' as 'Err(SelectionFailure::UnsupportedSourceKind)'. [crates/gwiki/src/commands/refresh/tests.rs:437-445]
- `all_source_refresh_skips_unsupported_records` (function) component `all_source_refresh_skips_unsupported_records [function]` (`01d45770-ff0f-5b92-8aaf-0fbb9fcb8add`) lines 448-464 [crates/gwiki/src/commands/refresh/tests.rs:448-464]
  - Signature: `fn all_source_refresh_skips_unsupported_records() {`
  - Purpose: Verifies that a full-source refresh leaves supported records unchanged while placing unsupported connector records in the 'skipped' list. [crates/gwiki/src/commands/refresh/tests.rs:448-464]

