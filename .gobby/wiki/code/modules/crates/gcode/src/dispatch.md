---
title: crates/gcode/src/dispatch
type: code_module
provenance:
- file: crates/gcode/src/dispatch/tests.rs
  ranges:
  - 5-9
  - 12-52
  - 55-69
  - 72-89
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/dispatch

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The dispatch module orchestrates the routing and initialization of G-code command execution. It supports early dispatch setup using parsed requests without requiring full context, enables command lookup that can bypass service configuration resolution, and manages service dependency resolution specifically for graph and AI commands. The module includes tests verifying the correctness of these dispatch, lookup, and service selection mechanisms.
[crates/gcode/src/dispatch/tests.rs:5-9]
[crates/gcode/src/dispatch/tests.rs:12-52]
[crates/gcode/src/dispatch/tests.rs:55-69]
[crates/gcode/src/dispatch/tests.rs:72-89]

## Files

- [[code/files/crates/gcode/src/dispatch/tests.rs|crates/gcode/src/dispatch/tests.rs]] - `crates/gcode/src/dispatch/tests.rs` exposes 4 indexed API symbols.
[crates/gcode/src/dispatch/tests.rs:5-9]
[crates/gcode/src/dispatch/tests.rs:12-52]
[crates/gcode/src/dispatch/tests.rs:55-69]
[crates/gcode/src/dispatch/tests.rs:72-89]

## Components

- `fc1559c1-f164-54c8-b94f-ad104dc8e5e8`
- `2fca8eb4-00af-5c4d-8c50-88191dd4205c`
- `5253d1cd-23d7-5140-81a5-8d9180840fc5`
- `b90e3843-b015-5222-b4fd-b2f92d553ea3`

