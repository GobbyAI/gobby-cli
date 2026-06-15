---
title: crates/gcode/src/vector/code_symbols/qdrant.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/qdrant.rs
  ranges:
  - 21-27
  - 29-35
  - 37-39
  - 41-48
  - 50-58
  - 60-85
  - 87-143
  - 145-163
  - 165-192
  - 194-215
  - 217-227
  - 229-240
  - 242-257
  - 259-268
  - 270-280
  - 282-289
  - 291-310
  - 312-333
  - 335-343
  - 345-415
  - 417-427
  - 434-439
  - 442-452
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols/qdrant.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

This file is the Qdrant integration layer for code-symbol vectors: it defines the project-specific collection naming and path helpers, configures and caches a blocking HTTP client, and provides delete/search/cleanup operations for project collections and file-scoped vectors. Its support functions parse Qdrant JSON responses, build requests and error values, and the test helpers verify the degradation warnings for missing or unreachable Qdrant.
[crates/gcode/src/vector/code_symbols/qdrant.rs:21-27]
[crates/gcode/src/vector/code_symbols/qdrant.rs:29-35]
[crates/gcode/src/vector/code_symbols/qdrant.rs:37-39]
[crates/gcode/src/vector/code_symbols/qdrant.rs:41-48]
[crates/gcode/src/vector/code_symbols/qdrant.rs:50-58]

## API Symbols

- `VectorOrphanCleanup` (class) component `VectorOrphanCleanup [class]` (`ead3513c-5a8d-5e3b-b007-5c58b90cbf24`) lines 21-27 [crates/gcode/src/vector/code_symbols/qdrant.rs:21-27]
  - Signature: `pub struct VectorOrphanCleanup {`
  - Purpose: 'VectorOrphanCleanup' is a record of a cleanup run that identifies and removes orphaned vector files for a specific project collection, tracking the project and collection identifiers plus counts of scanned vector files, deleted orphan files, and deleted vectors. [crates/gcode/src/vector/code_symbols/qdrant.rs:21-27]
- `collection_name` (function) component `collection_name [function]` (`e84efa11-2d2f-59c6-8703-1e73819a2c05`) lines 29-35 [crates/gcode/src/vector/code_symbols/qdrant.rs:29-35]
  - Signature: `pub fn collection_name(`
  - Purpose: Builds a custom Qdrant collection name by concatenating 'collection_prefix' and 'project_id', then passes it with the '"gcode"' namespace to 'gobby_core::qdrant::collection_name', returning the resulting 'Result<String, CollectionNameError>'. [crates/gcode/src/vector/code_symbols/qdrant.rs:29-35]
- `collection_path` (function) component `collection_path [function]` (`9dca0307-94e2-5528-abf8-4a118c21f1bc`) lines 37-39 [crates/gcode/src/vector/code_symbols/qdrant.rs:37-39]
  - Signature: `pub(super) fn collection_path(collection: &str) -> String {`
  - Purpose: Returns the '/collections/' URL path for a collection name by percent-encoding 'collection' with 'urlencoding::encode' and concatenating it into a 'String'. [crates/gcode/src/vector/code_symbols/qdrant.rs:37-39]
- `delete_project_collection` (function) component `delete_project_collection [function]` (`7ecb9909-1269-5525-bf65-5fc9ce9e0c89`) lines 41-48 [crates/gcode/src/vector/code_symbols/qdrant.rs:41-48]
  - Signature: `pub fn delete_project_collection(`
  - Purpose: Creates a Qdrant HTTP client, derives the code-symbol collection name for the given 'project_id', and deletes that collection via 'delete_qdrant_collection', returning the number of deleted collections or a 'VectorLifecycleError'. [crates/gcode/src/vector/code_symbols/qdrant.rs:41-48]
