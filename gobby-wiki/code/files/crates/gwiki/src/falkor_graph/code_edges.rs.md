---
title: crates/gwiki/src/falkor_graph/code_edges.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph/code_edges.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/falkor_graph/code_edges.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/falkor_graph/code_edges.rs` exposes 15 indexed API symbols.

## How it fits

`crates/gwiki/src/falkor_graph/code_edges.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `LimitedCodeGraphEdges` | class | 'LimitedCodeGraphEdges' is a struct that encapsulates a vector of 'WikiGraphCodeEdge' objects with a boolean flag indicating whether the result set was truncated. [crates/gwiki/src/falkor_graph/code_edges.rs:18-21] |
| `load_code_graph_edges` | function | # Summary Loads code graph edges from a GraphClient for project documents, enforcing configurable per-component and cumulative edge limits while tracking truncation violations. [crates/gwiki/src/falkor_graph/code_edges.rs:23-114] |
| `code_call_edges` | function | Executes a parameterized graph query to retrieve code call edges for a specified file, maps results to WikiGraphCodeEdge objects with incoming/outgoing classification based on file path matching, and returns a truncated collection with an overflow indicator. [crates/gwiki/src/falkor_graph/code_edges.rs:116-157] |
| `code_call_edges_query` | function | This function returns a Neo4j Cypher query string that retrieves 'CALLS' relationships between 'CodeSymbol' nodes within a specified project, filtered by source or target file path, and ordered by file and line number. [crates/gwiki/src/falkor_graph/code_edges.rs:159-167] |
| `code_import_edges` | function | # Summary Retrieves code import edges from a GraphClient bounded by a limit, transforms the query results into WikiGraphCodeEdge structures with scope and document path metadata, and returns them wrapped in a LimitedCodeGraphEdges container with a truncation flag. [crates/gwiki/src/falkor_graph/code_edges.rs:169-205] |
| `code_import_edges_query` | function | # Summary Returns a static Cypher query string that retrieves 'IMPORTS' relationships between 'CodeFile' and 'CodeModule' nodes, projecting source file paths and target module names filtered by project and file path. [crates/gwiki/src/falkor_graph/code_edges.rs:207-213] |
| `code_edge_query_params` | function | Constructs a HashMap of URL query parameters by escaping the project ID and file path strings and converting a validated limit value to a string. [crates/gwiki/src/falkor_graph/code_edges.rs:215-231] |
| `sentinel_limit` | function | Safely increments the input limit by one using checked arithmetic, returning the incremented value or an 'anyhow::Error' if the operation would overflow. [crates/gwiki/src/falkor_graph/code_edges.rs:233-237] |
| `truncate_to_limit` | function | This function truncates a mutable vector to a specified size limit and returns a boolean indicating whether truncation was performed. [crates/gwiki/src/falkor_graph/code_edges.rs:239-245] |
| `remaining_code_edge_limit` | function | This function returns the minimum of a configured limit and remaining edges as 'Some(usize)' if edges remain, or 'None' if the remaining edge count is zero. [crates/gwiki/src/falkor_graph/code_edges.rs:247-252] |
| `record_code_edge_truncation` | function | This function records a code edge truncation component in a set, selecting either a total edge truncation component or a configured component-specific truncation based on whether the query limit is less than the configured limit. [crates/gwiki/src/falkor_graph/code_edges.rs:254-266] |
| `truncation_component` | function | This function returns a formatted 'String' that concatenates the input 'component' parameter with a ''>'' separator and the string representation of the 'limit' parameter. [crates/gwiki/src/falkor_graph/code_edges.rs:268-270] |
| `code_doc_source_path` | function | Normalizes a path and returns an owned 'String' containing the substring between the 'code/files/' prefix and '.md' suffix, or 'None' if either boundary is absent. [crates/gwiki/src/falkor_graph/code_edges.rs:272-277] |
| `code_endpoint` | function | This function constructs a code location reference by returning the file path as a String if the symbol is empty, otherwise concatenating the file path and symbol with a colon delimiter. [crates/gwiki/src/falkor_graph/code_edges.rs:279-285] |
| `normalize_graph_path` | function | Converts a filesystem path reference to a lossy UTF-8 string with all backslashes replaced by forward slashes. [crates/gwiki/src/falkor_graph/code_edges.rs:287-289] |

