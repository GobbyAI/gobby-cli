---
title: crates/gcode/src/graph/code_graph/read/graph_payloads.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/graph_payloads.rs
  ranges:
  - 19-98
  - 100-126
  - 128-164
  - 166-239
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/read/graph_payloads.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Purpose

Builds graph payloads for different code-graph views using the optional core graph and helper query/add-row utilities. `project_overview_graph` gathers project file nodes, then adds import and definition links plus related module and symbol nodes until node/link limits are hit; `file_graph` starts from one file, adds its defined symbols and call relations; `symbol_neighbors` centers on a symbol and attaches nearby symbols with directed call edges and metadata; `blast_radius_graph` builds a bounded neighborhood around a symbol or file path, choosing or synthesizing the center node and marking its blast distance.
[crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98]
[crates/gcode/src/graph/code_graph/read/graph_payloads.rs:100-126]
[crates/gcode/src/graph/code_graph/read/graph_payloads.rs:128-164]
[crates/gcode/src/graph/code_graph/read/graph_payloads.rs:166-239]

## API Symbols

- `project_overview_graph` (function) component `project_overview_graph [function]` (`39d3125a-94cc-53e8-8317-11ad473c5029`) lines 19-98 [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98]
  - Signature: `pub fn project_overview_graph(ctx: &Context, limit: usize) -> anyhow::Result<GraphPayload> {`
  - Purpose: Builds a bounded project overview 'GraphPayload' by querying file nodes for the project, then augmenting them with import and definition links plus corresponding module/symbol nodes until node and link limits are reached. [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98]
- `file_graph` (function) component `file_graph [function]` (`21810cf0-1169-5f2b-af49-61f0e0af250e`) lines 100-126 [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:100-126]
  - Signature: `pub fn file_graph(ctx: &Context, file_path: &str) -> anyhow::Result<GraphPayload> {`
  - Purpose: Builds and returns a 'GraphPayload' for 'file_path' by adding a file node, querying the project’s symbols defined in that file and linking them with 'DEFINES' edges, then querying file call relations and adding prefixed source/target nodes and corresponding links. [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:100-126]
- `symbol_neighbors` (function) component `symbol_neighbors [function]` (`2611c2e5-47f5-5547-a6ad-7bb227d987e3`) lines 128-164 [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:128-164]
  - Signature: `pub fn symbol_neighbors(`
  - Purpose: Queries the optional core graph for a symbol’s center node and up to 'limit' neighboring symbols, then builds a 'GraphPayload' containing the center, unresolved neighbor nodes, and directed 'CALLS' links with line and projection metadata. [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:128-164]
- `blast_radius_graph` (function) component `blast_radius_graph [function]` (`4525912e-48ac-59e3-8a09-bb5064171c7d`) lines 166-239 [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:166-239]
  - Signature: `pub fn blast_radius_graph(`
  - Purpose: Builds and returns a 'GraphPayload' for the blast-radius neighborhood around either a symbol ID or file path by querying the core graph for nodes and edges within the specified 'depth' and 'limit', selecting or synthesizing the center node, and marking it at 'blast_distance = 0'. [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:166-239]

