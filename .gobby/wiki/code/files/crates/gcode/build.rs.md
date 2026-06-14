---
title: crates/gcode/build.rs
type: code_file
provenance:
- file: crates/gcode/build.rs
  ranges:
  - 1-8
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/build.rs

Module: [[code/modules/crates/gcode|crates/gcode]]

## Purpose

This is a Cargo build script that conditionally enables PostgreSQL-related tests. The main function instructs Cargo to rerun the build whenever the GCODE_POSTGRES_TEST_DATABASE_URL environment variable changes, and it sets the gcode_postgres_tests conditional compilation flag when that variable is present, allowing test code guarded by that cfg attribute to be compiled into the binary. [crates/gcode/build.rs:1-8]

## API Symbols

- `main` (function) component `main [function]` (`a0d760c2-abd5-5181-9527-a7b6ba1d6e27`) lines 1-8 [crates/gcode/build.rs:1-8]
  - Signature: `fn main() {`
  - Purpose: Indexed function `main` in `crates/gcode/build.rs`. [crates/gcode/build.rs:1-8]

