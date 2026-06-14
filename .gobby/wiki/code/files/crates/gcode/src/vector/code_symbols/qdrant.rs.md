---
title: crates/gcode/src/vector/code_symbols/qdrant.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/qdrant.rs
  ranges:
  - 18-24
  - 26-28
  - 30-37
  - 39-47
  - 49-76
  - 78-99
  - 101-111
  - 113-124
  - 126-141
  - 143-152
  - 154-164
  - 166-173
  - 175-194
  - 196-217
  - 219-227
  - 229-299
  - 301-311
  - 318-323
  - 326-336
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols/qdrant.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

This file is the Qdrant integration layer for gcode’s code-symbol vectors. It standardizes collection naming and paths, builds and caches a blocking Qdrant HTTP client from config, and constructs requests against the configured Qdrant base URL and API key. On top of that, it implements the main lifecycle operations: deleting an entire project collection, deleting vectors for a specific file or filter, and removing all code-symbol collections with the configured prefix. It also provides vector search by translating a query vector into a Qdrant search request, then converting results and surfacing a degradation warning when Qdrant is unavailable or unconfigured. The parsing helpers extract collection schemas, collection names, and point counts from Qdrant JSON responses, while the error helper turns failed HTTP responses into `VectorLifecycleError` values. The tests verify the user-facing degradation messages for missing and unreachable Qdrant.
[crates/gcode/src/vector/code_symbols/qdrant.rs:18-24]
[crates/gcode/src/vector/code_symbols/qdrant.rs:26-28]
[crates/gcode/src/vector/code_symbols/qdrant.rs:30-37]
[crates/gcode/src/vector/code_symbols/qdrant.rs:39-47]
[crates/gcode/src/vector/code_symbols/qdrant.rs:49-76]

## API Symbols

- `collection_name` (function) component `collection_name [function]` (`753537a7-c2e6-552d-b8ef-08f7def1f99b`) lines 18-24 [crates/gcode/src/vector/code_symbols/qdrant.rs:18-24]
  - Signature: `pub fn collection_name(`
  - Purpose: Builds a custom Qdrant collection name by concatenating `collection_prefix` and `project_id`, then validating/normalizing it via `gobby_core::qdrant::collection_name("gcode", CollectionScope::Custom(&collection))`. [crates/gcode/src/vector/code_symbols/qdrant.rs:18-24]
- `collection_path` (function) component `collection_path [function]` (`d1f6ab42-05ef-5849-b9c8-27615e3b516b`) lines 26-28 [crates/gcode/src/vector/code_symbols/qdrant.rs:26-28]
  - Signature: `pub(super) fn collection_path(collection: &str) -> String {`
  - Purpose: Returns a `String` path in the form `/collections/{url-encoded collection}` by URL-encoding `collection` and prefixing it with `/collections/`. [crates/gcode/src/vector/code_symbols/qdrant.rs:26-28]
- `delete_project_collection` (function) component `delete_project_collection [function]` (`cfd613b1-9447-5b9e-9dfe-c63f66e3f148`) lines 30-37 [crates/gcode/src/vector/code_symbols/qdrant.rs:30-37]
  - Signature: `pub fn delete_project_collection(`
  - Purpose: Creates a Qdrant HTTP client, derives the project’s code-symbol collection name from `CODE_SYMBOL_COLLECTION_PREFIX` and `project_id`, and delegates deletion to `delete_qdrant_collection`, returning its `Result<usize, VectorLifecycleError>`. [crates/gcode/src/vector/code_symbols/qdrant.rs:30-37]
- `delete_file_vectors` (function) component `delete_file_vectors [function]` (`207703c8-c51f-58dc-a2dd-7cecf74d1cfc`) lines 39-47 [crates/gcode/src/vector/code_symbols/qdrant.rs:39-47]
  - Signature: `pub fn delete_file_vectors(`
  - Purpose: Creates a Qdrant HTTP client, resolves the project’s code-symbol collection name, and deletes all vectors matching the given `project_id` and `file_path`, returning the number removed or a `VectorLifecycleError`. [crates/gcode/src/vector/code_symbols/qdrant.rs:39-47]
- `delete_code_symbol_collections_with_prefix` (function) component `delete_code_symbol_collections_with_prefix [function]` (`576b7d03-3244-54a6-ad82-ad63d740b15c`) lines 49-76 [crates/gcode/src/vector/code_symbols/qdrant.rs:49-76]
  - Signature: `pub fn delete_code_symbol_collections_with_prefix(`
  - Purpose: Fetches all Qdrant collections, filters those whose names start with `CODE_SYMBOL_COLLECTION_PREFIX`, deletes each matching collection, and returns the names of the collections that were successfully deleted. [crates/gcode/src/vector/code_symbols/qdrant.rs:49-76]
