---
title: crates/gcore/src/qdrant.rs
type: code_file
provenance:
- file: crates/gcore/src/qdrant.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/qdrant.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/qdrant.rs` exposes 30 indexed API symbols.

## How it fits

`crates/gcore/src/qdrant.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `QdrantError` | type | Indexed type `QdrantError` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:20-36] |
| `http_status_context` | function | Returns a context suffix string that conditionally includes the collection name and/or request label in the form ' for collection '...' during '...'', ' for collection '...'', ' during '...'', or an empty string when both inputs are 'None'. [crates/gcore/src/qdrant.rs:38-47] |
| `VectorCollectionSchema` | class | 'VectorCollectionSchema' is a Rust struct representing a vector collection schema with a 'size' field of type 'usize' and a 'distance' field of type 'String'. [crates/gcore/src/qdrant.rs:50-53] |
| `ExistingVectorCollectionSchema` | class | 'ExistingVectorCollectionSchema' is a schema container for an existing vector collection that optionally specifies the vector dimensionality ('size: Option<usize>') and the distance metric identifier ('distance: Option<String>'). [crates/gcore/src/qdrant.rs:56-59] |
| `UpsertRequest` | class | 'UpsertRequest' is a data-carrying request struct for inserting or updating a record, containing an 'id: String', an embedding 'vector: Vec<f32>', and an arbitrary JSON-like 'payload: Map<String, Value>'. [crates/gcore/src/qdrant.rs:63-67] |
| `UpsertResult` | class | 'UpsertResult' is a struct containing an optional 'u64' 'operation_id' and a 'String' 'status' describing the outcome of an upsert operation. [crates/gcore/src/qdrant.rs:70-73] |
| `SearchRequest` | class | 'SearchRequest' is a request payload containing a query embedding vector ('Vec<f32>'), a result count limit ('usize'), and an optional JSON filter ('Option<Value>') to constrain the search. [crates/gcore/src/qdrant.rs:77-81] |
| `SearchHit` | class | 'SearchHit' is a struct representing a search result entry with a string 'id', a floating-point relevance 'score', and an arbitrary JSON-like 'payload' stored as a 'Map<String, Value>'. [crates/gcore/src/qdrant.rs:85-89] |
| `with_qdrant` | function | 'with_qdrant' conditionally executes a closure with a configured Qdrant config and returns either its result marked 'Available', a provided default marked 'NotConfigured' or 'Unreachable' when Qdrant is absent or unreachable, or propagates any other error. [crates/gcore/src/qdrant.rs:92-114] |
| `search` | function | Sends a blocking POST search request to a Qdrant collection’s '/points/search' endpoint with the query vector, limit, filter, and 'with_payload=true', optionally authenticates with an API key, converts non-success HTTP responses into a 'QdrantError::HttpStatus', and returns the parsed 'result' array as 'Vec<SearchHit>'. [crates/gcore/src/qdrant.rs:117-173] |
| `ensure_collection` | function | Checks whether a Qdrant collection exists, verifies any existing schema is compatible with the expected 'VectorCollectionSchema', returns a schema with missing 'size' or 'distance' filled from the expected values, or creates the collection and returns the expected schema if it is absent. [crates/gcore/src/qdrant.rs:176-194] |
| `collection_schema` | function | Performs a GET request for the named Qdrant collection, returns 'Ok(None)' if it is missing ('404'), otherwise parses the successful JSON response into an 'ExistingVectorCollectionSchema' and wraps it in 'Some', propagating HTTP or parsing errors. [crates/gcore/src/qdrant.rs:197-219] |
| `collection_point_count` | function | Sends a 'GET' request to the Qdrant collection endpoint and returns 'Ok(Some(count))' by parsing the collection’s point count from the JSON response, 'Ok(None)' on '404 Not Found', or an error for any other non-success status or request/parse failure. [crates/gcore/src/qdrant.rs:222-244] |
| `delete_points_by_filter` | function | Sends a synchronous 'POST' to Qdrant’s '/{collection}/points/delete?wait=true' with a JSON 'filter', treats '404 Not Found' as a no-op, and otherwise returns an error unless the response contains 'result.status == "completed"'. [crates/gcore/src/qdrant.rs:247-306] |
| `create_collection` | function | Creates a Qdrant collection by issuing a 'PUT' request to the collection endpoint with the vector size and distance from 'schema', then returns an error if the HTTP response status is not successful. [crates/gcore/src/qdrant.rs:308-334] |
| `upsert` | function | Performs a blocking HTTP 'PUT' to Qdrant’s '/collections/{collection}/points?wait=true' endpoint to upsert a batch of points, optionally authenticating with 'api-key', then returns the parsed 'UpsertResult' only if the HTTP response is successful and the operation status is 'completed'. [crates/gcore/src/qdrant.rs:337-399] |
| `upsert_batched` | function | 'upsert_batched' forwards the provided points to 'upsert_batched_with_size' using 'DEFAULT_UPSERT_BATCH_SIZE' and returns the resulting 'anyhow::Result<usize>' upsert count. [crates/gcore/src/qdrant.rs:401-407] |
| `upsert_batched_with_size` | function | Upserts the given 'UpsertRequest' points into the specified Qdrant collection in fixed-size batches of at least one item, returning the total number of requested points processed and short-circuiting to '0' when the input is empty. [crates/gcore/src/qdrant.rs:409-433] |
| `parse_upsert_result` | function | Extracts 'result.status' as a required string and 'result.operation_id' as an optional 'u64' from a Qdrant upsert response 'Value', returning an 'UpsertResult' or an error if the 'result' object or status field is missing. [crates/gcore/src/qdrant.rs:435-449] |
| `parse_search_hit` | function | Parses a JSON 'hit' object into a 'SearchHit' by extracting and validating 'id' via 'parse_point_id', reading 'score' as an 'f64' cast to 'f32', cloning the 'payload' object if present or using an empty map, and returning 'None' on any missing or invalid field. [crates/gcore/src/qdrant.rs:451-461] |
| `parse_point_id` | function | Returns a cloned 'String' representation of the input 'Value' when it is a string or number, and 'None' for all other variants. [crates/gcore/src/qdrant.rs:463-469] |
| `parse_collection_schema` | function | 'parse_collection_schema' reads '/result/config/params/vectors' from a JSON 'Value' and returns an 'ExistingVectorCollectionSchema' with 'size' parsed as an optional 'usize' from 'vectors.size' and 'distance' parsed as an optional 'String' from 'vectors.distance'. [crates/gcore/src/qdrant.rs:471-482] |
| `parse_collection_point_count` | function | Returns the 'u64' value at '/result/points_count' if present, otherwise falls back to '/result/vectors_count', and returns 'None' if neither exists or is an unsigned integer. [crates/gcore/src/qdrant.rs:484-491] |
| `ensure_compatible_collection` | function | Checks that an existing Qdrant collection matches the expected vector dimension and distance metric, and returns an error if either differs. [crates/gcore/src/qdrant.rs:493-510] |
| `is_qdrant_unreachable` | function | Returns 'true' if any error in the chain is either a 'reqwest::Error' marked as a connection or timeout failure, or a 'QdrantError::HttpStatus' with a 5xx server error status, indicating Qdrant is unreachable. [crates/gcore/src/qdrant.rs:512-524] |
| `encoded_collection` | function | Returns a percent-encoded 'String' representation of 'collection' by URL-encoding the input and converting the result into an owned string. [crates/gcore/src/qdrant.rs:526-528] |
| `collection_request_path` | function | Returns the request path for a collection by formatting '"/collections/{encoded_collection(collection)}"' into a 'String'. [crates/gcore/src/qdrant.rs:530-532] |
| `qdrant_request` | function | Builds a blocking 'reqwest' request to 'config.url + path' with a fixed timeout, adds an 'api-key' header when 'config.api_key' is present, and returns an error if the Qdrant URL is unset. [crates/gcore/src/qdrant.rs:534-552] |
| `qdrant_http_error` | function | Builds an 'anyhow::Error' wrapping a 'QdrantError::HttpStatus' by consuming an HTTP response, extracting its body text or a read-failure placeholder, and attaching the operation, status code, collection name, and request method/path. [crates/gcore/src/qdrant.rs:554-572] |
| `operation_method` | function | Maps an operation name string to an HTTP method string, returning 'GET' for '"get collection"', 'PUT' for '"create collection"' and '"upsert"', 'POST' for '"delete points"' and '"search"', and 'POST' for any unrecognized operation. [crates/gcore/src/qdrant.rs:574-583] |

