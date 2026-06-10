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

# crates/gcore/src/qdrant.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

`crates/gcore/src/qdrant.rs` exposes 30 indexed API symbols.
[crates/gcore/src/qdrant.rs:20-36]
[crates/gcore/src/qdrant.rs:38-47]
[crates/gcore/src/qdrant.rs:50-53]
[crates/gcore/src/qdrant.rs:56-59]
[crates/gcore/src/qdrant.rs:63-67]
[crates/gcore/src/qdrant.rs:70-73]
[crates/gcore/src/qdrant.rs:77-81]
[crates/gcore/src/qdrant.rs:85-89]
[crates/gcore/src/qdrant.rs:92-114]
[crates/gcore/src/qdrant.rs:117-173]
[crates/gcore/src/qdrant.rs:176-194]
[crates/gcore/src/qdrant.rs:197-219]
[crates/gcore/src/qdrant.rs:222-244]
[crates/gcore/src/qdrant.rs:247-306]
[crates/gcore/src/qdrant.rs:308-334]
[crates/gcore/src/qdrant.rs:337-399]
[crates/gcore/src/qdrant.rs:401-407]
[crates/gcore/src/qdrant.rs:409-433]
[crates/gcore/src/qdrant.rs:435-449]
[crates/gcore/src/qdrant.rs:451-461]
[crates/gcore/src/qdrant.rs:463-469]
[crates/gcore/src/qdrant.rs:471-482]
[crates/gcore/src/qdrant.rs:484-491]
[crates/gcore/src/qdrant.rs:493-510]
[crates/gcore/src/qdrant.rs:512-524]
[crates/gcore/src/qdrant.rs:526-528]
[crates/gcore/src/qdrant.rs:530-532]
[crates/gcore/src/qdrant.rs:534-552]
[crates/gcore/src/qdrant.rs:554-572]
[crates/gcore/src/qdrant.rs:574-583]

## API Symbols

- `QdrantError` (type) component `QdrantError [type]` (`3f3afd3e-537e-5fcb-964f-b3a60a899679`) lines 20-36 [crates/gcore/src/qdrant.rs:20-36]
  - Signature: `pub enum QdrantError {`
  - Purpose: Indexed type `QdrantError` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:20-36]
- `http_status_context` (function) component `http_status_context [function]` (`7d4a78a8-4438-5abc-a6c6-ffb413778e35`) lines 38-47 [crates/gcore/src/qdrant.rs:38-47]
  - Signature: `fn http_status_context(collection: &Option<String>, request: &Option<String>) -> String {`
  - Purpose: Indexed function `http_status_context` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:38-47]
- `VectorCollectionSchema` (class) component `VectorCollectionSchema [class]` (`5fd996e9-13db-517c-a396-4c0aae591934`) lines 50-53 [crates/gcore/src/qdrant.rs:50-53]
  - Signature: `pub struct VectorCollectionSchema {`
  - Purpose: Indexed class `VectorCollectionSchema` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:50-53]
- `ExistingVectorCollectionSchema` (class) component `ExistingVectorCollectionSchema [class]` (`bc76d138-f73c-5e57-aba4-3c1d9ecfd1e3`) lines 56-59 [crates/gcore/src/qdrant.rs:56-59]
  - Signature: `pub struct ExistingVectorCollectionSchema {`
  - Purpose: Indexed class `ExistingVectorCollectionSchema` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:56-59]
- `UpsertRequest` (class) component `UpsertRequest [class]` (`bfbb25c4-dcc0-5b12-ba37-42bbab0865dc`) lines 63-67 [crates/gcore/src/qdrant.rs:63-67]
  - Signature: `pub struct UpsertRequest {`
  - Purpose: Indexed class `UpsertRequest` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:63-67]
- `UpsertResult` (class) component `UpsertResult [class]` (`57b6ea02-c93e-5ba1-a297-c1af14e7905f`) lines 70-73 [crates/gcore/src/qdrant.rs:70-73]
  - Signature: `pub struct UpsertResult {`
  - Purpose: Indexed class `UpsertResult` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:70-73]
