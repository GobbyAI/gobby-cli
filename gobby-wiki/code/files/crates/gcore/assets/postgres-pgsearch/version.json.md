---
title: crates/gcore/assets/postgres-pgsearch/version.json
type: code_file
provenance:
- file: crates/gcore/assets/postgres-pgsearch/version.json
  ranges:
  - 2-8
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/assets/postgres-pgsearch/version.json:2-8](crates/gcore/assets/postgres-pgsearch/version.json#L2-L8)

</details>

# crates/gcore/assets/postgres-pgsearch/version.json

Module: [[code/modules/crates/gcore/assets/postgres-pgsearch|crates/gcore/assets/postgres-pgsearch]]

## Purpose

This JSON file records the packaged `pg_search` release metadata for Postgres search assets: the version, the overall SHA-256 checksum, per-architecture checksums for `amd64` and `arm64`, and the target `postgres_major` version. The fields work together as a small manifest that lets the build or update logic identify the exact artifact to use and verify its integrity for each supported architecture.
[crates/gcore/assets/postgres-pgsearch/version.json:2]
[crates/gcore/assets/postgres-pgsearch/version.json:3]
[crates/gcore/assets/postgres-pgsearch/version.json:4-7]
[crates/gcore/assets/postgres-pgsearch/version.json:5]
[crates/gcore/assets/postgres-pgsearch/version.json:6]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `pg_search_version` | property | `"pg_search_version": "0.23.4",` | `pg_search_version [property]` | `17581f92-e7dd-5204-bf06-e074856e1e24` | 2-2 [crates/gcore/assets/postgres-pgsearch/version.json:2] | Indexed property `pg_search_version` in `crates/gcore/assets/postgres-pgsearch/version.json`. [crates/gcore/assets/postgres-pgsearch/version.json:2] |
| `pg_search_sha256` | property | `"pg_search_sha256": "6b042d61d156ca5fdcb1c417e291d90bffe3026848890be30bf6e578146b4676",` | `pg_search_sha256 [property]` | `285db167-531d-5f8d-bce7-fb83e7b6eec1` | 3-3 [crates/gcore/assets/postgres-pgsearch/version.json:3] | Indexed property `pg_search_sha256` in `crates/gcore/assets/postgres-pgsearch/version.json`. [crates/gcore/assets/postgres-pgsearch/version.json:3] |
| `pg_search_sha256_by_arch` | property | `"pg_search_sha256_by_arch": {` | `pg_search_sha256_by_arch [property]` | `639c4bb7-5d6b-5c42-97ae-a91ad5dd89e2` | 4-7 [crates/gcore/assets/postgres-pgsearch/version.json:4-7] | Indexed property `pg_search_sha256_by_arch` in `crates/gcore/assets/postgres-pgsearch/version.json`. [crates/gcore/assets/postgres-pgsearch/version.json:4-7] |
| `amd64` | property | `"amd64": "6b042d61d156ca5fdcb1c417e291d90bffe3026848890be30bf6e578146b4676",` | `amd64 [property]` | `f9a502f7-9ea0-511e-acbd-bcbca7e3d51c` | 5-5 [crates/gcore/assets/postgres-pgsearch/version.json:5] | Indexed property `amd64` in `crates/gcore/assets/postgres-pgsearch/version.json`. [crates/gcore/assets/postgres-pgsearch/version.json:5] |
| `arm64` | property | `"arm64": "5ad13a80b76c46590914e0c366bd8deaf807d5b352f5ad489876ec836d06d3d1"` | `arm64 [property]` | `ee9fce5b-6a4d-55a5-8041-72c6a34b2055` | 6-6 [crates/gcore/assets/postgres-pgsearch/version.json:6] | Indexed property `arm64` in `crates/gcore/assets/postgres-pgsearch/version.json`. [crates/gcore/assets/postgres-pgsearch/version.json:6] |
| `postgres_major` | property | `"postgres_major": "18"` | `postgres_major [property]` | `f8bb4329-ce0c-5c51-8419-610e3adaba84` | 8-8 [crates/gcore/assets/postgres-pgsearch/version.json:8] | Indexed property `postgres_major` in `crates/gcore/assets/postgres-pgsearch/version.json`. [crates/gcore/assets/postgres-pgsearch/version.json:8] |
