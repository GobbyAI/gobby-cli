---
title: crates/gcore/assets/postgres-pgsearch
type: code_module
provenance:
- file: crates/gcore/assets/postgres-pgsearch/version.json
  ranges:
  - '2'
  - '3'
  - 4-7
  - '5'
  - '6'
  - '8'
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/assets/postgres-pgsearch

Parent: [[code/modules/crates/gcore/assets|crates/gcore/assets]]

## Overview

This module provides PostgreSQL infrastructure and configuration assets for the pg_search and pgaudit extensions. It includes a Dockerfile, version metadata tracking build checksums and architecture-specific variants, initialization SQL scripts for extension bootstrapping, and shell scripts for audit data export management. The module contains no application-level APIs, serving exclusively as setup and operational tooling for PostgreSQL environments.
[crates/gcore/assets/postgres-pgsearch/version.json:2]
[crates/gcore/assets/postgres-pgsearch/version.json:3]
[crates/gcore/assets/postgres-pgsearch/version.json:4-7]
[crates/gcore/assets/postgres-pgsearch/version.json:5]
[crates/gcore/assets/postgres-pgsearch/version.json:6]
[crates/gcore/assets/postgres-pgsearch/version.json:8]

## Child Modules

- [[code/modules/crates/gcore/assets/postgres-pgsearch/initdb.d|crates/gcore/assets/postgres-pgsearch/initdb.d]] - This module contains PostgreSQL initialization SQL scripts for configuring the pg_search and pgaudit extensions. It consists of two sequential database setup files that execute during bootstrapping. The module contains no application-level APIs, stable components, or nested submodules.
- [[code/modules/crates/gcore/assets/postgres-pgsearch/scripts|crates/gcore/assets/postgres-pgsearch/scripts]] - This module provides shell scripts for PostgreSQL database operations, specifically managing audit data export. It contains the pg_audit_export.sh script and does not expose indexed API symbols or child modules.

## Files

- [[code/files/crates/gcore/assets/postgres-pgsearch/Dockerfile|crates/gcore/assets/postgres-pgsearch/Dockerfile]] - `crates/gcore/assets/postgres-pgsearch/Dockerfile` has no indexed API symbols.
- [[code/files/crates/gcore/assets/postgres-pgsearch/version.json|crates/gcore/assets/postgres-pgsearch/version.json]] - `crates/gcore/assets/postgres-pgsearch/version.json` exposes 6 indexed API symbols.
[crates/gcore/assets/postgres-pgsearch/version.json:2]
[crates/gcore/assets/postgres-pgsearch/version.json:3]
[crates/gcore/assets/postgres-pgsearch/version.json:4-7]
[crates/gcore/assets/postgres-pgsearch/version.json:5]
[crates/gcore/assets/postgres-pgsearch/version.json:6]
[crates/gcore/assets/postgres-pgsearch/version.json:8]

## Components

- `17581f92-e7dd-5204-bf06-e074856e1e24`
- `285db167-531d-5f8d-bce7-fb83e7b6eec1`
- `639c4bb7-5d6b-5c42-97ae-a91ad5dd89e2`
- `f9a502f7-9ea0-511e-acbd-bcbca7e3d51c`
- `ee9fce5b-6a4d-55a5-8041-72c6a34b2055`
- `f8bb4329-ce0c-5c51-8419-610e3adaba84`

