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
  - 152-166
  - 170-191
  - 195-229
  - 232-242
  - 246-268
  - 272-295
  - 299-313
  - 317-333
  - 336-348
  - 351-367
  - 370-389
  - 392-426
  - 429-449
  - 452-466
  - 469-500
  - 503-515
  - 518-525
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/config/tests.rs

Module: [[code/modules/crates/gcode/src/config|crates/gcode/src/config]]

## Purpose

This file is a test suite for the gcode configuration system. It provides utility functions to set up test environments (write_project_json, run_git, create_linked_worktree, with_service_env) and manage test configuration state. The test functions validate multiple aspects of configuration resolution: environment variable precedence, JSON decoding, project ID persistence across different repository contexts (main repos, linked worktrees, isolated markers with parent metadata), daemon URL normalization and fallback behavior, service credential resolution (Falkordb, Qdrant secrets), embedding and vector configuration parsing, and error propagation through config sources. Tests also verify validation logic that rejects incomplete metadata, missing paths, and invalid service ports while applying sensible defaults.
[crates/gcode/src/config/tests.rs:14-22]
[crates/gcode/src/config/tests.rs:24-38]
[crates/gcode/src/config/tests.rs:40-70]
[crates/gcode/src/config/tests.rs:80-90]
[crates/gcode/src/config/tests.rs:92-96]

## API Symbols

- `write_project_json` (function) component `write_project_json [function]` (`595fac55-0d4e-55e5-b2fd-69fe49196253`) lines 14-22 [crates/gcode/src/config/tests.rs:14-22]
  - Signature: `fn write_project_json(root: &Path, json: serde_json::Value) {`
  - Purpose: Indexed function `write_project_json` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:14-22]
- `run_git` (function) component `run_git [function]` (`f7f4f1d9-0ff8-51db-b7e9-3b84c3dc6657`) lines 24-38 [crates/gcode/src/config/tests.rs:24-38]
  - Signature: `fn run_git(dir: &Path, args: &[&str]) {`
  - Purpose: Indexed function `run_git` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:24-38]
- `create_linked_worktree` (function) component `create_linked_worktree [function]` (`e65d015b-ff27-55ad-991f-4d67c5588b34`) lines 40-70 [crates/gcode/src/config/tests.rs:40-70]
  - Signature: `fn create_linked_worktree(tmp: &tempfile::TempDir) -> (PathBuf, PathBuf) {`
  - Purpose: Indexed function `create_linked_worktree` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:40-70]
- `with_service_env` (function) component `with_service_env [function]` (`80b86ae0-52b6-557e-a3f7-fcd29acbffbd`) lines 80-90 [crates/gcode/src/config/tests.rs:80-90]
  - Signature: `fn with_service_env<R>(`
  - Purpose: Indexed function `with_service_env` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:80-90]
- `config_value_for` (function) component `config_value_for [function]` (`99326af5-69bd-5565-bee6-cb3375d238ae`) lines 92-96 [crates/gcode/src/config/tests.rs:92-96]
  - Signature: `fn config_value_for<'a>(`
  - Purpose: Indexed function `config_value_for` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:92-96]
- `adapter_env_precedence_and_json_decode` (function) component `adapter_env_precedence_and_json_decode [function]` (`9681c9c5-f04e-5c15-8d67-f0a4b2222fcf`) lines 100-140 [crates/gcode/src/config/tests.rs:100-140]
  - Signature: `fn adapter_env_precedence_and_json_decode() {`
  - Purpose: Indexed function `adapter_env_precedence_and_json_decode` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:100-140]
- `project_name_lookup_suffixes_cover_unix_and_windows_paths` (function) component `project_name_lookup_suffixes_cover_unix_and_windows_paths [function]` (`76c2c53a-d210-5ce2-bcda-aef0b42e95eb`) lines 143-148 [crates/gcode/src/config/tests.rs:143-148]
  - Signature: `fn project_name_lookup_suffixes_cover_unix_and_windows_paths() {`
  - Purpose: Indexed function `project_name_lookup_suffixes_cover_unix_and_windows_paths` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:143-148]
