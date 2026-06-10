---
title: crates/gcode/src/graph/report/summary.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/summary.rs
  ranges:
  - 14-17
  - 19-41
  - 43-49
  - 51-91
  - 93-100
  - 102-156
  - 158-195
  - 197-231
  - 233-237
  - 239-275
  - 277-317
  - 319-329
  - 333-347
  - 349-378
  - 380-388
  - 390-395
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/report/summary.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

`crates/gcode/src/graph/report/summary.rs` exposes 16 indexed API symbols.
[crates/gcode/src/graph/report/summary.rs:14-17]
[crates/gcode/src/graph/report/summary.rs:19-41]
[crates/gcode/src/graph/report/summary.rs:43-49]
[crates/gcode/src/graph/report/summary.rs:51-91]
[crates/gcode/src/graph/report/summary.rs:93-100]
[crates/gcode/src/graph/report/summary.rs:102-156]
[crates/gcode/src/graph/report/summary.rs:158-195]
[crates/gcode/src/graph/report/summary.rs:197-231]
[crates/gcode/src/graph/report/summary.rs:233-237]
[crates/gcode/src/graph/report/summary.rs:239-275]
[crates/gcode/src/graph/report/summary.rs:277-317]
[crates/gcode/src/graph/report/summary.rs:319-329]
[crates/gcode/src/graph/report/summary.rs:333-347]
[crates/gcode/src/graph/report/summary.rs:349-378]
[crates/gcode/src/graph/report/summary.rs:380-388]
[crates/gcode/src/graph/report/summary.rs:390-395]

## API Symbols

- `DegreeStats` (class) component `DegreeStats [class]` (`1b9188fc-b061-57eb-ba0c-bf8f2b2563ec`) lines 14-17 [crates/gcode/src/graph/report/summary.rs:14-17]
  - Signature: `struct DegreeStats {`
  - Purpose: Indexed class `DegreeStats` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:14-17]
- `summarize_graph` (function) component `summarize_graph [function]` (`6f2f5615-8ab2-599f-bf2c-44493b4890c8`) lines 19-41 [crates/gcode/src/graph/report/summary.rs:19-41]
  - Signature: `pub(super) fn summarize_graph(`
  - Purpose: Indexed function `summarize_graph` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:19-41]
- `summarize_hotspots` (function) component `summarize_hotspots [function]` (`cbfd7503-3454-533b-bcbf-6a7881123cfe`) lines 43-49 [crates/gcode/src/graph/report/summary.rs:43-49]
  - Signature: `pub(super) fn summarize_hotspots(`
  - Purpose: Indexed function `summarize_hotspots` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:43-49]
- `gcore_hotspots_for_code_graph` (function) component `gcore_hotspots_for_code_graph [function]` (`256697eb-3260-5da6-8730-b028b9a3d578`) lines 51-91 [crates/gcode/src/graph/report/summary.rs:51-91]
  - Signature: `fn gcore_hotspots_for_code_graph(`
  - Purpose: Indexed function `gcore_hotspots_for_code_graph` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:51-91]
- `edge_degree_stats` (function) component `edge_degree_stats [function]` (`009b304a-4e55-5816-99ea-938130de7ee9`) lines 93-100 [crates/gcode/src/graph/report/summary.rs:93-100]
  - Signature: `fn edge_degree_stats(edges: &[ReportCodeEdge]) -> HashMap<&str, DegreeStats> {`
  - Purpose: Indexed function `edge_degree_stats` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:93-100]
- `gcore_incoming_call_hotspots` (function) component `gcore_incoming_call_hotspots [function]` (`6be392bf-708d-562c-a0c7-387684751985`) lines 102-156 [crates/gcode/src/graph/report/summary.rs:102-156]
  - Signature: `fn gcore_incoming_call_hotspots(`
  - Purpose: Indexed function `gcore_incoming_call_hotspots` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:102-156]
