---
title: crates/gcode/src/savings.rs
type: code_file
provenance:
- file: crates/gcode/src/savings.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/savings.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/savings.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gcode/src/savings.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `savings_pct` | function | Returns the percentage reduction from 'original_chars' to 'actual_chars' as '((1.0 - actual_chars / original_chars) * 100.0)', with a zero baseline guarded to return '0.0' when 'original_chars' is '0'. [crates/gcode/src/savings.rs:7-12] |
| `report_savings` | function | Sends a best-effort 1-second JSON 'POST' to '"{base_url}/api/admin/savings/record"' recording 'code_index' savings with the supplied original and actual character counts plus '{"strategy":"outline"}' metadata, ignoring any response or error. [crates/gcode/src/savings.rs:18-29] |
| `test_savings_pct_basic` | function | Verifies that 'savings_pct(1000, 200)' returns approximately '80.0' by asserting the absolute error is less than '0.01'. [crates/gcode/src/savings.rs:36-39] |
| `test_savings_pct_zero_original` | function | Verifies that 'savings_pct(0, 0)' returns '0.0' when both inputs are zero. [crates/gcode/src/savings.rs:42-44] |
| `test_savings_pct_no_savings` | function | Verifies that 'savings_pct(100, 100)' returns a value whose absolute magnitude is less than '0.01', i.e. effectively zero savings when the compared values are equal. [crates/gcode/src/savings.rs:47-49] |

