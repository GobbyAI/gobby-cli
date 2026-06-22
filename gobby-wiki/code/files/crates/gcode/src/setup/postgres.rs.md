---
title: crates/gcode/src/setup/postgres.rs
type: code_file
provenance:
- file: crates/gcode/src/setup/postgres.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/setup/postgres.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Overview

`crates/gcode/src/setup/postgres.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gcode/src/setup/postgres.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `run_standalone_setup` | function | Validates a standalone setup request, opens a PostgreSQL transaction, optionally resets or verifies code-index compatibility, runs 'GcodeStandaloneSetup::create' in a non-interactive 'SetupContext', commits only if creation succeeded without failures, and returns a 'StandaloneSetupStatus' derived from the resulting 'SetupReport' or a 'SetupError' on transaction/setup failure. [crates/gcode/src/setup/postgres.rs:12-57] |
| `standalone_setup_status` | function | Constructs a 'StandaloneSetupStatus' from a 'GcodeStandaloneSetup' and 'SetupReport' by copying the setup namespace and schema, transferring 'created' and 'skipped', converting each '(name, reason)' failure into a 'StandaloneFailure', and setting 'config_file', 'services', and 'embedding' to 'None'. [crates/gcode/src/setup/postgres.rs:59-77] |
| `ensure_postgres_code_index_compatible` | function | Checks for incompatible PostgreSQL code-index relations in the given schema and returns 'Ok(())' when none are found, otherwise raises 'SetupError::CreationFailed' with a preflight failure message listing the issues and overwrite guidance. [crates/gcode/src/setup/postgres.rs:85-101] |
| `reset_postgres_code_index` | function | Builds the schema-specific PostgreSQL overwrite-reset SQL for the code index and executes it via 'batch_execute', mapping any database error into 'SetupError::CreationFailed' for the 'code-index overwrite reset' object. [crates/gcode/src/setup/postgres.rs:103-114] |
| `postgres_overwrite_reset_sql` | function | Generates a newline-separated PostgreSQL reset script for the given schema by emitting 'DROP INDEX IF EXISTS' statements for all code-index index names and then 'DROP TABLE IF EXISTS' statements for all code-index table names in reverse order, returning any qualification error as 'SetupError'. [crates/gcode/src/setup/postgres.rs:116-131] |
| `incompatible_postgres_code_index_relations` | function | Iterates over all table and index contracts for the given PostgreSQL schema, inspects each against the database via 'client', accumulates any compatibility issues into a 'Vec<String>', and returns them or a 'SetupError' if inspection fails. [crates/gcode/src/setup/postgres.rs:133-145] |
| `inspect_table_contract` | function | Checks whether a named relation in a schema exists as an ordinary table and records issues if it is a non-table relation or if any required contract columns are missing, returning 'Ok(())' otherwise. [crates/gcode/src/setup/postgres.rs:147-179] |
| `inspect_index_contract` | function | Checks whether an existing catalog object for 'contract.name' is an index and, if so, verifies that it is attached to the expected table and uses the expected access method, appending mismatch messages to 'issues' and returning 'Ok(())' even when the index is absent. [crates/gcode/src/setup/postgres.rs:181-212] |
| `relation_kind` | function | Queries PostgreSQL 'pg_class'/'pg_namespace' for a relation named by 'schema' and 'relation', returning 'Ok(Some(relkind))' if found, 'Ok(None)' if absent, or 'SetupError::CreationFailed' if the lookup query fails. [crates/gcode/src/setup/postgres.rs:214-232] |
| `table_columns` | function | Queries PostgreSQL system catalogs for the named schema/table and returns a 'HashSet<String>' of all non-dropped, user-defined column names, mapping any query failure to 'SetupError::CreationFailed' with a '{table} preflight' object label. [crates/gcode/src/setup/postgres.rs:234-256] |
| `ExistingIndexInfo` | class | 'ExistingIndexInfo' is a data container for an existing relation’s kind plus optional associated table name and index method, with fields 'relkind: String', 'table_name: Option<String>', and 'method: Option<String>'. [crates/gcode/src/setup/postgres.rs:258-262] |
| `index_info` | function | Queries PostgreSQL system catalogs for a named object in a schema and returns 'Ok(Some(ExistingIndexInfo))' with its 'relkind', owning table name, and access method if found, otherwise 'Ok(None)', mapping query failures to 'SetupError::CreationFailed'. [crates/gcode/src/setup/postgres.rs:264-292] |
| `validate_standalone_request` | function | Returns 'Ok(())' only when the request is in standalone mode and uses the 'public' schema, otherwise it rejects attached mode or any non-'public' schema with a 'SetupError'. [crates/gcode/src/setup/postgres.rs:294-308] |

