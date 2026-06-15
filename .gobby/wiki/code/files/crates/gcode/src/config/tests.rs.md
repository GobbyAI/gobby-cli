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

This file contains integration-style tests for `gcode` configuration resolution, especially how project identity, daemon URL selection, and service-specific settings are derived from on-disk config and environment variables. It also defines small test helpers for writing `.gobby/project.json`, running `git`, creating linked worktrees, and scoping service environment overrides so the tests can exercise precedence, secret resolution, error propagation, and project-identity edge cases consistently.
[crates/gcode/src/config/tests.rs:14-22]
[crates/gcode/src/config/tests.rs:24-38]
[crates/gcode/src/config/tests.rs:40-70]
[crates/gcode/src/config/tests.rs:80-90]
[crates/gcode/src/config/tests.rs:92-96]

## API Symbols

- `write_project_json` (function) component `write_project_json [function]` (`595fac55-0d4e-55e5-b2fd-69fe49196253`) lines 14-22 [crates/gcode/src/config/tests.rs:14-22]
  - Signature: `fn write_project_json(root: &Path, json: serde_json::Value) {`
  - Purpose: Creates the '.gobby' directory under 'root' if needed and writes 'json' to '.gobby/project.json' as pretty-printed JSON, panicking on any directory creation, serialization, or write failure. [crates/gcode/src/config/tests.rs:14-22]
- `run_git` (function) component `run_git [function]` (`f7f4f1d9-0ff8-51db-b7e9-3b84c3dc6657`) lines 24-38 [crates/gcode/src/config/tests.rs:24-38]
  - Signature: `fn run_git(dir: &Path, args: &[&str]) {`
  - Purpose: Runs 'git -C <dir> ...args', panicking if the command fails and including captured stdout and stderr in the assertion message. [crates/gcode/src/config/tests.rs:24-38]
- `create_linked_worktree` (function) component `create_linked_worktree [function]` (`e65d015b-ff27-55ad-991f-4d67c5588b34`) lines 40-70 [crates/gcode/src/config/tests.rs:40-70]
  - Signature: `fn create_linked_worktree(tmp: &tempfile::TempDir) -> (PathBuf, PathBuf) {`
  - Purpose: Creates a temporary Git repository with an initial 'README.md' commit, then adds a linked worktree on a new branch named 'linked-branch' and returns the paths to the primary repo and the linked worktree. [crates/gcode/src/config/tests.rs:40-70]
- `with_service_env` (function) component `with_service_env [function]` (`80b86ae0-52b6-557e-a3f7-fcd29acbffbd`) lines 80-90 [crates/gcode/src/config/tests.rs:80-90]
  - Signature: `fn with_service_env<R>(`
  - Purpose: Temporarily sets the process environment for the keys in 'SERVICE_ENV_KEYS', applies any provided '(key, value)' overrides, and runs 'closure' under those scoped variable values via 'temp_env::with_vars'. [crates/gcode/src/config/tests.rs:80-90]
- `config_value_for` (function) component `config_value_for [function]` (`99326af5-69bd-5565-bee6-cb3375d238ae`) lines 92-96 [crates/gcode/src/config/tests.rs:92-96]
  - Signature: `fn config_value_for<'a>(`
  - Purpose: Returns a closure that looks up a key in the provided 'HashMap<&str, &str>' and, if found, clones the borrowed value into an owned 'String' wrapped in 'Some', otherwise returns 'None'. [crates/gcode/src/config/tests.rs:92-96]
- `adapter_env_precedence_and_json_decode` (function) component `adapter_env_precedence_and_json_decode [function]` (`9681c9c5-f04e-5c15-8d67-f0a4b2222fcf`) lines 100-140 [crates/gcode/src/config/tests.rs:100-140]
  - Signature: `fn adapter_env_precedence_and_json_decode() {`
  - Purpose: Verifies that environment variables override stored config values while JSON-encoded stored strings are decoded correctly when resolving FalkorDB, Qdrant, and embedding configuration, including null-to-'None' handling and default timeout assignment. [crates/gcode/src/config/tests.rs:100-140]
