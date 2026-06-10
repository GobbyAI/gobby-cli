---
title: crates/gcode/src/config/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/config/tests.rs
  ranges:
  - 14-22
  - 24-38
  - 40-70
  - 80-90
  - 92-96
  - 100-140
  - 143-148
  - 152-165
  - 169-189
  - 193-227
  - 204-211
  - 231-253
  - 257-280
  - 284-298
  - 302-318
  - 321-333
  - 336-352
  - 355-374
  - 377-411
  - 414-434
  - 437-451
  - 454-485
  - 488-500
  - 503-510
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/config/tests.rs

Module: [[code/modules/crates/gcode/src/config|crates/gcode/src/config]]

## Purpose

`crates/gcode/src/config/tests.rs` exposes 24 indexed API symbols.
[crates/gcode/src/config/tests.rs:14-22]
[crates/gcode/src/config/tests.rs:24-38]
[crates/gcode/src/config/tests.rs:40-70]
[crates/gcode/src/config/tests.rs:80-90]
[crates/gcode/src/config/tests.rs:92-96]
[crates/gcode/src/config/tests.rs:100-140]
[crates/gcode/src/config/tests.rs:143-148]
[crates/gcode/src/config/tests.rs:152-165]
[crates/gcode/src/config/tests.rs:169-189]
[crates/gcode/src/config/tests.rs:193-227]
[crates/gcode/src/config/tests.rs:204-211]
[crates/gcode/src/config/tests.rs:231-253]
[crates/gcode/src/config/tests.rs:257-280]
[crates/gcode/src/config/tests.rs:284-298]
[crates/gcode/src/config/tests.rs:302-318]
[crates/gcode/src/config/tests.rs:321-333]
[crates/gcode/src/config/tests.rs:336-352]
[crates/gcode/src/config/tests.rs:355-374]
[crates/gcode/src/config/tests.rs:377-411]
[crates/gcode/src/config/tests.rs:414-434]
[crates/gcode/src/config/tests.rs:437-451]
[crates/gcode/src/config/tests.rs:454-485]
[crates/gcode/src/config/tests.rs:488-500]
[crates/gcode/src/config/tests.rs:503-510]

## API Symbols

- `write_project_json` (function) component `write_project_json [function]` (`22d95967-4c47-5301-9893-eea888265aa6`) lines 14-22 [crates/gcode/src/config/tests.rs:14-22]
  - Signature: `fn write_project_json(root: &Path, json: serde_json::Value) {`
  - Purpose: Indexed function `write_project_json` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:14-22]
- `run_git` (function) component `run_git [function]` (`d62437bb-180d-55c1-b833-f7027755f35a`) lines 24-38 [crates/gcode/src/config/tests.rs:24-38]
  - Signature: `fn run_git(dir: &Path, args: &[&str]) {`
  - Purpose: Indexed function `run_git` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:24-38]
- `create_linked_worktree` (function) component `create_linked_worktree [function]` (`61abcfc3-fe76-5500-8838-75ac4b17f916`) lines 40-70 [crates/gcode/src/config/tests.rs:40-70]
  - Signature: `fn create_linked_worktree(tmp: &tempfile::TempDir) -> (PathBuf, PathBuf) {`
  - Purpose: Indexed function `create_linked_worktree` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:40-70]
- `with_service_env` (function) component `with_service_env [function]` (`d06b8de3-1553-5342-ba44-f1745930b5b1`) lines 80-90 [crates/gcode/src/config/tests.rs:80-90]
  - Signature: `fn with_service_env<R>(`
  - Purpose: Indexed function `with_service_env` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:80-90]
- `config_value_for` (function) component `config_value_for [function]` (`be80e8f1-1e5a-5700-b35e-39bccbfa4e08`) lines 92-96 [crates/gcode/src/config/tests.rs:92-96]
  - Signature: `fn config_value_for<'a>(`
  - Purpose: Indexed function `config_value_for` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:92-96]
- `adapter_env_precedence_and_json_decode` (function) component `adapter_env_precedence_and_json_decode [function]` (`dc2980b8-a6f8-5578-b588-1bdcabd2da5b`) lines 100-140 [crates/gcode/src/config/tests.rs:100-140]
  - Signature: `fn adapter_env_precedence_and_json_decode() {`
  - Purpose: Indexed function `adapter_env_precedence_and_json_decode` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:100-140]
