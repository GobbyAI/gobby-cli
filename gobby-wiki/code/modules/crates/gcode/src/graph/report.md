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

## crates/gcode/src/graph/report

The `report` module is the analytics and reporting layer of the `gcode` graph subsystem. Its central responsibility is producing `ProjectGraphReport` — a fully self-contained, serializable snapshot of a project's code graph that bundles structural summaries, degree-based hotspot rankings, unresolved and external dependency frequencies, optional bridge-edge hypotheses, degradation notices, suggested investigation questions, and a pre-rendered Markdown document. Two generation paths are provided: a live path that queries a running graph database and a snapshot path (`generate_report_from_snapshot` / `generate_report_from_snapshot_with_options`) that operates entirely in memory from a pre-loaded `ReportGraphSnapshot`, making it suitable for tests and offline analysis (types.rs:54–65, generation.rs component table).

The internal pipeline flows through four cooperating sub-files. `queries.rs` constructs the parameterised graph-database queries for node counts, edge counts, hotspots, incoming-call hotspots, target frequencies, and bridge edges, using helper expressions `report_node_type_case`, `report_node_id_expr`, and `report_node_name_expr` to normalise heterogeneous node shapes. `loading.rs` executes those queries and materialises the raw row streams into typed collections via `load_report_snapshot`, `load_hotspots`, `load_incoming_call_hotspots`, and `load_target_frequencies`. `rows.rs` provides the low-level row-to-struct converters (`row_string`, `row_usize`, `row_f64`, and their compound forms `row_to_graph_hotspot`, `row_to_target_frequency`, `row_to_bridge_edge_hypothesis`) that safely extract values from `gobby_core::falkor::Row` instances (rows.rs:1–65). `summary.rs` then applies `gobby_core::graph_analytics::analyze` to the assembled `GraphPayload` to derive centrality and degree statistics, building `GraphReportHotspots` (files, symbols, modules, incoming-call leaders) and `BridgeReportSummary` (aggregating cross-source-system hypothesis edges); `render.rs` finally formats the result as CommonMark Markdown, including backtick-safe inline code via `max_backtick_run` (render.rs component table).

This module collaborates outward with `gobby_core::graph_analytics` for centralised graph-analytics computation and `gobby_core::falkor::Row` for database row access (rows.rs:4, summary.rs:3). It imports domain models from `crate::models::{ProjectionMetadata, ProjectionProvenance}` and graph primitives from `crate::graph::code_graph::GraphPayload` (summary.rs:4–5). Callers elsewhere in the codebase drive the module through the generation entry points; tests in `tests.rs` exercise both the snapshot-based generation path and the Markdown renderer directly (tests.rs:1–100), including a pinned-output contract (`graph_report_hotspots_and_bridge_summary_match_pinned_output`) and a degradation contract (`report_degradation_contract`).

### Public API — Generation

| Symbol | File | Description |
|---|---|---|
| `generate_report` | generation.rs | Live-query generation with default options |
| `generate_report_with_options` | generation.rs | Live-query generation with explicit `ProjectGraphReportOptions` |
| `empty_report` | generation.rs | Returns a zero-content report (fallback/error path) |
| `generate_report_from_snapshot` | generation.rs | In-memory generation from a `ReportGraphSnapshot` |
| `generate_report_from_snapshot_with_options` | generation.rs | In-memory generation with explicit options |

### Public API — Core Types

| Type | Key Fields / Notes |
|---|---|
| `ProjectGraphReport` | `project_id`, `summary`, `hotspots`, `unresolved_targets`, `external_targets`, `bridge_summary`, `bridge_edges`, `degradation_details`, `markdown` (types.rs:54–65) |
| `ProjectGraphReportOptions` | `top_n: usize`; defaults to `DEFAULT_TOP_LIMIT`; has `normalized()` helper (types.rs:67–79) |
| `ReportGraphSnapshot` | Input DTO: `nodes`, `code_edges`, `bridge_edges: BridgeEdgeInput` |
| `ReportNode` | `id`, `name`, `node_type`, optional `file_path`; built via `new` + `with_file_path` (types.rs) |
| `ReportCodeEdge` | `source`, `target`, `edge_type`; built via `new` (types.rs) |
| `BridgeEdgeHypothesis` | `source_id`, `target_symbol_id`, `relation`, `read_only: true`, `metadata: ProjectionMetadata`; built via `new` or `inferred` (types.rs:9–49) |
| `BridgeEdgeInput` | Enum wrapper: `available(Vec<BridgeEdgeHypothesis>)` / `unavailable()` / `default()` |
| `GraphReportSummary` | `node_count`, `edge_count`, `node_counts_by_type`, `code_edge_counts` |
| `GraphReportHotspots` | `high_degree_files`, `high_degree_symbols`, `high_degree_modules`, `incoming_call_hotspots` |
| `BridgeReportSummary` | Aggregated bridge-edge data with `ConfidenceRange` |
| `ReportDegradation` | Degradation notice entries appended to `degradation_details` |
| `ProjectGraphReportError` | Error type with `fmt` impl |

### Public API — Queries

| Function | Purpose |
|---|---|
| `report_node_type_case` | CASE expression normalising node types |
| `report_node_id_expr` | Expression selecting node ID |
| `report_node_name_expr` | Expression selecting node display name |
| `report_node_counts_query` | Counts nodes grouped by type |
| `report_code_edge_counts_query` | Counts edges grouped by type |
| `report_hotspots_query` | Degree-ranked hotspot nodes |
| `report_incoming_call_hotspots_query` | Nodes ranked by incoming call edges |
| `report_target_frequencies_query` | Frequency of unresolved/external targets |
| `report_bridge_edges_query` | Bridge-edge hypothesis rows |

### Public API — Loading & Summary

| Function | File | Purpose |
|---|---|---|
| `load_report_snapshot` | loading.rs | Executes all queries; returns `ReportGraphSnapshot` |
| `load_hotspots` | loading.rs | Materialises hotspot query rows |
| `load_incoming_call_hotspots` | loading.rs | Materialises incoming-call hotspot rows |
| `load_target_frequencies` | loading.rs | Materialises target-frequency rows |
| `summarize_graph` | summary.rs | Builds `GraphReportSummary` from nodes + edges |
| `summarize_hotspots` | summary.rs | Runs `gobby_core` analytics; returns `GraphReportHotspots` |
| `summarize_bridge_edges` | summary.rs | Aggregates `BridgeEdgeHypothesis` list into `BridgeReportSummary` |
| `suggested_questions` | summary.rs | Generates investigation-question strings |
| `collect_report_rows` | queries.rs | Collects raw rows for the report pipeline |
[crates/gcode/src/graph/report/generation.rs:21-23]
[crates/gcode/src/graph/report/loading.rs:18-78]
[crates/gcode/src/graph/report/queries.rs:7-18]
[crates/gcode/src/graph/report/render.rs:8-18]
[crates/gcode/src/graph/report/rows.rs:11-19]

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

