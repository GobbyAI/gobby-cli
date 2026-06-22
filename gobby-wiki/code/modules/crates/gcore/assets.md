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

## Module: crates/gcore/assets

This module is the infrastructure-as-code layer for the Gobby platform's local development and daemon-managed service dependencies. Its primary artifact is `docker-compose.services.yml`, which declares three containerised backing services — FalkorDB (graph/Redis), Qdrant (vector store), and a custom-built PostgreSQL instance with `pg_search` and `pgaudit` extensions — together with the named volumes that persist their data across container restarts. The file is installed via the `gobby install` command and is consumed by the daemon's start/stop lifecycle through Docker Compose profiles, as documented in the file header at `docker-compose.services.yml:1-4`.

The `postgres` service differs from the other two in that it is not pulled from a public image directly; instead it is built from the `./postgres-pgsearch` child module context (`docker-compose.services.yml:52-56`), which supplies a parameterised Dockerfile keyed on `PG_SEARCH_VERSION` and `PG_SEARCH_SHA256`. The resulting image is tagged `gobby-postgres-local:18-pgsearch` and started with an explicit `command` block that loads `pg_search` and `pgaudit` as shared preload libraries and routes audit logs to `/var/log/pgaudit` (`docker-compose.services.yml:57-74`). Shell utility functions registered in the component table (`usage`, `die_usage`, `require_value`, `parse_epoch`, `timestamp_epoch`, `audit_line_epoch`, `emit_windowed_audit_lines`) suggest a companion script — likely inside `postgres-pgsearch` — for post-processing pgaudit log windows.

All three services declare `restart: unless-stopped` and liveness `healthcheck` blocks so the daemon can gate dependent application startup on actual service readiness. Profile guards (`falkordb`, `qdrant`, `all`; `postgres` is always-on) let operators bring up only the subset of services their workload requires (`docker-compose.services.yml:26`, `48-50`).

### Services

| Service | Image / Build | Default Ports | Profile(s) |
|---|---|---|---|
| `falkordb` | `falkordb/falkordb:latest` | `16379→6379`, `13000→3000` | `falkordb`, `all` |
| `qdrant` | `qdrant/qdrant:latest` | `6333→6333` (HTTP), `6334→6334` (gRPC) | `qdrant`, `all` |
| `postgres` | Built from `./postgres-pgsearch` | `5432` (default) | _(always active)_ |

### Environment Variables

| Variable | Service | Default | Purpose |
|---|---|---|---|
| `GOBBY_FALKORDB_PORT` | falkordb | `16379` | Host-side Redis port |
| `GOBBY_FALKORDB_BROWSER_PORT` | falkordb | `13000` | Host-side browser UI port |
| `GOBBY_FALKORDB_PASSWORD` | falkordb | `gobbyfalkor` | Redis AUTH password (`REDIS_ARGS`) |
| `GOBBY_QDRANT_HTTP_PORT` | qdrant | `6333` | Qdrant REST API host port |
| `GOBBY_QDRANT_GRPC_PORT` | qdrant | `6334` | Qdrant gRPC host port |
| `GOBBY_QDRANT_LOG_LEVEL` | qdrant | `WARN` | Qdrant log verbosity |
| `GOBBY_PG_SEARCH_VERSION` | postgres (build arg) | `0.23.4` | `pg_search` extension version |
| `GOBBY_PG_SEARCH_SHA256` | postgres (build arg) | _(required)_ | SHA-256 checksum for `pg_search` package |
| `POSTGRES_DB` | postgres | — | Initial database name |
| `POSTGRES_USER` | postgres | — | Superuser name |
| `POSTGRES_PASSWORD` | postgres | — | Superuser password |
| `GOBBY_PGAUDIT_LOG` | postgres | `ddl` | pgaudit log level (`pgaudit.log`) |

### Named Volumes

| Volume | Purpose |
|---|---|
| `gobby_falkordb_data` | FalkorDB graph/RDB persistence (`/data`) |
| `gobby_qdrant_data` | Qdrant vector storage (`/qdrant/storage`) |
| `gobby_postgres_data` | PostgreSQL data directory |
| `gobby_pgaudit_log` | pgaudit structured log output (`/var/log/pgaudit`) |

### Build Arguments (postgres-pgsearch child module)

| Arg | Component ID | Notes |
|---|---|---|
| `PG_SEARCH_VERSION` | `b9c73405` | Forwarded from `GOBBY_PG_SEARCH_VERSION` |
| `PG_SEARCH_SHA256` | `559072d8` | Per-architecture checksums via `pg_search_sha256_by_arch` (`amd64`, `arm64`) |
| `postgres_major` | `f8bb4329` | Major PostgreSQL version baked into the base image tag |
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:10-17]
[crates/gcore/assets/docker-compose.services.yml:5-117]
[crates/gcore/assets/postgres-pgsearch/version.json:2]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:19-23]
[crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh:25-36]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcore/assets/postgres-pgsearch\|crates/gcore/assets/postgres-pgsearch]] | ## Module: crates/gcore/assets/postgres-pgsearch |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/assets/docker-compose.services.yml\|crates/gcore/assets/docker-compose.services.yml]] | `crates/gcore/assets/docker-compose.services.yml` exposes 57 indexed API symbols. |