- `project_name_lookup_suffixes_cover_unix_and_windows_paths` (function) component `project_name_lookup_suffixes_cover_unix_and_windows_paths [function]` (`76c2c53a-d210-5ce2-bcda-aef0b42e95eb`) lines 143-148 [crates/gcode/src/config/tests.rs:143-148]
  - Signature: `fn project_name_lookup_suffixes_cover_unix_and_windows_paths() {`
  - Purpose: Verifies that 'project_name_suffixes("api_%")' returns the expected Unix and Windows path suffixes, '"/api_%"' and '"\\api_%"', respectively. [crates/gcode/src/config/tests.rs:143-148]
- `daemon_url_falls_back_when_bootstrap_path_is_unavailable` (function) component `daemon_url_falls_back_when_bootstrap_path_is_unavailable [function]` (`4b1d863f-178d-5c97-bd65-0beb804d2ac0`) lines 152-166 [crates/gcode/src/config/tests.rs:152-166]
  - Signature: `fn daemon_url_falls_back_when_bootstrap_path_is_unavailable() {`
  - Purpose: Verifies that 'gobby_core::daemon_url::daemon_url()' falls back to 'http://127.0.0.1:60887' when 'GOBBY_DAEMON_URL' and 'GOBBY_PORT' are unset and 'GOBBY_HOME' points to an invalid non-directory path. [crates/gcode/src/config/tests.rs:152-166]
- `daemon_url_normalizes_wildcard_bootstrap_bind_host` (function) component `daemon_url_normalizes_wildcard_bootstrap_bind_host [function]` (`de39c51f-2749-5cc4-97e4-f187d47b7e0f`) lines 170-191 [crates/gcode/src/config/tests.rs:170-191]
  - Signature: `fn daemon_url_normalizes_wildcard_bootstrap_bind_host() {`
  - Purpose: Verifies that 'daemon_url()' normalizes a wildcard bootstrap 'bind_host: 0.0.0.0' to '127.0.0.1' and returns 'http://127.0.0.1:61234' when only 'bootstrap.yaml' provides the daemon port. [crates/gcode/src/config/tests.rs:170-191]
- `adapter_resolves_config_store_secrets` (function) component `adapter_resolves_config_store_secrets [function]` (`e96521b6-6626-5d1d-ab17-986f939c4f9e`) lines 195-229 [crates/gcode/src/config/tests.rs:195-229]
  - Signature: `fn adapter_resolves_config_store_secrets() {`
  - Purpose: Verifies that the adapter-specific config resolvers correctly replace '$secret:*' placeholders in service environment values with the corresponding resolved secret strings for FalkorDB, Qdrant, and embedding configuration fields. [crates/gcode/src/config/tests.rs:195-229]
- `resolve_secret_stub` (function) component `resolve_secret_stub [function]` (`61f1f75a-f159-5d07-8627-5cbc4cd12085`) lines 206-213 [crates/gcode/src/config/tests.rs:206-213]
  - Signature: `fn resolve_secret_stub(value: &str) -> anyhow::Result<String> {`
  - Purpose: Returns a 'String' by mapping three known secret placeholders to fixed resolved values and otherwise passing the input through unchanged. [crates/gcode/src/config/tests.rs:206-213]
- `embedding_config_source_errors_are_propagated` (function) component `embedding_config_source_errors_are_propagated [function]` (`d1cfe3e5-dc7e-5baa-a4fe-e01a042e81c5`) lines 232-242 [crates/gcode/src/config/tests.rs:232-242]
  - Signature: `fn embedding_config_source_errors_are_propagated() {`
  - Purpose: Verifies that 'resolve_embedding_config_from_fallible_values' propagates source-read failures as an error whose formatted message includes both the config-key read failure context and the underlying 'database read failed' cause. [crates/gcode/src/config/tests.rs:232-242]
