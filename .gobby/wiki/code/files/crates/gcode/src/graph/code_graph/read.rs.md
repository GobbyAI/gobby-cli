---
title: crates/gcode/src/graph/code_graph/read.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read.rs
  ranges:
  - 45-93
  - 95-97
  - 99-111
  - 113-128
  - 130-149
  - 151-170
  - 172-188
  - 190-206
  - 208-227
  - 229-246
  - 248-267
  - 269-286
  - 288-298
  - 300-317
  - 319-338
  - 340-356
  - 358-377
  - 379-399
  - 401-412
  - 414-436
  - 438-459
  - 461-475
  - 477-501
  - 503-525
  - 527-553
  - 555-564
  - 566-645
  - 647-673
  - 675-711
  - 713-786
  - 788-798
  - 800-810
  - 812-823
  - 825-836
  - 838-851
  - 853-862
  - 864-877
  - 879-895
  - 897-910
  - 912-928
  - 930-936
  - 938-949
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/read.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Purpose

This file provides a query layer for analyzing code call graphs stored in Neo4j. It contains three main categories of functions working together:

**Query builders** generate parameterized Cypher queries for different analysis patterns: single-symbol queries (find callers, usages, neighbors), batch queries (multiple symbols at once), file-level analysis (symbols and calls within files), import graph navigation, and transitive dependency analysis (blast radius queries). These builders use constants like CALL_TARGET_PREDICATE and NEIGHBOR_TYPE_CASE to handle multiple Neo4j node types (CodeSymbol, UnresolvedCallee, ExternalSymbol).

**Execution wrappers** are the public API that run these queries against an optional core graph database using `with_optional_core_graph`, executing operations like `count_callers`, `find_usages`, and `blast_radius`. They map query results to GraphResult objects via `row_to_graph_result`.

**Payload builders** (`project_overview_graph`, `file_graph`, `symbol_neighbors`, `blast_radius_graph`) transform raw query rows into structured GraphPayload objects containing nodes and links for visualization. Helper functions like `row_usize`, `count_from_rows`, and `dedupe_limited_blast_rows` process raw database results, with `clamp_limit` and `clamp_offset` enforcing the MAX_GRAPH_LIMIT (100) boundary on all result sets.

Together these components enable exploring code relationships from multiple perspectives: direct caller/callee relationships, project-wide file and module imports, file-level function definitions and calls, and impact analysis showing all symbols that transitively depend on a given target.
[crates/gcode/src/graph/code_graph/read.rs:45-90]
[crates/gcode/src/graph/code_graph/read.rs:91-93]
[crates/gcode/src/graph/code_graph/read.rs:95-97]
[crates/gcode/src/graph/code_graph/read.rs:99-111]
[crates/gcode/src/graph/code_graph/read.rs:113-128]

## API Symbols

- `row_to_graph_result` (function) component `row_to_graph_result [function]` (`4a77dc3d-2ed0-5ea4-9b83-c099cfe94f94`) lines 45-90 [crates/gcode/src/graph/code_graph/read.rs:45-90]
  - Signature: `pub(crate) fn row_to_graph_result(row: &Row) -> GraphResult {`
  - Purpose: Converts a database Row to a GraphResult struct by extracting graph node and relation properties using cascading column name fallbacks with type conversions. [crates/gcode/src/graph/code_graph/read.rs:45-90]
- `clamp_limit` (function) component `clamp_limit [function]` (`5ee1320e-2e49-5c1c-b8b7-2cbb7a1adc50`) lines 91-93 [crates/gcode/src/graph/code_graph/read.rs:91-93]
  - Signature: `fn clamp_limit(limit: usize) -> usize {`
  - Purpose: Clamps the input `limit` to a maximum of `MAX_GRAPH_LIMIT` by delegating to `typed_query::clamp_limit`. [crates/gcode/src/graph/code_graph/read.rs:91-93]
- `clamp_offset` (function) component `clamp_offset [function]` (`c2c5846c-da6e-516d-ba8c-aec079725d4b`) lines 95-97 [crates/gcode/src/graph/code_graph/read.rs:95-97]
  - Signature: `fn clamp_offset(offset: usize) -> usize {`
  - Purpose: Clamps the offset value to a maximum threshold of MAX_GRAPH_LIMIT. [crates/gcode/src/graph/code_graph/read.rs:95-97]