- `SearchRequest` (class) component `SearchRequest [class]` (`ee391642-4147-521c-9f58-2ddb154fc0ea`) lines 77-81 [crates/gcore/src/qdrant.rs:77-81]
  - Signature: `pub struct SearchRequest {`
  - Purpose: Indexed class `SearchRequest` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:77-81]
- `SearchHit` (class) component `SearchHit [class]` (`0ffa9e1d-4d91-50ec-994c-aef48b1afee7`) lines 85-89 [crates/gcore/src/qdrant.rs:85-89]
  - Signature: `pub struct SearchHit {`
  - Purpose: Indexed class `SearchHit` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:85-89]
- `with_qdrant` (function) component `with_qdrant [function]` (`3bd05d55-ab7b-57d2-bb59-626ed5cbf5eb`) lines 92-114 [crates/gcore/src/qdrant.rs:92-114]
  - Signature: `pub fn with_qdrant<T>(`
  - Purpose: Indexed function `with_qdrant` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:92-114]
- `search` (function) component `search [function]` (`1a52c591-a1fa-5d33-8c12-709397c534c8`) lines 117-173 [crates/gcore/src/qdrant.rs:117-173]
  - Signature: `pub fn search(`
  - Purpose: Indexed function `search` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:117-173]
- `ensure_collection` (function) component `ensure_collection [function]` (`cc4647c8-5e89-5221-a607-5b436d87e860`) lines 176-194 [crates/gcore/src/qdrant.rs:176-194]
  - Signature: `pub fn ensure_collection(`
  - Purpose: Indexed function `ensure_collection` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:176-194]
- `collection_schema` (function) component `collection_schema [function]` (`575a8256-c7ee-5f35-9251-ee8e3b2dff42`) lines 197-219 [crates/gcore/src/qdrant.rs:197-219]
  - Signature: `pub fn collection_schema(`
  - Purpose: Indexed function `collection_schema` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:197-219]
- `collection_point_count` (function) component `collection_point_count [function]` (`898a6dea-8e4c-57a8-8927-6e64a1e06d02`) lines 222-244 [crates/gcore/src/qdrant.rs:222-244]
  - Signature: `pub fn collection_point_count(`
  - Purpose: Indexed function `collection_point_count` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:222-244]
- `delete_points_by_filter` (function) component `delete_points_by_filter [function]` (`e1385733-65fd-528d-8b34-542fb5578a46`) lines 247-306 [crates/gcore/src/qdrant.rs:247-306]
  - Signature: `pub fn delete_points_by_filter(`
  - Purpose: Indexed function `delete_points_by_filter` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:247-306]
- `create_collection` (function) component `create_collection [function]` (`f22fc1a8-5ade-5c22-988b-f80c33c8c727`) lines 308-334 [crates/gcore/src/qdrant.rs:308-334]
  - Signature: `fn create_collection(`
  - Purpose: Indexed function `create_collection` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:308-334]
- `upsert` (function) component `upsert [function]` (`46cb1da9-3c87-5897-a6b2-04309e65f043`) lines 337-399 [crates/gcore/src/qdrant.rs:337-399]
  - Signature: `pub fn upsert(`
  - Purpose: Indexed function `upsert` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:337-399]
- `upsert_batched` (function) component `upsert_batched [function]` (`fafaf2db-6f62-51b9-8b67-a75a5fe70e8d`) lines 401-407 [crates/gcore/src/qdrant.rs:401-407]
  - Signature: `pub fn upsert_batched(`
  - Purpose: Indexed function `upsert_batched` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:401-407]
- `upsert_batched_with_size` (function) component `upsert_batched_with_size [function]` (`b878d1da-4449-5395-8926-bf473388fc3e`) lines 409-433 [crates/gcore/src/qdrant.rs:409-433]
  - Signature: `pub fn upsert_batched_with_size(`
  - Purpose: Indexed function `upsert_batched_with_size` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:409-433]
- `parse_upsert_result` (function) component `parse_upsert_result [function]` (`5b639239-8eba-5689-998b-f2355c3c1895`) lines 435-449 [crates/gcore/src/qdrant.rs:435-449]
  - Signature: `fn parse_upsert_result(data: &Value) -> anyhow::Result<UpsertResult> {`
  - Purpose: Indexed function `parse_upsert_result` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:435-449]
