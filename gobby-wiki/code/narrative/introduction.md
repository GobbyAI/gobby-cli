---
title: System Orientation
type: code_narrative
provenance:
- file: crates/gcode/contract/gcode.contract.json
- file: crates/gcode/src/commands/codewiki/prompts.rs
- file: crates/gcode/src/commands/codewiki/types.rs
- file: crates/gcode/src/commands/graph/reads.rs
- file: crates/gcode/src/commands/grep.rs
- file: crates/gcode/src/commands/search.rs
- file: crates/gcode/src/commands/symbol_at.rs
- file: crates/gcode/src/config/services.rs
- file: crates/gcode/src/db/resolution.rs
- file: crates/gcode/src/index/semantic.rs
- file: crates/gcode/src/models.rs
- file: crates/gcore/assets/docker-compose.services.yml
- file: crates/gcore/src/ai_context.rs
- file: crates/ghook/schemas/diagnose-output.v2.schema.json
- file: crates/ghook/schemas/inbox-envelope.v1.schema.json
- file: crates/gwiki/contract/gwiki.contract.json
- file: crates/gwiki/src/ai/chunk.rs
- file: crates/gwiki/src/benchmark.rs
- file: crates/gwiki/src/collect.rs
- file: crates/gwiki/src/commands/citation_quality.rs
- file: crates/gwiki/src/commands/sources.rs
- file: crates/gwiki/src/graph/mod.rs
- file: crates/gwiki/src/health.rs
- file: crates/gwiki/src/ingest/audio.rs
- file: crates/gwiki/src/ingest/mod.rs
- file: crates/gwiki/src/ingest/session.rs
- file: crates/gwiki/src/links.rs
- file: crates/gwiki/src/main.rs
- file: crates/gwiki/src/search/semantic.rs
- file: crates/gwiki/src/vector.rs
provenance_truncated: 442
generated_by: gcode-codewiki
trust: generated
freshness: indexed
verify_notes:
- id: 2
  reason: '`gcode` role and its command/application responsibilities are not shown in the excerpt.'
- id: 3
  reason: '`gcore` foundation claims are not evidenced here; only the compose-file header is shown.'
- id: 4
  reason: The layered design summary is not supported by the provided excerpt.
- id: 6
  reason: No evidence shows a top-level `crates` workspace or that `crates/gcode` and `crates/gcore` have those roles.
- id: 7
  reason: '`gcode` contract details like invocation schema, flags, metadata, and error codes are not in the excerpt.'
- id: 8
  reason: '`gcode` orchestration claims about search, grep, setup, freshness, visibility, and projections are not evidenced.'
- id: 9
  reason: '`gcore` owning AI, configuration, service, and degradation layers is not shown in the excerpt.'
- id: 16
  reason: The `crates/gcode` and `crates/gcore` module rows are unsupported by the provided evidence.
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/contract/gcode.contract.json](crates/gcode/contract/gcode.contract.json)
- [crates/gcode/src/commands/codewiki/prompts.rs](crates/gcode/src/commands/codewiki/prompts.rs)
- [crates/gcode/src/commands/codewiki/types.rs](crates/gcode/src/commands/codewiki/types.rs)
- [crates/gcode/src/commands/graph/reads.rs](crates/gcode/src/commands/graph/reads.rs)
- [crates/gcode/src/commands/grep.rs](crates/gcode/src/commands/grep.rs)
- [crates/gcode/src/commands/search.rs](crates/gcode/src/commands/search.rs)
- [crates/gcode/src/commands/symbol_at.rs](crates/gcode/src/commands/symbol_at.rs)
- [crates/gcode/src/config/services.rs](crates/gcode/src/config/services.rs)
- [crates/gcode/src/db/resolution.rs](crates/gcode/src/db/resolution.rs)
- [crates/gcode/src/index/semantic.rs](crates/gcode/src/index/semantic.rs)
- [crates/gcode/src/models.rs](crates/gcode/src/models.rs)
- [crates/gcore/assets/docker-compose.services.yml](crates/gcore/assets/docker-compose.services.yml)

_460 more source files omitted._

</details>

# System Orientation

## Why this matters

Gobby splits responsibilities between a command-facing workspace and a shared core substrate. The `crates/gcode` module is the GCode CLI side: it owns the “Fast code index CLI for Gobby” contract, including invocation shape, global flags, scope resolution, command metadata, JSON output keys, and error metadata. Its application layer handles orchestration around CLI commands, configuration/context resolution, PostgreSQL index access, graph/vector projection lifecycle, search, grep, setup, freshness, visibility, and shared output/model contracts.

The boundary matters because `crates/gcore` carries the reusable foundation underneath those commands. It centralizes AI routing/context/types, layered configuration, service provisioning, graph/vector/search primitives, setup validation, and degradation contracts, so domain-facing callers do not need to manage transport or storage details directly. The service assets in `crates/gcore/assets` make that concrete: local dependencies are “Installed via: gobby install” and “Managed by daemon start/stop via Docker Compose profiles” .

