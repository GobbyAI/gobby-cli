---
title: crates/gcode/src/graph/report/loading.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/loading.rs
  ranges:
  - 18-78
  - 80-95
  - 97-111
  - 113-128
  - 130-146
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/report/loading.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

`crates/gcode/src/graph/report/loading.rs` exposes 5 indexed API symbols.
[crates/gcode/src/graph/report/loading.rs:18-78]
[crates/gcode/src/graph/report/loading.rs:80-95]
[crates/gcode/src/graph/report/loading.rs:97-111]
[crates/gcode/src/graph/report/loading.rs:113-128]
[crates/gcode/src/graph/report/loading.rs:130-146]

## API Symbols

- `load_report_snapshot` (function) component `load_report_snapshot [function]` (`84e19c1d-61b0-598f-888a-90153e662249`) lines 18-78 [crates/gcode/src/graph/report/loading.rs:18-78]
  - Signature: `pub(super) fn load_report_snapshot(`
  - Purpose: Loads a graph report snapshot containing aggregated statistics (node/edge counts by type), high-degree hotspots across files/symbols/modules, and unresolved/external target frequencies for a specified project by executing multiple graph database queries. [crates/gcode/src/graph/report/loading.rs:18-78]
- `load_hotspots` (function) component `load_hotspots [function]` (`5ad444d5-80f0-5359-92f1-6bf86dd21413`) lines 80-95 [crates/gcode/src/graph/report/loading.rs:80-95]
  - Signature: `fn load_hotspots(`
  - Purpose: Executes a parameterized query on a GraphClient to fetch and transform the top N hotspots for a specified node class within a project into a `Vec<GraphHotspot>`. [crates/gcode/src/graph/report/loading.rs:80-95]
- `load_incoming_call_hotspots` (function) component `load_incoming_call_hotspots [function]` (`44c52bb8-57e0-5886-8ef4-eed59fbd332c`) lines 97-111 [crates/gcode/src/graph/report/loading.rs:97-111]
  - Signature: `fn load_incoming_call_hotspots(`
  - Purpose: Queries a GraphClient for the top N incoming call hotspots for a given project and transforms the result rows into GraphHotspot objects. [crates/gcode/src/graph/report/loading.rs:97-111]
- `load_target_frequencies` (function) component `load_target_frequencies [function]` (`ceaf1a7e-466e-586d-a445-21c5b1b3ce1c`) lines 113-128 [crates/gcode/src/graph/report/loading.rs:113-128]
  - Signature: `fn load_target_frequencies(`
  - Purpose: Executes a graph database query to retrieve the top N target frequencies for a specified project and target type, converting the results into a `Vec<TargetFrequency>`. [crates/gcode/src/graph/report/loading.rs:113-128]
- `collect_report_rows` (function) component `collect_report_rows [function]` (`f78fff36-26fb-56b9-ad90-02a78833f458`) lines 130-146 [crates/gcode/src/graph/report/loading.rs:130-146]
  - Signature: `fn collect_report_rows<T>(rows: &[Row], label: &str, mapper: impl Fn(&Row) -> Option<T>) -> Vec<T> {`
  - Purpose: Applies a fallible mapper function to a row slice, collecting successful results into a vector while logging warnings for dropped entries. [crates/gcode/src/graph/report/loading.rs:130-146]

