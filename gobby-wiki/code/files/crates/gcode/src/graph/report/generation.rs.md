---
title: crates/gcode/src/graph/report/generation.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/generation.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/report/generation.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Overview

`crates/gcode/src/graph/report/generation.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gcode/src/graph/report/generation.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `generate_report` | function | 'generate_report' delegates to 'generate_report_with_options' using 'ProjectGraphReportOptions::default()' and returns its 'Result<ProjectGraphReport, ProjectGraphReportError>'. [crates/gcode/src/graph/report/generation.rs:21-23] |
| `generate_report_with_options` | function | 'generate_report_with_options' validates that FalkorDB is configured, normalizes the supplied options, loads a report snapshot via 'gobby_core::falkor::with_graph' using 'options.top_n', and then either builds a 'ProjectGraphReport' from that snapshot or maps configuration/query/service failures into the შესაბამის 'ProjectGraphReportError' variant. [crates/gcode/src/graph/report/generation.rs:25-59] |
| `empty_report` | function | Creates and returns a 'ProjectGraphReport' by converting 'project_id' into a 'String' and passing it, the current ISO-8601 timestamp, and a default 'ReportGraphSnapshot' to 'generate_report_from_snapshot'. [crates/gcode/src/graph/report/generation.rs:61-63] |
| `generate_report_from_snapshot` | function | Constructs a 'ProjectGraphReport' from a 'ReportGraphSnapshot' by delegating to 'generate_report_from_snapshot_with_options' with the default normalized 'ProjectGraphReportOptions'. [crates/gcode/src/graph/report/generation.rs:65-76] |
| `generate_report_from_snapshot_with_options` | function | Builds a 'ProjectGraphReport' from a snapshot by normalizing identifiers, deriving or reusing the graph summary, hotspots, unresolved and external target frequencies, and bridge-edge summary, while recording any missing bridge-edge input as a sorted degradation detail. [crates/gcode/src/graph/report/generation.rs:78-159] |