- `vector_search` (function) component `vector_search [function]` (`70028223-97ec-5788-a29d-3fd6171deeea`) lines 78-99 [crates/gcode/src/vector/code_symbols/qdrant.rs:78-99]
  - Signature: `pub fn vector_search(`
  - Purpose: Builds a Qdrant `SearchRequest` from the provided query vector and limit, executes it against the given collection via `with_qdrant`, logs any degradation warning from the search state, and returns the hits as `(id, score)` pairs with scores converted to `f64`. [crates/gcode/src/vector/code_symbols/qdrant.rs:78-99]
- `vector_search_degradation_warning` (function) component `vector_search_degradation_warning [function]` (`7f84e19d-1d90-5085-8761-c055f88fa761`) lines 101-111 [crates/gcode/src/vector/code_symbols/qdrant.rs:101-111]
  - Signature: `fn vector_search_degradation_warning(state: &ServiceState) -> Option<String> {`
  - Purpose: Returns `None` when vector search is available, otherwise returns a human-readable warning explaining that semantic vector search was skipped because Qdrant is either not configured or unreachable, including the unreachable message when present. [crates/gcode/src/vector/code_symbols/qdrant.rs:101-111]
- `parse_collection_schema` (function) component `parse_collection_schema [function]` (`0a0b99d3-cc8b-56ca-a68b-3ad40cfcefcb`) lines 113-124 [crates/gcode/src/vector/code_symbols/qdrant.rs:113-124]
  - Signature: `pub(super) fn parse_collection_schema(data: &Value) -> Option<ExistingVectorCollectionSchema> {`
  - Purpose: It looks up `/result/config/params/vectors` in the JSON value and, if found, returns an `ExistingVectorCollectionSchema` containing an optional `usize` `size` and optional `distance` string, otherwise `None`. [crates/gcode/src/vector/code_symbols/qdrant.rs:113-124]
- `parse_collection_names` (function) component `parse_collection_names [function]` (`52077fa3-0b70-5755-99e7-875ea2992569`) lines 126-141 [crates/gcode/src/vector/code_symbols/qdrant.rs:126-141]
  - Signature: `fn parse_collection_names(data: &Value) -> Vec<String> {`
  - Purpose: Returns a `Vec<String>` of collection names by reading `data["result"]["collections"]` as an array and collecting each element’s `"name"` string, or `[]` if the path is missing or invalid. [crates/gcode/src/vector/code_symbols/qdrant.rs:126-141]
- `parse_points_count` (function) component `parse_points_count [function]` (`6e0290ce-9997-5d73-988f-9d8cccd380c7`) lines 143-152 [crates/gcode/src/vector/code_symbols/qdrant.rs:143-152]
  - Signature: `fn parse_points_count(data: &Value) -> Result<usize, VectorLifecycleError> {`
  - Purpose: It reads `data["result"]["count"]` as a `u64`, converts it to `usize`, and returns a `VectorLifecycleError::QdrantOperation` if the field is missing, not an unsigned integer, or does not fit in `usize`. [crates/gcode/src/vector/code_symbols/qdrant.rs:143-152]
- `qdrant_http_client` (function) component `qdrant_http_client [function]` (`f9ba033c-f3c6-5bc3-8b1f-e7b40ad825f4`) lines 154-164 [crates/gcode/src/vector/code_symbols/qdrant.rs:154-164]
  - Signature: `fn qdrant_http_client() -> Result<reqwest::blocking::Client, VectorLifecycleError> {`
  - Purpose: Returns a cached global `reqwest::blocking::Client` for Qdrant HTTP calls if available, otherwise builds one with `qdrant_delete_timeout()`, stores it in `QDRANT_HTTP_CLIENT`, and converts build errors into `VectorLifecycleError::QdrantOperation`. [crates/gcode/src/vector/code_symbols/qdrant.rs:154-164]
- `qdrant_delete_timeout` (function) component `qdrant_delete_timeout [function]` (`800cebd9-b264-52cb-bd2f-e261d8cb5242`) lines 166-173 [crates/gcode/src/vector/code_symbols/qdrant.rs:166-173]
  - Signature: `fn qdrant_delete_timeout() -> Duration {`
  - Purpose: Returns a `Duration` built from the positive `u64` value of `QDRANT_DELETE_TIMEOUT_SECS_ENV` if it is set and parseable, otherwise falls back to `DEFAULT_QDRANT_DELETE_TIMEOUT`. [crates/gcode/src/vector/code_symbols/qdrant.rs:166-173]
