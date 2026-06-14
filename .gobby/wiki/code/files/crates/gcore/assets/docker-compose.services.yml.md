---
title: crates/gcore/assets/docker-compose.services.yml
type: code_file
provenance:
- file: crates/gcore/assets/docker-compose.services.yml
  ranges:
  - 5-117
  - 119-128
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/assets/docker-compose.services.yml

Module: [[code/modules/crates/gcore/assets|crates/gcore/assets]]

## Purpose

This file defines the Docker Compose service bundle for Gobby’s local dependencies and persistence. It wires up three services: `falkordb` for Redis-compatible storage, `qdrant` for vector search, and `postgres` for the main database with pg_search/pgaudit support. Each service is configured with ports, environment variables, volumes, restart policy, and healthchecks so the daemon can start and stop them reliably through Compose profiles, while the bottom `volumes` section declares the named data volumes used to persist each service’s state.
[crates/gcore/assets/docker-compose.services.yml:5-117]
[crates/gcore/assets/docker-compose.services.yml:6-28]
[crates/gcore/assets/docker-compose.services.yml:7]
[crates/gcore/assets/docker-compose.services.yml:8-10]
[crates/gcore/assets/docker-compose.services.yml:11-16]

## API Symbols

- `services` (property) component `services [property]` (`591e4361-5db2-5f0c-922e-3fc17b8a0992`) lines 5-117 [crates/gcore/assets/docker-compose.services.yml:5-117]
  - Signature: `services:`
  - Purpose: Indexed property `services` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:5-117]
- `falkordb` (property) component `falkordb [property]` (`8060bf8a-009e-510d-a92e-2414ef58fee9`) lines 6-28 [crates/gcore/assets/docker-compose.services.yml:6-28]
  - Signature: `falkordb:`
  - Purpose: Indexed property `falkordb` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:6-28]
- `image` (property) component `image [property]` (`0ec81f31-b1bd-5fd3-a5dc-df0048a6cf04`) lines 7-7 [crates/gcore/assets/docker-compose.services.yml:7]
  - Signature: `image: falkordb/falkordb:latest`
  - Purpose: Indexed property `image` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:7]
- `ports` (property) component `ports [property]` (`e5e8281a-5074-5ab4-a173-8b0061be39c0`) lines 8-10 [crates/gcore/assets/docker-compose.services.yml:8-10]
  - Signature: `ports:`
  - Purpose: Indexed property `ports` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:8-10]
- `environment` (property) component `environment [property]` (`2e970e6d-aeb2-5338-9656-ea9da8c17209`) lines 11-16 [crates/gcore/assets/docker-compose.services.yml:11-16]
  - Signature: `environment:`
  - Purpose: Indexed property `environment` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:11-16]
- `volumes` (property) component `volumes [property]` (`3a6c487e-a23c-53e1-8485-fd39120f9f8c`) lines 17-18 [crates/gcore/assets/docker-compose.services.yml:17-18]
  - Signature: `volumes:`
  - Purpose: Indexed property `volumes` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:17-18]
- `healthcheck` (property) component `healthcheck [property]` (`ac1cb913-f9bd-5a46-8d1d-e8179a54fba0`) lines 19-26 [crates/gcore/assets/docker-compose.services.yml:19-26]
  - Signature: `healthcheck:`
  - Purpose: Indexed property `healthcheck` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:19-26]
- `test` (property) component `test [property]` (`dfa0baf7-1895-5c9e-a2e7-3e00224f40c5`) lines 21-23 [crates/gcore/assets/docker-compose.services.yml:21-23]
  - Signature: `test:`
  - Purpose: Indexed property `test` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:21-23]
- `interval` (property) component `interval [property]` (`25136f51-692a-5741-ab29-4c28b7d41fd5`) lines 24-24 [crates/gcore/assets/docker-compose.services.yml:24]
  - Signature: `interval: 10s`
  - Purpose: Indexed property `interval` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:24]
