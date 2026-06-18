---
title: crates/gwiki/src/commands/index.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/index.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/index.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/index.rs` exposes 35 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/index.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `IndexReport` | class | Indexed class `IndexReport` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:35-38] |
| `execute` | function | Indexed function `execute` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:40-46] |
| `index_resolved_scope` | function | Indexed function `index_resolved_scope` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:48-52] |
| `index_resolved_scope_report` | function | Indexed function `index_resolved_scope_report` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:54-86] |
| `execute_ingest_file` | function | Indexed function `execute_ingest_file` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:88-153] |
| `execute_ingest_url` | function | Indexed function `execute_ingest_url` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:155-191] |
| `resolve_ingest_ai_context` | function | Indexed function `resolve_ingest_ai_context` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:193-205] |
| `resolve_ingest_file_ai_context` | function | Indexed function `resolve_ingest_file_ai_context` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:207-229] |
| `resolve_video_frame_interval_seconds` | function | Indexed function `resolve_video_frame_interval_seconds` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:231-254] |
| `ai_project_id` | function | Indexed function `ai_project_id` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:256-258] |
| `ai_project_id_for_search` | function | Indexed function `ai_project_id_for_search` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:260-266] |
| `gobby_home` | function | Indexed function `gobby_home` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:268-272] |
| `connect_postgres_index` | function | Indexed function `connect_postgres_index` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:274-281] |
| `postgres_store_for_search` | function | Indexed function `postgres_store_for_search` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:283-288] |
| `sync_falkor_graph` | function | Indexed function `sync_falkor_graph` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:290-314] |
| `sync_qdrant_vectors` | function | Indexed function `sync_qdrant_vectors` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:316-367] |
| `qdrant_sync_degradation` | function | Indexed function `qdrant_sync_degradation` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:369-371] |
| `not_configured_degradation` | function | Indexed function `not_configured_degradation` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:373-375] |
| `unreachable_degradation` | function | Indexed function `unreachable_degradation` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:377-387] |
| `service_unavailable_degradation` | function | Indexed function `service_unavailable_degradation` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:389-394] |
| `resolve_vector_embedding` | function | Indexed function `resolve_vector_embedding` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:396-431] |
| `effective_embedding_route` | function | Indexed function `effective_embedding_route` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:433-457] |
| `indexed_counts_for_postgres` | function | Indexed function `indexed_counts_for_postgres` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:459-469] |
| `render_index` | function | Indexed function `render_index` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:471-512] |
| `render_ingest_file` | function | Indexed function `render_ingest_file` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:514-569] |
| `render_ingest_url` | function | Indexed function `render_ingest_url` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:571-641] |
| `ensure_scope_root` | function | Indexed function `ensure_scope_root` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:643-653] |
| `TestConfigSource` | class | Indexed class `TestConfigSource` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:659-661] |
| `TestConfigSource::config_value` | method | Indexed method `TestConfigSource::config_value` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:664-668] |
| `TestConfigSource::resolve_value` | method | Indexed method `TestConfigSource::resolve_value` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:670-672] |
| `video_frame_interval_zero_is_invalid` | function | Indexed function `video_frame_interval_zero_is_invalid` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:676-683] |
| `index_render_includes_empty_degradations` | function | Indexed function `index_render_includes_empty_degradations` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:686-703] |
| `index_render_reports_qdrant_sync_failure_degradation` | function | Indexed function `index_render_reports_qdrant_sync_failure_degradation` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:706-730] |
| `auto_embedding_route_falls_back_to_direct_without_ai` | function | Indexed function `auto_embedding_route_falls_back_to_direct_without_ai` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:734-739] |
| `sample_counts` | function | Indexed function `sample_counts` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:741-749] |

