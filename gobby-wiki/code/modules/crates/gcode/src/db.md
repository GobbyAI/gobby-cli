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

`crates/gcode/src/db` is the gcode database boundary: it resolves the hub PostgreSQL DSN, opens read/write or read-only connections, validates the runtime schema, delegates config reads to `gobby_core`, and re-exports the query and resolution APIs from its submodules (`crates/gcode/src/db/mod.rs:1-36`). Its query layer works over `postgres::GenericClient` and the gcode model types to read indexed file paths, project/file existence, graph facts, and graph sync state from hub tables such as `code_indexed_files` and `code_indexed_projects` (`crates/gcode/src/db/queries.rs:1-100`).

The main connection flow is `resolve_database_url()` followed by `connect_readwrite()` or `connect_readonly()`. URL resolution uses Gobby home/bootstrap state, environment overrides, a local daemon broker, reachability checks through `gobby_core::postgres::connect_readonly`, and hub identity probing through `gobby_core::provisioning::probe_postgres_hub_identity` (`crates/gcode/src/db/resolution.rs:23-45`). The module intentionally has no local database fallback: it asks the daemon broker first, then falls back to explicit DSN sources for daemonless operation (`crates/gcode/src/db/resolution.rs:31-34`).

Collaboration points are explicit: this module imports `gobby_core::postgres`, `gobby_core::provisioning`, `postgres`, `serde`, and `anyhow`, while callers import `db::*` through the re-exports in `mod.rs` (`crates/gcode/src/db/mod.rs:1-7`, `crates/gcode/src/db/resolution.rs:1-8`). The query layer calls into `crate::models` for graph data shapes and `crate::utils::i64_to_usize`, so it sits between database rows and higher-level indexed-code representations (`crates/gcode/src/db/queries.rs:1-6`).

| Public API | Responsibility | Citation |
| --- | --- | --- |
| `connect_readwrite(database_url)` | Opens a writable hub connection and validates runtime schema. | `crates/gcode/src/db/mod.rs:12-17` |
| `connect_readonly(database_url)` | Opens a read-only hub connection and validates runtime schema. | `crates/gcode/src/db/mod.rs:24-29` |
| `read_config_value(conn, key)` | Reads a Postgres-backed config value through `gobby_core`. | `crates/gcode/src/db/mod.rs:32-34` |
| `list_indexed_file_paths` | Lists indexed files for a project. | `crates/gcode/src/db/queries.rs:13-24` |
| `read_graph_file_facts` | Aggregates imports, definitions, and calls for one file. | `crates/gcode/src/db/queries.rs:36-51` |
| `resolve_database_url` | Resolves the PostgreSQL hub DSN from broker/env/bootstrap sources. | `crates/gcode/src/db/resolution.rs:29-45` |

| Environment Variable | Purpose | Citation |
| --- | --- | --- |
| `GCODE_DATABASE_URL` | gcode-specific database URL override. | `crates/gcode/src/db/resolution.rs:8-10` |
| `GOBBY_POSTGRES_DSN` | fallback Gobby PostgreSQL DSN. | `crates/gcode/src/db/resolution.rs:8-10` |
| `GCODE_BROKER_TIMEOUT_MS` | broker timeout override; default is 7000 ms. | `crates/gcode/src/db/resolution.rs:10-13` |
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

