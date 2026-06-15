---
title: crates/gcore/src/qdrant/tests.rs
type: code_file
provenance:
- file: crates/gcore/src/qdrant/tests.rs
  ranges:
  - 12-30
  - 33-59
  - 62-99
  - 102-128
  - 131-161
  - 164-207
  - 210-250
  - 253-292
  - 295-376
  - 379-397
  - 400-414
  - 417-494
  - 497-523
  - 525-527
  - 529-556
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/qdrant/tests.rs

Module: [[code/modules/crates/gcore/src/qdrant|crates/gcore/src/qdrant]]

## Purpose

Test module for the Qdrant client layer. It exercises the request/response and degradation contracts around search, upsert, collection management, error typing, schema validation, and point-count parsing, and includes local test-server helpers that spin up mocked Qdrant HTTP responses for those cases.
[crates/gcore/src/qdrant/tests.rs:12-30]
[crates/gcore/src/qdrant/tests.rs:33-59]
[crates/gcore/src/qdrant/tests.rs:62-99]
[crates/gcore/src/qdrant/tests.rs:102-128]
[crates/gcore/src/qdrant/tests.rs:131-161]

## API Symbols

- `payload_schema_is_opaque` (function) component `payload_schema_is_opaque [function]` (`fdec4d4e-02b7-5962-980d-d73a15f5d363`) lines 12-30 [crates/gcore/src/qdrant/tests.rs:12-30]
  - Signature: `fn payload_schema_is_opaque() {`
  - Purpose: Verifies that payload data is preserved verbatim in an 'UpsertRequest' and that a 'SearchRequest' filter can be constructed and inspected without imposing schema interpretation on the payload. [crates/gcore/src/qdrant/tests.rs:12-30]
- `with_qdrant_degradation_contract` (function) component `with_qdrant_degradation_contract [function]` (`e21d7f59-75e8-5680-8551-5e8d6aa293ec`) lines 33-59 [crates/gcore/src/qdrant/tests.rs:33-59]
  - Signature: `fn with_qdrant_degradation_contract() {`
  - Purpose: Verifies that 'with_qdrant' returns the fallback value and 'ServiceState::NotConfigured' when Qdrant is absent or missing a URL, returns the closure result with 'ServiceState::Available' when configured, and propagates closure errors unchanged. [crates/gcore/src/qdrant/tests.rs:33-59]
- `sync_search_from_cli_path` (function) component `sync_search_from_cli_path [function]` (`31cabca6-dbe6-580b-9a4e-bc76bb061c08`) lines 62-99 [crates/gcore/src/qdrant/tests.rs:62-99]
  - Signature: `fn sync_search_from_cli_path() {`
  - Purpose: Verifies that 'search' issues an authenticated POST to Qdrant’s '/collections/code_symbols_project/points/search' endpoint with payload retrieval enabled, then parses a single returned point into a hit with the expected 'id', 'score', and 'payload'. [crates/gcore/src/qdrant/tests.rs:62-99]
- `with_qdrant_search_composition` (function) component `with_qdrant_search_composition [function]` (`9076148c-352b-5a2d-bfa7-0da5b765f8ff`) lines 102-128 [crates/gcore/src/qdrant/tests.rs:102-128]
  - Signature: `fn with_qdrant_search_composition() {`
  - Purpose: Executes a composed Qdrant search through 'with_qdrant', verifies the service is reported 'Available', and asserts the returned hit contains the expected point ID from the mocked 200 response. [crates/gcore/src/qdrant/tests.rs:102-128]
- `upsert_requires_completed_qdrant_operation` (function) component `upsert_requires_completed_qdrant_operation [function]` (`bd76bbfb-0dd3-5bed-8c52-cb5f2c1775e2`) lines 131-161 [crates/gcore/src/qdrant/tests.rs:131-161]
  - Signature: `fn upsert_requires_completed_qdrant_operation() {`
  - Purpose: Verifies that 'upsert' against Qdrant succeeds only when the response reports a completed operation, returning the operation ID/status and sending the request with 'wait=true'. [crates/gcore/src/qdrant/tests.rs:131-161]
- `upsert_batched_splits_points_by_batch_size` (function) component `upsert_batched_splits_points_by_batch_size [function]` (`ae324ee7-57ba-5837-afc5-8b3ea14a82d4`) lines 164-207 [crates/gcore/src/qdrant/tests.rs:164-207]
  - Signature: `fn upsert_batched_splits_points_by_batch_size() {`
  - Purpose: Tests that 'upsert_batched_with_size' splits five upsert requests into batches of size 2, issues three Qdrant requests, and returns the total number of successfully upserted points. [crates/gcore/src/qdrant/tests.rs:164-207]
- `upsert_rejects_non_completed_qdrant_operation` (function) component `upsert_rejects_non_completed_qdrant_operation [function]` (`53fee626-a49b-55dd-ba91-975c899bcdde`) lines 210-250 [crates/gcore/src/qdrant/tests.rs:210-250]
  - Signature: `fn upsert_rejects_non_completed_qdrant_operation() {`
  - Purpose: Verifies that 'upsert' returns a 'QdrantError::OperationStatus' when Qdrant responds with a non-completed '"acknowledged"' operation, and that the error preserves the operation name, status, target collection, and request path. [crates/gcore/src/qdrant/tests.rs:210-250]
