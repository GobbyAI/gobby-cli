---
title: Service Infrastructure
type: code_concept
provenance:
- file: crates/gcore/assets/docker-compose.services.yml
- file: crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh
- file: crates/gcore/assets/postgres-pgsearch/version.json
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/assets/docker-compose.services.yml](crates/gcore/assets/docker-compose.services.yml)
- [crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh](crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh)
- [crates/gcore/assets/postgres-pgsearch/version.json](crates/gcore/assets/postgres-pgsearch/version.json)

</details>

# Service Infrastructure

## Purpose

Service Infrastructure is the set of Docker Compose definitions and build artifacts that describe the backing services the platform depends on at runtime. Rather than requiring an engineer to install and configure PostgreSQL, Qdrant, and FalkorDB by hand, this concept packages those services as declarative container definitions so the platform can provision them and health-check them consistently across environments [crates/gcore/assets/docker-compose.services.yml:5-117].

The problem it solves is reproducible local and deployable service setup: a single Compose definition captures which services run, how they are built or pulled, and how the platform confirms each one is ready before depending on it.

## Covers / Does not cover

This page covers the Compose-based declaration of the three backing services bundled in `crates/gcore/assets`: PostgreSQL (with the `pg_search` extension), Qdrant, and FalkorDB, along with the build artifacts and health-check wiring those definitions express [crates/gcore/assets/docker-compose.services.yml:5-117].

It does not cover the application-side code that connects to these services, the provisioning/orchestration logic that invokes Compose, or service-specific query and indexing APIs — none of those appear in the supplied input. Because no indexed symbols or additional source excerpts were provided, internal connection clients, configuration loaders, and runtime callers are out of scope here.

## Architecture

The infrastructure is arranged as a single Compose asset living alongside the `gcore` crate, in its `assets` module [crates/gcore/assets/docker-compose.services.yml:5-117]. Keeping the service definitions as a versioned asset inside the crate means the backing-service topology travels with the code that needs it, so the platform always provisions a matching set of services rather than relying on an externally managed environment.

The Compose file groups three independent services — PostgreSQL (with `pg_search`), Qdrant, and FalkorDB — under one definition. They are co-located in one file because the platform treats them as a single provisioning unit: brought up together and individually health-checked. The `pg_search` requirement is the reason PostgreSQL is expressed as a build artifact rather than a stock image pull, since the search extension must be present in the running database. Health-check declarations are embedded per service so the provisioning step can wait for readiness before the rest of the platform proceeds.

## Data flow

The supplied input shows the declarative definition rather than the executing orchestrator, so the runtime flow below is traced at the level the evidence supports [crates/gcore/assets/docker-compose.services.yml:5-117]:

1. The platform reads the Compose service definition from the `gcore` assets module [crates/gcore/assets/docker-compose.services.yml:5-117].
2. It provisions the three backing services described there — PostgreSQL (with `pg_search`), Qdrant, and FalkorDB — building or pulling each as the definition specifies.
3. For PostgreSQL, the build artifact ensures the `pg_search` extension is available before the database is considered usable.
4. The platform applies the per-service health checks declared in the file to confirm each service is ready.
5. If a service's health check does not pass — i.e. a dependency is unavailable — the provisioning step continues to wait/fail on that service rather than letting dependent components proceed against an unready backing service, as the embedded health-check wiring is what gates readiness [crates/gcore/assets/docker-compose.services.yml:5-117].

## Key components

The only component exposed by the supplied input is the Compose asset itself; treat the table below as the single authoritative entry rather than an exhaustive map of the services.

| Component | Kind | Role |
| --- | --- | --- |
| `crates/gcore/assets` (docker-compose.services.yml) | Compose asset / module | Declares and health-checks the backing services — PostgreSQL with `pg_search`, Qdrant, and FalkorDB — that the platform provisions [crates/gcore/assets/docker-compose.services.yml:5-117] |

## Where to start

Start by reading the Compose definition directly at [crates/gcore/assets/docker-compose.services.yml:5-117]. It is the single source of truth for which backing services exist, how PostgreSQL is built to include `pg_search`, and how each service's health check is declared — everything else about this concept follows from that file.

## Explore

- [[code/modules/crates/gcore/assets|crates/gcore/assets]]

