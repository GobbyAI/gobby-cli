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

`crates/gcode/src/config/context.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `FalkorConfig` | class | 'FalkorConfig' is a configuration struct that stores the Falkor database connection host, port, optional password, and target graph name. [crates/gcode/src/config/context.rs:26-31] |
| `QdrantConfig` | type | Indexed type `QdrantConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:34] |
| `EmbeddingConfig` | type | Indexed type `EmbeddingConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:37] |
| `CodeVectorSettings` | class | 'CodeVectorSettings' is a Rust configuration struct that optionally specifies the dimensionality of a code vector via 'vector_dim: Option<usize>'. [crates/gcode/src/config/context.rs:51-53] |
| `IndexingSettings` | type | Indexed type `IndexingSettings` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:55] |
| `ServiceConfigSelection` | class | 'ServiceConfigSelection' is a boolean feature-selection struct indicating whether the 'falkordb', 'qdrant', 'embedding', and 'code_vectors' service configurations are enabled. [crates/gcode/src/config/context.rs:58-63] |
| `ServiceConfigSelection::all` | method | Constructs and returns a 'Self' value with all feature flags enabled by setting 'falkordb', 'qdrant', 'embedding', and 'code_vectors' to 'true'. [crates/gcode/src/config/context.rs:66-73] |
| `ServiceConfigSelection::database_only` | method | Returns a 'Self' value configured for database-only mode by setting 'falkordb', 'qdrant', 'embedding', and 'code_vectors' all to 'false'. [crates/gcode/src/config/context.rs:75-82] |
| `ServiceConfigSelection::falkordb_only` | method | Returns a configuration instance with 'falkordb' enabled and 'qdrant', 'embedding', and 'code_vectors' disabled. [crates/gcode/src/config/context.rs:84-91] |
| `ServiceConfigSelection::qdrant_only` | method | Returns a 'Self' value configured to enable only 'qdrant' while disabling 'falkordb', 'embedding', and 'code_vectors'. [crates/gcode/src/config/context.rs:93-100] |
| `ServiceConfigSelection::projection_cleanup` | method | Returns a 'Self' configuration for projection cleanup with 'falkordb' and 'qdrant' enabled and 'embedding' and 'code_vectors' disabled. [crates/gcode/src/config/context.rs:102-109] |
| `ServiceConfigSelection::vectors` | method | Returns a 'Self' value with 'falkordb' disabled and 'qdrant', 'embedding', and 'code_vectors' enabled. [crates/gcode/src/config/context.rs:111-118] |
| `ServiceConfigSelection::hybrid_search` | method | 'hybrid_search' constructs and returns a 'Self' configuration with 'falkordb', 'qdrant', and 'embedding' enabled, while 'code_vectors' remains disabled. [crates/gcode/src/config/context.rs:120-127] |
| `ServiceConfigSelection::default` | method | Returns the 'Self::all()' value as this type’s default instance. [crates/gcode/src/config/context.rs:131-133] |
| `CodeVectorConfigError` | type | Indexed type `CodeVectorConfigError` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:137-140] |
| `CodeVectorConfigError::fmt` | method | Implements 'Display' formatting for the error by matching on 'InvalidVectorDim' and 'Read' variants and writing a corresponding human-readable message to the formatter. [crates/gcode/src/config/context.rs:143-151] |
| `FalkorConfig::connection_config` | method | Returns a 'gobby_core::config::FalkorConfig' by cloning 'self.host' and 'self.password' and copying 'self.port' into the corresponding fields. [crates/gcode/src/config/context.rs:157-163] |
| `Context` | class | 'Context' is a runtime configuration struct that aggregates project identity and paths with database, daemon, indexing, and optional vector-search/embedding backend settings needed to operate Gobby. [crates/gcode/src/config/context.rs:168-191] |
| `ProjectIndexScope` | type | Indexed type `ProjectIndexScope` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:194-203] |
| `MissingIdentity` | type | Indexed type `MissingIdentity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:206-209] |
| `ProjectIdentitySource` | type | Indexed type `ProjectIdentitySource` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:212-219] |
| `ProjectIdentity` | class | 'ProjectIdentity' is a Rust struct that identifies a project by its 'project_id', root 'PathBuf', origin 'source', optional 'warning', a 'should_write_gcode_json' flag, and an 'index_scope' controlling indexing behavior. [crates/gcode/src/config/context.rs:222-229] |
| `Context::resolve` | method | 'resolve' constructs a 'Self' by delegating to 'Self::resolve_with_services(project_override, quiet, ServiceConfigSelection::all())' and returns the resulting 'anyhow::Result<Self>'. [crates/gcode/src/config/context.rs:233-235] |
| `Context::resolve_with_services` | method | Resolves the target project root from an override or auto-detection, loads and validates its identity and index scope, then builds 'Self' by reading optional standalone config and database-backed service settings for the requested components ('falkordb', 'qdrant', 'embedding', 'indexing', and 'code_vectors'). [crates/gcode/src/config/context.rs:237-302] |

_13 more symbol(s) not shown — run `gcode outline crates/gcode/src/config/context.rs` for the full list._

_Verified by 1 in-file unit test._

