---
title: crates/gcode/src/commands/codewiki/graph.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/graph.rs
  ranges:
  - 4-109
  - 113-142
  - 148-163
  - 165-180
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/graph.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This file manages code dependency graph operations by querying FalkorDB and transforming results into graph edge representations. The primary function fetch_codewiki_graph_edges orchestrates the process: it filters symbols from core files, establishes a FalkorDB connection, executes parametric Cypher queries to retrieve both call and import edges, and returns a CodewikiGraph structure. Helper function query_or_unavailable handles query execution with error handling and optional logging. The query generator functions codewiki_call_edges_query and codewiki_import_edges_query create parameterized Cypher strings that retrieve CALLS relationships between CodeSymbols and IMPORTS relationships between CodeFile and CodeModule nodes respectively, bounded by the specified project and edge limit. The import_edges_from_pairs function transforms raw file-module import pairs into typed CodewikiGraphEdge instances by resolving files to their component IDs and filtering for imports originating from core files.
[crates/gcode/src/commands/codewiki/graph.rs:4-109]
[crates/gcode/src/commands/codewiki/graph.rs:34-49]
[crates/gcode/src/commands/codewiki/graph.rs:113-142]
[crates/gcode/src/commands/codewiki/graph.rs:148-163]
[crates/gcode/src/commands/codewiki/graph.rs:165-180]

## API Symbols

- `fetch_codewiki_graph_edges` (function) component `fetch_codewiki_graph_edges [function]` (`1653d1e5-3ac6-5f4e-96de-bb46fd727b1f`) lines 4-109 [crates/gcode/src/commands/codewiki/graph.rs:4-109]
  - Signature: `pub(crate) fn fetch_codewiki_graph_edges(`
  - Purpose: Fetches code dependency graph edges from FalkorDB for symbols in core files, up to a specified limit, returning either an available `CodewikiGraph` with the queried edges or an unavailable graph on connection/query failure. [crates/gcode/src/commands/codewiki/graph.rs:4-109]
- `query_or_unavailable` (function) component `query_or_unavailable [function]` (`c2474b4a-3816-5e4d-9f13-a1a296986eb3`) lines 34-49 [crates/gcode/src/commands/codewiki/graph.rs:34-49]
  - Signature: `fn query_or_unavailable(`
  - Purpose: Executes a FalkorDB graph query via GraphClient, returning `Some(rows)` on success or `None` on failure with optional error logging to stderr. [crates/gcode/src/commands/codewiki/graph.rs:34-49]
- `import_edges_from_pairs` (function) component `import_edges_from_pairs [function]` (`4e862278-2391-5e0a-8b76-f04cf8df3287`) lines 113-142 [crates/gcode/src/commands/codewiki/graph.rs:113-142]
  - Signature: `pub(crate) fn import_edges_from_pairs(`
  - Purpose: Transforms file-module import pairs into `CodewikiGraphEdge` instances by resolving files to their first component IDs and filtering for imports originating from designated core files. [crates/gcode/src/commands/codewiki/graph.rs:113-142]
- `codewiki_call_edges_query` (function) component `codewiki_call_edges_query [function]` (`4912a584-cc76-5735-80de-0cb286e853c4`) lines 148-163 [crates/gcode/src/commands/codewiki/graph.rs:148-163]
  - Signature: `pub(crate) fn codewiki_call_edges_query(`
  - Purpose: Generates a Cypher query string with parameters to fetch call graph edges (CALLS relationships) between CodeSymbols within a specified project, bounded by the given edge limit. [crates/gcode/src/commands/codewiki/graph.rs:148-163]
- `codewiki_import_edges_query` (function) component `codewiki_import_edges_query [function]` (`d515c347-b86d-5297-9803-cc692b841646`) lines 165-180 [crates/gcode/src/commands/codewiki/graph.rs:165-180]
  - Signature: `pub(crate) fn codewiki_import_edges_query(`
  - Purpose: Generates a parameterized Cypher query that retrieves import edges (IMPORTS relationships) between CodeFile and CodeModule nodes for a specified project, with a configurable result limit. [crates/gcode/src/commands/codewiki/graph.rs:165-180]

