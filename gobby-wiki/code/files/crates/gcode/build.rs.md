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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/build.rs:1-8](crates/gcode/build.rs#L1-L8)

</details>

# crates/gcode/build.rs

Module: [[code/modules/crates/gcode|crates/gcode]]

## Purpose

Build script for the `gcode` crate that configures Cargo rebuild and conditional compilation for PostgreSQL tests. It always tells Cargo to rerun if `GCODE_POSTGRES_TEST_DATABASE_URL` changes, declares the `gcode_postgres_tests` cfg as an expected conditional, and enables that cfg when the environment variable is present. [crates/gcode/build.rs:1-8]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `main` | function | `fn main() {` | `main [function]` | `a0d760c2-abd5-5181-9527-a7b6ba1d6e27` | 1-8 [crates/gcode/build.rs:1-8] | Indexed function `main` in `crates/gcode/build.rs`. [crates/gcode/build.rs:1-8] |
