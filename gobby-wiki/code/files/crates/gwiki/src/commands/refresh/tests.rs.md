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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/refresh/tests.rs:7-13](crates/gwiki/src/commands/refresh/tests.rs#L7-L13), [crates/gwiki/src/commands/refresh/tests.rs:15-31](crates/gwiki/src/commands/refresh/tests.rs#L15-L31), [crates/gwiki/src/commands/refresh/tests.rs:33-49](crates/gwiki/src/commands/refresh/tests.rs#L33-L49), [crates/gwiki/src/commands/refresh/tests.rs:51-103](crates/gwiki/src/commands/refresh/tests.rs#L51-L103), [crates/gwiki/src/commands/refresh/tests.rs:105-121](crates/gwiki/src/commands/refresh/tests.rs#L105-L121), [crates/gwiki/src/commands/refresh/tests.rs:123-131](crates/gwiki/src/commands/refresh/tests.rs#L123-L131), [crates/gwiki/src/commands/refresh/tests.rs:134-160](crates/gwiki/src/commands/refresh/tests.rs#L134-L160), [crates/gwiki/src/commands/refresh/tests.rs:163-185](crates/gwiki/src/commands/refresh/tests.rs#L163-L185), [crates/gwiki/src/commands/refresh/tests.rs:188-214](crates/gwiki/src/commands/refresh/tests.rs#L188-L214), [crates/gwiki/src/commands/refresh/tests.rs:217-250](crates/gwiki/src/commands/refresh/tests.rs#L217-L250), [crates/gwiki/src/commands/refresh/tests.rs:253-316](crates/gwiki/src/commands/refresh/tests.rs#L253-L316), [crates/gwiki/src/commands/refresh/tests.rs:319-342](crates/gwiki/src/commands/refresh/tests.rs#L319-L342), [crates/gwiki/src/commands/refresh/tests.rs:345-362](crates/gwiki/src/commands/refresh/tests.rs#L345-L362), [crates/gwiki/src/commands/refresh/tests.rs:365-370](crates/gwiki/src/commands/refresh/tests.rs#L365-L370), [crates/gwiki/src/commands/refresh/tests.rs:373-386](crates/gwiki/src/commands/refresh/tests.rs#L373-L386), [crates/gwiki/src/commands/refresh/tests.rs:389-406](crates/gwiki/src/commands/refresh/tests.rs#L389-L406), [crates/gwiki/src/commands/refresh/tests.rs:409-420](crates/gwiki/src/commands/refresh/tests.rs#L409-L420), [crates/gwiki/src/commands/refresh/tests.rs:423-434](crates/gwiki/src/commands/refresh/tests.rs#L423-L434), [crates/gwiki/src/commands/refresh/tests.rs:437-445](crates/gwiki/src/commands/refresh/tests.rs#L437-L445), [crates/gwiki/src/commands/refresh/tests.rs:448-464](crates/gwiki/src/commands/refresh/tests.rs#L448-L464)

</details>

# crates/gwiki/src/commands/refresh/tests.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Purpose

This file contains the test suite for the refresh command in `gwiki`. It defines small seeding helpers for building a test `ResolvedScope`, registering URL and file-backed `SourceRecord`s, and creating local replay files, then uses those fixtures to exercise refresh behavior end to end.

The tests check that dry runs only plan work, unchanged sources are not rewritten or reindexed, changed sources replace manifests and clean up old raw assets, unsupported or missing sources fail structurally, raw source IDs and asset paths are parsed and validated correctly, relative-file cleanup rejects unsafe paths but normalizes `.` segments, URL refresh accepts case-insensitive HTTP schemes, invalid HTTP-like locations are not treated as URL sources, and an all-source refresh skips unsupported records.
[crates/gwiki/src/commands/refresh/tests.rs:7-13]
[crates/gwiki/src/commands/refresh/tests.rs:15-31]
[crates/gwiki/src/commands/refresh/tests.rs:33-49]
[crates/gwiki/src/commands/refresh/tests.rs:51-103]
[crates/gwiki/src/commands/refresh/tests.rs:105-121]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `test_scope` | function | `fn test_scope(root: &Path) -> ResolvedScope {` | `test_scope [function]` | `f0c37b2c-e586-5edd-83aa-ecf554126398` | 7-13 [crates/gwiki/src/commands/refresh/tests.rs:7-13] | Indexed function `test_scope` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:7-13] |
| `seed_url` | function | `fn seed_url(root: &Path, location: &str, fetched_at: &str, body: &[u8]) -> SourceRecord {` | `seed_url [function]` | `89d5ac91-7ebb-524b-afcd-aef82ff7e4bd` | 15-31 [crates/gwiki/src/commands/refresh/tests.rs:15-31] | Indexed function `seed_url` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:15-31] |
| `seed_file_without_replay` | function | `fn seed_file_without_replay(root: &Path) -> SourceRecord {` | `seed_file_without_replay [function]` | `3ad695f4-9565-51ea-9256-24cdf83998ea` | 33-49 [crates/gwiki/src/commands/refresh/tests.rs:33-49] | Indexed function `seed_file_without_replay` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:33-49] |
| `seed_local_file` | function | `fn seed_local_file(root: &Path, relative_path: &str, body: &[u8]) -> SourceRecord {` | `seed_local_file [function]` | `84002a94-24c5-5225-8eae-3d954ae5f21f` | 51-103 [crates/gwiki/src/commands/refresh/tests.rs:51-103] | Indexed function `seed_local_file` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:51-103] |
| `seed_unsupported_connector` | function | `fn seed_unsupported_connector(root: &Path) -> SourceRecord {` | `seed_unsupported_connector [function]` | `5a5a8b89-8f80-5e29-911d-0e57b4729095` | 105-121 [crates/gwiki/src/commands/refresh/tests.rs:105-121] | Indexed function `seed_unsupported_connector` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:105-121] |
| `snapshot` | function | `fn snapshot(url: &str, body: &str) -> UrlSnapshot {` | `snapshot [function]` | `a40abd46-665f-5ed9-bf15-40147ac6ba9f` | 123-131 [crates/gwiki/src/commands/refresh/tests.rs:123-131] | Indexed function `snapshot` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:123-131] |
| `dry_run_plans_without_fetching_or_writing` | function | `fn dry_run_plans_without_fetching_or_writing() {` | `dry_run_plans_without_fetching_or_writing [function]` | `d6fb63c9-a2d7-5932-b6eb-71439d96a961` | 134-160 [crates/gwiki/src/commands/refresh/tests.rs:134-160] | Indexed function `dry_run_plans_without_fetching_or_writing` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:134-160] |
| `unchanged_content_does_not_rewrite_or_index` | function | `fn unchanged_content_does_not_rewrite_or_index() {` | `unchanged_content_does_not_rewrite_or_index [function]` | `5e442ff7-e6d7-5623-aa92-6f39de454509` | 163-185 [crates/gwiki/src/commands/refresh/tests.rs:163-185] | Indexed function `unchanged_content_does_not_rewrite_or_index` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:163-185] |
| `unchanged_local_file_does_not_replay_or_index` | function | `fn unchanged_local_file_does_not_replay_or_index() {` | `unchanged_local_file_does_not_replay_or_index [function]` | `ca67f7fa-b319-5b17-8ab5-4262fe13b736` | 188-214 [crates/gwiki/src/commands/refresh/tests.rs:188-214] | Indexed function `unchanged_local_file_does_not_replay_or_index` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:188-214] |
| `changed_content_replaces_manifest_and_removes_old_raw` | function | `fn changed_content_replaces_manifest_and_removes_old_raw() {` | `changed_content_replaces_manifest_and_removes_old_raw [function]` | `72a0b3b7-9571-5c41-a72d-81e1dcfaa1ca` | 217-250 [crates/gwiki/src/commands/refresh/tests.rs:217-250] | Indexed function `changed_content_replaces_manifest_and_removes_old_raw` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:217-250] |
| `changed_local_file_replays_and_removes_old_raw_assets` | function | `fn changed_local_file_replays_and_removes_old_raw_assets() {` | `changed_local_file_replays_and_removes_old_raw_assets [function]` | `7caa4d04-5754-51a6-b0fa-50d48cdfc3c3` | 253-316 [crates/gwiki/src/commands/refresh/tests.rs:253-316] | Indexed function `changed_local_file_replays_and_removes_old_raw_assets` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:253-316] |
| `explicit_unsupported_and_missing_sources_fail_structurally` | function | `fn explicit_unsupported_and_missing_sources_fail_structurally() {` | `explicit_unsupported_and_missing_sources_fail_structurally [function]` | `6ad1cf88-5527-56ac-8fee-0a7b0e5337da` | 319-342 [crates/gwiki/src/commands/refresh/tests.rs:319-342] | Indexed function `explicit_unsupported_and_missing_sources_fail_structurally` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:319-342] |
| `explicit_selection_reports_malformed_raw_source_ids` | function | `fn explicit_selection_reports_malformed_raw_source_ids() {` | `explicit_selection_reports_malformed_raw_source_ids [function]` | `bb82ea79-87de-595c-b6a5-29a7060493ae` | 345-362 [crates/gwiki/src/commands/refresh/tests.rs:345-362] | Indexed function `explicit_selection_reports_malformed_raw_source_ids` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:345-362] |
| `raw_source_path_trims_source_ids` | function | `fn raw_source_path_trims_source_ids() {` | `raw_source_path_trims_source_ids [function]` | `15891dbb-a94f-557e-a2a8-58e41edc447b` | 365-370 [crates/gwiki/src/commands/refresh/tests.rs:365-370] | Indexed function `raw_source_path_trims_source_ids` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:365-370] |
| `source_asset_paths_for_id_accepts_only_single_extension_assets` | function | `fn source_asset_paths_for_id_accepts_only_single_extension_assets() {` | `source_asset_paths_for_id_accepts_only_single_extension_assets [function]` | `6435efb4-6a3a-59ea-beca-f03f22b17bc9` | 373-386 [crates/gwiki/src/commands/refresh/tests.rs:373-386] | Indexed function `source_asset_paths_for_id_accepts_only_single_extension_assets` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:373-386] |
| `remove_relative_file_rejects_unsafe_paths_before_join` | function | `fn remove_relative_file_rejects_unsafe_paths_before_join() {` | `remove_relative_file_rejects_unsafe_paths_before_join [function]` | `b40cd965-6aba-5110-ae2d-a7836be41da6` | 389-406 [crates/gwiki/src/commands/refresh/tests.rs:389-406] | Indexed function `remove_relative_file_rejects_unsafe_paths_before_join` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:389-406] |
| `remove_relative_file_normalizes_current_dir_components` | function | `fn remove_relative_file_normalizes_current_dir_components() {` | `remove_relative_file_normalizes_current_dir_components [function]` | `86663790-f95c-5160-b1e0-d687141387f3` | 409-420 [crates/gwiki/src/commands/refresh/tests.rs:409-420] | Indexed function `remove_relative_file_normalizes_current_dir_components` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:409-420] |
| `refresh_url_accepts_case_insensitive_http_scheme` | function | `fn refresh_url_accepts_case_insensitive_http_scheme() {` | `refresh_url_accepts_case_insensitive_http_scheme [function]` | `ee373694-2e3b-52b7-b803-38861eb67d49` | 423-434 [crates/gwiki/src/commands/refresh/tests.rs:423-434] | Indexed function `refresh_url_accepts_case_insensitive_http_scheme` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:423-434] |
| `invalid_http_like_locations_are_not_url_sources` | function | `fn invalid_http_like_locations_are_not_url_sources() {` | `invalid_http_like_locations_are_not_url_sources [function]` | `43829ce6-08fa-5a08-997b-2a8d28afae4d` | 437-445 [crates/gwiki/src/commands/refresh/tests.rs:437-445] | Indexed function `invalid_http_like_locations_are_not_url_sources` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:437-445] |
| `all_source_refresh_skips_unsupported_records` | function | `fn all_source_refresh_skips_unsupported_records() {` | `all_source_refresh_skips_unsupported_records [function]` | `01d45770-ff0f-5b92-8aaf-0fbb9fcb8add` | 448-464 [crates/gwiki/src/commands/refresh/tests.rs:448-464] | Indexed function `all_source_refresh_skips_unsupported_records` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:448-464] |
