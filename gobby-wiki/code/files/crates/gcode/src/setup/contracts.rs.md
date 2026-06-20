---
title: crates/gcode/src/setup/contracts.rs
type: code_file
provenance:
- file: crates/gcode/src/setup/contracts.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/setup/contracts.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Overview

`crates/gcode/src/setup/contracts.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/setup/contracts.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `TableContract` | class | 'TableContract' is a module-private struct that defines a table schema contract by pairing a static table name with a static list of required column names. [crates/gcode/src/setup/contracts.rs:5-8] |
| `IndexContract` | class | 'IndexContract' is a module-visible struct that stores three static string references identifying an index contract’s 'name', target 'table', and associated 'method'. [crates/gcode/src/setup/contracts.rs:10-14] |
| `code_index_table_names` | function | Returns a double-ended iterator over the static 'name' field of each contract in 'TABLE_CONTRACTS'. [crates/gcode/src/setup/contracts.rs:191-193] |
| `code_index_index_names` | function | Returns a double-ended iterator over the static 'name' field of each contract in 'INDEX_CONTRACTS'. [crates/gcode/src/setup/contracts.rs:195-197] |