- `qdrant_request_for_config` (function) component `qdrant_request_for_config [function]` (`7f9161ad-3ab2-5577-8ac0-3562563d9937`) lines 175-194 [crates/gcode/src/vector/code_symbols/qdrant.rs:175-194]
  - Signature: `pub(super) fn qdrant_request_for_config(`
  - Purpose: Builds a `reqwest::blocking::RequestBuilder` for a Qdrant endpoint by requiring a non-empty trimmed base URL from `QdrantConfig`, stripping any trailing slash, appending the provided `path`, and conditionally adding the `api-key` header, or returning `VectorLifecycleError::MissingQdrantConfig` if the URL is absent. [crates/gcode/src/vector/code_symbols/qdrant.rs:175-194]
- `delete_qdrant_collection` (function) component `delete_qdrant_collection [function]` (`0e7c1d57-7114-50e2-84a9-1682d3a28e18`) lines 196-217 [crates/gcode/src/vector/code_symbols/qdrant.rs:196-217]
  - Signature: `fn delete_qdrant_collection(`
  - Purpose: Sends a blocking `DELETE` request to the Qdrant collection endpoint and returns `Ok(0)` if the collection does not exist, `Ok(1)` on successful deletion, or a `VectorLifecycleError` on request or HTTP failure. [crates/gcode/src/vector/code_symbols/qdrant.rs:196-217]
- `delete_vectors_for_filter` (function) component `delete_vectors_for_filter [function]` (`ec0b0c90-cf56-5a49-bea0-b8c2fabb962a`) lines 219-227 [crates/gcode/src/vector/code_symbols/qdrant.rs:219-227]
  - Signature: `pub(super) fn delete_vectors_for_filter(`
  - Purpose: Calls `delete_vectors_for_filter_excluding_ids` with an empty excluded-ID list to delete all vectors in `collection` matching the given `project_id` and optional `file_path`, returning the deleted count. [crates/gcode/src/vector/code_symbols/qdrant.rs:219-227]
- `delete_vectors_for_filter_excluding_ids` (function) component `delete_vectors_for_filter_excluding_ids [function]` (`f7191d77-0ad0-5a2d-bcd0-12dc369404b0`) lines 229-299 [crates/gcode/src/vector/code_symbols/qdrant.rs:229-299]
  - Signature: `pub(super) fn delete_vectors_for_filter_excluding_ids(`
  - Purpose: I’m checking the full function body so the summary matches its exact Qdrant delete/count behavior, not just the partial snippet.The first search didn’t hit the file, so I’m broadening the lookup to the whole repo to confirm the tail of the function.It builds an exact Qdrant filter for a given `project_id` and optional `file_path`, excludes any IDs in `keep_point_ids`, counts the matching points, and if any exist issues a synchronous `points/delete?wait=true` request, returning `0` when nothing matches or the collection is missing. [crates/gcode/src/vector/code_symbols/qdrant.rs:229-299]
- `qdrant_http_error` (function) component `qdrant_http_error [function]` (`d35c16dd-7eb0-5a67-b10f-6ae70cac681b`) lines 301-311 [crates/gcode/src/vector/code_symbols/qdrant.rs:301-311]
  - Signature: `pub(super) fn qdrant_http_error(`
  - Purpose: Creates a `VectorLifecycleError::QdrantHttp` that captures the operation name, HTTP status code as `u16`, and the response body text from a blocking `reqwest` response, defaulting to an empty body if reading fails. [crates/gcode/src/vector/code_symbols/qdrant.rs:301-311]
- `vector_search_degradation_warning_mentions_missing_qdrant_config` (function) component `vector_search_degradation_warning_mentions_missing_qdrant_config [function]` (`73c68735-f143-51ac-88e4-f972c8e48dff`) lines 318-323 [crates/gcode/src/vector/code_symbols/qdrant.rs:318-323]
  - Signature: `fn vector_search_degradation_warning_mentions_missing_qdrant_config() {`
  - Purpose: Verifies that `vector_search_degradation_warning` returns `Some("semantic vector search skipped: Qdrant is not configured")` when passed `ServiceState::NotConfigured`. [crates/gcode/src/vector/code_symbols/qdrant.rs:318-323]
- `vector_search_degradation_warning_mentions_unreachable_qdrant` (function) component `vector_search_degradation_warning_mentions_unreachable_qdrant [function]` (`ec0952ba-dfaa-5357-83f0-dddd5c7283cb`) lines 326-336 [crates/gcode/src/vector/code_symbols/qdrant.rs:326-336]
  - Signature: `fn vector_search_degradation_warning_mentions_unreachable_qdrant() {`
  - Purpose: This test asserts that `vector_search_degradation_warning` returns `Some("semantic vector search skipped: Qdrant is unreachable: connection refused")` when passed `ServiceState::Unreachable { message: "connection refused" }`. [crates/gcode/src/vector/code_symbols/qdrant.rs:326-336]

