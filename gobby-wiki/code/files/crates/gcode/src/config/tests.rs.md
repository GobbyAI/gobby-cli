---
title: crates/gcode/src/config/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/config/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/config/tests.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

## How it fits
[crates/gcode/src/config/tests.rs:14-22]
[crates/gcode/src/config/tests.rs:24-38]
[crates/gcode/src/config/tests.rs:40-70]
[crates/gcode/src/config/tests.rs:80-90]
[crates/gcode/src/config/tests.rs:92-96]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `write_project_json` | function | Creates 'root/.gobby', then serializes 'json' as pretty-printed JSON and writes it to 'project.json' inside that directory, panicking on any filesystem or serialization error. [crates/gcode/src/config/tests.rs:14-22] |
| `run_git` | function | Runs 'git -C <dir> <args...>', expects the command to execute successfully, and panics with captured stdout and stderr if 'git' returns a non-success exit status. [crates/gcode/src/config/tests.rs:24-38] |
| `create_linked_worktree` | function | Creates a temporary Git repository with an initial commit, then adds a linked worktree on a new branch and returns the paths to the primary repo and the linked worktree. [crates/gcode/src/config/tests.rs:40-70] |
| `with_service_env` | function | 'with_service_env' constructs a temporary environment override set initialized with all 'SERVICE_ENV_KEYS' cleared to 'None', applies the caller-provided 'overrides', and runs 'closure' under those transient variables via 'temp_env::with_vars'. [crates/gcode/src/config/tests.rs:80-90] |
| `config_value_for` | function | Returns a closure that looks up a '&str' key in the provided 'HashMap<&str, &str>' and, if present, clones the matched value into an owned 'String' wrapped in 'Some', otherwise returns 'None'. [crates/gcode/src/config/tests.rs:92-96] |
| `adapter_env_precedence_and_json_decode` | function | Verifies that service environment variables override stored config values for adapter settings while JSON-decoded stored strings and 'null' map correctly into typed FalkorDB, Qdrant, and embedding configs, including parsing numeric ports and optional secrets. [crates/gcode/src/config/tests.rs:100-140] |
| `project_name_lookup_suffixes_cover_unix_and_windows_paths` | function | Verifies that 'project_name_suffixes("api_%")' returns Unix and Windows path suffixes prefixed with '/' and '\', respectively. [crates/gcode/src/config/tests.rs:143-148] |
| `daemon_url_falls_back_when_bootstrap_path_is_unavailable` | function | Verifies that 'gobby_core::daemon_url::daemon_url()' falls back to the default 'http://127.0.0.1:60887' when 'GOBBY_DAEMON_URL' and 'GOBBY_PORT' are unset and 'GOBBY_HOME' points to an unusable path. [crates/gcode/src/config/tests.rs:152-166] |
| `daemon_url_normalizes_wildcard_bootstrap_bind_host` | function | Verifies that 'gobby_core::daemon_url::daemon_url()' normalizes a 'bind_host' of '0.0.0.0' from 'bootstrap.yaml' to '127.0.0.1' when constructing the daemon URL, yielding 'http://127.0.0.1:61234' in the absence of override environment variables. [crates/gcode/src/config/tests.rs:170-191] |
| `adapter_resolves_config_store_secrets` | function | Verifies that adapter-specific config resolution functions substitute '$secret:' placeholders from a config store using the provided secret resolver for FalkorDB, Qdrant, and embedding settings. [crates/gcode/src/config/tests.rs:195-229] |
| `resolve_secret_stub` | function | Returns a 'String' by mapping three known secret placeholders ('$secret:falkordb_password', '$secret:qdrant_api_key', '$secret:embedding_api_key') to hardcoded resolved values and otherwise cloning the input unchanged. [crates/gcode/src/config/tests.rs:206-213] |
| `embedding_config_source_errors_are_propagated` | function | Verifies that 'resolve_embedding_config_from_fallible_values' propagates source read failures as an error containing both the config-key read failure context and the underlying '"database read failed"' message, rather than treating the value as missing embeddings. [crates/gcode/src/config/tests.rs:232-242] |
| `vector_dim_setting_reads_ai_config_no_env` | function | Verifies that, with no service environment variables set, 'resolve_code_vector_settings_from_values' reads 'embedding_keys::AI_DIM' from config-store values as 'Some(2048)' for '"2048"', 'None' for '"null"', and returns 'CodeVectorConfigError::InvalidVectorDim' for an invalid string value. [crates/gcode/src/config/tests.rs:246-268] |
| `phase7_config_resolution_returns_gcode_falkor_config_with_core_fields_and_graph_name` | function | Verifies that resolving FalkorDB config from stored values yields a config with the expected host, port, password, and fixed 'graph_name' '"gobby_code"', and that its derived connection config matches those core fields. [crates/gcode/src/config/tests.rs:272-295] |
| `falkor_password_reads_password_key` | function | Verifies that FalkorDB config resolution reads 'databases.falkordb.password' from the supplied config values and populates the resulting 'password' field with 'Some("stored-pass")'. [crates/gcode/src/config/tests.rs:299-313] |
| `invalid_service_port_warns_and_uses_default` | function | Verifies that when the configured FalkorDB service port is invalid ('"0"' or a non-numeric string), 'resolve_falkordb_config_from_values' falls back to the default port '16379' while still resolving the config successfully. [crates/gcode/src/config/tests.rs:317-333] |
| `test_resolve_project_id_requires_project_context` | function | Verifies that 'resolve_project_id' returns an error when called in a directory without gcode project context, and that the error message mentions both “No gcode project found” and 'gcode init'. [crates/gcode/src/config/tests.rs:336-348] |
| `main_repo_keeps_project_json_id` | function | Verifies that when a repository contains a 'project.json' with an 'id', 'resolve_project_identity' returns that ID as the project identity, marks the source as 'ProjectJson', does not request writing 'gcode.json', and emits no warning. [crates/gcode/src/config/tests.rs:351-367] |
| `self_referential_parent_marker_keeps_project_json_id` | function | Verifies that when 'project.json' declares the current project as its own parent via 'parent_project_path' and matching 'parent_project_id', 'resolve_project_identity' preserves the 'project_id' from 'project.json', marks the source as 'ProjectJson', disables G-code JSON writing, and emits no warning. [crates/gcode/src/config/tests.rs:370-389] |
| `isolated_marker_with_parent_metadata_resolves_overlay_scope` | function | Verifies that resolving project identity for a worktree with isolated marker metadata yields an 'IsolatedOverlay' identity whose project ID is the worktree’s code index ID, whose index scope points to the canonical overlay and parent roots with the provided parent project ID, and that it does not write 'gcode.json' or emit a warning. [crates/gcode/src/config/tests.rs:392-426] |
| `isolated_marker_without_complete_parent_metadata_is_rejected` | function | Verifies that 'resolve_project_identity' rejects a project isolation marker when 'parent_project_path' is present without 'parent_project_id', returning an error that identifies the invalid '.gobby/project.json' metadata pair. [crates/gcode/src/config/tests.rs:429-449] |
| `isolated_marker_rejects_missing_parent_path` | function | Creates a temporary project JSON containing 'id' and 'parent_project_id' but no 'parent_path', then asserts that 'resolve_project_identity(..., MissingIdentity::Error)' fails with an error indicating those parent fields must be set together. [crates/gcode/src/config/tests.rs:452-466] |
| `linked_worktree_uses_path_id_and_ignores_copied_project_id` | function | Verifies that a linked worktree’s resolved project identity always uses 'code_index_id_for_root(&linked)' as the 'project_id' and remains 'ProjectIdentitySource::LinkedWorktree' with no warning and no '.gcode.json' write recommendation, even when a copied 'project.json' contains a different 'id'. [crates/gcode/src/config/tests.rs:469-500] |
| `generated_identity_writes_only_for_non_isolated_roots` | function | Verifies that resolving a project identity with 'MissingIdentity::Generate' in a temporary root yields a generated identity whose source is 'Generated', whose 'gcode.json' should be written, and whose 'project_id' matches 'code_index_id_for_root(tmp.path())'. [crates/gcode/src/config/tests.rs:503-515] |
| `project_id_only_context_rejects_empty_id_before_runtime_resolution` | function | Asserts that resolving a project-id-only context with a whitespace-only project ID fails immediately, before any runtime/DB resolution, with an error indicating '--project-id' must not be empty. [crates/gcode/src/config/tests.rs:518-529] |
| `project_id_projection_cleanup_selection_includes_qdrant_without_embeddings` | function | Verifies that 'ServiceConfigSelection::projection_cleanup()' enables 'falkordb' and 'qdrant' while leaving 'embedding' and 'code_vectors' disabled. [crates/gcode/src/config/tests.rs:532-539] |
| `project_id_context_with_services_rejects_empty_id_before_runtime_resolution` | function | Verifies that 'Context::resolve_for_project_id_with_services' rejects a whitespace-only project ID immediately, returning an error containing '--project-id must not be empty' before any database/runtime resolution occurs. [crates/gcode/src/config/tests.rs:542-553] |

