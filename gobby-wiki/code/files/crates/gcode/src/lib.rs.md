---
title: crates/gcode/src/lib.rs
type: code_file
provenance:
- file: crates/gcode/src/lib.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/lib.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/lib.rs` exposes 6 indexed API symbols.

## How it fits

`crates/gcode/src/lib.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `assert_cli_independent_contract` | function | Asserts at runtime that the generic type 'T' is serializable/deserializable and does not reference CLI-specific modules or clap types by checking its Rust type name for forbidden substrings. [crates/gcode/src/lib.rs:34-42] |
| `visit` | function | Recursively traverses a directory tree, reading each '.rs' file and appending its path to 'offenders' if the file contents contain the string 'FalkorClientBuilder'. [crates/gcode/src/lib.rs:187-204] |

_Verified by 4 in-file unit tests._

