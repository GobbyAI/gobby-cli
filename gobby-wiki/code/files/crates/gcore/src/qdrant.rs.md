---
title: crates/gcore/src/qdrant.rs
type: code_file
provenance:
- file: crates/gcore/src/qdrant.rs
  ranges:
  - 20-36
  - 38-47
  - 50-53
  - 56-59
  - 63-67
  - 70-73
  - 77-81
  - 85-89
  - 92-114
  - 117-173
  - 176-194
  - 197-219
  - 222-244
  - 247-306
  - 308-334
  - 337-399
  - 401-407
  - 409-433
  - 435-449
  - 451-461
  - 463-469
  - 471-482
  - 484-491
  - 493-510
  - 512-524
  - 526-528
  - 530-532
  - 534-552
  - 554-572
  - 574-583
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/qdrant.rs:20-36](crates/gcore/src/qdrant.rs#L20-L36), [crates/gcore/src/qdrant.rs:38-47](crates/gcore/src/qdrant.rs#L38-L47), [crates/gcore/src/qdrant.rs:50-53](crates/gcore/src/qdrant.rs#L50-L53), [crates/gcore/src/qdrant.rs:56-59](crates/gcore/src/qdrant.rs#L56-L59), [crates/gcore/src/qdrant.rs:63-67](crates/gcore/src/qdrant.rs#L63-L67), [crates/gcore/src/qdrant.rs:70-73](crates/gcore/src/qdrant.rs#L70-L73), [crates/gcore/src/qdrant.rs:77-81](crates/gcore/src/qdrant.rs#L77-L81), [crates/gcore/src/qdrant.rs:85-89](crates/gcore/src/qdrant.rs#L85-L89), [crates/gcore/src/qdrant.rs:92-114](crates/gcore/src/qdrant.rs#L92-L114), [crates/gcore/src/qdrant.rs:117-173](crates/gcore/src/qdrant.rs#L117-L173), [crates/gcore/src/qdrant.rs:176-194](crates/gcore/src/qdrant.rs#L176-L194), [crates/gcore/src/qdrant.rs:197-219](crates/gcore/src/qdrant.rs#L197-L219), [crates/gcore/src/qdrant.rs:222-244](crates/gcore/src/qdrant.rs#L222-L244), [crates/gcore/src/qdrant.rs:247-306](crates/gcore/src/qdrant.rs#L247-L306), [crates/gcore/src/qdrant.rs:308-334](crates/gcore/src/qdrant.rs#L308-L334), [crates/gcore/src/qdrant.rs:337-399](crates/gcore/src/qdrant.rs#L337-L399), [crates/gcore/src/qdrant.rs:401-407](crates/gcore/src/qdrant.rs#L401-L407), [crates/gcore/src/qdrant.rs:409-433](crates/gcore/src/qdrant.rs#L409-L433), [crates/gcore/src/qdrant.rs:435-449](crates/gcore/src/qdrant.rs#L435-L449), [crates/gcore/src/qdrant.rs:451-461](crates/gcore/src/qdrant.rs#L451-L461), [crates/gcore/src/qdrant.rs:463-469](crates/gcore/src/qdrant.rs#L463-L469), [crates/gcore/src/qdrant.rs:471-482](crates/gcore/src/qdrant.rs#L471-L482), [crates/gcore/src/qdrant.rs:484-491](crates/gcore/src/qdrant.rs#L484-L491), [crates/gcore/src/qdrant.rs:493-510](crates/gcore/src/qdrant.rs#L493-L510), [crates/gcore/src/qdrant.rs:512-524](crates/gcore/src/qdrant.rs#L512-L524), [crates/gcore/src/qdrant.rs:526-528](crates/gcore/src/qdrant.rs#L526-L528), [crates/gcore/src/qdrant.rs:530-532](crates/gcore/src/qdrant.rs#L530-L532), [crates/gcore/src/qdrant.rs:534-552](crates/gcore/src/qdrant.rs#L534-L552), [crates/gcore/src/qdrant.rs:554-572](crates/gcore/src/qdrant.rs#L554-L572), [crates/gcore/src/qdrant.rs:574-583](crates/gcore/src/qdrant.rs#L574-L583)

</details>

# crates/gcore/src/qdrant.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This file defines the Qdrant adapter boundary for vector storage and search behind the `qdrant` feature. It provides typed request/response models and schema structs for collection configuration, a `QdrantError` type with context-aware HTTP/operation-status messages, and a set of helpers that build requests, issue Qdrant HTTP calls, parse responses, and translate failures into typed degradation. The higher-level functions cover collection lifecycle and validation (`ensure_collection`, `create_collection`, `collection_schema`, `collection_point_count`, `ensure_compatible_collection`), vector operations (`search`, `upsert`, batched upsert, delete-by-filter), and low-level utilities for request path construction, operation method selection, and unreachable-service detection.
[crates/gcore/src/qdrant.rs:20-36]
[crates/gcore/src/qdrant.rs:38-47]
[crates/gcore/src/qdrant.rs:50-53]
[crates/gcore/src/qdrant.rs:56-59]
[crates/gcore/src/qdrant.rs:63-67]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `QdrantError` | type | `pub enum QdrantError {` | `QdrantError [type]` | `3f3afd3e-537e-5fcb-964f-b3a60a899679` | 20-36 [crates/gcore/src/qdrant.rs:20-36] | Indexed type `QdrantError` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:20-36] |
| `http_status_context` | function | `fn http_status_context(collection: &Option<String>, request: &Option<String>) -> String {` | `http_status_context [function]` | `7d4a78a8-4438-5abc-a6c6-ffb413778e35` | 38-47 [crates/gcore/src/qdrant.rs:38-47] | Indexed function `http_status_context` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:38-47] |
| `VectorCollectionSchema` | class | `pub struct VectorCollectionSchema {` | `VectorCollectionSchema [class]` | `5fd996e9-13db-517c-a396-4c0aae591934` | 50-53 [crates/gcore/src/qdrant.rs:50-53] | Indexed class `VectorCollectionSchema` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:50-53] |
| `ExistingVectorCollectionSchema` | class | `pub struct ExistingVectorCollectionSchema {` | `ExistingVectorCollectionSchema [class]` | `bc76d138-f73c-5e57-aba4-3c1d9ecfd1e3` | 56-59 [crates/gcore/src/qdrant.rs:56-59] | Indexed class `ExistingVectorCollectionSchema` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:56-59] |
| `UpsertRequest` | class | `pub struct UpsertRequest {` | `UpsertRequest [class]` | `bfbb25c4-dcc0-5b12-ba37-42bbab0865dc` | 63-67 [crates/gcore/src/qdrant.rs:63-67] | Indexed class `UpsertRequest` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:63-67] |
| `UpsertResult` | class | `pub struct UpsertResult {` | `UpsertResult [class]` | `57b6ea02-c93e-5ba1-a297-c1af14e7905f` | 70-73 [crates/gcore/src/qdrant.rs:70-73] | Indexed class `UpsertResult` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:70-73] |
| `SearchRequest` | class | `pub struct SearchRequest {` | `SearchRequest [class]` | `ee391642-4147-521c-9f58-2ddb154fc0ea` | 77-81 [crates/gcore/src/qdrant.rs:77-81] | Indexed class `SearchRequest` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:77-81] |
| `SearchHit` | class | `pub struct SearchHit {` | `SearchHit [class]` | `0ffa9e1d-4d91-50ec-994c-aef48b1afee7` | 85-89 [crates/gcore/src/qdrant.rs:85-89] | Indexed class `SearchHit` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:85-89] |
| `with_qdrant` | function | `pub fn with_qdrant<T>(` | `with_qdrant [function]` | `3bd05d55-ab7b-57d2-bb59-626ed5cbf5eb` | 92-114 [crates/gcore/src/qdrant.rs:92-114] | Indexed function `with_qdrant` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:92-114] |
| `search` | function | `pub fn search(` | `search [function]` | `1a52c591-a1fa-5d33-8c12-709397c534c8` | 117-173 [crates/gcore/src/qdrant.rs:117-173] | Indexed function `search` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:117-173] |
| `ensure_collection` | function | `pub fn ensure_collection(` | `ensure_collection [function]` | `cc4647c8-5e89-5221-a607-5b436d87e860` | 176-194 [crates/gcore/src/qdrant.rs:176-194] | Indexed function `ensure_collection` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:176-194] |
| `collection_schema` | function | `pub fn collection_schema(` | `collection_schema [function]` | `575a8256-c7ee-5f35-9251-ee8e3b2dff42` | 197-219 [crates/gcore/src/qdrant.rs:197-219] | Indexed function `collection_schema` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:197-219] |
| `collection_point_count` | function | `pub fn collection_point_count(` | `collection_point_count [function]` | `898a6dea-8e4c-57a8-8927-6e64a1e06d02` | 222-244 [crates/gcore/src/qdrant.rs:222-244] | Indexed function `collection_point_count` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:222-244] |
| `delete_points_by_filter` | function | `pub fn delete_points_by_filter(` | `delete_points_by_filter [function]` | `e1385733-65fd-528d-8b34-542fb5578a46` | 247-306 [crates/gcore/src/qdrant.rs:247-306] | Indexed function `delete_points_by_filter` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:247-306] |
| `create_collection` | function | `fn create_collection(` | `create_collection [function]` | `f22fc1a8-5ade-5c22-988b-f80c33c8c727` | 308-334 [crates/gcore/src/qdrant.rs:308-334] | Indexed function `create_collection` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:308-334] |
| `upsert` | function | `pub fn upsert(` | `upsert [function]` | `46cb1da9-3c87-5897-a6b2-04309e65f043` | 337-399 [crates/gcore/src/qdrant.rs:337-399] | Indexed function `upsert` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:337-399] |
| `upsert_batched` | function | `pub fn upsert_batched(` | `upsert_batched [function]` | `fafaf2db-6f62-51b9-8b67-a75a5fe70e8d` | 401-407 [crates/gcore/src/qdrant.rs:401-407] | Indexed function `upsert_batched` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:401-407] |
| `upsert_batched_with_size` | function | `pub fn upsert_batched_with_size(` | `upsert_batched_with_size [function]` | `b878d1da-4449-5395-8926-bf473388fc3e` | 409-433 [crates/gcore/src/qdrant.rs:409-433] | Indexed function `upsert_batched_with_size` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:409-433] |
| `parse_upsert_result` | function | `fn parse_upsert_result(data: &Value) -> anyhow::Result<UpsertResult> {` | `parse_upsert_result [function]` | `5b639239-8eba-5689-998b-f2355c3c1895` | 435-449 [crates/gcore/src/qdrant.rs:435-449] | Indexed function `parse_upsert_result` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:435-449] |
| `parse_search_hit` | function | `fn parse_search_hit(hit: &Value) -> Option<SearchHit> {` | `parse_search_hit [function]` | `46cbcd63-6d33-5c5b-87f3-4e831d555001` | 451-461 [crates/gcore/src/qdrant.rs:451-461] | Indexed function `parse_search_hit` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:451-461] |
| `parse_point_id` | function | `fn parse_point_id(id: &Value) -> Option<String> {` | `parse_point_id [function]` | `51e8a4ce-e4b8-5d60-8c7e-fec53098919d` | 463-469 [crates/gcore/src/qdrant.rs:463-469] | Indexed function `parse_point_id` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:463-469] |
| `parse_collection_schema` | function | `fn parse_collection_schema(data: &Value) -> ExistingVectorCollectionSchema {` | `parse_collection_schema [function]` | `32a245e8-0f61-5285-b0fc-ca38839285bb` | 471-482 [crates/gcore/src/qdrant.rs:471-482] | Indexed function `parse_collection_schema` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:471-482] |
| `parse_collection_point_count` | function | `fn parse_collection_point_count(data: &Value) -> Option<u64> {` | `parse_collection_point_count [function]` | `2a169f39-ad73-5773-a5bf-d680f1f3feef` | 484-491 [crates/gcore/src/qdrant.rs:484-491] | Indexed function `parse_collection_point_count` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:484-491] |
| `ensure_compatible_collection` | function | `fn ensure_compatible_collection(` | `ensure_compatible_collection [function]` | `27b50f1b-ae00-5982-978d-eca8816a11c0` | 493-510 [crates/gcore/src/qdrant.rs:493-510] | Indexed function `ensure_compatible_collection` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:493-510] |
| `is_qdrant_unreachable` | function | `fn is_qdrant_unreachable(error: &anyhow::Error) -> bool {` | `is_qdrant_unreachable [function]` | `1ab72e09-39eb-5a1c-acec-66859cfaacb3` | 512-524 [crates/gcore/src/qdrant.rs:512-524] | Indexed function `is_qdrant_unreachable` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:512-524] |
| `encoded_collection` | function | `fn encoded_collection(collection: &str) -> String {` | `encoded_collection [function]` | `e4f9501e-2b35-5186-aed5-8e884b87dc2e` | 526-528 [crates/gcore/src/qdrant.rs:526-528] | Indexed function `encoded_collection` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:526-528] |
| `collection_request_path` | function | `fn collection_request_path(collection: &str) -> String {` | `collection_request_path [function]` | `e4c63f0a-3aaa-5ef7-848a-40b219355e07` | 530-532 [crates/gcore/src/qdrant.rs:530-532] | Indexed function `collection_request_path` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:530-532] |
| `qdrant_request` | function | `fn qdrant_request(` | `qdrant_request [function]` | `96933fff-5ceb-591e-8409-26a1f62ca292` | 534-552 [crates/gcore/src/qdrant.rs:534-552] | Indexed function `qdrant_request` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:534-552] |
| `qdrant_http_error` | function | `fn qdrant_http_error(` | `qdrant_http_error [function]` | `c9231c8f-47c4-5b83-9240-60a2baa6af00` | 554-572 [crates/gcore/src/qdrant.rs:554-572] | Indexed function `qdrant_http_error` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:554-572] |
| `operation_method` | function | `fn operation_method(operation: &str) -> &'static str {` | `operation_method [function]` | `cc110399-83e9-5b80-ab46-6acc305b7b03` | 574-583 [crates/gcore/src/qdrant.rs:574-583] | Indexed function `operation_method` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:574-583] |
