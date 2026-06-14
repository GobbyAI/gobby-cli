---
title: crates/gcode/src/db/mod.rs
type: code_file
provenance:
- file: crates/gcode/src/db/mod.rs
  ranges:
  - 16-20
  - 27-31
  - 33-35
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/db/mod.rs

Module: [[code/modules/crates/gcode/src/db|crates/gcode/src/db]]

## Purpose

This module provides database connection management for a PostgreSQL-based system. It exposes two connection functions—connect_readwrite and connect_readonly—that establish database clients and validate the runtime schema before returning them. The separate functions preserve explicit access intent for future routing or permission enhancements. The module also wraps a config value reader that delegates to the postgres module, and re-exports query and resolution utilities from submodules. Together, these pieces form a centralized database abstraction layer with schema validation and differentiated access patterns.
[crates/gcode/src/db/mod.rs:16-20]
[crates/gcode/src/db/mod.rs:27-31]
[crates/gcode/src/db/mod.rs:33-35]

## API Symbols

- `connect_readwrite` (function) component `connect_readwrite [function]` (`8b63e348-5e46-53b5-9fc7-6a0c636e3b84`) lines 16-20 [crates/gcode/src/db/mod.rs:16-20]
  - Signature: `pub fn connect_readwrite(database_url: &str) -> anyhow::Result<Client> {`
  - Purpose: Connects to a PostgreSQL database in read-write mode and validates the runtime schema before returning the client, or an error if either operation fails. [crates/gcode/src/db/mod.rs:16-20]
- `connect_readonly` (function) component `connect_readonly [function]` (`972f2a42-df59-5828-a61a-48ae143430ea`) lines 27-31 [crates/gcode/src/db/mod.rs:27-31]
  - Signature: `pub fn connect_readonly(database_url: &str) -> anyhow::Result<Client> {`
  - Purpose: Creates a read-only PostgreSQL database client from the provided URL and validates that the database schema conforms to the expected runtime schema before returning the connected client. [crates/gcode/src/db/mod.rs:27-31]
- `read_config_value` (function) component `read_config_value [function]` (`b8a73bdd-11bb-5d01-8187-08674eccc507`) lines 33-35 [crates/gcode/src/db/mod.rs:33-35]
  - Signature: `pub fn read_config_value(conn: &mut Client, key: &str) -> anyhow::Result<Option<String>> {`
  - Purpose: Wrapper function that delegates to the postgres module to retrieve an optional string configuration value from PostgreSQL by the given key, returning a Result-wrapped Option. [crates/gcode/src/db/mod.rs:33-35]

