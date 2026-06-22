---
title: crates/gcore/src/provisioning
type: code_module
provenance:
- file: crates/gcore/src/provisioning/bootstrap.rs
- file: crates/gcore/src/provisioning/docker.rs
- file: crates/gcore/src/provisioning/hub.rs
- file: crates/gcore/src/provisioning/mod.rs
- file: crates/gcore/src/provisioning/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/provisioning

Parent: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

## crates/gcore/src/provisioning

This module is the central runtime provisioning layer for the Gobby core library, responsible for two tightly coupled concerns: writing and reading the standalone `gcore.yaml` bootstrap configuration, and spinning up (or verifying) the full Docker services stack that backs a running instance. The module root (`mod.rs`) declares all shared constants, embeds static asset files at compile time via `include_str!`, and re-exports the three sub-files through `pub mod` declarations. Embedded assets include the Docker Compose template, a custom `postgres-pgsearch` Dockerfile, version metadata, and SQL init scripts, making the binary self-contained for first-time provisioning (`mod.rs:44-55`).

`bootstrap.rs` owns the YAML configuration contract. `EmbeddingBootstrap` offers two factory methods — `lm_studio` and `ollama` — that produce a fully-populated key/value map for the `gcore.yaml` file, covering embedding provider, API base URL, model name, vector dimension, and shared API key. `TextGenerationBootstrap` can be derived from an embedding config (`from_embedding`) or a raw endpoint (`from_endpoint`), injecting text-generation routing, API base, model, and API key fields. The `apply_text_generation_bootstrap` function merges these defaults without overwriting values already present in the config, and `write_standalone_bootstrap` serialises the result to disk. YAML keys use a dotted-path notation; `flatten_yaml_value` / `flatten_yaml_value_at_depth` parse nested and flat YAML into a uniform `BTreeMap<String, String>`, with `yaml_path` and `scalar_to_string` handling traversal and type coercion. Tests in `tests.rs` validate collision detection, excessive nesting rejection, sequence scalars, tagged scalars, and dotted-prefix resolution (`tests.rs:1-100`).

`docker.rs` implements service orchestration. `DockerServiceOptions` holds port bindings and connection defaults for PostgreSQL, Qdrant, and FalkorDB; its `database_url` and `qdrant_url` helpers produce ready-to-use connection strings. `provision_docker_services` and `provision_docker_services_with` copy bundled assets into `~/.gobby/services`, write an `.env` file via `update_env_file`, invoke `docker compose up` through the `CommandRunner` trait abstraction, and return a `DockerProvisioningReport`. `TcpDockerHealthChecker` (the default `DockerHealthChecker` impl) polls each service over raw TCP with `wait_for_tcp` / `wait_for` until the service accepts connections, performing dedicated waits for Postgres, Qdrant, and FalkorDB (`docker.rs:1-100`). `RealCommandRunner` delegates directly to `std::process::Command`, while tests use `RecordingRunner` and `RecordingHealth` to capture invocations without side effects.

`hub.rs` provides the idempotent `ensure_hub` entry point, which resolves the authoritative database URL by checking candidate URLs from environment variables, comparing live `HubIdentity` probes (system identifier + database name), and provisioning Docker services only when necessary. The enum `RecordedHubIdentityStatus` (`SingleReachable`, `VerifiedSameHub`, `IdentityUnknownInsufficientPrivilege`) drives conflict detection: divergent hub identities surface an error, insufficient privilege preserves the recorded hub rather than replacing it, and an already-reachable hub skips re-provisioning entirely (`tests.rs`: `divergent_hubs_surface_conflict`, `no_double_provision_when_reachable`, `insufficient_identity_privilege_preserves_hub`).

---

### Module-level constants (`mod.rs`)

| Constant | Value | Purpose |
|---|---|---|
| `GCORE_CONFIG_FILENAME` | `"gcore.yaml"` | Standalone config file name |
| `SERVICES_DIRNAME` | `"services"` | Subdirectory under `~/.gobby` |
| `COMPOSE_FILENAME` | `"docker-compose.yml"` | Compose file written on provision |
| `DEFAULT_POSTGRES_PORT` | `60891` | Local Postgres port |
| `DEFAULT_POSTGRES_DB/USER/PASSWORD` | `gobby` / `gobby` / `gobby_dev` | Postgres defaults |
| `DEFAULT_FALKORDB_PORT` | `16379` | FalkorDB Redis port |
| `DEFAULT_FALKORDB_BROWSER_PORT` | `13000` | FalkorDB browser UI |
| `DEFAULT_FALKORDB_PASSWORD` | `"gobbyfalkor"` | FalkorDB auth |
| `DEFAULT_QDRANT_HTTP_PORT` | `6333` | Qdrant REST port |
| `DEFAULT_QDRANT_GRPC_PORT` | `6334` | Qdrant gRPC port |
| `DEFAULT_LM_STUDIO_API_BASE` | `http://localhost:1234/v1` | LM Studio endpoint |
| `DEFAULT_LM_STUDIO_MODEL` | `text-embedding-nomic-embed-text-v1.5@f16` | Embedding model |
| `DEFAULT_LM_STUDIO_TEXT_MODEL` | `qwen2.5-vl-7b-instruct` | Text-gen model |
| `DEFAULT_OLLAMA_API_BASE` | `http://localhost:11434/v1` | Ollama endpoint |
| `DEFAULT_OLLAMA_MODEL` | `nomic-embed-text` | Ollama embedding model |
| `DEFAULT_OLLAMA_TEXT_MODEL` | `qwen3-coder` | Ollama text-gen model |
| `DEFAULT_EMBEDDING_VECTOR_DIM` | `768` | Vector dimension |

