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

`crates/gwiki/src/commands/refresh/tests.rs` exposes 20 indexed API symbols.
[crates/gwiki/src/commands/refresh/tests.rs:7-13]
[crates/gwiki/src/commands/refresh/tests.rs:15-31]
[crates/gwiki/src/commands/refresh/tests.rs:33-49]
[crates/gwiki/src/commands/refresh/tests.rs:51-103]
[crates/gwiki/src/commands/refresh/tests.rs:105-121]

## API Symbols

- `test_scope` (function) component `test_scope [function]` (`f0c37b2c-e586-5edd-83aa-ecf554126398`) lines 7-13 [crates/gwiki/src/commands/refresh/tests.rs:7-13]
  - Signature: `fn test_scope(root: &Path) -> ResolvedScope {`
  - Purpose: Indexed function `test_scope` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:7-13]
- `seed_url` (function) component `seed_url [function]` (`89d5ac91-7ebb-524b-afcd-aef82ff7e4bd`) lines 15-31 [crates/gwiki/src/commands/refresh/tests.rs:15-31]
  - Signature: `fn seed_url(root: &Path, location: &str, fetched_at: &str, body: &[u8]) -> SourceRecord {`
  - Purpose: Indexed function `seed_url` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:15-31]
- `seed_file_without_replay` (function) component `seed_file_without_replay [function]` (`3ad695f4-9565-51ea-9256-24cdf83998ea`) lines 33-49 [crates/gwiki/src/commands/refresh/tests.rs:33-49]
  - Signature: `fn seed_file_without_replay(root: &Path) -> SourceRecord {`
  - Purpose: Indexed function `seed_file_without_replay` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:33-49]
- `seed_local_file` (function) component `seed_local_file [function]` (`84002a94-24c5-5225-8eae-3d954ae5f21f`) lines 51-103 [crates/gwiki/src/commands/refresh/tests.rs:51-103]
  - Signature: `fn seed_local_file(root: &Path, relative_path: &str, body: &[u8]) -> SourceRecord {`
  - Purpose: Indexed function `seed_local_file` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:51-103]
- `seed_unsupported_connector` (function) component `seed_unsupported_connector [function]` (`5a5a8b89-8f80-5e29-911d-0e57b4729095`) lines 105-121 [crates/gwiki/src/commands/refresh/tests.rs:105-121]
  - Signature: `fn seed_unsupported_connector(root: &Path) -> SourceRecord {`
  - Purpose: Indexed function `seed_unsupported_connector` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:105-121]
- `snapshot` (function) component `snapshot [function]` (`a40abd46-665f-5ed9-bf15-40147ac6ba9f`) lines 123-131 [crates/gwiki/src/commands/refresh/tests.rs:123-131]
  - Signature: `fn snapshot(url: &str, body: &str) -> UrlSnapshot {`
  - Purpose: Indexed function `snapshot` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:123-131]
- `dry_run_plans_without_fetching_or_writing` (function) component `dry_run_plans_without_fetching_or_writing [function]` (`d6fb63c9-a2d7-5932-b6eb-71439d96a961`) lines 134-160 [crates/gwiki/src/commands/refresh/tests.rs:134-160]
  - Signature: `fn dry_run_plans_without_fetching_or_writing() {`
  - Purpose: Indexed function `dry_run_plans_without_fetching_or_writing` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:134-160]
- `unchanged_content_does_not_rewrite_or_index` (function) component `unchanged_content_does_not_rewrite_or_index [function]` (`5e442ff7-e6d7-5623-aa92-6f39de454509`) lines 163-185 [crates/gwiki/src/commands/refresh/tests.rs:163-185]
  - Signature: `fn unchanged_content_does_not_rewrite_or_index() {`
  - Purpose: Indexed function `unchanged_content_does_not_rewrite_or_index` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:163-185]
- `unchanged_local_file_does_not_replay_or_index` (function) component `unchanged_local_file_does_not_replay_or_index [function]` (`ca67f7fa-b319-5b17-8ab5-4262fe13b736`) lines 188-214 [crates/gwiki/src/commands/refresh/tests.rs:188-214]
  - Signature: `fn unchanged_local_file_does_not_replay_or_index() {`
  - Purpose: Indexed function `unchanged_local_file_does_not_replay_or_index` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:188-214]
- `changed_content_replaces_manifest_and_removes_old_raw` (function) component `changed_content_replaces_manifest_and_removes_old_raw [function]` (`72a0b3b7-9571-5c41-a72d-81e1dcfaa1ca`) lines 217-250 [crates/gwiki/src/commands/refresh/tests.rs:217-250]
  - Signature: `fn changed_content_replaces_manifest_and_removes_old_raw() {`
  - Purpose: Indexed function `changed_content_replaces_manifest_and_removes_old_raw` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:217-250]