- `count_callers_query` (function) component `count_callers_query [function]` (`947df2c3-4e25-5192-a7fe-f91ebec51657`) lines 99-111 [crates/gcode/src/graph/code_graph/read.rs:99-111]
  - Signature: `pub(crate) fn count_callers_query(`
  - Purpose: Generates a parameterized Cypher query that counts the distinct number of CodeSymbol nodes calling a specified target symbol within a project graph. [crates/gcode/src/graph/code_graph/read.rs:99-111]
- `count_usages_query` (function) component `count_usages_query [function]` (`9b3ee435-9157-5583-bb9c-52593d59bf64`) lines 113-128 [crates/gcode/src/graph/code_graph/read.rs:113-128]
  - Signature: `pub(crate) fn count_usages_query(`
  - Purpose: # Summary

Constructs a parameterized Cypher query that counts the number of code symbols in a specified project that have CALLS relationships targeting a given symbol. [crates/gcode/src/graph/code_graph/read.rs:113-128]
- `find_callers_query` (function) component `find_callers_query [function]` (`2e283c0b-5213-51ac-acab-4e551320c9ba`) lines 130-149 [crates/gcode/src/graph/code_graph/read.rs:130-149]
  - Signature: `pub(crate) fn find_callers_query(`
  - Purpose: Constructs a parameterized Neo4j Cypher query that retrieves paginated results of all code symbols that call a specified target symbol within a project. [crates/gcode/src/graph/code_graph/read.rs:130-149]
- `find_usages_query` (function) component `find_usages_query [function]` (`23753c47-43dc-5968-b295-595699d8fb38`) lines 151-170 [crates/gcode/src/graph/code_graph/read.rs:151-170]
  - Signature: `pub(crate) fn find_usages_query(`
  - Purpose: Constructs a parameterized Neo4j Cypher query to retrieve all code symbols that call a specified target symbol, returning caller metadata and call site information with pagination support. [crates/gcode/src/graph/code_graph/read.rs:151-170]
- `find_caller_ids_query` (function) component `find_caller_ids_query [function]` (`a90a1b19-e2c4-5f45-aa1f-dffac723aaab`) lines 172-188 [crates/gcode/src/graph/code_graph/read.rs:172-188]
  - Signature: `fn find_caller_ids_query(`
  - Purpose: Returns a tuple containing a parameterized Neo4j Cypher query and string parameters that retrieves distinct CodeSymbol IDs of all callers invoking a specified target symbol within a given project. [crates/gcode/src/graph/code_graph/read.rs:172-188]
- `find_usage_ids_query` (function) component `find_usage_ids_query [function]` (`80914974-32bb-5651-b04e-40673403e891`) lines 190-206 [crates/gcode/src/graph/code_graph/read.rs:190-206]
  - Signature: `fn find_usage_ids_query(`
  - Purpose: Constructs a parameterized Neo4j Cypher query that retrieves distinct source code symbol identifiers invoking a specified target symbol within a given project, ordered by source ID and limited by count. [crates/gcode/src/graph/code_graph/read.rs:190-206]
- `find_callers_batch_query` (function) component `find_callers_batch_query [function]` (`b3c4580a-e2b4-5d89-9dda-c0ada4b56e08`) lines 208-227 [crates/gcode/src/graph/code_graph/read.rs:208-227]
  - Signature: `pub(crate) fn find_callers_batch_query(`
  - Purpose: Generates a parameterized Cypher query to retrieve all code symbols that call specified target symbols, returning their identifiers, names, and earliest call locations. [crates/gcode/src/graph/code_graph/read.rs:208-227]
- `find_caller_ids_batch_query` (function) component `find_caller_ids_batch_query [function]` (`94d28483-6e5e-5319-bac6-4064ac82b702`) lines 229-246 [crates/gcode/src/graph/code_graph/read.rs:229-246]
  - Signature: `fn find_caller_ids_batch_query(`
  - Purpose: Constructs a parameterized Cypher query to retrieve distinct caller symbol IDs that invoke any of the specified target symbol IDs within a project. [crates/gcode/src/graph/code_graph/read.rs:229-246]