- `delete_file_vectors` (function) component `delete_file_vectors [function]` (`de7217ce-0632-57fb-9d09-0de63cfa80f2`) lines 50-58 [crates/gcode/src/vector/code_symbols/qdrant.rs:50-58]
  - Signature: `pub fn delete_file_vectors(`
  - Purpose: Deletes all vectors in the project’s code-symbol Qdrant collection associated with the given 'file_path', returning the number deleted or a 'VectorLifecycleError'. [crates/gcode/src/vector/code_symbols/qdrant.rs:50-58]
- `cleanup_orphan_file_vectors` (function) component `cleanup_orphan_file_vectors [function]` (`35d81eea-765a-5536-863c-8248cc076670`) lines 60-85 [crates/gcode/src/vector/code_symbols/qdrant.rs:60-85]
  - Signature: `pub fn cleanup_orphan_file_vectors(`
  - Purpose: Scans all vector-backed file paths for a project, deletes vectors for any path not present in 'indexed_file_paths', and returns a 'VectorOrphanCleanup' summary with scan and deletion counts. [crates/gcode/src/vector/code_symbols/qdrant.rs:60-85]
- `list_project_vector_file_paths` (function) component `list_project_vector_file_paths [function]` (`2c99769c-4862-54e7-8c30-dfffa699cf7b`) lines 87-143 [crates/gcode/src/vector/code_symbols/qdrant.rs:87-143]
  - Signature: `pub(super) fn list_project_vector_file_paths(`
  - Purpose: Lists and returns the distinct 'file_path' payload values for all Qdrant points in the project-specific code-symbol collection matching the given 'project_id', paging through scroll results until exhaustion or a 404 is returned. [crates/gcode/src/vector/code_symbols/qdrant.rs:87-143]
- `collect_file_paths_from_scroll_page` (function) component `collect_file_paths_from_scroll_page [function]` (`2d5fcd0e-7e48-5b32-92f7-dd6f6121265f`) lines 145-163 [crates/gcode/src/vector/code_symbols/qdrant.rs:145-163]
  - Signature: `fn collect_file_paths_from_scroll_page(`
  - Purpose: Extracts 'result.points[*].payload.file_path' string values from a Qdrant scroll response JSON, inserts them into the provided 'BTreeSet<String>' to deduplicate and sort them, and returns an error if 'result.points' is missing or not an array. [crates/gcode/src/vector/code_symbols/qdrant.rs:145-163]
- `delete_code_symbol_collections_with_prefix` (function) component `delete_code_symbol_collections_with_prefix [function]` (`2daa5684-3b05-5ba6-b777-674423274d01`) lines 165-192 [crates/gcode/src/vector/code_symbols/qdrant.rs:165-192]
  - Signature: `pub fn delete_code_symbol_collections_with_prefix(`
  - Purpose: Queries Qdrant for all collections, filters those whose names start with 'CODE_SYMBOL_COLLECTION_PREFIX', deletes each matching collection, and returns the names of the collections that were actually removed. [crates/gcode/src/vector/code_symbols/qdrant.rs:165-192]
- `vector_search` (function) component `vector_search [function]` (`5964aa3a-e623-5b81-9a2b-bb38e49e752c`) lines 194-215 [crates/gcode/src/vector/code_symbols/qdrant.rs:194-215]
  - Signature: `pub fn vector_search(`
  - Purpose: Performs a Qdrant vector similarity search for the given collection and query vector, logs any degradation warning from the search state, and returns the hit IDs paired with their scores as 'Vec<(String, f64)>'. [crates/gcode/src/vector/code_symbols/qdrant.rs:194-215]
- `vector_search_degradation_warning` (function) component `vector_search_degradation_warning [function]` (`dbe28a81-ba92-52e8-8f35-3fc9cd79d10c`) lines 217-227 [crates/gcode/src/vector/code_symbols/qdrant.rs:217-227]
  - Signature: `fn vector_search_degradation_warning(state: &ServiceState) -> Option<String> {`
  - Purpose: Returns 'None' when vector search is available, otherwise returns a warning string explaining that semantic vector search was skipped because Qdrant is either not configured or unreachable, including the unreachable error message when present. [crates/gcode/src/vector/code_symbols/qdrant.rs:217-227]
