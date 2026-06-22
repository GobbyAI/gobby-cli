---
title: crates/gcode/src/db
type: code_module
provenance:
- file: crates/gcode/src/db/mod.rs
- file: crates/gcode/src/db/queries.rs
- file: crates/gcode/src/db/resolution.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/db

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

## crates/gcode/src/db

The `db` module is the database access layer for the `gcode` crate. It is the single entry point through which all other `gcode` code opens PostgreSQL connections and executes queries against a Gobby hub. `mod.rs` (lines 1–36) re-exports everything from its two sub-files with `pub use queries::*` and `pub use resolution::*`, making the module a flat, unified surface. Every connection returned by this module is validated against the runtime schema via `schema::validate_runtime_schema` before being handed back to the caller, ensuring callers never receive a connection whose schema is stale or incompatible.

`resolution.rs` implements a layered, priority-ordered strategy for locating the PostgreSQL DSN at runtime. The top-level entry point is `resolve_database_url`, which delegates to `resolve_database_url_from_sources_with_identity_and_reachability` with concrete environment and filesystem dependencies injected. Resolution tries sources in the following order: environment variables, the long-lived daemon broker (via `resolve_brokered_database_url_at`), a `bootstrap.yaml` file in the Gobby home directory, and finally a `gcore` provisioning config file. The broker path contacts a loopback HTTP daemon, reading a `local_cli_token` from disk and enforcing that the daemon URL resolves only to loopback addresses before transmitting the token, preventing credential exfiltration (`validate_loopback_daemon_url`, `read_local_cli_token_at`, `request_broker_database_url`). Broker contact is bounded by a configurable timeout whose default is 7 000 ms (`DEFAULT_BROKER_TIMEOUT`) and whose override is read from `GCODE_BROKER_TIMEOUT_MS`.

`queries.rs` provides all SQL operations against the hub. It models per-file code graph facts through `GraphFileFacts`, which aggregates imports, symbol definitions, and call relations for a single file in one round-trip group. Functions follow a consistent signature of accepting a `&mut impl GenericClient` plus project/file coordinates. Coverage spans the full lifecycle of an indexed file: existence checks, listing, reading graph data, stamping sync attempts, recording successful syncs, writing new file facts, and deletion. Project-level operations (`indexed_project_exists`, `upsert_indexed_project`, `delete_indexed_project`) are also present.

### Public API

| Symbol | Kind | File |
|---|---|---|
| `connect_readwrite` | fn | `mod.rs:17` |
| `connect_readonly` | fn | `mod.rs:27` |
| `read_config_value` | fn | `mod.rs:33` |
| `resolve_database_url` | fn | `resolution.rs:39` |
| `gobby_home` | fn | `resolution.rs:28` |
| `bootstrap_path` | fn | `resolution.rs:32` |
| `resolve_brokered_database_url_at` | fn | `resolution.rs` |
| `parse_bootstrap_database` | fn | `resolution.rs` |
| `resolve_database_url_from_bootstrap_file` | fn | `resolution.rs` |
| `resolve_database_url_from_gcore_config` | fn | `resolution.rs` |
| `resolve_database_url_from_env` | fn | `resolution.rs` |
| `broker_timeout` | fn | `resolution.rs` |
| `list_indexed_file_paths` | fn | `queries.rs:15` |
| `indexed_project_exists` | fn | `queries.rs:23` |
| `indexed_file_exists` | fn | `queries.rs:55` |
| `read_graph_file_facts` | fn | `queries.rs:37` |
| `mark_graph_sync_attempted` | fn | `queries.rs:68` |
| `mark_graph_synced` | fn | `queries.rs:82` |
| `GraphFileFacts` | struct | `queries.rs:8` |

### Environment Variables

| Variable | Purpose | Default |
|---|---|---|
| `GCODE_DATABASE_URL` | Primary DSN override for gcode (`resolution.rs:9`) | — |
| `GOBBY_POSTGRES_DSN` | Fallback DSN shared with other Gobby tools (`resolution.rs:10`) | — |
| `GCODE_BROKER_TIMEOUT_MS` | Daemon broker contact timeout in milliseconds (`resolution.rs:11`) | `7000` |
| `GOBBY_HOME` | Override for the Gobby home directory (`resolution.rs:28`) | platform default |

### Resolution Priority Order

| Priority | Source |
|---|---|
| 1 | `GCODE_DATABASE_URL` environment variable |
| 2 | `GOBBY_POSTGRES_DSN` environment variable |
| 3 | Loopback daemon broker (authenticated via `local_cli_token`) |
| 4 | `bootstrap.yaml` inline URL in Gobby home |
| 5 | `gcore` provisioning config (`GCORE_CONFIG_FILENAME`) |

### External Collaboration

This module calls into `gobby_core::postgres` for the underlying connection primitives (`connect_readwrite`, `connect_readonly`, `read_config_value`) and into `gobby_core::provisioning` for `probe_postgres_hub_identity`, `StandaloneConfig`, and `GCORE_CONFIG_FILENAME` (`resolution.rs:6`). It calls `crate::schema::validate_runtime_schema` on every new connection (`mod.rs:19`, `mod.rs:29`). The rest of the `gcode` crate consumes this module's flat re-exported surface — primarily `resolve_database_url` to obtain a DSN and `connect_readwrite`/`connect_readonly` to open a validated client — without needing to interact with `queries` or `resolution` directly by name.
[crates/gcode/src/db/mod.rs:16-20]
[crates/gcode/src/db/queries.rs:8-13]
[crates/gcode/src/db/resolution.rs:16-18]
[crates/gcode/src/db/mod.rs:27-31]
[crates/gcode/src/db/mod.rs:33-35]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/db/mod.rs\|crates/gcode/src/db/mod.rs]] | `crates/gcode/src/db/mod.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/db/queries.rs\|crates/gcode/src/db/queries.rs]] | `crates/gcode/src/db/queries.rs` exposes 36 indexed API symbols. |
| [[code/files/crates/gcode/src/db/resolution.rs\|crates/gcode/src/db/resolution.rs]] | `crates/gcode/src/db/resolution.rs` exposes 55 indexed API symbols. |

