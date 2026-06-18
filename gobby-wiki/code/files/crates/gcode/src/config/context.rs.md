---
title: crates/gcode/src/config/context.rs
type: code_file
provenance:
- file: crates/gcode/src/config/context.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/config/context.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/config/context.rs` exposes 38 indexed API symbols.

## How it fits

`crates/gcode/src/config/context.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `FalkorConfig` | class | Indexed class `FalkorConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:26-31] |
| `QdrantConfig` | type | Indexed type `QdrantConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:34] |
| `EmbeddingConfig` | type | Indexed type `EmbeddingConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:37] |
| `CodeVectorSettings` | class | Indexed class `CodeVectorSettings` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:51-53] |
| `IndexingSettings` | type | Indexed type `IndexingSettings` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:55] |
| `ServiceConfigSelection` | class | Indexed class `ServiceConfigSelection` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:58-63] |
| `ServiceConfigSelection::all` | method | Indexed method `ServiceConfigSelection::all` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:66-73] |
| `ServiceConfigSelection::database_only` | method | Indexed method `ServiceConfigSelection::database_only` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:75-82] |
| `ServiceConfigSelection::falkordb_only` | method | Indexed method `ServiceConfigSelection::falkordb_only` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:84-91] |
| `ServiceConfigSelection::qdrant_only` | method | Indexed method `ServiceConfigSelection::qdrant_only` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:93-100] |
| `ServiceConfigSelection::projection_cleanup` | method | Indexed method `ServiceConfigSelection::projection_cleanup` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:102-109] |
| `ServiceConfigSelection::vectors` | method | Indexed method `ServiceConfigSelection::vectors` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:111-118] |
| `ServiceConfigSelection::hybrid_search` | method | Indexed method `ServiceConfigSelection::hybrid_search` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:120-127] |
| `ServiceConfigSelection::default` | method | Indexed method `ServiceConfigSelection::default` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:131-133] |
| `CodeVectorConfigError` | type | Indexed type `CodeVectorConfigError` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:137-140] |
| `CodeVectorConfigError::fmt` | method | Indexed method `CodeVectorConfigError::fmt` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:143-151] |
| `FalkorConfig::connection_config` | method | Indexed method `FalkorConfig::connection_config` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:157-163] |
| `Context` | class | Indexed class `Context` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:168-191] |
| `ProjectIndexScope` | type | Indexed type `ProjectIndexScope` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:194-203] |
| `MissingIdentity` | type | Indexed type `MissingIdentity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:206-209] |
| `ProjectIdentitySource` | type | Indexed type `ProjectIdentitySource` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:212-219] |
| `ProjectIdentity` | class | Indexed class `ProjectIdentity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:222-229] |
| `Context::resolve` | method | Indexed method `Context::resolve` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:233-235] |
| `Context::resolve_with_services` | method | Indexed method `Context::resolve_with_services` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:237-302] |
| `Context::resolve_for_project_id_with_services` | method | Indexed method `Context::resolve_for_project_id_with_services` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:305-352] |
| `resolve_project_identity` | function | Indexed function `resolve_project_identity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:355-408] |
| `resolve_non_isolated_project_identity` | function | Indexed function `resolve_non_isolated_project_identity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:410-464] |
| `is_self_referential_isolation_marker` | function | Indexed function `is_self_referential_isolation_marker` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:466-474] |
| `resolve_parent_project_root` | function | Indexed function `resolve_parent_project_root` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:476-484] |
| `normalize_project_id` | function | Indexed function `normalize_project_id` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:486-494] |
| `validate_parent_code_index` | function | Indexed function `validate_parent_code_index` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:496-527] |
| `warn_project_identity` | function | Indexed function `warn_project_identity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:529-536] |
| `resolve_project_by_name` | function | Indexed function `resolve_project_by_name` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:541-565] |
| `project_name_suffixes` | function | Indexed function `project_name_suffixes` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:567-569] |
| `detect_project_root` | function | Indexed function `detect_project_root` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:577-580] |
| `detect_project_root_from` | function | Indexed function `detect_project_root_from` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:582-618] |
| `resolve_project_id` | function | Indexed function `resolve_project_id` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:627-629] |
| `absolute_fallback` | function | Indexed function `absolute_fallback` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:631-639] |

