---
title: Configuration and PostgreSQL Setup
type: code_concept
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
generated_by: gcode-codewiki
trust: generated
freshness: indexed
verify_notes:
- id: 2
  reason: Claims about hub database resolution are not shown in the supplied excerpts.
- id: 3
  reason: Config/context resolution chain and db-layer behavior are not evidenced here; only standalone setup objects are shown.
- id: 6
  reason: The query-layer reads and GenericClient/model behavior are not shown in the provided excerpts.
- id: 7
  reason: The hub database row cites db/mod.rs, but no db excerpt is provided; that claim is unsupported.
- id: 10
  reason: The provenance/expansion behavior attributed to context.rs is not shown in the supplied excerpts.
- id: 11
  reason: db/mod.rs behavior is not in the provided excerpts.
- id: 14
  reason: The config resolution order and expansion details are not shown in the supplied excerpts.
- id: 16
  reason: db/mod.rs DSN, connection, and API claims are not evidenced here.
- id: 19
  reason: Behavior of ensure_postgres_code_index_compatible is not shown in the excerpts.
- id: 20
  reason: Neither incompatible_postgres_code_index_relations nor index_info appears in the supplied excerpts.
- id: 22
  reason: The create method behavior is not shown in the provided excerpts.
- id: 23
  reason: execute_postgres_ddl behavior is not shown in the provided excerpts.
- id: 27
  reason: The ensure_postgres_code_index_compatible and execute_postgres_ddl role claims are not supported by the excerpts.
- id: 29
  reason: The reference to ensure_postgres_code_index_compatible is not supported by the supplied excerpts.
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

_1 more source file omitted._

</details>

# Configuration and PostgreSQL Setup

## Purpose

Configuration and PostgreSQL setup give gcode commands a consistent runtime base: first by resolving project and service settings, then by resolving the hub PostgreSQL database boundary, and finally by provisioning or validating the standalone PostgreSQL code-index schema when needed.

The configuration layer is the entry point for typed runtime settings. Its context facade documents the resolution chain as `bootstrap.yaml -> PostgreSQL hub -> config_store -> service configs`, with `$secret:NAME` and `${VAR}` expansion, and exposes service settings consumed elsewhere in gcode [crates/gcode/src/config/context.rs:26-31]. The database layer then owns hub PostgreSQL DSN resolution, connection opening, schema validation, and query access over hub tables [crates/gcode/src/db/mod.rs:16-20]. Standalone setup covers the PostgreSQL objects needed for the code index, including `pg_search` and tables such as `code_indexed_projects`, `code_indexed_files`, `code_symbols`, `code_content_chunks`, `code_imports`, and `code_calls` .

## Covers / Does not cover

This page covers the runtime base shared by gcode commands: configuration resolution, hub database access, and standalone PostgreSQL code-index setup. It also covers compatibility checks and overwrite behavior for existing PostgreSQL relations.

It does not cover the full indexing pipeline, graph/vector service internals, or every query shape. The query layer is only relevant here as the consumer of a validated database boundary; it reads indexed file paths, project/file existence, graph facts, and graph sync state from hub tables using `postgres::GenericClient` and model types [crates/gcode/src/db/mod.rs:16-20].

| Area | Included here | Boundary |
| --- | --- | --- |
| Configuration | Project context and typed service settings exposed by `crates/gcode/src/config.rs` [crates/gcode/src/config.rs:1-25] | Not the implementation details of each service resolver |
| Hub database | DSN resolution, connection mode, schema validation, config reads [crates/gcode/src/db/mod.rs:16-20] | Not exhaustive query behavior |
| Standalone setup | Code-index schema contracts, DDL creation, compatibility checks, reset helpers [crates/gcode/src/setup/contracts.rs:5-8] | Not non-PostgreSQL provisioning |

## Architecture

The pieces are arranged as three boundaries that progressively make runtime state more concrete.

`crates/gcode/src/config` is the high-level configuration facade. It exposes project identity helpers, service config types, FalkorDB/Qdrant/embedding settings, and standalone config loading through `context` and `services` exports [crates/gcode/src/config.rs:1-25]. This keeps command code from knowing whether a value came from bootstrap configuration, the hub database, config-store data, environment interpolation, or secret expansion [crates/gcode/src/config/context.rs:26-31].

`crates/gcode/src/db` is the database boundary. It resolves the PostgreSQL hub DSN, opens read/write or read-only connections, validates the runtime schema, and delegates configuration reads to `gobby_core` [crates/gcode/src/db/mod.rs:16-20]. This isolates commands from connection details and lets the query layer operate through `postgres::GenericClient`.