- `timeout` (property) component `timeout [property]` (`71631f91-ce85-558b-97ed-d206043e8c43`) lines 25-25 [crates/gcore/assets/docker-compose.services.yml:25]
  - Signature: `timeout: 5s`
  - Purpose: Indexed property `timeout` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:25]
- `retries` (property) component `retries [property]` (`f2cd6e50-9249-5d8c-bace-bf9f9b6efa74`) lines 26-26 [crates/gcore/assets/docker-compose.services.yml:26]
  - Signature: `retries: 5`
  - Purpose: Indexed property `retries` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:26]
- `restart` (property) component `restart [property]` (`eabd17d7-01df-523b-a9de-de4d7e061518`) lines 27-27 [crates/gcore/assets/docker-compose.services.yml:27]
  - Signature: `restart: unless-stopped`
  - Purpose: Indexed property `restart` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:27]
- `profiles` (property) component `profiles [property]` (`6f734415-ad4b-59cb-a679-b7098a150c07`) lines 28-28 [crates/gcore/assets/docker-compose.services.yml:28]
  - Signature: `profiles: [falkordb, all]`
  - Purpose: Indexed property `profiles` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:28]
- `qdrant` (property) component `qdrant [property]` (`aaa98d08-01b0-58a7-9914-f5ecb4008772`) lines 30-49 [crates/gcore/assets/docker-compose.services.yml:30-49]
  - Signature: `qdrant:`
  - Purpose: Indexed property `qdrant` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:30-49]
- `image` (property) component `image [property]` (`e64c3f3e-8873-5d83-ba15-885eda52bb3c`) lines 31-31 [crates/gcore/assets/docker-compose.services.yml:31]
  - Signature: `image: qdrant/qdrant:latest`
  - Purpose: Indexed property `image` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:31]
- `ports` (property) component `ports [property]` (`e363d09d-ba01-58d2-b24d-025d1d78a3a7`) lines 32-34 [crates/gcore/assets/docker-compose.services.yml:32-34]
  - Signature: `ports:`
  - Purpose: Indexed property `ports` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:32-34]
- `environment` (property) component `environment [property]` (`8f061858-1bbf-5aee-8317-7872aea29d82`) lines 35-38 [crates/gcore/assets/docker-compose.services.yml:35-38]
  - Signature: `environment:`
  - Purpose: Indexed property `environment` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:35-38]
- `volumes` (property) component `volumes [property]` (`3533eb39-72ad-5fa7-b3bc-2991f0fe7702`) lines 39-40 [crates/gcore/assets/docker-compose.services.yml:39-40]
  - Signature: `volumes:`
  - Purpose: Indexed property `volumes` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:39-40]
- `healthcheck` (property) component `healthcheck [property]` (`0dfefab0-a488-5d49-b63a-6371927d8cd1`) lines 41-45 [crates/gcore/assets/docker-compose.services.yml:41-45]
  - Signature: `healthcheck:`
  - Purpose: Indexed property `healthcheck` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:41-45]
- `test` (property) component `test [property]` (`58d0ad72-9f33-5425-a131-4036300e06ac`) lines 42-42 [crates/gcore/assets/docker-compose.services.yml:42]
  - Signature: `test: ["CMD-SHELL", "bash -c 'exec 3<>/dev/tcp/localhost/6333 && printf \"GET /healthz HTTP/1.0\\r\\nHost: localhost\\r\\n\\r\\n\" >&3 && grep -q \"healthz check passed\" <&3'"]`
  - Purpose: Indexed property `test` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:42]
- `interval` (property) component `interval [property]` (`1937d982-be22-5131-9d30-4c9521d19049`) lines 43-43 [crates/gcore/assets/docker-compose.services.yml:43]
  - Signature: `interval: 10s`
  - Purpose: Indexed property `interval` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:43]