- `parse_search_hit` (function) component `parse_search_hit [function]` (`46cbcd63-6d33-5c5b-87f3-4e831d555001`) lines 451-461 [crates/gcore/src/qdrant.rs:451-461]
  - Signature: `fn parse_search_hit(hit: &Value) -> Option<SearchHit> {`
  - Purpose: Indexed function `parse_search_hit` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:451-461]
- `parse_point_id` (function) component `parse_point_id [function]` (`51e8a4ce-e4b8-5d60-8c7e-fec53098919d`) lines 463-469 [crates/gcore/src/qdrant.rs:463-469]
  - Signature: `fn parse_point_id(id: &Value) -> Option<String> {`
  - Purpose: Indexed function `parse_point_id` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:463-469]
- `parse_collection_schema` (function) component `parse_collection_schema [function]` (`32a245e8-0f61-5285-b0fc-ca38839285bb`) lines 471-482 [crates/gcore/src/qdrant.rs:471-482]
  - Signature: `fn parse_collection_schema(data: &Value) -> ExistingVectorCollectionSchema {`
  - Purpose: Indexed function `parse_collection_schema` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:471-482]
- `parse_collection_point_count` (function) component `parse_collection_point_count [function]` (`2a169f39-ad73-5773-a5bf-d680f1f3feef`) lines 484-491 [crates/gcore/src/qdrant.rs:484-491]
  - Signature: `fn parse_collection_point_count(data: &Value) -> Option<u64> {`
  - Purpose: Indexed function `parse_collection_point_count` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:484-491]
- `ensure_compatible_collection` (function) component `ensure_compatible_collection [function]` (`27b50f1b-ae00-5982-978d-eca8816a11c0`) lines 493-510 [crates/gcore/src/qdrant.rs:493-510]
  - Signature: `fn ensure_compatible_collection(`
  - Purpose: Indexed function `ensure_compatible_collection` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:493-510]
- `is_qdrant_unreachable` (function) component `is_qdrant_unreachable [function]` (`1ab72e09-39eb-5a1c-acec-66859cfaacb3`) lines 512-524 [crates/gcore/src/qdrant.rs:512-524]
  - Signature: `fn is_qdrant_unreachable(error: &anyhow::Error) -> bool {`
  - Purpose: Indexed function `is_qdrant_unreachable` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:512-524]
- `encoded_collection` (function) component `encoded_collection [function]` (`e4f9501e-2b35-5186-aed5-8e884b87dc2e`) lines 526-528 [crates/gcore/src/qdrant.rs:526-528]
  - Signature: `fn encoded_collection(collection: &str) -> String {`
  - Purpose: Indexed function `encoded_collection` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:526-528]
- `collection_request_path` (function) component `collection_request_path [function]` (`e4c63f0a-3aaa-5ef7-848a-40b219355e07`) lines 530-532 [crates/gcore/src/qdrant.rs:530-532]
  - Signature: `fn collection_request_path(collection: &str) -> String {`
  - Purpose: Indexed function `collection_request_path` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:530-532]
- `qdrant_request` (function) component `qdrant_request [function]` (`96933fff-5ceb-591e-8409-26a1f62ca292`) lines 534-552 [crates/gcore/src/qdrant.rs:534-552]
  - Signature: `fn qdrant_request(`
  - Purpose: Indexed function `qdrant_request` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:534-552]
- `qdrant_http_error` (function) component `qdrant_http_error [function]` (`c9231c8f-47c4-5b83-9240-60a2baa6af00`) lines 554-572 [crates/gcore/src/qdrant.rs:554-572]
  - Signature: `fn qdrant_http_error(`
  - Purpose: Indexed function `qdrant_http_error` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:554-572]
- `operation_method` (function) component `operation_method [function]` (`cc110399-83e9-5b80-ab46-6acc305b7b03`) lines 574-583 [crates/gcore/src/qdrant.rs:574-583]
  - Signature: `fn operation_method(operation: &str) -> &'static str {`
  - Purpose: Indexed function `operation_method` in `crates/gcore/src/qdrant.rs`. [crates/gcore/src/qdrant.rs:574-583]

