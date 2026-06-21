---
title: crates/gcore/src/falkor.rs
type: code_file
provenance:
- file: crates/gcore/src/falkor.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/falkor.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/falkor.rs` exposes 31 indexed API symbols.

## How it fits

`crates/gcore/src/falkor.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Row` | type | Indexed type `Row` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:22] |
| `GraphClient` | class | GraphClient is a public struct that wraps a SyncGraph instance, serving as a client interface for synchronized graph operations. [crates/gcore/src/falkor.rs:28-30] |
| `ReadOnlySyncGraph` | class | 'ReadOnlySyncGraph<'a>' is a lifetime-generic wrapper struct that provides read-only access to a 'SyncGraph' through a held mutable reference bounded by lifetime ''a'. [crates/gcore/src/falkor.rs:36-38] |
| `graph_name` | function | This method returns an immutable string slice ('&str') by delegating to the 'graph_name()' method of the contained graph field. [crates/gcore/src/falkor.rs:42-44] |
| `ro_query` | function | Delegates a read-only query string to the underlying graph and returns a 'QueryBuilder' for constructing a lazy, evaluated query result. [crates/gcore/src/falkor.rs:47-52] |
| `GraphClient::from_config` | method | Builds a Falkor database client from configuration parameters by constructing a URL-encoded connection string and selecting the specified graph. [crates/gcore/src/falkor.rs:57-72] |
| `GraphClient::with_sync_graph` | method | # Summary Executes a provided closure with mutable access to the internal graph wrapped in a 'ReadOnlySyncGraph' type, returning the closure's result. [crates/gcore/src/falkor.rs:79-87] |
| `GraphClient::query` | method | This method executes a Cypher query against a graph database with optional string-valued parameters and returns the parsed result as a 'Vec<Row>'. [crates/gcore/src/falkor.rs:90-105] |
| `GraphClient::ensure_exact_node_index` | method | Idempotently creates a database index on a labeled node property by executing a CREATE INDEX Cypher statement, suppressing duplicate-index errors. [crates/gcore/src/falkor.rs:108-126] |
| `with_graph` | function | Initializes a GraphClient from the provided optional FalkorConfig and executes a closure with mutable access to it, returning the closure's result paired with ServiceState. [crates/gcore/src/falkor.rs:136-143] |
| `with_graph_client` | function | Attempts to instantiate a FalkorDB graph client from an optional configuration, executes a provided closure against it, and returns the result paired with a ServiceState indicating success, missing configuration, or connection failure—or falls back to a default value. [crates/gcore/src/falkor.rs:145-172] |
| `escape_label` | function | This function escapes a label string by delegating to the 'escape_identifier' function and returning the escaped result as an owned 'String'. [crates/gcore/src/falkor.rs:175-177] |
| `escape_rel_type` | function | Escapes a relation type identifier string by delegating to the 'escape_identifier' function and returning the sanitized result. [crates/gcore/src/falkor.rs:180-182] |
| `escape_property` | function | This function escapes a property key by delegating to the 'escape_identifier' function, accepting a string reference and returning an owned String. [crates/gcore/src/falkor.rs:185-187] |
| `escape_string` | function | This function escapes backslashes and single quotes in a string by doubling backslashes and prefixing single quotes with backslashes, then returns the result wrapped in single quotes. [crates/gcore/src/falkor.rs:195-198] |
| `escape_identifier` | function | The function escapes a string value for SQL identifiers by doubling all single quotes and wrapping the result in single quotes. [crates/gcore/src/falkor.rs:200-202] |
| `is_existing_index_error` | function | This function returns 'true' if the provided error message matches any predefined patterns indicating a FalkorDB duplicate-index creation error, with fallback debug logging for unmatched index-related errors. [crates/gcore/src/falkor.rs:207-220] |
| `parse_falkor_result` | function | Converts a 'QueryResult<LazyResultSet>' into a 'Vec<Row>' by delegating to 'parse_falkor_records' with its header and data components. [crates/gcore/src/falkor.rs:222-224] |
| `parse_falkor_records` | function | Transforms an iterator of FalkorValue vectors into a vector of HashMaps by associating each value with its corresponding header name and converting values to JSON format. [crates/gcore/src/falkor.rs:226-241] |
| `falkor_value_to_json` | function | Recursively converts a 'FalkorValue' enum to a JSON 'Value' type through pattern matching, mapping primitive types directly while recursively transforming nested arrays and maps, with unmatched variants falling back to debug string representation. [crates/gcore/src/falkor.rs:243-266] |
| `FakeGraphClient` | class | FakeGraphClient is an empty unit-like Rust struct designed to serve as a mock or test double for graph client functionality. [crates/gcore/src/falkor.rs:275] |
| `test_config` | function | This function returns a 'FalkorConfig' instance initialized with localhost (127.0.0.1), port 1, and no password authentication. [crates/gcore/src/falkor.rs:277-283] |
| `live_falkor_fixture` | function | Returns an 'Option' containing a 'FalkorConfig' and graph name string built from environment variables (GOBBY_FALKORDB_HOST required, GOBBY_FALKORDB_PORT defaulting to 16379, GOBBY_FALKORDB_PASSWORD optional if non-empty, GOBBY_FALKORDB_TEST_GRAPH defaulting to "gobby_core_live_test"), or 'None' if the required HOST variable is absent. [crates/gcore/src/falkor.rs:443-462] |

_Verified by 8 in-file unit tests._

