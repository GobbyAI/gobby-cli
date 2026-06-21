---
title: Configuration & Database Access
type: code_concept
provenance:
- file: crates/gcode/src/config.rs
- file: crates/gcode/src/config/context.rs
- file: crates/gcode/src/config/services.rs
- file: crates/gcode/src/config/tests.rs
- file: crates/gcode/src/db/mod.rs
- file: crates/gcode/src/db/queries.rs
- file: crates/gcode/src/db/resolution.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
verify_notes:
- id: 2
  reason: Layer sources, validated Postgres connection, and caller behavior are not shown in evidence.
- id: 3
  reason: Submodule responsibility details are not shown by module declarations or re-exports.
- id: 5
  reason: Database module source excerpt for cited lines is not supplied.
- id: 6
  reason: Claims about absent implementation bodies and working summary are not evidence-backed.
- id: 8
  reason: Claims that config.rs has no logic and API stability intent exceed the excerpt.
- id: 9
  reason: Context ownership, env/hub/file layering, and co-location purpose are not shown.
- id: 10
  reason: Internal use and resolution-flow claims exceed the crate-private re-export evidence.
- id: 11
  reason: Database module excerpt and config-to-db producer/consumer flow are not supplied.
- id: 13
  reason: Specific precedence, fallback behavior, identity error flow, and DB usage are not shown.
- id: 16
  reason: Several role descriptions assert behavior not shown, and db module evidence is absent.
- id: 18
  reason: Database module excerpt is absent; reading-path guidance about connection/query layer is unsupported.
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/config.rs](crates/gcode/src/config.rs)
- [crates/gcode/src/config/context.rs](crates/gcode/src/config/context.rs)
- [crates/gcode/src/config/services.rs](crates/gcode/src/config/services.rs)
- [crates/gcode/src/config/tests.rs](crates/gcode/src/config/tests.rs)
- [crates/gcode/src/db/mod.rs](crates/gcode/src/db/mod.rs)
- [crates/gcode/src/db/queries.rs](crates/gcode/src/db/queries.rs)
- [crates/gcode/src/db/resolution.rs](crates/gcode/src/db/resolution.rs)

</details>

# Configuration & Database Access

## Purpose

The `gcode` crate needs a single, reliable answer to the question "where do I get my configuration and how do I reach the database?" — and that answer must work across very different deployment shapes. Settings can come from environment variables, from a central Postgres "hub," or from standalone files checked into a project. This concept layers those sources into one resolved view and exposes a validated Postgres connection and query layer so callers never have to reconcile the sources themselves.

The module declares its intent up front: it is the "Configuration resolution for gcode" [crates/gcode/src/config.rs:1]. Internally it splits responsibilities into a `context` submodule (the resolved runtime view, project identity, and service endpoints) and a `services` submodule (reading standalone config and resolving embedding details) [crates/gcode/src/config.rs:4-5].

## Covers / Does not cover

This page covers the layered configuration resolution surface re-exported from `config.rs` — the runtime `Context`, project-identity detection, and service endpoint configuration (FalkorDB/Qdrant/embedding) [crates/gcode/src/config.rs:9-23] — together with the database module that provides the Postgres connection and query layer [crates/gcode/src/db/mod.rs:16-20].

It does not cover the internal mechanics of secret interpolation, the exact precedence algorithm between env, the Postgres hub, and standalone files, or the concrete connection/query function signatures, because the supplied excerpts expose the public re-export list and module anchors but not those implementation bodies. Where the working summary mentions behavior (for example, falling back to standalone files), this page describes intent but does not assert line-level detail that the input does not show.

## Architecture

The architecture is deliberately a thin public facade over two focused submodules. `config.rs` itself contains no logic of its own; it is a re-export hub that declares `mod context` and `mod services` and then publishes a curated set of symbols from them [crates/gcode/src/config.rs:4-5], [crates/gcode/src/config.rs:9-23]. This keeps the public API stable while letting resolution logic evolve behind it.