- `find_callees_batch_query` (function) component `find_callees_batch_query [function]` (`2280ab06-6ecd-52db-a9c1-f33bbd0eb73c`) lines 248-267 [crates/gcode/src/graph/code_graph/read.rs:248-267]
  - Signature: `pub(crate) fn find_callees_batch_query(`
  - Purpose: Generates a parameterized Neo4j Cypher query that retrieves all callee symbols and their earliest call locations for a batch of source code symbols, ordered by callee ID and limited by the specified constraint. [crates/gcode/src/graph/code_graph/read.rs:248-267]
- `find_callee_ids_batch_query` (function) component `find_callee_ids_batch_query [function]` (`4e980fea-090b-56e8-81e9-ea910d31d297`) lines 269-286 [crates/gcode/src/graph/code_graph/read.rs:269-286]
  - Signature: `fn find_callee_ids_batch_query(`
  - Purpose: Constructs a Cypher query and parameter map that retrieves distinct target symbol IDs from all outbound CALLS relationships originating from a batch of source symbols within a project, ordered and limited by count. [crates/gcode/src/graph/code_graph/read.rs:269-286]
- `get_imports_query` (function) component `get_imports_query [function]` (`753e67e2-a227-5261-9c26-e75e046b0ff2`) lines 288-298 [crates/gcode/src/graph/code_graph/read.rs:288-298]
  - Signature: `pub(crate) fn get_imports_query(`
  - Purpose: Constructs a Cypher query and parameter map to retrieve all modules imported by a specified code file from a Neo4j graph database. [crates/gcode/src/graph/code_graph/read.rs:288-298]
- `blast_radius_query` (function) component `blast_radius_query [function]` (`7281c24b-2a5b-5ed2-90f0-d958adebdbac`) lines 300-317 [crates/gcode/src/graph/code_graph/read.rs:300-317]
  - Signature: `pub(crate) fn blast_radius_query(depth: usize, limit: usize) -> String {`
  - Purpose: Generates a Neo4j Cypher query that identifies all code symbols transitively calling a specified target symbol within a bounded call-chain depth (1-5 levels), returning caller metadata sorted by minimum call distance. [crates/gcode/src/graph/code_graph/read.rs:300-317]
- `project_overview_files_query` (function) component `project_overview_files_query [function]` (`781eab46-0a56-55c3-9f71-65a1f5699927`) lines 319-338 [crates/gcode/src/graph/code_graph/read.rs:319-338]
  - Signature: `fn project_overview_files_query(`
  - Purpose: # Summary

Generates a parameterized Neo4j Cypher query that retrieves project files ranked by their import count and symbol definitions with a clamped result limit. [crates/gcode/src/graph/code_graph/read.rs:319-338]
- `project_overview_imports_query` (function) component `project_overview_imports_query [function]` (`549f79f5-c9f5-59b6-a967-814716cd3d63`) lines 340-356 [crates/gcode/src/graph/code_graph/read.rs:340-356]
  - Signature: `fn project_overview_imports_query(`
  - Purpose: Constructs a Cypher query and parameter map to retrieve IMPORTS relationships from specified CodeFiles to CodeModules within a project, limited by a clamped result count. [crates/gcode/src/graph/code_graph/read.rs:340-356]
- `project_overview_defines_query` (function) component `project_overview_defines_query [function]` (`dacc64d4-cd96-5be4-ba7a-ef0466d00c9b`) lines 358-377 [crates/gcode/src/graph/code_graph/read.rs:358-377]
  - Signature: `fn project_overview_defines_query(`
  - Purpose: This function generates a parameterized Cypher query that retrieves all code symbols defined by specified project files along with their metadata (name, kind, location), limited to a maximum result count. [crates/gcode/src/graph/code_graph/read.rs:358-377]
- `project_overview_calls_query` (function) component `project_overview_calls_query [function]` (`08f81370-6f2e-5152-8fb0-4017d6ac1ff0`) lines 379-399 [crates/gcode/src/graph/code_graph/read.rs:379-399]
  - Signature: `fn project_overview_calls_query(`
  - Purpose: Generates a Neo4j Cypher query with parameters that retrieves call graph relationships (sources, targets, and metadata) for code symbols defined in specified project files, with a bounded result set. [crates/gcode/src/graph/code_graph/read.rs:379-399]
