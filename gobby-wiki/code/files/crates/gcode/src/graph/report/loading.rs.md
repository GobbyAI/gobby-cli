---
title: crates/gcode/src/graph/report/loading.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/loading.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/report/loading.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Overview

`crates/gcode/src/graph/report/loading.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gcode/src/graph/report/loading.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `load_report_snapshot` | function | Loads a 'ReportGraphSnapshot' for a project by querying graph node and code-edge counts, computing summary totals, fetching top-N hotspot and target-frequency metadata, and collecting available bridge-edge hypotheses. [crates/gcode/src/graph/report/loading.rs:18-78] |
| `load_hotspots` | function | Queries the graph client for the top 'top_n' hotspots for a given 'project_id' and 'node_class', then converts the returned rows into 'GraphHotspot' values and returns them as a 'Result<Vec<GraphHotspot>>'. [crates/gcode/src/graph/report/loading.rs:80-95] |
| `load_incoming_call_hotspots` | function | Builds and executes the incoming-call-hotspots graph query for the given 'project_id' and 'top_n', then converts the returned rows into a 'Vec<GraphHotspot>' with contextual error handling. [crates/gcode/src/graph/report/loading.rs:97-111] |
| `load_target_frequencies` | function | Builds and executes a graph query for the top 'top_n' target frequencies for the given project and target type, then converts the returned rows into a 'Vec<TargetFrequency>' with contextual error handling. [crates/gcode/src/graph/report/loading.rs:113-128] |
| `collect_report_rows` | function | Collects 'T' values from 'rows' by applying 'mapper' to each 'Row', silently skipping 'None' results while counting them, and emits a warning with 'label' if any malformed rows were dropped. [crates/gcode/src/graph/report/loading.rs:130-146] |

