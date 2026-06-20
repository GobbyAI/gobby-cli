---
title: crates/gcode/src/config
type: code_module
provenance:
- file: crates/gcode/src/config/context.rs
- file: crates/gcode/src/config/services.rs
- file: crates/gcode/src/config/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/config

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/config` is the gcode configuration layer. Its `context.rs` facade documents the resolution order as `bootstrap.yaml -> PostgreSQL hub -> config_store -> service configs`, including `$secret:NAME` and `${VAR}` expansion, and exposes the typed service settings used by the rest of gcode . It delegates concrete service resolution to `services.rs`, importing `resolve_falkordb_config`, `resolve_qdrant_config`, `resolve_embedding_config`, `resolve_code_vector_settings`, `resolve_indexing_settings`, and standalone config loading .

`services.rs` owns the backend mechanics: it reads config values from PostgreSQL via `gobby_core::postgres::read_config_value`, decodes stored values, treats a missing config table as “no value,” and resolves secret-backed values through `crate::secrets` . It also layers fallback inputs through `FallbackConfigSource`, combining PostgreSQL with optional standalone provisioning config . The module collaborates outward with `gobby_core` config/provisioning types, `postgres::Client`, local `db`, local `secrets`, and project/git helpers used by `context.rs`  .

Tests exercise both the context-level project identity flow and service-specific value resolvers. The supplied test excerpt calls `resolve_project_id` and `project_name_suffixes`, pure `*_from_values` service resolvers, writes `.gobby/project.json`, and creates linked git worktrees to validate project/worktree-sensitive behavior .

| Fact | Symbol / key | Notes |
| --- | --- | --- |
| FalkorDB config type | `FalkorConfig` | `host`, `port`, `password`, `graph_name`  |
| Qdrant config type | `QdrantConfig` | Alias to `gobby_core::config::QdrantConfig`  |
| Embedding config type | `EmbeddingConfig` | Alias to `gobby_core::config::EmbeddingConfig`  |
| Code vector settings | `CodeVectorSettings` | Optional `vector_dim`  |
| Indexing settings | `IndexingSettings` | Alias to `gobby_core::config::IndexingConfig` [crates/gcode/src/config/context.rs:55] |
| Service selection | `ServiceConfigSelection` | Toggles `falkordb`, `qdrant`, `embedding`, `code_vectors`  |

| Config key | Environment variable |
| --- | --- |
| `databases.falkordb.host` | `GOBBY_FALKORDB_HOST` |
| `databases.falkordb.port` | `GOBBY_FALKORDB_PORT` |
| `databases.falkordb.password` | `GOBBY_FALKORDB_PASSWORD` |
| `databases.qdrant.url` | `GOBBY_QDRANT_URL` |
| `databases.qdrant.api_key` | `GOBBY_QDRANT_API_KEY` |

Supported by  and [crates/gcode/src/config/services.rs:29-39].

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/config/context.rs\|crates/gcode/src/config/context.rs]] | `crates/gcode/src/config/context.rs` exposes 38 indexed API symbols. |
| [[code/files/crates/gcode/src/config/services.rs\|crates/gcode/src/config/services.rs]] | `crates/gcode/src/config/services.rs` exposes 53 indexed API symbols. |
| [[code/files/crates/gcode/src/config/tests.rs\|crates/gcode/src/config/tests.rs]] | `crates/gcode/src/config/tests.rs` exposes 27 indexed API symbols. |

