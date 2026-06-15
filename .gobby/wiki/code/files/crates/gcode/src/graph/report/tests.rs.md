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

# crates/gcode/src/graph/report/tests.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

Test suite for the graph reporting pipeline. It builds synthetic `ReportGraphSnapshot` fixtures and checks that report generation, hotspot summarization, bridge-edge aggregation, and markdown rendering all produce the expected serialized output and pinned summaries, including error/degradation behavior when the graph service is unavailable.
[crates/gcode/src/graph/report/tests.rs:15-65]
[crates/gcode/src/graph/report/tests.rs:68-84]
[crates/gcode/src/graph/report/tests.rs:87-127]
[crates/gcode/src/graph/report/tests.rs:129-179]
[crates/gcode/src/graph/report/tests.rs:181-196]

## API Symbols

- `report_shape` (function) component `report_shape [function]` (`9142cd68-b487-5f7a-a910-fbd4b71d3cc1`) lines 15-65 [crates/gcode/src/graph/report/tests.rs:15-65]
  - Signature: `fn report_shape() {`
  - Purpose: Constructs a synthetic 'ReportGraphSnapshot', generates a report for 'project-1' at a fixed timestamp, serializes it to JSON, and verifies the expected summary counts, hotspot ordering, unresolved/external targets, and bridge-summary relation. [crates/gcode/src/graph/report/tests.rs:15-65]
- `graph_report_hotspots_use_shared_centrality_degree` (function) component `graph_report_hotspots_use_shared_centrality_degree [function]` (`4c344a58-b80f-5dba-88e1-4e6a793a4d4a`) lines 68-84 [crates/gcode/src/graph/report/tests.rs:68-84]
  - Signature: `fn graph_report_hotspots_use_shared_centrality_degree() {`
  - Purpose: Verifies that 'summarize_hotspots' uses shared centrality degree for both files and symbols so duplicate 'DEFINES' edges increase incoming/outgoing counts while the unique degree remains '1'. [crates/gcode/src/graph/report/tests.rs:68-84]
- `graph_report_hotspots_and_bridge_summary_match_pinned_output` (function) component `graph_report_hotspots_and_bridge_summary_match_pinned_output [function]` (`e5131274-82e9-5402-a913-b768b70681ed`) lines 87-127 [crates/gcode/src/graph/report/tests.rs:87-127]
  - Signature: `fn graph_report_hotspots_and_bridge_summary_match_pinned_output() {`
  - Purpose: Constructs a 'ReportGraphSnapshot' with file, module, function, unresolved, and external nodes plus code and inferred bridge edges, then asserts that 'summarize_hotspots' and 'summarize_bridge_edges' produce the pinned expected hotspot and bridge summary outputs. [crates/gcode/src/graph/report/tests.rs:87-127]
- `expected_graph_hotspots` (function) component `expected_graph_hotspots [function]` (`42a312ac-939c-5aed-bd1e-bfbb76a10060`) lines 129-179 [crates/gcode/src/graph/report/tests.rs:129-179]
  - Signature: `fn expected_graph_hotspots() -> GraphReportHotspots {`
  - Purpose: Returns a 'GraphReportHotspots' test fixture populated with one high-degree file ('src/lib.rs'), two high-degree symbols ('handler' and 'parse' in 'src/lib.rs'), one high-degree module ('api'), and one incoming-call hotspot for 'parse'. [crates/gcode/src/graph/report/tests.rs:129-179]
- `expected_bridge_summary` (function) component `expected_bridge_summary [function]` (`77a058fd-c4f1-54f6-bd2f-6552561eace5`) lines 181-196 [crates/gcode/src/graph/report/tests.rs:181-196]
  - Signature: `fn expected_bridge_summary() -> BridgeReportSummary {`
  - Purpose: Returns a 'BridgeReportSummary' indicating an inferred, read-only 'RELATES_TO_CODE' bridge with one edge, a single 'gobby-memory' source count, and a confidence range fixed at '0.72..=0.72'. [crates/gcode/src/graph/report/tests.rs:181-196]
