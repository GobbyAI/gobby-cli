---
title: crates/gcode/src/graph/report
type: code_module
provenance:
- file: crates/gcode/src/graph/report/generation.rs
- file: crates/gcode/src/graph/report/loading.rs
- file: crates/gcode/src/graph/report/queries.rs
- file: crates/gcode/src/graph/report/render.rs
- file: crates/gcode/src/graph/report/rows.rs
- file: crates/gcode/src/graph/report/summary.rs
- file: crates/gcode/src/graph/report/tests.rs
- file: crates/gcode/src/graph/report/time.rs
- file: crates/gcode/src/graph/report/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/report

Parent: [[code/modules/crates/gcode/src/graph|crates/gcode/src/graph]]

## Overview

`crates/gcode/src/graph/report` builds project graph reports from snapshots or loaded graph rows, then renders the same report as structured JSON plus Markdown. Its core model is `ProjectGraphReport`, which carries project identity, generation time, summary counts, hotspots, unresolved/external targets, optional bridge summaries, degradation details, suggested questions, and rendered Markdown (`crates/gcode/src/graph/report/types.rs:42-61`). Report sizing is controlled by `ProjectGraphReportOptions`, whose default `top_n` comes from `DEFAULT_TOP_LIMIT` (`crates/gcode/src/graph/report/types.rs:64-76`).

The main flow is: collect or load graph-shaped inputs, normalize database rows into typed report records, summarize graph structure, then render. Row conversion functions translate Falkor rows into named counts, hotspots, target frequencies, and bridge-edge hypotheses while preserving projection provenance and confidence metadata (`crates/gcode/src/graph/report/rows.rs:1-100`). Summary code counts nodes and code edges, builds analytics graphs through `GraphPayload::analytics_graph_from_parts`, and delegates centrality-style analysis to `gobby_core::graph_analytics::analyze` for high-degree files, symbols, and modules (`crates/gcode/src/graph/report/summary.rs:1-100`).

This module sits between storage/query code, graph analytics, report rendering, and callers that need stable report artifacts. It imports Serde for serialized report structs, `ProjectionMetadata`/`ProjectionProvenance` for bridge evidence, `gobby_core::falkor::Row` for query result ingestion, and `GraphPayload` plus `gobby_core` analytics for graph scoring (`crates/gcode/src/graph/report/types.rs:1-6`, `crates/gcode/src/graph/report/rows.rs:1-8`, `crates/gcode/src/graph/report/summary.rs:1-8`). Tests exercise the public snapshot path by constructing a `ReportGraphSnapshot`, calling `generate_report_from_snapshot`, and asserting JSON shape, summary counts, hotspots, unresolved/external targets, and bridge behavior (`crates/gcode/src/graph/report/tests.rs:1-100`).

| Public surface | Symbols |
| --- | --- |
| Generation | `generate_report`, `generate_report_with_options`, `generate_report_from_snapshot`, `generate_report_from_snapshot_with_options`, `empty_report` |
| Loading/querying | `load_report_snapshot`, `load_hotspots`, `load_incoming_call_hotspots`, `load_target_frequencies`, `collect_report_rows` |
| Rendering | `RenderMarkdownInput`, `render_markdown`, `append_hotspot_section`, `append_target_section` |
| Core report types | `ProjectGraphReport`, `ProjectGraphReportOptions`, `GraphReportSummary`, `GraphReportHotspots`, `GraphHotspot`, `TargetFrequency`, `BridgeReportSummary`, `ReportDegradation` |
| Snapshot/input types | `ReportGraphSnapshot`, `ReportNode`, `ReportCodeEdge`, `BridgeEdgeInput`, `BridgeEdgeHypothesis` |
| Row helpers | `rows_to_named_counts`, `row_to_graph_hotspot`, `row_to_target_frequency`, `row_to_bridge_edge_hypothesis` |

| Option/key | Meaning | Source |
| --- | --- | --- |
| `top_n` | Limits report rankings such as hotspots and target lists. | `crates/gcode/src/graph/report/types.rs:64-76` |
| `DEFAULT_TOP_LIMIT` | Default used by `ProjectGraphReportOptions::default`. | `crates/gcode/src/graph/report/types.rs:4-6` |
[crates/gcode/src/graph/report/generation.rs:21-23]
[crates/gcode/src/graph/report/loading.rs:18-78]
[crates/gcode/src/graph/report/render.rs:8-18]
[crates/gcode/src/graph/report/rows.rs:11-19]
[crates/gcode/src/graph/report/summary.rs:14-17]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/graph/report/generation.rs\|crates/gcode/src/graph/report/generation.rs]] | `crates/gcode/src/graph/report/generation.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/report/loading.rs\|crates/gcode/src/graph/report/loading.rs]] | `crates/gcode/src/graph/report/loading.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/report/queries.rs\|crates/gcode/src/graph/report/queries.rs]] | `crates/gcode/src/graph/report/queries.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/report/render.rs\|crates/gcode/src/graph/report/render.rs]] | `crates/gcode/src/graph/report/render.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/report/rows.rs\|crates/gcode/src/graph/report/rows.rs]] | `crates/gcode/src/graph/report/rows.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/report/summary.rs\|crates/gcode/src/graph/report/summary.rs]] | `crates/gcode/src/graph/report/summary.rs` exposes 15 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/report/tests.rs\|crates/gcode/src/graph/report/tests.rs]] | `crates/gcode/src/graph/report/tests.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/report/time.rs\|crates/gcode/src/graph/report/time.rs]] | `crates/gcode/src/graph/report/time.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gcode/src/graph/report/types.rs\|crates/gcode/src/graph/report/types.rs]] | `crates/gcode/src/graph/report/types.rs` exposes 27 indexed API symbols. |

