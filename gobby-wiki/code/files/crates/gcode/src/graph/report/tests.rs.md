---
title: crates/gcode/src/graph/report/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/tests.rs
  ranges:
  - 15-65
  - 68-84
  - 87-127
  - 129-179
  - 181-196
  - 199-225
  - 228-249
  - 252-277
  - 280-317
  - 320-342
  - 345-390
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/report/tests.rs:15-65](crates/gcode/src/graph/report/tests.rs#L15-L65), [crates/gcode/src/graph/report/tests.rs:68-84](crates/gcode/src/graph/report/tests.rs#L68-L84), [crates/gcode/src/graph/report/tests.rs:87-127](crates/gcode/src/graph/report/tests.rs#L87-L127), [crates/gcode/src/graph/report/tests.rs:129-179](crates/gcode/src/graph/report/tests.rs#L129-L179), [crates/gcode/src/graph/report/tests.rs:181-196](crates/gcode/src/graph/report/tests.rs#L181-L196), [crates/gcode/src/graph/report/tests.rs:199-225](crates/gcode/src/graph/report/tests.rs#L199-L225), [crates/gcode/src/graph/report/tests.rs:228-249](crates/gcode/src/graph/report/tests.rs#L228-L249), [crates/gcode/src/graph/report/tests.rs:252-277](crates/gcode/src/graph/report/tests.rs#L252-L277), [crates/gcode/src/graph/report/tests.rs:280-317](crates/gcode/src/graph/report/tests.rs#L280-L317), [crates/gcode/src/graph/report/tests.rs:320-342](crates/gcode/src/graph/report/tests.rs#L320-L342), [crates/gcode/src/graph/report/tests.rs:345-390](crates/gcode/src/graph/report/tests.rs#L345-L390)

</details>

# crates/gcode/src/graph/report/tests.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

This file contains integration-style tests for graph report generation, hotspot summarization, bridge-edge handling, and markdown rendering. It builds synthetic `ReportGraphSnapshot` fixtures, runs `generate_report_from_snapshot`, `summarize_hotspots`, `summarize_bridge_edges`, and `render_markdown`, then asserts the report shape and pinned output stay stable. The helper functions `expected_graph_hotspots` and `expected_bridge_summary` define the expected summaries, while the other tests verify centrality-based hotspot ordering, read-only bridge edges, CommonMark inline code formatting, degradation behavior, and aggregation of shared-symbol bridge hypotheses across source systems.
[crates/gcode/src/graph/report/tests.rs:15-65]
[crates/gcode/src/graph/report/tests.rs:68-84]
[crates/gcode/src/graph/report/tests.rs:87-127]
[crates/gcode/src/graph/report/tests.rs:129-179]
[crates/gcode/src/graph/report/tests.rs:181-196]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `report_shape` | function | `fn report_shape() {` | `report_shape [function]` | `9142cd68-b487-5f7a-a910-fbd4b71d3cc1` | 15-65 [crates/gcode/src/graph/report/tests.rs:15-65] | Indexed function `report_shape` in `crates/gcode/src/graph/report/tests.rs`. [crates/gcode/src/graph/report/tests.rs:15-65] |
| `graph_report_hotspots_use_shared_centrality_degree` | function | `fn graph_report_hotspots_use_shared_centrality_degree() {` | `graph_report_hotspots_use_shared_centrality_degree [function]` | `4c344a58-b80f-5dba-88e1-4e6a793a4d4a` | 68-84 [crates/gcode/src/graph/report/tests.rs:68-84] | Indexed function `graph_report_hotspots_use_shared_centrality_degree` in `crates/gcode/src/graph/report/tests.rs`. [crates/gcode/src/graph/report/tests.rs:68-84] |
| `graph_report_hotspots_and_bridge_summary_match_pinned_output` | function | `fn graph_report_hotspots_and_bridge_summary_match_pinned_output() {` | `graph_report_hotspots_and_bridge_summary_match_pinned_output [function]` | `e5131274-82e9-5402-a913-b768b70681ed` | 87-127 [crates/gcode/src/graph/report/tests.rs:87-127] | Indexed function `graph_report_hotspots_and_bridge_summary_match_pinned_output` in `crates/gcode/src/graph/report/tests.rs`. [crates/gcode/src/graph/report/tests.rs:87-127] |
| `expected_graph_hotspots` | function | `fn expected_graph_hotspots() -> GraphReportHotspots {` | `expected_graph_hotspots [function]` | `42a312ac-939c-5aed-bd1e-bfbb76a10060` | 129-179 [crates/gcode/src/graph/report/tests.rs:129-179] | Indexed function `expected_graph_hotspots` in `crates/gcode/src/graph/report/tests.rs`. [crates/gcode/src/graph/report/tests.rs:129-179] |
| `expected_bridge_summary` | function | `fn expected_bridge_summary() -> BridgeReportSummary {` | `expected_bridge_summary [function]` | `77a058fd-c4f1-54f6-bd2f-6552561eace5` | 181-196 [crates/gcode/src/graph/report/tests.rs:181-196] | Indexed function `expected_bridge_summary` in `crates/gcode/src/graph/report/tests.rs`. [crates/gcode/src/graph/report/tests.rs:181-196] |
| `bridge_edges_are_read_only` | function | `fn bridge_edges_are_read_only() {` | `bridge_edges_are_read_only [function]` | `4e209230-a203-5a38-932a-469515c165a2` | 199-225 [crates/gcode/src/graph/report/tests.rs:199-225] | Indexed function `bridge_edges_are_read_only` in `crates/gcode/src/graph/report/tests.rs`. [crates/gcode/src/graph/report/tests.rs:199-225] |
| `markdown_inline_code_uses_commonmark_backtick_delimiters` | function | `fn markdown_inline_code_uses_commonmark_backtick_delimiters() {` | `markdown_inline_code_uses_commonmark_backtick_delimiters [function]` | `80742743-b1b9-5969-991d-b08533e34b25` | 228-249 [crates/gcode/src/graph/report/tests.rs:228-249] | Indexed function `markdown_inline_code_uses_commonmark_backtick_delimiters` in `crates/gcode/src/graph/report/tests.rs`. [crates/gcode/src/graph/report/tests.rs:228-249] |
| `markdown_renders_high_degree_modules` | function | `fn markdown_renders_high_degree_modules() {` | `markdown_renders_high_degree_modules [function]` | `67d84179-c1ea-54af-9db4-dedfb36d6a33` | 252-277 [crates/gcode/src/graph/report/tests.rs:252-277] | Indexed function `markdown_renders_high_degree_modules` in `crates/gcode/src/graph/report/tests.rs`. [crates/gcode/src/graph/report/tests.rs:252-277] |
| `report_degradation_contract` | function | `fn report_degradation_contract() {` | `report_degradation_contract [function]` | `598b9a05-6d4b-59b0-add1-86c233395c2b` | 280-317 [crates/gcode/src/graph/report/tests.rs:280-317] | Indexed function `report_degradation_contract` in `crates/gcode/src/graph/report/tests.rs`. [crates/gcode/src/graph/report/tests.rs:280-317] |
| `bridge_edges_are_hypotheses` | function | `fn bridge_edges_are_hypotheses() {` | `bridge_edges_are_hypotheses [function]` | `41f4c5f5-0451-5521-aee1-10c5edcef7bd` | 320-342 [crates/gcode/src/graph/report/tests.rs:320-342] | Indexed function `bridge_edges_are_hypotheses` in `crates/gcode/src/graph/report/tests.rs`. [crates/gcode/src/graph/report/tests.rs:320-342] |
| `bridge_summary_aggregates_shared_symbol_hypotheses_across_source_systems` | function | `fn bridge_summary_aggregates_shared_symbol_hypotheses_across_source_systems() {` | `bridge_summary_aggregates_shared_symbol_hypotheses_across_source_systems [function]` | `aaf1e11c-c8dd-5091-b6b8-fbb2364b8daf` | 345-390 [crates/gcode/src/graph/report/tests.rs:345-390] | Indexed function `bridge_summary_aggregates_shared_symbol_hypotheses_across_source_systems` in `crates/gcode/src/graph/report/tests.rs`. [crates/gcode/src/graph/report/tests.rs:345-390] |
