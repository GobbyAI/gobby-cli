---
title: crates/gcode/src/commands/codewiki/graph.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/graph.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/graph.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

The primary entry point is `fetch_codewiki_graph_edges` crates/gcode/src/commands/codewiki/graph.rs:5-110, which orchestrates the retrieval of graph data for core files. If FalkorDB is unconfigured, or if connection or queries fail, it gracefully falls back to returning an unavailable graph state. It also ensures that the returned graph is conservatively marked as truncated if the number of returned records reaches the designated limit.

## How it fits
This file lives within the `codewiki` command module, acting as the data retrieval layer that interfaces directly with FalkorDB to pull structural relationships. It relies on FalkorDB configuration provided via the `Context` and is designed to handle query execution robustly.
[crates/gcode/src/commands/codewiki/graph.rs:5-110]
[crates/gcode/src/commands/codewiki/graph.rs:35-50]
[crates/gcode/src/commands/codewiki/graph.rs:114-143]
[crates/gcode/src/commands/codewiki/graph.rs:149-164]
[crates/gcode/src/commands/codewiki/graph.rs:166-181]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `fetch_codewiki_graph_edges` | function | Fetches Codewiki graph edges for core-file symbols from FalkorDB, returning an unavailable graph on missing config, connection/query failure, or no core symbols, and conservatively marking the result truncated when the edge query returns 'edge_limit' rows. [crates/gcode/src/commands/codewiki/graph.rs:5-110] |
| `query_or_unavailable` | function | Executes a FalkorDB query with the provided parameters and returns 'Some(rows)' on success, or logs a warning unless 'ctx.quiet' is set and returns 'None' if the query fails. [crates/gcode/src/commands/codewiki/graph.rs:35-50] |
| `import_edges_from_pairs` | function | Filters '(source_file, target_module)' import pairs to core source files, resolves each file to its first component ID via 'file_symbols', expands each target module to matching core files, and returns a 'Vec<CodewikiGraphEdge>' of import edges from source component to target component. [crates/gcode/src/commands/codewiki/graph.rs:114-143] |
| `codewiki_call_edges_query` | function | Builds and returns a Cypher query plus parameter map that selects intra-project 'CALLS' edges between 'CodeSymbol' nodes, returning source and target IDs and applying the provided 'edge_limit'. [crates/gcode/src/commands/codewiki/graph.rs:149-164] |
| `codewiki_import_edges_query` | function | Builds and returns a Cypher 'MATCH' query that selects 'CodeFile' nodes importing 'CodeModule' nodes within the given 'project_id', limits results to 'edge_limit', and supplies a parameter map containing the quoted 'project' value. [crates/gcode/src/commands/codewiki/graph.rs:166-181] |

