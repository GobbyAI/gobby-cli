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

## crates/gcode/src/config

This module is the configuration resolution layer for the `gcode` crate. It implements a layered lookup chain described in `context.rs:1-6`: `bootstrap.yaml → PostgreSQL hub → config_store → service configs`, and handles secret/variable interpolation patterns (`$secret:NAME`, `${VAR}`). The public surface is split across two files: `context.rs` owns all type definitions, environment-variable name constants, and the high-level `GcodeContext` builder; `services.rs` contains the concrete resolution functions and the two config-source adapters — `PostgresConfigSource` (backed by `gobby_core::postgres::read_config_value`) and `FallbackConfigSource` (which tries Postgres first then falls back to `StandaloneConfig` loaded from a local `gcore_config` file) (services.rs:19-65).

`services.rs` exports one resolution function per subsystem: `resolve_falkordb_config`, `resolve_qdrant_config`, `resolve_embedding_config`, `resolve_code_vector_settings`, and `resolve_indexing_settings` (context.rs:14-20). Each function accepts a mutable `ServiceConfigSource` and tries, in priority order: environment variable → Postgres/fallback store → defaults. The `service_env_value` dispatcher (services.rs:31-41) maps the five canonical config keys to their environment variable names, making env overrides possible without touching the database. `ServiceConfigSelection` lets callers choose which subsystems to resolve, with the two preset constructors `all()` and `database_only()` (context.rs:62-80).

### Public types

| Type | Description | Defined at |
|---|---|---|
| `FalkorConfig` | FalkorDB host/port/password/graph_name | context.rs:26-32 |
| `QdrantConfig` | Re-export of `gobby_core::config::QdrantConfig` | context.rs:35 |
| `EmbeddingConfig` | Re-export of `gobby_core::config::EmbeddingConfig` | context.rs:38 |
| `CodeVectorSettings` | Optional `vector_dim` for the code-symbol Qdrant collection | context.rs:52-54 |
| `IndexingSettings` | Re-export of `gobby_core::config::IndexingConfig` | context.rs:57 |
| `ServiceConfigSelection` | Boolean flags selecting which services to resolve | context.rs:59-80 |

### Environment variables

| Variable | Config key | Service |
|---|---|---|
| `GOBBY_FALKORDB_HOST` | `databases.falkordb.host` | FalkorDB |
| `GOBBY_FALKORDB_PORT` | `databases.falkordb.port` | FalkorDB |
| `GOBBY_FALKORDB_PASSWORD` | `databases.falkordb.password` | FalkorDB |
| `GOBBY_QDRANT_URL` | `databases.qdrant.url` | Qdrant |
| `GOBBY_QDRANT_API_KEY` | `databases.qdrant.api_key` | Qdrant |

### Notable constants

| Constant | Value / Purpose | Location |
|---|---|---|
| `FALKORDB_GRAPH_NAME` | Re-exports `gobby_core::config::CODE_GRAPH_NAME` | context.rs:43 |
| `CODE_SYMBOL_COLLECTION_PREFIX` | `"code_symbols_"` — Qdrant collection name prefix | context.rs:44 |

The module collaborates tightly with `gobby_core::config` (for `AiCapability`, `AiRouting`, `CapabilityBinding`, `ConfigSource`, and embedding key constants), `gobby_core::provisioning` (for `StandaloneConfig` and `GCORE_CONFIG_FILENAME`), and `gobby_core::postgres` (for the low-level `read_config_value` call) (services.rs:1-7). Within `gcode` itself it calls into `crate::db` for Postgres client setup and `crate::secrets` to expand secret references (services.rs:17-18). Git worktree awareness comes from `crate::git::WorktreeKind`, used in `context.rs:22` when deriving per-project identifiers such as Qdrant collection suffixes.

`tests.rs` validates the module without a live database by providing `resolve_*_from_values` variants of each resolver and an `with_service_env` helper that clears all five env vars before running a closure, preventing test cross-contamination (tests.rs:63-90). It also exercises `project_name_suffixes` and `resolve_project_id` against real git worktrees constructed with `create_linked_worktree` (tests.rs:42-63), confirming that linked worktrees produce distinct suffixes from their parent repo.
[crates/gcode/src/config/context.rs:26-31]
[crates/gcode/src/config/services.rs:20-22]
[crates/gcode/src/config/tests.rs:14-22]
[crates/gcode/src/config/context.rs:34]
[crates/gcode/src/config/context.rs:37]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/config/context.rs\|crates/gcode/src/config/context.rs]] | `crates/gcode/src/config/context.rs` exposes 38 indexed API symbols. |
| [[code/files/crates/gcode/src/config/services.rs\|crates/gcode/src/config/services.rs]] | `crates/gcode/src/config/services.rs` exposes 53 indexed API symbols. |
| [[code/files/crates/gcode/src/config/tests.rs\|crates/gcode/src/config/tests.rs]] | `crates/gcode/src/config/tests.rs` exposes 27 indexed API symbols. |

