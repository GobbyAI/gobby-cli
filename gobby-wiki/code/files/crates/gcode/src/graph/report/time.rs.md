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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/report/time.rs:3-5](crates/gcode/src/graph/report/time.rs#L3-L5)

</details>

# crates/gcode/src/graph/report/time.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

Provides a small time utility for graph reporting: `now_iso8601` returns the current UTC timestamp formatted as an ISO 8601/RFC 3339 string with microsecond precision and a trailing `Z`. The file is just this helper, using `chrono`’s `Utc::now()` and RFC 3339 formatting options. [crates/gcode/src/graph/report/time.rs:3-5]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `now_iso8601` | function | `pub(super) fn now_iso8601() -> String {` | `now_iso8601 [function]` | `c0d03fb4-d57c-59c8-a5d7-b4cbddaa9c60` | 3-5 [crates/gcode/src/graph/report/time.rs:3-5] | Indexed function `now_iso8601` in `crates/gcode/src/graph/report/time.rs`. [crates/gcode/src/graph/report/time.rs:3-5] |
