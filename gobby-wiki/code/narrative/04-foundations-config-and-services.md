---
title: 'Foundations: Configuration, Connectivity, and Services'
type: code_narrative
provenance:
- file: crates/gcode/src/config.rs
- file: crates/gcode/src/config/context.rs
- file: crates/gcode/src/config/services.rs
- file: crates/gcode/src/config/tests.rs
- file: crates/gcode/src/db/mod.rs
- file: crates/gcode/src/db/queries.rs
- file: crates/gcode/src/db/resolution.rs
- file: crates/gcode/src/setup/contracts.rs
- file: crates/gcode/src/setup/ddl.rs
- file: crates/gcode/src/setup/identifiers.rs
- file: crates/gcode/src/setup/postgres.rs
- file: crates/gcode/src/setup/tests.rs
- file: crates/gcode/src/setup/types.rs
- file: crates/gcore/assets/docker-compose.services.yml
- file: crates/gcore/assets/postgres-pgsearch/scripts/pg_audit_export.sh
- file: crates/gcore/assets/postgres-pgsearch/version.json
generated_by: gcode-codewiki
trust: generated
freshness: indexed
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
- [crates/gcode/src/setup/contracts.rs](crates/gcode/src/setup/contracts.rs)
- [crates/gcode/src/setup/ddl.rs](crates/gcode/src/setup/ddl.rs)
- [crates/gcode/src/setup/identifiers.rs](crates/gcode/src/setup/identifiers.rs)
- [crates/gcode/src/setup/postgres.rs](crates/gcode/src/setup/postgres.rs)
- [crates/gcode/src/setup/tests.rs](crates/gcode/src/setup/tests.rs)

_4 more source files omitted._

</details>

# Foundations: Configuration, Connectivity, and Services

# Foundations: Configuration, Connectivity, and Services

## Why this matters

Before any `gcode` command can do real work — indexing a project, querying symbols, writing vectors — it has to answer a chain of questions: *Which project am I operating on? Where do its backing services live? Are those services reachable? Has their schema been created yet?* If each command answered those questions in its own ad‑hoc way, you'd get subtle drift: one command reading an environment variable, another a config file, a third assuming localhost.

This part of the system centralizes that resolution into a single runtime **`Context`**. The design decision is to layer the sources — declared services, file config, environment overrides — so a command resolves exactly one authoritative view of where FalkorDB and Qdrant live and how to reach them. The backing services themselves are declared as data (a compose file at [crates/gcore/assets/docker-compose.services.yml:5-117]) rather than hardcoded, so the runtime topology and the configuration code stay in sync.

The public surface of this foundation is exported from one place, the config crate root [crates/gcode/src/config.rs:1-25], which re‑exports the `Context`, the service config types, and the well‑known keys and environment‑variable names other modules depend on.

## How it works

1. **Backing services are declared, not assumed.** The compose file [crates/gcore/assets/docker-compose.services.yml:5-117] enumerates the stateful services a command depends on — the FalkorDB graph store and the Qdrant vector store among them. This is the ground truth for what must be running.

2. **The project identity is resolved.** Configuration is anchored to a project. The config module walks outward from the working directory using `detect_project_root` / `detect_project_root_from` and then `resolve_project_identity` to produce a `ProjectIdentity` (tracking its `ProjectIdentitySource`). When identity can't be established, the code surfaces this explicitly through `MissingIdentity` and `warn_project_identity` rather than guessing — see the exports at [crates/gcode/src/config.rs:1-25].

3. **Service config is layered.** For each backing service the `Context` builds a typed config (`FalkorConfig`, `QdrantConfig`, `EmbeddingConfig`) via a `ServiceConfigSelection`. FalkorDB shows the layering clearly: a file-level config key (e.g. `FALKORDB_HOST_CONFIG_KEY`, `FALKORDB_PORT_CONFIG_KEY`, `FALKORDB_PASSWORD_CONFIG_KEY`) provides the base value, and a matching environment variable (`GOBBY_FALKORDB_HOST_ENV`, `GOBBY_FALKORDB_PORT_ENV`, `GOBBY_FALKORDB_PASSWORD_ENV`) overrides it. These constants are defined alongside the `Context` in [crates/gcode/src/config/context.rs:26-31] and re‑exported at [crates/gcode/src/config.rs:1-25].

