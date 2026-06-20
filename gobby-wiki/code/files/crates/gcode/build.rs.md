---
title: crates/gcode/build.rs
type: code_file
provenance:
- file: crates/gcode/build.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/build.rs

Module: [[code/modules/crates/gcode|crates/gcode]]

## Overview

`crates/gcode/build.rs` exposes 1 indexed API symbol.

## How it fits

`crates/gcode/build.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `main` | function | Emits Cargo build-script directives to rerun when 'GCODE_POSTGRES_TEST_DATABASE_URL' changes, register the 'gcode_postgres_tests' cfg for check-cfg, and enable that cfg when the environment variable is set. [crates/gcode/build.rs:1-8] |