- `file_symbols_query` (function) component `file_symbols_query [function]` (`935f63b4-e712-5177-854a-28a8a67e0f29`) lines 401-412 [crates/gcode/src/graph/code_graph/read.rs:401-412]
  - Signature: `fn file_symbols_query(project_id: &str, file_path: &str) -> (String, HashMap<String, String>) {`
  - Purpose: Generates a Neo4j Cypher query string and typed parameter map to retrieve all code symbols defined within a specified project file. [crates/gcode/src/graph/code_graph/read.rs:401-412]
- `file_calls_query` (function) component `file_calls_query [function]` (`616c9984-e531-5527-bac8-1a89c15149b3`) lines 414-436 [crates/gcode/src/graph/code_graph/read.rs:414-436]
  - Signature: `pub(super) fn file_calls_query(`
  - Purpose: Constructs a parameterized Cypher query that retrieves all CALLS relationship edges between code symbols where either the caller or callee resides in the specified file path, returning detailed source and target node properties along with call metadata. [crates/gcode/src/graph/code_graph/read.rs:414-436]
- `symbol_neighbors_query` (function) component `symbol_neighbors_query [function]` (`df7a8d96-eb1c-5655-a488-c233bdcbe631`) lines 438-459 [crates/gcode/src/graph/code_graph/read.rs:438-459]
  - Signature: `fn symbol_neighbors_query(`
  - Purpose: Generates a parameterized Cypher query that retrieves bidirectional call-graph neighbors (incoming and outgoing calls) of a specified code symbol, returning their metadata and relationship direction, limited to a clamped count. [crates/gcode/src/graph/code_graph/read.rs:438-459]
- `blast_radius_center_query` (function) component `blast_radius_center_query [function]` (`262a2e33-8e04-5f40-9886-1c9aaed12ca6`) lines 461-475 [crates/gcode/src/graph/code_graph/read.rs:461-475]
  - Signature: `fn blast_radius_center_query(`
  - Purpose: Constructs a parameterized Cypher query to retrieve a single code symbol's metadata (id, name, type, kind, file_path) from a Neo4j graph database, filtered by project and symbol ID across CodeSymbol, UnresolvedCallee, and ExternalSymbol node types. [crates/gcode/src/graph/code_graph/read.rs:461-475]
- `blast_radius_file_call_query` (function) component `blast_radius_file_call_query [function]` (`73c30320-453a-5537-81c5-3a818ac4ebf5`) lines 477-501 [crates/gcode/src/graph/code_graph/read.rs:477-501]
  - Signature: `fn blast_radius_file_call_query(`
  - Purpose: # Summary

Generates a parameterized Neo4j Cypher query that identifies all code symbols that transitively call (within a configurable depth limit) symbols defined in a target file, returning results sorted by minimum call-chain distance. [crates/gcode/src/graph/code_graph/read.rs:477-501]
- `blast_radius_file_import_query` (function) component `blast_radius_file_import_query [function]` (`6c9bb637-f396-5be1-bfb5-a902c9953ff2`) lines 503-525 [crates/gcode/src/graph/code_graph/read.rs:503-525]
  - Signature: `pub(super) fn blast_radius_file_import_query(`
  - Purpose: Generates a Neo4j Cypher query that identifies files transitively importing the modules used by a specified file within a configurable depth (1-5), ordered by minimum import path distance. [crates/gcode/src/graph/code_graph/read.rs:503-525]
- `dedupe_limited_blast_rows` (function) component `dedupe_limited_blast_rows [function]` (`e02e9136-83d4-522c-aa86-32c89bb17ea9`) lines 527-553 [crates/gcode/src/graph/code_graph/read.rs:527-553]
  - Signature: `pub(super) fn dedupe_limited_blast_rows(mut rows: Vec<Row>, limit: usize) -> Vec<Row> {`
  - Purpose: Sorts rows by distance and node identifiers, deduplicates by node_id (retaining first occurrences), and truncates the result to a clamped limit. [crates/gcode/src/graph/code_graph/read.rs:527-553]
- `count_from_rows` (function) component `count_from_rows [function]` (`99f413e0-edfe-5119-8e72-191a20e73aca`) lines 555-564 [crates/gcode/src/graph/code_graph/read.rs:555-564]
  - Signature: `fn count_from_rows(rows: &[Row]) -> usize {`
  - Purpose: Extracts the 'cnt' field from the first row, converts it to `usize` via u64 or i64 intermediate types, and returns 0 if the value is absent or conversion fails. [crates/gcode/src/graph/code_graph/read.rs:555-564]
