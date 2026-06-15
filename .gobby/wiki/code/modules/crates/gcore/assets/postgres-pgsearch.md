---
title: crates/gcore/assets/postgres-pgsearch
type: code_module
provenance:
- file: crates/gcore/assets/postgres-pgsearch/version.json
  ranges:
  - 2-8
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/assets/postgres-pgsearch

Parent: [[code/modules/crates/gcore/assets|crates/gcore/assets]]

## Overview

This module is a compact asset manifest for the packaged Postgres `pg_search` extension. Its single file records the extension release version, a top-level SHA-256 checksum, architecture-specific checksums, and the Postgres major version the asset targets, binding the packaged binary identity to `pg_search` version `0.23.4` and Postgres `18` (`crates/gcore/assets/postgres-pgsearch/version.json:2-9`).

The key flow is lookup and verification: consumers can select the correct artifact by architecture from `pg_search_sha256_by_arch`, using the `amd64` and `arm64` entries for platform-specific integrity checks, while the top-level `pg_search_sha256` mirrors the `amd64` checksum for the default or canonical artifact (`crates/gcore/assets/postgres-pgsearch/version.json:3-7`). There are no child modules, so collaboration is limited to this manifest supplying stable metadata that higher-level packaging or deployment code can read to choose a compatible `pg_search` build for Postgres 18 (`crates/gcore/assets/postgres-pgsearch/version.json:8`).
[crates/gcore/assets/postgres-pgsearch/version.json:2]
[crates/gcore/assets/postgres-pgsearch/version.json:3]
[crates/gcore/assets/postgres-pgsearch/version.json:4-7]
[crates/gcore/assets/postgres-pgsearch/version.json:5]
[crates/gcore/assets/postgres-pgsearch/version.json:6]

## Files

- [[code/files/crates/gcore/assets/postgres-pgsearch/version.json|crates/gcore/assets/postgres-pgsearch/version.json]] - This JSON file records the packaged `pg_search` release metadata for the Postgres pgsearch asset: the version, its SHA-256 checksum, per-architecture checksums for `amd64` and `arm64`, and the target `postgres_major` version. The fields work together as a small manifest used to identify and verify the correct binary/artifact for each architecture.
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

