---
title: crates/gwiki/src/code_graph.rs
type: code_file
provenance:
- file: crates/gwiki/src/code_graph.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/code_graph.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/code_graph.rs` exposes 30 indexed API symbols.

## How it fits

`crates/gwiki/src/code_graph.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CodeGraphQuery` | type | Indexed type `CodeGraphQuery` in `crates/gwiki/src/code_graph.rs`. [crates/gwiki/src/code_graph.rs:15-18] |
| `CodeGraphEdge` | class | 'CodeGraphEdge' is a crate-private struct representing a directed edge in a code graph with required source and target node identifiers and an edge-type classifier, supplemented by optional source location (file path and line number) and detail metadata. [crates/gwiki/src/code_graph.rs:21-28] |
| `CodeChangeSet` | class | 'CodeChangeSet' is a crate-private struct that encapsulates a set of code changes by aggregating affected file paths and modified code symbols as separate 'Vec<String>' collections. [crates/gwiki/src/code_graph.rs:31-34] |
| `AffectedPages` | class | # Summary 'AffectedPages' is a crate-private struct that aggregates a collection of 'AffectedPage' instances and associated 'DegradationKind' variants. [crates/gwiki/src/code_graph.rs:37-40] |
| `AffectedPage` | class | 'AffectedPage' is a crate-private struct that stores a page's file path along with associated source identifiers and source file paths. [crates/gwiki/src/code_graph.rs:43-47] |
| `code_edges` | function | Retrieves code graph edges for a specified project and query target, returning the matched edges along with service degradation status based on availability state. [crates/gwiki/src/code_graph.rs:49-68] |
| `affected_pages_for_changes` | function | Determines which pages are affected by code changes by traversing the provenance graph to identify transitive dependencies using project-specific code edge lookups. [crates/gwiki/src/code_graph.rs:70-79] |
| `affected_pages_for_changes_with_edges` | function | # Summary This function identifies all affected pages resulting from code changes by querying code graph edges for each modified file and symbol, aggregating the reachable dependencies using the provenance graph, and collecting associated code degradations. [crates/gwiki/src/code_graph.rs:81-124] |
| `add_edge_paths` | function | Populates a mutable BTreeSet by extracting and normalizing file paths from a collection of CodeGraphEdge objects. [crates/gwiki/src/code_graph.rs:126-132] |
| `affected_pages_for_targets` | function | Queries a provenance graph to identify pages affected by specified target sources, returning each affected page mapped to its contributing source identifiers and file paths. [crates/gwiki/src/code_graph.rs:134-162] |
| `normalized_path` | function | This function converts a trimmed string slice into an 'Option<PathBuf>', returning 'Some(PathBuf)' if the trimmed string is non-empty, otherwise 'None'. [crates/gwiki/src/code_graph.rs:164-167] |
| `normalized_source_id` | function | Returns 'Some(String)' containing the whitespace-trimmed input if non-empty, otherwise 'None'. [crates/gwiki/src/code_graph.rs:169-172] |
| `query_edges` | function | Queries a code graph with project-scoped parameters and returns a vector of CodeGraphEdge objects parsed and filtered from the result rows. [crates/gwiki/src/code_graph.rs:174-181] |
| `query_params` | function | Constructs a HashMap of query parameters containing the project name and conditional parameters (file_path or symbol_id) derived from a CodeGraphQuery variant. [crates/gwiki/src/code_graph.rs:183-194] |
| `edge_from_row` | function | Converts a database 'Row' into a 'CodeGraphEdge' by extracting required string fields ('edge', 'source', 'target') and optional metadata ('detail', 'file_path', 'line'), returning 'None' if any required field is absent. [crates/gwiki/src/code_graph.rs:196-208] |
| `required_row_string` | function | Retrieves a string value from a row by key and returns 'Some(value)' only if the value is non-empty after trimming whitespace; otherwise, logs a warning and returns 'None'. [crates/gwiki/src/code_graph.rs:210-220] |
| `degradation_key` | function | This function transforms a 'DegradationKind' enum variant into a colon-delimited string key that encodes the degradation type and its associated context metadata. [crates/gwiki/src/code_graph.rs:222-243] |
| `row_string` | function | This function retrieves a value from a Row by the given key and returns it as an owned String wrapped in Option if the value exists and is of string type, otherwise returns None. [crates/gwiki/src/code_graph.rs:245-249] |
| `row_i64` | function | This function retrieves a value from a 'Row' by string key and attempts to convert it to an 'i64', returning 'Some(i64)' on success or 'None' if the key is absent or the conversion fails. [crates/gwiki/src/code_graph.rs:251-253] |
| `graph_query` | function | This function dispatches to either 'file_graph_query()' or 'symbol_graph_query()' based on pattern matching the input 'CodeGraphQuery' enum variant and returns a 'String' result. [crates/gwiki/src/code_graph.rs:255-260] |
| `file_graph_query` | function | Constructs and returns a Neo4j Cypher query string that unions four parametrized subqueries to retrieve IMPORTS, DEFINES, CALLS, and CALLER relationships for a specified code file within a project dependency graph. [crates/gwiki/src/code_graph.rs:262-275] |
| `symbol_graph_query` | function | Returns a Cypher UNION ALL query string that retrieves all direct relationships for a specified code symbol, including its definitions, imports, outgoing function calls, and inbound callers from a code graph database. [crates/gwiki/src/code_graph.rs:277-291] |

_Verified by 8 in-file unit tests._

