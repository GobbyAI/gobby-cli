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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/db/mod.rs:16-20](crates/gcode/src/db/mod.rs#L16-L20), [crates/gcode/src/db/mod.rs:27-31](crates/gcode/src/db/mod.rs#L27-L31), [crates/gcode/src/db/mod.rs:33-35](crates/gcode/src/db/mod.rs#L33-L35)

</details>

# crates/gcode/src/db/mod.rs

Module: [[code/modules/crates/gcode/src/db|crates/gcode/src/db]]

## Purpose

This module re-exports query and resolution database helpers, then provides two explicit connection entry points: `connect_readwrite` and `connect_readonly`. Both delegate to `gobby_core::postgres` for the actual connection, run `schema::validate_runtime_schema` before returning the `Client`, and keep separate read/write intent for future routing differences. It also exposes `read_config_value` as a thin wrapper around the core postgres config lookup.
[crates/gcode/src/db/mod.rs:16-20]
[crates/gcode/src/db/mod.rs:27-31]
[crates/gcode/src/db/mod.rs:33-35]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `connect_readwrite` | function | `pub fn connect_readwrite(database_url: &str) -> anyhow::Result<Client> {` | `connect_readwrite [function]` | `8b63e348-5e46-53b5-9fc7-6a0c636e3b84` | 16-20 [crates/gcode/src/db/mod.rs:16-20] | Indexed function `connect_readwrite` in `crates/gcode/src/db/mod.rs`. [crates/gcode/src/db/mod.rs:16-20] |
| `connect_readonly` | function | `pub fn connect_readonly(database_url: &str) -> anyhow::Result<Client> {` | `connect_readonly [function]` | `972f2a42-df59-5828-a61a-48ae143430ea` | 27-31 [crates/gcode/src/db/mod.rs:27-31] | Indexed function `connect_readonly` in `crates/gcode/src/db/mod.rs`. [crates/gcode/src/db/mod.rs:27-31] |
| `read_config_value` | function | `pub fn read_config_value(conn: &mut Client, key: &str) -> anyhow::Result<Option<String>> {` | `read_config_value [function]` | `b8a73bdd-11bb-5d01-8187-08674eccc507` | 33-35 [crates/gcode/src/db/mod.rs:33-35] | Indexed function `read_config_value` in `crates/gcode/src/db/mod.rs`. [crates/gcode/src/db/mod.rs:33-35] |
