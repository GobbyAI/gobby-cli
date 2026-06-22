---
title: crates/gcode/src/graph/code_graph/read/payload_queries.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/payload_queries.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/read/payload_queries.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Overview

`crates/gcode/src/graph/code_graph/read/payload_queries.rs` exposes 10 indexed API symbols.

## How it fits

`crates/gcode/src/graph/code_graph/read/payload_queries.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `project_overview_files_query` | function | Builds a parameterized Cypher query that selects 'CodeFile' nodes for a given project, counts distinct defined symbols and imported modules per file, and returns file path metadata plus symbol counts sorted by import count, symbol count, and path, limited by a clamped 'limit'. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29] |
| `project_overview_imports_query` | function | Builds a Cypher query and parameter map that returns 'IMPORTS' edges from specified source file paths within a project, with the result count capped by 'clamp_limit(limit)'. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:31-47] |
| `project_overview_defines_query` | function | Builds a parameterized Cypher query and string-parameter map that returns 'DEFINES' edges from 'CodeFile' nodes in the given 'project' whose paths are in 'file_paths', projecting symbol metadata and enforcing a clamped 'LIMIT'. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:49-68] |
| `project_overview_calls_query` | function | Builds a parameterized Cypher query and string-parameter map that returns up to 'limit' call edges from symbols defined in the specified 'file_paths' within a project, including source/target IDs, target metadata, call line, and link metadata. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:70-90] |
| `file_symbols_query` | function | Builds a Cypher query and string parameter map to fetch symbols defined by a given code file in a project, returning each symbol’s id, name, kind/type, file path, line start, signature, and link metadata. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:92-106] |
| `file_calls_query` | function | Builds and returns a parameterized Cypher query plus string parameters that select 'CALLS' relationships involving the specified file in a project, returning source/target symbol metadata, line number, and link metadata. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:108-130] |
| `symbol_neighbors_query` | function | Builds a Cypher query and string parameter map that, for a given project and symbol ID, returns up to 'limit' 'CALLS'-connected neighboring symbols with their identity, type/kind, location, signature, edge direction, line, and link metadata, after clamping the requested limit. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:132-153] |
| `blast_radius_center_query` | function | Constructs and returns a Cypher query plus string parameters that, for a given project and symbol ID, retrieves at most one matching node of type 'CodeSymbol', 'UnresolvedCallee', or 'ExternalSymbol', projecting its id, name, computed node type, kind, and file path. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:155-169] |
| `blast_radius_file_call_query` | function | Builds a parameterized Cypher query that, for a given project file, finds all symbols that call any symbol defined in that file within a bounded call-depth ('1..=5'), annotates them with shortest call distance and optional defining file path, orders by proximity then name, and returns the query plus 'project'/'path' string parameters. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:171-195] |
| `blast_radius_file_import_query` | function | Builds a Cypher query and string parameter map that, for a given project/file, clamps 'depth' to 1..5 and 'limit' via 'clamp_limit', then finds distinct importer files reachable through up to 'depth' import hops from the file’s imported module, ordered by shortest import distance and limited to 'limit' results. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:197-219] |