- `vector_dim_setting_reads_ai_config_no_env` (function) component `vector_dim_setting_reads_ai_config_no_env [function]` (`0726e300-44c4-51cc-abca-bed13666836f`) lines 246-268 [crates/gcode/src/config/tests.rs:246-268]
  - Signature: `fn vector_dim_setting_reads_ai_config_no_env() {`
  - Purpose: Verifies that, with no service environment overrides, code vector settings are resolved from config-store 'AI_DIM' values such that '"2048"' parses to 'Some(2048)', '"null"' maps to 'None', and an invalid string like '""wide""' returns 'CodeVectorConfigError::InvalidVectorDim'. [crates/gcode/src/config/tests.rs:246-268]
- `phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name` (function) component `phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name [function]` (`3ece38b5-268b-5b8a-9823-117d1d053be8`) lines 272-295 [crates/gcode/src/config/tests.rs:272-295]
  - Signature: `fn phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name() {`
  - Purpose: Verifies that FalkorDB config resolution returns a 'gcode'-backed config with the stored host, port, and password parsed correctly, sets 'graph_name' to 'gobby_code', and propagates those fields into the derived connection config. [crates/gcode/src/config/tests.rs:272-295]
- `falkor_password_reads_password_key` (function) component `falkor_password_reads_password_key [function]` (`011a0baa-dc8d-5b8e-b0e9-cb9f4295edb3`) lines 299-313 [crates/gcode/src/config/tests.rs:299-313]
  - Signature: `fn falkor_password_reads_password_key() {`
  - Purpose: Verifies that 'resolve_falkordb_config_from_values' reads the 'databases.falkordb.password' setting from config values and populates 'falkor.password' with 'stored-pass'. [crates/gcode/src/config/tests.rs:299-313]
- `invalid_service_port_warns_and_uses_default` (function) component `invalid_service_port_warns_and_uses_default [function]` (`4df88ecd-d98f-5d27-9a58-10523f89bb89`) lines 317-333 [crates/gcode/src/config/tests.rs:317-333]
  - Signature: `fn invalid_service_port_warns_and_uses_default() {`
  - Purpose: Verifies that when 'databases.falkordb.port' is configured with an invalid value ('0' or a non-numeric string), 'resolve_falkordb_config_from_values' falls back to the default port '16379' under an empty service environment. [crates/gcode/src/config/tests.rs:317-333]
- `test_resolve_project_id_requires_project_context` (function) component `test_resolve_project_id_requires_project_context [function]` (`1e617892-a520-5f9d-9b5b-6e2cc90d5955`) lines 336-348 [crates/gcode/src/config/tests.rs:336-348]
  - Signature: `fn test_resolve_project_id_requires_project_context() {`
  - Purpose: Verifies that 'resolve_project_id' fails when called in a directory without project context and that the resulting error message includes both 'No gcode project found' and 'gcode init'. [crates/gcode/src/config/tests.rs:336-348]
- `main_repo_keeps_project_json_id` (function) component `main_repo_keeps_project_json_id [function]` (`2ac646f0-7ad2-54bd-969e-9f0be46734dc`) lines 351-367 [crates/gcode/src/config/tests.rs:351-367]
  - Signature: `fn main_repo_keeps_project_json_id() {`
  - Purpose: Creates a temporary project with a 'project.json' containing 'id: "main-project-id"' and verifies that identity resolution returns that ID from 'ProjectJson' without requesting a gcode JSON write or emitting a warning. [crates/gcode/src/config/tests.rs:351-367]
- `self_referential_parent_marker_keeps_project_json_id` (function) component `self_referential_parent_marker_keeps_project_json_id [function]` (`037d8ca9-2112-5a2a-a6d8-fc5b94b97da4`) lines 370-389 [crates/gcode/src/config/tests.rs:370-389]
  - Signature: `fn self_referential_parent_marker_keeps_project_json_id() {`
  - Purpose: Verifies that a 'project.json' whose 'parent_project_path' and 'parent_project_id' both point to the project itself is resolved as the existing 'project_id' from 'project.json', with source 'ProjectJson', no warning, and no need to write 'gcode.json'. [crates/gcode/src/config/tests.rs:370-389]
