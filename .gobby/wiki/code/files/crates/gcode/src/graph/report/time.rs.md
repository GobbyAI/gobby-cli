---
title: crates/gcode/src/graph/report/time.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/time.rs
  ranges:
  - 3-5
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/report/time.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

Provides a small time utility for report generation: `now_iso8601` returns the current UTC timestamp as an RFC3339/ISO8601 string with microsecond precision using `chrono`’s `Utc::now()` and `to_rfc3339_opts`. [crates/gcode/src/graph/report/time.rs:3-5]

## API Symbols

- `now_iso8601` (function) component `now_iso8601 [function]` (`c0d03fb4-d57c-59c8-a5d7-b4cbddaa9c60`) lines 3-5 [crates/gcode/src/graph/report/time.rs:3-5]
  - Signature: `pub(super) fn now_iso8601() -> String {`
  - Purpose: Returns the current UTC time as an RFC3339-formatted ISO8601 string with microsecond precision. [crates/gcode/src/graph/report/time.rs:3-5]