- `analytics_top_hotspots` (function) component `analytics_top_hotspots [function]` (`41b21694-17bd-593c-a79a-d2ba9d3155db`) lines 158-195 [crates/gcode/src/graph/report/summary.rs:158-195]
  - Signature: `fn analytics_top_hotspots(`
  - Purpose: Indexed function `analytics_top_hotspots` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:158-195]
- `target_frequencies` (function) component `target_frequencies [function]` (`c26052ea-da95-5d91-a445-496dbde9e891`) lines 197-231 [crates/gcode/src/graph/report/summary.rs:197-231]
  - Signature: `pub(super) fn target_frequencies(`
  - Purpose: Indexed function `target_frequencies` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:197-231]
- `summarize_bridge_edges` (function) component `summarize_bridge_edges [function]` (`c2fc5858-0831-5bf4-9194-6e698e80d73e`) lines 233-237 [crates/gcode/src/graph/report/summary.rs:233-237]
  - Signature: `pub(super) fn summarize_bridge_edges(`
  - Purpose: Indexed function `summarize_bridge_edges` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:233-237]
- `gcore_bridge_summary_for_edges` (function) component `gcore_bridge_summary_for_edges [function]` (`edf1bb51-29f7-531b-bc41-d1854aa0f1a8`) lines 239-275 [crates/gcode/src/graph/report/summary.rs:239-275]
  - Signature: `fn gcore_bridge_summary_for_edges(edges: &[BridgeEdgeHypothesis]) -> Option<BridgeReportSummary> {`
  - Purpose: Indexed function `gcore_bridge_summary_for_edges` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:239-275]
- `bridge_summary_from_analytics_edges` (function) component `bridge_summary_from_analytics_edges [function]` (`725671b1-345b-5368-8440-bfa739f0f387`) lines 277-317 [crates/gcode/src/graph/report/summary.rs:277-317]
  - Signature: `fn bridge_summary_from_analytics_edges(`
  - Purpose: Indexed function `bridge_summary_from_analytics_edges` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:277-317]
- `bridge_analytics_nodes` (function) component `bridge_analytics_nodes [function]` (`760705a1-521d-5b02-94af-4b71a825c14f`) lines 319-329 [crates/gcode/src/graph/report/summary.rs:319-329]
  - Signature: `fn bridge_analytics_nodes(edges: &[BridgeEdgeHypothesis]) -> Vec<(String, String, f64)> {`
  - Purpose: Indexed function `bridge_analytics_nodes` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:319-329]
- `normalize_bridge_edges` (function) component `normalize_bridge_edges [function]` (`6c99d805-b521-5cb6-b98b-3914edc8429b`) lines 333-347 [crates/gcode/src/graph/report/summary.rs:333-347]
  - Signature: `pub(super) fn normalize_bridge_edges(`
  - Purpose: Indexed function `normalize_bridge_edges` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:333-347]
- `suggested_questions` (function) component `suggested_questions [function]` (`19746df8-f404-5edf-bfd7-01e277739958`) lines 349-378 [crates/gcode/src/graph/report/summary.rs:349-378]
  - Signature: `pub(super) fn suggested_questions(`
  - Purpose: Indexed function `suggested_questions` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:349-378]
- `sort_hotspots` (function) component `sort_hotspots [function]` (`611e6df0-8875-5913-95a4-52e0ed78efd9`) lines 380-388 [crates/gcode/src/graph/report/summary.rs:380-388]
  - Signature: `fn sort_hotspots(hotspots: &mut [GraphHotspot]) {`
  - Purpose: Indexed function `sort_hotspots` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:380-388]
- `is_symbol_node` (function) component `is_symbol_node [function]` (`db6e7f0e-dfb0-5948-8313-779e6fde1b4f`) lines 390-395 [crates/gcode/src/graph/report/summary.rs:390-395]
  - Signature: `fn is_symbol_node(node_type: &str) -> bool {`
  - Purpose: Indexed function `is_symbol_node` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:390-395]

