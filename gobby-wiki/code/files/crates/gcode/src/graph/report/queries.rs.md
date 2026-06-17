---
title: crates/gcode/src/graph/report/queries.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/queries.rs
  ranges:
  - 7-18
  - 20-22
  - 24-26
  - 28-38
  - 40-49
  - 51-85
  - 87-104
  - 106-126
  - 128-144
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/report/queries.rs:7-18](crates/gcode/src/graph/report/queries.rs#L7-L18), [crates/gcode/src/graph/report/queries.rs:20-22](crates/gcode/src/graph/report/queries.rs#L20-L22), [crates/gcode/src/graph/report/queries.rs:24-26](crates/gcode/src/graph/report/queries.rs#L24-L26), [crates/gcode/src/graph/report/queries.rs:28-38](crates/gcode/src/graph/report/queries.rs#L28-L38), [crates/gcode/src/graph/report/queries.rs:40-49](crates/gcode/src/graph/report/queries.rs#L40-L49), [crates/gcode/src/graph/report/queries.rs:51-85](crates/gcode/src/graph/report/queries.rs#L51-L85), [crates/gcode/src/graph/report/queries.rs:87-104](crates/gcode/src/graph/report/queries.rs#L87-L104), [crates/gcode/src/graph/report/queries.rs:106-126](crates/gcode/src/graph/report/queries.rs#L106-L126), [crates/gcode/src/graph/report/queries.rs:128-144](crates/gcode/src/graph/report/queries.rs#L128-L144)

</details>

# crates/gcode/src/graph/report/queries.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

Builds Cypher report queries for graph reporting, returning each query string alongside typed project parameters. The file factors out shared node-label expressions (`report_node_type_case`, node id/name coalescing helpers) and reuses them across query builders that count node and edge types, rank hotspots and incoming call hotspots, compute target frequencies, and identify bridge edges, all filtered by project and the code-edge relationship set.
[crates/gcode/src/graph/report/queries.rs:7-18]
[crates/gcode/src/graph/report/queries.rs:20-22]
[crates/gcode/src/graph/report/queries.rs:24-26]
[crates/gcode/src/graph/report/queries.rs:28-38]
[crates/gcode/src/graph/report/queries.rs:40-49]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `report_node_type_case` | function | `pub(super) fn report_node_type_case(alias: &str) -> String {` | `report_node_type_case [function]` | `e93dcb0f-4b3e-5880-95fc-e9d117c8904a` | 7-18 [crates/gcode/src/graph/report/queries.rs:7-18] | Indexed function `report_node_type_case` in `crates/gcode/src/graph/report/queries.rs`. [crates/gcode/src/graph/report/queries.rs:7-18] |
| `report_node_id_expr` | function | `fn report_node_id_expr(alias: &str) -> String {` | `report_node_id_expr [function]` | `64ebc387-e3a1-563b-b207-890b25ddd958` | 20-22 [crates/gcode/src/graph/report/queries.rs:20-22] | Indexed function `report_node_id_expr` in `crates/gcode/src/graph/report/queries.rs`. [crates/gcode/src/graph/report/queries.rs:20-22] |
| `report_node_name_expr` | function | `fn report_node_name_expr(alias: &str) -> String {` | `report_node_name_expr [function]` | `7f6fc2d7-84f2-5786-b53e-3454eb92974c` | 24-26 [crates/gcode/src/graph/report/queries.rs:24-26] | Indexed function `report_node_name_expr` in `crates/gcode/src/graph/report/queries.rs`. [crates/gcode/src/graph/report/queries.rs:24-26] |
| `report_node_counts_query` | function | `pub(super) fn report_node_counts_query(project_id: &str) -> (String, HashMap<String, String>) {` | `report_node_counts_query [function]` | `e938825f-a1b9-5945-b60c-33e9b9caf8f7` | 28-38 [crates/gcode/src/graph/report/queries.rs:28-38] | Indexed function `report_node_counts_query` in `crates/gcode/src/graph/report/queries.rs`. [crates/gcode/src/graph/report/queries.rs:28-38] |
| `report_code_edge_counts_query` | function | `pub(super) fn report_code_edge_counts_query(project_id: &str) -> (String, HashMap<String, String>) {` | `report_code_edge_counts_query [function]` | `456fe611-43e7-5035-be45-cd7e440f8147` | 40-49 [crates/gcode/src/graph/report/queries.rs:40-49] | Indexed function `report_code_edge_counts_query` in `crates/gcode/src/graph/report/queries.rs`. [crates/gcode/src/graph/report/queries.rs:40-49] |
| `report_hotspots_query` | function | `pub(super) fn report_hotspots_query(` | `report_hotspots_query [function]` | `bdb18233-a822-5fc0-bf1b-8920f03a76ac` | 51-85 [crates/gcode/src/graph/report/queries.rs:51-85] | Indexed function `report_hotspots_query` in `crates/gcode/src/graph/report/queries.rs`. [crates/gcode/src/graph/report/queries.rs:51-85] |
| `report_incoming_call_hotspots_query` | function | `pub(super) fn report_incoming_call_hotspots_query(` | `report_incoming_call_hotspots_query [function]` | `71d0e8a5-06c9-52d1-a7f9-756bc2937435` | 87-104 [crates/gcode/src/graph/report/queries.rs:87-104] | Indexed function `report_incoming_call_hotspots_query` in `crates/gcode/src/graph/report/queries.rs`. [crates/gcode/src/graph/report/queries.rs:87-104] |
| `report_target_frequencies_query` | function | `pub(super) fn report_target_frequencies_query(` | `report_target_frequencies_query [function]` | `d95e7a4b-e4a7-598b-9330-4d5f8e131e67` | 106-126 [crates/gcode/src/graph/report/queries.rs:106-126] | Indexed function `report_target_frequencies_query` in `crates/gcode/src/graph/report/queries.rs`. [crates/gcode/src/graph/report/queries.rs:106-126] |
| `report_bridge_edges_query` | function | `pub(super) fn report_bridge_edges_query(project_id: &str) -> (String, HashMap<String, String>) {` | `report_bridge_edges_query [function]` | `cd1c8b80-df45-5871-aec5-91174598d776` | 128-144 [crates/gcode/src/graph/report/queries.rs:128-144] | Indexed function `report_bridge_edges_query` in `crates/gcode/src/graph/report/queries.rs`. [crates/gcode/src/graph/report/queries.rs:128-144] |
