---
title: crates/gcode/src/graph/code_graph/read/payload_queries.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/payload_queries.rs
  ranges:
  - 10-29
  - 31-47
  - 49-68
  - 70-90
  - 92-106
  - 108-130
  - 132-153
  - 155-169
  - 171-195
  - 197-219
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/read/payload_queries.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Purpose

Builds Cypher read queries for the code graph and returns each query with its string parameter map. The functions cover project overview, file-centric symbol/call listing, symbol neighborhood lookup, and blast-radius traversals, and they all share the same helpers for clamping result limits, formatting typed ID lists, and injecting common link/type metadata so the query shapes stay consistent.
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29]
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:31-47]
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:49-68]
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:70-90]
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:92-106]

## API Symbols

- `project_overview_files_query` (function) component `project_overview_files_query [function]` (`6d014b62-6981-513f-b630-77e05091f813`) lines 10-29 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29]
  - Signature: `pub(super) fn project_overview_files_query(`
  - Purpose: Builds a Cypher query and string parameter map that list 'CodeFile' nodes for a given project, compute each file’s distinct defined-symbol count and import count, and return file metadata sorted by descending import count, symbol count, then path, limited by a clamped 'limit'. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29]
- `project_overview_imports_query` (function) component `project_overview_imports_query [function]` (`01a3ccf5-d2d1-5ce6-92bc-687095e11869`) lines 31-47 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:31-47]
  - Signature: `pub(super) fn project_overview_imports_query(`
  - Purpose: Builds a Cypher query and parameter map that return 'IMPORTS' relationships from 'CodeFile' nodes in the given project whose paths match the provided list, limited by a clamped 'limit', with the project bound as a string parameter. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:31-47]
- `project_overview_defines_query` (function) component `project_overview_defines_query [function]` (`a4367271-426d-590f-824a-9556d7c192fa`) lines 49-68 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:49-68]
  - Signature: `pub(super) fn project_overview_defines_query(`
  - Purpose: Builds a Cypher query and string parameter map that selects 'DEFINES' relationships between 'CodeFile' and 'CodeSymbol' nodes for a given project, filtered to the provided file paths and capped by a clamped limit. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:49-68]
- `project_overview_calls_query` (function) component `project_overview_calls_query [function]` (`8b0c237a-fa1b-5ee8-9f21-555cc8d45e29`) lines 70-90 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:70-90]
  - Signature: `pub(super) fn project_overview_calls_query(`
  - Purpose: Builds a parameterized Cypher query and string-parameter map that returns 'CALLS' relationships from symbols defined in the specified file paths for a given project, with the result count capped by 'clamp_limit(limit)'. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:70-90]
- `file_symbols_query` (function) component `file_symbols_query [function]` (`87eb1231-cd2e-5a60-9d83-4356b3705e94`) lines 92-106 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:92-106]
  - Signature: `pub(super) fn file_symbols_query(`
  - Purpose: Constructs and returns a Cypher query plus string parameters to fetch all 'CodeSymbol' nodes defined by a given 'CodeFile' in a specified project, returning symbol metadata such as id, name, kind/type, file path, line start, signature, and link metadata. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:92-106]
- `file_calls_query` (function) component `file_calls_query [function]` (`93cf4493-2000-50a1-becc-4b8c376941d3`) lines 108-130 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:108-130]
  - Signature: `pub(in crate::graph::code_graph) fn file_calls_query(`
  - Purpose: Builds and parameterizes a Cypher query that returns all 'CALLS' relationships involving symbols in the specified file within a project, including source/target symbol metadata, edge line number, and link metadata. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:108-130]
- `symbol_neighbors_query` (function) component `symbol_neighbors_query [function]` (`8a178b30-5b98-5d1f-9c0f-cac8cbeb7df0`) lines 132-153 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:132-153]
  - Signature: `pub(super) fn symbol_neighbors_query(`
  - Purpose: Builds a parameterized Cypher query that, after clamping 'limit', finds CALLS neighbors of a given symbol node within a project and returns each neighbor’s identity, type, kind, location, signature, edge direction, line, and link metadata. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:132-153]
- `blast_radius_center_query` (function) component `blast_radius_center_query [function]` (`bb1959b0-6d27-550f-86b0-1cc6f1059b6a`) lines 155-169 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:155-169]
  - Signature: `pub(super) fn blast_radius_center_query(`
  - Purpose: Builds and returns a parameterized Cypher query with 'project' and 'id' bindings that looks up a single 'CodeSymbol', 'UnresolvedCallee', or 'ExternalSymbol' node by project-scoped ID and returns its 'id', 'name', computed type, 'kind', and 'file_path'. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:155-169]
- `blast_radius_file_call_query` (function) component `blast_radius_file_call_query [function]` (`30c5026a-d8e4-5662-b7e2-8b88703b58e1`) lines 171-195 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:171-195]
  - Signature: `pub(super) fn blast_radius_file_call_query(`
  - Purpose: Builds a Neo4j Cypher query and parameter map that, for a given project and file path, finds symbols that call any symbol defined in that file within a clamped call-depth range of 1..=5, computes each caller’s minimum distance, enriches results with defining file and location metadata, orders by shortest distance then name, and limits the result set with a clamped limit. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:171-195]
- `blast_radius_file_import_query` (function) component `blast_radius_file_import_query [function]` (`523340bd-a63d-5155-9cd2-fd5554f1c20c`) lines 197-219 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:197-219]
  - Signature: `pub(in crate::graph::code_graph) fn blast_radius_file_import_query(`
  - Purpose: Builds a Cypher query and parameter map that, for a given project and file path, returns distinct importing 'CodeFile' nodes within a clamped 1-5 hop import blast radius, ordered by minimum import distance and limited by a clamped result count. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:197-219]

