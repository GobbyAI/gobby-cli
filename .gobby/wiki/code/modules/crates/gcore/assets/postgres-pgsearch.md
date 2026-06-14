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

This module is a single asset manifest for the bundled `postgres-pgsearch` dependency. Its responsibility is to pin the pg_search release version and integrity hashes used by build or packaging code, with `pg_search_version` fixed at `0.23.4` and a default `pg_search_sha256` for artifact verification. It also records the target PostgreSQL major version as `18`, tying the asset to the expected database runtime compatibility range.  [crates/gcore/assets/postgres-pgsearch/version.json:8]

The key flow is artifact selection followed by checksum validation. Consumers can use the top-level checksum as the default value, or select an architecture-specific checksum from `pg_search_sha256_by_arch`, which currently differentiates `amd64` and `arm64` artifacts. This keeps the version pin, platform-specific binary verification data, and PostgreSQL compatibility target together in one compact manifest, with no child modules involved. [crates/gcore/assets/postgres-pgsearch/version.json:4-7]

## Files

- [[code/files/crates/gcore/assets/postgres-pgsearch/version.json|crates/gcore/assets/postgres-pgsearch/version.json]] - This file is a version manifest for the `postgres-pgsearch` asset. It records the `pg_search_version`, a default `pg_search_sha256`, architecture-specific SHA-256 values for `amd64` and `arm64`, and the target `postgres_major` version so the build or packaging logic can select and verify the correct binary artifact.
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

