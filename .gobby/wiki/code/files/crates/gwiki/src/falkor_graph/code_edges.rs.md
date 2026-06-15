---
title: crates/gwiki/src/falkor_graph/code_edges.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph/code_edges.rs
  ranges:
  - 18-21
  - 23-114
  - 116-157
  - 159-167
  - 169-205
  - 207-213
  - 215-231
  - 233-237
  - 239-245
  - 247-252
  - 254-266
  - 268-270
  - 272-277
  - 279-285
  - 287-289
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/falkor_graph/code_edges.rs

Module: [[code/modules/crates/gwiki/src/falkor_graph|crates/gwiki/src/falkor_graph]]

## Purpose

Builds shared code-graph edge data for a set of documents by querying Falkor for call and import relationships, applying per-edge and global caps, and collecting any truncation markers. `load_code_graph_edges` drives the process: it filters documents to code files, fetches call edges and import edges through the query helpers, tracks remaining edge budget, and records truncation components when limits are hit. The smaller helpers normalize file paths, build query parameters and Cypher strings, map edge endpoints, and encapsulate limit/truncation bookkeeping so the loader can assemble a bounded `SharedCodeGraphEdges` result.
[crates/gwiki/src/falkor_graph/code_edges.rs:18-21]
[crates/gwiki/src/falkor_graph/code_edges.rs:23-114]
[crates/gwiki/src/falkor_graph/code_edges.rs:116-157]
[crates/gwiki/src/falkor_graph/code_edges.rs:159-167]
[crates/gwiki/src/falkor_graph/code_edges.rs:169-205]

## API Symbols

- `LimitedCodeGraphEdges` (class) component `LimitedCodeGraphEdges [class]` (`32f4b0e4-d704-5a95-a9b3-254e2bffa0f9`) lines 18-21 [crates/gwiki/src/falkor_graph/code_edges.rs:18-21]
  - Signature: `struct LimitedCodeGraphEdges {`
  - Purpose: 'LimitedCodeGraphEdges' is a struct that wraps a 'Vec<WikiGraphCodeEdge>' together with a 'truncated' flag indicating whether the edge list was cut off. [crates/gwiki/src/falkor_graph/code_edges.rs:18-21]
- `load_code_graph_edges` (function) component `load_code_graph_edges [function]` (`0775c1dd-d659-5a29-90e5-e97c7e504a3a`) lines 23-114 [crates/gwiki/src/falkor_graph/code_edges.rs:23-114]
  - Signature: `pub(crate) fn load_code_graph_edges(`
  - Purpose: Loads code documents from 'documents', queries the graph client for per-file call and import edges within the supplied limits while tracking truncation and a global edge cap, and returns the accumulated 'SharedCodeGraphEdges' or an error. [crates/gwiki/src/falkor_graph/code_edges.rs:23-114]
- `code_call_edges` (function) component `code_call_edges [function]` (`fb62f197-8f94-5f03-9473-580d85ce25d3`) lines 116-157 [crates/gwiki/src/falkor_graph/code_edges.rs:116-157]
  - Signature: `fn code_call_edges(`
  - Purpose: Queries call-edge rows for a file from 'GraphClient', maps each row into a 'WikiGraphCodeEdge' with inferred 'calls'/'callers' direction and provenance metadata, truncates to the requested limit, and returns the edges plus a truncation flag. [crates/gwiki/src/falkor_graph/code_edges.rs:116-157]
- `code_call_edges_query` (function) component `code_call_edges_query [function]` (`af1379bb-6fbc-5be2-b869-42db0a5f1569`) lines 159-167 [crates/gwiki/src/falkor_graph/code_edges.rs:159-167]
  - Signature: `pub(super) fn code_call_edges_query() -> &'static str {`
  - Purpose: Returns a Cypher query string that finds 'CALLS' edges in the given project involving a specified file path, returning source/target file paths and symbol names plus the call line, ordered deterministically and capped by '$limit'. [crates/gwiki/src/falkor_graph/code_edges.rs:159-167]
- `code_import_edges` (function) component `code_import_edges [function]` (`417d8bea-062d-5470-a99f-c23cdb2dd730`) lines 169-205 [crates/gwiki/src/falkor_graph/code_edges.rs:169-205]
  - Signature: `fn code_import_edges(`
  - Purpose: Queries the graph client for import edges for a given project/file, truncates the result to the requested limit, and maps each row into a 'LimitedCodeGraphEdges' list of outgoing '"imports"' 'WikiGraphCodeEdge's with defaulted source/target fields and fixed provenance. [crates/gwiki/src/falkor_graph/code_edges.rs:169-205]
- `code_import_edges_query` (function) component `code_import_edges_query [function]` (`7767ef79-f4a2-5855-b756-46de4172a8d9`) lines 207-213 [crates/gwiki/src/falkor_graph/code_edges.rs:207-213]
  - Signature: `pub(super) fn code_import_edges_query() -> &'static str {`
  - Purpose: Returns a Cypher query string that finds 'CodeFile' nodes by 'path' and 'project', follows outgoing 'IMPORTS' edges to same-project 'CodeModule' nodes, and returns the source file path and target module name ordered by source and target with a 'LIMIT' parameter. [crates/gwiki/src/falkor_graph/code_edges.rs:207-213]
