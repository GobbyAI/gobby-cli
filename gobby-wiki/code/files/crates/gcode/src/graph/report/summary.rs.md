---
title: crates/gcode/src/graph/report/summary.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/summary.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/report/summary.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Overview

`crates/gcode/src/graph/report/summary.rs` exposes 15 indexed API symbols.

## How it fits

`crates/gcode/src/graph/report/summary.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DegreeStats` | class | 'DegreeStats' is a struct that stores the in-degree and out-degree counts of a node as 'usize' values in the 'incoming' and 'outgoing' fields. [crates/gcode/src/graph/report/summary.rs:14-17] |
| `summarize_graph` | function | Builds a 'GraphReportSummary' by counting total nodes and edges and aggregating their occurrences by 'node_type' and 'edge_type' into 'BTreeMap's. [crates/gcode/src/graph/report/summary.rs:19-41] |
| `summarize_hotspots` | function | Returns the top 'top_n' hotspot entries for a code graph by delegating to 'gcore_hotspots_for_code_graph' with the provided 'nodes' and 'edges'. [crates/gcode/src/graph/report/summary.rs:43-49] |
| `gcore_hotspots_for_code_graph` | function | Builds an analytics graph from the supplied nodes and edges, computes graph and edge-degree statistics, and returns the top 'top_n' hotspot nodes partitioned into file, symbol, module, and incoming-call categories. [crates/gcode/src/graph/report/summary.rs:51-91] |
| `edge_degree_stats` | function | Computes per-code-degree counts by scanning 'edges' once and returning a 'HashMap' keyed by node name where each 'DegreeStats' accumulates 'outgoing' for 'edge.source' and 'incoming' for 'edge.target'. [crates/gcode/src/graph/report/summary.rs:93-100] |
| `gcore_incoming_call_hotspots` | function | Builds an analytics graph containing all nodes plus synthetic 'call:*' intermediates for 'CALLS' edges, computes centrality, filters to symbol nodes with nonzero degree, maps them into 'GraphHotspot's with incoming degree set and outgoing zero, sorts them, and returns the top 'top_n' hotspots. [crates/gcode/src/graph/report/summary.rs:102-156] |
| `analytics_top_hotspots` | function | Builds a node-id lookup, filters 'analytics.centrality' to included 'ReportNode's with positive degree, maps each to a 'GraphHotspot' using edge-degree stats when available, sorts the hotspots, truncates to 'top_n', and returns the resulting vector. [crates/gcode/src/graph/report/summary.rs:158-195] |
| `target_frequencies` | function | Counts 'CALLS' edges targeting nodes of 'target_type' by node ID, then returns the top 'top_n' 'TargetFrequency' records sorted by descending count and tie-broken by name then ID. [crates/gcode/src/graph/report/summary.rs:197-231] |
| `summarize_bridge_edges` | function | Returns the 'BridgeReportSummary' produced by 'gcore_bridge_summary_for_edges(edges)', or 'None' if no summary is available. [crates/gcode/src/graph/report/summary.rs:233-237] |
| `gcore_bridge_summary_for_edges` | function | Returns the direct bridge summary for the provided 'BridgeEdgeHypothesis' slice by delegating to 'bridge_summary_from_analytics_edges', yielding 'None' only if that summarization fails or is unavailable. [crates/gcode/src/graph/report/summary.rs:239-248] |
| `bridge_summary_from_analytics_edges` | function | Returns 'None' for an empty edge slice, otherwise aggregates the edges by 'metadata.source_system', computes the finite confidence min/max range when any confidence values are present, and builds a 'BridgeReportSummary' with 'RELATES_TO_CODE', the edge count, 'inferred = true', 'read_only = true', the per-source counts, and an optional confidence range. [crates/gcode/src/graph/report/summary.rs:250-290] |
| `normalize_bridge_edges` | function | Rebuilds each 'BridgeEdgeHypothesis' in the input vector via 'BridgeEdgeHypothesis::new' using its 'source_id', 'target_symbol_id', 'relation', and 'metadata', returning the resulting normalized vector. [crates/gcode/src/graph/report/summary.rs:294-308] |
| `suggested_questions` | function | Builds a vector of prioritized review questions for a report, always including a high-degree refactor question and conditionally adding questions based on incoming-call hotspots, unresolved/external targets, inferred bridges, and degraded report inputs. [crates/gcode/src/graph/report/summary.rs:310-339] |
| `sort_hotspots` | function | Sorts 'hotspots' in-place by descending 'degree', then ascending 'name', and finally ascending 'id' as a deterministic tie-breaker. [crates/gcode/src/graph/report/summary.rs:341-349] |
| `is_symbol_node` | function | Returns 'true' when 'node_type' is one of '"function"', '"method"', '"class"', '"type"', or '"property"', and 'false' otherwise. [crates/gcode/src/graph/report/summary.rs:351-356] |