- `project_overview_graph` (function) component `project_overview_graph [function]` (`6ecab80b-a13c-5f86-a65b-b85d453fe648`) lines 566-645 [crates/gcode/src/graph/code_graph/read.rs:566-645]
  - Signature: `pub fn project_overview_graph(ctx: &Context, limit: usize) -> anyhow::Result<GraphPayload> {`
  - Purpose: Constructs a GraphPayload containing project files, their imported modules, and defined symbols with their dependency links, bounded by configurable node and link count limits. [crates/gcode/src/graph/code_graph/read.rs:566-645]
- `file_graph` (function) component `file_graph [function]` (`6ae9710e-d584-5253-8e5a-bc68334d5c13`) lines 647-673 [crates/gcode/src/graph/code_graph/read.rs:647-673]
  - Signature: `pub fn file_graph(ctx: &Context, file_path: &str) -> anyhow::Result<GraphPayload> {`
  - Purpose: Constructs a GraphPayload containing a file node, its defined function symbols, and directed edges representing function definitions and inter-function call relationships. [crates/gcode/src/graph/code_graph/read.rs:647-673]
- `symbol_neighbors` (function) component `symbol_neighbors [function]` (`c623ca8d-407a-5735-bbe9-9f6d63e3d5a5`) lines 675-711 [crates/gcode/src/graph/code_graph/read.rs:675-711]
  - Signature: `pub fn symbol_neighbors(`
  - Purpose: Constructs a GraphPayload containing a focal symbol and its up-to-N neighboring functions connected by directional CALLS links, with directionality determined by whether the relationship is incoming or outgoing. [crates/gcode/src/graph/code_graph/read.rs:675-711]
- `blast_radius_graph` (function) component `blast_radius_graph [function]` (`2aa33b89-b550-5e1a-8fbb-2c941b585662`) lines 713-786 [crates/gcode/src/graph/code_graph/read.rs:713-786]
  - Signature: `pub fn blast_radius_graph(`
  - Purpose: Constructs a GraphPayload representing all code symbols and files that transitively depend on a target symbol or file, bounded by specified traversal depth and result cardinality limits. [crates/gcode/src/graph/code_graph/read.rs:713-786]
- `count_callers` (function) component `count_callers [function]` (`33f555c1-e680-5b0d-9bda-37989270b502`) lines 788-798 [crates/gcode/src/graph/code_graph/read.rs:788-798]
  - Signature: `pub fn count_callers(ctx: &Context, symbol_id: &str) -> anyhow::Result<usize> {`
  - Purpose: Executes a database query against an optional code graph to count the number of callers for a specified symbol, returning 0 if the graph is unavailable. [crates/gcode/src/graph/code_graph/read.rs:788-798]
- `count_usages` (function) component `count_usages [function]` (`4b7701b1-c6b2-5ef0-8966-5fcde6677cc5`) lines 800-810 [crates/gcode/src/graph/code_graph/read.rs:800-810]
  - Signature: `pub fn count_usages(ctx: &Context, symbol_id: &str) -> anyhow::Result<usize> {`
  - Purpose: Returns the count of usages for a specified symbol in the given project by querying the core graph database, with a fallback of zero if the graph is unavailable. [crates/gcode/src/graph/code_graph/read.rs:800-810]
- `find_callers` (function) component `find_callers [function]` (`ee5d723d-639e-5469-88a0-1bda04d72888`) lines 812-823 [crates/gcode/src/graph/code_graph/read.rs:812-823]
  - Signature: `pub fn find_callers(`
  - Purpose: Queries an optional graph database to retrieve a paginated list of callers for a specified symbol, mapping the results to GraphResult objects. [crates/gcode/src/graph/code_graph/read.rs:812-823]
- `find_usages` (function) component `find_usages [function]` (`123ef69e-6051-5e0f-9ee9-494551e7e4a1`) lines 825-836 [crates/gcode/src/graph/code_graph/read.rs:825-836]
  - Signature: `pub fn find_usages(`
  - Purpose: Executes a paginated graph database query to retrieve all usages of a specified symbol and maps the result rows to `GraphResult` structures. [crates/gcode/src/graph/code_graph/read.rs:825-836]
