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

# crates/gcode/src/graph/report/summary.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

This file assembles graph-report analytics for code graphs. It counts nodes and edge types into a `GraphReportSummary`, then builds hotspot reports by turning `ReportNode` and `ReportCodeEdge` data into an analytics graph, computing degrees and centrality, and splitting the top results into files, symbols, modules, and incoming-call hotspots. It also summarizes bridge-edge hypotheses into a `BridgeReportSummary`, normalizes bridge edges into a canonical form, generates review questions from the presence of hotspots, unresolved/external targets, and inferred bridges, and provides small helpers for sorting hotspots, counting edge degrees, and identifying symbol-like node types.
[crates/gcode/src/graph/report/summary.rs:14-17]
[crates/gcode/src/graph/report/summary.rs:19-41]
[crates/gcode/src/graph/report/summary.rs:43-49]
[crates/gcode/src/graph/report/summary.rs:51-91]
[crates/gcode/src/graph/report/summary.rs:93-100]

## API Symbols

- `DegreeStats` (class) component `DegreeStats [class]` (`925017d8-d365-54d5-85b8-7aa496662e1c`) lines 14-17 [crates/gcode/src/graph/report/summary.rs:14-17]
  - Signature: `struct DegreeStats {`
  - Purpose: 'DegreeStats' is a struct that stores a node’s directed graph degree counts as two 'usize' fields: 'incoming' for in-degree and 'outgoing' for out-degree. [crates/gcode/src/graph/report/summary.rs:14-17]
- `summarize_graph` (function) component `summarize_graph [function]` (`bef7b28c-43f5-592a-b119-6908a02c3c0d`) lines 19-41 [crates/gcode/src/graph/report/summary.rs:19-41]
  - Signature: `pub(super) fn summarize_graph(`
  - Purpose: 'summarize_graph' computes a 'GraphReportSummary' by counting total nodes and edges and aggregating per-type frequencies for 'ReportNode.node_type' and 'ReportCodeEdge.edge_type' into 'BTreeMap's. [crates/gcode/src/graph/report/summary.rs:19-41]
- `summarize_hotspots` (function) component `summarize_hotspots [function]` (`cec6eee5-bd3c-5999-b0fa-d7134a561156`) lines 43-49 [crates/gcode/src/graph/report/summary.rs:43-49]
  - Signature: `pub(super) fn summarize_hotspots(`
  - Purpose: Returns the top 'top_n' code-graph hotspots by delegating to 'gcore_hotspots_for_code_graph' with the provided 'nodes' and 'edges', producing a 'GraphReportHotspots' result. [crates/gcode/src/graph/report/summary.rs:43-49]
- `gcore_hotspots_for_code_graph` (function) component `gcore_hotspots_for_code_graph [function]` (`1cc48fe7-57c1-552b-87be-3a25312cbdbd`) lines 51-91 [crates/gcode/src/graph/report/summary.rs:51-91]
  - Signature: `fn gcore_hotspots_for_code_graph(`
  - Purpose: Builds a graph analytics report from the given nodes and edges, then returns the top-degree hotspot nodes partitioned into files, symbols, and modules, plus incoming call hotspots. [crates/gcode/src/graph/report/summary.rs:51-91]
- `edge_degree_stats` (function) component `edge_degree_stats [function]` (`6a038b6e-5b0f-509f-ab0e-2c4d36366a30`) lines 93-100 [crates/gcode/src/graph/report/summary.rs:93-100]
  - Signature: `fn edge_degree_stats(edges: &[ReportCodeEdge]) -> HashMap<&str, DegreeStats> {`
  - Purpose: Builds a 'HashMap' keyed by node label that accumulates 'incoming' and 'outgoing' edge counts for each 'ReportCodeEdge' source and target in the input slice. [crates/gcode/src/graph/report/summary.rs:93-100]
- `gcore_incoming_call_hotspots` (function) component `gcore_incoming_call_hotspots [function]` (`b93d8daf-0360-5930-b283-c7cac27dd5fe`) lines 102-156 [crates/gcode/src/graph/report/summary.rs:102-156]
  - Signature: `fn gcore_incoming_call_hotspots(`
  - Purpose: Builds an analytics graph from all nodes plus synthetic 'CALLS' edge nodes, computes centrality, filters to symbol nodes with nonzero degree, and returns the top 'top_n' incoming-call hotspots sorted by hotspot rank with 'incoming = degree' and 'outgoing = 0'. [crates/gcode/src/graph/report/summary.rs:102-156]
- `analytics_top_hotspots` (function) component `analytics_top_hotspots [function]` (`1b4c649e-57ea-5272-bbb7-b3aa184e7fc0`) lines 158-195 [crates/gcode/src/graph/report/summary.rs:158-195]
  - Signature: `fn analytics_top_hotspots(`
  - Purpose: Builds a 'Vec<GraphHotspot>' for up to 'top_n' included nodes by joining analytics centrality scores to 'nodes' by ID, skipping nodes with zero degree, filling in edge degree stats from 'edge_degree' when available, sorting the resulting hotspots, and truncating the list. [crates/gcode/src/graph/report/summary.rs:158-195]
