---
title: crates/gcode/src/db/mod.rs
type: code_file
provenance:
- file: crates/gcode/src/db/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/db/mod.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/db/mod.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gcode/src/db/mod.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `connect_readwrite` | function | Connects to a PostgreSQL database using 'gobby_core::postgres::connect_readwrite', validates the runtime schema on the returned client, and returns the initialized 'Client' or an error. [crates/gcode/src/db/mod.rs:16-20] |
| `connect_readonly` | function | Establishes a read-only PostgreSQL client from 'database_url', validates the runtime schema against it, and returns the initialized 'Client' or an error. [crates/gcode/src/db/mod.rs:27-31] |
| `read_config_value` | function | Delegates to 'gobby_core::postgres::read_config_value' to fetch the given config key from the PostgreSQL client and returns it as 'anyhow::Result<Option<String>>'. [crates/gcode/src/db/mod.rs:33-35] |