- `timeout` (property) component `timeout [property]` (`caec3d67-8d20-50c1-b7d3-42a81e9c9fdc`) lines 44-44 [crates/gcore/assets/docker-compose.services.yml:44]
  - Signature: `timeout: 5s`
  - Purpose: Indexed property `timeout` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:44]
- `retries` (property) component `retries [property]` (`65f0c110-1164-5bb6-9e18-dceda58bb5ae`) lines 45-45 [crates/gcore/assets/docker-compose.services.yml:45]
  - Signature: `retries: 5`
  - Purpose: Indexed property `retries` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:45]
- `restart` (property) component `restart [property]` (`4cf7dd10-d55a-5505-8c15-2181b63f1c39`) lines 46-46 [crates/gcore/assets/docker-compose.services.yml:46]
  - Signature: `restart: unless-stopped`
  - Purpose: Indexed property `restart` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:46]
- `profiles` (property) component `profiles [property]` (`950b901b-1e15-5ff5-b5f7-d0246b41a10e`) lines 47-49 [crates/gcore/assets/docker-compose.services.yml:47-49]
  - Signature: `profiles:`
  - Purpose: Indexed property `profiles` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:47-49]
- `postgres` (property) component `postgres [property]` (`aa7fa767-3f9c-5987-b78c-5828aa2ce570`) lines 51-117 [crates/gcore/assets/docker-compose.services.yml:51-117]
  - Signature: `postgres:`
  - Purpose: Indexed property `postgres` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:51-117]
- `build` (property) component `build [property]` (`b11ff9b0-d225-5134-a210-e50d3f7fbaa9`) lines 52-56 [crates/gcore/assets/docker-compose.services.yml:52-56]
  - Signature: `build:`
  - Purpose: Indexed property `build` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:52-56]
- `context` (property) component `context [property]` (`5f6b234a-7f4a-5568-acce-93c88ab53c55`) lines 53-53 [crates/gcore/assets/docker-compose.services.yml:53]
  - Signature: `context: ./postgres-pgsearch`
  - Purpose: Indexed property `context` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:53]
- `args` (property) component `args [property]` (`6f0bfa87-de13-5ba9-984c-a13b9b333edb`) lines 54-56 [crates/gcore/assets/docker-compose.services.yml:54-56]
  - Signature: `args:`
  - Purpose: Indexed property `args` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:54-56]
- `PG_SEARCH_VERSION` (property) component `PG_SEARCH_VERSION [property]` (`b9c73405-ea2f-55ea-9606-1769f2a21ca7`) lines 55-55 [crates/gcore/assets/docker-compose.services.yml:55]
  - Signature: `PG_SEARCH_VERSION: ${GOBBY_PG_SEARCH_VERSION:-0.23.4}`
  - Purpose: Indexed property `PG_SEARCH_VERSION` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:55]
- `PG_SEARCH_SHA256` (property) component `PG_SEARCH_SHA256 [property]` (`559072d8-376a-5dbc-be18-88dc0070ed8a`) lines 56-56 [crates/gcore/assets/docker-compose.services.yml:56]
  - Signature: `PG_SEARCH_SHA256: ${GOBBY_PG_SEARCH_SHA256}`
  - Purpose: Indexed property `PG_SEARCH_SHA256` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:56]
- `image` (property) component `image [property]` (`a731605a-ef10-5f25-a180-5ebbcaaa1151`) lines 57-57 [crates/gcore/assets/docker-compose.services.yml:57]
  - Signature: `image: gobby-postgres-local:18-pgsearch`
  - Purpose: Indexed property `image` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:57]
- `container_name` (property) component `container_name [property]` (`ca8649e4-5e48-5f1f-a550-4403b005d889`) lines 58-58 [crates/gcore/assets/docker-compose.services.yml:58]
  - Signature: `container_name: gobby-postgres`
  - Purpose: Indexed property `container_name` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:58]
- `command` (property) component `command [property]` (`683c70af-f961-5b6e-9a16-6b4beae8d68e`) lines 59-82 [crates/gcore/assets/docker-compose.services.yml:59-82]
  - Signature: `command:`
  - Purpose: Indexed property `command` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:59-82]
