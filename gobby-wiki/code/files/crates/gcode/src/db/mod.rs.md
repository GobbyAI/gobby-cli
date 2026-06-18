---
title: crates/gcode/src/db/mod.rs
type: code_file
provenance:
- file: crates/gcode/src/db/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/db/mod.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The `crates/gcode/src/db/mod.rs` file manages the initialization and configuration of PostgreSQL database connections for the `gcode` crate. It provides dedicated entry points for both read-write and read-only database operations to ensure that database access intentions are kept clear and explicit.

When establishing a connection, the file utilizes specialized functions to connect to the database and validate the database schema against the expected runtime schema definition. Specifically, `connect_readwrite` in crates/gcode/src/db/mod.rs:16-20 is designated for command paths that may modify database state, while `connect_readonly` in crates/gcode/src/db/mod.rs:27-31 is used for paths that only read data. Both pathways ensure schema integrity before exposing the connection client.

Additionally, the file exposes utility functionality such as `read_config_value` in crates/gcode/src/db/mod.rs:33-35. This allows callers to safely query specific configuration parameters stored within the database using an active database connection.

## How it fits

This file acts as the primary API boundary and module coordinator for the database layer within the `gcode` crate. It declares and re-exports two submodules, `queries` and `resolution`, as shown in crates/gcode/src/db/mod.rs:5-9, bringing query implementations and resolution logic into the main database namespace.

In the broader system data flow, this file integrates local database requirements with lower-level utilities. It relies on the database client definitions from the `postgres` crate crates/gcode/src/db/mod.rs:1 and schema validation functionality defined in `crate::schema` crates/gcode/src/db/mod.rs:3. When a connection is requested, the code delegates the initial handshake to the underlying database helpers in `gobby_core::postgres` before performing local validation via `schema::validate_runtime_schema`.
[crates/gcode/src/db/mod.rs:16-20]
[crates/gcode/src/db/mod.rs:27-31]
[crates/gcode/src/db/mod.rs:33-35]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `connect_readwrite` | function | Connects to a PostgreSQL database using 'gobby_core::postgres::connect_readwrite', validates the runtime schema on the returned client, and returns the initialized 'Client' or an error. [crates/gcode/src/db/mod.rs:16-20] |
| `connect_readonly` | function | Establishes a read-only PostgreSQL client from 'database_url', validates the runtime schema against it, and returns the initialized 'Client' or an error. [crates/gcode/src/db/mod.rs:27-31] |
| `read_config_value` | function | Delegates to 'gobby_core::postgres::read_config_value' to fetch the given config key from the PostgreSQL client and returns it as 'anyhow::Result<Option<String>>'. [crates/gcode/src/db/mod.rs:33-35] |

