---
title: crates/gcode/src/graph/code_graph/read/relationship_queries.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/relationship_queries.rs
  ranges:
  - 9-21
  - 23-38
  - 40-62
  - 64-84
  - 86-102
  - 104-120
  - 122-143
  - 145-162
  - 164-185
  - 187-204
  - 206-220
  - 222-238
  - 240-250
  - 252-278
  - 280-297
  - 304-310
  - 313-318
  - 321-329
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:9-21](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L9-L21), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:23-38](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L23-L38), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:40-62](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L40-L62), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:64-84](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L64-L84), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:86-102](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L86-L102), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:104-120](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L104-L120), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:122-143](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L122-L143), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:145-162](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L145-L162), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:164-185](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L164-L185), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:187-204](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L187-L204), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:206-220](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L206-L220), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:222-238](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L222-L238), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:240-250](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L240-L250), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:252-278](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L252-L278), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:280-297](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L280-L297), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:304-310](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L304-L310), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:313-318](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L313-L318), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:321-329](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L321-L329)

</details>

# crates/gcode/src/graph/code_graph/read/relationship_queries.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Purpose

Builds Cypher read queries for code-graph relationship lookups within a project. The functions cover counts and paginated retrieval of callers/usages, batch caller/callee expansion, symbol edge/path traversal, import lookup, external-call target resolution, and blast-radius analysis, while sharing common helpers for typed parameters, limit/offset clamping, call-target filtering, and confidence-label metadata aggregation.
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:9-21]
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:23-38]
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:40-62]
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:64-84]
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:86-102]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `count_callers_query` | function | `pub(crate) fn count_callers_query(` | `count_callers_query [function]` | `c37d3deb-918f-587f-97ea-f5cb4f3d851c` | 9-21 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:9-21] | Indexed function `count_callers_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:9-21] |
| `count_usages_query` | function | `pub(crate) fn count_usages_query(` | `count_usages_query [function]` | `072c5082-3f7a-585d-9ff4-da40fd69190c` | 23-38 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:23-38] | Indexed function `count_usages_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:23-38] |
| `find_callers_query` | function | `pub(crate) fn find_callers_query(` | `find_callers_query [function]` | `d03ede71-eb00-53e9-8caa-c07800478e9c` | 40-62 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:40-62] | Indexed function `find_callers_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:40-62] |
| `find_usages_query` | function | `pub(crate) fn find_usages_query(` | `find_usages_query [function]` | `09dc987b-7ca1-54df-9bd2-0665c05e64d7` | 64-84 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:64-84] | Indexed function `find_usages_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:64-84] |
| `find_caller_ids_query` | function | `pub(super) fn find_caller_ids_query(` | `find_caller_ids_query [function]` | `cd9d7794-8fc0-5874-b432-0508018909b3` | 86-102 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:86-102] | Indexed function `find_caller_ids_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:86-102] |
| `find_usage_ids_query` | function | `pub(super) fn find_usage_ids_query(` | `find_usage_ids_query [function]` | `4dec84f3-f12b-56e3-b621-808d448a4901` | 104-120 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:104-120] | Indexed function `find_usage_ids_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:104-120] |
| `find_callers_batch_query` | function | `pub(crate) fn find_callers_batch_query(` | `find_callers_batch_query [function]` | `1af288d8-23f1-5892-a97d-1b8bc93831c6` | 122-143 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:122-143] | Indexed function `find_callers_batch_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:122-143] |
| `find_caller_ids_batch_query` | function | `pub(super) fn find_caller_ids_batch_query(` | `find_caller_ids_batch_query [function]` | `f30fd3f4-f9e5-54e2-8c9d-48d5ca6664b8` | 145-162 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:145-162] | Indexed function `find_caller_ids_batch_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:145-162] |
| `find_callees_batch_query` | function | `pub(crate) fn find_callees_batch_query(` | `find_callees_batch_query [function]` | `e34952dc-345f-586a-b1e7-ef579d83c7c0` | 164-185 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:164-185] | Indexed function `find_callees_batch_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:164-185] |
| `find_callee_ids_batch_query` | function | `pub(super) fn find_callee_ids_batch_query(` | `find_callee_ids_batch_query [function]` | `669706c2-64bc-5dca-b3c3-1393fc93fe08` | 187-204 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:187-204] | Indexed function `find_callee_ids_batch_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:187-204] |
| `symbol_callee_edges_query` | function | `pub(crate) fn symbol_callee_edges_query(` | `symbol_callee_edges_query [function]` | `6f1902fa-a531-57ed-9df4-d78ece2a4051` | 206-220 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:206-220] | Indexed function `symbol_callee_edges_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:206-220] |
| `symbol_path_steps_query` | function | `pub(crate) fn symbol_path_steps_query(` | `symbol_path_steps_query [function]` | `486293fa-6bc1-5340-9e77-f8720dce1fd1` | 222-238 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:222-238] | Indexed function `symbol_path_steps_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:222-238] |
| `get_imports_query` | function | `pub(crate) fn get_imports_query(` | `get_imports_query [function]` | `0136e1b4-09ce-5809-9961-af7ce76274e9` | 240-250 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:240-250] | Indexed function `get_imports_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:240-250] |
| `resolve_external_call_target_query` | function | `pub(crate) fn resolve_external_call_target_query(` | `resolve_external_call_target_query [function]` | `9e86f53f-3315-5bf2-93f5-88dcd64937fc` | 252-278 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:252-278] | Indexed function `resolve_external_call_target_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:252-278] |
| `blast_radius_query` | function | `pub(crate) fn blast_radius_query(depth: usize, limit: usize) -> String {` | `blast_radius_query [function]` | `87106fe7-d1fd-54e5-9218-860a6086b2e0` | 280-297 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:280-297] | Indexed function `blast_radius_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:280-297] |
| `callers_query_projects_confidence_without_edge_metadata_duplication` | function | `fn callers_query_projects_confidence_without_edge_metadata_duplication() {` | `callers_query_projects_confidence_without_edge_metadata_duplication [function]` | `b8fbeeaf-b411-5bd7-9e3f-a1e98bd3e6df` | 304-310 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:304-310] | Indexed function `callers_query_projects_confidence_without_edge_metadata_duplication` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:304-310] |
| `usages_query_projects_edge_confidence_and_metadata` | function | `fn usages_query_projects_edge_confidence_and_metadata() {` | `usages_query_projects_edge_confidence_and_metadata [function]` | `6f1896dc-5090-5829-a73f-0a237be7c452` | 313-318 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:313-318] | Indexed function `usages_query_projects_edge_confidence_and_metadata` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:313-318] |
| `batched_relationship_queries_project_confidence_label` | function | `fn batched_relationship_queries_project_confidence_label() {` | `batched_relationship_queries_project_confidence_label [function]` | `fb558f5c-b3ef-5525-9eb0-b1bebc844d35` | 321-329 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:321-329] | Indexed function `batched_relationship_queries_project_confidence_label` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:321-329] |
