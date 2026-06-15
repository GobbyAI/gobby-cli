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

# crates/gcode/src/main.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This file is the binary entry point for `gcode`. It declares the `cli` and `dispatch` modules, then hands control to `dispatch::run_with_exit_code()` from `main`, returning that function’s `std::process::ExitCode` as the program exit status. [crates/gcode/src/main.rs:4-6]

## API Symbols

- `main` (function) component `main [function]` (`8e467992-cf7d-50da-9171-184b5fcdf4b4`) lines 4-6 [crates/gcode/src/main.rs:4-6]
  - Signature: `fn main() -> std::process::ExitCode {`
  - Purpose: The 'main' function delegates execution to 'dispatch::run_with_exit_code()' and returns its 'std::process::ExitCode' result. [crates/gcode/src/main.rs:4-6]

