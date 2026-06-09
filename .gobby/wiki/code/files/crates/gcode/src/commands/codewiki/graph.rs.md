---
title: crates/gcode/src/commands/codewiki/graph.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/graph.rs
  ranges:
  - 4-124
  - 34-49
  - 126-145
  - 147-165
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/graph.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/graph.rs` exposes 4 indexed API symbols. [crates/gcode/src/commands/codewiki/graph.rs:4-124] [crates/gcode/src/commands/codewiki/graph.rs:34-49] [crates/gcode/src/commands/codewiki/graph.rs:126-145] [crates/gcode/src/commands/codewiki/graph.rs:147-165]

## API Symbols

- `fetch_codewiki_graph_edges` (function) component `fetch_codewiki_graph_edges [function]` (`1653d1e5-3ac6-5f4e-96de-bb46fd727b1f`) lines 4-124 [crates/gcode/src/commands/codewiki/graph.rs:4-124]
  - Signature: `pub(crate) fn fetch_codewiki_graph_edges(`
  - Purpose: # Summary

Fetches a limited set of call graph edges from FalkorDB for core file symbols and returns a CodewikiGraph with availability status and connection error handling. [crates/gcode/src/commands/codewiki/graph.rs:4-124]
- `query_or_unavailable` (function) component `query_or_unavailable [function]` (`c2474b4a-3816-5e4d-9f13-a1a296986eb3`) lines 34-49 [crates/gcode/src/commands/codewiki/graph.rs:34-49]
  - Signature: `fn query_or_unavailable(`
  - Purpose: Executes a FalkorDB query with parameters via GraphClient and returns `Some(Vec<Row>)` on success or `None` on failure, optionally logging the error to stderr based on the context's `quiet` flag. [crates/gcode/src/commands/codewiki/graph.rs:34-49]
- `codewiki_call_edges_query` (function) component `codewiki_call_edges_query [function]` (`23e63664-9d01-514e-b8a5-f351bc339c96`) lines 126-145 [crates/gcode/src/commands/codewiki/graph.rs:126-145]
  - Signature: `pub(crate) fn codewiki_call_edges_query(`
  - Purpose: Constructs a parameterized Cypher query to retrieve function call edges (CALLS relationships) between specified code symbols within a project, limited to a maximum number of results. [crates/gcode/src/commands/codewiki/graph.rs:126-145]
- `codewiki_import_edges_query` (function) component `codewiki_import_edges_query [function]` (`f7c4038e-ef0e-55b5-a450-91cfd5a57cf2`) lines 147-165 [crates/gcode/src/commands/codewiki/graph.rs:147-165]
  - Signature: `pub(crate) fn codewiki_import_edges_query(`
  - Purpose: Generates a parameterized Neo4j Cypher query to retrieve IMPORTS edges from specified source files to target modules within a project, limited by edge count. [crates/gcode/src/commands/codewiki/graph.rs:147-165]

