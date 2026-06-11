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

`crates/gcore/src/qdrant/tests.rs` exposes 15 indexed API symbols.
[crates/gcore/src/qdrant/tests.rs:12-30]
[crates/gcore/src/qdrant/tests.rs:33-59]
[crates/gcore/src/qdrant/tests.rs:62-99]
[crates/gcore/src/qdrant/tests.rs:102-128]
[crates/gcore/src/qdrant/tests.rs:131-161]

## API Symbols

- `payload_schema_is_opaque` (function) component `payload_schema_is_opaque [function]` (`fdec4d4e-02b7-5962-980d-d73a15f5d363`) lines 12-30 [crates/gcore/src/qdrant/tests.rs:12-30]
  - Signature: `fn payload_schema_is_opaque() {`
  - Purpose: Indexed function `payload_schema_is_opaque` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:12-30]
- `with_qdrant_degradation_contract` (function) component `with_qdrant_degradation_contract [function]` (`e21d7f59-75e8-5680-8551-5e8d6aa293ec`) lines 33-59 [crates/gcore/src/qdrant/tests.rs:33-59]
  - Signature: `fn with_qdrant_degradation_contract() {`
  - Purpose: Indexed function `with_qdrant_degradation_contract` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:33-59]
- `sync_search_from_cli_path` (function) component `sync_search_from_cli_path [function]` (`31cabca6-dbe6-580b-9a4e-bc76bb061c08`) lines 62-99 [crates/gcore/src/qdrant/tests.rs:62-99]
  - Signature: `fn sync_search_from_cli_path() {`
  - Purpose: Indexed function `sync_search_from_cli_path` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:62-99]
- `with_qdrant_search_composition` (function) component `with_qdrant_search_composition [function]` (`9076148c-352b-5a2d-bfa7-0da5b765f8ff`) lines 102-128 [crates/gcore/src/qdrant/tests.rs:102-128]
  - Signature: `fn with_qdrant_search_composition() {`
  - Purpose: Indexed function `with_qdrant_search_composition` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:102-128]
- `upsert_requires_completed_qdrant_operation` (function) component `upsert_requires_completed_qdrant_operation [function]` (`bd76bbfb-0dd3-5bed-8c52-cb5f2c1775e2`) lines 131-161 [crates/gcore/src/qdrant/tests.rs:131-161]
  - Signature: `fn upsert_requires_completed_qdrant_operation() {`
  - Purpose: Indexed function `upsert_requires_completed_qdrant_operation` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:131-161]
- `upsert_batched_splits_points_by_batch_size` (function) component `upsert_batched_splits_points_by_batch_size [function]` (`ae324ee7-57ba-5837-afc5-8b3ea14a82d4`) lines 164-207 [crates/gcore/src/qdrant/tests.rs:164-207]
  - Signature: `fn upsert_batched_splits_points_by_batch_size() {`
  - Purpose: Indexed function `upsert_batched_splits_points_by_batch_size` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:164-207]
- `upsert_rejects_non_completed_qdrant_operation` (function) component `upsert_rejects_non_completed_qdrant_operation [function]` (`53fee626-a49b-55dd-ba91-975c899bcdde`) lines 210-250 [crates/gcore/src/qdrant/tests.rs:210-250]
  - Signature: `fn upsert_rejects_non_completed_qdrant_operation() {`
  - Purpose: Indexed function `upsert_rejects_non_completed_qdrant_operation` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:210-250]
- `qdrant_single_state_boundary` (function) component `qdrant_single_state_boundary [function]` (`ae7b5f11-863c-5d7f-910f-ae6e6ffb5009`) lines 253-292 [crates/gcore/src/qdrant/tests.rs:253-292]
  - Signature: `fn qdrant_single_state_boundary() {`
  - Purpose: Indexed function `qdrant_single_state_boundary` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:253-292]
- `qdrant_http_failures_are_typed_errors` (function) component `qdrant_http_failures_are_typed_errors [function]` (`a4ad68c8-4467-56bb-864c-0dda2557516d`) lines 295-376 [crates/gcore/src/qdrant/tests.rs:295-376]
  - Signature: `fn qdrant_http_failures_are_typed_errors() {`
  - Purpose: Indexed function `qdrant_http_failures_are_typed_errors` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:295-376]
- `qdrant_http_status_unreachable_only_for_server_errors` (function) component `qdrant_http_status_unreachable_only_for_server_errors [function]` (`6a91fc46-49fa-5e6c-b115-9dabe3c153c7`) lines 379-397 [crates/gcore/src/qdrant/tests.rs:379-397]
  - Signature: `fn qdrant_http_status_unreachable_only_for_server_errors() {`
  - Purpose: Indexed function `qdrant_http_status_unreachable_only_for_server_errors` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:379-397]
- `qdrant_collection_schema_rejects_named_or_unrecognized_vectors` (function) component `qdrant_collection_schema_rejects_named_or_unrecognized_vectors [function]` (`ee35f9a2-79e8-5b90-bbc0-7ef8b981570d`) lines 400-414 [crates/gcore/src/qdrant/tests.rs:400-414]
  - Signature: `fn qdrant_collection_schema_rejects_named_or_unrecognized_vectors() {`
  - Purpose: Indexed function `qdrant_collection_schema_rejects_named_or_unrecognized_vectors` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:400-414]
- `collection_lifecycle_ensures_schema_and_deletes_filtered_points` (function) component `collection_lifecycle_ensures_schema_and_deletes_filtered_points [function]` (`3015a1c8-f157-5eb2-a87b-fb6490ab6851`) lines 417-494 [crates/gcore/src/qdrant/tests.rs:417-494]
  - Signature: `fn collection_lifecycle_ensures_schema_and_deletes_filtered_points() {`
  - Purpose: Indexed function `collection_lifecycle_ensures_schema_and_deletes_filtered_points` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:417-494]
- `collection_point_count_reads_collection_info` (function) component `collection_point_count_reads_collection_info [function]` (`a9d0d29a-dfde-5112-b26b-9b3361c0843c`) lines 497-523 [crates/gcore/src/qdrant/tests.rs:497-523]
  - Signature: `fn collection_point_count_reads_collection_info() {`
  - Purpose: Indexed function `collection_point_count_reads_collection_info` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:497-523]
- `spawn_qdrant_response` (function) component `spawn_qdrant_response [function]` (`c59eca72-ba1e-5e48-b120-c59e976d98f1`) lines 525-527 [crates/gcore/src/qdrant/tests.rs:525-527]
  - Signature: `fn spawn_qdrant_response(status: u16, body: Value) -> (String, RequestHandle) {`
  - Purpose: Indexed function `spawn_qdrant_response` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:525-527]
- `spawn_qdrant_responses` (function) component `spawn_qdrant_responses [function]` (`4e562e15-2142-5340-8584-8872887efeaf`) lines 529-556 [crates/gcore/src/qdrant/tests.rs:529-556]
  - Signature: `fn spawn_qdrant_responses(`
  - Purpose: Indexed function `spawn_qdrant_responses` in `crates/gcore/src/qdrant/tests.rs`. [crates/gcore/src/qdrant/tests.rs:529-556]