`crates/gcode/src/setup` owns standalone PostgreSQL provisioning. `GcodeStandaloneSetup` stores the target schema, qualifies relation names through that schema, and produces ordered PostgreSQL object definitions [crates/gcode/src/setup/ddl.rs:8-10]. The contracts layer records the expected tables, columns, indexes, and overwrite guidance . The PostgreSQL setup layer then validates requests, starts a transaction, optionally resets existing code-index relations, checks compatibility, executes setup, and commits only when setup succeeds .

## Data flow

1. A command starts from configuration context. The config facade resolves project identity and service settings through the documented order `bootstrap.yaml -> PostgreSQL hub -> config_store -> service configs`, including `$secret:NAME` and `${VAR}` expansion [crates/gcode/src/config/context.rs:26-31].

2. Service-specific settings are resolved through the config service layer. The public facade exposes typed settings and helpers such as `FalkorConfig`, `QdrantConfig`, `EmbeddingConfig`, `ProjectIdentity`, `ProjectIndexScope`, and project-root detection [crates/gcode/src/config.rs:1-25].

3. Database access moves through `crates/gcode/src/db`, which resolves the hub PostgreSQL DSN, opens read/write or read-only connections, validates runtime schema, and provides query/config APIs to the rest of gcode [crates/gcode/src/db/mod.rs:16-20].

4. For standalone PostgreSQL setup, `run_standalone_setup` validates the request, constructs `GcodeStandaloneSetup` from the requested schema, and opens a PostgreSQL transaction .

5. If `overwrite_code_index` is set, setup attempts to reset the gcode-owned code-index relations first. If that reset fails, the failure is recorded as `"code-index overwrite reset"` and returned in standalone setup status instead of continuing .

6. If overwrite is not set, setup runs `ensure_postgres_code_index_compatible`. That function reports success when no incompatible relations are found, or returns `SetupError::CreationFailed` with a preflight failure message and overwrite guidance when conflicts exist [crates/gcode/src/setup/postgres.rs:85-101].

7. Compatibility inspection walks both table and index contracts for the schema. `incompatible_postgres_code_index_relations` accumulates issues from catalog inspection and returns either the issue list or a setup error [crates/gcode/src/setup/postgres.rs:133-145]. `index_info` reads PostgreSQL catalogs for a named object and returns relation kind, owning table, and access method when found [crates/gcode/src/setup/postgres.rs:264-292].

8. Setup builds a `SetupContext` with `pg: Some(&mut tx)` and no FalkorDB or Qdrant config, then calls `GcodeStandaloneSetup::create` . The DDL layer emits PostgreSQL object definitions including `pg_search` and the code-index tables .

9. `create` executes owned objects in order, records created names, and on the first error records the failure, marks remaining objects as skipped, and returns the accumulated report instead of propagating that object error [crates/gcode/src/setup/ddl.rs:294-308].

10. Each PostgreSQL object is executed through `execute_postgres_ddl`. If the setup context has no PostgreSQL connection, it returns `ConnectionFailed`; if `batch_execute` fails, it maps the failure to `SetupError::CreationFailed` for that object [crates/gcode/src/setup/ddl.rs:321-338].

11. If no object failures were recorded, the transaction commits. If failures exist, setup clears `created` and `skipped` before returning status, so callers do not treat partially attempted setup as successfully created objects .

## Key components

The important symbols are the facades and contracts that keep setup deterministic: schema ownership lives in `GcodeStandaloneSetup`, compatibility expectations live in table/index contracts, and PostgreSQL inspection/execution functions enforce those expectations before DDL is committed.

| Symbol | Role |
| --- | --- |
| `GcodeStandaloneSetup` | Holds the target schema and produces qualified PostgreSQL object definitions for standalone setup [crates/gcode/src/setup/ddl.rs:8-10] |
| `TableContract` | Defines expected code-index tables and required columns [crates/gcode/src/setup/contracts.rs:5-8] |
| `IndexContract` | Defines expected index name, target table, and index method [crates/gcode/src/setup/contracts.rs:10-14] |
| `ensure_postgres_code_index_compatible` | Preflights existing relations and raises overwrite guidance on incompatibility [crates/gcode/src/setup/postgres.rs:85-101] |
| `execute_postgres_ddl` | Runs DDL through the setup PostgreSQL connection and reports missing connection or execution failures [crates/gcode/src/setup/ddl.rs:321-338] |

## Where to start

Start with `crates/gcode/src/config.rs` to see the public configuration facade and the exported runtime concepts [crates/gcode/src/config.rs:1-25]. Then read `GcodeStandaloneSetup` for how standalone PostgreSQL objects are defined and created [crates/gcode/src/setup/ddl.rs:8-10]. For the safety checks around existing schemas, read `ensure_postgres_code_index_compatible` next [crates/gcode/src/setup/postgres.rs:85-101].

## Explore

- [[code/modules/crates/gcode/src/config|crates/gcode/src/config]]
- [[code/modules/crates/gcode/src/db|crates/gcode/src/db]]
- [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

