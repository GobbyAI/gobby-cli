---
title: crates/gcore/assets
type: code_module
provenance:
- file: crates/gcore/assets/docker-compose.services.yml
  ranges:
  - 5-117
  - 6-28
  - '7'
  - 8-10
  - 11-16
  - 17-18
  - 19-26
  - 21-23
  - '24'
  - '25'
  - '26'
  - '27'
  - '28'
  - 30-49
  - '31'
  - 32-34
  - 35-38
  - 39-40
  - 41-45
  - '42'
  - '43'
  - '44'
  - '45'
  - '46'
  - 47-49
  - 51-117
  - 52-56
  - '53'
  - 54-56
  - '55'
  - '56'
  - '57'
  - '58'
  - 59-82
  - 83-87
  - '84'
  - '85'
  - '86'
  - '87'
  - 88-89
  - 90-92
  - 93-113
  - 94-110
  - '111'
  - '112'
  - '113'
  - '114'
  - 115-117
  - 119-128
  - 120-121
  - '121'
  - 122-123
  - '123'
  - 124-125
  - '125'
  - 126-128
  - '127'
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

# crates/gcore/assets

Parent: [[code/modules/crates/gcore|crates/gcore]]

## Overview

This module provides containerized infrastructure assets for the gcore crate. The `docker-compose.services.yml` defines the backing services for the Gobby stack—FalkorDB (graph), Qdrant (vector search), and PostgreSQL—each configured with images, ports, volumes, environment variables, healthchecks, restart policies, and profiles, plus named persistent volumes. The accompanying `postgres-pgsearch` child module packages a custom PostgreSQL image bundling the `pg_search` full-text search and `pgaudit` audit-logging extensions, with version and per-architecture SHA256 build arguments.
[crates/gcore/assets/docker-compose.services.yml:5-117]
[crates/gcore/assets/postgres-pgsearch/version.json:2]
[crates/gcore/assets/docker-compose.services.yml:6-28]
[crates/gcore/assets/docker-compose.services.yml:7]
[crates/gcore/assets/docker-compose.services.yml:8-10]

## Child Modules

- [[code/modules/crates/gcore/assets/postgres-pgsearch|crates/gcore/assets/postgres-pgsearch]] - This module packages a custom PostgreSQL container image with the `pg_search` (full-text search) and `pgaudit` (audit logging) extensions for the gcore crate.

A Dockerfile defines the image build, while `version.json` pins extension versions and per-architecture (amd64/arm64) SHA256 checksums alongside the target PostgreSQL major version. The `initdb.d` directory holds ordered SQL scripts that enable the required extensions on database startup, and the `scripts` directory provides `pg_audit_export.sh` for exporting audit data.
[crates/gcore/assets/postgres-pgsearch/version.json:2]
[crates/gcore/assets/postgres-pgsearch/version.json:3]
[crates/gcore/assets/postgres-pgsearch/version.json:4-7]
[crates/gcore/assets/postgres-pgsearch/version.json:5]
[crates/gcore/assets/postgres-pgsearch/version.json:6]

## Files

- [[code/files/crates/gcore/assets/docker-compose.services.yml|crates/gcore/assets/docker-compose.services.yml]] - `crates/gcore/assets/docker-compose.services.yml` exposes 57 indexed API symbols.
[crates/gcore/assets/docker-compose.services.yml:5-117]
[crates/gcore/assets/docker-compose.services.yml:6-28]
[crates/gcore/assets/docker-compose.services.yml:7]
[crates/gcore/assets/docker-compose.services.yml:8-10]
[crates/gcore/assets/docker-compose.services.yml:11-16]

## Components