- `project_name_lookup_suffixes_cover_unix_and_windows_paths` (function) component `project_name_lookup_suffixes_cover_unix_and_windows_paths [function]` (`e910f040-f10a-5e17-9d6a-b3022f74b52b`) lines 143-148 [crates/gcode/src/config/tests.rs:143-148]
  - Signature: `fn project_name_lookup_suffixes_cover_unix_and_windows_paths() {`
  - Purpose: Indexed function `project_name_lookup_suffixes_cover_unix_and_windows_paths` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:143-148]
- `daemon_url_falls_back_when_bootstrap_path_is_unavailable` (function) component `daemon_url_falls_back_when_bootstrap_path_is_unavailable [function]` (`55454640-c86e-515e-8fee-3b7189883fe8`) lines 152-165 [crates/gcode/src/config/tests.rs:152-165]
  - Signature: `fn daemon_url_falls_back_when_bootstrap_path_is_unavailable() {`
  - Purpose: Indexed function `daemon_url_falls_back_when_bootstrap_path_is_unavailable` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:152-165]
- `daemon_url_normalizes_wildcard_bootstrap_bind_host` (function) component `daemon_url_normalizes_wildcard_bootstrap_bind_host [function]` (`d1a6b3c8-8c6a-5d16-a932-537861278482`) lines 169-189 [crates/gcode/src/config/tests.rs:169-189]
  - Signature: `fn daemon_url_normalizes_wildcard_bootstrap_bind_host() {`
  - Purpose: Indexed function `daemon_url_normalizes_wildcard_bootstrap_bind_host` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:169-189]
- `adapter_resolves_config_store_secrets` (function) component `adapter_resolves_config_store_secrets [function]` (`bcd73b9b-420b-5979-8a5b-6fda2cbfcfad`) lines 193-227 [crates/gcode/src/config/tests.rs:193-227]
  - Signature: `fn adapter_resolves_config_store_secrets() {`
  - Purpose: Indexed function `adapter_resolves_config_store_secrets` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:193-227]
- `resolve_secret_stub` (function) component `resolve_secret_stub [function]` (`1c4fc141-62b4-51ce-ad6d-628f37472fc7`) lines 204-211 [crates/gcode/src/config/tests.rs:204-211]
  - Signature: `fn resolve_secret_stub(value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed function `resolve_secret_stub` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:204-211]
- `vector_dim_setting_reads_ai_config_no_env` (function) component `vector_dim_setting_reads_ai_config_no_env [function]` (`bd61a8b0-4f4a-55a4-953c-ce21de81b3e5`) lines 231-253 [crates/gcode/src/config/tests.rs:231-253]
  - Signature: `fn vector_dim_setting_reads_ai_config_no_env() {`
  - Purpose: Indexed function `vector_dim_setting_reads_ai_config_no_env` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:231-253]
- `phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name` (function) component `phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name [function]` (`ae99a563-1411-56af-9bc0-c4737941286a`) lines 257-280 [crates/gcode/src/config/tests.rs:257-280]
  - Signature: `fn phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name() {`
  - Purpose: Indexed function `phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:257-280]
- `falkor_password_reads_password_key` (function) component `falkor_password_reads_password_key [function]` (`d884867c-bea0-5618-a5d7-0b70d8daa610`) lines 284-298 [crates/gcode/src/config/tests.rs:284-298]
  - Signature: `fn falkor_password_reads_password_key() {`
  - Purpose: Indexed function `falkor_password_reads_password_key` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:284-298]
- `invalid_service_port_warns_and_uses_default` (function) component `invalid_service_port_warns_and_uses_default [function]` (`c2c00cde-b914-5ede-98c3-612ab58cfb66`) lines 302-318 [crates/gcode/src/config/tests.rs:302-318]
  - Signature: `fn invalid_service_port_warns_and_uses_default() {`
  - Purpose: Indexed function `invalid_service_port_warns_and_uses_default` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:302-318]
