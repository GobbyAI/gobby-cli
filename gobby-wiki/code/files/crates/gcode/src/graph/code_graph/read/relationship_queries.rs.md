---
title: crates/gcode/src/graph/code_graph/read/relationship_queries.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/relationship_queries.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/read/relationship_queries.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Overview

`crates/gcode/src/graph/code_graph/read/relationship_queries.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gcode/src/graph/code_graph/read/relationship_queries.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `count_callers_query` | function | Indexed function `count_callers_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:9-21] |
| `count_usages_query` | function | Indexed function `count_usages_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:23-38] |
| `find_callers_query` | function | Indexed function `find_callers_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:40-62] |
| `find_usages_query` | function | Indexed function `find_usages_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:64-84] |
| `find_caller_ids_query` | function | Indexed function `find_caller_ids_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:86-102] |
| `find_usage_ids_query` | function | Indexed function `find_usage_ids_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:104-120] |
| `find_callers_batch_query` | function | Indexed function `find_callers_batch_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:122-143] |
| `find_caller_ids_batch_query` | function | Indexed function `find_caller_ids_batch_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:145-162] |
| `find_callees_batch_query` | function | Indexed function `find_callees_batch_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:164-185] |
| `find_callee_ids_batch_query` | function | Indexed function `find_callee_ids_batch_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:187-204] |
| `symbol_callee_edges_query` | function | Indexed function `symbol_callee_edges_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:206-220] |
| `symbol_path_steps_query` | function | Indexed function `symbol_path_steps_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:222-238] |
| `get_imports_query` | function | Indexed function `get_imports_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:240-250] |
| `resolve_external_call_target_query` | function | Indexed function `resolve_external_call_target_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:252-278] |
| `blast_radius_query` | function | Indexed function `blast_radius_query` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:280-297] |
| `callers_query_projects_confidence_without_edge_metadata_duplication` | function | Indexed function `callers_query_projects_confidence_without_edge_metadata_duplication` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:304-310] |
| `usages_query_projects_edge_confidence_and_metadata` | function | Indexed function `usages_query_projects_edge_confidence_and_metadata` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:313-318] |
| `batched_relationship_queries_project_confidence_label` | function | Indexed function `batched_relationship_queries_project_confidence_label` in `crates/gcode/src/graph/code_graph/read/relationship_queries.rs`. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:321-329] |

