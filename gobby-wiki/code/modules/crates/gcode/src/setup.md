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

## crates/gcode/src/setup

This module is responsible for provisioning the gcode code-index schema inside a PostgreSQL database. It owns the full lifecycle of the standalone setup: validating a caller-supplied request, optionally wiping incompatible objects, generating schema-qualified DDL for every table, index, and extension the code-index requires, executing that DDL inside a single transaction, and returning a structured status report. The module is the sole authority on what constitutes a "compatible" code-index schema and what SQL must be executed to create or recreate one.

The central orchestrator is `run_standalone_setup` (postgres.rs:12), which drives the flow: it calls `validate_standalone_request`, constructs a `GcodeStandaloneSetup` instance, opens a Postgres transaction, conditionally calls `reset_postgres_code_index` or `ensure_postgres_code_index_compatible`, delegates object creation to `setup.create(&mut ctx)` (the `StandaloneSetup` trait from `gobby_core`), commits only when all objects succeed, and wraps the result in a `StandaloneSetupStatus`. Identifier safety is enforced throughout by `quote_identifier` (identifiers.rs) and `qualified_relation` (identifiers.rs), both of which are called before any SQL is assembled so that schema names and relation names are always double-quoted and byte-length-validated against Postgres's 63-byte limit.

The module integrates tightly with `gobby_core::setup` (imported at postgres.rs:8 and ddl.rs:3): `GcodeStandaloneSetup` implements the `StandaloneSetup` trait, surfacing `namespace`, `schema`, `owned_objects`, and `create`. The `owned_objects` method enumerates every `OwnedObject` with `StoreKind::Postgres`, covering tables (`code_indexed_projects`, `code_indexed_files`, `code_symbols`, `code_content_chunks`, `code_imports`, `code_calls`), indexes (BM25 and others), and the `pg_search` extension; tests at tests.rs:10–50 assert that no gobby-internal objects (e.g. `config_store`, `secrets`, `schema_migrations`) are accidentally declared. The `Redacted` wrapper type (types.rs:5) is applied to any secret field (`database_url`, `embedding_api_key`, `falkordb_password`) so that `Debug` and JSON serialization never leak credentials, a property verified by dedicated tests at tests.rs (components `standalone_setup_request_redacts_password_in_json`, `standalone_setup_request_debug_redacts_database_url`).

### Public API Symbols

| Symbol | Kind | Location | Purpose |
|---|---|---|---|
| `GcodeStandaloneSetup` | struct | ddl.rs | Schema-aware DDL builder; implements `StandaloneSetup` |
| `GcodeStandaloneSetup::new` | method | ddl.rs | Construct with a target schema name |
| `GcodeStandaloneSetup::schema` | method | ddl.rs | Return the configured schema |
| `GcodeStandaloneSetup::namespace` | method | ddl.rs | Returns `"gcode"` constant namespace |
| `GcodeStandaloneSetup::owned_objects` | method | ddl.rs | Enumerate all `OwnedObject` records |
| `GcodeStandaloneSetup::create` | method | ddl.rs | Execute DDL via `SetupContext` |
| `PostgresObjectDefinition` | struct | ddl.rs | Internal name+SQL pair for a single DDL statement |
| `run_standalone_setup` | fn | postgres.rs:12 | Top-level entry point; validates, resets, creates, commits |
| `standalone_setup_status` | fn | postgres.rs | Converts `SetupReport` into `StandaloneSetupStatus` |
| `ensure_postgres_code_index_compatible` | fn | postgres.rs | Aborts if schema has incompatible objects |
| `reset_postgres_code_index` | fn | postgres.rs | Drops and recreates all code-index relations |
| `postgres_overwrite_reset_sql` | fn | postgres.rs | Generates allowlisted DROP/reset SQL |
| `incompatible_postgres_code_index_relations` | fn | postgres.rs | Detects schema mismatches |
| `execute_postgres_ddl` | fn | postgres.rs | Low-level DDL executor |
| `quote_identifier` | fn | identifiers.rs | Double-quotes and validates a Postgres identifier |
| `qualified_relation` | fn | identifiers.rs | Produces `"schema"."relation"` form |
| `code_index_table_names` | fn | contracts.rs | Returns canonical code-index table name set |
| `code_index_index_names` | fn | contracts.rs | Returns canonical code-index index name set |
| `TableContract` | struct | contracts.rs | Declarative contract for expected table columns |
| `IndexContract` | struct | contracts.rs | Declarative contract for expected index definitions |
| `StandaloneSetupRequest` | struct | types.rs:40 | Caller-supplied parameters; secrets held in `Redacted` fields |
| `StandaloneSetupStatus` | struct | types.rs | Outcome report with `created`, `skipped`, `failed` lists |
| `StandaloneFailure` | struct | types.rs | Per-object failure record serialized as a JSON object |
| `StandaloneServicesStatus` | struct | types.rs | Optional service-level status attached to setup output |
| `Redacted` | struct | types.rs:5 | `Option<String>` newtype that prints `<redacted>` in `Debug` |

