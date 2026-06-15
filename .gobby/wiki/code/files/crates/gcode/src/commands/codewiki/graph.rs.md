---
title: crates/gcode/src/commands/codewiki/graph.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/graph.rs
  ranges:
  - 5-110
  - 114-143
  - 149-164
  - 166-181
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/graph.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

Fetches Codewiki graph edges for core symbols and assembles a `CodewikiGraph` from FalkorDB data, falling back to an unavailable graph when config, connection, or query execution fails. It first builds a core-symbol ID set and, if there are no core symbols, returns an empty available graph. It then queries call edges, filters rows to valid core symbol source/target pairs, tracks truncation when the result count reaches the limit, and separately derives import edges by mapping core file imports through file-to-symbol relationships. The file also contains the Cypher query builders and a small query wrapper that centralizes FalkorDB error handling and quiet-mode warning suppression.
[crates/gcode/src/commands/codewiki/graph.rs:5-110]
[crates/gcode/src/commands/codewiki/graph.rs:35-50]
[crates/gcode/src/commands/codewiki/graph.rs:114-143]
[crates/gcode/src/commands/codewiki/graph.rs:149-164]
[crates/gcode/src/commands/codewiki/graph.rs:166-181]

## API Symbols

- `fetch_codewiki_graph_edges` (function) component `fetch_codewiki_graph_edges [function]` (`44dfe8d0-2fa6-573e-9ce3-ec77e5bfd076`) lines 5-110 [crates/gcode/src/commands/codewiki/graph.rs:5-110]
  - Signature: `pub(crate) fn fetch_codewiki_graph_edges(`
  - Purpose: Fetches Codewiki graph call edges for core symbols from FalkorDB, returning an unavailable graph on missing config/connection/query failure, and marking the result truncated when the query returns 'edge_limit' rows. [crates/gcode/src/commands/codewiki/graph.rs:5-110]
- `query_or_unavailable` (function) component `query_or_unavailable [function]` (`f32e2489-a73a-5598-bcd0-f56db06d0742`) lines 35-50 [crates/gcode/src/commands/codewiki/graph.rs:35-50]
  - Signature: `fn query_or_unavailable(`
  - Purpose: Executes a GraphClient query with the provided parameters and returns 'Some(rows)' on success, or logs a FalkorDB warning unless 'ctx.quiet' is set and returns 'None' on failure. [crates/gcode/src/commands/codewiki/graph.rs:35-50]
- `import_edges_from_pairs` (function) component `import_edges_from_pairs [function]` (`ea534b97-87ed-523b-a237-0630b2735f70`) lines 114-143 [crates/gcode/src/commands/codewiki/graph.rs:114-143]
  - Signature: `pub(crate) fn import_edges_from_pairs(`
  - Purpose: Builds a list of import edges by filtering 'pairs' to imports originating from 'core_files', resolving each source and target file to their first component IDs via 'file_symbols', and emitting a 'CodewikiGraphEdge::import' for each valid source-target component pair. [crates/gcode/src/commands/codewiki/graph.rs:114-143]
- `codewiki_call_edges_query` (function) component `codewiki_call_edges_query [function]` (`9c90a7ea-835e-5fa5-a2f8-ee25e4dfbabf`) lines 149-164 [crates/gcode/src/commands/codewiki/graph.rs:149-164]
  - Signature: `pub(crate) fn codewiki_call_edges_query(`
  - Purpose: Builds and returns a Cypher query plus parameter map that selects 'CALLS' edges between 'CodeSymbol' nodes within the given 'project_id', returning 'source.id' and 'target.id' and capping results at 'edge_limit'. [crates/gcode/src/commands/codewiki/graph.rs:149-164]
- `codewiki_import_edges_query` (function) component `codewiki_import_edges_query [function]` (`664e6e45-ca66-5fb8-8554-b30b5f396afa`) lines 166-181 [crates/gcode/src/commands/codewiki/graph.rs:166-181]
  - Signature: `pub(crate) fn codewiki_import_edges_query(`
  - Purpose: Builds and returns a Cypher query string plus parameter map that selects 'CodeFile'-to-'CodeModule' 'IMPORTS' edges for a given project, returning 'source.path' and 'target.name' and applying the specified 'LIMIT'. [crates/gcode/src/commands/codewiki/graph.rs:166-181]