- `environment` (property) component `environment [property]` (`606c0eae-93d0-5497-aedf-8bdddefc0733`) lines 83-87 [crates/gcore/assets/docker-compose.services.yml:83-87]
  - Signature: `environment:`
  - Purpose: Indexed property `environment` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:83-87]
- `POSTGRES_DB` (property) component `POSTGRES_DB [property]` (`0784a3df-b47e-564a-b2f7-0470d4e7a3b3`) lines 84-84 [crates/gcore/assets/docker-compose.services.yml:84]
  - Signature: `POSTGRES_DB: ${GOBBY_POSTGRES_DB:-gobby}`
  - Purpose: Indexed property `POSTGRES_DB` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:84]
- `POSTGRES_USER` (property) component `POSTGRES_USER [property]` (`071bd758-4848-505d-8fb3-acc39810af60`) lines 85-85 [crates/gcore/assets/docker-compose.services.yml:85]
  - Signature: `POSTGRES_USER: ${GOBBY_POSTGRES_USER:-gobby}`
  - Purpose: Indexed property `POSTGRES_USER` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:85]
- `POSTGRES_PASSWORD` (property) component `POSTGRES_PASSWORD [property]` (`990e0119-a144-5b12-8db0-3eebeee0da20`) lines 86-86 [crates/gcore/assets/docker-compose.services.yml:86]
  - Signature: `POSTGRES_PASSWORD: ${GOBBY_POSTGRES_PASSWORD:-gobby_dev}`
  - Purpose: Indexed property `POSTGRES_PASSWORD` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:86]
- `GOBBY_PGAUDIT_LOG` (property) component `GOBBY_PGAUDIT_LOG [property]` (`7b6d7e3d-be6c-5b72-805b-ccf370f728e5`) lines 87-87 [crates/gcore/assets/docker-compose.services.yml:87]
  - Signature: `GOBBY_PGAUDIT_LOG: ${GOBBY_PGAUDIT_LOG:-ddl}`
  - Purpose: Indexed property `GOBBY_PGAUDIT_LOG` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:87]
- `ports` (property) component `ports [property]` (`23d164da-b584-5c84-a7d8-8d37cea87b8b`) lines 88-89 [crates/gcore/assets/docker-compose.services.yml:88-89]
  - Signature: `ports:`
  - Purpose: Indexed property `ports` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:88-89]
- `volumes` (property) component `volumes [property]` (`f9855082-a3a2-5eb2-bf07-2e6de0bfb613`) lines 90-92 [crates/gcore/assets/docker-compose.services.yml:90-92]
  - Signature: `volumes:`
  - Purpose: Indexed property `volumes` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:90-92]
- `healthcheck` (property) component `healthcheck [property]` (`582781f7-6818-5dba-8912-5e4d5f853ba2`) lines 93-113 [crates/gcore/assets/docker-compose.services.yml:93-113]
  - Signature: `healthcheck:`
  - Purpose: Indexed property `healthcheck` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:93-113]
- `test` (property) component `test [property]` (`d6748349-1adb-53d1-8645-4026726ea6b2`) lines 94-110 [crates/gcore/assets/docker-compose.services.yml:94-110]
  - Signature: `test:`
  - Purpose: Indexed property `test` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:94-110]
- `interval` (property) component `interval [property]` (`22bb68ed-6f43-550c-bfac-d4f6273fed95`) lines 111-111 [crates/gcore/assets/docker-compose.services.yml:111]
  - Signature: `interval: 5s`
  - Purpose: Indexed property `interval` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:111]
- `timeout` (property) component `timeout [property]` (`455e568d-a625-52cc-8d0d-9917b9e75857`) lines 112-112 [crates/gcore/assets/docker-compose.services.yml:112]
  - Signature: `timeout: 3s`
  - Purpose: Indexed property `timeout` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:112]
