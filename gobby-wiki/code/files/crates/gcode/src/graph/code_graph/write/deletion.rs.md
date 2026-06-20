---
title: crates/gcode/src/graph/code_graph/write/deletion.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/write/deletion.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/write/deletion.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/graph/code_graph/write/deletion.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gcode/src/graph/code_graph/write/deletion.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `delete_file_graph_queries` | function | Builds a vector of Cypher 'TypedQuery's that delete a file’s 'IMPORTS' and 'DEFINES' relationships and outgoing 'CALLS' edges, then 'DETACH DELETE's all 'CodeSymbol' nodes for that file unless their IDs are listed in 'current_symbol_ids', in which case only non-listed symbols are deleted. [crates/gcode/src/graph/code_graph/write/deletion.rs:8-66] |
| `delete_stale_file_graph_queries` | function | Builds and returns four Cypher delete queries that remove stale 'IMPORTS', 'DEFINES', 'CALLS', and file-scoped 'CodeSymbol' records for a given project/file when their 'sync_token' is missing or differs from the supplied token. [crates/gcode/src/graph/code_graph/write/deletion.rs:68-113] |
| `delete_file_node_query` | function | Builds and returns a typed Cypher query that matches a 'CodeFile' node by 'project' and 'path' and deletes it with 'DETACH DELETE', parameterizing the provided project ID and file path. [crates/gcode/src/graph/code_graph/write/deletion.rs:115-127] |
| `project_file_path_queries` | function | Returns two parameterized Cypher 'TypedQuery's for the given 'project_id', one selecting distinct non-null 'CodeFile.path' values and the other selecting distinct non-null 'CodeSymbol.file_path' values as 'path'. [crates/gcode/src/graph/code_graph/write/deletion.rs:129-145] |
| `count_file_projection_nodes_query` | function | Builds a parameterized typed Cypher query that, for a given project ID and file path, counts matching 'CodeFile' and 'CodeSymbol' nodes in that project and returns the count as 'nodes'. [crates/gcode/src/graph/code_graph/write/deletion.rs:147-161] |
| `cleanup_orphans_queries` | function | Builds and returns a 'Vec<TypedQuery>' of orphan-cleanup Cypher queries for the given 'project_id', binding 'project' as a string parameter in each query. [crates/gcode/src/graph/code_graph/write/deletion.rs:163-171] |
| `cleanup_orphans_cypher_segments` | function | Returns three Cypher 'MATCH'/'DETACH DELETE' statements that remove project-scoped orphan graph nodes: unimported 'CodeModule's, uncalled 'UnresolvedCallee'/'ExternalSymbol' nodes, and 'CodeSymbol's with no file path or defining/calling relationships. [crates/gcode/src/graph/code_graph/write/deletion.rs:173-189] |
| `clear_project_query` | function | Builds a parameterized Cypher 'MATCH'/'DETACH DELETE' typed query that deletes all project-scoped nodes matching 'PROJECT_NODE_PREDICATE' for the given 'project_id'. [crates/gcode/src/graph/code_graph/write/deletion.rs:191-200] |
| `clear_all_code_index_query` | function | Builds and returns a 'TypedQuery' that deletes all project-matching nodes from the graph by issuing a Cypher 'MATCH' with 'WHERE {PROJECT_NODE_PREDICATE}' followed by 'DETACH DELETE n', using no parameters. [crates/gcode/src/graph/code_graph/write/deletion.rs:202-211] |

