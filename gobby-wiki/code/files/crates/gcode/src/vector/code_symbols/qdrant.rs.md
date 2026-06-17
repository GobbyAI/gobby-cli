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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/vector/code_symbols/qdrant.rs:21-27](crates/gcode/src/vector/code_symbols/qdrant.rs#L21-L27), [crates/gcode/src/vector/code_symbols/qdrant.rs:29-35](crates/gcode/src/vector/code_symbols/qdrant.rs#L29-L35), [crates/gcode/src/vector/code_symbols/qdrant.rs:37-39](crates/gcode/src/vector/code_symbols/qdrant.rs#L37-L39), [crates/gcode/src/vector/code_symbols/qdrant.rs:41-48](crates/gcode/src/vector/code_symbols/qdrant.rs#L41-L48), [crates/gcode/src/vector/code_symbols/qdrant.rs:50-58](crates/gcode/src/vector/code_symbols/qdrant.rs#L50-L58), [crates/gcode/src/vector/code_symbols/qdrant.rs:60-85](crates/gcode/src/vector/code_symbols/qdrant.rs#L60-L85), [crates/gcode/src/vector/code_symbols/qdrant.rs:87-143](crates/gcode/src/vector/code_symbols/qdrant.rs#L87-L143), [crates/gcode/src/vector/code_symbols/qdrant.rs:145-163](crates/gcode/src/vector/code_symbols/qdrant.rs#L145-L163), [crates/gcode/src/vector/code_symbols/qdrant.rs:165-192](crates/gcode/src/vector/code_symbols/qdrant.rs#L165-L192), [crates/gcode/src/vector/code_symbols/qdrant.rs:194-215](crates/gcode/src/vector/code_symbols/qdrant.rs#L194-L215), [crates/gcode/src/vector/code_symbols/qdrant.rs:217-227](crates/gcode/src/vector/code_symbols/qdrant.rs#L217-L227), [crates/gcode/src/vector/code_symbols/qdrant.rs:229-240](crates/gcode/src/vector/code_symbols/qdrant.rs#L229-L240), [crates/gcode/src/vector/code_symbols/qdrant.rs:242-257](crates/gcode/src/vector/code_symbols/qdrant.rs#L242-L257), [crates/gcode/src/vector/code_symbols/qdrant.rs:259-268](crates/gcode/src/vector/code_symbols/qdrant.rs#L259-L268), [crates/gcode/src/vector/code_symbols/qdrant.rs:270-280](crates/gcode/src/vector/code_symbols/qdrant.rs#L270-L280), [crates/gcode/src/vector/code_symbols/qdrant.rs:282-289](crates/gcode/src/vector/code_symbols/qdrant.rs#L282-L289), [crates/gcode/src/vector/code_symbols/qdrant.rs:291-310](crates/gcode/src/vector/code_symbols/qdrant.rs#L291-L310), [crates/gcode/src/vector/code_symbols/qdrant.rs:312-333](crates/gcode/src/vector/code_symbols/qdrant.rs#L312-L333), [crates/gcode/src/vector/code_symbols/qdrant.rs:335-343](crates/gcode/src/vector/code_symbols/qdrant.rs#L335-L343), [crates/gcode/src/vector/code_symbols/qdrant.rs:345-415](crates/gcode/src/vector/code_symbols/qdrant.rs#L345-L415), [crates/gcode/src/vector/code_symbols/qdrant.rs:417-427](crates/gcode/src/vector/code_symbols/qdrant.rs#L417-L427), [crates/gcode/src/vector/code_symbols/qdrant.rs:434-439](crates/gcode/src/vector/code_symbols/qdrant.rs#L434-L439), [crates/gcode/src/vector/code_symbols/qdrant.rs:442-452](crates/gcode/src/vector/code_symbols/qdrant.rs#L442-L452)

</details>

# crates/gcode/src/vector/code_symbols/qdrant.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

Provides Qdrant-backed helpers for code-symbol vectors: it builds collection names and paths, creates a shared blocking HTTP client, and centralizes timeout and request construction for Qdrant operations. The main workflows delete whole project collections, delete vectors for a file or filter, clean up orphaned vectors by comparing indexed file paths against what is stored in Qdrant, list stored file paths via scroll pages, and run vector search. Parsing helpers turn Qdrant responses into collection schemas, collection-name lists, and point counts, while degradation-warning functions report missing config or unreachable Qdrant so callers can surface fallback behavior.
[crates/gcode/src/vector/code_symbols/qdrant.rs:21-27]
[crates/gcode/src/vector/code_symbols/qdrant.rs:29-35]
[crates/gcode/src/vector/code_symbols/qdrant.rs:37-39]
[crates/gcode/src/vector/code_symbols/qdrant.rs:41-48]
[crates/gcode/src/vector/code_symbols/qdrant.rs:50-58]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `VectorOrphanCleanup` | class | `pub struct VectorOrphanCleanup {` | `VectorOrphanCleanup [class]` | `ead3513c-5a8d-5e3b-b007-5c58b90cbf24` | 21-27 [crates/gcode/src/vector/code_symbols/qdrant.rs:21-27] | Indexed class `VectorOrphanCleanup` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:21-27] |
| `collection_name` | function | `pub fn collection_name(` | `collection_name [function]` | `e84efa11-2d2f-59c6-8703-1e73819a2c05` | 29-35 [crates/gcode/src/vector/code_symbols/qdrant.rs:29-35] | Indexed function `collection_name` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:29-35] |
| `collection_path` | function | `pub(super) fn collection_path(collection: &str) -> String {` | `collection_path [function]` | `9dca0307-94e2-5528-abf8-4a118c21f1bc` | 37-39 [crates/gcode/src/vector/code_symbols/qdrant.rs:37-39] | Indexed function `collection_path` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:37-39] |
| `delete_project_collection` | function | `pub fn delete_project_collection(` | `delete_project_collection [function]` | `7ecb9909-1269-5525-bf65-5fc9ce9e0c89` | 41-48 [crates/gcode/src/vector/code_symbols/qdrant.rs:41-48] | Indexed function `delete_project_collection` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:41-48] |
| `delete_file_vectors` | function | `pub fn delete_file_vectors(` | `delete_file_vectors [function]` | `de7217ce-0632-57fb-9d09-0de63cfa80f2` | 50-58 [crates/gcode/src/vector/code_symbols/qdrant.rs:50-58] | Indexed function `delete_file_vectors` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:50-58] |
| `cleanup_orphan_file_vectors` | function | `pub fn cleanup_orphan_file_vectors(` | `cleanup_orphan_file_vectors [function]` | `35d81eea-765a-5536-863c-8248cc076670` | 60-85 [crates/gcode/src/vector/code_symbols/qdrant.rs:60-85] | Indexed function `cleanup_orphan_file_vectors` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:60-85] |
| `list_project_vector_file_paths` | function | `pub(super) fn list_project_vector_file_paths(` | `list_project_vector_file_paths [function]` | `2c99769c-4862-54e7-8c30-dfffa699cf7b` | 87-143 [crates/gcode/src/vector/code_symbols/qdrant.rs:87-143] | Indexed function `list_project_vector_file_paths` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:87-143] |
| `collect_file_paths_from_scroll_page` | function | `fn collect_file_paths_from_scroll_page(` | `collect_file_paths_from_scroll_page [function]` | `2d5fcd0e-7e48-5b32-92f7-dd6f6121265f` | 145-163 [crates/gcode/src/vector/code_symbols/qdrant.rs:145-163] | Indexed function `collect_file_paths_from_scroll_page` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:145-163] |
| `delete_code_symbol_collections_with_prefix` | function | `pub fn delete_code_symbol_collections_with_prefix(` | `delete_code_symbol_collections_with_prefix [function]` | `2daa5684-3b05-5ba6-b777-674423274d01` | 165-192 [crates/gcode/src/vector/code_symbols/qdrant.rs:165-192] | Indexed function `delete_code_symbol_collections_with_prefix` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:165-192] |
| `vector_search` | function | `pub fn vector_search(` | `vector_search [function]` | `5964aa3a-e623-5b81-9a2b-bb38e49e752c` | 194-215 [crates/gcode/src/vector/code_symbols/qdrant.rs:194-215] | Indexed function `vector_search` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:194-215] |
| `vector_search_degradation_warning` | function | `fn vector_search_degradation_warning(state: &ServiceState) -> Option<String> {` | `vector_search_degradation_warning [function]` | `dbe28a81-ba92-52e8-8f35-3fc9cd79d10c` | 217-227 [crates/gcode/src/vector/code_symbols/qdrant.rs:217-227] | Indexed function `vector_search_degradation_warning` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:217-227] |
| `parse_collection_schema` | function | `pub(super) fn parse_collection_schema(data: &Value) -> Option<ExistingVectorCollectionSchema> {` | `parse_collection_schema [function]` | `9d5637ec-7102-50b7-85f5-cf0314d6fd72` | 229-240 [crates/gcode/src/vector/code_symbols/qdrant.rs:229-240] | Indexed function `parse_collection_schema` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:229-240] |
| `parse_collection_names` | function | `fn parse_collection_names(data: &Value) -> Vec<String> {` | `parse_collection_names [function]` | `d2946e16-3bb3-54c5-8039-26e48445cc97` | 242-257 [crates/gcode/src/vector/code_symbols/qdrant.rs:242-257] | Indexed function `parse_collection_names` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:242-257] |
| `parse_points_count` | function | `fn parse_points_count(data: &Value) -> Result<usize, VectorLifecycleError> {` | `parse_points_count [function]` | `144e62b9-f549-58c9-bbd2-bbb2bddd95f6` | 259-268 [crates/gcode/src/vector/code_symbols/qdrant.rs:259-268] | Indexed function `parse_points_count` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:259-268] |
| `qdrant_http_client` | function | `fn qdrant_http_client() -> Result<reqwest::blocking::Client, VectorLifecycleError> {` | `qdrant_http_client [function]` | `2fc6618f-0bf1-5c56-8370-379c9de3e029` | 270-280 [crates/gcode/src/vector/code_symbols/qdrant.rs:270-280] | Indexed function `qdrant_http_client` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:270-280] |
| `qdrant_delete_timeout` | function | `fn qdrant_delete_timeout() -> Duration {` | `qdrant_delete_timeout [function]` | `7ff829ec-3e2b-5228-9bea-85d06192aa3c` | 282-289 [crates/gcode/src/vector/code_symbols/qdrant.rs:282-289] | Indexed function `qdrant_delete_timeout` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:282-289] |
| `qdrant_request_for_config` | function | `pub(super) fn qdrant_request_for_config(` | `qdrant_request_for_config [function]` | `2d629473-f8c0-53a3-9dc5-ee8dd8f143c6` | 291-310 [crates/gcode/src/vector/code_symbols/qdrant.rs:291-310] | Indexed function `qdrant_request_for_config` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:291-310] |
| `delete_qdrant_collection` | function | `fn delete_qdrant_collection(` | `delete_qdrant_collection [function]` | `90ccda4e-368e-5519-ad73-5916cb2b0908` | 312-333 [crates/gcode/src/vector/code_symbols/qdrant.rs:312-333] | Indexed function `delete_qdrant_collection` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:312-333] |
| `delete_vectors_for_filter` | function | `pub(super) fn delete_vectors_for_filter(` | `delete_vectors_for_filter [function]` | `bae0c82d-87ea-5f64-82ab-374901cd361a` | 335-343 [crates/gcode/src/vector/code_symbols/qdrant.rs:335-343] | Indexed function `delete_vectors_for_filter` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:335-343] |
| `delete_vectors_for_filter_excluding_ids` | function | `pub(super) fn delete_vectors_for_filter_excluding_ids(` | `delete_vectors_for_filter_excluding_ids [function]` | `3b498207-df2f-5adc-8763-cf72c81ac6c8` | 345-415 [crates/gcode/src/vector/code_symbols/qdrant.rs:345-415] | Indexed function `delete_vectors_for_filter_excluding_ids` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:345-415] |
| `qdrant_http_error` | function | `pub(super) fn qdrant_http_error(` | `qdrant_http_error [function]` | `907f6d44-8027-5ca2-a6d3-358dc9baa609` | 417-427 [crates/gcode/src/vector/code_symbols/qdrant.rs:417-427] | Indexed function `qdrant_http_error` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:417-427] |
| `vector_search_degradation_warning_mentions_missing_qdrant_config` | function | `fn vector_search_degradation_warning_mentions_missing_qdrant_config() {` | `vector_search_degradation_warning_mentions_missing_qdrant_config [function]` | `acfc3c97-8a04-5cca-996a-5e2e3f0e0ac6` | 434-439 [crates/gcode/src/vector/code_symbols/qdrant.rs:434-439] | Indexed function `vector_search_degradation_warning_mentions_missing_qdrant_config` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:434-439] |
| `vector_search_degradation_warning_mentions_unreachable_qdrant` | function | `fn vector_search_degradation_warning_mentions_unreachable_qdrant() {` | `vector_search_degradation_warning_mentions_unreachable_qdrant [function]` | `5b5bf808-2885-5431-a061-3cf0e4c3b813` | 442-452 [crates/gcode/src/vector/code_symbols/qdrant.rs:442-452] | Indexed function `vector_search_degradation_warning_mentions_unreachable_qdrant` in `crates/gcode/src/vector/code_symbols/qdrant.rs`. [crates/gcode/src/vector/code_symbols/qdrant.rs:442-452] |