### StandaloneSetupRequest Fields

| Field | Type | Serialized | Purpose |
|---|---|---|---|
| `standalone` | `bool` | yes | Activates standalone mode |
| `database_url` | `Redacted` | **no** | Setup-only Postgres URL; never written to JSON |
| `schema` | `String` | yes | Target Postgres schema (default `public`) |
| `overwrite_code_index` | `bool` | yes | Drop and recreate incompatible objects |
| `no_services` | `bool` | yes | Skip external service provisioning |
| `embedding_provider/model/api_base/query_prefix/vector_dim` | various | yes | Embedding configuration |
| `embedding_api_key` | `Redacted` | **no** | Embedding secret; redacted in Debug and JSON |
| `falkordb_host/port` | `Option<…>` | yes | FalkorDB connection details |
| `falkordb_password` | `Redacted` | **no** | FalkorDB secret; redacted |
| `qdrant_url` | `Option<String>` | yes | Qdrant connection URL |

### Cross-Module Collaboration

| Direction | Counterpart | What is exchanged |
|---|---|---|
| Imports | `gobby_core::setup` (postgres.rs:8, ddl.rs:3) | `StandaloneSetup`, `SetupContext`, `SetupError`, `SetupReport`, `OwnedObject`, `StoreKind` |
| Imports | `postgres` crate (postgres.rs:9) | `Client`, `GenericClient` for DDL execution |
| Implements | `gobby_core::setup::StandaloneSetup` | `GcodeStandaloneSetup` satisfies the trait (verified at tests.rs:56) |
| Called by | Parent `crates/gcode` entry points | `run_standalone_setup` is the public boundary invoked by CLI/service orchestration |
[crates/gcode/src/setup/contracts.rs:5-8]
[crates/gcode/src/setup/ddl.rs:8-10]
[crates/gcode/src/setup/identifiers.rs:5-15]
[crates/gcode/src/setup/postgres.rs:12-57]
[crates/gcode/src/setup/tests.rs:12-55]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/setup/contracts.rs\|crates/gcode/src/setup/contracts.rs]] | `crates/gcode/src/setup/contracts.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/setup/ddl.rs\|crates/gcode/src/setup/ddl.rs]] | `crates/gcode/src/setup/ddl.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gcode/src/setup/identifiers.rs\|crates/gcode/src/setup/identifiers.rs]] | `crates/gcode/src/setup/identifiers.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gcode/src/setup/postgres.rs\|crates/gcode/src/setup/postgres.rs]] | `crates/gcode/src/setup/postgres.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gcode/src/setup/tests.rs\|crates/gcode/src/setup/tests.rs]] | `crates/gcode/src/setup/tests.rs` exposes 24 indexed API symbols. |
| [[code/files/crates/gcode/src/setup/types.rs\|crates/gcode/src/setup/types.rs]] | `crates/gcode/src/setup/types.rs` exposes 14 indexed API symbols. |