- `code_edge_query_params` (function) component `code_edge_query_params [function]` (`9da3f5ac-e05b-5052-8e0e-be8d1ad1362b`) lines 215-231 [crates/gwiki/src/falkor_graph/code_edges.rs:215-231]
  - Signature: `pub(super) fn code_edge_query_params(`
  - Purpose: Builds and returns a 'HashMap<String, String>' of escaped Falkor query parameters for 'project', 'path', and a validated 'limit' sentinel converted to a string, wrapped in 'anyhow::Result'. [crates/gwiki/src/falkor_graph/code_edges.rs:215-231]
- `sentinel_limit` (function) component `sentinel_limit [function]` (`d5d73cb3-82f3-5d7b-bc10-66bfce067773`) lines 233-237 [crates/gwiki/src/falkor_graph/code_edges.rs:233-237]
  - Signature: `fn sentinel_limit(limit: usize) -> anyhow::Result<usize> {`
  - Purpose: Returns 'limit + 1' as a 'usize', or an 'anyhow' error if the addition overflows, using the message 'shared code graph edge limit is too large: {limit}'. [crates/gwiki/src/falkor_graph/code_edges.rs:233-237]
- `truncate_to_limit` (function) component `truncate_to_limit [function]` (`2a422e76-1369-55f6-981d-3c337d9e0ea9`) lines 239-245 [crates/gwiki/src/falkor_graph/code_edges.rs:239-245]
  - Signature: `pub(super) fn truncate_to_limit<T>(rows: &mut Vec<T>, limit: usize) -> bool {`
  - Purpose: Returns 'true' if 'rows' currently exceeds 'limit', truncating the vector in place to 'limit' elements when it does, and 'false' otherwise. [crates/gwiki/src/falkor_graph/code_edges.rs:239-245]
- `remaining_code_edge_limit` (function) component `remaining_code_edge_limit [function]` (`c6bc2497-2af6-5490-9620-23ac5d92b0c7`) lines 247-252 [crates/gwiki/src/falkor_graph/code_edges.rs:247-252]
  - Signature: `pub(super) fn remaining_code_edge_limit(`
  - Purpose: Returns 'Some(min(configured_limit, remaining_edges))' when 'remaining_edges > 0', otherwise returns 'None'. [crates/gwiki/src/falkor_graph/code_edges.rs:247-252]
- `record_code_edge_truncation` (function) component `record_code_edge_truncation [function]` (`e8c3e0ef-4465-58d5-841a-5cd8343d05c0`) lines 254-266 [crates/gwiki/src/falkor_graph/code_edges.rs:254-266]
  - Signature: `pub(super) fn record_code_edge_truncation(`
  - Purpose: Inserts a truncation marker into 'components', using a global code-edge truncation component with 'MAX_TOTAL_CODE_EDGES' when 'query_limit' is lower than 'configured_limit', otherwise using the provided 'component' and 'configured_limit'. [crates/gwiki/src/falkor_graph/code_edges.rs:254-266]
- `truncation_component` (function) component `truncation_component [function]` (`c9480e0d-41f7-59cb-9cb1-7b0e6d3928d6`) lines 268-270 [crates/gwiki/src/falkor_graph/code_edges.rs:268-270]
  - Signature: `pub(super) fn truncation_component(component: &str, limit: usize) -> String {`
  - Purpose: Returns a 'String' containing the input 'component', a '>' separator, and the numeric 'limit' formatted as '"{component}>{limit}"'. [crates/gwiki/src/falkor_graph/code_edges.rs:268-270]
- `code_doc_source_path` (function) component `code_doc_source_path [function]` (`bf490a72-e183-5fd3-9932-411dfaaecca9`) lines 272-277 [crates/gwiki/src/falkor_graph/code_edges.rs:272-277]
  - Signature: `pub(super) fn code_doc_source_path(path: &Path) -> Option<String> {`
  - Purpose: Returns the normalized graph path as a 'String' only if it lies under 'code/files/' and ends with '.md', stripping both the prefix and suffix. [crates/gwiki/src/falkor_graph/code_edges.rs:272-277]
- `code_endpoint` (function) component `code_endpoint [function]` (`ca4d8e56-ae15-57b4-821d-33a58460bb4b`) lines 279-285 [crates/gwiki/src/falkor_graph/code_edges.rs:279-285]
  - Signature: `fn code_endpoint(file_path: &str, symbol: &str) -> String {`
  - Purpose: Returns the file path unchanged when 'symbol' is empty, otherwise returns a new string formatted as '"<file_path>:<symbol>"'. [crates/gwiki/src/falkor_graph/code_edges.rs:279-285]
- `normalize_graph_path` (function) component `normalize_graph_path [function]` (`3066fff2-6ead-566f-a56b-e95deef1c12e`) lines 287-289 [crates/gwiki/src/falkor_graph/code_edges.rs:287-289]
  - Signature: `fn normalize_graph_path(path: &Path) -> String {`
  - Purpose: Converts a 'Path' to a lossily decoded 'String' and normalizes Windows separators by replacing all '\' characters with '/'. [crates/gwiki/src/falkor_graph/code_edges.rs:287-289]

