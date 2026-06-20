---
title: crates/gcode/src/vector/code_symbols/qdrant.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/qdrant.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols/qdrant.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Overview

`crates/gcode/src/vector/code_symbols/qdrant.rs` exposes 23 indexed API symbols.

## How it fits

`crates/gcode/src/vector/code_symbols/qdrant.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `VectorOrphanCleanup` | class | 'VectorOrphanCleanup' is a summary struct that records the project and collection being processed plus counts of vector files scanned, orphan files deleted, and vectors deleted during cleanup. [crates/gcode/src/vector/code_symbols/qdrant.rs:21-27] |
| `collection_name` | function | Builds a custom Qdrant collection name by concatenating 'collection_prefix' and 'project_id', then delegates to 'gobby_core::qdrant::collection_name("gcode", CollectionScope::Custom(&collection))' to return a validated 'Result<String, CollectionNameError>'. [crates/gcode/src/vector/code_symbols/qdrant.rs:29-35] |
| `collection_path` | function | Returns the URL path for a collection by prefixing '/collections/' to the URL-encoded 'collection' string. [crates/gcode/src/vector/code_symbols/qdrant.rs:37-39] |
| `delete_project_collection` | function | Creates a Qdrant HTTP client, derives the code-symbol collection name for the given 'project_id', and deletes that collection via 'delete_qdrant_collection', returning the number of deleted items or a 'VectorLifecycleError'. [crates/gcode/src/vector/code_symbols/qdrant.rs:41-48] |
| `delete_file_vectors` | function | Creates a Qdrant HTTP client, derives the project-specific code-symbol collection name, and deletes all vectors for the given 'file_path' filter in that collection, returning the number deleted or a 'VectorLifecycleError'. [crates/gcode/src/vector/code_symbols/qdrant.rs:50-58] |
| `cleanup_orphan_file_vectors` | function | Scans all vector-backed file paths for a project, deletes vectors for any path not present in 'indexed_file_paths', and returns a 'VectorOrphanCleanup' report with scan, deletion, and collection metadata. [crates/gcode/src/vector/code_symbols/qdrant.rs:60-85] |
| `list_project_vector_file_paths` | function | Scans the Qdrant code-symbol collection for the given 'project_id' via paginated 'points/scroll' requests, extracts all non-null 'file_path' payload values into a 'BTreeSet', and returns them or a 'VectorLifecycleError' on failure. [crates/gcode/src/vector/code_symbols/qdrant.rs:87-143] |
| `collect_file_paths_from_scroll_page` | function | Parses a Qdrant scroll response, extracts each point’s 'payload.file_path' string from 'result.points', inserts the paths into a 'BTreeSet', and returns an error if 'result.points' is missing or not an array. [crates/gcode/src/vector/code_symbols/qdrant.rs:145-163] |
| `delete_code_symbol_collections_with_prefix` | function | Lists Qdrant collections, filters names by 'CODE_SYMBOL_COLLECTION_PREFIX', deletes each matching collection, and returns the names of those successfully removed. [crates/gcode/src/vector/code_symbols/qdrant.rs:165-192] |
| `vector_search` | function | Executes a Qdrant vector similarity search for the given collection and query embedding with the specified limit, logs any degradation warning from the Qdrant state, and returns the matching hit IDs with their scores converted to 'f64'. [crates/gcode/src/vector/code_symbols/qdrant.rs:194-215] |
| `vector_search_degradation_warning` | function | Returns 'None' when the service is 'Available', otherwise returns a warning string indicating semantic vector search was skipped because Qdrant is either not configured or unreachable, including the unreachable error message when present. [crates/gcode/src/vector/code_symbols/qdrant.rs:217-227] |
| `parse_collection_schema` | function | Extracts '/result/config/params/vectors' from a JSON 'Value' and, if present, returns an 'ExistingVectorCollectionSchema' with an optional 'usize' 'size' parsed from 'vectors.size' and an optional 'String' 'distance' parsed from 'vectors.distance'. [crates/gcode/src/vector/code_symbols/qdrant.rs:229-240] |
| `parse_collection_names` | function | Returns a 'Vec<String>' of all '"name"' string fields found under '/result/collections' in the input JSON 'Value', or an empty vector if that path is missing or not an array. [crates/gcode/src/vector/code_symbols/qdrant.rs:242-257] |
| `parse_points_count` | function | Extracts 'result.count' from a JSON 'Value', converts it to 'usize', and returns a 'QdrantOperation' error if the field is missing or not a valid unsigned integer. [crates/gcode/src/vector/code_symbols/qdrant.rs:259-268] |
| `qdrant_http_client` | function | Returns a cached global 'reqwest::blocking::Client' for Qdrant if already initialized, otherwise builds one with 'qdrant_delete_timeout()', maps any build error into 'VectorLifecycleError::QdrantOperation', stores the client in 'QDRANT_HTTP_CLIENT', and returns it. [crates/gcode/src/vector/code_symbols/qdrant.rs:270-280] |
| `qdrant_delete_timeout` | function | Returns a 'Duration' for Qdrant delete operations by reading 'QDRANT_DELETE_TIMEOUT_SECS_ENV' as a positive 'u64' number of seconds and falling back to 'DEFAULT_QDRANT_DELETE_TIMEOUT' if the variable is unset, invalid, or non-positive. [crates/gcode/src/vector/code_symbols/qdrant.rs:282-289] |
| `qdrant_request_for_config` | function | Builds a 'reqwest::blocking::RequestBuilder' for a Qdrant endpoint by validating and trimming the configured base URL, concatenating it with the given path, and conditionally adding the 'api-key' header, or returns 'MissingQdrantConfig' if no non-empty URL is set. [crates/gcode/src/vector/code_symbols/qdrant.rs:291-310] |
| `delete_qdrant_collection` | function | Sends an HTTP 'DELETE' request to the Qdrant collection endpoint and returns 'Ok(0)' if the collection is missing ('404'), 'Ok(1)' on any successful deletion response, or a 'VectorLifecycleError' for request/HTTP failures. [crates/gcode/src/vector/code_symbols/qdrant.rs:312-333] |
| `delete_vectors_for_filter` | function | 'delete_vectors_for_filter' deletes all vectors matching the given collection, project ID, and optional file path filter by delegating to 'delete_vectors_for_filter_excluding_ids' with an empty exclusion list, returning the number deleted or a 'VectorLifecycleError'. [crates/gcode/src/vector/code_symbols/qdrant.rs:335-343] |
| `delete_vectors_for_filter_excluding_ids` | function | Deletes Qdrant points in the specified collection that match 'project_id' and optional 'file_path' while excluding 'keep_point_ids', first counting matches to return '0' for missing/empty sets, then issuing a 'wait=true' delete request and returning the number of deleted vectors. [crates/gcode/src/vector/code_symbols/qdrant.rs:345-415] |
| `qdrant_http_error` | function | Constructs a 'VectorLifecycleError::QdrantHttp' from a failed Qdrant HTTP response by recording the operation name, numeric HTTP status code, and response body text. [crates/gcode/src/vector/code_symbols/qdrant.rs:417-427] |

_Verified by 2 in-file unit tests._