- `test_resolve_project_id_requires_project_context` (function) component `test_resolve_project_id_requires_project_context [function]` (`5d5f2185-07ab-5517-bc40-59eb9b6f6187`) lines 321-333 [crates/gcode/src/config/tests.rs:321-333]
  - Signature: `fn test_resolve_project_id_requires_project_context() {`
  - Purpose: Indexed function `test_resolve_project_id_requires_project_context` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:321-333]
- `main_repo_keeps_project_json_id` (function) component `main_repo_keeps_project_json_id [function]` (`745a76d2-a635-56e8-8ef1-75f60d2231f1`) lines 336-352 [crates/gcode/src/config/tests.rs:336-352]
  - Signature: `fn main_repo_keeps_project_json_id() {`
  - Purpose: Indexed function `main_repo_keeps_project_json_id` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:336-352]
- `self_referential_parent_marker_keeps_project_json_id` (function) component `self_referential_parent_marker_keeps_project_json_id [function]` (`f5aa1d4a-ce3b-5dd8-b095-a5f96261877d`) lines 355-374 [crates/gcode/src/config/tests.rs:355-374]
  - Signature: `fn self_referential_parent_marker_keeps_project_json_id() {`
  - Purpose: Indexed function `self_referential_parent_marker_keeps_project_json_id` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:355-374]
- `isolated_marker_with_parent_metadata_resolves_overlay_scope` (function) component `isolated_marker_with_parent_metadata_resolves_overlay_scope [function]` (`20f92f08-6f19-56bc-865e-304f414c4563`) lines 377-411 [crates/gcode/src/config/tests.rs:377-411]
  - Signature: `fn isolated_marker_with_parent_metadata_resolves_overlay_scope() {`
  - Purpose: Indexed function `isolated_marker_with_parent_metadata_resolves_overlay_scope` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:377-411]
- `isolated_marker_without_complete_parent_metadata_is_rejected` (function) component `isolated_marker_without_complete_parent_metadata_is_rejected [function]` (`e8a687ef-a35c-56de-9ffd-87fa42a43170`) lines 414-434 [crates/gcode/src/config/tests.rs:414-434]
  - Signature: `fn isolated_marker_without_complete_parent_metadata_is_rejected() {`
  - Purpose: Indexed function `isolated_marker_without_complete_parent_metadata_is_rejected` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:414-434]
- `isolated_marker_rejects_missing_parent_path` (function) component `isolated_marker_rejects_missing_parent_path [function]` (`b42a268f-2850-5575-9888-91d5aed30743`) lines 437-451 [crates/gcode/src/config/tests.rs:437-451]
  - Signature: `fn isolated_marker_rejects_missing_parent_path() {`
  - Purpose: Indexed function `isolated_marker_rejects_missing_parent_path` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:437-451]
- `linked_worktree_uses_path_id_and_warns_only_for_copied_project_id` (function) component `linked_worktree_uses_path_id_and_warns_only_for_copied_project_id [function]` (`96b35a60-feb6-570c-9df5-21cc1e46ceab`) lines 454-485 [crates/gcode/src/config/tests.rs:454-485]
  - Signature: `fn linked_worktree_uses_path_id_and_warns_only_for_copied_project_id() {`
  - Purpose: Indexed function `linked_worktree_uses_path_id_and_warns_only_for_copied_project_id` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:454-485]
- `generated_identity_writes_only_for_non_isolated_roots` (function) component `generated_identity_writes_only_for_non_isolated_roots [function]` (`a40c0a2e-4087-58f1-8246-0d074946d175`) lines 488-500 [crates/gcode/src/config/tests.rs:488-500]
  - Signature: `fn generated_identity_writes_only_for_non_isolated_roots() {`
  - Purpose: Indexed function `generated_identity_writes_only_for_non_isolated_roots` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:488-500]
- `project_id_only_context_rejects_empty_id_before_runtime_resolution` (function) component `project_id_only_context_rejects_empty_id_before_runtime_resolution [function]` (`b1edf567-bce7-56cd-bb8b-0ba800d056f6`) lines 503-510 [crates/gcode/src/config/tests.rs:503-510]
  - Signature: `fn project_id_only_context_rejects_empty_id_before_runtime_resolution() {`
  - Purpose: Indexed function `project_id_only_context_rejects_empty_id_before_runtime_resolution` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:503-510]