- `qdrant_single_state_boundary` (function) component `qdrant_single_state_boundary [function]` (`ae7b5f11-863c-5d7f-910f-ae6e6ffb5009`) lines 253-292 [crates/gcore/src/qdrant/tests.rs:253-292]
  - Signature: `fn qdrant_single_state_boundary() {`
  - Purpose: Verifies that 'with_qdrant' degrades to 'ServiceState::NotConfigured' and returns no hits when the Qdrant URL is absent, and degrades to 'ServiceState::Unreachable' with an HTTP 503 error message when a search request fails. [crates/gcore/src/qdrant/tests.rs:253-292]
- `qdrant_http_failures_are_typed_errors` (function) component `qdrant_http_failures_are_typed_errors [function]` (`a4ad68c8-4467-56bb-864c-0dda2557516d`) lines 295-376 [crates/gcore/src/qdrant/tests.rs:295-376]
  - Signature: `fn qdrant_http_failures_are_typed_errors() {`
  - Purpose: Verifies that Qdrant 'search' and 'upsert' convert HTTP error responses into 'QdrantError::HttpStatus' with the correct operation, status code, body, collection, and request metadata. [crates/gcore/src/qdrant/tests.rs:295-376]
- `qdrant_http_status_unreachable_only_for_server_errors` (function) component `qdrant_http_status_unreachable_only_for_server_errors [function]` (`6a91fc46-49fa-5e6c-b115-9dabe3c153c7`) lines 379-397 [crates/gcore/src/qdrant/tests.rs:379-397]
  - Signature: `fn qdrant_http_status_unreachable_only_for_server_errors() {`
  - Purpose: Verifies that 'is_qdrant_unreachable' returns 'false' for a Qdrant HTTP 4xx client error and 'true' for a 5xx server error. [crates/gcore/src/qdrant/tests.rs:379-397]
- `qdrant_collection_schema_rejects_named_or_unrecognized_vectors` (function) component `qdrant_collection_schema_rejects_named_or_unrecognized_vectors [function]` (`ee35f9a2-79e8-5b90-bbc0-7ef8b981570d`) lines 400-414 [crates/gcore/src/qdrant/tests.rs:400-414]
  - Signature: `fn qdrant_collection_schema_rejects_named_or_unrecognized_vectors() {`
  - Purpose: Verifies that 'ensure_compatible_collection' rejects Qdrant collection schemas that are incomplete, including those with a named 'vectors.default' entry or no 'vectors' config at all, by asserting it returns an “incompatible schema” error. [crates/gcore/src/qdrant/tests.rs:400-414]
- `collection_lifecycle_ensures_schema_and_deletes_filtered_points` (function) component `collection_lifecycle_ensures_schema_and_deletes_filtered_points [function]` (`3015a1c8-f157-5eb2-a87b-fb6490ab6851`) lines 417-494 [crates/gcore/src/qdrant/tests.rs:417-494]
  - Signature: `fn collection_lifecycle_ensures_schema_and_deletes_filtered_points() {`
  - Purpose: Verifies that 'ensure_collection' reuses an existing Qdrant collection while preserving the expected vector schema and that 'delete_points_by_filter' issues a 'POST /collections/{name}/points/delete?wait=true' request containing the supplied metadata filter, including the 'path' match. [crates/gcore/src/qdrant/tests.rs:417-494]
- `collection_point_count_reads_collection_info` (function) component `collection_point_count_reads_collection_info [function]` (`a9d0d29a-dfde-5112-b26b-9b3361c0843c`) lines 497-523 [crates/gcore/src/qdrant/tests.rs:497-523]
  - Signature: `fn collection_point_count_reads_collection_info() {`
  - Purpose: Verifies that 'collection_point_count' issues a 'GET /collections/{collection}' request, returns 'points_count' from the Qdrant collection info response, and that 'parse_collection_point_count' falls back to 'vectors_count' while rejecting non-numeric 'points_count' values. [crates/gcore/src/qdrant/tests.rs:497-523]
- `spawn_qdrant_response` (function) component `spawn_qdrant_response [function]` (`c59eca72-ba1e-5e48-b120-c59e976d98f1`) lines 525-527 [crates/gcore/src/qdrant/tests.rs:525-527]
  - Signature: `fn spawn_qdrant_response(status: u16, body: Value) -> (String, RequestHandle) {`
  - Purpose: Creates a Qdrant test-server JSON response with the given HTTP status and serialized 'body', then unwraps and returns the resulting '(String, RequestHandle)' from 'spawn_json_response_with_status', panicking with '"spawn qdrant test server"' on failure. [crates/gcore/src/qdrant/tests.rs:525-527]
- `spawn_qdrant_responses` (function) component `spawn_qdrant_responses [function]` (`4e562e15-2142-5340-8584-8872887efeaf`) lines 529-556 [crates/gcore/src/qdrant/tests.rs:529-556]
  - Signature: `fn spawn_qdrant_responses(`
  - Purpose: Binds an ephemeral localhost TCP listener, spawns a thread that sequentially accepts one connection per provided '(status, body)' pair, records each incoming HTTP request, and replies with a JSON HTTP response using the specified status code and body, returning the base URL and the join handle for the captured request list. [crates/gcore/src/qdrant/tests.rs:529-556]