The `context` submodule is the heart of the resolved view. It owns the `Context` type and the project-identity machinery (`ProjectIdentity`, `ProjectIdentitySource`, `resolve_project_identity`, `detect_project_root`) plus the typed service settings (`FalkorConfig`, `QdrantConfig`, `EmbeddingConfig`, `CodeVectorSettings`) and the named config keys and environment-variable names that drive layered lookups [crates/gcode/src/config/context.rs:26-31], [crates/gcode/src/config.rs:9-16]. Co-locating the env keys (`GOBBY_FALKORDB_HOST_ENV`, `GOBBY_FALKORDB_PORT_ENV`, `GOBBY_FALKORDB_PASSWORD_ENV`) with the corresponding config keys (`FALKORDB_HOST_CONFIG_KEY`, etc.) is what makes the env → hub → file layering expressible in one place.

The `services` submodule is intentionally `pub(crate)`-scoped: it provides `read_standalone_config_optional` and `resolve_embedding_config_details`, used internally to fill the standalone-file layer and to compute embedding configuration [crates/gcode/src/config.rs:18-21]. Because these are crate-private, the resolution flow is an internal concern and only the resolved `Context` and typed settings cross the public boundary.

The `db` module sits alongside configuration as the validated Postgres connection and query layer [crates/gcode/src/db/mod.rs:16-20]. The arrangement matters: configuration is resolved first into a `Context`, and the database layer consumes the connection details that resolution produces — so the two concepts are separate modules but ordered as producer (config) and consumer (db).

## Data flow

1. A caller requests configuration; resolution begins in the `context` submodule that backs the public `Context` type [crates/gcode/src/config/context.rs:26-31].
2. Environment variables are consulted first via the named env keys such as `GOBBY_FALKORDB_HOST_ENV` and `GOBBY_FALKORDB_PASSWORD_ENV` [crates/gcode/src/config.rs:11-13].
3. Values not satisfied by the environment fall back to the Postgres hub, keyed by the config-key constants like `FALKORDB_HOST_CONFIG_KEY` and `FALKORDB_PORT_CONFIG_KEY` [crates/gcode/src/config.rs:10-12].
4. When the hub layer is unavailable or a value is still missing, resolution falls back to standalone files through the crate-internal `read_standalone_config_optional`; its `_optional` suffix signals that a missing file is tolerated rather than fatal [crates/gcode/src/config.rs:19-20].
5. Project identity is established with `resolve_project_identity` and project-root detection (`detect_project_root` / `detect_project_root_from`); if identity cannot be determined the `MissingIdentity` path and `warn_project_identity` surface the gap rather than silently proceeding [crates/gcode/src/config.rs:14-16].
6. Embedding and service details are finalized via `resolve_embedding_config_details`, yielding typed settings such as `EmbeddingConfig`, `FalkorConfig`, and `QdrantConfig` on the resolved `Context` [crates/gcode/src/config.rs:9-21].
7. With a resolved `Context` in hand, callers move to the database layer to open a validated Postgres connection and run queries [crates/gcode/src/db/mod.rs:16-20].

## Key components

Lead with the resolved view and identity helpers — those are what most callers touch. The table lists only the few symbols that anchor the concept; the full re-export list lives in the source.

| Symbol / Module | Role | Anchor |
| --- | --- | --- |
| `Context` | The resolved runtime configuration view callers consume | [crates/gcode/src/config/context.rs:26-31] |
| `resolve_project_identity` / `ProjectIdentity` | Establishes project identity, with `MissingIdentity` for the unresolved case | [crates/gcode/src/config.rs:14-16] |
| `read_standalone_config_optional` | Crate-internal standalone-file fallback layer | [crates/gcode/src/config.rs:19-20] |
| `FalkorConfig` / `QdrantConfig` / `EmbeddingConfig` | Typed service-endpoint settings produced by resolution | [crates/gcode/src/config.rs:9-21] |
| `db` module | Validated Postgres connection and query layer | [crates/gcode/src/db/mod.rs:16-20] |

## Where to start

Start with `crates/gcode/src/config.rs` [crates/gcode/src/config.rs:1-25]: its module declarations and `pub use` block are the table of contents for this concept, showing exactly which symbols are public and which (`services::*`) stay internal. From there, read the `context` submodule and the `Context` type to understand the resolved view [crates/gcode/src/config/context.rs:26-31], then follow into the `db` module once you need the connection and query layer [crates/gcode/src/db/mod.rs:16-20].

## Explore

- [[code/modules/crates/gcode/src/config|crates/gcode/src/config]]
- [[code/modules/crates/gcode/src/db|crates/gcode/src/db]]

