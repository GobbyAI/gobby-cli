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

`crates/gcore/src/provisioning` owns standalone bootstrap plus local Docker service provisioning: it mirrors daemon service assets, copies them under `~/.gobby/services`, starts daemon-style profiles, and persists bootstrap keys in `gcore.yaml` (`crates/gcore/src/provisioning/mod.rs:1-7`). The module root centralizes service filenames, default database/vector/AI endpoint settings, and embedded Docker/Postgres asset templates (`crates/gcore/src/provisioning/mod.rs:14-52`).

The Docker path is option-driven: `DockerServiceOptions` carries home, Postgres, Qdrant, and FalkorDB settings, with helpers to derive the Postgres DSN and Qdrant URL (`crates/gcore/src/provisioning/docker.rs:9-37`). Provisioning returns asset/run reports and uses an injectable `CommandRunner`; production execution goes through `RealCommandRunner`, which builds a `std::process::Command` from the supplied command spec (`crates/gcore/src/provisioning/docker.rs:39-100`).

Hub resolution sits above Docker provisioning. `EnsureHubOptions` combines `gobby_home`, Docker options, candidate database URLs, and a `provision_services` switch (`crates/gcore/src/provisioning/hub.rs:3-17`). `ensure_hub` reads environment, checks Postgres reachability, probes hub identity, and provisions Docker services when needed (`crates/gcore/src/provisioning/hub.rs:47-54`); tests can inject environment, reachability, identity, and provisioning callbacks through the internal variants (`crates/gcore/src/provisioning/hub.rs:56-75`). The module collaborates with `crate::config` for AI key names, capability binding, env-pattern resolution, and test locking, and with `crate::degradation::CoreError` for error reporting (`crates/gcore/src/provisioning/mod.rs:9-12`, `crates/gcore/src/provisioning/tests.rs:1-3`).

| Public area | Symbols |
| --- | --- |
| Bootstrap | `EmbeddingBootstrap`, `TextGenerationBootstrap`, `apply_text_generation_bootstrap`, `write_standalone_bootstrap`, `default_text_model` |
| Docker provisioning | `DockerServiceOptions`, `DockerProvisioningReport`, `ServiceAssetReport`, `provision_docker_services`, `prepare_service_assets`, `docker_compose_up_spec` |
| Command/health injection | `CommandSpec`, `CommandOutput`, `CommandRunner`, `RealCommandRunner`, `DockerHealthChecker`, `TcpDockerHealthChecker` |
| YAML helpers | `flatten_yaml_value`, `yaml_path`, `scalar_to_string`, `flatten` |
| Hub orchestration | `EnsureHubOptions`, `HubIdentity`, `ensure_hub` |

| Default/config fact | Value or role | Source |
| --- | --- | --- |
| Config filename | `gcore.yaml` | `crates/gcore/src/provisioning/mod.rs:14` |
| Services directory | `services` | `crates/gcore/src/provisioning/mod.rs:15` |
| Compose filename | `docker-compose.yml` | `crates/gcore/src/provisioning/mod.rs:16` |
| Postgres defaults | host `127.0.0.1`, port `60891`, db/user `gobby`, password `gobby_dev` | `crates/gcore/src/provisioning/mod.rs:18-22` |
| FalkorDB defaults | host `127.0.0.1`, port `16379`, browser `13000`, password `gobbyfalkor` | `crates/gcore/src/provisioning/mod.rs:24-27` |
| Qdrant defaults | host `127.0.0.1`, HTTP `6333`, gRPC `6334` | `crates/gcore/src/provisioning/mod.rs:29-31` |
| AI defaults | LM Studio and Ollama API bases/models, embedding dimension `768` | `crates/gcore/src/provisioning/mod.rs:33-43` |
| Test-cleared env vars | `GOBBY_FALKORDB_HOST`, `GOBBY_FALKORDB_PORT`, `GOBBY_FALKORDB_PASSWORD`, `GOBBY_POSTGRES_DSN`, `GOBBY_QDRANT_URL`, `GOBBY_QDRANT_API_KEY` | `crates/gcore/src/provisioning/tests.rs:17-28` |
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

