---
title: crates/gcode/src/vector/code_symbols/qdrant.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/qdrant.rs
  ranges:
  - 17-23
  - 25-27
  - 29-36
  - 38-46
  - 48-75
  - 77-95
  - 97-108
  - 110-125
  - 127-136
  - 138-148
  - 150-157
  - 159-178
  - 180-201
  - 203-211
  - 213-283
  - 285-295
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols/qdrant.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

`crates/gcode/src/vector/code_symbols/qdrant.rs` exposes 16 indexed API symbols.
[crates/gcode/src/vector/code_symbols/qdrant.rs:17-23]
[crates/gcode/src/vector/code_symbols/qdrant.rs:25-27]
[crates/gcode/src/vector/code_symbols/qdrant.rs:29-36]
[crates/gcode/src/vector/code_symbols/qdrant.rs:38-46]
[crates/gcode/src/vector/code_symbols/qdrant.rs:48-75]

## API Symbols

- `collection_name` (function) component `collection_name [function]` (`e886a0d1-302c-50be-a33f-22fb7f4245dc`) lines 17-23 [crates/gcode/src/vector/code_symbols/qdrant.rs:17-23]
  - Signature: `pub fn collection_name(`
  - Purpose: Indexed function `collection_name` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:17-23]
- `collection_path` (function) component `collection_path [function]` (`bb3d04bd-e803-5207-a588-d8de469049ab`) lines 25-27 [crates/gcode/src/vector/code_symbols/qdrant.rs:25-27]
  - Signature: `pub(super) fn collection_path(collection: &str) -> String {`
  - Purpose: Indexed function `collection_path` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:25-27]
- `delete_project_collection` (function) component `delete_project_collection [function]` (`66c1dc48-35d6-5d59-a76f-88a8bab73f50`) lines 29-36 [crates/gcode/src/vector/code_symbols/qdrant.rs:29-36]
  - Signature: `pub fn delete_project_collection(`
  - Purpose: Indexed function `delete_project_collection` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:29-36]
- `delete_file_vectors` (function) component `delete_file_vectors [function]` (`af1c9417-c3f5-5b9d-a7ae-a55787d15482`) lines 38-46 [crates/gcode/src/vector/code_symbols/qdrant.rs:38-46]
  - Signature: `pub fn delete_file_vectors(`
  - Purpose: Indexed function `delete_file_vectors` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:38-46]
- `delete_code_symbol_collections_with_prefix` (function) component `delete_code_symbol_collections_with_prefix [function]` (`a4f560f1-3e79-5c18-a250-153793614d63`) lines 48-75 [crates/gcode/src/vector/code_symbols/qdrant.rs:48-75]
  - Signature: `pub fn delete_code_symbol_collections_with_prefix(`
  - Purpose: Indexed function `delete_code_symbol_collections_with_prefix` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:48-75]
- `vector_search` (function) component `vector_search [function]` (`d2719ad0-3758-5c8f-8d95-5fca474142e3`) lines 77-95 [crates/gcode/src/vector/code_symbols/qdrant.rs:77-95]
  - Signature: `pub fn vector_search(`
  - Purpose: Indexed function `vector_search` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:77-95]
- `parse_collection_schema` (function) component `parse_collection_schema [function]` (`fc175c6b-2b3a-51c7-b146-d3fb86d05750`) lines 97-108 [crates/gcode/src/vector/code_symbols/qdrant.rs:97-108]
  - Signature: `pub(super) fn parse_collection_schema(data: &Value) -> Option<ExistingVectorCollectionSchema> {`
  - Purpose: Indexed function `parse_collection_schema` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:97-108]
- `parse_collection_names` (function) component `parse_collection_names [function]` (`2f152d5b-5f8f-5868-9890-8b48df0a3248`) lines 110-125 [crates/gcode/src/vector/code_symbols/qdrant.rs:110-125]
  - Signature: `fn parse_collection_names(data: &Value) -> Vec<String> {`
  - Purpose: Indexed function `parse_collection_names` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:110-125]
- `parse_points_count` (function) component `parse_points_count [function]` (`e400f9fb-95ef-538b-b177-d5537e1efff6`) lines 127-136 [crates/gcode/src/vector/code_symbols/qdrant.rs:127-136]
  - Signature: `fn parse_points_count(data: &Value) -> Result<usize, VectorLifecycleError> {`
  - Purpose: Indexed function `parse_points_count` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:127-136]
- `qdrant_http_client` (function) component `qdrant_http_client [function]` (`7a7f54d3-51df-5574-8945-c039f98855f7`) lines 138-148 [crates/gcode/src/vector/code_symbols/qdrant.rs:138-148]
  - Signature: `fn qdrant_http_client() -> Result<reqwest::blocking::Client, VectorLifecycleError> {`
  - Purpose: Indexed function `qdrant_http_client` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:138-148]
- `qdrant_delete_timeout` (function) component `qdrant_delete_timeout [function]` (`6f7b3cf7-41ab-52bc-bf8b-27028a5f817a`) lines 150-157 [crates/gcode/src/vector/code_symbols/qdrant.rs:150-157]
  - Signature: `fn qdrant_delete_timeout() -> Duration {`
  - Purpose: Indexed function `qdrant_delete_timeout` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:150-157]
- `qdrant_request_for_config` (function) component `qdrant_request_for_config [function]` (`4147d05b-fbaf-5cf5-8a4d-b51c92390afe`) lines 159-178 [crates/gcode/src/vector/code_symbols/qdrant.rs:159-178]
  - Signature: `pub(super) fn qdrant_request_for_config(`
  - Purpose: Indexed function `qdrant_request_for_config` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:159-178]
- `delete_qdrant_collection` (function) component `delete_qdrant_collection [function]` (`c5ff425d-f22e-59ca-b980-86c24a8a1230`) lines 180-201 [crates/gcode/src/vector/code_symbols/qdrant.rs:180-201]
  - Signature: `fn delete_qdrant_collection(`
  - Purpose: Indexed function `delete_qdrant_collection` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:180-201]
- `delete_vectors_for_filter` (function) component `delete_vectors_for_filter [function]` (`8c491da8-31ae-5891-b0e9-328d53965250`) lines 203-211 [crates/gcode/src/vector/code_symbols/qdrant.rs:203-211]
  - Signature: `pub(super) fn delete_vectors_for_filter(`
  - Purpose: Indexed function `delete_vectors_for_filter` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:203-211]
- `delete_vectors_for_filter_excluding_ids` (function) component `delete_vectors_for_filter_excluding_ids [function]` (`05ddf195-9e0c-5edd-b7a9-e3c1a56c8c05`) lines 213-283 [crates/gcode/src/vector/code_symbols/qdrant.rs:213-283]
  - Signature: `pub(super) fn delete_vectors_for_filter_excluding_ids(`
  - Purpose: Indexed function `delete_vectors_for_filter_excluding_ids` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:213-283]
- `qdrant_http_error` (function) component `qdrant_http_error [function]` (`ee6101fe-f3f4-543c-9543-67c9ee079fca`) lines 285-295 [crates/gcode/src/vector/code_symbols/qdrant.rs:285-295]
  - Signature: `pub(super) fn qdrant_http_error(`
  - Purpose: Indexed function `qdrant_http_error` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:285-295]