- `bridge_edges_are_read_only` (function) component `bridge_edges_are_read_only [function]` (`4e209230-a203-5a38-932a-469515c165a2`) lines 199-225 [crates/gcode/src/graph/report/tests.rs:199-225]
  - Signature: `fn bridge_edges_are_read_only() {`
  - Purpose: Verifies that a 'BridgeEdgeHypothesis' created from gcode-extracted metadata is marked 'read_only', labeled as an inferred hypothesis with 'Extracted' provenance, and remains serialized as read-only in the generated report. [crates/gcode/src/graph/report/tests.rs:199-225]
- `markdown_inline_code_uses_commonmark_backtick_delimiters` (function) component `markdown_inline_code_uses_commonmark_backtick_delimiters [function]` (`80742743-b1b9-5969-991d-b08533e34b25`) lines 228-249 [crates/gcode/src/graph/report/tests.rs:228-249]
  - Signature: `fn markdown_inline_code_uses_commonmark_backtick_delimiters() {`
  - Purpose: Asserts that 'render_markdown' emits inline code for project and target names using CommonMark backtick delimiters, preserving embedded apostrophes without backslash escaping. [crates/gcode/src/graph/report/tests.rs:228-249]
- `markdown_renders_high_degree_modules` (function) component `markdown_renders_high_degree_modules [function]` (`67d84179-c1ea-54af-9db4-dedfb36d6a33`) lines 252-277 [crates/gcode/src/graph/report/tests.rs:252-277]
  - Signature: `fn markdown_renders_high_degree_modules() {`
  - Purpose: Verifies that 'render_markdown' includes a '## High-degree modules' section and formats a module hotspot as '- 'api' (degree 4, in 1, out 3)' when the report contains a high-degree module. [crates/gcode/src/graph/report/tests.rs:252-277]
- `report_degradation_contract` (function) component `report_degradation_contract [function]` (`598b9a05-6d4b-59b0-add1-86c233395c2b`) lines 280-317 [crates/gcode/src/graph/report/tests.rs:280-317]
  - Signature: `fn report_degradation_contract() {`
  - Purpose: Verifies that 'generate_report' fails with 'ProjectGraphReportError::GraphServiceNotConfigured' when the graph service is unavailable, and that 'generate_report_from_snapshot' records a non-required 'RELATES_TO_CODE' degradation with escaped markdown while still producing a node-counted report. [crates/gcode/src/graph/report/tests.rs:280-317]
- `bridge_edges_are_hypotheses` (function) component `bridge_edges_are_hypotheses [function]` (`41f4c5f5-0451-5521-aee1-10c5edcef7bd`) lines 320-342 [crates/gcode/src/graph/report/tests.rs:320-342]
  - Signature: `fn bridge_edges_are_hypotheses() {`
  - Purpose: Verifies that an inferred 'BridgeEdgeHypothesis' is marked as a hypothesis with 'Inferred' provenance and serializes to JSON with the expected label and provenance fields. [crates/gcode/src/graph/report/tests.rs:320-342]
- `bridge_summary_aggregates_shared_symbol_hypotheses_across_source_systems` (function) component `bridge_summary_aggregates_shared_symbol_hypotheses_across_source_systems [function]` (`aaf1e11c-c8dd-5091-b6b8-fbb2364b8daf`) lines 345-390 [crates/gcode/src/graph/report/tests.rs:345-390]
  - Signature: `fn bridge_summary_aggregates_shared_symbol_hypotheses_across_source_systems() {`
  - Purpose: Verifies that 'summarize_bridge_edges' aggregates two inferred 'RELATES_TO_CODE' bridge hypotheses targeting the same symbol from different source systems into a single 'BridgeReportSummary' with edge count 2, per-source counts, 'read_only = true', and a confidence range spanning 0.6 to 0.9. [crates/gcode/src/graph/report/tests.rs:345-390]

