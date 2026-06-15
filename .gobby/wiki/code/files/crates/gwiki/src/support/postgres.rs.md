---
title: crates/gwiki/src/support/postgres.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/postgres.rs
  ranges:
  - 6-39
  - 41-51
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/postgres.rs

Module: [[code/modules/crates/gwiki/src/support|crates/gwiki/src/support]]

## Purpose

Provides PostgreSQL index checks for command handlers. `require_attached_index` resolves the configured database URL, opens a read-only connection, runs runtime schema validation against the attached PostgreSQL index, and turns missing config, connection failures, or schema mismatches into `WikiError::Config`. `require_postgres_index` is the lower-level helper that just resolves the database URL and returns a read-only `postgres::Client`, again mapping missing configuration or connection errors into command-specific config errors.
[crates/gwiki/src/support/postgres.rs:6-39]
[crates/gwiki/src/support/postgres.rs:41-51]

## API Symbols

- `require_attached_index` (function) component `require_attached_index [function]` (`e5e4bf14-b0e4-5ecf-a2e7-b9ca1e8a01db`) lines 6-39 [crates/gwiki/src/support/postgres.rs:6-39]
  - Signature: `pub(crate) fn require_attached_index(command: &'static str) -> Result<(), WikiError> {`
  - Purpose: Checks that a PostgreSQL hub is configured for 'command', opens a read-only connection, validates the runtime schema against the attached PostgreSQL index, and returns a 'WikiError::Config' if the hub is missing, the connection fails, or any schema requirements are unmet. [crates/gwiki/src/support/postgres.rs:6-39]
- `require_postgres_index` (function) component `require_postgres_index [function]` (`5f965f9d-b719-59de-84bd-72e703a7bc08`) lines 41-51 [crates/gwiki/src/support/postgres.rs:41-51]
  - Signature: `pub(crate) fn require_postgres_index(command: &'static str) -> Result<Client, WikiError> {`
  - Purpose: Returns a read-only PostgreSQL 'Client' for the given command by resolving the database URL from configuration and converting missing or connection failures into 'WikiError::Config' with command-specific details. [crates/gwiki/src/support/postgres.rs:41-51]

