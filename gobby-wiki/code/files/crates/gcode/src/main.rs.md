---
title: crates/gcode/src/main.rs
type: code_file
provenance:
- file: crates/gcode/src/main.rs
  ranges:
  - 4-6
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/main.rs:4-6](crates/gcode/src/main.rs#L4-L6)

</details>

# crates/gcode/src/main.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Entry point for the `gcode` binary. It declares the `cli` and `dispatch` modules, then hands control to `dispatch::run_with_exit_code()` from `main`, making this file a thin startup wrapper that returns the process exit code. [crates/gcode/src/main.rs:4-6]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `main` | function | `fn main() -> std::process::ExitCode {` | `main [function]` | `8e467992-cf7d-50da-9171-184b5fcdf4b4` | 4-6 [crates/gcode/src/main.rs:4-6] | Indexed function `main` in `crates/gcode/src/main.rs`. [crates/gcode/src/main.rs:4-6] |
