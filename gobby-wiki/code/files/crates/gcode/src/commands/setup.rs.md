---
title: crates/gcode/src/commands/setup.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/setup.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/setup.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

`crates/gcode/src/commands/setup.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gcode/src/commands/setup.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `run` | function | Validates a standalone setup request, provisions or connects to the required Docker/Postgres services, optionally clears overwrite projections, runs the standalone gcode setup, emits failures in the requested format and aborts on error, then writes the gcore config and records service and embedding status in the returned setup report. [crates/gcode/src/commands/setup.rs:23-95] |
| `OverwriteProjectionConfigs` | class | 'OverwriteProjectionConfigs' is a configuration override struct containing optional 'FalkorConfig' and 'QdrantConfig' fields for selectively replacing projection backend settings. [crates/gcode/src/commands/setup.rs:97-100] |
| `clear_overwrite_projections` | function | Clears any existing overwrite-related projections by resolving projection configs for the given setup and, if present, wiping the FalkorDB code index and deleting Qdrant code-symbol collections with the configured prefix. [crates/gcode/src/commands/setup.rs:102-118] |
| `overwrite_projection_configs` | function | Loads the standalone config from 'home', applies Docker-provisioned defaults when 'service_report' is present and then overrides them with any request-specified FalkorDB/Qdrant fields, resolves the final FalkorDB and Qdrant connection configs, and returns them as 'OverwriteProjectionConfigs'. [crates/gcode/src/commands/setup.rs:120-166] |
| `resolve_or_provision_database` | function | Returns the explicitly provided database URL if present, otherwise either resolves an existing database URL when services are disabled or builds 'EnsureHubOptions' from 'home' and 'service_options' (including any currently resolvable database URL) and delegates to 'ensure_hub', yielding the chosen database URL plus an optional provisioning report. [crates/gcode/src/commands/setup.rs:168-187] |
| `apply_service_overrides` | function | Overrides 'service_options' with any provided FalkorDB host, port, and password values from 'request', leaving unspecified fields unchanged. [crates/gcode/src/commands/setup.rs:189-202] |
| `connect_postgres_with_retry` | function | Attempts to establish a read-write PostgreSQL client connection via 'gobby_core::postgres::connect_readwrite', retrying up to 30 times with 2-second delays when 'retry' is true, and otherwise returning the first error wrapped with context if all attempts fail. [crates/gcode/src/commands/setup.rs:204-220] |
| `write_gcore_config` | function | Loads or creates the standalone gcore config at 'gcore_config_path(home)', populates it with the Postgres DSN plus either provisioned Docker service endpoints or explicit request overrides, applies optional embedding provider settings, and returns the config file path. [crates/gcode/src/commands/setup.rs:222-288] |
| `remove_embedding_keys` | function | Removes the embedding-related configuration entries 'AI_PROVIDER', 'AI_API_BASE', 'AI_MODEL', 'AI_DIM', 'AI_QUERY_PREFIX', and 'AI_API_KEY' from the given 'StandaloneConfig' by calling 'config.remove' on each key. [crates/gcode/src/commands/setup.rs:290-301] |
| `service_configured_compose_file` | function | Returns the configured compose file path as a string if 'compose_file_path(home)' exists on disk, otherwise 'None'. [crates/gcode/src/commands/setup.rs:303-306] |
| `resolve_embedding_bootstrap` | function | 'resolve_embedding_bootstrap' selects an 'EmbeddingBootstrap' configuration from 'StandaloneSetupRequest' by honoring an explicit 'embedding_provider' (or inferring LM Studio/Ollama from reachable defaults or explicit embedding fields), applying request overrides for base URL, model, query prefix, vector dimension, and API key, rejecting unsupported providers or nonpositive vector dimensions, and returning 'Ok(None)' when the provider is 'none'. [crates/gcode/src/commands/setup.rs:308-356] |
| `explicit_embedding_bootstrap` | function | Validates that 'embedding_api_base' is present, then constructs and returns an 'EmbeddingBootstrap' for the 'openai-compatible' provider using the request’s embedding model, vector dimension, query prefix, and API key, falling back to the default Ollama model and default embedding dimension when unspecified. [crates/gcode/src/commands/setup.rs:358-377] |
| `endpoint_reachable` | function | Returns 'true' if 'api_base' parses as a URL with a resolvable host and port and at least one resulting socket address accepts a TCP connection within 150 ms, otherwise 'false'. [crates/gcode/src/commands/setup.rs:379-395] |
| `standalone_command_installs_public_code_index_subset` | function | Creates a temporary GOBBY_HOME, runs standalone setup against the test Postgres database with code-index installation enabled, asserts that 'public.code_symbols' is created while 'public.config_store' is not, verifies 'gcore.yaml' was written, and then drops the code-index test objects and clears the env var. [crates/gcode/src/commands/setup.rs:573-610] |

_Verified by 4 in-file unit tests._

