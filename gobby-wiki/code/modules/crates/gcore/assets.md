---
title: crates/gcore/assets
type: code_module
provenance:
- file: crates/gcore/assets/docker-compose.services.yml
- file: crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh
- file: crates/gcore/assets/postgres-pgsearch/version.json
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/assets

Parent: [[code/modules/crates/gcore|crates/gcore]]

## Overview

`crates/gcore/assets` packages local service assets for Gobby. Its main Compose asset defines service dependencies “installed via: gobby install” and managed by daemon start/stop through Docker Compose profiles (`crates/gcore/assets/docker-compose.services.yml:1-3`). It provides FalkorDB, Qdrant, and PostgreSQL profiles, each with persistent named volumes, health checks, restart policy, and configurable host ports (`crates/gcore/assets/docker-compose.services.yml:5-46`).

The PostgreSQL path collaborates with the `postgres-pgsearch` child module: Compose builds from `./postgres-pgsearch`, passes pg_search version/checksum build args, and starts Postgres with `pg_search` plus `pgaudit` preloaded (`crates/gcore/assets/docker-compose.services.yml:48-70`). The child manifest pins pg_search `0.23.4`, records SHA-256 values including per-architecture hashes, and targets PostgreSQL major version `18` (`crates/gcore/assets/postgres-pgsearch/version.json:1-10`).

| Service | Role | Profile(s) | Key integration |
| --- | --- | --- | --- |
| `falkordb` | Graph/Redis-compatible dependency | `falkordb`, `all` | Uses `falkordb/falkordb:latest`, Redis auth via `REDIS_ARGS`, and a Redis `PING` healthcheck (`crates/gcore/assets/docker-compose.services.yml:6-27`) |
| `qdrant` | Vector database dependency | `qdrant`, `all` | Uses `qdrant/qdrant:latest`, local unauthenticated HTTP/gRPC ports, and `/healthz` probing (`crates/gcore/assets/docker-compose.services.yml:29-46`) |
| `postgres` | Local PostgreSQL with pg_search and audit logging | implied by service definition | Builds from `postgres-pgsearch` and enables `pg_search,pgaudit` at startup (`crates/gcore/assets/docker-compose.services.yml:48-70`) |

| Configuration | Default / Value | Used by |
| --- | --- | --- |
| `GOBBY_FALKORDB_PORT` | `16379` | FalkorDB Redis port mapping (`crates/gcore/assets/docker-compose.services.yml:8`) |
| `GOBBY_FALKORDB_BROWSER_PORT` | `13000` | FalkorDB browser port mapping (`crates/gcore/assets/docker-compose.services.yml:9`) |
| `GOBBY_FALKORDB_PASSWORD` | `gobbyfalkor` | Redis auth and healthcheck password (`crates/gcore/assets/docker-compose.services.yml:13-16`) |
| `GOBBY_QDRANT_HTTP_PORT` | `6333` | Qdrant HTTP port mapping (`crates/gcore/assets/docker-compose.services.yml:31`) |
| `GOBBY_QDRANT_GRPC_PORT` | `6334` | Qdrant gRPC port mapping (`crates/gcore/assets/docker-compose.services.yml:32`) |
| `GOBBY_QDRANT_LOG_LEVEL` | `WARN` | Qdrant log level (`crates/gcore/assets/docker-compose.services.yml:36`) |
| `GOBBY_PG_SEARCH_VERSION` | `0.23.4` | PostgreSQL build arg (`crates/gcore/assets/docker-compose.services.yml:52`) |
| `GOBBY_PG_SEARCH_SHA256` | unset | PostgreSQL build arg checksum override (`crates/gcore/assets/docker-compose.services.yml:53`) |
| `GOBBY_PGAUDIT_LOG` | `ddl` | PostgreSQL `pgaudit.log` setting (`crates/gcore/assets/docker-compose.services.yml:62-63`) |

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcore/assets/postgres-pgsearch\|crates/gcore/assets/postgres-pgsearch]] | This module packages pg_search asset metadata and supporting PostgreSQL audit-log export tooling. The version manifest pins pg_search `0.23.4`, records SHA-256 checksums, includes per-architecture hashes, and targets PostgreSQL major version `18` (`crates/gcore/assets/postgres-pgsearch/version.json:1-10`). |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/assets/docker-compose.services.yml\|crates/gcore/assets/docker-compose.services.yml]] | `crates/gcore/assets/docker-compose.services.yml` exposes 57 indexed API symbols. |

