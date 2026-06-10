---
title: crates/gcode/src/savings.rs
type: code_file
provenance:
- file: crates/gcode/src/savings.rs
  ranges:
  - 7-12
  - 18-29
  - 34-54
  - 61-64
  - 67-69
  - 72-74
  - 77-80
  - 84-89
  - 93-97
  - 101-106
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/savings.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

`crates/gcode/src/savings.rs` exposes 10 indexed API symbols.
[crates/gcode/src/savings.rs:7-12]
[crates/gcode/src/savings.rs:18-29]
[crates/gcode/src/savings.rs:34-54]
[crates/gcode/src/savings.rs:61-64]
[crates/gcode/src/savings.rs:67-69]
[crates/gcode/src/savings.rs:72-74]
[crates/gcode/src/savings.rs:77-80]
[crates/gcode/src/savings.rs:84-89]
[crates/gcode/src/savings.rs:93-97]
[crates/gcode/src/savings.rs:101-106]

## API Symbols

- `savings_pct` (function) component `savings_pct [function]` (`db2bda4d-2adf-5fd2-b648-3c24a61b1538`) lines 7-12 [crates/gcode/src/savings.rs:7-12]
  - Signature: `pub fn savings_pct(original_chars: usize, actual_chars: usize) -> f64 {`
  - Purpose: Calculates the percentage reduction in character count from an original value to an actual value, returning (1 - actual/original) × 100 or 0 if the original is zero. [crates/gcode/src/savings.rs:7-12]
- `report_savings` (function) component `report_savings [function]` (`6c008c9c-58a7-5e66-8d7f-1f802776a52b`) lines 18-29 [crates/gcode/src/savings.rs:18-29]
  - Signature: `pub fn report_savings(base_url: &str, original_chars: usize, actual_chars: usize) {`
  - Purpose: POSTs compression metrics (original and actual character counts) to an admin API endpoint with a one-second timeout, ignoring any response or error. [crates/gcode/src/savings.rs:18-29]
- `resolve_daemon_url` (function) component `resolve_daemon_url [function]` (`99dace60-cedc-5b27-87cf-2420cd730436`) lines 34-54 [crates/gcode/src/savings.rs:34-54]
  - Signature: `pub fn resolve_daemon_url(config_url: Option<&str>) -> Option<String> {`
  - Purpose: Resolves a daemon URL by interpolating `${GOBBY_PORT}` in a provided config string, falling back to the `GOBBY_PORT` environment variable, and defaulting to `http://localhost:60887`. [crates/gcode/src/savings.rs:34-54]
- `test_savings_pct_basic` (function) component `test_savings_pct_basic [function]` (`128b4e84-041d-597e-8da8-8a3ad8b66d70`) lines 61-64 [crates/gcode/src/savings.rs:61-64]
  - Signature: `fn test_savings_pct_basic() {`
  - Purpose: This test verifies that `savings_pct(1000, 200)` returns a value within 0.01 of 80.0, asserting the savings percentage calculation is correct for the given inputs. [crates/gcode/src/savings.rs:61-64]
- `test_savings_pct_zero_original` (function) component `test_savings_pct_zero_original [function]` (`bf19c38a-267a-5880-a042-12e032edf4e3`) lines 67-69 [crates/gcode/src/savings.rs:67-69]
  - Signature: `fn test_savings_pct_zero_original() {`
  - Purpose: Tests that the `savings_pct` function returns 0.0 when both arguments are zero. [crates/gcode/src/savings.rs:67-69]
- `test_savings_pct_no_savings` (function) component `test_savings_pct_no_savings [function]` (`c9f3213d-0849-5eb5-b7a4-3c8ea6956a0f`) lines 72-74 [crates/gcode/src/savings.rs:72-74]
  - Signature: `fn test_savings_pct_no_savings() {`
  - Purpose: This test asserts that `savings_pct(100, 100)` returns a value within 0.01 of zero, verifying that the savings percentage calculation correctly represents zero savings when the original and final values are equal. [crates/gcode/src/savings.rs:72-74]
- `test_resolve_daemon_url_config_value` (function) component `test_resolve_daemon_url_config_value [function]` (`2248f804-561a-556b-afe3-300538438f28`) lines 77-80 [crates/gcode/src/savings.rs:77-80]
  - Signature: `fn test_resolve_daemon_url_config_value() {`
  - Purpose: Tests that `resolve_daemon_url` returns the provided custom daemon URL unchanged when supplied as a `Some` argument. [crates/gcode/src/savings.rs:77-80]
- `test_resolve_daemon_url_env_var` (function) component `test_resolve_daemon_url_env_var [function]` (`e09c7cc6-a5b0-5930-bedc-c5e367cc11a0`) lines 84-89 [crates/gcode/src/savings.rs:84-89]
  - Signature: `fn test_resolve_daemon_url_env_var() {`
  - Purpose: Unit test verifying that `resolve_daemon_url(None)` correctly reads the `GOBBY_PORT` environment variable and constructs a localhost daemon URL in the format `http://localhost:<port>`. [crates/gcode/src/savings.rs:84-89]
- `test_resolve_daemon_url_default` (function) component `test_resolve_daemon_url_default [function]` (`46cc49a0-7fe8-5a37-be9a-719ae17ef857`) lines 93-97 [crates/gcode/src/savings.rs:93-97]
  - Signature: `fn test_resolve_daemon_url_default() {`
  - Purpose: Verifies that `resolve_daemon_url(None)` returns `Some("http://localhost:60887")` when the `GOBBY_PORT` environment variable is absent. [crates/gcode/src/savings.rs:93-97]
- `test_resolve_daemon_url_expand_port` (function) component `test_resolve_daemon_url_expand_port [function]` (`8fd5c450-0c1c-5276-afa8-a98c7c604707`) lines 101-106 [crates/gcode/src/savings.rs:101-106]
  - Signature: `fn test_resolve_daemon_url_expand_port() {`
  - Purpose: Tests that `resolve_daemon_url` expands environment variable placeholders (syntax: `${VAR_NAME}`) within daemon URL strings. [crates/gcode/src/savings.rs:101-106]

