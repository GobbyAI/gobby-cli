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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/write/deletion.rs:8-66](crates/gcode/src/graph/code_graph/write/deletion.rs#L8-L66), [crates/gcode/src/graph/code_graph/write/deletion.rs:68-113](crates/gcode/src/graph/code_graph/write/deletion.rs#L68-L113), [crates/gcode/src/graph/code_graph/write/deletion.rs:115-127](crates/gcode/src/graph/code_graph/write/deletion.rs#L115-L127), [crates/gcode/src/graph/code_graph/write/deletion.rs:129-145](crates/gcode/src/graph/code_graph/write/deletion.rs#L129-L145), [crates/gcode/src/graph/code_graph/write/deletion.rs:147-161](crates/gcode/src/graph/code_graph/write/deletion.rs#L147-L161), [crates/gcode/src/graph/code_graph/write/deletion.rs:163-171](crates/gcode/src/graph/code_graph/write/deletion.rs#L163-L171), [crates/gcode/src/graph/code_graph/write/deletion.rs:173-189](crates/gcode/src/graph/code_graph/write/deletion.rs#L173-L189), [crates/gcode/src/graph/code_graph/write/deletion.rs:191-200](crates/gcode/src/graph/code_graph/write/deletion.rs#L191-L200), [crates/gcode/src/graph/code_graph/write/deletion.rs:202-211](crates/gcode/src/graph/code_graph/write/deletion.rs#L202-L211)

</details>

# crates/gcode/src/graph/code_graph/write/deletion.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Builds typed Cypher delete/cleanup queries for maintaining the code graph when a file or project changes. The helpers generate query batches to remove file relationships, delete stale or missing symbol nodes, clean orphaned graph nodes and segments, and clear either one project’s index data or the entire code index.
[crates/gcode/src/graph/code_graph/write/deletion.rs:8-66]
[crates/gcode/src/graph/code_graph/write/deletion.rs:68-113]
[crates/gcode/src/graph/code_graph/write/deletion.rs:115-127]
[crates/gcode/src/graph/code_graph/write/deletion.rs:129-145]
[crates/gcode/src/graph/code_graph/write/deletion.rs:147-161]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `delete_file_graph_queries` | function | `pub(crate) fn delete_file_graph_queries(` | `delete_file_graph_queries [function]` | `6b7fce22-df5b-550f-b53a-72c5d45e6fe2` | 8-66 [crates/gcode/src/graph/code_graph/write/deletion.rs:8-66] | Indexed function `delete_file_graph_queries` in `crates/gcode/src/graph/code_graph/write/deletion.rs`. [crates/gcode/src/graph/code_graph/write/deletion.rs:8-66] |
| `delete_stale_file_graph_queries` | function | `pub(crate) fn delete_stale_file_graph_queries(` | `delete_stale_file_graph_queries [function]` | `b4ecc305-d084-55c5-8058-c6f2b143a53d` | 68-113 [crates/gcode/src/graph/code_graph/write/deletion.rs:68-113] | Indexed function `delete_stale_file_graph_queries` in `crates/gcode/src/graph/code_graph/write/deletion.rs`. [crates/gcode/src/graph/code_graph/write/deletion.rs:68-113] |
| `delete_file_node_query` | function | `pub(crate) fn delete_file_node_query(` | `delete_file_node_query [function]` | `c790d893-e066-5cef-810c-ef7a64d0f12a` | 115-127 [crates/gcode/src/graph/code_graph/write/deletion.rs:115-127] | Indexed function `delete_file_node_query` in `crates/gcode/src/graph/code_graph/write/deletion.rs`. [crates/gcode/src/graph/code_graph/write/deletion.rs:115-127] |
| `project_file_path_queries` | function | `pub(crate) fn project_file_path_queries(project_id: &str) -> anyhow::Result<Vec<TypedQuery>> {` | `project_file_path_queries [function]` | `bcb69555-7e78-5eeb-bea9-35eff3655ee2` | 129-145 [crates/gcode/src/graph/code_graph/write/deletion.rs:129-145] | Indexed function `project_file_path_queries` in `crates/gcode/src/graph/code_graph/write/deletion.rs`. [crates/gcode/src/graph/code_graph/write/deletion.rs:129-145] |
| `count_file_projection_nodes_query` | function | `pub(crate) fn count_file_projection_nodes_query(` | `count_file_projection_nodes_query [function]` | `133ee9df-3449-58f5-ba59-70c7dfc942fb` | 147-161 [crates/gcode/src/graph/code_graph/write/deletion.rs:147-161] | Indexed function `count_file_projection_nodes_query` in `crates/gcode/src/graph/code_graph/write/deletion.rs`. [crates/gcode/src/graph/code_graph/write/deletion.rs:147-161] |
| `cleanup_orphans_queries` | function | `pub(crate) fn cleanup_orphans_queries(project_id: &str) -> anyhow::Result<Vec<TypedQuery>> {` | `cleanup_orphans_queries [function]` | `b3e61529-6088-569f-8f2a-410a2406e5e5` | 163-171 [crates/gcode/src/graph/code_graph/write/deletion.rs:163-171] | Indexed function `cleanup_orphans_queries` in `crates/gcode/src/graph/code_graph/write/deletion.rs`. [crates/gcode/src/graph/code_graph/write/deletion.rs:163-171] |
| `cleanup_orphans_cypher_segments` | function | `fn cleanup_orphans_cypher_segments() -> [&'static str; 3] {` | `cleanup_orphans_cypher_segments [function]` | `c562163b-a042-58a0-81c8-23d07ac78c60` | 173-189 [crates/gcode/src/graph/code_graph/write/deletion.rs:173-189] | Indexed function `cleanup_orphans_cypher_segments` in `crates/gcode/src/graph/code_graph/write/deletion.rs`. [crates/gcode/src/graph/code_graph/write/deletion.rs:173-189] |
| `clear_project_query` | function | `pub(crate) fn clear_project_query(project_id: &str) -> anyhow::Result<TypedQuery> {` | `clear_project_query [function]` | `5b08f08d-5c67-5c69-82e8-c701ee409a6d` | 191-200 [crates/gcode/src/graph/code_graph/write/deletion.rs:191-200] | Indexed function `clear_project_query` in `crates/gcode/src/graph/code_graph/write/deletion.rs`. [crates/gcode/src/graph/code_graph/write/deletion.rs:191-200] |
| `clear_all_code_index_query` | function | `pub(crate) fn clear_all_code_index_query() -> anyhow::Result<TypedQuery> {` | `clear_all_code_index_query [function]` | `f7b8b82a-1170-5017-a16b-e26c31f4381f` | 202-211 [crates/gcode/src/graph/code_graph/write/deletion.rs:202-211] | Indexed function `clear_all_code_index_query` in `crates/gcode/src/graph/code_graph/write/deletion.rs`. [crates/gcode/src/graph/code_graph/write/deletion.rs:202-211] |
