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

This file provides PostgreSQL-specific support checks for `gwiki`. `require_attached_index` verifies that a PostgreSQL hub is configured, opens a readonly connection, runs runtime schema validation through `ValidationContext`, and returns a config error if required index pieces are missing. `require_postgres_index` is the lower-level helper that resolves the database URL from environment settings and returns a readonly `postgres::Client`, converting missing config or connection failures into `WikiError::Config`.
[crates/gwiki/src/support/postgres.rs:6-39]
[crates/gwiki/src/support/postgres.rs:41-51]

## API Symbols

- `require_attached_index` (function) component `require_attached_index [function]` (`e5e4bf14-b0e4-5ecf-a2e7-b9ca1e8a01db`) lines 6-39 [crates/gwiki/src/support/postgres.rs:6-39]
  - Signature: `pub(crate) fn require_attached_index(command: &'static str) -> Result<(), WikiError> {`
  - Purpose: Indexed function `require_attached_index` in `crates/gwiki/src/support/postgres.rs`. [crates/gwiki/src/support/postgres.rs:6-39]
- `require_postgres_index` (function) component `require_postgres_index [function]` (`5f965f9d-b719-59de-84bd-72e703a7bc08`) lines 41-51 [crates/gwiki/src/support/postgres.rs:41-51]
  - Signature: `pub(crate) fn require_postgres_index(command: &'static str) -> Result<Client, WikiError> {`
  - Purpose: Indexed function `require_postgres_index` in `crates/gwiki/src/support/postgres.rs`. [crates/gwiki/src/support/postgres.rs:41-51]

