---
title: Architecture
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

# Architecture

# Architecture

## Why this matters

Before you can navigate any codebase confidently, you need a map of where things live and how the pieces fit together. This chapter is that map. It traces the workspace from the top-level `crates` module down into the `gcode` crate, where the bulk of the indexing logic lives, and shows how configuration, the database layer, the indexer, and the filesystem walker relate to one another.

The central design decision here is *separation by responsibility within a single crate*. Rather than scattering concerns, `gcode` keeps configuration resolution ([crates/gcode/src/config/context.rs:26-31]), persistence ([crates/gcode/src/db/mod.rs:16-20]), indexing ([crates/gcode/src/index/api.rs:16-23]), and project setup ([crates/gcode/src/setup/contracts.rs:5-8]) in clearly named submodules. The supporting `gcore` crate carries shared assets such as the service definitions in its Docker Compose file ([crates/gcore/assets/docker-compose.services.yml:5-117]). Understanding this layout means you can predict where a given behavior is implemented before you ever open the file.

## How it works

Here is the real flow, from build time through configuration to the indexing modules.

1. **Build-time wiring happens first.** The crate's build script, `main`, emits Cargo directives so the build reruns when `GCODE_POSTGRES_TEST_DATABASE_URL` changes, registers the `gcode_postgres_tests` cfg, and enables that cfg only when the environment variable is set ([crates/gcode/build.rs:1-8]). This is how the Postgres-backed tests are gated: with no database URL present, the cfg stays off and those tests are compiled out.

2. **Configuration is resolved through the `config` module.** The crate root re-exports the public configuration surface — `Context`, `ProjectIdentity`, `FalkorConfig`, `QdrantConfig`, and the embedding types — from `context` ([crates/gcode/src/config.rs:9-15]). This module is the entry point for answering "what project am I in, and which services do I talk to?" via helpers like `detect_project_root` and `resolve_project_identity` ([crates/gcode/src/config.rs:9-15]).

3. **Service settings come from environment variables and config keys.** Configuration distinguishes named config keys (such as `FALKORDB_HOST_CONFIG_KEY`) from their environment-variable counterparts (`GOBBY_FALKORDB_HOST_ENV`), letting a value be supplied either way ([crates/gcode/src/config.rs:11-14]). Internal helpers like `read_standalone_config_optional` and `resolve_embedding_config_details` are re-exported only at crate-internal visibility ([crates/gcode/src/config.rs:18-20]), keeping the public API focused.

4. **The database layer backs persistence.** With identity and service config resolved, the `db` module ([crates/gcode/src/db/mod.rs:16-20]) provides the storage interface the rest of the crate builds on — the same FalkorDB and Qdrant services described in the shared Compose assets ([crates/gcore/assets/docker-compose.services.yml:5-117]).

5. **Indexing drives the walker and indexer.** The `index` module exposes its API ([crates/gcode/src/index/api.rs:16-23]) and coordinates two collaborators: the `walker`, which classifies files as it traverses the tree ([crates/gcode/src/index/walker/classification.rs:15-52]), and the `indexer`, which processes individual files ([crates/gcode/src/index/indexer/file.rs:15-91]). Setup contracts in the `setup` module ([crates/gcode/src/setup/contracts.rs:5-8]) define the agreements that initialize a project before indexing runs.

The notable fallback to remember is the build-script gate from step 1: absent `GCODE_POSTGRES_TEST_DATABASE_URL`, the `gcode_postgres_tests` cfg is never enabled ([crates/gcode/build.rs:4-7]).

## Key components

| Symbol / Module | Where | Role |
| --- | --- | --- |
| `main` (build script) | [crates/gcode/build.rs:1-8] | Gates Postgres tests on the `GCODE_POSTGRES_TEST_DATABASE_URL` env var |
| `config` | [crates/gcode/src/config/context.rs:26-31] | Resolves project identity and service settings |
| `db` | [crates/gcode/src/db/mod.rs:16-20] | Persistence layer backing the index |
| `index` | [crates/gcode/src/index/api.rs:16-23] | Public indexing entry point |
| `index/walker` | [crates/gcode/src/index/walker/classification.rs:15-52] | Traverses and classifies files |
| `index/indexer` | [crates/gcode/src/index/indexer/file.rs:15-91] | Processes individual files |

Selected configuration variables, surfaced through the crate root ([crates/gcode/src/config.rs:9-20]):

| Name | Kind |
| --- | --- |
| `GCODE_POSTGRES_TEST_DATABASE_URL` | Env var (build-time test gate) [crates/gcode/build.rs:2] |
| `GOBBY_FALKORDB_HOST_ENV` / `GOBBY_FALKORDB_PORT_ENV` / `GOBBY_FALKORDB_PASSWORD_ENV` | FalkorDB env vars [crates/gcode/src/config.rs:13-14] |
| `FALKORDB_HOST_CONFIG_KEY` / `FALKORDB_PORT_CONFIG_KEY` / `FALKORDB_PASSWORD_CONFIG_KEY` | FalkorDB config keys [crates/gcode/src/config.rs:11-12] |
| `CODE_SYMBOL_COLLECTION_PREFIX` | Collection naming prefix [crates/gcode/src/config.rs:10] |

## What to read next

Follow the flow in the order the code uses it. Start with the **Configuration** reference for the `config` module ([crates/gcode/src/config/context.rs:26-31]) to see how project identity and service settings are resolved, then move to the **Indexing** chapter covering the `index` API ([crates/gcode/src/index/api.rs:16-23]) and its `walker` ([crates/gcode/src/index/walker/classification.rs:15-52]) and `indexer` ([crates/gcode/src/index/indexer/file.rs:15-91]) collaborators.

## Concepts

- [[code/concepts/crates|Workspace Topology]]
- [[code/concepts/crates-gcore|Shared Platform Primitives]]
- [[code/concepts/crates-gcore-assets|Service Infrastructure]]
- [[code/concepts/crates-gcode-src-config|Configuration & Database Access]]
- [[code/concepts/crates-gcode-src-setup|Schema Provisioning]]
- [[code/concepts/crates-gcode-src-index|Code Indexing Pipeline]]

## Continue the tour

- ← Previous: [[code/narrative/01-introduction|Introduction: The Gobby Code Intelligence Workspace]]
- Next →: [[code/narrative/03-data-flow|Data Flow]]