- `retries` (property) component `retries [property]` (`e78dd862-9429-5383-9b4c-68b264e6ebaa`) lines 113-113 [crates/gcore/assets/docker-compose.services.yml:113]
  - Signature: `retries: 10`
  - Purpose: Indexed property `retries` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:113]
- `restart` (property) component `restart [property]` (`8dc8e30b-6df9-5d1d-ba43-60a28dc03600`) lines 114-114 [crates/gcore/assets/docker-compose.services.yml:114]
  - Signature: `restart: unless-stopped`
  - Purpose: Indexed property `restart` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:114]
- `profiles` (property) component `profiles [property]` (`6359ef78-ad73-5281-ab3b-6341a749a6f1`) lines 115-117 [crates/gcore/assets/docker-compose.services.yml:115-117]
  - Signature: `profiles:`
  - Purpose: Indexed property `profiles` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:115-117]
- `volumes` (property) component `volumes [property]` (`64153251-c5bd-59c7-b6eb-defc1369fdcd`) lines 119-128 [crates/gcore/assets/docker-compose.services.yml:119-128]
  - Signature: `volumes:`
  - Purpose: Indexed property `volumes` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:119-128]
- `gobby_falkordb_data` (property) component `gobby_falkordb_data [property]` (`4d2cee14-286f-566c-9c85-9c96a283e16a`) lines 120-121 [crates/gcore/assets/docker-compose.services.yml:120-121]
  - Signature: `gobby_falkordb_data:`
  - Purpose: Indexed property `gobby_falkordb_data` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:120-121]
- `name` (property) component `name [property]` (`abc8afa0-7ef9-518e-ae76-84800c614485`) lines 121-121 [crates/gcore/assets/docker-compose.services.yml:121]
  - Signature: `name: gobby_falkordb_data`
  - Purpose: Indexed property `name` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:121]
- `gobby_qdrant_data` (property) component `gobby_qdrant_data [property]` (`5e6428e3-951c-5c9a-95ac-0b3c40d4c322`) lines 122-123 [crates/gcore/assets/docker-compose.services.yml:122-123]
  - Signature: `gobby_qdrant_data:`
  - Purpose: Indexed property `gobby_qdrant_data` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:122-123]
- `name` (property) component `name [property]` (`dcb576b4-a5af-5983-96e9-a80472f4c65b`) lines 123-123 [crates/gcore/assets/docker-compose.services.yml:123]
  - Signature: `name: gobby_qdrant_data`
  - Purpose: Indexed property `name` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:123]
- `gobby_postgres_data` (property) component `gobby_postgres_data [property]` (`27f328c9-6b58-561c-a919-a5cce2486667`) lines 124-125 [crates/gcore/assets/docker-compose.services.yml:124-125]
  - Signature: `gobby_postgres_data:`
  - Purpose: Indexed property `gobby_postgres_data` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:124-125]
- `name` (property) component `name [property]` (`500f6f15-fce0-5878-ba8d-10ebbbdb5071`) lines 125-125 [crates/gcore/assets/docker-compose.services.yml:125]
  - Signature: `name: gobby_postgres_data`
  - Purpose: Indexed property `name` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:125]
- `gobby_pgaudit_log` (property) component `gobby_pgaudit_log [property]` (`69cc6e92-3262-5da5-9494-733e42d29757`) lines 126-128 [crates/gcore/assets/docker-compose.services.yml:126-128]
  - Signature: `gobby_pgaudit_log:`
  - Purpose: Indexed property `gobby_pgaudit_log` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:126-128]
- `name` (property) component `name [property]` (`72678802-facf-508b-892a-07eb709831db`) lines 127-127 [crates/gcore/assets/docker-compose.services.yml:127]
  - Signature: `name: gobby_pgaudit_log`
  - Purpose: Indexed property `name` in `crates/gcore/assets/docker-compose.services.yml`. [crates/gcore/assets/docker-compose.services.yml:127]

