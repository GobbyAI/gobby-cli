---
title: crates/gcode/src/setup/postgres.rs
type: code_file
provenance:
- file: crates/gcode/src/setup/postgres.rs
  ranges:
  - 12-57
  - 59-77
  - 85-101
  - 103-114
  - 116-131
  - 133-145
  - 147-179
  - 181-212
  - 214-232
  - 234-256
  - 258-262
  - 264-292
  - 294-308
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/setup/postgres.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Purpose

This file implements PostgreSQL-backed standalone setup for gcode. `run_standalone_setup` validates the request, optionally resets or compatibility-checks the existing code-index schema, runs the setup inside a transaction, and converts the resulting `SetupReport` into a `StandaloneSetupStatus`; the rest of the file is the support layer for that flow, including status mapping, schema-contract inspection, catalog queries for tables and indexes, reset SQL generation, and request validation against the required standalone/public schema.
[crates/gcode/src/setup/postgres.rs:12-57]
[crates/gcode/src/setup/postgres.rs:59-77]
[crates/gcode/src/setup/postgres.rs:85-101]
[crates/gcode/src/setup/postgres.rs:103-114]
[crates/gcode/src/setup/postgres.rs:116-131]

## API Symbols

- `run_standalone_setup` (function) component `run_standalone_setup [function]` (`11681dec-a19e-5e08-b39e-19ee0b3f0498`) lines 12-57 [crates/gcode/src/setup/postgres.rs:12-57]
  - Signature: `pub fn run_standalone_setup(`
  - Purpose: Validates a standalone setup request, conditionally manages PostgreSQL code index state (reset or compatibility check), executes setup creation within a transaction, and returns the operation status with results. [crates/gcode/src/setup/postgres.rs:12-57]
- `standalone_setup_status` (function) component `standalone_setup_status [function]` (`89cace5d-69f7-5df5-a793-f42f65af553c`) lines 59-77 [crates/gcode/src/setup/postgres.rs:59-77]
  - Signature: `fn standalone_setup_status(`
  - Purpose: Transforms a `GcodeStandaloneSetup` and `SetupReport` into a `StandaloneSetupStatus` struct by extracting namespace/schema metadata, propagating setup metrics (created/skipped counts), and converting failed entries into structured `StandaloneFailure` objects. [crates/gcode/src/setup/postgres.rs:59-77]
- `ensure_postgres_code_index_compatible` (function) component `ensure_postgres_code_index_compatible [function]` (`e574eea3-b6bc-5388-a882-5c5e664ff8d9`) lines 85-101 [crates/gcode/src/setup/postgres.rs:85-101]
  - Signature: `pub(crate) fn ensure_postgres_code_index_compatible(`
  - Purpose: This function validates that the existing PostgreSQL code-index relations are compatible with the specified schema, returning a `SetupError` if incompatibilities are detected. [crates/gcode/src/setup/postgres.rs:85-101]
- `reset_postgres_code_index` (function) component `reset_postgres_code_index [function]` (`dc7786dc-8f65-54b0-bdc0-a259549f1298`) lines 103-114 [crates/gcode/src/setup/postgres.rs:103-114]
  - Signature: `pub(crate) fn reset_postgres_code_index(`
  - Purpose: Executes a schema-specific SQL reset operation on a PostgreSQL code-index, converting any client execution errors to a SetupError. [crates/gcode/src/setup/postgres.rs:103-114]
- `postgres_overwrite_reset_sql` (function) component `postgres_overwrite_reset_sql [function]` (`77341870-4d98-5e54-be3e-43a1ebabf437`) lines 116-131 [crates/gcode/src/setup/postgres.rs:116-131]
  - Signature: `pub(crate) fn postgres_overwrite_reset_sql(schema: &str) -> Result<String, SetupError> {`
  - Purpose: Generates a SQL string containing DROP INDEX and DROP TABLE statements for all code index tables and indexes in the specified schema, with tables dropped in reverse order. [crates/gcode/src/setup/postgres.rs:116-131]
