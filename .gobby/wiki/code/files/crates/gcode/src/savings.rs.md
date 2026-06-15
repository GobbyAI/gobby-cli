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

This file provides daemon-based savings tracking for `gcode`: it computes the percentage reduction from original to actual character counts, returning `0.0` when the original count is zero. It also best-effort reports each savings event to the Gobby daemon via a short-timeout JSON POST with fixed `code_index` and `outline` metadata, and includes tests covering a basic savings case, zero-original handling, and no-savings behavior.
[crates/gcode/src/savings.rs:7-12]
[crates/gcode/src/savings.rs:18-29]
[crates/gcode/src/savings.rs:36-39]
[crates/gcode/src/savings.rs:42-44]
[crates/gcode/src/savings.rs:47-49]

## API Symbols

- `savings_pct` (function) component `savings_pct [function]` (`db2bda4d-2adf-5fd2-b648-3c24a61b1538`) lines 7-12 [crates/gcode/src/savings.rs:7-12]
  - Signature: `pub fn savings_pct(original_chars: usize, actual_chars: usize) -> f64 {`
  - Purpose: Returns the percentage reduction from 'original_chars' to 'actual_chars', yielding '0.0' when 'original_chars' is zero and otherwise computing '(1.0 - actual_chars as f64 / original_chars as f64) * 100.0'. [crates/gcode/src/savings.rs:7-12]
- `report_savings` (function) component `report_savings [function]` (`6c008c9c-58a7-5e66-8d7f-1f802776a52b`) lines 18-29 [crates/gcode/src/savings.rs:18-29]
  - Signature: `pub fn report_savings(base_url: &str, original_chars: usize, actual_chars: usize) {`
  - Purpose: Sends a JSON POST to '"{base_url}/api/admin/savings/record"' with 'category="code_index"', the provided character counts, and 'metadata.strategy="outline"', using a 1-second timeout and discarding any response or error. [crates/gcode/src/savings.rs:18-29]
- `test_savings_pct_basic` (function) component `test_savings_pct_basic [function]` (`d4572a4d-abcd-5da5-8797-f80458d0f042`) lines 36-39 [crates/gcode/src/savings.rs:36-39]
  - Signature: `fn test_savings_pct_basic() {`
  - Purpose: Verifies that 'savings_pct(1000, 200)' computes an approximately '80.0' percent savings value within a '0.01' tolerance. [crates/gcode/src/savings.rs:36-39]
- `test_savings_pct_zero_original` (function) component `test_savings_pct_zero_original [function]` (`f3a804e3-4b91-511f-833b-ea1c0a8b2024`) lines 42-44 [crates/gcode/src/savings.rs:42-44]
  - Signature: `fn test_savings_pct_zero_original() {`
  - Purpose: Verifies that 'savings_pct(0, 0)' returns '0.0' when both inputs are zero. [crates/gcode/src/savings.rs:42-44]
- `test_savings_pct_no_savings` (function) component `test_savings_pct_no_savings [function]` (`bbf18bf9-0db8-5cad-98db-59e3fdad255c`) lines 47-49 [crates/gcode/src/savings.rs:47-49]
  - Signature: `fn test_savings_pct_no_savings() {`
  - Purpose: Verifies that 'savings_pct(100, 100)' evaluates to approximately '0.0' by asserting its absolute value is less than '0.01'. [crates/gcode/src/savings.rs:47-49]

