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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/qdrant/tests.rs:12-30](crates/gcore/src/qdrant/tests.rs#L12-L30), [crates/gcore/src/qdrant/tests.rs:33-59](crates/gcore/src/qdrant/tests.rs#L33-L59), [crates/gcore/src/qdrant/tests.rs:62-99](crates/gcore/src/qdrant/tests.rs#L62-L99), [crates/gcore/src/qdrant/tests.rs:102-128](crates/gcore/src/qdrant/tests.rs#L102-L128), [crates/gcore/src/qdrant/tests.rs:131-161](crates/gcore/src/qdrant/tests.rs#L131-L161), [crates/gcore/src/qdrant/tests.rs:164-207](crates/gcore/src/qdrant/tests.rs#L164-L207), [crates/gcore/src/qdrant/tests.rs:210-250](crates/gcore/src/qdrant/tests.rs#L210-L250), [crates/gcore/src/qdrant/tests.rs:253-292](crates/gcore/src/qdrant/tests.rs#L253-L292), [crates/gcore/src/qdrant/tests.rs:295-376](crates/gcore/src/qdrant/tests.rs#L295-L376), [crates/gcore/src/qdrant/tests.rs:379-397](crates/gcore/src/qdrant/tests.rs#L379-L397), [crates/gcore/src/qdrant/tests.rs:400-414](crates/gcore/src/qdrant/tests.rs#L400-L414), [crates/gcore/src/qdrant/tests.rs:417-494](crates/gcore/src/qdrant/tests.rs#L417-L494), [crates/gcore/src/qdrant/tests.rs:497-523](crates/gcore/src/qdrant/tests.rs#L497-L523), [crates/gcore/src/qdrant/tests.rs:525-527](crates/gcore/src/qdrant/tests.rs#L525-L527), [crates/gcore/src/qdrant/tests.rs:529-556](crates/gcore/src/qdrant/tests.rs#L529-L556)

</details>

# crates/gcore/src/qdrant/tests.rs

Module: [[code/modules/crates/gcore/src/qdrant|crates/gcore/src/qdrant]]

## Purpose

This file contains integration-style tests for the Qdrant-backed search layer in `gcore`. The tests verify that payloads and search filters stay opaque, Qdrant configuration is degraded or applied correctly through `with_qdrant`, CLI-path search issues the expected request and returns hits, batched upserts respect batch sizing and operation completion state, HTTP failures map to typed errors and server-only unreachable status, collection schemas reject unsupported vector naming, and collection lifecycle helpers create schema, delete filtered points, and read point counts from collection info.
[crates/gcore/src/qdrant/tests.rs:12-30]
[crates/gcore/src/qdrant/tests.rs:33-59]
[crates/gcore/src/qdrant/tests.rs:62-99]
[crates/gcore/src/qdrant/tests.rs:102-128]
[crates/gcore/src/qdrant/tests.rs:131-161]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `payload_schema_is_opaque` | function | `fn payload_schema_is_opaque() {` | `payload_schema_is_opaque [function]` | `fdec4d4e-02b7-5962-980d-d73a15f5d363` | 12-30 [crates/gcore/src/qdrant/tests.rs:12-30] | Indexed function `payload_schema_is_opaque` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:12-30] |
| `with_qdrant_degradation_contract` | function | `fn with_qdrant_degradation_contract() {` | `with_qdrant_degradation_contract [function]` | `e21d7f59-75e8-5680-8551-5e8d6aa293ec` | 33-59 [crates/gcore/src/qdrant/tests.rs:33-59] | Indexed function `with_qdrant_degradation_contract` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:33-59] |
| `sync_search_from_cli_path` | function | `fn sync_search_from_cli_path() {` | `sync_search_from_cli_path [function]` | `31cabca6-dbe6-580b-9a4e-bc76bb061c08` | 62-99 [crates/gcore/src/qdrant/tests.rs:62-99] | Indexed function `sync_search_from_cli_path` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:62-99] |
| `with_qdrant_search_composition` | function | `fn with_qdrant_search_composition() {` | `with_qdrant_search_composition [function]` | `9076148c-352b-5a2d-bfa7-0da5b765f8ff` | 102-128 [crates/gcore/src/qdrant/tests.rs:102-128] | Indexed function `with_qdrant_search_composition` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:102-128] |
| `upsert_requires_completed_qdrant_operation` | function | `fn upsert_requires_completed_qdrant_operation() {` | `upsert_requires_completed_qdrant_operation [function]` | `bd76bbfb-0dd3-5bed-8c52-cb5f2c1775e2` | 131-161 [crates/gcore/src/qdrant/tests.rs:131-161] | Indexed function `upsert_requires_completed_qdrant_operation` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:131-161] |
| `upsert_batched_splits_points_by_batch_size` | function | `fn upsert_batched_splits_points_by_batch_size() {` | `upsert_batched_splits_points_by_batch_size [function]` | `ae324ee7-57ba-5837-afc5-8b3ea14a82d4` | 164-207 [crates/gcore/src/qdrant/tests.rs:164-207] | Indexed function `upsert_batched_splits_points_by_batch_size` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:164-207] |
| `upsert_rejects_non_completed_qdrant_operation` | function | `fn upsert_rejects_non_completed_qdrant_operation() {` | `upsert_rejects_non_completed_qdrant_operation [function]` | `53fee626-a49b-55dd-ba91-975c899bcdde` | 210-250 [crates/gcore/src/qdrant/tests.rs:210-250] | Indexed function `upsert_rejects_non_completed_qdrant_operation` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:210-250] |
| `qdrant_single_state_boundary` | function | `fn qdrant_single_state_boundary() {` | `qdrant_single_state_boundary [function]` | `ae7b5f11-863c-5d7f-910f-ae6e6ffb5009` | 253-292 [crates/gcore/src/qdrant/tests.rs:253-292] | Indexed function `qdrant_single_state_boundary` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:253-292] |
| `qdrant_http_failures_are_typed_errors` | function | `fn qdrant_http_failures_are_typed_errors() {` | `qdrant_http_failures_are_typed_errors [function]` | `a4ad68c8-4467-56bb-864c-0dda2557516d` | 295-376 [crates/gcore/src/qdrant/tests.rs:295-376] | Indexed function `qdrant_http_failures_are_typed_errors` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:295-376] |
| `qdrant_http_status_unreachable_only_for_server_errors` | function | `fn qdrant_http_status_unreachable_only_for_server_errors() {` | `qdrant_http_status_unreachable_only_for_server_errors [function]` | `6a91fc46-49fa-5e6c-b115-9dabe3c153c7` | 379-397 [crates/gcore/src/qdrant/tests.rs:379-397] | Indexed function `qdrant_http_status_unreachable_only_for_server_errors` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:379-397] |
| `qdrant_collection_schema_rejects_named_or_unrecognized_vectors` | function | `fn qdrant_collection_schema_rejects_named_or_unrecognized_vectors() {` | `qdrant_collection_schema_rejects_named_or_unrecognized_vectors [function]` | `ee35f9a2-79e8-5b90-bbc0-7ef8b981570d` | 400-414 [crates/gcore/src/qdrant/tests.rs:400-414] | Indexed function `qdrant_collection_schema_rejects_named_or_unrecognized_vectors` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:400-414] |
| `collection_lifecycle_ensures_schema_and_deletes_filtered_points` | function | `fn collection_lifecycle_ensures_schema_and_deletes_filtered_points() {` | `collection_lifecycle_ensures_schema_and_deletes_filtered_points [function]` | `3015a1c8-f157-5eb2-a87b-fb6490ab6851` | 417-494 [crates/gcore/src/qdrant/tests.rs:417-494] | Indexed function `collection_lifecycle_ensures_schema_and_deletes_filtered_points` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:417-494] |
| `collection_point_count_reads_collection_info` | function | `fn collection_point_count_reads_collection_info() {` | `collection_point_count_reads_collection_info [function]` | `a9d0d29a-dfde-5112-b26b-9b3361c0843c` | 497-523 [crates/gcore/src/qdrant/tests.rs:497-523] | Indexed function `collection_point_count_reads_collection_info` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:497-523] |
| `spawn_qdrant_response` | function | `fn spawn_qdrant_response(status: u16, body: Value) -> (String, RequestHandle) {` | `spawn_qdrant_response [function]` | `c59eca72-ba1e-5e48-b120-c59e976d98f1` | 525-527 [crates/gcore/src/qdrant/tests.rs:525-527] | Indexed function `spawn_qdrant_response` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:525-527] |
| `spawn_qdrant_responses` | function | `fn spawn_qdrant_responses(` | `spawn_qdrant_responses [function]` | `4e562e15-2142-5340-8584-8872887efeaf` | 529-556 [crates/gcore/src/qdrant/tests.rs:529-556] | Indexed function `spawn_qdrant_responses` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:529-556] |
