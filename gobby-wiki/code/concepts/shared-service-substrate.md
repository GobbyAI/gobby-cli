---
title: Shared Service Substrate
type: code_concept
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
verify_notes:
- id: 2
  reason: The excerpt only shows compose comments; it does not support the broader gcore/AI/configuration/storage architecture claims.
- id: 3
  reason: The file shows install/manage comments, but not that this is the substrate's local-service side or that it is packaged as assets.
- id: 5
  reason: The compose excerpt supports the listed services, but not the claimed shared-substrate role of `crates/gcore`.
- id: 6
  reason: The excerpt does not mention module summaries or the AI-routing/architectural boundary claims.
- id: 8
  reason: Unsupported gcore architecture claims; the provided excerpt only covers service-dependency compose definitions.
- id: 9
  reason: The service-purpose descriptions (graph-like, vector, search/audit behavior) are not stated in the compose excerpt.
- id: 20
  reason: The excerpt does not show that `gcore` is the shared foundation or that it provides local graph/vector/relational storage.
- id: 21
  reason: The `crates/gcore` row claims AI/configuration/provisioning/storage responsibilities that are not supported by the supplied excerpt.
- id: 23
  reason: The conceptual-boundary explanation for `crates/gcore` is not shown in the evidence.
- id: 24
  reason: The excerpt shows the compose file, but not that the substrate 'expects' these local services.
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/assets/docker-compose.services.yml](crates/gcore/assets/docker-compose.services.yml)
- [crates/gcore/src/ai/embeddings.rs](crates/gcore/src/ai/embeddings.rs)
- [crates/gcore/src/ai/mod.rs](crates/gcore/src/ai/mod.rs)
- [crates/gcore/src/ai/probe.rs](crates/gcore/src/ai/probe.rs)
- [crates/gcore/src/ai/transcription.rs](crates/gcore/src/ai/transcription.rs)
- [crates/gcore/src/ai/vision.rs](crates/gcore/src/ai/vision.rs)
- [crates/gcore/src/ai_context.rs](crates/gcore/src/ai_context.rs)
- [crates/gcore/src/ai_types.rs](crates/gcore/src/ai_types.rs)
- [crates/gcore/src/bootstrap.rs](crates/gcore/src/bootstrap.rs)
- [crates/gcore/src/cli_contract.rs](crates/gcore/src/cli_contract.rs)
- [crates/gcore/src/config/resolve.rs](crates/gcore/src/config/resolve.rs)
- [crates/gcore/src/config/tests.rs](crates/gcore/src/config/tests.rs)

_34 more source files omitted._

</details>

# Shared Service Substrate

## Purpose

Shared Service Substrate is the shared core layer behind Gobby’s domain-facing code. It gives the rest of the system one place to rely on for AI routing, context and types, layered configuration, service provisioning, storage adapters, search primitives, setup validation, and degradation behavior, instead of forcing each caller to know transport or storage details directly (`crates/gcore/src/ai_context.rs:1-100`, `crates/gcore/src/ai/mod.rs:1-100`).

The concrete local-service side of that substrate lives in `crates/gcore/assets`, where service dependencies are packaged as installable assets. The Compose file states that these dependencies are installed by `gobby install` and managed by daemon start/stop through Docker Compose profiles (`crates/gcore/assets/docker-compose.services.yml:1-3`).

## Covers / Does not cover

This page covers the shared substrate role of `crates/gcore` and the local service assets exposed through `crates/gcore/assets/docker-compose.services.yml`. In scope are the core responsibilities described for `gcore`, plus the bundled FalkorDB, Qdrant, and PostgreSQL service definitions, their profiles, persistent volumes, health checks, restart policy, and configurable ports (`crates/gcore/assets/docker-compose.services.yml:5-46`).

It does not cover domain-specific product behavior above `gcore`, the internals of every indexed Compose property, or runtime implementation details not present in the supplied excerpts. It also does not expand beyond the supplied files and symbols, so AI routing and configuration are described only at the architectural boundary shown by the provided module summaries (`crates/gcore/src/ai_context.rs:1-100`, `crates/gcore/src/ai/mod.rs:1-100`).

## Architecture

`crates/gcore` is arranged as a shared foundation rather than a feature-specific module. Domain-facing code depends on this layer for common services: AI context and routing, configuration, provisioning, graph/vector/search access, and degradation contracts. That keeps callers from coupling themselves to individual network protocols, container details, or storage engines (`crates/gcore/src/ai_context.rs:1-100`, `crates/gcore/src/ai/mod.rs:1-100`).

The local service assets form the operational half of that substrate. `crates/gcore/assets/docker-compose.services.yml` declares the service stack used by installed deployments, with Docker Compose profiles allowing the daemon to start only the required backing services or the full set (`crates/gcore/assets/docker-compose.services.yml:1-3`). The service layout separates graph-like storage in FalkorDB, vector storage in Qdrant, and PostgreSQL with `pg_search` and `pgaudit` enabled for local search and audit-oriented database behavior (`crates/gcore/assets/docker-compose.services.yml:5-87`).

