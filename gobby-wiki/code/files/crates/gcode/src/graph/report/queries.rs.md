---
title: crates/gcode/src/graph/report/queries.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/queries.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/report/queries.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Overview

`crates/gcode/src/graph/report/queries.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gcode/src/graph/report/queries.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `report_node_type_case` | function | Constructs and returns a Cypher 'CASE' expression string that maps a node alias’s labels to a report type ('file', 'module', 'symbol' or its 'kind', 'unresolved', 'external', or default 'node'). [crates/gcode/src/graph/report/queries.rs:7-18] |
| `report_node_id_expr` | function | Returns a SQL 'coalesce' expression string that selects the first non-null value from '{alias}.id', '{alias}.path', and '{alias}.name'. [crates/gcode/src/graph/report/queries.rs:20-22] |
| `report_node_name_expr` | function | Returns a SQL 'coalesce' expression that resolves a node name by preferring '{alias}.name', then '{alias}.path', and finally '{alias}.id'. [crates/gcode/src/graph/report/queries.rs:24-26] |
| `report_node_counts_query` | function | Builds and returns a parameterized Cypher query that counts nodes in the given project whose labels are 'CodeFile', 'CodeSymbol', 'CodeModule', 'UnresolvedCallee', or 'ExternalSymbol', using 'report_node_type_case("n")' for the returned name and 'typed_query::string_params' to bind 'project_id' as '$project'. [crates/gcode/src/graph/report/queries.rs:28-38] |
| `report_code_edge_counts_query` | function | Builds a Cypher query that counts project-scoped relationships whose types are in 'CODE_EDGE_REL_TYPES', returning each relationship type as 'name' and its count, along with a string-parameter map binding 'project' to 'project_id'. [crates/gcode/src/graph/report/queries.rs:40-49] |
| `report_hotspots_query` | function | Builds a Cypher query and project parameter map to report the top 'top_n' hotspots for a given 'node_class' by counting incoming and outgoing code-edge relationships, filtering to nodes with positive degree, and returning them sorted by descending degree then name/id. [crates/gcode/src/graph/report/queries.rs:51-85] |
| `report_incoming_call_hotspots_query` | function | Builds a parameterized Cypher query and string-parameter map that, for a given project, ranks 'CodeSymbol' nodes by incoming 'CALLS' edge count, returning the top 'max(top_n, 1)' call hotspots ordered by degree descending then name/id ascending. [crates/gcode/src/graph/report/queries.rs:87-104] |
| `report_target_frequencies_query` | function | Builds a Cypher query and string parameter map to report the top 'top_n' called targets for a given project, selecting either 'ExternalSymbol' or 'UnresolvedCallee' by 'target_type', counting incoming 'CALLS' relationships, ordering by descending call count then name and id, and enforcing a minimum limit of 1. [crates/gcode/src/graph/report/queries.rs:106-126] |
| `report_bridge_edges_query` | function | Constructs a Cypher query and parameter map that fetches 'RELATES_TO_CODE' edges into 'CodeSymbol' nodes for a given project, returning source/target identifiers and edge metadata such as provenance, confidence, source system, file path, line, source symbol ID, and matching method. [crates/gcode/src/graph/report/queries.rs:128-144] |

