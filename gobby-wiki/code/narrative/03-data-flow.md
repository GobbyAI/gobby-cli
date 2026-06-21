---
title: Data Flow
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

# Data Flow

# Data Flow

## Why this matters

Before `gcode` can answer a single question about your code, raw bytes on disk have to travel a long way: a project root must be located, every file has to be classified and parsed, and the resulting symbols have to land in the right backing stores. If any one of those stages guesses wrong — picks the wrong project, walks a file it should skip, or connects to the wrong database — everything downstream is silently corrupted.

The design decision that holds this together is *explicit configuration resolution at the front of the pipeline*. Instead of scattering host/port/path lookups across the indexer, `gcode` concentrates them in one module, `crates/gcode/src/config` [crates/gcode/src/config/context.rs:26-31], and exposes a single resolved `Context` plus typed service configs (`FalkorConfig`, `QdrantConfig`, `EmbeddingConfig`) [crates/gcode/src/config.rs:9-16]. Every later stage reads from that resolved context rather than re-deriving it. That is why this chapter starts with config and follows the data outward toward storage.

## How it works

The flow moves left-to-right, from environment and disk into the graph and vector stores.

1. **Build-time feature gating.** Before the crate even runs, its build script decides whether Postgres-backed tests are compiled in. `main` in `crates/gcode/build.rs` emits a `rerun-if-env-changed` directive, registers the `gcode_postgres_tests` cfg, and enables that cfg only when `GCODE_POSTGRES_TEST_DATABASE_URL` is set [crates/gcode/build.rs:1-8]. If the variable is absent, the cfg stays off and those code paths are excluded — a fallback to "no Postgres tests" rather than a failure.

2. **Project identity resolution.** At runtime the config module locates the project. `detect_project_root` / `detect_project_root_from` find the root on disk, and `resolve_project_identity` turns that into a `ProjectIdentity` with a `ProjectIdentitySource` [crates/gcode/src/config.rs:13-15]. When identity is missing or ambiguous, the surfaced `MissingIdentity` and `warn_project_identity` types let the system warn instead of hard-stopping [crates/gcode/src/config.rs:11-15].

3. **Service configuration.** From the same module the backing services are resolved. FalkorDB connection details are read from config keys (`FALKORDB_HOST_CONFIG_KEY`, `FALKORDB_PORT_CONFIG_KEY`, `FALKORDB_PASSWORD_CONFIG_KEY`) or their environment overrides (`GOBBY_FALKORDB_HOST_ENV`, `GOBBY_FALKORDB_PORT_ENV`, `GOBBY_FALKORDB_PASSWORD_ENV`) into a `FalkorConfig`; vector storage is described by `QdrantConfig` and `CodeVectorSettings`, and embeddings by `EmbeddingConfig` [crates/gcode/src/config.rs:9-16]. The actual service processes these point at are defined in `crates/gcore/assets/docker-compose.services.yml` [crates/gcore/assets/docker-compose.services.yml:5-117]. `read_standalone_config_optional` and `resolve_embedding_config_details` provide the optional/fallback reads [crates/gcode/src/config.rs:18-20].

4. **Walking and classification.** With a resolved root, the walker enumerates files and decides what each one is. Classification lives in `crates/gcode/src/index/walker/classification.rs` [crates/gcode/src/index/walker/classification.rs:15-52], which is where files that should not be indexed get filtered out before any parsing cost is paid.

5. **Per-file indexing.** Surviving files flow into the indexer at `crates/gcode/src/index/indexer/file.rs` [crates/gcode/src/index/indexer/file.rs:15-91], which extracts the symbols for each file.

6. **Persistence through the index API and DB layer.** Extracted symbols are committed through the index API surface [crates/gcode/src/index/api.rs:16-23] into the database layer [crates/gcode/src/db/mod.rs:16-20], which writes to the graph and vector stores using the `FalkorConfig`/`QdrantConfig` resolved in step 3. Collection naming is anchored by constants such as `FALKORDB_GRAPH_NAME` and `CODE_SYMBOL_COLLECTION_PREFIX` [crates/gcode/src/config.rs:9-12].

The `setup` module's contracts [crates/gcode/src/setup/contracts.rs:5-8] tie these stages together so the same resolved configuration is honored end to end.

## Key components

| Symbol / Anchor | Role in the flow |
| --- | --- |
| `main` [crates/gcode/build.rs:1-8] | Build-time gate; enables `gcode_postgres_tests` only when the test DB URL env var is set |
| `Context`, `resolve_project_identity` [crates/gcode/src/config.rs:9-15] | Resolves project root and identity at the front of the pipeline |
| `FalkorConfig`, `QdrantConfig`, `EmbeddingConfig` [crates/gcode/src/config.rs:9-16] | Typed service configs consumed by storage |
| walker `classification.rs` [crates/gcode/src/index/walker/classification.rs:15-52] | Decides which files enter the pipeline |
| indexer `file.rs` [crates/gcode/src/index/indexer/file.rs:15-91] | Extracts symbols per file |
| index `api.rs` [crates/gcode/src/index/api.rs:16-23] → db `mod.rs` [crates/gcode/src/db/mod.rs:16-20] | Persists results to graph/vector stores |

## What to read next

Continue into the **Configuration** reference for the full set of `FALKORDB_*` config keys and `GOBBY_FALKORDB_*` environment overrides exposed from `crates/gcode/src/config.rs` [crates/gcode/src/config.rs:9-16], then follow with the **Indexing** chapter to see how the walker and indexer stages in `crates/gcode/src/index` turn classified files into stored symbols [crates/gcode/src/index/api.rs:16-23].

## Concepts

- [[code/concepts/crates|Workspace Topology]]
- [[code/concepts/crates-gcore|Shared Platform Primitives]]
- [[code/concepts/crates-gcore-assets|Service Infrastructure]]
- [[code/concepts/crates-gcode-src-config|Configuration & Database Access]]
- [[code/concepts/crates-gcode-src-setup|Schema Provisioning]]
- [[code/concepts/crates-gcode-src-index|Code Indexing Pipeline]]

## Continue the tour

- ← Previous: [[code/narrative/02-architecture|Architecture]]
- Next →: [[code/narrative/04-foundations-config-and-services|Foundations: Configuration, Connectivity, and Services]]

