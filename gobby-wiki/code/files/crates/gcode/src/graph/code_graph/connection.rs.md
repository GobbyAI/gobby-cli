---
title: crates/gcode/src/graph/code_graph/connection.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/connection.rs
  ranges:
  - 7-12
  - 14-40
  - 42-68
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/connection.rs:7-12](crates/gcode/src/graph/code_graph/connection.rs#L7-L12), [crates/gcode/src/graph/code_graph/connection.rs:14-40](crates/gcode/src/graph/code_graph/connection.rs#L14-L40), [crates/gcode/src/graph/code_graph/connection.rs:42-68](crates/gcode/src/graph/code_graph/connection.rs#L42-L68)

</details>

# crates/gcode/src/graph/code_graph/connection.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Provides small helpers for running code-graph reads against FalkorDB through the current `Context`. `require_graph_reads` rejects requests when graph access is not configured, `with_required_core_graph` opens a graph client and maps connection/query failures into `GraphReadError` for mandatory reads, and `with_optional_core_graph` does the same for optional reads but falls back to a caller-supplied default when graph access is missing or unavailable.
[crates/gcode/src/graph/code_graph/connection.rs:7-12]
[crates/gcode/src/graph/code_graph/connection.rs:14-40]
[crates/gcode/src/graph/code_graph/connection.rs:42-68]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `require_graph_reads` | function | `pub fn require_graph_reads(ctx: &Context) -> anyhow::Result<()> {` | `require_graph_reads [function]` | `347ab6bb-ae29-5207-ae9e-d0805653885a` | 7-12 [crates/gcode/src/graph/code_graph/connection.rs:7-12] | Indexed function `require_graph_reads` in `crates/gcode/src/graph/code_graph/connection.rs`. [crates/gcode/src/graph/code_graph/connection.rs:7-12] |
| `with_required_core_graph` | function | `pub(super) fn with_required_core_graph<T>(` | `with_required_core_graph [function]` | `48bed7c5-177e-50e4-abd2-79973010a2e8` | 14-40 [crates/gcode/src/graph/code_graph/connection.rs:14-40] | Indexed function `with_required_core_graph` in `crates/gcode/src/graph/code_graph/connection.rs`. [crates/gcode/src/graph/code_graph/connection.rs:14-40] |
| `with_optional_core_graph` | function | `pub(super) fn with_optional_core_graph<T>(` | `with_optional_core_graph [function]` | `61eebd5a-28cf-5755-8ba3-f59696c28b98` | 42-68 [crates/gcode/src/graph/code_graph/connection.rs:42-68] | Indexed function `with_optional_core_graph` in `crates/gcode/src/graph/code_graph/connection.rs`. [crates/gcode/src/graph/code_graph/connection.rs:42-68] |
