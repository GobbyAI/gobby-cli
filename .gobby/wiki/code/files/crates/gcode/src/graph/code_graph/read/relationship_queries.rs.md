---
title: crates/gcode/src/graph/code_graph/read/relationship_queries.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/relationship_queries.rs
  ranges:
  - 7-19
  - 21-36
  - 38-57
  - 59-78
  - 80-96
  - 98-114
  - 116-135
  - 137-154
  - 156-175
  - 177-194
  - 196-206
  - 208-225
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/read/relationship_queries.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Purpose

This file collects read-side Cypher query builders for code-graph relationships in a project, centered on `CALLS`-based caller/usage lookups, batch ID retrieval, import lookup, and a blast-radius traversal.

The functions share the same pattern: they build parameterized query strings plus string parameter maps, clamp pagination or result bounds through shared helpers, and use `CALL_TARGET_PREDICATE` to filter valid call targets while returning counts, distinct nodes, or minimal location metadata as needed.
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:7-19]
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:21-36]
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:38-57]
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:59-78]
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:80-96]

## API Symbols

- `count_callers_query` (function) component `count_callers_query [function]` (`298cad5d-ba20-506d-a7e6-7bfff9764958`) lines 7-19 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:7-19]
  - Signature: `pub(crate) fn count_callers_query(`
  - Purpose: Constructs a Cypher query and string-parameter map that count the number of distinct 'CodeSymbol' caller nodes in a given project that 'CALLS' the target symbol with the specified 'id', applying 'CALL_TARGET_PREDICATE' before returning 'cnt'. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:7-19]
- `count_usages_query` (function) component `count_usages_query [function]` (`1981900e-76e7-5c47-b9e3-deb98b371541`) lines 21-36 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:21-36]
  - Signature: `pub(crate) fn count_usages_query(`
  - Purpose: Returns a Cypher count query and string parameter map that count 'source:CodeSymbol' nodes in the given project with 'CALLS' edges to the target symbol ID, filtered by 'CALL_TARGET_PREDICATE', and labeled for the broader “usages” API surface. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:21-36]
- `find_callers_query` (function) component `find_callers_query [function]` (`8002e729-eacc-5e45-aa84-870ae0522825`) lines 38-57 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:38-57]
  - Signature: `pub(crate) fn find_callers_query(`
  - Purpose: Builds a parameterized Cypher query and string-parameter map that, after clamping pagination inputs, returns distinct callers of the target symbol in a project with their id, name, file path, and start line, ordered by caller id and paginated with 'SKIP'/'LIMIT'. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:38-57]
- `find_usages_query` (function) component `find_usages_query [function]` (`9d9777ff-0127-5e66-98b3-dde3bd129868`) lines 59-78 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:59-78]
  - Signature: `pub(crate) fn find_usages_query(`
  - Purpose: Builds a parameterized Cypher query and string-typed parameter map that, after clamping pagination bounds, returns incoming 'CALLS' usages for a target code symbol in a project, ordered by source ID and location with 'SKIP'/'LIMIT' applied. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:59-78]
- `find_caller_ids_query` (function) component `find_caller_ids_query [function]` (`4580d72c-2f7b-55fa-a073-04b3a0f002a2`) lines 80-96 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:80-96]
  - Signature: `pub(super) fn find_caller_ids_query(`
  - Purpose: Builds and returns a parameterized Cypher query plus string parameters to find distinct caller symbol IDs in a given project that CALL the target symbol ID, applying a clamped result limit and ordering the IDs. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:80-96]
- `find_usage_ids_query` (function) component `find_usage_ids_query [function]` (`8c3a74cd-b8e3-5dae-9b70-e60b649907df`) lines 98-114 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:98-114]
  - Signature: `pub(super) fn find_usage_ids_query(`
  - Purpose: Constructs and returns a Cypher query plus string parameters that, for a given project and symbol ID, finds distinct calling 'CodeSymbol' source IDs that 'CALLS' the target symbol and satisfy 'CALL_TARGET_PREDICATE', ordered by source ID and capped by a clamped limit. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:98-114]
- `find_callers_batch_query` (function) component `find_callers_batch_query [function]` (`ce66ea98-0568-5767-ae78-d6e966ecf0bd`) lines 116-135 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:116-135]
  - Signature: `pub(crate) fn find_callers_batch_query(`
  - Purpose: Builds a Cypher query and parameter map that, for a given project and list of symbol IDs, finds distinct callers of matching target symbols via 'CALLS' relationships, groups by caller to return caller id/name plus minimum file and line metadata, orders by caller id, and applies a clamped result limit. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:116-135]
- `find_caller_ids_batch_query` (function) component `find_caller_ids_batch_query [function]` (`cc3fe52d-b679-5b06-8a13-0cd432ce0ef7`) lines 137-154 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:137-154]
  - Signature: `pub(super) fn find_caller_ids_batch_query(`
  - Purpose: Builds a Cypher query and parameter map that, for a given project and list of target symbol IDs, returns the distinct IDs of callers in that project that call any matching target, ordered by caller ID and capped by a clamped limit. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:137-154]
- `find_callees_batch_query` (function) component `find_callees_batch_query [function]` (`774061eb-9c9e-576b-9d5d-50da936723a6`) lines 156-175 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:156-175]
  - Signature: `pub(crate) fn find_callees_batch_query(`
  - Purpose: Builds a parameterized Cypher query and string-parameter map that find 'CALLS' targets for the given 'symbol_ids' within a project, aggregates the minimum source file/line per target, orders by callee ID, and applies a clamped result limit. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:156-175]
- `find_callee_ids_batch_query` (function) component `find_callee_ids_batch_query [function]` (`d17232fd-534f-5fa2-8245-80d800e729d6`) lines 177-194 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:177-194]
  - Signature: `pub(super) fn find_callee_ids_batch_query(`
  - Purpose: Builds a parameterized Cypher query and string-parameter map that finds distinct callee 'target.id' values for the given 'symbol_ids' within a project via 'CALLS' edges, applying a clamped result limit and ordering the IDs. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:177-194]
- `get_imports_query` (function) component `get_imports_query [function]` (`6629c8c2-eed8-516d-a72f-46e80c9da206`) lines 196-206 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:196-206]
  - Signature: `pub(crate) fn get_imports_query(`
  - Purpose: Returns a Cypher query and string parameters that match a 'CodeFile' by 'path' and 'project', traverse outgoing 'IMPORTS' edges to 'CodeModule' nodes, and return each imported module’s name as both 'id' and 'module_name'. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:196-206]
- `blast_radius_query` (function) component `blast_radius_query [function]` (`432b02fc-0481-53c9-b6b1-31d8e0c59664`) lines 208-225 [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:208-225]
  - Signature: `pub(crate) fn blast_radius_query(depth: usize, limit: usize) -> String {`
  - Purpose: Returns a Cypher query string that clamps 'depth' to 1–5 and 'limit' via 'clamp_limit', then finds symbols in the same project that can reach the target through '[:CALLS*1..depth]', annotates each with minimum call distance and optional defining file path, and orders/limits the distinct results. [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:208-225]

