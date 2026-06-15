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

# crates/gcode/src/graph/report/generation.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

This file orchestrates project graph report creation. `generate_report` is a convenience wrapper that uses default options, while `generate_report_with_options` normalizes options, checks that FalkorDB is configured, loads a top-N graph snapshot through `load_report_snapshot`, and turns service availability or query failures into `ProjectGraphReportError`s. `empty_report` produces a timestamped report with an empty snapshot, and the `generate_report_from_snapshot*` helpers build a `ProjectGraphReport` directly from a `ReportGraphSnapshot`, filling in missing analysis such as graph summaries, hotspots, target frequencies, bridge relationships, suggested questions, and rendered markdown using the shared summary and rendering utilities.
[crates/gcode/src/graph/report/generation.rs:21-23]
[crates/gcode/src/graph/report/generation.rs:25-59]
[crates/gcode/src/graph/report/generation.rs:61-63]
[crates/gcode/src/graph/report/generation.rs:65-76]
[crates/gcode/src/graph/report/generation.rs:78-159]

## API Symbols

- `generate_report` (function) component `generate_report [function]` (`e0217ea3-a71e-5e9a-bb03-932e835e10ba`) lines 21-23 [crates/gcode/src/graph/report/generation.rs:21-23]
  - Signature: `pub fn generate_report(ctx: &Context) -> Result<ProjectGraphReport, ProjectGraphReportError> {`
  - Purpose: Generates a `ProjectGraphReport` from the provided `Context` reference using default `ProjectGraphReportOptions`. [crates/gcode/src/graph/report/generation.rs:21-23]
- `generate_report_with_options` (function) component `generate_report_with_options [function]` (`22d472bb-0e6e-553b-8160-09db28c2ce94`) lines 25-59 [crates/gcode/src/graph/report/generation.rs:25-59]
  - Signature: `pub fn generate_report_with_options(`
  - Purpose: Generates a timestamped ProjectGraphReport by connecting to FalkorDB, loading a top-N-filtered graph snapshot, and applying normalized options with comprehensive error handling for service availability states. [crates/gcode/src/graph/report/generation.rs:25-59]
- `empty_report` (function) component `empty_report [function]` (`07d606ca-c504-5800-9a55-25109e41cbee`) lines 61-63 [crates/gcode/src/graph/report/generation.rs:61-63]
  - Signature: `pub fn empty_report(project_id: impl Into<String>) -> ProjectGraphReport {`
  - Purpose: Generates a `ProjectGraphReport` for the specified project using the current ISO8601 timestamp and a default (empty) `ReportGraphSnapshot`. [crates/gcode/src/graph/report/generation.rs:61-63]
- `generate_report_from_snapshot` (function) component `generate_report_from_snapshot [function]` (`1d3aae22-c86e-5f25-b30d-fa181fa82726`) lines 65-76 [crates/gcode/src/graph/report/generation.rs:65-76]
  - Signature: `pub(super) fn generate_report_from_snapshot(`
  - Purpose: Generates a `ProjectGraphReport` from a `ReportGraphSnapshot` using default normalized `ProjectGraphReportOptions`. [crates/gcode/src/graph/report/generation.rs:65-76]
- `generate_report_from_snapshot_with_options` (function) component `generate_report_from_snapshot_with_options [function]` (`f0e586e1-4d76-5191-b194-c8fd1efd03ff`) lines 78-159 [crates/gcode/src/graph/report/generation.rs:78-159]
  - Signature: `fn generate_report_from_snapshot_with_options(`
  - Purpose: # Summary

Generates a `ProjectGraphReport` from a `ReportGraphSnapshot` by computing missing analysis components (summary, hotspots, unresolved/external targets, bridge relationships) with configurable options. [crates/gcode/src/graph/report/generation.rs:78-159]

