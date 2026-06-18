---
title: crates/gcode/src/graph/code_graph/write.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/write.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/write.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/graph/code_graph/write.rs` exposes 27 indexed API symbols.

## How it fits

`crates/gcode/src/graph/code_graph/write.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CodeGraph` | class | Indexed class `CodeGraph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:47-50] |
| `GraphOrphanCleanup` | class | Indexed class `GraphOrphanCleanup` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:53-56] |
| `new` | function | Indexed function `new` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:59-61] |
| `sync_file` | function | Indexed function `sync_file` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:63-101] |
| `ensure_project_indexes` | function | Indexed function `ensure_project_indexes` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:103-108] |
| `ensure_file_node` | function | Indexed function `ensure_file_node` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:110-120] |
| `add_imports` | function | Indexed function `add_imports` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:122-138] |
| `add_definitions` | function | Indexed function `add_definitions` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:140-159] |
| `add_calls` | function | Indexed function `add_calls` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:161-192] |
| `delete_stale_file_graph` | function | Indexed function `delete_stale_file_graph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:194-203] |
| `delete_file_graph` | function | Indexed function `delete_file_graph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:205-214] |
| `delete_file_node` | function | Indexed function `delete_file_node` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:216-221] |
| `delete_file_projection` | function | Indexed function `delete_file_projection` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:223-227] |
| `cleanup_orphans` | function | Indexed function `cleanup_orphans` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:229-234] |
| `cleanup_deleted_files` | function | Indexed function `cleanup_deleted_files` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:236-258] |
| `project_file_paths` | function | Indexed function `project_file_paths` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:260-271] |
| `count_file_projection_nodes` | function | Indexed function `count_file_projection_nodes` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:273-282] |
| `clear_project` | function | Indexed function `clear_project` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:284-286] |
| `value_to_usize` | function | Indexed function `value_to_usize` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:289-294] |
| `sync_file_graph` | function | Indexed function `sync_file_graph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:296-307] |
| `with_code_graph` | function | Indexed function `with_code_graph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:309-318] |
| `delete_file_graph` | function | Indexed function `delete_file_graph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:320-328] |
| `delete_file_projection` | function | Indexed function `delete_file_projection` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:330-334] |
| `cleanup_orphans` | function | Indexed function `cleanup_orphans` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:336-338] |
| `cleanup_deleted_files` | function | Indexed function `cleanup_deleted_files` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:340-345] |
| `clear_project` | function | Indexed function `clear_project` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:347-351] |
| `clear_all_code_index` | function | Indexed function `clear_all_code_index` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:353-376] |

