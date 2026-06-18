---
title: crates/gwiki/src/commands/refresh/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/refresh/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh/tests.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Overview

`crates/gwiki/src/commands/refresh/tests.rs` exposes 20 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/refresh/tests.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `test_scope` | function | Indexed function `test_scope` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:7-13] |
| `seed_url` | function | Indexed function `seed_url` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:15-31] |
| `seed_file_without_replay` | function | Indexed function `seed_file_without_replay` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:33-49] |
| `seed_local_file` | function | Indexed function `seed_local_file` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:51-103] |
| `seed_unsupported_connector` | function | Indexed function `seed_unsupported_connector` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:105-121] |
| `snapshot` | function | Indexed function `snapshot` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:123-131] |
| `dry_run_plans_without_fetching_or_writing` | function | Indexed function `dry_run_plans_without_fetching_or_writing` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:134-160] |
| `unchanged_content_does_not_rewrite_or_index` | function | Indexed function `unchanged_content_does_not_rewrite_or_index` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:163-185] |
| `unchanged_local_file_does_not_replay_or_index` | function | Indexed function `unchanged_local_file_does_not_replay_or_index` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:188-214] |
| `changed_content_replaces_manifest_and_removes_old_raw` | function | Indexed function `changed_content_replaces_manifest_and_removes_old_raw` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:217-250] |
| `changed_local_file_replays_and_removes_old_raw_assets` | function | Indexed function `changed_local_file_replays_and_removes_old_raw_assets` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:253-316] |
| `explicit_unsupported_and_missing_sources_fail_structurally` | function | Indexed function `explicit_unsupported_and_missing_sources_fail_structurally` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:319-342] |
| `explicit_selection_reports_malformed_raw_source_ids` | function | Indexed function `explicit_selection_reports_malformed_raw_source_ids` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:345-362] |
| `raw_source_path_trims_source_ids` | function | Indexed function `raw_source_path_trims_source_ids` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:365-370] |
| `source_asset_paths_for_id_accepts_only_single_extension_assets` | function | Indexed function `source_asset_paths_for_id_accepts_only_single_extension_assets` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:373-386] |
| `remove_relative_file_rejects_unsafe_paths_before_join` | function | Indexed function `remove_relative_file_rejects_unsafe_paths_before_join` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:389-406] |
| `remove_relative_file_normalizes_current_dir_components` | function | Indexed function `remove_relative_file_normalizes_current_dir_components` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:409-420] |
| `refresh_url_accepts_case_insensitive_http_scheme` | function | Indexed function `refresh_url_accepts_case_insensitive_http_scheme` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:423-434] |
| `invalid_http_like_locations_are_not_url_sources` | function | Indexed function `invalid_http_like_locations_are_not_url_sources` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:437-445] |
| `all_source_refresh_skips_unsupported_records` | function | Indexed function `all_source_refresh_skips_unsupported_records` in `crates/gwiki/src/commands/refresh/tests.rs`. [crates/gwiki/src/commands/refresh/tests.rs:448-464] |

