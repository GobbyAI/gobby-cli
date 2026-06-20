---
title: crates/gcode/src/setup
type: code_module
provenance:
- file: crates/gcode/src/setup/contracts.rs
- file: crates/gcode/src/setup/ddl.rs
- file: crates/gcode/src/setup/identifiers.rs
- file: crates/gcode/src/setup/postgres.rs
- file: crates/gcode/src/setup/tests.rs
- file: crates/gcode/src/setup/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/setup

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/setup` owns standalone provisioning for the gcode PostgreSQL code index: request/status DTOs, secret redaction, DDL construction, identifier qualification, catalog contracts, compatibility checks, and reset helpers. `GcodeStandaloneSetup` carries a schema, qualifies relations, emits PostgreSQL object definitions, and implements the `gobby_core::setup::StandaloneSetup` contract; its DDL includes `pg_search` plus code-index tables such as `code_indexed_projects`, `code_indexed_files`, `code_symbols`, `code_content_chunks`, `code_imports`, and `code_calls` (`crates/gcode/src/setup/ddl.rs:1-100`).

The main flow is `run_standalone_setup`: validate the `StandaloneSetupRequest`, create `GcodeStandaloneSetup` from the requested schema, open a PostgreSQL transaction, either reset incompatible code-index relations when overwrite is enabled or check compatibility otherwise, then call `setup.create` through a `SetupContext` and commit only if the setup report has no failures (`crates/gcode/src/setup/postgres.rs:1-100`). Status output is normalized into `StandaloneSetupStatus`, with failures converted into structured `StandaloneFailure` objects (`crates/gcode/src/setup/postgres.rs:1-100`).

This module collaborates upward with `gobby_core::setup` by importing `SetupContext`, `SetupError`, `SetupReport`, `StandaloneSetup`, `OwnedObject`, and `StoreKind`; PostgreSQL execution is mediated through `postgres::Client`/`GenericClient` (`crates/gcode/src/setup/postgres.rs:1-100`, `crates/gcode/src/setup/ddl.rs:1-100`). Tests verify that standalone setup declares only the public daemon code-index subset, uses namespace `gcode`, defaults to schema `public`, targets `StoreKind::Postgres`, includes expected code-index objects, and excludes broader daemon/core objects such as config, migrations, secrets, project JSON, and sync-state tables (`crates/gcode/src/setup/tests.rs:1-100`).

| Public API / Type | Responsibility |
| --- | --- |
| `GcodeStandaloneSetup` | Schema-scoped standalone setup implementation |
| `run_standalone_setup` | Transactional setup entry point |
| `ensure_postgres_code_index_compatible` | Preflight compatibility check |
| `reset_postgres_code_index` | Overwrite/reset path for incompatible relations |
| `postgres_overwrite_reset_sql` | Reset SQL generation |
| `quote_identifier` / `qualified_relation` | PostgreSQL-safe identifier handling |
| `TableContract` / `IndexContract` | Expected catalog contract definitions |
| `StandaloneSetupRequest` | Setup input, including schema and service options |
| `StandaloneSetupStatus` | Setup result with created/skipped/failed objects |
| `Redacted` | Secret wrapper that suppresses sensitive debug/JSON output |

| Request Field | Purpose |
| --- | --- |
| `standalone` | Enables standalone setup mode |
| `database_url` | Setup-only PostgreSQL URL, redacted and skipped in JSON |
| `no_services` | Disables service provisioning |
| `overwrite_code_index` | Allows destructive code-index reset |
| `schema` | Target PostgreSQL schema, defaulted from `DEFAULT_SCHEMA` |
| `embedding_*` | Embedding provider/model/API/vector configuration |
| `falkordb_*` | FalkorDB host/port/password provisioning inputs |
| `qdrant_url` | Qdrant service endpoint |
[crates/gcode/src/setup/contracts.rs:5-8]
[crates/gcode/src/setup/ddl.rs:8-10]
[crates/gcode/src/setup/postgres.rs:12-57]
[crates/gcode/src/setup/tests.rs:12-55]
[crates/gcode/src/setup/identifiers.rs:5-15]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/setup/contracts.rs\|crates/gcode/src/setup/contracts.rs]] | `crates/gcode/src/setup/contracts.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/setup/ddl.rs\|crates/gcode/src/setup/ddl.rs]] | `crates/gcode/src/setup/ddl.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gcode/src/setup/identifiers.rs\|crates/gcode/src/setup/identifiers.rs]] | `crates/gcode/src/setup/identifiers.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gcode/src/setup/postgres.rs\|crates/gcode/src/setup/postgres.rs]] | `crates/gcode/src/setup/postgres.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gcode/src/setup/tests.rs\|crates/gcode/src/setup/tests.rs]] | `crates/gcode/src/setup/tests.rs` exposes 24 indexed API symbols. |
| [[code/files/crates/gcode/src/setup/types.rs\|crates/gcode/src/setup/types.rs]] | `crates/gcode/src/setup/types.rs` exposes 14 indexed API symbols. |