4. **Embedding config is resolved separately and may be optional.** The `services` submodule resolves embedding settings through `resolve_embedding_config_details` and `read_standalone_config_optional` (note the `_optional` suffix — a missing standalone embedding config is a tolerated fallback, not a hard error), producing `EmbeddingConfigDetails` for the vector path. The vector side carries its own validation surface, `CodeVectorSettings` and `CodeVectorConfigError`, used together with `CODE_SYMBOL_COLLECTION_PREFIX` to name collections consistently.

5. **The connection is validated.** With config in hand, the `db` module establishes and checks the database connection [crates/gcode/src/db/mod.rs:16-20]. Validation here is what turns "we have a host and port" into "we can actually talk to the graph named `FALKORDB_GRAPH_NAME`."

6. **Schema is provisioned once.** The `setup` module defines the provisioning contract [crates/gcode/src/setup/contracts.rs:5-8] — the one‑time creation of the schema the validated connection expects. Because it's contract‑driven, provisioning is idempotent in intent: it describes the required end state rather than blindly re‑creating it on every command. The `validate_parent_code_index` helper (a crate‑internal export in [crates/gcode/src/config.rs:1-25]) likewise guards against operating against an index that isn't in the expected state.

The effect is a strict order: declared services → project identity → layered service config → validated connection → provisioned schema. Each step has an explicit failure mode (`MissingIdentity`, `CodeVectorConfigError`, the optional embedding fallback) so a misconfiguration fails where it's diagnosable instead of deep inside command logic.

## Key components

| Symbol | Role | Anchor |
| --- | --- | --- |
| `Context` | The resolved runtime context a command operates within | [crates/gcode/src/config/context.rs:26-31] |
| `FalkorConfig` / `QdrantConfig` | Typed connection config for each backing service | [crates/gcode/src/config.rs:1-25] |
| `ServiceConfigSelection` | Selects/layers which service config applies | [crates/gcode/src/config.rs:1-25] |
| `resolve_project_identity` / `detect_project_root` | Establish the `ProjectIdentity` anchor | [crates/gcode/src/config.rs:1-25] |
| `FALKORDB_*_CONFIG_KEY` / `GOBBY_FALKORDB_*_ENV` | File keys and env overrides for FalkorDB | [crates/gcode/src/config/context.rs:26-31] |
| `db` connection validation | Confirms the service is reachable | [crates/gcode/src/db/mod.rs:16-20] |
| `setup` provisioning contract | One‑time schema creation | [crates/gcode/src/setup/contracts.rs:5-8] |
| `docker-compose.services.yml` | Declares the backing services | [crates/gcore/assets/docker-compose.services.yml:5-117] |

### FalkorDB resolution sources at a glance

| File config key | Environment override |
| --- | --- |
| `FALKORDB_HOST_CONFIG_KEY` | `GOBBY_FALKORDB_HOST_ENV` |
| `FALKORDB_PORT_CONFIG_KEY` | `GOBBY_FALKORDB_PORT_ENV` |
| `FALKORDB_PASSWORD_CONFIG_KEY` | `GOBBY_FALKORDB_PASSWORD_ENV` |

All re‑exported from [crates/gcode/src/config.rs:1-25].

## What to read next

Now that you can see how a command resolves its `Context`, validates connectivity, and provisions schema, the next chapter follows what happens *after* the foundation is in place: how the validated `db` connection and the vector settings (`CodeVectorSettings`, `CODE_SYMBOL_COLLECTION_PREFIX`) are used to index and query a project. Start with the `db` module entry point at [crates/gcode/src/db/mod.rs:16-20], then trace into the setup contracts at [crates/gcode/src/setup/contracts.rs:5-8] to see how the schema those operations depend on is established.

## Concepts

- [[code/concepts/crates-gcore-assets|Service Infrastructure]]
- [[code/concepts/crates-gcode-src-config|Configuration & Database Access]]
- [[code/concepts/crates-gcode-src-setup|Schema Provisioning]]

## Explore

- [[code/modules/crates/gcore/assets|crates/gcore/assets]]
- [[code/modules/crates/gcode/src/config|crates/gcode/src/config]]
- [[code/modules/crates/gcode/src/db|crates/gcode/src/db]]
- [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Continue the tour

- ← Previous: [[code/narrative/03-data-flow|Data Flow]]
- Next →: [[code/narrative/05-indexing-pipeline|Turning Source Files into Code Facts]]