- `daemon_url_falls_back_when_bootstrap_path_is_unavailable` (function) component `daemon_url_falls_back_when_bootstrap_path_is_unavailable [function]` (`4b1d863f-178d-5c97-bd65-0beb804d2ac0`) lines 152-166 [crates/gcode/src/config/tests.rs:152-166]
  - Signature: `fn daemon_url_falls_back_when_bootstrap_path_is_unavailable() {`
  - Purpose: Indexed function `daemon_url_falls_back_when_bootstrap_path_is_unavailable` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:152-166]
- `daemon_url_normalizes_wildcard_bootstrap_bind_host` (function) component `daemon_url_normalizes_wildcard_bootstrap_bind_host [function]` (`de39c51f-2749-5cc4-97e4-f187d47b7e0f`) lines 170-191 [crates/gcode/src/config/tests.rs:170-191]
  - Signature: `fn daemon_url_normalizes_wildcard_bootstrap_bind_host() {`
  - Purpose: Indexed function `daemon_url_normalizes_wildcard_bootstrap_bind_host` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:170-191]
- `adapter_resolves_config_store_secrets` (function) component `adapter_resolves_config_store_secrets [function]` (`e96521b6-6626-5d1d-ab17-986f939c4f9e`) lines 195-229 [crates/gcode/src/config/tests.rs:195-229]
  - Signature: `fn adapter_resolves_config_store_secrets() {`
  - Purpose: Indexed function `adapter_resolves_config_store_secrets` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:195-229]
- `resolve_secret_stub` (function) component `resolve_secret_stub [function]` (`61f1f75a-f159-5d07-8627-5cbc4cd12085`) lines 206-213 [crates/gcode/src/config/tests.rs:206-213]
  - Signature: `fn resolve_secret_stub(value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed function `resolve_secret_stub` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:206-213]
- `embedding_config_source_errors_are_propagated` (function) component `embedding_config_source_errors_are_propagated [function]` (`d1cfe3e5-dc7e-5baa-a4fe-e01a042e81c5`) lines 232-242 [crates/gcode/src/config/tests.rs:232-242]
  - Signature: `fn embedding_config_source_errors_are_propagated() {`
  - Purpose: Indexed function `embedding_config_source_errors_are_propagated` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:232-242]
- `vector_dim_setting_reads_ai_config_no_env` (function) component `vector_dim_setting_reads_ai_config_no_env [function]` (`0726e300-44c4-51cc-abca-bed13666836f`) lines 246-268 [crates/gcode/src/config/tests.rs:246-268]
  - Signature: `fn vector_dim_setting_reads_ai_config_no_env() {`
  - Purpose: Indexed function `vector_dim_setting_reads_ai_config_no_env` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:246-268]
- `phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name` (function) component `phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name [function]` (`3ece38b5-268b-5b8a-9823-117d1d053be8`) lines 272-295 [crates/gcode/src/config/tests.rs:272-295]
  - Signature: `fn phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name() {`
  - Purpose: Indexed function `phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:272-295]
- `falkor_password_reads_password_key` (function) component `falkor_password_reads_password_key [function]` (`011a0baa-dc8d-5b8e-b0e9-cb9f4295edb3`) lines 299-313 [crates/gcode/src/config/tests.rs:299-313]
  - Signature: `fn falkor_password_reads_password_key() {`
  - Purpose: Indexed function `falkor_password_reads_password_key` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:299-313]
- `invalid_service_port_warns_and_uses_default` (function) component `invalid_service_port_warns_and_uses_default [function]` (`4df88ecd-d98f-5d27-9a58-10523f89bb89`) lines 317-333 [crates/gcode/src/config/tests.rs:317-333]
  - Signature: `fn invalid_service_port_warns_and_uses_default() {`
  - Purpose: Indexed function `invalid_service_port_warns_and_uses_default` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:317-333]
- `test_resolve_project_id_requires_project_context` (function) component `test_resolve_project_id_requires_project_context [function]` (`1e617892-a520-5f9d-9b5b-6e2cc90d5955`) lines 336-348 [crates/gcode/src/config/tests.rs:336-348]
  - Signature: `fn test_resolve_project_id_requires_project_context() {`
  - Purpose: Indexed function `test_resolve_project_id_requires_project_context` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:336-348]
