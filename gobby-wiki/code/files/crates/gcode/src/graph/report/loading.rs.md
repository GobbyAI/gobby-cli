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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/report/loading.rs:18-78](crates/gcode/src/graph/report/loading.rs#L18-L78), [crates/gcode/src/graph/report/loading.rs:80-95](crates/gcode/src/graph/report/loading.rs#L80-L95), [crates/gcode/src/graph/report/loading.rs:97-111](crates/gcode/src/graph/report/loading.rs#L97-L111), [crates/gcode/src/graph/report/loading.rs:113-128](crates/gcode/src/graph/report/loading.rs#L113-L128), [crates/gcode/src/graph/report/loading.rs:130-146](crates/gcode/src/graph/report/loading.rs#L130-L146)

</details>

# crates/gcode/src/graph/report/loading.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

Builds a graph-report snapshot from the Falkor graph client by running report queries and converting result rows into typed summary data. `load_report_snapshot` is the orchestrator: it gathers node and edge counts, hotspot groups, target frequencies, and bridge-edge candidates, then packages them into a `ReportGraphSnapshot`. The helper loaders each handle one slice of the report, with `collect_report_rows` providing shared row collection and transformation for the bridge-edge and other row-to-typed conversions.
[crates/gcode/src/graph/report/loading.rs:18-78]
[crates/gcode/src/graph/report/loading.rs:80-95]
[crates/gcode/src/graph/report/loading.rs:97-111]
[crates/gcode/src/graph/report/loading.rs:113-128]
[crates/gcode/src/graph/report/loading.rs:130-146]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `load_report_snapshot` | function | `pub(super) fn load_report_snapshot(` | `load_report_snapshot [function]` | `84e19c1d-61b0-598f-888a-90153e662249` | 18-78 [crates/gcode/src/graph/report/loading.rs:18-78] | Indexed function `load_report_snapshot` in `crates/gcode/src/graph/report/loading.rs`. [crates/gcode/src/graph/report/loading.rs:18-78] |
| `load_hotspots` | function | `fn load_hotspots(` | `load_hotspots [function]` | `5ad444d5-80f0-5359-92f1-6bf86dd21413` | 80-95 [crates/gcode/src/graph/report/loading.rs:80-95] | Indexed function `load_hotspots` in `crates/gcode/src/graph/report/loading.rs`. [crates/gcode/src/graph/report/loading.rs:80-95] |
| `load_incoming_call_hotspots` | function | `fn load_incoming_call_hotspots(` | `load_incoming_call_hotspots [function]` | `44c52bb8-57e0-5886-8ef4-eed59fbd332c` | 97-111 [crates/gcode/src/graph/report/loading.rs:97-111] | Indexed function `load_incoming_call_hotspots` in `crates/gcode/src/graph/report/loading.rs`. [crates/gcode/src/graph/report/loading.rs:97-111] |
| `load_target_frequencies` | function | `fn load_target_frequencies(` | `load_target_frequencies [function]` | `ceaf1a7e-466e-586d-a445-21c5b1b3ce1c` | 113-128 [crates/gcode/src/graph/report/loading.rs:113-128] | Indexed function `load_target_frequencies` in `crates/gcode/src/graph/report/loading.rs`. [crates/gcode/src/graph/report/loading.rs:113-128] |
| `collect_report_rows` | function | `fn collect_report_rows<T>(rows: &[Row], label: &str, mapper: impl Fn(&Row) -> Option<T>) -> Vec<T> {` | `collect_report_rows [function]` | `f78fff36-26fb-56b9-ad90-02a78833f458` | 130-146 [crates/gcode/src/graph/report/loading.rs:130-146] | Indexed function `collect_report_rows` in `crates/gcode/src/graph/report/loading.rs`. [crates/gcode/src/graph/report/loading.rs:130-146] |
