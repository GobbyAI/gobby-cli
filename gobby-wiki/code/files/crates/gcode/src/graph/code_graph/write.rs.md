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

`crates/gcode/src/graph/code_graph/write.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CodeGraph` | class | 'CodeGraph<'a>' is a borrowed wrapper over a project identifier and a mutable 'GraphClient', tying graph operations to a specific project via 'project_id: &'a str' and 'client: &'a mut GraphClient'. [crates/gcode/src/graph/code_graph/write.rs:47-50] |
| `GraphOrphanCleanup` | class | 'GraphOrphanCleanup' is a struct that records cleanup results for a graph, tracking the number of stale files deleted and graph nodes deleted. [crates/gcode/src/graph/code_graph/write.rs:53-56] |
| `new` | function | Constructs a new instance by storing the provided 'project_id' string slice and mutable 'GraphClient' reference in 'Self'. [crates/gcode/src/graph/code_graph/write.rs:59-61] |
| `sync_file` | function | Synchronizes a file’s import, definition, and call graph records into the database in bounded write batches, deletes stale rows using a per-file sync token, optionally cleans up orphaned graph data, and returns the total number of relationships processed. [crates/gcode/src/graph/code_graph/write.rs:63-101] |
| `ensure_project_indexes` | function | Ensures that each label in 'PROJECT_INDEXED_LABELS' has an exact node index on the 'project' field by invoking 'self.client.ensure_exact_node_index' for each label and returning any error encountered. [crates/gcode/src/graph/code_graph/write.rs:103-108] |
| `ensure_file_node` | function | Executes a write query to ensure a file node exists for the given project, file path, symbol count, and sync token, returning 'anyhow::Result<()>'. [crates/gcode/src/graph/code_graph/write.rs:110-120] |
| `add_imports` | function | Builds import-graph items for a file, returns 'Ok(0)' if none exist, otherwise executes the 'add_imports_query' write against 'self.client' with the project ID and sync token, and returns the number of imported items written. [crates/gcode/src/graph/code_graph/write.rs:122-138] |
| `add_definitions` | function | Filters the input 'definitions' to symbols with non-empty 'id' and 'name', returns 'Ok(0)' if none remain, otherwise writes them via 'add_definitions_query' and returns the number of symbols written. [crates/gcode/src/graph/code_graph/write.rs:140-159] |
| `add_calls` | function | Partitions the provided 'CallRelation' slice into symbol, external, and unresolved call groups for the current project and file, writes each non-empty group via its corresponding query with the given 'sync_token', and returns the total number of call records written. [crates/gcode/src/graph/code_graph/write.rs:161-192] |
| `delete_stale_file_graph` | function | Executes all write queries returned by 'delete_stale_file_graph_queries' for the given 'project_id', 'file_path', and 'sync_token' to remove stale file-graph state, then returns 'Ok(())' if every query succeeds. [crates/gcode/src/graph/code_graph/write.rs:194-203] |
| `delete_file_graph` | function | Deletes the graph records associated with 'file_path' for the given 'current_symbol_ids' by generating the relevant write queries, executing each against 'self.client', and returning any resulting error. [crates/gcode/src/graph/code_graph/write.rs:205-214] |
| `delete_file_node` | function | Deletes the file-node record for the given 'file_path' by executing a generated write query against 'self.client' using 'self.project_id', and returns any resulting error. [crates/gcode/src/graph/code_graph/write.rs:216-221] |
| `delete_file_projection` | function | Deletes the file’s graph and node state for 'file_path', then performs orphan cleanup, returning any error encountered. [crates/gcode/src/graph/code_graph/write.rs:223-227] |
| `cleanup_orphans` | function | Iterates over the cleanup-orphan queries for the current project and executes each as a write query on the client, returning any encountered error. [crates/gcode/src/graph/code_graph/write.rs:229-234] |
| `cleanup_deleted_files` | function | Removes from the graph every project file path absent from 'indexed_file_paths', counts and deletes each stale file’s projection nodes and file node, runs orphan cleanup, and returns a 'GraphOrphanCleanup' summarizing deleted stale files and graph nodes. [crates/gcode/src/graph/code_graph/write.rs:236-258] |
| `project_file_paths` | function | Executes all Cypher queries returned by 'project_file_path_queries(self.project_id)', collects each row’s string 'path' field into a deduplicated 'BTreeSet<String>', and returns it as 'anyhow::Result'. [crates/gcode/src/graph/code_graph/write.rs:260-271] |
| `count_file_projection_nodes` | function | Builds and executes a typed graph query for the given 'file_path' and returns the first row’s '"nodes"' value as a 'usize', defaulting to '0' if missing or unparseable. [crates/gcode/src/graph/code_graph/write.rs:273-282] |
| `clear_project` | function | Executes the write query produced by 'clear_project_query(self.project_id)?' using 'self.client', returning the resulting 'anyhow::Result<()>'. [crates/gcode/src/graph/code_graph/write.rs:284-286] |
| `value_to_usize` | function | Converts a 'serde_json::Value' to 'Option<usize>' by first accepting an unsigned 64-bit integer and 'try_from'-casting it to 'usize', otherwise accepting a signed 64-bit integer only if it fits losslessly into 'usize'. [crates/gcode/src/graph/code_graph/write.rs:289-294] |
| `sync_file_graph` | function | Acquires the code graph from 'ctx' and delegates to 'graph.sync_file' to synchronize the given file’s imports, definitions, and call relations, optionally cleaning orphaned nodes, returning the resulting 'usize' through 'anyhow::Result'. [crates/gcode/src/graph/code_graph/write.rs:296-307] |
| `with_code_graph` | function | Creates a 'CodeGraph' for the current project using the required core graph client, ensures its project indexes exist, and then invokes the provided closure with mutable access to that graph, returning the closure’s 'anyhow::Result<T>'. [crates/gcode/src/graph/code_graph/write.rs:309-318] |
| `delete_file_graph` | function | Deletes the graph entries for 'file_path' in the project’s code graph by invoking 'CodeGraph::delete_file_graph' through the required core graph client, passing the current symbol IDs, and returns any resulting error. [crates/gcode/src/graph/code_graph/write.rs:320-328] |
| `delete_file_projection` | function | Deletes the file projection identified by 'file_path' from the current project’s core graph by constructing a 'CodeGraph' with 'ctx.project_id' and delegating to 'delete_file_projection', returning any resulting error. [crates/gcode/src/graph/code_graph/write.rs:330-334] |
| `cleanup_orphans` | function | Calls 'with_code_graph' on the provided 'Context' and delegates to 'graph.cleanup_orphans()', returning its 'anyhow::Result<()>'. [crates/gcode/src/graph/code_graph/write.rs:336-338] |

_3 more symbol(s) not shown — run `gcode outline crates/gcode/src/graph/code_graph/write.rs` for the full list._