- `parse_collection_schema` (function) component `parse_collection_schema [function]` (`9d5637ec-7102-50b7-85f5-cf0314d6fd72`) lines 229-240 [crates/gcode/src/vector/code_symbols/qdrant.rs:229-240]
  - Signature: `pub(super) fn parse_collection_schema(data: &Value) -> Option<ExistingVectorCollectionSchema> {`
  - Purpose: Extracts '/result/config/params/vectors' from a JSON 'Value' and, if present, returns an 'ExistingVectorCollectionSchema' populated with an optional 'usize' 'size' parsed from 'vectors.size' and an optional 'String' 'distance' parsed from 'vectors.distance'. [crates/gcode/src/vector/code_symbols/qdrant.rs:229-240]
- `parse_collection_names` (function) component `parse_collection_names [function]` (`d2946e16-3bb3-54c5-8039-26e48445cc97`) lines 242-257 [crates/gcode/src/vector/code_symbols/qdrant.rs:242-257]
  - Signature: `fn parse_collection_names(data: &Value) -> Vec<String> {`
  - Purpose: Returns the '"name"' string from each object in 'data["result"]["collections"]' as a 'Vec<String>', or an empty vector if that path is missing, not an array, or yields no valid names. [crates/gcode/src/vector/code_symbols/qdrant.rs:242-257]
- `parse_points_count` (function) component `parse_points_count [function]` (`144e62b9-f549-58c9-bbd2-bbb2bddd95f6`) lines 259-268 [crates/gcode/src/vector/code_symbols/qdrant.rs:259-268]
  - Signature: `fn parse_points_count(data: &Value) -> Result<usize, VectorLifecycleError> {`
  - Purpose: Extracts 'result.count' from a JSON 'Value' as a 'usize', returning 'VectorLifecycleError::QdrantOperation' if the field is missing, non-integer, or does not fit in 'usize'. [crates/gcode/src/vector/code_symbols/qdrant.rs:259-268]
- `qdrant_http_client` (function) component `qdrant_http_client [function]` (`2fc6618f-0bf1-5c56-8370-379c9de3e029`) lines 270-280 [crates/gcode/src/vector/code_symbols/qdrant.rs:270-280]
  - Signature: `fn qdrant_http_client() -> Result<reqwest::blocking::Client, VectorLifecycleError> {`
  - Purpose: Returns a cached 'reqwest::blocking::Client' for Qdrant if already initialized, otherwise builds one with 'qdrant_delete_timeout()', stores it in 'QDRANT_HTTP_CLIENT', and maps build failures to 'VectorLifecycleError::QdrantOperation'. [crates/gcode/src/vector/code_symbols/qdrant.rs:270-280]
- `qdrant_delete_timeout` (function) component `qdrant_delete_timeout [function]` (`7ff829ec-3e2b-5228-9bea-85d06192aa3c`) lines 282-289 [crates/gcode/src/vector/code_symbols/qdrant.rs:282-289]
  - Signature: `fn qdrant_delete_timeout() -> Duration {`
  - Purpose: Returns the Qdrant delete timeout as a 'Duration', using the positive 'u64' value from 'QDRANT_DELETE_TIMEOUT_SECS_ENV' if present and valid, otherwise falling back to 'DEFAULT_QDRANT_DELETE_TIMEOUT'. [crates/gcode/src/vector/code_symbols/qdrant.rs:282-289]
- `qdrant_request_for_config` (function) component `qdrant_request_for_config [function]` (`2d629473-f8c0-53a3-9dc5-ee8dd8f143c6`) lines 291-310 [crates/gcode/src/vector/code_symbols/qdrant.rs:291-310]
  - Signature: `pub(super) fn qdrant_request_for_config(`
  - Purpose: Builds a 'reqwest' blocking request for the configured Qdrant base URL plus the given path, returning 'MissingQdrantConfig' if the trimmed URL is absent/empty and attaching an 'api-key' header when present. [crates/gcode/src/vector/code_symbols/qdrant.rs:291-310]