- `incompatible_postgres_code_index_relations` (function) component `incompatible_postgres_code_index_relations [function]` (`235f4be8-628e-5fc2-adf5-172e0cc94e9d`) lines 133-145 [crates/gcode/src/setup/postgres.rs:133-145]
  - Signature: `fn incompatible_postgres_code_index_relations(`
  - Purpose: Validates PostgreSQL table and index schema contracts against a specified schema, accumulating and returning any identified incompatibilities as a vector of strings. [crates/gcode/src/setup/postgres.rs:133-145]
- `inspect_table_contract` (function) component `inspect_table_contract [function]` (`a3b0568e-44cd-5cc2-a219-b916c0dd8b26`) lines 147-179 [crates/gcode/src/setup/postgres.rs:147-179]
  - Signature: `fn inspect_table_contract(`
  - Purpose: Validates that a table exists as an ordinary relation and contains all required columns specified in a `TableContract`, accumulating validation failures to an issues vector. [crates/gcode/src/setup/postgres.rs:147-179]
- `inspect_index_contract` (function) component `inspect_index_contract [function]` (`f312243d-71fa-5712-96a3-9cf9f738e90a`) lines 181-212 [crates/gcode/src/setup/postgres.rs:181-212]
  - Signature: `fn inspect_index_contract(`
  - Purpose: Verifies a PostgreSQL index's metadata (relkind, table attachment, and access method) against an `IndexContract` specification, recording any validation failures in the provided issues vector. [crates/gcode/src/setup/postgres.rs:181-212]
- `relation_kind` (function) component `relation_kind [function]` (`97bf37d5-752a-5416-93b2-11b6302a37e6`) lines 214-232 [crates/gcode/src/setup/postgres.rs:214-232]
  - Signature: `fn relation_kind(`
  - Purpose: Queries PostgreSQL's system catalog to retrieve the relkind (relation type code) for a schema-qualified relation, returning `None` if the relation does not exist. [crates/gcode/src/setup/postgres.rs:214-232]
- `table_columns` (function) component `table_columns [function]` (`c0d54b4e-fe77-5139-b186-661ebd52cf67`) lines 234-256 [crates/gcode/src/setup/postgres.rs:234-256]
  - Signature: `fn table_columns(`
  - Purpose: Retrieves the set of non-dropped column names for a specified PostgreSQL table by querying the system catalog. [crates/gcode/src/setup/postgres.rs:234-256]
- `ExistingIndexInfo` (class) component `ExistingIndexInfo [class]` (`1aa5e932-55e1-536a-99c9-c17d14a1c796`) lines 258-262 [crates/gcode/src/setup/postgres.rs:258-262]
  - Signature: `struct ExistingIndexInfo {`
  - Purpose: `ExistingIndexInfo` is a struct that encapsulates metadata about an existing database index, containing a required relation kind string and optional table name and indexing method fields. [crates/gcode/src/setup/postgres.rs:258-262]
- `index_info` (function) component `index_info [function]` (`50e1ea5f-6e3b-53e0-84ac-db6ec5a79d96`) lines 264-292 [crates/gcode/src/setup/postgres.rs:264-292]
  - Signature: `fn index_info(`
  - Purpose: Retrieves metadata for a specified PostgreSQL index in a given schema, including its relation kind, indexed table name, and access method. [crates/gcode/src/setup/postgres.rs:264-292]
- `validate_standalone_request` (function) component `validate_standalone_request [function]` (`45d1441b-1225-5a18-987b-bf8deff951da`) lines 294-308 [crates/gcode/src/setup/postgres.rs:294-308]
  - Signature: `pub fn validate_standalone_request(request: &StandaloneSetupRequest) -> Result<(), SetupError> {`
  - Purpose: Validates that a `StandaloneSetupRequest` has the `standalone` flag enabled and uses the `DEFAULT_SCHEMA` ("public") to ensure the daemon can adopt the code-index tables. [crates/gcode/src/setup/postgres.rs:294-308]

