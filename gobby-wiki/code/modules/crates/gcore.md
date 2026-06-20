---
title: crates/gcore
type: code_module
provenance:
- file: crates/gcore/assets/docker-compose.services.yml
- file: crates/gcore/src/ai/embeddings.rs
- file: crates/gcore/src/ai/mod.rs
- file: crates/gcore/src/ai/probe.rs
- file: crates/gcore/src/ai/transcription.rs
- file: crates/gcore/src/ai/vision.rs
- file: crates/gcore/src/ai_context.rs
- file: crates/gcore/src/ai_types.rs
- file: crates/gcore/src/bootstrap.rs
- file: crates/gcore/src/cli_contract.rs
- file: crates/gcore/src/config/resolve.rs
- file: crates/gcore/src/config/tests.rs
- file: crates/gcore/src/config/types.rs
- file: crates/gcore/src/daemon_url.rs
- file: crates/gcore/src/degradation.rs
- file: crates/gcore/src/falkor.rs
- file: crates/gcore/src/graph_analytics.rs
- file: crates/gcore/src/graph_analytics/leiden.rs
- file: crates/gcore/src/indexing.rs
- file: crates/gcore/src/postgres.rs
- file: crates/gcore/src/provisioning/bootstrap.rs
- file: crates/gcore/src/provisioning/docker.rs
- file: crates/gcore/src/provisioning/hub.rs
- file: crates/gcore/src/provisioning/mod.rs
- file: crates/gcore/src/provisioning/tests.rs
- file: crates/gcore/src/qdrant.rs
- file: crates/gcore/src/qdrant/tests.rs
- file: crates/gcore/src/search.rs
- file: crates/gcore/src/secrets.rs
- file: crates/gcore/src/setup.rs
provenance_truncated: 16
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore

Parent: [[code/modules/crates|crates]]

## Overview

`crates/gcore` is Gobby’s shared core layer: it centralizes AI routing and result types, configuration resolution, storage clients, indexing/search primitives, graph analytics, setup/degradation contracts, and local service provisioning. Its `src` child keeps service configuration behind a lightweight shared surface, covering FalkorDB, Qdrant, embeddings, indexing, AI routing, capability bindings, tuning, and feature candidates, while leaving consumer-owned choices such as graph and collection names outside the shared config layer (`crates/gcore/src/config/mod.rs:1-17`, `crates/gcore/src/config/types.rs:1-30`).

The module’s main flows connect configuration to runtime capabilities. AI callers resolve bindings through context and config sources, probe daemon availability, choose daemon/direct/off routing, and then call transport helpers for text, embeddings, audio, and vision. Storage flows expose PostgreSQL connection/schema helpers, Falkor graph querying and analytics, Qdrant collection/search/upsert handling, and search result merging. Provisioning flows prepare Docker service assets, write standalone/bootstrap configuration, bring services up, and health-check PostgreSQL, Qdrant, and FalkorDB.

`crates/gcore/assets` supplies the local service stack consumed by the provisioning path. Its Compose asset declares that services are “installed via: gobby install” and managed by daemon start/stop using Docker Compose profiles (`crates/gcore/assets/docker-compose.services.yml:1-3`). The stack provides FalkorDB, Qdrant, and PostgreSQL profiles with persistent named volumes, health checks, restart policy, and configurable host ports (`crates/gcore/assets/docker-compose.services.yml:5-46`).

| Area | Public symbols |
| --- | --- |
| AI routing/client | `AiContext`, `AiBindings`, `AiLimiter`, `AiTransport`, `generate_text`, `generate_text_with_max_tokens`, `transcribe`, `describe_image`, `embed_one`, `embed_batch` |
| AI capability probing | `CapabilityProbeReport`, `CapabilityAvailability`, `probe_daemon_capability`, `probe_daemon_capabilities`, `capability_status_route` |
| Config | `ConfigSource`, `LayeredConfigSource`, `EnvOnlySource`, `StandaloneConfig`, `resolve_falkordb_config`, `resolve_qdrant_config`, `resolve_embedding_config`, `resolve_indexing_config` |
| Provisioning | `DockerServiceOptions`, `ServiceAssetReport`, `DockerProvisioningReport`, `prepare_service_assets`, `provision_docker_services`, `ensure_hub` |
| Storage/search | `GraphClient`, `ReadOnlySyncGraph`, `with_graph`, `with_qdrant`, `ensure_collection`, `search`, `upsert_batched`, `rrf_merge` |
| Setup/degradation | `CliContract`, `DegradationContract`, `ServiceState`, `SetupIssue`, `Guidance`, `ValidationReport`, `RuntimeValidator` |

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcore/assets\|crates/gcore/assets]] | `crates/gcore/assets` packages local service assets for Gobby. Its main Compose asset defines service dependencies “installed via: gobby install” and managed by daemon start/stop through Docker Compose profiles (`crates/gcore/assets/docker-compose.services.yml:1-3`). It provides FalkorDB, Qdrant, and PostgreSQL profiles, each with persistent named volumes, health checks, restart policy, and configurable host ports (`crates/gcore/assets/docker-compose.services.yml:5-46`). |
| [[code/modules/crates/gcore/src\|crates/gcore/src]] | `crates/gcore/src` is the shared core layer for Gobby Rust crates: it centralizes AI routing/types, configuration resolution, storage clients, indexing/search primitives, graph analytics, setup/degradation contracts, and local provisioning. Configuration stays behind a lightweight shared surface, with service config types for FalkorDB, Qdrant, embeddings, indexing, AI routing, AI capability bindings, tuning, and feature candidates, while consumer-owned choices such as graph and collection names remain outside the shared config layer (`crates/gcore/src/config/mod.rs:1-17`,… |