- `find_caller_ids` (function) component `find_caller_ids [function]` (`8b4f038e-63dc-562a-b860-c527dc966ae3`) lines 838-851 [crates/gcode/src/graph/code_graph/read.rs:838-851]
  - Signature: `pub fn find_caller_ids(`
  - Purpose: Queries an optional code graph database to retrieve a vector of caller IDs for a given symbol, constrained by a specified result limit. [crates/gcode/src/graph/code_graph/read.rs:838-851]
- `find_usage_ids` (function) component `find_usage_ids [function]` (`93feef96-c223-5590-9af4-8e95dbb1c21f`) lines 853-862 [crates/gcode/src/graph/code_graph/read.rs:853-862]
  - Signature: `pub fn find_usage_ids(ctx: &Context, symbol_id: &str, limit: usize) -> anyhow::Result<Vec<String>> {`
  - Purpose: Executes a parameterized database query to retrieve usage IDs for a specified symbol up to a given limit and returns the results as a vector of strings. [crates/gcode/src/graph/code_graph/read.rs:853-862]
- `find_callers_batch` (function) component `find_callers_batch [function]` (`c3b3335e-8ad0-590f-95f9-c38a8dad1b24`) lines 864-877 [crates/gcode/src/graph/code_graph/read.rs:864-877]
  - Signature: `pub fn find_callers_batch(`
  - Purpose: Retrieves callers of multiple symbols by executing a parameterized batch query against a graph database, limited by count and returning a collection of GraphResult objects. [crates/gcode/src/graph/code_graph/read.rs:864-877]
- `find_caller_ids_batch` (function) component `find_caller_ids_batch [function]` (`7cb6c81f-0649-5b8b-8c6d-ca1d161be669`) lines 879-895 [crates/gcode/src/graph/code_graph/read.rs:879-895]
  - Signature: `pub fn find_caller_ids_batch(`
  - Purpose: Retrieves the IDs of functions calling a batch of symbols from an optional code graph database up to a specified limit. [crates/gcode/src/graph/code_graph/read.rs:879-895]
- `find_callees_batch` (function) component `find_callees_batch [function]` (`012eaa3b-661d-5d53-9d81-3c47594e071f`) lines 897-910 [crates/gcode/src/graph/code_graph/read.rs:897-910]
  - Signature: `pub fn find_callees_batch(`
  - Purpose: Batch-retrieves functions called by multiple symbol IDs from a graph database, returning results as GraphResult objects up to a specified limit. [crates/gcode/src/graph/code_graph/read.rs:897-910]
- `find_callee_ids_batch` (function) component `find_callee_ids_batch [function]` (`6ac6bb29-2cd6-50da-b870-5b41e6d5a100`) lines 912-928 [crates/gcode/src/graph/code_graph/read.rs:912-928]
  - Signature: `pub fn find_callee_ids_batch(`
  - Purpose: Executes a batch query against the core graph to retrieve callee symbol IDs for a given set of symbol identifiers, limited by the specified bound. [crates/gcode/src/graph/code_graph/read.rs:912-928]
- `get_imports` (function) component `get_imports [function]` (`a676e7bd-4c78-54ec-981e-1774d22d7da5`) lines 930-936 [crates/gcode/src/graph/code_graph/read.rs:930-936]
  - Signature: `pub fn get_imports(ctx: &Context, file_path: &str) -> anyhow::Result<Vec<GraphResult>> {`
  - Purpose: Executes a parameterized graph database query to retrieve all import relationships for a specified file path and returns the results as a vector of `GraphResult` objects. [crates/gcode/src/graph/code_graph/read.rs:930-936]
- `blast_radius` (function) component `blast_radius [function]` (`768dc91e-d2a4-586c-81a3-4f937d599f2a`) lines 938-949 [crates/gcode/src/graph/code_graph/read.rs:938-949]
  - Signature: `pub fn blast_radius(`
  - Purpose: Executes a depth-constrained graph database query to retrieve all direct and transitive dependents of a specified symbol, returning them as a vector of GraphResult objects. [crates/gcode/src/graph/code_graph/read.rs:938-949]

