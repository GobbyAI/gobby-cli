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

# crates/gcode/src/graph/report/queries.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

`crates/gcode/src/graph/report/queries.rs` exposes 9 indexed API symbols.
[crates/gcode/src/graph/report/queries.rs:7-18]
[crates/gcode/src/graph/report/queries.rs:20-22]
[crates/gcode/src/graph/report/queries.rs:24-26]
[crates/gcode/src/graph/report/queries.rs:28-38]
[crates/gcode/src/graph/report/queries.rs:40-49]
[crates/gcode/src/graph/report/queries.rs:51-85]
[crates/gcode/src/graph/report/queries.rs:87-104]
[crates/gcode/src/graph/report/queries.rs:106-126]
[crates/gcode/src/graph/report/queries.rs:128-144]

## API Symbols

- `report_node_type_case` (function) component `report_node_type_case [function]` (`e93dcb0f-4b3e-5880-95fc-e9d117c8904a`) lines 7-18 [crates/gcode/src/graph/report/queries.rs:7-18]
  - Signature: `pub(super) fn report_node_type_case(alias: &str) -> String {`
  - Purpose: Returns a formatted Cypher CASE expression string that maps code node type labels (CodeFile, CodeModule, CodeSymbol, UnresolvedCallee, ExternalSymbol) to their corresponding string type identifiers for query reporting. [crates/gcode/src/graph/report/queries.rs:7-18]
- `report_node_id_expr` (function) component `report_node_id_expr [function]` (`64ebc387-e3a1-563b-b207-890b25ddd958`) lines 20-22 [crates/gcode/src/graph/report/queries.rs:20-22]
  - Signature: `fn report_node_id_expr(alias: &str) -> String {`
  - Purpose: This function generates a SQL `COALESCE` expression that returns the first non-null value from the `id`, `path`, or `name` columns of a given table alias. [crates/gcode/src/graph/report/queries.rs:20-22]
- `report_node_name_expr` (function) component `report_node_name_expr [function]` (`7f6fc2d7-84f2-5786-b53e-3454eb92974c`) lines 24-26 [crates/gcode/src/graph/report/queries.rs:24-26]
  - Signature: `fn report_node_name_expr(alias: &str) -> String {`
  - Purpose: Generates a SQL COALESCE expression string that returns the first non-null value among a node's name, path, or id column references. [crates/gcode/src/graph/report/queries.rs:24-26]
- `report_node_counts_query` (function) component `report_node_counts_query [function]` (`e938825f-a1b9-5945-b60c-33e9b9caf8f7`) lines 28-38 [crates/gcode/src/graph/report/queries.rs:28-38]
  - Signature: `pub(super) fn report_node_counts_query(project_id: &str) -> (String, HashMap<String, String>) {`
  - Purpose: This function constructs a Neo4j Cypher query string and typed parameter map that counts nodes of specific code-related types (CodeFile, CodeSymbol, CodeModule, UnresolvedCallee, ExternalSymbol) grouped by node type for a given project. [crates/gcode/src/graph/report/queries.rs:28-38]
- `report_code_edge_counts_query` (function) component `report_code_edge_counts_query [function]` (`456fe611-43e7-5035-be45-cd7e440f8147`) lines 40-49 [crates/gcode/src/graph/report/queries.rs:40-49]
  - Signature: `pub(super) fn report_code_edge_counts_query(project_id: &str) -> (String, HashMap<String, String>) {`
  - Purpose: Returns a Cypher query and parameter map that groups and counts code-edge relationships by type for a specified Neo4j project. [crates/gcode/src/graph/report/queries.rs:40-49]
- `report_hotspots_query` (function) component `report_hotspots_query [function]` (`bdb18233-a822-5fc0-bf1b-8920f03a76ac`) lines 51-85 [crates/gcode/src/graph/report/queries.rs:51-85]
  - Signature: `pub(super) fn report_hotspots_query(`
  - Purpose: Generates a parameterized Cypher query that ranks code nodes of a specified class by total edge degree (incoming plus outgoing connections) and returns the top N hotspots for a given project. [crates/gcode/src/graph/report/queries.rs:51-85]
- `report_incoming_call_hotspots_query` (function) component `report_incoming_call_hotspots_query [function]` (`71d0e8a5-06c9-52d1-a7f9-756bc2937435`) lines 87-104 [crates/gcode/src/graph/report/queries.rs:87-104]
  - Signature: `pub(super) fn report_incoming_call_hotspots_query(`
  - Purpose: Returns a Cypher query string and parameter map that retrieves the top N code symbols ranked by incoming call in-degree for a specified project. [crates/gcode/src/graph/report/queries.rs:87-104]
- `report_target_frequencies_query` (function) component `report_target_frequencies_query [function]` (`d95e7a4b-e4a7-598b-9330-4d5f8e131e67`) lines 106-126 [crates/gcode/src/graph/report/queries.rs:106-126]
  - Signature: `pub(super) fn report_target_frequencies_query(`
  - Purpose: Constructs a parameterized Cypher query to retrieve and rank the top N most frequently called external symbols or unresolved callees for a specified project. [crates/gcode/src/graph/report/queries.rs:106-126]
- `report_bridge_edges_query` (function) component `report_bridge_edges_query [function]` (`cd1c8b80-df45-5871-aec5-91174598d776`) lines 128-144 [crates/gcode/src/graph/report/queries.rs:128-144]
  - Signature: `pub(super) fn report_bridge_edges_query(project_id: &str) -> (String, HashMap<String, String>) {`
  - Purpose: Constructs a parameterized Cypher query that retrieves all RELATES_TO_CODE bridge edges terminating at CodeSymbols within a specified project, including source identification and provenance metadata. [crates/gcode/src/graph/report/queries.rs:128-144]

