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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/support/postgres.rs:6-39](crates/gwiki/src/support/postgres.rs#L6-L39), [crates/gwiki/src/support/postgres.rs:41-51](crates/gwiki/src/support/postgres.rs#L41-L51)

</details>

# crates/gwiki/src/support/postgres.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Provides PostgreSQL-backed configuration checks for commands that depend on a wiki index. `require_attached_index` resolves the command’s database URL, opens a read-only PostgreSQL connection, runs runtime schema validation through `ValidationContext`, and returns a config error if any required index pieces are missing. `require_postgres_index` is the simpler helper that only resolves the database URL and returns a read-only `postgres::Client`, failing with a config error if no DSN is configured or the connection cannot be established.
[crates/gwiki/src/support/postgres.rs:6-39]
[crates/gwiki/src/support/postgres.rs:41-51]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `require_attached_index` | function | `pub(crate) fn require_attached_index(command: &'static str) -> Result<(), WikiError> {` | `require_attached_index [function]` | `e5e4bf14-b0e4-5ecf-a2e7-b9ca1e8a01db` | 6-39 [crates/gwiki/src/support/postgres.rs:6-39] | Indexed function `require_attached_index` in `crates/gwiki/src/support/postgres.rs`. [crates/gwiki/src/support/postgres.rs:6-39] |
| `require_postgres_index` | function | `pub(crate) fn require_postgres_index(command: &'static str) -> Result<Client, WikiError> {` | `require_postgres_index [function]` | `5f965f9d-b719-59de-84bd-72e703a7bc08` | 41-51 [crates/gwiki/src/support/postgres.rs:41-51] | Indexed function `require_postgres_index` in `crates/gwiki/src/support/postgres.rs`. [crates/gwiki/src/support/postgres.rs:41-51] |
