---
title: crates/gcode/src/graph/code_graph/write/deletion.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/write/deletion.rs
  ranges:
  - 8-66
  - 68-113
  - 115-127
  - 129-145
  - 147-161
  - 163-171
  - 173-189
  - 191-200
  - 202-211
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/write/deletion.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/write|crates/gcode/src/graph/code_graph/write]]

## Purpose

Provides Cypher write queries for deleting and cleaning up graph data tied to a code file or project. It removes file-local `IMPORTS`, `DEFINES`, and `CALLS` edges, deletes stale or obsolete `CodeSymbol` nodes based on current IDs or sync tokens, can detach-delete a `CodeFile` node by path and project, enumerates project file paths and node counts, and offers broader orphan/project purge queries built from shared parameterized query helpers.
[crates/gcode/src/graph/code_graph/write/deletion.rs:8-66]
[crates/gcode/src/graph/code_graph/write/deletion.rs:68-113]
[crates/gcode/src/graph/code_graph/write/deletion.rs:115-127]
[crates/gcode/src/graph/code_graph/write/deletion.rs:129-145]
[crates/gcode/src/graph/code_graph/write/deletion.rs:147-161]

## API Symbols

- `delete_file_graph_queries` (function) component `delete_file_graph_queries [function]` (`6b7fce22-df5b-550f-b53a-72c5d45e6fe2`) lines 8-66 [crates/gcode/src/graph/code_graph/write/deletion.rs:8-66]
  - Signature: `pub(crate) fn delete_file_graph_queries(`
  - Purpose: Constructs and returns a sequence of Cypher 'TypedQuery's that remove a file’s 'IMPORTS', 'DEFINES', and symbol 'CALLS' relationships, then 'DETACH DELETE's all 'CodeSymbol' nodes for that file except any symbols whose IDs are listed in 'current_symbol_ids'. [crates/gcode/src/graph/code_graph/write/deletion.rs:8-66]
- `delete_stale_file_graph_queries` (function) component `delete_stale_file_graph_queries [function]` (`b4ecc305-d084-55c5-8058-c6f2b143a53d`) lines 68-113 [crates/gcode/src/graph/code_graph/write/deletion.rs:68-113]
  - Signature: `pub(crate) fn delete_stale_file_graph_queries(`
  - Purpose: Builds and returns a set of Cypher delete queries that remove stale 'IMPORTS', 'DEFINES', and 'CALLS' relationships, plus detach-delete stale 'CodeSymbol' nodes for the given project/file when their 'sync_token' is missing or differs from the supplied token. [crates/gcode/src/graph/code_graph/write/deletion.rs:68-113]
- `delete_file_node_query` (function) component `delete_file_node_query [function]` (`c790d893-e066-5cef-810c-ef7a64d0f12a`) lines 115-127 [crates/gcode/src/graph/code_graph/write/deletion.rs:115-127]
  - Signature: `pub(crate) fn delete_file_node_query(`
  - Purpose: Builds a parameterized Cypher 'TypedQuery' that matches a 'CodeFile' node by 'path' and 'project' and returns a 'DETACH DELETE' query to remove that file node and all its relationships. [crates/gcode/src/graph/code_graph/write/deletion.rs:115-127]
- `project_file_path_queries` (function) component `project_file_path_queries [function]` (`bcb69555-7e78-5eeb-bea9-35eff3655ee2`) lines 129-145 [crates/gcode/src/graph/code_graph/write/deletion.rs:129-145]
  - Signature: `pub(crate) fn project_file_path_queries(project_id: &str) -> anyhow::Result<Vec<TypedQuery>> {`
  - Purpose: Returns two Cypher 'TypedQuery's parameterized by 'project_id' that each select distinct non-null file paths for that project, one from 'CodeFile.path' and one from 'CodeSymbol.file_path'. [crates/gcode/src/graph/code_graph/write/deletion.rs:129-145]
- `count_file_projection_nodes_query` (function) component `count_file_projection_nodes_query [function]` (`133ee9df-3449-58f5-ba59-70c7dfc942fb`) lines 147-161 [crates/gcode/src/graph/code_graph/write/deletion.rs:147-161]
  - Signature: `pub(crate) fn count_file_projection_nodes_query(`
  - Purpose: Builds a 'TypedQuery' that counts graph nodes for a given project whose file identity matches 'file_path' either as a 'CodeFile' with 'path = $file_path' or as a 'CodeSymbol' with 'file_path = $file_path', returning the count as 'nodes'. [crates/gcode/src/graph/code_graph/write/deletion.rs:147-161]
- `cleanup_orphans_queries` (function) component `cleanup_orphans_queries [function]` (`b3e61529-6088-569f-8f2a-410a2406e5e5`) lines 163-171 [crates/gcode/src/graph/code_graph/write/deletion.rs:163-171]
  - Signature: `pub(crate) fn cleanup_orphans_queries(project_id: &str) -> anyhow::Result<Vec<TypedQuery>> {`
  - Purpose: Builds and returns a 'Vec<TypedQuery>' by wrapping each Cypher statement from 'cleanup_orphans_cypher_segments()' with a 'project' string parameter derived from 'project_id'. [crates/gcode/src/graph/code_graph/write/deletion.rs:163-171]
- `cleanup_orphans_cypher_segments` (function) component `cleanup_orphans_cypher_segments [function]` (`c562163b-a042-58a0-81c8-23d07ac78c60`) lines 173-189 [crates/gcode/src/graph/code_graph/write/deletion.rs:173-189]
  - Signature: `fn cleanup_orphans_cypher_segments() -> [&'static str; 3] {`
  - Purpose: Returns three Cypher 'DETACH DELETE' statements that, scoped by '$project', remove orphaned 'CodeModule' nodes not imported by any 'CodeFile', orphaned 'UnresolvedCallee'/'ExternalSymbol' nodes not called by the project, and 'CodeSymbol' nodes with no 'file_path' that are neither defined by a 'CodeFile' nor connected by 'CALLS' relationships in either direction. [crates/gcode/src/graph/code_graph/write/deletion.rs:173-189]
- `clear_project_query` (function) component `clear_project_query [function]` (`5b08f08d-5c67-5c69-82e8-c701ee409a6d`) lines 191-200 [crates/gcode/src/graph/code_graph/write/deletion.rs:191-200]
  - Signature: `pub(crate) fn clear_project_query(project_id: &str) -> anyhow::Result<TypedQuery> {`
  - Purpose: Constructs a parameterized Cypher 'MATCH'/'DETACH DELETE' 'TypedQuery' that deletes all project-scoped nodes satisfying 'PROJECT_NODE_PREDICATE' for the given 'project_id'. [crates/gcode/src/graph/code_graph/write/deletion.rs:191-200]
- `clear_all_code_index_query` (function) component `clear_all_code_index_query [function]` (`f7b8b82a-1170-5017-a16b-e26c31f4381f`) lines 202-211 [crates/gcode/src/graph/code_graph/write/deletion.rs:202-211]
  - Signature: `pub(crate) fn clear_all_code_index_query() -> anyhow::Result<TypedQuery> {`
  - Purpose: Builds and returns a 'TypedQuery' that matches all project nodes and detaches and deletes them, using an empty parameter list. [crates/gcode/src/graph/code_graph/write/deletion.rs:202-211]