- `591e4361-5db2-5f0c-922e-3fc17b8a0992`
- `8060bf8a-009e-510d-a92e-2414ef58fee9`
- `0ec81f31-b1bd-5fd3-a5dc-df0048a6cf04`
- `e5e8281a-5074-5ab4-a173-8b0061be39c0`
- `2e970e6d-aeb2-5338-9656-ea9da8c17209`
- `3a6c487e-a23c-53e1-8485-fd39120f9f8c`
- `ac1cb913-f9bd-5a46-8d1d-e8179a54fba0`
- `dfa0baf7-1895-5c9e-a2e7-3e00224f40c5`
- `25136f51-692a-5741-ab29-4c28b7d41fd5`
- `71631f91-ce85-558b-97ed-d206043e8c43`
- `f2cd6e50-9249-5d8c-bace-bf9f9b6efa74`
- `eabd17d7-01df-523b-a9de-de4d7e061518`
- `6f734415-ad4b-59cb-a679-b7098a150c07`
- `aaa98d08-01b0-58a7-9914-f5ecb4008772`
- `e64c3f3e-8873-5d83-ba15-885eda52bb3c`
- `e363d09d-ba01-58d2-b24d-025d1d78a3a7`
- `8f061858-1bbf-5aee-8317-7872aea29d82`
- `3533eb39-72ad-5fa7-b3bc-2991f0fe7702`
- `0dfefab0-a488-5d49-b63a-6371927d8cd1`
- `58d0ad72-9f33-5425-a131-4036300e06ac`
- `1937d982-be22-5131-9d30-4c9521d19049`
- `caec3d67-8d20-50c1-b7d3-42a81e9c9fdc`
- `65f0c110-1164-5bb6-9e18-dceda58bb5ae`
- `4cf7dd10-d55a-5505-8c15-2181b63f1c39`
- `950b901b-1e15-5ff5-b5f7-d0246b41a10e`
- `aa7fa767-3f9c-5987-b78c-5828aa2ce570`
- `b11ff9b0-d225-5134-a210-e50d3f7fbaa9`
- `5f6b234a-7f4a-5568-acce-93c88ab53c55`
- `6f0bfa87-de13-5ba9-984c-a13b9b333edb`
- `b9c73405-ea2f-55ea-9606-1769f2a21ca7`
- `559072d8-376a-5dbc-be18-88dc0070ed8a`
- `a731605a-ef10-5f25-a180-5ebbcaaa1151`
- `ca8649e4-5e48-5f1f-a550-4403b005d889`
- `683c70af-f961-5b6e-9a16-6b4beae8d68e`
- `606c0eae-93d0-5497-aedf-8bdddefc0733`
- `0784a3df-b47e-564a-b2f7-0470d4e7a3b3`
- `071bd758-4848-505d-8fb3-acc39810af60`
- `990e0119-a144-5b12-8db0-3eebeee0da20`
- `7b6d7e3d-be6c-5b72-805b-ccf370f728e5`
- `23d164da-b584-5c84-a7d8-8d37cea87b8b`
- `f9855082-a3a2-5eb2-bf07-2e6de0bfb613`
- `582781f7-6818-5dba-8912-5e4d5f853ba2`
- `d6748349-1adb-53d1-8645-4026726ea6b2`
- `22bb68ed-6f43-550c-bfac-d4f6273fed95`
- `455e568d-a625-52cc-8d0d-9917b9e75857`
- `e78dd862-9429-5383-9b4c-68b264e6ebaa`
- `8dc8e30b-6df9-5d1d-ba43-60a28dc03600`
- `6359ef78-ad73-5281-ab3b-6341a749a6f1`
- `64153251-c5bd-59c7-b6eb-defc1369fdcd`
- `4d2cee14-286f-566c-9c85-9c96a283e16a`
- `abc8afa0-7ef9-518e-ae76-84800c614485`
- `5e6428e3-951c-5c9a-95ac-0b3c40d4c322`
- `dcb576b4-a5af-5983-96e9-a80472f4c65b`
- `27f328c9-6b58-561c-a919-a5cce2486667`
- `500f6f15-fce0-5878-ba8d-10ebbbdb5071`
- `69cc6e92-3262-5da5-9494-733e42d29757`
- `72678802-facf-508b-892a-07eb709831db`
- `17581f92-e7dd-5204-bf06-e074856e1e24`
- `285db167-531d-5f8d-bce7-fb83e7b6eec1`
- `639c4bb7-5d6b-5c42-97ae-a91ad5dd89e2`
- `f9a502f7-9ea0-511e-acbd-bcbca7e3d51c`
- `ee9fce5b-6a4d-55a5-8041-72c6a34b2055`
- `f8bb4329-ce0c-5c51-8419-610e3adaba84`

