---
title: crates/gcode/src/savings.rs
type: code_file
provenance:
- file: crates/gcode/src/savings.rs
  ranges:
  - 7-12
  - 18-29
  - 36-39
  - 42-44
  - 47-49
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/savings.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This file implements daemon-based savings tracking for gcode. It calculates and reports token savings when gcode returns compact symbol/outline data instead of full file contents.

The core functionality centers on two functions: `savings_pct` computes the percentage reduction between original and actual character counts, handling the edge case of zero-length originals by returning 0.0. `report_savings` wraps this calculation and sends it to the Gobby daemon via HTTP POST with context metadata (strategy: "outline"), designed as best-effort with all errors silently ignored so daemon downtime never breaks gcode functionality.

Three unit tests validate `savings_pct` behavior across basic calculation, zero-division handling, and no-savings scenarios.
[crates/gcode/src/savings.rs:7-12]
[crates/gcode/src/savings.rs:18-29]
[crates/gcode/src/savings.rs:36-39]
[crates/gcode/src/savings.rs:42-44]
[crates/gcode/src/savings.rs:47-49]

## API Symbols

- `savings_pct` (function) component `savings_pct [function]` (`db2bda4d-2adf-5fd2-b648-3c24a61b1538`) lines 7-12 [crates/gcode/src/savings.rs:7-12]
  - Signature: `pub fn savings_pct(original_chars: usize, actual_chars: usize) -> f64 {`
  - Purpose: Indexed function `savings_pct` in `crates/gcode/src/savings.rs`. [crates/gcode/src/savings.rs:7-12]
- `report_savings` (function) component `report_savings [function]` (`6c008c9c-58a7-5e66-8d7f-1f802776a52b`) lines 18-29 [crates/gcode/src/savings.rs:18-29]
  - Signature: `pub fn report_savings(base_url: &str, original_chars: usize, actual_chars: usize) {`
  - Purpose: Indexed function `report_savings` in `crates/gcode/src/savings.rs`. [crates/gcode/src/savings.rs:18-29]
- `test_savings_pct_basic` (function) component `test_savings_pct_basic [function]` (`d4572a4d-abcd-5da5-8797-f80458d0f042`) lines 36-39 [crates/gcode/src/savings.rs:36-39]
  - Signature: `fn test_savings_pct_basic() {`
  - Purpose: Indexed function `test_savings_pct_basic` in `crates/gcode/src/savings.rs`. [crates/gcode/src/savings.rs:36-39]
- `test_savings_pct_zero_original` (function) component `test_savings_pct_zero_original [function]` (`f3a804e3-4b91-511f-833b-ea1c0a8b2024`) lines 42-44 [crates/gcode/src/savings.rs:42-44]
  - Signature: `fn test_savings_pct_zero_original() {`
  - Purpose: Indexed function `test_savings_pct_zero_original` in `crates/gcode/src/savings.rs`. [crates/gcode/src/savings.rs:42-44]
- `test_savings_pct_no_savings` (function) component `test_savings_pct_no_savings [function]` (`bbf18bf9-0db8-5cad-98db-59e3fdad255c`) lines 47-49 [crates/gcode/src/savings.rs:47-49]
  - Signature: `fn test_savings_pct_no_savings() {`
  - Purpose: Indexed function `test_savings_pct_no_savings` in `crates/gcode/src/savings.rs`. [crates/gcode/src/savings.rs:47-49]

