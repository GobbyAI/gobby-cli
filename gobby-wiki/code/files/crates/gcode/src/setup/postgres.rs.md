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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/setup/postgres.rs:12-57](crates/gcode/src/setup/postgres.rs#L12-L57), [crates/gcode/src/setup/postgres.rs:59-77](crates/gcode/src/setup/postgres.rs#L59-L77), [crates/gcode/src/setup/postgres.rs:85-101](crates/gcode/src/setup/postgres.rs#L85-L101), [crates/gcode/src/setup/postgres.rs:103-114](crates/gcode/src/setup/postgres.rs#L103-L114), [crates/gcode/src/setup/postgres.rs:116-131](crates/gcode/src/setup/postgres.rs#L116-L131), [crates/gcode/src/setup/postgres.rs:133-145](crates/gcode/src/setup/postgres.rs#L133-L145), [crates/gcode/src/setup/postgres.rs:147-179](crates/gcode/src/setup/postgres.rs#L147-L179), [crates/gcode/src/setup/postgres.rs:181-212](crates/gcode/src/setup/postgres.rs#L181-L212), [crates/gcode/src/setup/postgres.rs:214-232](crates/gcode/src/setup/postgres.rs#L214-L232), [crates/gcode/src/setup/postgres.rs:234-256](crates/gcode/src/setup/postgres.rs#L234-L256), [crates/gcode/src/setup/postgres.rs:258-262](crates/gcode/src/setup/postgres.rs#L258-L262), [crates/gcode/src/setup/postgres.rs:264-292](crates/gcode/src/setup/postgres.rs#L264-L292), [crates/gcode/src/setup/postgres.rs:294-308](crates/gcode/src/setup/postgres.rs#L294-L308)

</details>

# crates/gcode/src/setup/postgres.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Purpose

Implements PostgreSQL-backed standalone setup for Gcode: it validates a request, opens a transaction, optionally resets an existing code index or checks that it is compatible, runs the `GcodeStandaloneSetup` creation flow, and commits on success. The helper functions break that work into status shaping, compatibility inspection, index reset SQL generation, relation and column introspection, and request validation so the setup can report created, skipped, and failed objects in a `StandaloneSetupStatus`.
[crates/gcode/src/setup/postgres.rs:12-57]
[crates/gcode/src/setup/postgres.rs:59-77]
[crates/gcode/src/setup/postgres.rs:85-101]
[crates/gcode/src/setup/postgres.rs:103-114]
[crates/gcode/src/setup/postgres.rs:116-131]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `run_standalone_setup` | function | `pub fn run_standalone_setup(` | `run_standalone_setup [function]` | `11681dec-a19e-5e08-b39e-19ee0b3f0498` | 12-57 [crates/gcode/src/setup/postgres.rs:12-57] | Indexed function `run_standalone_setup` in `crates/gcode/src/setup/postgres.rs`. [crates/gcode/src/setup/postgres.rs:12-57] |
| `standalone_setup_status` | function | `fn standalone_setup_status(` | `standalone_setup_status [function]` | `89cace5d-69f7-5df5-a793-f42f65af553c` | 59-77 [crates/gcode/src/setup/postgres.rs:59-77] | Indexed function `standalone_setup_status` in `crates/gcode/src/setup/postgres.rs`. [crates/gcode/src/setup/postgres.rs:59-77] |
| `ensure_postgres_code_index_compatible` | function | `pub(crate) fn ensure_postgres_code_index_compatible(` | `ensure_postgres_code_index_compatible [function]` | `e574eea3-b6bc-5388-a882-5c5e664ff8d9` | 85-101 [crates/gcode/src/setup/postgres.rs:85-101] | Indexed function `ensure_postgres_code_index_compatible` in `crates/gcode/src/setup/postgres.rs`. [crates/gcode/src/setup/postgres.rs:85-101] |
| `reset_postgres_code_index` | function | `pub(crate) fn reset_postgres_code_index(` | `reset_postgres_code_index [function]` | `dc7786dc-8f65-54b0-bdc0-a259549f1298` | 103-114 [crates/gcode/src/setup/postgres.rs:103-114] | Indexed function `reset_postgres_code_index` in `crates/gcode/src/setup/postgres.rs`. [crates/gcode/src/setup/postgres.rs:103-114] |
| `postgres_overwrite_reset_sql` | function | `pub(crate) fn postgres_overwrite_reset_sql(schema: &str) -> Result<String, SetupError> {` | `postgres_overwrite_reset_sql [function]` | `77341870-4d98-5e54-be3e-43a1ebabf437` | 116-131 [crates/gcode/src/setup/postgres.rs:116-131] | Indexed function `postgres_overwrite_reset_sql` in `crates/gcode/src/setup/postgres.rs`. [crates/gcode/src/setup/postgres.rs:116-131] |
| `incompatible_postgres_code_index_relations` | function | `fn incompatible_postgres_code_index_relations(` | `incompatible_postgres_code_index_relations [function]` | `235f4be8-628e-5fc2-adf5-172e0cc94e9d` | 133-145 [crates/gcode/src/setup/postgres.rs:133-145] | Indexed function `incompatible_postgres_code_index_relations` in `crates/gcode/src/setup/postgres.rs`. [crates/gcode/src/setup/postgres.rs:133-145] |
| `inspect_table_contract` | function | `fn inspect_table_contract(` | `inspect_table_contract [function]` | `a3b0568e-44cd-5cc2-a219-b916c0dd8b26` | 147-179 [crates/gcode/src/setup/postgres.rs:147-179] | Indexed function `inspect_table_contract` in `crates/gcode/src/setup/postgres.rs`. [crates/gcode/src/setup/postgres.rs:147-179] |
| `inspect_index_contract` | function | `fn inspect_index_contract(` | `inspect_index_contract [function]` | `f312243d-71fa-5712-96a3-9cf9f738e90a` | 181-212 [crates/gcode/src/setup/postgres.rs:181-212] | Indexed function `inspect_index_contract` in `crates/gcode/src/setup/postgres.rs`. [crates/gcode/src/setup/postgres.rs:181-212] |
| `relation_kind` | function | `fn relation_kind(` | `relation_kind [function]` | `97bf37d5-752a-5416-93b2-11b6302a37e6` | 214-232 [crates/gcode/src/setup/postgres.rs:214-232] | Indexed function `relation_kind` in `crates/gcode/src/setup/postgres.rs`. [crates/gcode/src/setup/postgres.rs:214-232] |
| `table_columns` | function | `fn table_columns(` | `table_columns [function]` | `c0d54b4e-fe77-5139-b186-661ebd52cf67` | 234-256 [crates/gcode/src/setup/postgres.rs:234-256] | Indexed function `table_columns` in `crates/gcode/src/setup/postgres.rs`. [crates/gcode/src/setup/postgres.rs:234-256] |
| `ExistingIndexInfo` | class | `struct ExistingIndexInfo {` | `ExistingIndexInfo [class]` | `1aa5e932-55e1-536a-99c9-c17d14a1c796` | 258-262 [crates/gcode/src/setup/postgres.rs:258-262] | Indexed class `ExistingIndexInfo` in `crates/gcode/src/setup/postgres.rs`. [crates/gcode/src/setup/postgres.rs:258-262] |
| `index_info` | function | `fn index_info(` | `index_info [function]` | `50e1ea5f-6e3b-53e0-84ac-db6ec5a79d96` | 264-292 [crates/gcode/src/setup/postgres.rs:264-292] | Indexed function `index_info` in `crates/gcode/src/setup/postgres.rs`. [crates/gcode/src/setup/postgres.rs:264-292] |
| `validate_standalone_request` | function | `pub fn validate_standalone_request(request: &StandaloneSetupRequest) -> Result<(), SetupError> {` | `validate_standalone_request [function]` | `45d1441b-1225-5a18-987b-bf8deff951da` | 294-308 [crates/gcode/src/setup/postgres.rs:294-308] | Indexed function `validate_standalone_request` in `crates/gcode/src/setup/postgres.rs`. [crates/gcode/src/setup/postgres.rs:294-308] |
