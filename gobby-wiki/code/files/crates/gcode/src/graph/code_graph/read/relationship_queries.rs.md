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

`crates/gcode/src/graph/code_graph/read/relationship_queries.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `count_callers_query` | function | Builds a Cypher query and string-parameter map that count the number of distinct 'CodeSymbol' caller nodes in a project that 'CALLS' the target symbol with the given 'id', filtered by 'CALL_TARGET_PREDICATE'. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:9-21] |
| `count_usages_query` | function | Builds and returns a Cypher query string plus typed string parameters that count 'CodeSymbol' nodes in the given project with outgoing 'CALLS' edges to the specified target symbol, constrained by 'CALL_TARGET_PREDICATE'. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:23-38] |
| `find_callers_query` | function | Builds a parameterized Cypher query and string-parameter map that, after clamping 'offset' and 'limit', finds 'CodeSymbol' callers of a given target symbol within a project, aggregates call provenance to derive a confidence label, and returns each caller’s id, name, file path, line, and confidence label with ordering and pagination. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:40-62] |
| `find_usages_query` | function | Builds a parameterized Cypher query and string-parameter map to find incoming 'CALLS' usages of a target symbol within a project, with clamped pagination via 'offset' and 'limit'. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:64-84] |
| `find_caller_ids_query` | function | Builds a parameterized Cypher query that clamps the requested limit and returns the query plus string parameters to find distinct 'CodeSymbol' caller IDs for a given project and target symbol, ordered by caller ID and limited to the clamped value. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:86-102] |
| `find_usage_ids_query` | function | Builds and returns a parameterized Cypher query plus string parameters to find distinct caller 'source.id' values for a given 'symbol_id' within a 'project_id', applying a clamped 'LIMIT' and ordering by 'source.id'. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:104-120] |
| `find_callers_batch_query` | function | Builds and returns a Cypher batch query plus 'project' parameter map that finds callers of any symbol in 'symbol_ids' within a project, aggregates call-site metadata to derive file/line and confidence, orders by caller ID, and applies a clamped result limit. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:122-143] |
| `find_caller_ids_batch_query` | function | Builds a Cypher query and parameter map that, for a given project and list of target symbol IDs, returns the distinct IDs of caller 'CodeSymbol' nodes that call any matching target, ordered by caller ID and capped by a clamped limit. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:145-162] |
| `find_callees_batch_query` | function | Builds a parameterized Cypher query and string-parameter map that, for a given project and list of caller symbol IDs, returns distinct callees reached by 'CALLS' edges with their earliest file/line provenance and computed confidence label, ordered by callee ID and capped by a clamped limit. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:164-185] |
| `find_callee_ids_batch_query` | function | Builds a Cypher query and string-parameter map that, for a given project and list of source symbol IDs, returns up to 'limit' distinct callee 'target.id' values from '(:CodeSymbol)-[:CALLS]->' edges after clamping the limit and inlining the source ID list. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:187-204] |
| `symbol_callee_edges_query` | function | Constructs and returns a Cypher query plus parameters that, for a given project and list of symbol IDs, retrieves all distinct 'CALLS' edges from matching 'CodeSymbol' nodes to same-project target symbols, ordered by source and target ID. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:206-220] |
| `symbol_path_steps_query` | function | Builds a Cypher query and parameter map that, for a given 'project_id' and list of 'symbol_ids', selects matching 'CodeSymbol' nodes in that project and returns each symbol's id, name fallback, file path fallback, and starting line. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:222-238] |
| `get_imports_query` | function | Returns a Cypher query and string parameter map that match a 'CodeFile' by 'project' and 'path', traverse its 'IMPORTS' edges to 'CodeModule' nodes, and return each module’s name as both 'id' and 'module_name'. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:240-250] |
| `resolve_external_call_target_query` | function | Builds and returns a Cypher query plus string parameters that resolve an external symbol target for a project by matching either exact 'id', qualified 'module.member', or unqualified 'name', then ordering the best match first and limiting results to 11. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:252-278] |
| `blast_radius_query` | function | Builds a parameterized Cypher query that clamps 'depth' to 1..5 and 'limit' via 'clamp_limit', then returns distinct 'CodeSymbol' nodes in the same project that reach the target through '[:CALLS*1..depth]', annotated with minimum call distance, defining file path, and sorted by distance then name. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:280-297] |

_Verified by 3 in-file unit tests._

