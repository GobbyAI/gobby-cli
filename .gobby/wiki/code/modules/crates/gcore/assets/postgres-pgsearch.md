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

This module packages a custom PostgreSQL container image with the `pg_search` (full-text search) and `pgaudit` (audit logging) extensions for the gcore crate.

A Dockerfile defines the image build, while `version.json` pins extension versions and per-architecture (amd64/arm64) SHA256 checksums alongside the target PostgreSQL major version. The `initdb.d` directory holds ordered SQL scripts that enable the required extensions on database startup, and the `scripts` directory provides `pg_audit_export.sh` for exporting audit data.
[crates/gcore/assets/postgres-pgsearch/version.json:2]
[crates/gcore/assets/postgres-pgsearch/version.json:3]
[crates/gcore/assets/postgres-pgsearch/version.json:4-7]
[crates/gcore/assets/postgres-pgsearch/version.json:5]
[crates/gcore/assets/postgres-pgsearch/version.json:6]

## Child Modules

- [[code/modules/crates/gcore/assets/postgres-pgsearch/initdb.d|crates/gcore/assets/postgres-pgsearch/initdb.d]] - PostgreSQL initialization scripts for the pgsearch container. Contains ordered SQL files that run on database startup to enable required extensions: `pg_search` (full-text search) and `pgaudit` (audit logging). 
- [[code/modules/crates/gcore/assets/postgres-pgsearch/scripts|crates/gcore/assets/postgres-pgsearch/scripts]] - This module provides a shell script (`pg_audit_export.sh`) for exporting PostgreSQL audit data, supporting the postgres-pgsearch asset configuration within the gcore crate. The script contains no indexed API symbols. 

## Files

- [[code/files/crates/gcore/assets/postgres-pgsearch/Dockerfile|crates/gcore/assets/postgres-pgsearch/Dockerfile]] - `crates/gcore/assets/postgres-pgsearch/Dockerfile` has no indexed API symbols. 
- [[code/files/crates/gcore/assets/postgres-pgsearch/version.json|crates/gcore/assets/postgres-pgsearch/version.json]] - `crates/gcore/assets/postgres-pgsearch/version.json` exposes 6 indexed API symbols.
[crates/gcore/assets/postgres-pgsearch/version.json:2]
[crates/gcore/assets/postgres-pgsearch/version.json:3]
[crates/gcore/assets/postgres-pgsearch/version.json:4-7]
[crates/gcore/assets/postgres-pgsearch/version.json:5]
[crates/gcore/assets/postgres-pgsearch/version.json:6]

## Components

- `17581f92-e7dd-5204-bf06-e074856e1e24`
- `285db167-531d-5f8d-bce7-fb83e7b6eec1`
- `639c4bb7-5d6b-5c42-97ae-a91ad5dd89e2`
- `f9a502f7-9ea0-511e-acbd-bcbca7e3d51c`
- `ee9fce5b-6a4d-55a5-8041-72c6a34b2055`
- `f8bb4329-ce0c-5c51-8419-610e3adaba84`