- `main_repo_keeps_project_json_id` (function) component `main_repo_keeps_project_json_id [function]` (`2ac646f0-7ad2-54bd-969e-9f0be46734dc`) lines 351-367 [crates/gcode/src/config/tests.rs:351-367]
  - Signature: `fn main_repo_keeps_project_json_id() {`
  - Purpose: Indexed function `main_repo_keeps_project_json_id` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:351-367]
- `self_referential_parent_marker_keeps_project_json_id` (function) component `self_referential_parent_marker_keeps_project_json_id [function]` (`037d8ca9-2112-5a2a-a6d8-fc5b94b97da4`) lines 370-389 [crates/gcode/src/config/tests.rs:370-389]
  - Signature: `fn self_referential_parent_marker_keeps_project_json_id() {`
  - Purpose: Indexed function `self_referential_parent_marker_keeps_project_json_id` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:370-389]
- `isolated_marker_with_parent_metadata_resolves_overlay_scope` (function) component `isolated_marker_with_parent_metadata_resolves_overlay_scope [function]` (`7510b96a-1e28-5409-89e9-379edd8b0db1`) lines 392-426 [crates/gcode/src/config/tests.rs:392-426]
  - Signature: `fn isolated_marker_with_parent_metadata_resolves_overlay_scope() {`
  - Purpose: Indexed function `isolated_marker_with_parent_metadata_resolves_overlay_scope` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:392-426]
- `isolated_marker_without_complete_parent_metadata_is_rejected` (function) component `isolated_marker_without_complete_parent_metadata_is_rejected [function]` (`af143919-a523-5668-8fd1-a757b2fa9dab`) lines 429-449 [crates/gcode/src/config/tests.rs:429-449]
  - Signature: `fn isolated_marker_without_complete_parent_metadata_is_rejected() {`
  - Purpose: Indexed function `isolated_marker_without_complete_parent_metadata_is_rejected` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:429-449]
- `isolated_marker_rejects_missing_parent_path` (function) component `isolated_marker_rejects_missing_parent_path [function]` (`7077a1e9-c8c5-5aa6-b33f-5fdf2f8ffb01`) lines 452-466 [crates/gcode/src/config/tests.rs:452-466]
  - Signature: `fn isolated_marker_rejects_missing_parent_path() {`
  - Purpose: Indexed function `isolated_marker_rejects_missing_parent_path` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:452-466]
- `linked_worktree_uses_path_id_and_ignores_copied_project_id` (function) component `linked_worktree_uses_path_id_and_ignores_copied_project_id [function]` (`dc387555-af78-5649-a814-00dbc63decf2`) lines 469-500 [crates/gcode/src/config/tests.rs:469-500]
  - Signature: `fn linked_worktree_uses_path_id_and_ignores_copied_project_id() {`
  - Purpose: Indexed function `linked_worktree_uses_path_id_and_ignores_copied_project_id` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:469-500]
- `generated_identity_writes_only_for_non_isolated_roots` (function) component `generated_identity_writes_only_for_non_isolated_roots [function]` (`e216bc71-c4fa-5991-b8b5-7b706c63c732`) lines 503-515 [crates/gcode/src/config/tests.rs:503-515]
  - Signature: `fn generated_identity_writes_only_for_non_isolated_roots() {`
  - Purpose: Indexed function `generated_identity_writes_only_for_non_isolated_roots` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:503-515]
- `project_id_only_context_rejects_empty_id_before_runtime_resolution` (function) component `project_id_only_context_rejects_empty_id_before_runtime_resolution [function]` (`cb578de5-07c5-5f19-817c-1030bfdbb004`) lines 518-525 [crates/gcode/src/config/tests.rs:518-525]
  - Signature: `fn project_id_only_context_rejects_empty_id_before_runtime_resolution() {`
  - Purpose: Indexed function `project_id_only_context_rejects_empty_id_before_runtime_resolution` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:518-525]

