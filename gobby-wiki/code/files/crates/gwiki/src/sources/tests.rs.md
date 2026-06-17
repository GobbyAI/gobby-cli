---
title: crates/gwiki/src/sources/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/sources/tests.rs
  ranges:
  - 8-50
  - 53-113
  - 116-121
  - 124-140
  - 143-160
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/sources/tests.rs:8-50](crates/gwiki/src/sources/tests.rs#L8-L50), [crates/gwiki/src/sources/tests.rs:53-113](crates/gwiki/src/sources/tests.rs#L53-L113), [crates/gwiki/src/sources/tests.rs:116-121](crates/gwiki/src/sources/tests.rs#L116-L121), [crates/gwiki/src/sources/tests.rs:124-140](crates/gwiki/src/sources/tests.rs#L124-L140), [crates/gwiki/src/sources/tests.rs:143-160](crates/gwiki/src/sources/tests.rs#L143-L160)

</details>

# crates/gwiki/src/sources/tests.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file contains tests for source manifest and index handling in `gwiki`: it verifies that source registration deduplicates by canonical location and content hash, and that local-file replay metadata round-trips correctly through the manifest. It also checks location canonicalization and the `existing_index_without_manifest` logic, ensuring unmarked manifests are stripped up to the next heading while marked manifests preserve the content that follows.
[crates/gwiki/src/sources/tests.rs:8-50]
[crates/gwiki/src/sources/tests.rs:53-113]
[crates/gwiki/src/sources/tests.rs:116-121]
[crates/gwiki/src/sources/tests.rs:124-140]
[crates/gwiki/src/sources/tests.rs:143-160]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `dedupes_by_canonical_identity_and_hash` | function | `fn dedupes_by_canonical_identity_and_hash() {` | `dedupes_by_canonical_identity_and_hash [function]` | `e90ad7dd-1e73-5888-a7ba-0bf11e3d78b9` | 8-50 [crates/gwiki/src/sources/tests.rs:8-50] | Indexed function `dedupes_by_canonical_identity_and_hash` in `crates/gwiki/src/sources/tests.rs`. [crates/gwiki/src/sources/tests.rs:8-50] |
| `local_file_replay_metadata_round_trips_through_manifest` | function | `fn local_file_replay_metadata_round_trips_through_manifest() {` | `local_file_replay_metadata_round_trips_through_manifest [function]` | `98234679-435b-5104-bd46-e7e1cfaba61f` | 53-113 [crates/gwiki/src/sources/tests.rs:53-113] | Indexed function `local_file_replay_metadata_round_trips_through_manifest` in `crates/gwiki/src/sources/tests.rs`. [crates/gwiki/src/sources/tests.rs:53-113] |
| `canonical_location_sorts_query_before_trimming_slash` | function | `fn canonical_location_sorts_query_before_trimming_slash() {` | `canonical_location_sorts_query_before_trimming_slash [function]` | `71e75e80-b30f-5090-9cf0-dfac821ca024` | 116-121 [crates/gwiki/src/sources/tests.rs:116-121] | Indexed function `canonical_location_sorts_query_before_trimming_slash` in `crates/gwiki/src/sources/tests.rs`. [crates/gwiki/src/sources/tests.rs:116-121] |
| `existing_index_strips_unmarked_manifest_until_next_heading` | function | `fn existing_index_strips_unmarked_manifest_until_next_heading() {` | `existing_index_strips_unmarked_manifest_until_next_heading [function]` | `2ae2fa17-e2ea-5fa2-ad13-a7bef2d414fe` | 124-140 [crates/gwiki/src/sources/tests.rs:124-140] | Indexed function `existing_index_strips_unmarked_manifest_until_next_heading` in `crates/gwiki/src/sources/tests.rs`. [crates/gwiki/src/sources/tests.rs:124-140] |
| `existing_index_preserves_content_after_marked_manifest` | function | `fn existing_index_preserves_content_after_marked_manifest() {` | `existing_index_preserves_content_after_marked_manifest [function]` | `cef27902-e350-5015-b565-f06bb54ffb9d` | 143-160 [crates/gwiki/src/sources/tests.rs:143-160] | Indexed function `existing_index_preserves_content_after_marked_manifest` in `crates/gwiki/src/sources/tests.rs`. [crates/gwiki/src/sources/tests.rs:143-160] |
