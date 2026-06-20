---
title: crates/gwiki/src/support/postgres.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/postgres.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/postgres.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/support/postgres.rs` exposes 2 indexed API symbols.

## How it fits

`crates/gwiki/src/support/postgres.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `require_attached_index` | function | Checks whether a PostgreSQL-backed index is configured and validates the runtime schema via a readonly PostgreSQL connection, returning 'Ok(())' when validation passes or a 'WikiError::Config' with command-specific diagnostics when the database is absent, unreachable, or schema validation reports missing requirements. [crates/gwiki/src/support/postgres.rs:6-39] |
| `require_postgres_index` | function | Resolves a PostgreSQL database URL for the given command, returns a 'Config' 'WikiError' if none is configured or if the index connection fails, and otherwise opens a read-only PostgreSQL 'Client'. [crates/gwiki/src/support/postgres.rs:41-51] |

