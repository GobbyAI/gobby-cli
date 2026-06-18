---
title: crates/gcode/src/config/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/config/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/config/tests.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/config/tests.rs` exposes 27 indexed API symbols.

## How it fits

`crates/gcode/src/config/tests.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `write_project_json` | function | Indexed function `write_project_json` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:14-22] |
| `run_git` | function | Indexed function `run_git` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:24-38] |
| `create_linked_worktree` | function | Indexed function `create_linked_worktree` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:40-70] |
| `with_service_env` | function | Indexed function `with_service_env` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:80-90] |
| `config_value_for` | function | Indexed function `config_value_for` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:92-96] |
| `adapter_env_precedence_and_json_decode` | function | Indexed function `adapter_env_precedence_and_json_decode` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:100-140] |
| `project_name_lookup_suffixes_cover_unix_and_windows_paths` | function | Indexed function `project_name_lookup_suffixes_cover_unix_and_windows_paths` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:143-148] |
| `daemon_url_falls_back_when_bootstrap_path_is_unavailable` | function | Indexed function `daemon_url_falls_back_when_bootstrap_path_is_unavailable` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:152-166] |
| `daemon_url_normalizes_wildcard_bootstrap_bind_host` | function | Indexed function `daemon_url_normalizes_wildcard_bootstrap_bind_host` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:170-191] |
| `adapter_resolves_config_store_secrets` | function | Indexed function `adapter_resolves_config_store_secrets` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:195-229] |
| `resolve_secret_stub` | function | Indexed function `resolve_secret_stub` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:206-213] |
| `embedding_config_source_errors_are_propagated` | function | Indexed function `embedding_config_source_errors_are_propagated` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:232-242] |
| `vector_dim_setting_reads_ai_config_no_env` | function | Indexed function `vector_dim_setting_reads_ai_config_no_env` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:246-268] |
| `phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name` | function | Indexed function `phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:272-295] |
| `falkor_password_reads_password_key` | function | Indexed function `falkor_password_reads_password_key` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:299-313] |
| `invalid_service_port_warns_and_uses_default` | function | Indexed function `invalid_service_port_warns_and_uses_default` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:317-333] |
| `test_resolve_project_id_requires_project_context` | function | Indexed function `test_resolve_project_id_requires_project_context` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:336-348] |
| `main_repo_keeps_project_json_id` | function | Indexed function `main_repo_keeps_project_json_id` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:351-367] |
| `self_referential_parent_marker_keeps_project_json_id` | function | Indexed function `self_referential_parent_marker_keeps_project_json_id` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:370-389] |
| `isolated_marker_with_parent_metadata_resolves_overlay_scope` | function | Indexed function `isolated_marker_with_parent_metadata_resolves_overlay_scope` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:392-426] |
| `isolated_marker_without_complete_parent_metadata_is_rejected` | function | Indexed function `isolated_marker_without_complete_parent_metadata_is_rejected` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:429-449] |
| `isolated_marker_rejects_missing_parent_path` | function | Indexed function `isolated_marker_rejects_missing_parent_path` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:452-466] |
| `linked_worktree_uses_path_id_and_ignores_copied_project_id` | function | Indexed function `linked_worktree_uses_path_id_and_ignores_copied_project_id` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:469-500] |
| `generated_identity_writes_only_for_non_isolated_roots` | function | Indexed function `generated_identity_writes_only_for_non_isolated_roots` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:503-515] |
| `project_id_only_context_rejects_empty_id_before_runtime_resolution` | function | Indexed function `project_id_only_context_rejects_empty_id_before_runtime_resolution` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:518-529] |
| `project_id_projection_cleanup_selection_includes_qdrant_without_embeddings` | function | Indexed function `project_id_projection_cleanup_selection_includes_qdrant_without_embeddings` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:532-539] |
| `project_id_context_with_services_rejects_empty_id_before_runtime_resolution` | function | Indexed function `project_id_context_with_services_rejects_empty_id_before_runtime_resolution` in `crates/gcode/src/config/tests.rs`. [crates/gcode/src/config/tests.rs:542-553] |