- `changed_local_file_replays_and_removes_old_raw_assets` (function) component `changed_local_file_replays_and_removes_old_raw_assets [function]` (`7caa4d04-5754-51a6-b0fa-50d48cdfc3c3`) lines 253-316 [crates/gwiki/src/commands/refresh/tests.rs:253-316]
  - Signature: `fn changed_local_file_replays_and_removes_old_raw_assets() {`
  - Purpose: Indexed function `changed_local_file_replays_and_removes_old_raw_assets` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:253-316]
- `explicit_unsupported_and_missing_sources_fail_structurally` (function) component `explicit_unsupported_and_missing_sources_fail_structurally [function]` (`6ad1cf88-5527-56ac-8fee-0a7b0e5337da`) lines 319-342 [crates/gwiki/src/commands/refresh/tests.rs:319-342]
  - Signature: `fn explicit_unsupported_and_missing_sources_fail_structurally() {`
  - Purpose: Indexed function `explicit_unsupported_and_missing_sources_fail_structurally` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:319-342]
- `explicit_selection_reports_malformed_raw_source_ids` (function) component `explicit_selection_reports_malformed_raw_source_ids [function]` (`bb82ea79-87de-595c-b6a5-29a7060493ae`) lines 345-362 [crates/gwiki/src/commands/refresh/tests.rs:345-362]
  - Signature: `fn explicit_selection_reports_malformed_raw_source_ids() {`
  - Purpose: Indexed function `explicit_selection_reports_malformed_raw_source_ids` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:345-362]
- `raw_source_path_trims_source_ids` (function) component `raw_source_path_trims_source_ids [function]` (`15891dbb-a94f-557e-a2a8-58e41edc447b`) lines 365-370 [crates/gwiki/src/commands/refresh/tests.rs:365-370]
  - Signature: `fn raw_source_path_trims_source_ids() {`
  - Purpose: Indexed function `raw_source_path_trims_source_ids` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:365-370]
- `source_asset_paths_for_id_accepts_only_single_extension_assets` (function) component `source_asset_paths_for_id_accepts_only_single_extension_assets [function]` (`6435efb4-6a3a-59ea-beca-f03f22b17bc9`) lines 373-386 [crates/gwiki/src/commands/refresh/tests.rs:373-386]
  - Signature: `fn source_asset_paths_for_id_accepts_only_single_extension_assets() {`
  - Purpose: Indexed function `source_asset_paths_for_id_accepts_only_single_extension_assets` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:373-386]
- `remove_relative_file_rejects_unsafe_paths_before_join` (function) component `remove_relative_file_rejects_unsafe_paths_before_join [function]` (`b40cd965-6aba-5110-ae2d-a7836be41da6`) lines 389-406 [crates/gwiki/src/commands/refresh/tests.rs:389-406]
  - Signature: `fn remove_relative_file_rejects_unsafe_paths_before_join() {`
  - Purpose: Indexed function `remove_relative_file_rejects_unsafe_paths_before_join` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:389-406]
- `remove_relative_file_normalizes_current_dir_components` (function) component `remove_relative_file_normalizes_current_dir_components [function]` (`86663790-f95c-5160-b1e0-d687141387f3`) lines 409-420 [crates/gwiki/src/commands/refresh/tests.rs:409-420]
  - Signature: `fn remove_relative_file_normalizes_current_dir_components() {`
  - Purpose: Indexed function `remove_relative_file_normalizes_current_dir_components` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:409-420]
- `refresh_url_accepts_case_insensitive_http_scheme` (function) component `refresh_url_accepts_case_insensitive_http_scheme [function]` (`ee373694-2e3b-52b7-b803-38861eb67d49`) lines 423-434 [crates/gwiki/src/commands/refresh/tests.rs:423-434]
  - Signature: `fn refresh_url_accepts_case_insensitive_http_scheme() {`
  - Purpose: Indexed function `refresh_url_accepts_case_insensitive_http_scheme` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:423-434]
- `invalid_http_like_locations_are_not_url_sources` (function) component `invalid_http_like_locations_are_not_url_sources [function]` (`43829ce6-08fa-5a08-997b-2a8d28afae4d`) lines 437-445 [crates/gwiki/src/commands/refresh/tests.rs:437-445]
  - Signature: `fn invalid_http_like_locations_are_not_url_sources() {`
  - Purpose: Indexed function `invalid_http_like_locations_are_not_url_sources` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:437-445]
- `all_source_refresh_skips_unsupported_records` (function) component `all_source_refresh_skips_unsupported_records [function]` (`01d45770-ff0f-5b92-8aaf-0fbb9fcb8add`) lines 448-464 [crates/gwiki/src/commands/refresh/tests.rs:448-464]
  - Signature: `fn all_source_refresh_skips_unsupported_records() {`
  - Purpose: Indexed function `all_source_refresh_skips_unsupported_records` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:448-464]