- `target_frequencies` (function) component `target_frequencies [function]` (`7eaf88da-8dc2-5fd6-878b-28e59dfd03ea`) lines 197-231 [crates/gcode/src/graph/report/summary.rs:197-231]
  - Signature: `pub(super) fn target_frequencies(`
  - Purpose: Counts 'CALLS' edges whose target node matches 'target_type', aggregates them by target id into 'TargetFrequency' records, then returns the top 'top_n' results sorted by descending count and tie-broken by name then id. [crates/gcode/src/graph/report/summary.rs:197-231]
- `summarize_bridge_edges` (function) component `summarize_bridge_edges [function]` (`95081d19-def9-50b6-8eb2-76258cb4debc`) lines 233-237 [crates/gcode/src/graph/report/summary.rs:233-237]
  - Signature: `pub(super) fn summarize_bridge_edges(`
  - Purpose: Returns the bridge-edge summary for the provided 'BridgeEdgeHypothesis' slice by delegating directly to 'gcore_bridge_summary_for_edges', yielding 'None' when no summary is produced. [crates/gcode/src/graph/report/summary.rs:233-237]
- `gcore_bridge_summary_for_edges` (function) component `gcore_bridge_summary_for_edges [function]` (`e7cb5812-0442-5589-bb3c-9bbc494b86e7`) lines 239-248 [crates/gcode/src/graph/report/summary.rs:239-248]
  - Signature: `fn gcore_bridge_summary_for_edges(edges: &[BridgeEdgeHypothesis]) -> Option<BridgeReportSummary> {`
  - Purpose: Returns the direct bridge-edge summary for the given 'BridgeEdgeHypothesis' slice by delegating to 'bridge_summary_from_analytics_edges', or 'None' if no summary can be produced. [crates/gcode/src/graph/report/summary.rs:239-248]
- `bridge_summary_from_analytics_edges` (function) component `bridge_summary_from_analytics_edges [function]` (`0573d814-3843-57a1-84c6-ec34ecb9fd97`) lines 250-290 [crates/gcode/src/graph/report/summary.rs:250-290]
  - Signature: `fn bridge_summary_from_analytics_edges(`
  - Purpose: Returns 'None' for an empty slice, otherwise aggregates 'BridgeEdgeHypothesis' entries into a 'BridgeReportSummary' with the total edge count, per-source-system counts, 'relation' set to 'RELATES_TO_CODE', 'inferred' and 'read_only' set 'true', and an optional finite confidence min/max range. [crates/gcode/src/graph/report/summary.rs:250-290]
- `normalize_bridge_edges` (function) component `normalize_bridge_edges [function]` (`152c72f0-394c-5195-b607-37dba9bc1a0f`) lines 294-308 [crates/gcode/src/graph/report/summary.rs:294-308]
  - Signature: `pub(super) fn normalize_bridge_edges(`
  - Purpose: Reconstructs each 'BridgeEdgeHypothesis' from the input vector via 'BridgeEdgeHypothesis::new', preserving 'source_id', 'target_symbol_id', 'relation', and 'metadata' while returning a new normalized 'Vec<BridgeEdgeHypothesis>'. [crates/gcode/src/graph/report/summary.rs:294-308]
- `suggested_questions` (function) component `suggested_questions [function]` (`c9df2982-392e-5ad5-bcc3-6547fb2ae40d`) lines 310-339 [crates/gcode/src/graph/report/summary.rs:310-339]
  - Signature: `pub(super) fn suggested_questions(`
  - Purpose: Builds a 'Vec<String>' of review questions for a graph report, always including a high-degree file/symbol refactor prompt and conditionally adding prompts for incoming-call hotspots, unresolved or external targets, inferred 'RELATES_TO_CODE' bridges, and degraded report inputs when the corresponding inputs are non-empty or present. [crates/gcode/src/graph/report/summary.rs:310-339]
- `sort_hotspots` (function) component `sort_hotspots [function]` (`64ba56fa-910b-5fd2-bfa0-ce613e729704`) lines 341-349 [crates/gcode/src/graph/report/summary.rs:341-349]
  - Signature: `fn sort_hotspots(hotspots: &mut [GraphHotspot]) {`
  - Purpose: Sorts 'hotspots' in place by descending 'degree', then ascending 'name', then ascending 'id' as deterministic tie-breakers. [crates/gcode/src/graph/report/summary.rs:341-349]
- `is_symbol_node` (function) component `is_symbol_node [function]` (`9939443a-02fa-51f8-8ddc-d352cb095bde`) lines 351-356 [crates/gcode/src/graph/report/summary.rs:351-356]
  - Signature: `fn is_symbol_node(node_type: &str) -> bool {`
  - Purpose: Returns 'true' when 'node_type' is one of '"function"', '"method"', '"class"', '"type"', or '"property"', and 'false' otherwise. [crates/gcode/src/graph/report/summary.rs:351-356]