- `isolated_marker_with_parent_metadata_resolves_overlay_scope` (function) component `isolated_marker_with_parent_metadata_resolves_overlay_scope [function]` (`7510b96a-1e28-5409-89e9-379edd8b0db1`) lines 392-426 [crates/gcode/src/config/tests.rs:392-426]
  - Signature: `fn isolated_marker_with_parent_metadata_resolves_overlay_scope() {`
  - Purpose: Verifies that when a worktree has a 'project.json' pointing to a parent project, 'resolve_project_identity' classifies it as an 'IsolatedOverlay', assigns the worktree’s code-index-derived project ID, constructs an overlay 'index_scope' with canonicalized overlay and parent roots plus the parent project ID, and disables 'gcode.json' writes without emitting a warning. [crates/gcode/src/config/tests.rs:392-426]
- `isolated_marker_without_complete_parent_metadata_is_rejected` (function) component `isolated_marker_without_complete_parent_metadata_is_rejected [function]` (`af143919-a523-5668-8fd1-a757b2fa9dab`) lines 429-449 [crates/gcode/src/config/tests.rs:429-449]
  - Signature: `fn isolated_marker_without_complete_parent_metadata_is_rejected() {`
  - Purpose: Verifies that 'resolve_project_identity' rejects a '.gobby/project.json' isolation marker when 'parent_project_path' is set without 'parent_project_id', and surfaces an error mentioning invalid isolation metadata. [crates/gcode/src/config/tests.rs:429-449]
- `isolated_marker_rejects_missing_parent_path` (function) component `isolated_marker_rejects_missing_parent_path [function]` (`7077a1e9-c8c5-5aa6-b33f-5fdf2f8ffb01`) lines 452-466 [crates/gcode/src/config/tests.rs:452-466]
  - Signature: `fn isolated_marker_rejects_missing_parent_path() {`
  - Purpose: Creates a temporary project JSON with only 'parent_project_id', verifies that 'resolve_project_identity(..., MissingIdentity::Error)' fails for incomplete parent metadata, and asserts the error mentions that the fields “must be set together.” [crates/gcode/src/config/tests.rs:452-466]
- `linked_worktree_uses_path_id_and_ignores_copied_project_id` (function) component `linked_worktree_uses_path_id_and_ignores_copied_project_id [function]` (`dc387555-af78-5649-a814-00dbc63decf2`) lines 469-500 [crates/gcode/src/config/tests.rs:469-500]
  - Signature: `fn linked_worktree_uses_path_id_and_ignores_copied_project_id() {`
  - Purpose: Verifies that a linked worktree always resolves its project identity from the worktree path-based code index ID, ignoring any copied 'gcode.json' project ID, while remaining classified as 'LinkedWorktree' with no warning and no need to write 'gcode.json'. [crates/gcode/src/config/tests.rs:469-500]
- `generated_identity_writes_only_for_non_isolated_roots` (function) component `generated_identity_writes_only_for_non_isolated_roots [function]` (`e216bc71-c4fa-5991-b8b5-7b706c63c732`) lines 503-515 [crates/gcode/src/config/tests.rs:503-515]
  - Signature: `fn generated_identity_writes_only_for_non_isolated_roots() {`
  - Purpose: Verifies that resolving a project identity with 'MissingIdentity::Generate' for a non-isolated temporary root yields a 'Generated' identity, enables 'gcode.json' writing, and assigns a project ID matching 'code_index_id_for_root(tmp.path())'. [crates/gcode/src/config/tests.rs:503-515]
- `project_id_only_context_rejects_empty_id_before_runtime_resolution` (function) component `project_id_only_context_rejects_empty_id_before_runtime_resolution [function]` (`cb578de5-07c5-5f19-817c-1030bfdbb004`) lines 518-525 [crates/gcode/src/config/tests.rs:518-525]
  - Signature: `fn project_id_only_context_rejects_empty_id_before_runtime_resolution() {`
  - Purpose: Verifies that 'Context::resolve_for_project_id(" ", true)' rejects a whitespace-only project ID before any database/runtime resolution and returns an error containing '--project-id must not be empty'. [crates/gcode/src/config/tests.rs:518-525]