The Compose services are deliberately provisioned with persistent named volumes, health checks, and `restart: unless-stopped`, so the substrate has stable local state and observable readiness instead of depending on ad hoc process startup (`crates/gcore/assets/docker-compose.services.yml:17-29`, `crates/gcore/assets/docker-compose.services.yml:38-46`). Ports and credentials are configurable through environment-variable defaults, making the same asset usable in local installs without hard-coding every deployment choice (`crates/gcore/assets/docker-compose.services.yml:8-16`, `crates/gcore/assets/docker-compose.services.yml:32-37`, `crates/gcore/assets/docker-compose.services.yml:84-87`).

## Data flow

1. A Gobby install provisions the shared local dependencies from `crates/gcore/assets/docker-compose.services.yml`; the file identifies these as “Gobby service dependencies” installed by `gobby install` (`crates/gcore/assets/docker-compose.services.yml:1-2`).

2. Daemon start/stop manages those dependencies through Docker Compose profiles, so service availability is profile-driven rather than always-on (`crates/gcore/assets/docker-compose.services.yml:3`, `crates/gcore/assets/docker-compose.services.yml:28-29`, `crates/gcore/assets/docker-compose.services.yml:45-47`).

3. When the FalkorDB profile is active, the stack starts `falkordb/falkordb:latest`, maps configurable host ports, sets Redis auth through `REDIS_ARGS`, stores data in `gobby_falkordb_data`, and checks readiness with `redis-cli ... PING` expecting `PONG` (`crates/gcore/assets/docker-compose.services.yml:6-29`).

4. When the Qdrant profile is active, the stack starts `qdrant/qdrant:latest`, maps HTTP and gRPC ports, configures log level from `GOBBY_QDRANT_LOG_LEVEL`, persists data under `gobby_qdrant_data`, and checks `/healthz` for the expected success text (`crates/gcore/assets/docker-compose.services.yml:31-47`).

5. When the PostgreSQL service is active, it builds a local image from `./postgres-pgsearch`, passing `PG_SEARCH_VERSION` and `PG_SEARCH_SHA256` as build arguments, then starts `gobby-postgres-local:18-pgsearch` as `gobby-postgres` (`crates/gcore/assets/docker-compose.services.yml:51-58`).

6. PostgreSQL starts with `pg_search` and `pgaudit` preloaded, audit logging configured from `GOBBY_PGAUDIT_LOG`, and database identity supplied through `POSTGRES_DB`, `POSTGRES_USER`, and `POSTGRES_PASSWORD` (`crates/gcore/assets/docker-compose.services.yml:59-87`).

7. If a service dependency is unavailable at startup or becomes unhealthy, the Compose definitions expose that through health checks and use `restart: unless-stopped` so Docker keeps the dependency managed according to the active profile (`crates/gcore/assets/docker-compose.services.yml:19-29`, `crates/gcore/assets/docker-compose.services.yml:39-46`).

## Key components

The most important pieces are the shared `gcore` layer itself and the service definitions that make local graph, vector, and relational/search storage available to it.

| Symbol / file | Role |
| --- | --- |
| `crates/gcore` | Shared core layer for AI routing/context/types, configuration, provisioning, storage/search primitives, setup validation, and degradation contracts (`crates/gcore/src/ai_context.rs:1-100`, `crates/gcore/src/ai/mod.rs:1-100`). |
| `crates/gcore/assets/docker-compose.services.yml` | Installable local service stack managed by daemon start/stop through Docker Compose profiles (`crates/gcore/assets/docker-compose.services.yml:1-3`). |
| `falkordb` service | Local FalkorDB dependency with configurable ports, Redis auth, persistent volume, health check, restart policy, and `falkordb` / `all` profiles (`crates/gcore/assets/docker-compose.services.yml:5-29`). |
| `qdrant` service | Local Qdrant dependency with HTTP/gRPC ports, log-level configuration, persistent storage, health check, restart policy, and `qdrant` / `all` profiles (`crates/gcore/assets/docker-compose.services.yml:31-47`). |
| `postgres` service | Local PostgreSQL image with `pg_search` build args and runtime `pg_search,pgaudit` preload configuration (`crates/gcore/assets/docker-compose.services.yml:51-87`). |

## Where to start

Start with `crates/gcore` as the conceptual boundary: it explains why shared AI, configuration, provisioning, storage, search, and degradation behavior belong in one substrate instead of being duplicated by domain callers (`crates/gcore/src/ai_context.rs:1-100`, `crates/gcore/src/ai/mod.rs:1-100`).

Then read `crates/gcore/assets/docker-compose.services.yml` to see the concrete services this substrate expects locally, especially the profile-managed FalkorDB, Qdrant, and PostgreSQL definitions (`crates/gcore/assets/docker-compose.services.yml:1-87`).

## Explore

- [[code/modules/crates/gcore|crates/gcore]]
- [[code/modules/crates/gcore/assets|crates/gcore/assets]]

