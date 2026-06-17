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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/savings.rs:7-12](crates/gcode/src/savings.rs#L7-L12), [crates/gcode/src/savings.rs:18-29](crates/gcode/src/savings.rs#L18-L29), [crates/gcode/src/savings.rs:36-39](crates/gcode/src/savings.rs#L36-L39), [crates/gcode/src/savings.rs:42-44](crates/gcode/src/savings.rs#L42-L44), [crates/gcode/src/savings.rs:47-49](crates/gcode/src/savings.rs#L47-L49)

</details>

# crates/gcode/src/savings.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Provides best-effort savings tracking for gcode when compact outline/symbol data is returned instead of full file contents. `savings_pct` computes the percentage reduction from original to actual character counts, with a zero-original guard to avoid division by zero. `report_savings` packages those counts into a JSON payload and posts them to the Gobby daemon’s savings-record endpoint with a short timeout, ignoring any network errors so reporting cannot break gcode behavior. The tests verify the percentage calculation for a normal case, the zero-input edge case, and the no-savings case.
[crates/gcode/src/savings.rs:7-12]
[crates/gcode/src/savings.rs:18-29]
[crates/gcode/src/savings.rs:36-39]
[crates/gcode/src/savings.rs:42-44]
[crates/gcode/src/savings.rs:47-49]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `savings_pct` | function | `pub fn savings_pct(original_chars: usize, actual_chars: usize) -> f64 {` | `savings_pct [function]` | `db2bda4d-2adf-5fd2-b648-3c24a61b1538` | 7-12 [crates/gcode/src/savings.rs:7-12] | Indexed function `savings_pct` in `crates/gcode/src/savings.rs`. [crates/gcode/src/savings.rs:7-12] |
| `report_savings` | function | `pub fn report_savings(base_url: &str, original_chars: usize, actual_chars: usize) {` | `report_savings [function]` | `6c008c9c-58a7-5e66-8d7f-1f802776a52b` | 18-29 [crates/gcode/src/savings.rs:18-29] | Indexed function `report_savings` in `crates/gcode/src/savings.rs`. [crates/gcode/src/savings.rs:18-29] |
| `test_savings_pct_basic` | function | `fn test_savings_pct_basic() {` | `test_savings_pct_basic [function]` | `d4572a4d-abcd-5da5-8797-f80458d0f042` | 36-39 [crates/gcode/src/savings.rs:36-39] | Indexed function `test_savings_pct_basic` in `crates/gcode/src/savings.rs`. [crates/gcode/src/savings.rs:36-39] |
| `test_savings_pct_zero_original` | function | `fn test_savings_pct_zero_original() {` | `test_savings_pct_zero_original [function]` | `f3a804e3-4b91-511f-833b-ea1c0a8b2024` | 42-44 [crates/gcode/src/savings.rs:42-44] | Indexed function `test_savings_pct_zero_original` in `crates/gcode/src/savings.rs`. [crates/gcode/src/savings.rs:42-44] |
| `test_savings_pct_no_savings` | function | `fn test_savings_pct_no_savings() {` | `test_savings_pct_no_savings [function]` | `bbf18bf9-0db8-5cad-98db-59e3fdad255c` | 47-49 [crates/gcode/src/savings.rs:47-49] | Indexed function `test_savings_pct_no_savings` in `crates/gcode/src/savings.rs`. [crates/gcode/src/savings.rs:47-49] |
