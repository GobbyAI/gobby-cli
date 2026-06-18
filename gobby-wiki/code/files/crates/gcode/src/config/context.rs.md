---
title: crates/gcode/src/config/context.rs
type: code_file
provenance:
- file: crates/gcode/src/config/context.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/config/context.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

## How it fits
[crates/gcode/src/config/context.rs:26-31]
[crates/gcode/src/config/context.rs:34]
[crates/gcode/src/config/context.rs:37]
[crates/gcode/src/config/context.rs:51-53]
[crates/gcode/src/config/context.rs:55]

## Key components

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
| `Context::resolve_for_project_id_with_services` | method | Resolves a project-scoped configuration by normalizing the project ID, loading the database URL and optional standalone config, querying read-only service-specific settings from the database according to 'ServiceConfigSelection', and constructing a 'Self' with the resolved service configs, indexing settings, daemon URL, and 'ProjectIndexScope::Single'. [crates/gcode/src/config/context.rs:305-352] |
| `resolve_project_identity` | function | Resolves a project’s 'ProjectIdentity' by canonicalizing the root, loading any '.gobby/project.json' isolation marker, validating parent-path/ID pairing, treating self-referential markers as non-isolated projects, and otherwise returning either an isolated overlay identity with normalized parent metadata or an isolated-root identity. [crates/gcode/src/config/context.rs:355-408] |
| `resolve_non_isolated_project_identity` | function | Resolves a non-isolated project identity by preferring a linked git worktree top-level, then '.gobby/project.json', then '.gobby/gcode.json', otherwise either generates a new single-scope 'ProjectIdentity' or returns an error depending on 'MissingIdentity'. [crates/gcode/src/config/context.rs:410-464] |
| `is_self_referential_isolation_marker` | function | Returns 'true' only when the marker has a 'parent_project_path' that, after resolution via 'resolve_parent_project_root(root, ...)', points back to the given 'root'; otherwise it returns 'false'. [crates/gcode/src/config/context.rs:466-474] |
| `resolve_parent_project_root` | function | Returns the canonicalized absolute path of 'parent_project_path', resolving relative paths against 'root' first and falling back to the unresolved joined path if canonicalization fails. [crates/gcode/src/config/context.rs:476-484] |
| `normalize_project_id` | function | Trims whitespace from 'project_id', rejects empty input with an error, and otherwise validates it as a UUID string, returning the canonical UUID representation or a context-rich 'anyhow::Error' if parsing fails. [crates/gcode/src/config/context.rs:486-494] |
| `validate_parent_code_index` | function | Returns 'Ok(())' for non-overlay scopes, otherwise verifies via the database that the parent project has at least one row in 'code_indexed_files' and bails with an error identifying the parent root and project ID if no parent code index exists. [crates/gcode/src/config/context.rs:496-527] |
| `warn_project_identity` | function | Prints 'Warning: {warning}' to standard error when 'quiet' is false and 'identity.warning' is 'Some', otherwise does nothing. [crates/gcode/src/config/context.rs:529-536] |
| `resolve_project_by_name` | function | Resolves a project name to an existing directory path by querying the readonly 'code_indexed_projects' table for matching 'root_path' values or name suffixes, returning the first indexed path that still exists on disk, or bailing with a not-found error if none match. [crates/gcode/src/config/context.rs:541-565] |
| `project_name_suffixes` | function | Returns a pair of 'String's containing the input 'name' prefixed with a forward slash and a backslash, respectively. [crates/gcode/src/config/context.rs:567-569] |
| `detect_project_root` | function | Returns the current working directory’s project root by reading 'std::env::current_dir()' and delegating to 'detect_project_root_from', propagating any error as 'anyhow::Result<PathBuf>'. [crates/gcode/src/config/context.rs:577-580] |
| `detect_project_root_from` | function | Resolves 'start' to an absolute directory and returns the nearest project root by preferring an identity file ('.gobby/project.json' or '.gobby/gcode.json'), then the Git worktree top-level for any Git-linked checkout, then the nearest '.git'/'.hg' ancestor, and finally 'start' itself as a last resort. [crates/gcode/src/config/context.rs:582-618] |
| `resolve_project_id` | function | Returns the current project’s ID by resolving its project identity from 'project_root' and propagating an error if the identity is missing. [crates/gcode/src/config/context.rs:627-629] |
| `absolute_fallback` | function | Returns 'path' unchanged when it is already absolute, otherwise prefixes it with the current working directory, falling back to the system temporary directory if 'current_dir()' fails. [crates/gcode/src/config/context.rs:631-639] |

