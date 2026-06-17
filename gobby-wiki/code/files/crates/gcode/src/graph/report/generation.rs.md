---
title: crates/gcode/src/graph/report/generation.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/generation.rs
  ranges:
  - 21-23
  - 25-59
  - 61-63
  - 65-76
  - 78-159
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/report/generation.rs:21-23](crates/gcode/src/graph/report/generation.rs#L21-L23), [crates/gcode/src/graph/report/generation.rs:25-59](crates/gcode/src/graph/report/generation.rs#L25-L59), [crates/gcode/src/graph/report/generation.rs:61-63](crates/gcode/src/graph/report/generation.rs#L61-L63), [crates/gcode/src/graph/report/generation.rs:65-76](crates/gcode/src/graph/report/generation.rs#L65-L76), [crates/gcode/src/graph/report/generation.rs:78-159](crates/gcode/src/graph/report/generation.rs#L78-L159)

</details>

# crates/gcode/src/graph/report/generation.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

This file builds project graph reports from Falkor-backed graph data or from a preloaded snapshot. `generate_report` is the simple entry point, delegating to `generate_report_with_options`, which normalizes report options, checks graph service configuration, loads a `ReportGraphSnapshot` through `load_report_snapshot`, and converts service states or query failures into `ProjectGraphReportError` values before handing the snapshot to `generate_report_from_snapshot_with_options`. The snapshot-based helpers provide the same report construction path without querying the graph, while `empty_report` produces a default report from an empty snapshot and the current timestamp.
[crates/gcode/src/graph/report/generation.rs:21-23]
[crates/gcode/src/graph/report/generation.rs:25-59]
[crates/gcode/src/graph/report/generation.rs:61-63]
[crates/gcode/src/graph/report/generation.rs:65-76]
[crates/gcode/src/graph/report/generation.rs:78-159]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `generate_report` | function | `pub fn generate_report(ctx: &Context) -> Result<ProjectGraphReport, ProjectGraphReportError> {` | `generate_report [function]` | `e0217ea3-a71e-5e9a-bb03-932e835e10ba` | 21-23 [crates/gcode/src/graph/report/generation.rs:21-23] | Indexed function `generate_report` in `crates/gcode/src/graph/report/generation.rs`. [crates/gcode/src/graph/report/generation.rs:21-23] |
| `generate_report_with_options` | function | `pub fn generate_report_with_options(` | `generate_report_with_options [function]` | `22d472bb-0e6e-553b-8160-09db28c2ce94` | 25-59 [crates/gcode/src/graph/report/generation.rs:25-59] | Indexed function `generate_report_with_options` in `crates/gcode/src/graph/report/generation.rs`. [crates/gcode/src/graph/report/generation.rs:25-59] |
| `empty_report` | function | `pub fn empty_report(project_id: impl Into<String>) -> ProjectGraphReport {` | `empty_report [function]` | `2c9f4c44-9b16-5e52-86ec-dbf38b5fe61f` | 61-63 [crates/gcode/src/graph/report/generation.rs:61-63] | Indexed function `empty_report` in `crates/gcode/src/graph/report/generation.rs`. [crates/gcode/src/graph/report/generation.rs:61-63] |
| `generate_report_from_snapshot` | function | `pub(super) fn generate_report_from_snapshot(` | `generate_report_from_snapshot [function]` | `ad6d4d1f-7654-5da8-9b42-a05d5f0d8a04` | 65-76 [crates/gcode/src/graph/report/generation.rs:65-76] | Indexed function `generate_report_from_snapshot` in `crates/gcode/src/graph/report/generation.rs`. [crates/gcode/src/graph/report/generation.rs:65-76] |
| `generate_report_from_snapshot_with_options` | function | `fn generate_report_from_snapshot_with_options(` | `generate_report_from_snapshot_with_options [function]` | `5ca1f20f-cc56-5dac-bfbd-6d8168b64381` | 78-159 [crates/gcode/src/graph/report/generation.rs:78-159] | Indexed function `generate_report_from_snapshot_with_options` in `crates/gcode/src/graph/report/generation.rs`. [crates/gcode/src/graph/report/generation.rs:78-159] |
