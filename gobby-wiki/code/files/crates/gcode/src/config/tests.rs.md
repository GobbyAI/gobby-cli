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
  - 518-529
  - 532-539
  - 542-553
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/config/tests.rs:14-22](crates/gcode/src/config/tests.rs#L14-L22), [crates/gcode/src/config/tests.rs:24-38](crates/gcode/src/config/tests.rs#L24-L38), [crates/gcode/src/config/tests.rs:40-70](crates/gcode/src/config/tests.rs#L40-L70), [crates/gcode/src/config/tests.rs:80-90](crates/gcode/src/config/tests.rs#L80-L90), [crates/gcode/src/config/tests.rs:92-96](crates/gcode/src/config/tests.rs#L92-L96), [crates/gcode/src/config/tests.rs:100-140](crates/gcode/src/config/tests.rs#L100-L140), [crates/gcode/src/config/tests.rs:143-148](crates/gcode/src/config/tests.rs#L143-L148), [crates/gcode/src/config/tests.rs:152-166](crates/gcode/src/config/tests.rs#L152-L166), [crates/gcode/src/config/tests.rs:170-191](crates/gcode/src/config/tests.rs#L170-L191), [crates/gcode/src/config/tests.rs:195-229](crates/gcode/src/config/tests.rs#L195-L229), [crates/gcode/src/config/tests.rs:232-242](crates/gcode/src/config/tests.rs#L232-L242), [crates/gcode/src/config/tests.rs:246-268](crates/gcode/src/config/tests.rs#L246-L268), [crates/gcode/src/config/tests.rs:272-295](crates/gcode/src/config/tests.rs#L272-L295), [crates/gcode/src/config/tests.rs:299-313](crates/gcode/src/config/tests.rs#L299-L313), [crates/gcode/src/config/tests.rs:317-333](crates/gcode/src/config/tests.rs#L317-L333), [crates/gcode/src/config/tests.rs:336-348](crates/gcode/src/config/tests.rs#L336-L348), [crates/gcode/src/config/tests.rs:351-367](crates/gcode/src/config/tests.rs#L351-L367), [crates/gcode/src/config/tests.rs:370-389](crates/gcode/src/config/tests.rs#L370-L389), [crates/gcode/src/config/tests.rs:392-426](crates/gcode/src/config/tests.rs#L392-L426), [crates/gcode/src/config/tests.rs:429-449](crates/gcode/src/config/tests.rs#L429-L449), [crates/gcode/src/config/tests.rs:452-466](crates/gcode/src/config/tests.rs#L452-L466), [crates/gcode/src/config/tests.rs:469-500](crates/gcode/src/config/tests.rs#L469-L500), [crates/gcode/src/config/tests.rs:503-515](crates/gcode/src/config/tests.rs#L503-L515), [crates/gcode/src/config/tests.rs:518-529](crates/gcode/src/config/tests.rs#L518-L529), [crates/gcode/src/config/tests.rs:532-539](crates/gcode/src/config/tests.rs#L532-L539), [crates/gcode/src/config/tests.rs:542-553](crates/gcode/src/config/tests.rs#L542-L553)

</details>

# crates/gcode/src/config/tests.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Test module for `gcode` config resolution. It defines small fixtures for writing `.gobby/project.json`, running git, creating linked worktrees, and temporarily overriding service env vars, then uses them to verify config behavior across adapter/env precedence, project-name and project-id resolution, daemon URL derivation, secret and embedding config handling, service-specific settings for FalkorDB and Qdrant, invalid port fallback, and a range of project identity cases for main repos, isolated markers, linked worktrees, and empty IDs.
[crates/gcode/src/config/tests.rs:14-22]
[crates/gcode/src/config/tests.rs:24-38]
[crates/gcode/src/config/tests.rs:40-70]
[crates/gcode/src/config/tests.rs:80-90]
[crates/gcode/src/config/tests.rs:92-96]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `write_project_json` | function | `fn write_project_json(root: &Path, json: serde_json::Value) {` | `write_project_json [function]` | `595fac55-0d4e-55e5-b2fd-69fe49196253` | 14-22 [crates/gcode/src/config/tests.rs:14-22] | Indexed function `write_project_json` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:14-22] |
| `run_git` | function | `fn run_git(dir: &Path, args: &[&str]) {` | `run_git [function]` | `f7f4f1d9-0ff8-51db-b7e9-3b84c3dc6657` | 24-38 [crates/gcode/src/config/tests.rs:24-38] | Indexed function `run_git` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:24-38] |
| `create_linked_worktree` | function | `fn create_linked_worktree(tmp: &tempfile::TempDir) -> (PathBuf, PathBuf) {` | `create_linked_worktree [function]` | `e65d015b-ff27-55ad-991f-4d67c5588b34` | 40-70 [crates/gcode/src/config/tests.rs:40-70] | Indexed function `create_linked_worktree` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:40-70] |
| `with_service_env` | function | `fn with_service_env<R>(` | `with_service_env [function]` | `80b86ae0-52b6-557e-a3f7-fcd29acbffbd` | 80-90 [crates/gcode/src/config/tests.rs:80-90] | Indexed function `with_service_env` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:80-90] |
| `config_value_for` | function | `fn config_value_for<'a>(` | `config_value_for [function]` | `99326af5-69bd-5565-bee6-cb3375d238ae` | 92-96 [crates/gcode/src/config/tests.rs:92-96] | Indexed function `config_value_for` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:92-96] |
| `adapter_env_precedence_and_json_decode` | function | `fn adapter_env_precedence_and_json_decode() {` | `adapter_env_precedence_and_json_decode [function]` | `9681c9c5-f04e-5c15-8d67-f0a4b2222fcf` | 100-140 [crates/gcode/src/config/tests.rs:100-140] | Indexed function `adapter_env_precedence_and_json_decode` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:100-140] |
| `project_name_lookup_suffixes_cover_unix_and_windows_paths` | function | `fn project_name_lookup_suffixes_cover_unix_and_windows_paths() {` | `project_name_lookup_suffixes_cover_unix_and_windows_paths [function]` | `76c2c53a-d210-5ce2-bcda-aef0b42e95eb` | 143-148 [crates/gcode/src/config/tests.rs:143-148] | Indexed function `project_name_lookup_suffixes_cover_unix_and_windows_paths` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:143-148] |
| `daemon_url_falls_back_when_bootstrap_path_is_unavailable` | function | `fn daemon_url_falls_back_when_bootstrap_path_is_unavailable() {` | `daemon_url_falls_back_when_bootstrap_path_is_unavailable [function]` | `4b1d863f-178d-5c97-bd65-0beb804d2ac0` | 152-166 [crates/gcode/src/config/tests.rs:152-166] | Indexed function `daemon_url_falls_back_when_bootstrap_path_is_unavailable` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:152-166] |
| `daemon_url_normalizes_wildcard_bootstrap_bind_host` | function | `fn daemon_url_normalizes_wildcard_bootstrap_bind_host() {` | `daemon_url_normalizes_wildcard_bootstrap_bind_host [function]` | `de39c51f-2749-5cc4-97e4-f187d47b7e0f` | 170-191 [crates/gcode/src/config/tests.rs:170-191] | Indexed function `daemon_url_normalizes_wildcard_bootstrap_bind_host` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:170-191] |
| `adapter_resolves_config_store_secrets` | function | `fn adapter_resolves_config_store_secrets() {` | `adapter_resolves_config_store_secrets [function]` | `e96521b6-6626-5d1d-ab17-986f939c4f9e` | 195-229 [crates/gcode/src/config/tests.rs:195-229] | Indexed function `adapter_resolves_config_store_secrets` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:195-229] |
| `resolve_secret_stub` | function | `fn resolve_secret_stub(value: &str) -> anyhow::Result<String> {` | `resolve_secret_stub [function]` | `61f1f75a-f159-5d07-8627-5cbc4cd12085` | 206-213 [crates/gcode/src/config/tests.rs:206-213] | Indexed function `resolve_secret_stub` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:206-213] |
| `embedding_config_source_errors_are_propagated` | function | `fn embedding_config_source_errors_are_propagated() {` | `embedding_config_source_errors_are_propagated [function]` | `d1cfe3e5-dc7e-5baa-a4fe-e01a042e81c5` | 232-242 [crates/gcode/src/config/tests.rs:232-242] | Indexed function `embedding_config_source_errors_are_propagated` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:232-242] |
| `vector_dim_setting_reads_ai_config_no_env` | function | `fn vector_dim_setting_reads_ai_config_no_env() {` | `vector_dim_setting_reads_ai_config_no_env [function]` | `0726e300-44c4-51cc-abca-bed13666836f` | 246-268 [crates/gcode/src/config/tests.rs:246-268] | Indexed function `vector_dim_setting_reads_ai_config_no_env` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:246-268] |
| `phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name` | function | `fn phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name() {` | `phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name [function]` | `3ece38b5-268b-5b8a-9823-117d1d053be8` | 272-295 [crates/gcode/src/config/tests.rs:272-295] | Indexed function `phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:272-295] |
| `falkor_password_reads_password_key` | function | `fn falkor_password_reads_password_key() {` | `falkor_password_reads_password_key [function]` | `011a0baa-dc8d-5b8e-b0e9-cb9f4295edb3` | 299-313 [crates/gcode/src/config/tests.rs:299-313] | Indexed function `falkor_password_reads_password_key` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:299-313] |
| `invalid_service_port_warns_and_uses_default` | function | `fn invalid_service_port_warns_and_uses_default() {` | `invalid_service_port_warns_and_uses_default [function]` | `4df88ecd-d98f-5d27-9a58-10523f89bb89` | 317-333 [crates/gcode/src/config/tests.rs:317-333] | Indexed function `invalid_service_port_warns_and_uses_default` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:317-333] |
| `test_resolve_project_id_requires_project_context` | function | `fn test_resolve_project_id_requires_project_context() {` | `test_resolve_project_id_requires_project_context [function]` | `1e617892-a520-5f9d-9b5b-6e2cc90d5955` | 336-348 [crates/gcode/src/config/tests.rs:336-348] | Indexed function `test_resolve_project_id_requires_project_context` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:336-348] |
| `main_repo_keeps_project_json_id` | function | `fn main_repo_keeps_project_json_id() {` | `main_repo_keeps_project_json_id [function]` | `2ac646f0-7ad2-54bd-969e-9f0be46734dc` | 351-367 [crates/gcode/src/config/tests.rs:351-367] | Indexed function `main_repo_keeps_project_json_id` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:351-367] |
| `self_referential_parent_marker_keeps_project_json_id` | function | `fn self_referential_parent_marker_keeps_project_json_id() {` | `self_referential_parent_marker_keeps_project_json_id [function]` | `037d8ca9-2112-5a2a-a6d8-fc5b94b97da4` | 370-389 [crates/gcode/src/config/tests.rs:370-389] | Indexed function `self_referential_parent_marker_keeps_project_json_id` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:370-389] |
| `isolated_marker_with_parent_metadata_resolves_overlay_scope` | function | `fn isolated_marker_with_parent_metadata_resolves_overlay_scope() {` | `isolated_marker_with_parent_metadata_resolves_overlay_scope [function]` | `7510b96a-1e28-5409-89e9-379edd8b0db1` | 392-426 [crates/gcode/src/config/tests.rs:392-426] | Indexed function `isolated_marker_with_parent_metadata_resolves_overlay_scope` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:392-426] |
| `isolated_marker_without_complete_parent_metadata_is_rejected` | function | `fn isolated_marker_without_complete_parent_metadata_is_rejected() {` | `isolated_marker_without_complete_parent_metadata_is_rejected [function]` | `af143919-a523-5668-8fd1-a757b2fa9dab` | 429-449 [crates/gcode/src/config/tests.rs:429-449] | Indexed function `isolated_marker_without_complete_parent_metadata_is_rejected` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:429-449] |
| `isolated_marker_rejects_missing_parent_path` | function | `fn isolated_marker_rejects_missing_parent_path() {` | `isolated_marker_rejects_missing_parent_path [function]` | `7077a1e9-c8c5-5aa6-b33f-5fdf2f8ffb01` | 452-466 [crates/gcode/src/config/tests.rs:452-466] | Indexed function `isolated_marker_rejects_missing_parent_path` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:452-466] |
| `linked_worktree_uses_path_id_and_ignores_copied_project_id` | function | `fn linked_worktree_uses_path_id_and_ignores_copied_project_id() {` | `linked_worktree_uses_path_id_and_ignores_copied_project_id [function]` | `dc387555-af78-5649-a814-00dbc63decf2` | 469-500 [crates/gcode/src/config/tests.rs:469-500] | Indexed function `linked_worktree_uses_path_id_and_ignores_copied_project_id` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:469-500] |
| `generated_identity_writes_only_for_non_isolated_roots` | function | `fn generated_identity_writes_only_for_non_isolated_roots() {` | `generated_identity_writes_only_for_non_isolated_roots [function]` | `e216bc71-c4fa-5991-b8b5-7b706c63c732` | 503-515 [crates/gcode/src/config/tests.rs:503-515] | Indexed function `generated_identity_writes_only_for_non_isolated_roots` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:503-515] |
| `project_id_only_context_rejects_empty_id_before_runtime_resolution` | function | `fn project_id_only_context_rejects_empty_id_before_runtime_resolution() {` | `project_id_only_context_rejects_empty_id_before_runtime_resolution [function]` | `cb578de5-07c5-5f19-817c-1030bfdbb004` | 518-529 [crates/gcode/src/config/tests.rs:518-529] | Indexed function `project_id_only_context_rejects_empty_id_before_runtime_resolution` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:518-529] |
| `project_id_projection_cleanup_selection_includes_qdrant_without_embeddings` | function | `fn project_id_projection_cleanup_selection_includes_qdrant_without_embeddings() {` | `project_id_projection_cleanup_selection_includes_qdrant_without_embeddings [function]` | `8232a947-be72-558b-90b5-50239e68e7cd` | 532-539 [crates/gcode/src/config/tests.rs:532-539] | Indexed function `project_id_projection_cleanup_selection_includes_qdrant_without_embeddings` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:532-539] |
| `project_id_context_with_services_rejects_empty_id_before_runtime_resolution` | function | `fn project_id_context_with_services_rejects_empty_id_before_runtime_resolution() {` | `project_id_context_with_services_rejects_empty_id_before_runtime_resolution [function]` | `ca3dbc67-f876-5738-a3c6-e21d730d6c3d` | 542-553 [crates/gcode/src/config/tests.rs:542-553] | Indexed function `project_id_context_with_services_rejects_empty_id_before_runtime_resolution` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:542-553] |
