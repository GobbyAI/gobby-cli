---
title: crates/gcode/src/graph/code_graph/read/relationships.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/relationships.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/read/relationships.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Overview

`crates/gcode/src/graph/code_graph/read/relationships.rs` exposes 24 indexed API symbols.

## How it fits

`crates/gcode/src/graph/code_graph/read/relationships.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ResolvedExternalCallTarget` | class | A 'ResolvedExternalCallTarget' is a struct that identifies an external call target with a string 'id' and a human-readable 'display_name'. [crates/gcode/src/graph/code_graph/read/relationships.rs:24-27] |
| `external_call_target_display_name` | function | Returns 'name' unchanged when 'module' is empty, otherwise formats the display name as '"{module}.{name}"'. [crates/gcode/src/graph/code_graph/read/relationships.rs:29-35] |
| `select_external_call_target` | function | Returns the sole external call target when exactly one candidate is provided, otherwise returns 'None' along with the display names of all candidate targets as suggestions. [crates/gcode/src/graph/code_graph/read/relationships.rs:37-48] |
| `count_callers` | function | Returns the number of caller relationships for the given 'symbol_id' by running 'count_callers_query' against the project’s core graph client when available, or '0' if the core graph is absent. [crates/gcode/src/graph/code_graph/read/relationships.rs:50-60] |
| `count_usages` | function | Returns the number of usage rows for 'symbol_id' in 'ctx.project_id' by executing a count query against the core graph client when available, and falls back to '0' if the core graph is absent. [crates/gcode/src/graph/code_graph/read/relationships.rs:62-72] |
| `find_callers` | function | Queries the optional core graph backend for caller relationships of the specified symbol in the given project, applying offset/limit pagination and converting the returned rows into 'GraphResult' values. [crates/gcode/src/graph/code_graph/read/relationships.rs:74-85] |
| `find_usages` | function | Queries the optional core graph for usages of the given 'symbol_id' in the current project using pagination ('offset', 'limit'), converts each returned row into a 'GraphResult', and returns the results as an 'anyhow::Result<Vec<GraphResult>>'. [crates/gcode/src/graph/code_graph/read/relationships.rs:87-98] |
| `find_caller_ids` | function | Queries the optional core graph for up to 'limit' caller node IDs for 'symbol_id' in the current project, returning the '"id"' field from each result row as a 'Vec<String>'. [crates/gcode/src/graph/code_graph/read/relationships.rs:100-113] |
| `find_usage_ids` | function | Queries the optional core graph for usages of 'symbol_id' in 'ctx.project_id' with the given 'limit', then returns a 'Vec<String>' of row '"id"' values extracted from the result set. [crates/gcode/src/graph/code_graph/read/relationships.rs:115-124] |
| `find_callers_batch` | function | Returns an empty vector for an empty 'symbol_ids' slice, otherwise queries the optional core graph for callers of the specified symbols with the given 'limit' and converts the resulting rows into 'GraphResult' values. [crates/gcode/src/graph/code_graph/read/relationships.rs:126-139] |
| `find_caller_ids_batch` | function | Returns an empty vector for no input, otherwise queries the optional core graph for caller 'id's of the given 'symbol_ids' in the specified project up to 'limit', and collects the 'id' string from each returned row into a 'Vec<String>'. [crates/gcode/src/graph/code_graph/read/relationships.rs:141-157] |
| `find_callees_batch` | function | Returns an empty vector when 'symbol_ids' is empty; otherwise it builds and executes a batched core-graph query for the given project, symbol IDs, and result limit, then converts the returned rows into 'GraphResult' values. [crates/gcode/src/graph/code_graph/read/relationships.rs:159-172] |
| `find_callee_ids_batch` | function | Returns an empty vector for an empty input slice, otherwise queries the optional core graph for callee IDs of the given 'symbol_ids' with the specified 'limit' and collects the '"id"' field from each returned row into a 'Vec<String>'. [crates/gcode/src/graph/code_graph/read/relationships.rs:174-190] |
| `get_imports` | function | Queries the optional core graph for all import relationships associated with 'file_path' in 'ctx.project_id', converts each returned row into a 'GraphResult', and returns the collected results as an 'anyhow::Result<Vec<GraphResult>>'. [crates/gcode/src/graph/code_graph/read/relationships.rs:192-198] |
| `resolve_external_call_target` | function | Queries the optional core graph for project-scoped external-call target candidates matching 'input', converts result rows into 'ResolvedExternalCallTarget' values using 'id', 'name', and 'module', and returns the selection produced by 'select_external_call_target' or '(None, Vec::new())' when no core graph is available. [crates/gcode/src/graph/code_graph/read/relationships.rs:200-225] |
| `symbol_callee_edges` | function | Returns an empty vector for no input, otherwise executes the callee-edge query for the given project and symbol IDs and collects each result row’s 'source_id' and 'target_id' into a 'Vec<(String, String)>'. [crates/gcode/src/graph/code_graph/read/relationships.rs:227-245] |
| `reconstruct_symbol_path` | function | Builds the inclusive ancestor path from 'from_id' to 'to_id' by walking parent links in 'parents', returning the reversed path as 'Vec<String>' or an empty vector if no complete chain exists. [crates/gcode/src/graph/code_graph/read/relationships.rs:247-263] |
| `symbol_path_steps` | function | Returns an ordered 'Vec<GraphPathStep>' for the requested 'symbol_ids' by querying the graph, mapping rows by symbol ID, filling in name/file/line defaults, assigning each step’s position to its input index, and returning an empty vector if the input is empty or any requested symbol is missing. [crates/gcode/src/graph/code_graph/read/relationships.rs:265-302] |
| `shortest_symbol_path` | function | Performs a bounded breadth-first search over the project’s symbol callee graph from 'from_id' to 'to_id', tracking parent links to reconstruct and return the shortest discovered symbol path as 'GraphPathStep's, or an empty vector if no path is found within 'max_depth'. [crates/gcode/src/graph/code_graph/read/relationships.rs:304-342] |
| `blast_radius` | function | Builds and executes a blast-radius graph query for the given symbol ID and depth against the optional core graph client, then maps the returned rows into 'GraphResult' values and returns them as an 'anyhow::Result<Vec<GraphResult>>'. [crates/gcode/src/graph/code_graph/read/relationships.rs:344-355] |
| `target` | function | Constructs and returns a 'ResolvedExternalCallTarget' by cloning the provided 'id' and 'display_name' string slices into owned 'String' fields. [crates/gcode/src/graph/code_graph/read/relationships.rs:361-366] |

_Verified by 3 in-file unit tests._