---

### Public API surface

| Symbol | Kind | File | Description |
|---|---|---|---|
| `EmbeddingBootstrap` | struct | `bootstrap.rs` | Factory for embedding config key/value sets |
| `EmbeddingBootstrap::lm_studio` | method | `bootstrap.rs` | LM Studio embedding bootstrap |
| `EmbeddingBootstrap::ollama` | method | `bootstrap.rs` | Ollama embedding bootstrap |
| `TextGenerationBootstrap` | struct | `bootstrap.rs` | Factory for text-gen config key/value sets |
| `TextGenerationBootstrap::from_embedding` | method | `bootstrap.rs` | Derive text-gen settings from embedding config |
| `TextGenerationBootstrap::from_endpoint` | method | `bootstrap.rs` | Build text-gen settings from raw endpoint |
| `apply_text_generation_bootstrap` | fn | `bootstrap.rs` | Merge text-gen defaults without overwriting |
| `write_standalone_bootstrap` | fn | `bootstrap.rs` | Serialise bootstrap map to `gcore.yaml` |
| `flatten_yaml_value` | fn | `bootstrap.rs` | Parse nested/flat YAML into `BTreeMap` |
| `DockerServiceOptions` | struct | `docker.rs` | Port bindings and connection parameters |
| `DockerServiceOptions::database_url` | method | `docker.rs` | Compute Postgres connection string |
| `DockerServiceOptions::qdrant_url` | method | `docker.rs` | Compute Qdrant HTTP URL |
| `provision_docker_services` | fn | `docker.rs` | Top-level provisioning entry point |
| `provision_docker_services_with` | fn | `docker.rs` | Injectable provisioning (for testing) |
| `prepare_service_assets` | fn | `docker.rs` | Copy bundled assets to `~/.gobby/services` |
| `CommandRunner` | trait | `docker.rs` | Abstraction over process execution |
| `RealCommandRunner` | struct | `docker.rs` | Production `CommandRunner` implementation |
| `TcpDockerHealthChecker` | struct | `docker.rs` | TCP-polling health checks for all services |
| `DockerProvisioningReport` | struct | `docker.rs` | Result of a provisioning run |
| `ensure_hub` | fn | `hub.rs` | Idempotent hub resolution + optional provisioning |
| `EnsureHubOptions` | struct | `hub.rs` | Parameters for hub resolution |
| `HubIdentity` | struct | `hub.rs` | Postgres system identifier + database name |
| `HubIdentityProbeResult` | enum | `hub.rs` | `Known` or `UnknownInsufficientPrivilege` |
| `RecordedHubResolution` | struct | `hub.rs` | Resolved URL + identity status |

---

### Environment variables consumed (test guard covers these, `tests.rs:22-32`)

| Variable | Service |
|---|---|
| `GOBBY_POSTGRES_DSN` | PostgreSQL connection string override |
| `GOBBY_FALKORDB_HOST` | FalkorDB host override |
| `GOBBY_FALKORDB_PORT` | FalkorDB port override |
| `GOBBY_FALKORDB_PASSWORD` | FalkorDB password override |
| `GOBBY_QDRANT_URL` | Qdrant URL override |
| `GOBBY_QDRANT_API_KEY` | Qdrant API key override |
[crates/gcore/src/provisioning/bootstrap.rs:8-15]
[crates/gcore/src/provisioning/docker.rs:9-18]
[crates/gcore/src/provisioning/hub.rs:4-9]
[crates/gcore/src/provisioning/mod.rs:55-57]
[crates/gcore/src/provisioning/tests.rs:5-7]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/src/provisioning/bootstrap.rs\|crates/gcore/src/provisioning/bootstrap.rs]] | `crates/gcore/src/provisioning/bootstrap.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcore/src/provisioning/docker.rs\|crates/gcore/src/provisioning/docker.rs]] | `crates/gcore/src/provisioning/docker.rs` exposes 30 indexed API symbols. |
| [[code/files/crates/gcore/src/provisioning/hub.rs\|crates/gcore/src/provisioning/hub.rs]] | `crates/gcore/src/provisioning/hub.rs` exposes 26 indexed API symbols. |
| [[code/files/crates/gcore/src/provisioning/mod.rs\|crates/gcore/src/provisioning/mod.rs]] | `crates/gcore/src/provisioning/mod.rs` exposes 19 indexed API symbols. |
| [[code/files/crates/gcore/src/provisioning/tests.rs\|crates/gcore/src/provisioning/tests.rs]] | `crates/gcore/src/provisioning/tests.rs` exposes 34 indexed API symbols. |