- `delete_qdrant_collection` (function) component `delete_qdrant_collection [function]` (`90ccda4e-368e-5519-ad73-5916cb2b0908`) lines 312-333 [crates/gcode/src/vector/code_symbols/qdrant.rs:312-333]
  - Signature: `fn delete_qdrant_collection(`
  - Purpose: Sends a blocking 'DELETE' request to the Qdrant collection endpoint and returns 'Ok(0)' if the collection is already '404 Not Found', 'Ok(1)' on any successful deletion response, or a wrapped 'VectorLifecycleError' on request or non-success HTTP failure. [crates/gcode/src/vector/code_symbols/qdrant.rs:312-333]
- `delete_vectors_for_filter` (function) component `delete_vectors_for_filter [function]` (`bae0c82d-87ea-5f64-82ab-374901cd361a`) lines 335-343 [crates/gcode/src/vector/code_symbols/qdrant.rs:335-343]
  - Signature: `pub(super) fn delete_vectors_for_filter(`
  - Purpose: Deletes vectors matching the specified 'project_id' and optional 'file_path' filter from the given Qdrant collection by delegating to 'delete_vectors_for_filter_excluding_ids' with an empty exclusion list, returning the number deleted or a 'VectorLifecycleError'. [crates/gcode/src/vector/code_symbols/qdrant.rs:335-343]
- `delete_vectors_for_filter_excluding_ids` (function) component `delete_vectors_for_filter_excluding_ids [function]` (`3b498207-df2f-5adc-8763-cf72c81ac6c8`) lines 345-415 [crates/gcode/src/vector/code_symbols/qdrant.rs:345-415]
  - Signature: `pub(super) fn delete_vectors_for_filter_excluding_ids(`
  - Purpose: Counts and, if any exist, deletes Qdrant points in the given collection matching 'project_id' and optional 'file_path', while excluding any 'keep_point_ids', returning the number deleted or '0' if none are found or the collection is missing. [crates/gcode/src/vector/code_symbols/qdrant.rs:345-415]
- `qdrant_http_error` (function) component `qdrant_http_error [function]` (`907f6d44-8027-5ca2-a6d3-358dc9baa609`) lines 417-427 [crates/gcode/src/vector/code_symbols/qdrant.rs:417-427]
  - Signature: `pub(super) fn qdrant_http_error(`
  - Purpose: Constructs a 'VectorLifecycleError::QdrantHttp' for a Qdrant request by recording the operation name, numeric HTTP status code, and response body text (or an empty string if reading the body fails). [crates/gcode/src/vector/code_symbols/qdrant.rs:417-427]
- `vector_search_degradation_warning_mentions_missing_qdrant_config` (function) component `vector_search_degradation_warning_mentions_missing_qdrant_config [function]` (`acfc3c97-8a04-5cca-996a-5e2e3f0e0ac6`) lines 434-439 [crates/gcode/src/vector/code_symbols/qdrant.rs:434-439]
  - Signature: `fn vector_search_degradation_warning_mentions_missing_qdrant_config() {`
  - Purpose: Verifies that 'vector_search_degradation_warning(&ServiceState::NotConfigured)' returns 'Some("semantic vector search skipped: Qdrant is not configured".to_string())'. [crates/gcode/src/vector/code_symbols/qdrant.rs:434-439]
- `vector_search_degradation_warning_mentions_unreachable_qdrant` (function) component `vector_search_degradation_warning_mentions_unreachable_qdrant [function]` (`5b5bf808-2885-5431-a061-3cf0e4c3b813`) lines 442-452 [crates/gcode/src/vector/code_symbols/qdrant.rs:442-452]
  - Signature: `fn vector_search_degradation_warning_mentions_unreachable_qdrant() {`
  - Purpose: Verifies that 'vector_search_degradation_warning' returns 'Some("semantic vector search skipped: Qdrant is unreachable: connection refused")' when given a 'ServiceState::Unreachable' with the message '"connection refused"'. [crates/gcode/src/vector/code_symbols/qdrant.rs:442-452]

