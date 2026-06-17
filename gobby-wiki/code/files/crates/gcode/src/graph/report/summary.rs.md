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
  - 239-248
  - 250-290
  - 294-308
  - 310-339
  - 341-349
  - 351-356
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/report/summary.rs:14-17](crates/gcode/src/graph/report/summary.rs#L14-L17), [crates/gcode/src/graph/report/summary.rs:19-41](crates/gcode/src/graph/report/summary.rs#L19-L41), [crates/gcode/src/graph/report/summary.rs:43-49](crates/gcode/src/graph/report/summary.rs#L43-L49), [crates/gcode/src/graph/report/summary.rs:51-91](crates/gcode/src/graph/report/summary.rs#L51-L91), [crates/gcode/src/graph/report/summary.rs:93-100](crates/gcode/src/graph/report/summary.rs#L93-L100), [crates/gcode/src/graph/report/summary.rs:102-156](crates/gcode/src/graph/report/summary.rs#L102-L156), [crates/gcode/src/graph/report/summary.rs:158-195](crates/gcode/src/graph/report/summary.rs#L158-L195), [crates/gcode/src/graph/report/summary.rs:197-231](crates/gcode/src/graph/report/summary.rs#L197-L231), [crates/gcode/src/graph/report/summary.rs:233-237](crates/gcode/src/graph/report/summary.rs#L233-L237), [crates/gcode/src/graph/report/summary.rs:239-248](crates/gcode/src/graph/report/summary.rs#L239-L248), [crates/gcode/src/graph/report/summary.rs:250-290](crates/gcode/src/graph/report/summary.rs#L250-L290), [crates/gcode/src/graph/report/summary.rs:294-308](crates/gcode/src/graph/report/summary.rs#L294-L308), [crates/gcode/src/graph/report/summary.rs:310-339](crates/gcode/src/graph/report/summary.rs#L310-L339), [crates/gcode/src/graph/report/summary.rs:341-349](crates/gcode/src/graph/report/summary.rs#L341-L349), [crates/gcode/src/graph/report/summary.rs:351-356](crates/gcode/src/graph/report/summary.rs#L351-L356)

</details>

# crates/gcode/src/graph/report/summary.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

Builds graph reporting summaries and hotspot analysis from code graph nodes and edges. `summarize_graph` counts nodes and edges by type into a `GraphReportSummary`, while `summarize_hotspots` delegates to `gcore_hotspots_for_code_graph`, which converts the report data into a `GraphPayload`, runs analytics, computes edge degree stats, and assembles `GraphReportHotspots` for files, symbols, modules, and additional hotspot views. The rest of the file is a set of helpers that rank and normalize hotspot candidates (`analytics_top_hotspots`, `sort_hotspots`, `edge_degree_stats`, `target_frequencies`, `normalize_bridge_edges`) and derive bridge/call summaries and suggested follow-up questions from the analytics results.
[crates/gcode/src/graph/report/summary.rs:14-17]
[crates/gcode/src/graph/report/summary.rs:19-41]
[crates/gcode/src/graph/report/summary.rs:43-49]
[crates/gcode/src/graph/report/summary.rs:51-91]
[crates/gcode/src/graph/report/summary.rs:93-100]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `DegreeStats` | class | `struct DegreeStats {` | `DegreeStats [class]` | `925017d8-d365-54d5-85b8-7aa496662e1c` | 14-17 [crates/gcode/src/graph/report/summary.rs:14-17] | Indexed class `DegreeStats` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:14-17] |
| `summarize_graph` | function | `pub(super) fn summarize_graph(` | `summarize_graph [function]` | `bef7b28c-43f5-592a-b119-6908a02c3c0d` | 19-41 [crates/gcode/src/graph/report/summary.rs:19-41] | Indexed function `summarize_graph` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:19-41] |
| `summarize_hotspots` | function | `pub(super) fn summarize_hotspots(` | `summarize_hotspots [function]` | `cec6eee5-bd3c-5999-b0fa-d7134a561156` | 43-49 [crates/gcode/src/graph/report/summary.rs:43-49] | Indexed function `summarize_hotspots` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:43-49] |
| `gcore_hotspots_for_code_graph` | function | `fn gcore_hotspots_for_code_graph(` | `gcore_hotspots_for_code_graph [function]` | `1cc48fe7-57c1-552b-87be-3a25312cbdbd` | 51-91 [crates/gcode/src/graph/report/summary.rs:51-91] | Indexed function `gcore_hotspots_for_code_graph` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:51-91] |
| `edge_degree_stats` | function | `fn edge_degree_stats(edges: &[ReportCodeEdge]) -> HashMap<&str, DegreeStats> {` | `edge_degree_stats [function]` | `6a038b6e-5b0f-509f-ab0e-2c4d36366a30` | 93-100 [crates/gcode/src/graph/report/summary.rs:93-100] | Indexed function `edge_degree_stats` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:93-100] |
| `gcore_incoming_call_hotspots` | function | `fn gcore_incoming_call_hotspots(` | `gcore_incoming_call_hotspots [function]` | `b93d8daf-0360-5930-b283-c7cac27dd5fe` | 102-156 [crates/gcode/src/graph/report/summary.rs:102-156] | Indexed function `gcore_incoming_call_hotspots` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:102-156] |
| `analytics_top_hotspots` | function | `fn analytics_top_hotspots(` | `analytics_top_hotspots [function]` | `1b4c649e-57ea-5272-bbb7-b3aa184e7fc0` | 158-195 [crates/gcode/src/graph/report/summary.rs:158-195] | Indexed function `analytics_top_hotspots` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:158-195] |
| `target_frequencies` | function | `pub(super) fn target_frequencies(` | `target_frequencies [function]` | `7eaf88da-8dc2-5fd6-878b-28e59dfd03ea` | 197-231 [crates/gcode/src/graph/report/summary.rs:197-231] | Indexed function `target_frequencies` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:197-231] |
| `summarize_bridge_edges` | function | `pub(super) fn summarize_bridge_edges(` | `summarize_bridge_edges [function]` | `95081d19-def9-50b6-8eb2-76258cb4debc` | 233-237 [crates/gcode/src/graph/report/summary.rs:233-237] | Indexed function `summarize_bridge_edges` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:233-237] |
| `gcore_bridge_summary_for_edges` | function | `fn gcore_bridge_summary_for_edges(edges: &[BridgeEdgeHypothesis]) -> Option<BridgeReportSummary> {` | `gcore_bridge_summary_for_edges [function]` | `e7cb5812-0442-5589-bb3c-9bbc494b86e7` | 239-248 [crates/gcode/src/graph/report/summary.rs:239-248] | Indexed function `gcore_bridge_summary_for_edges` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:239-248] |
| `bridge_summary_from_analytics_edges` | function | `fn bridge_summary_from_analytics_edges(` | `bridge_summary_from_analytics_edges [function]` | `0573d814-3843-57a1-84c6-ec34ecb9fd97` | 250-290 [crates/gcode/src/graph/report/summary.rs:250-290] | Indexed function `bridge_summary_from_analytics_edges` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:250-290] |
| `normalize_bridge_edges` | function | `pub(super) fn normalize_bridge_edges(` | `normalize_bridge_edges [function]` | `152c72f0-394c-5195-b607-37dba9bc1a0f` | 294-308 [crates/gcode/src/graph/report/summary.rs:294-308] | Indexed function `normalize_bridge_edges` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:294-308] |
| `suggested_questions` | function | `pub(super) fn suggested_questions(` | `suggested_questions [function]` | `c9df2982-392e-5ad5-bcc3-6547fb2ae40d` | 310-339 [crates/gcode/src/graph/report/summary.rs:310-339] | Indexed function `suggested_questions` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:310-339] |
| `sort_hotspots` | function | `fn sort_hotspots(hotspots: &mut [GraphHotspot]) {` | `sort_hotspots [function]` | `64ba56fa-910b-5fd2-bfa0-ce613e729704` | 341-349 [crates/gcode/src/graph/report/summary.rs:341-349] | Indexed function `sort_hotspots` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:341-349] |
| `is_symbol_node` | function | `fn is_symbol_node(node_type: &str) -> bool {` | `is_symbol_node [function]` | `9939443a-02fa-51f8-8ddc-d352cb095bde` | 351-356 [crates/gcode/src/graph/report/summary.rs:351-356] | Indexed function `is_symbol_node` in `crates/gcode/src/graph/report/summary.rs`. [crates/gcode/src/graph/report/summary.rs:351-356] |