The design decision is therefore layered: CLI behavior and command contracts live in `gcode`, while shared runtime services and infrastructure contracts live in `gcore`.

## How it works

1. Gobby starts from a workspace made of member crates. The top-level `crates` area includes `crates/gcode`, which is the CLI crate and contract bundle, and `crates/gcore`, which is the shared core layer [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2].

2. The CLI-facing side is defined by `crates/gcode`. Its contract describes a fast code index CLI for Gobby, including invocation schema, flags, command metadata, JSON output keys, and error-code metadata. That keeps command behavior explicit before the implementation reaches into indexes, projections, or services.

3. Command implementation then delegates through the application layer. `gcode` owns orchestration for search, grep, setup, freshness, visibility, context resolution, PostgreSQL index access, and graph/vector projection lifecycle, so the command layer can expose stable user-facing behavior while using shared lower layers.

4. Shared runtime concerns live in `crates/gcore`. This layer owns AI context/routing/types, local and layered configuration, service provisioning, graph/vector/search primitives, setup validation, and degradation contracts. In practice, this means later code can ask for capabilities instead of hard-coding every transport or storage detail.

5. Local service provisioning is packaged under `crates/gcore/assets`. The Compose file declares Gobby service dependencies, marks them as installed by `gobby install`, and says daemon start/stop manages them through Docker Compose profiles .

6. The service stack is profile-based. FalkorDB exposes Redis and browser ports with configurable defaults, stores data in `gobby_falkordb_data`, checks health with `redis-cli`, restarts unless stopped, and belongs to the `falkordb` and `all` profiles [crates/gcore/assets/docker-compose.services.yml:5-29].

7. Qdrant follows the same local-service pattern: configurable HTTP and gRPC ports, log-level environment configuration, persistent storage, a `/healthz` check, restart policy, and `qdrant` plus `all` profiles [crates/gcore/assets/docker-compose.services.yml:31-49]. Its excerpt notes that auth is disabled for local-only access and would require an API key plus TLS to enable safely [crates/gcore/assets/docker-compose.services.yml:35-37].

8. PostgreSQL is built locally with pg_search inputs. The `build` block points at `./postgres-pgsearch`, passes `PG_SEARCH_VERSION` from `GOBBY_PG_SEARCH_VERSION` with default `0.23.4`, and passes `PG_SEARCH_SHA256` from `GOBBY_PG_SEARCH_SHA256` [crates/gcore/assets/docker-compose.services.yml:52-56].

9. PostgreSQL then starts as `gobby-postgres` and enables `pg_search` plus `pgaudit` through its `command` settings [crates/gcore/assets/docker-compose.services.yml:58-64]. Audit logging falls back to `${GOBBY_PGAUDIT_LOG:-ddl}`, so the default behavior logs DDL unless overridden [crates/gcore/assets/docker-compose.services.yml:65].

## Key components

| Symbol | Kind | Why it matters |
| --- | --- | --- |
| `crates/gcode` | module | CLI crate and contract bundle for command invocation, flags, scope resolution, output shape, and command orchestration. |
| `crates/gcore` | module | Shared core layer for AI context, configuration, service provisioning, graph/vector/search primitives, setup validation, and degradation contracts. |
| `crates/gcore/assets/docker-compose.services.yml` | file | Defines local service dependencies installed by `gobby install` and managed by daemon start/stop profiles . |
| `falkordb` | service | Local graph/storage dependency with configurable ports, password pass-through, persistent volume, healthcheck, restart policy, and profiles [crates/gcore/assets/docker-compose.services.yml:5-29]. |
| `qdrant` | service | Local vector service with configurable ports, log-level environment, persistent storage, healthcheck, restart policy, and profiles [crates/gcore/assets/docker-compose.services.yml:31-49]. |
| `postgres` | service | Local PostgreSQL image with pg_search build args, fixed container name, and startup command enabling `pg_search` plus `pgaudit` [crates/gcore/assets/docker-compose.services.yml:52-65]. |
| `PG_SEARCH_VERSION` | property | Build arg supplied from `${GOBBY_PG_SEARCH_VERSION:-0.23.4}` for the local PostgreSQL pg_search image [crates/gcore/assets/docker-compose.services.yml:55]. |
| `GOBBY_PGAUDIT_LOG` | property | Runtime audit-log setting with `ddl` fallback in the PostgreSQL command [crates/gcore/assets/docker-compose.services.yml:65]. |

## What to read next

Read the `gcode` command-contract chapter next, especially the command metadata, global flags, output keys, and error-code contract. After that, move into the `gcore` service-provisioning reference for the Docker Compose profiles and local dependency lifecycle.

## Concepts

- [[code/concepts/workspace-map|Workspace Map]]
- [[code/concepts/shared-service-substrate|Shared Service Substrate]]

## Explore

- [[code/modules/crates|crates]]
- [[code/modules/crates/gcore|crates/gcore]]
- [[code/modules/crates/gcore/assets|crates/gcore/assets]]
- [[code/modules/crates/gcode|crates/gcode]]

## Continue the tour

- Next →: [[code/narrative/architecture|Architecture]]

