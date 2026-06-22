---
title: crates/gwiki/src/commands/setup.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/setup.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/setup.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/setup.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/setup.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `PostgresSetupResult` | type | Indexed type `PostgresSetupResult` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:19] |
| `execute` | function | 'execute' resolves the target scope, builds PostgreSQL object payloads from the wiki setup, and either provisions a standalone Gobby deployment to run PostgreSQL setup and write configuration or, in attached mode, selects a database URL for the setup workflow, returning the resulting command outcome or a 'WikiError'. [crates/gwiki/src/commands/setup.rs:21-93] |
| `run_gwiki_postgres_setup` | function | Connects to PostgreSQL using 'database_url', builds a non-interactive 'SetupContext' with the live client, runs 'setup.create', and returns the created/skipped/failed counts as 'PostgresSetupResult', mapping connection and setup errors into 'WikiError'. [crates/gwiki/src/commands/setup.rs:95-112] |
| `apply_service_overrides` | function | Applies any configured FalkorDB host, port, and password overrides from 'SetupOptions' to 'DockerServiceOptions', replacing the corresponding service fields when the option values are present. [crates/gwiki/src/commands/setup.rs:114-124] |
| `gobby_home` | function | Returns the 'PathBuf' produced by 'gobby_core::gobby_home()', propagating any error as 'anyhow::Result<PathBuf>'. [crates/gwiki/src/commands/setup.rs:126-128] |
| `write_gwiki_gcore_config` | function | Loads or creates the standalone GCore config at the computed home path, populates PostgreSQL and optional FalkorDB/Qdrant/service-compose settings from either provisioning report data or setup options, applies embedding options and required-service diagnostics, writes the config back to disk, and returns the config path. [crates/gwiki/src/commands/setup.rs:130-181] |
| `diagnose_required_service_config` | function | Checks a 'StandaloneConfig' for missing FalkorDB and blank-or-absent Qdrant URL settings and emits warnings when graph or semantic functionality will be unavailable. [crates/gwiki/src/commands/setup.rs:183-199] |
| `apply_embedding_options` | function | Validates the embedding vector dimension and, if any embedding-related option is set, writes the provided embedding provider, API base, model, query prefix, vector dimension, and API key into 'StandaloneConfig', then applies text-generation bootstrap settings derived from the embedding endpoint. [crates/gwiki/src/commands/setup.rs:201-244] |
| `validate_embedding_vector_dim` | function | Validates 'options.embedding_vector_dim' if present, returning an error unless the dimension is within the inclusive range '1..=8192'. [crates/gwiki/src/commands/setup.rs:246-253] |
| `standalone_error` | function | Converts an 'anyhow::Error' into 'WikiError::Config' by formatting it into the detail string '"standalone gwiki setup failed: {error}"'. [crates/gwiki/src/commands/setup.rs:255-259] |
| `render` | function | Builds a 'setup' command outcome by packaging the given scope, status, object lists, and ownership into a JSON payload, formatting a short summary string with the scope and object count, and delegating to 'super::scoped_outcome'. [crates/gwiki/src/commands/setup.rs:261-287] |
| `setup_status` | function | Returns a static status string based on the first non-empty input category, yielding '"failed"' if any failures exist, otherwise '"created"' if any items were created, '"already_present"' if any were skipped, and '"ready"' if all three collections are empty. [crates/gwiki/src/commands/setup.rs:289-303] |

_Verified by 6 in-file unit tests._

