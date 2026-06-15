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

# crates/gwiki/src/sources/tests.rs

Module: [[code/modules/crates/gwiki/src/sources|crates/gwiki/src/sources]]

## Purpose

This file contains tests for source-manifest and index handling in `gwiki`: it checks that `SourceManifest::register()` deduplicates equivalent sources by canonical URL and content hash, preserves replay metadata for local file ingestion, and keeps canonical URL normalization consistent. It also verifies `existing_index_without_manifest()` correctly strips generated manifest sections while preserving surrounding manual content in both marked and unmarked index layouts.
[crates/gwiki/src/sources/tests.rs:8-50]
[crates/gwiki/src/sources/tests.rs:53-113]
[crates/gwiki/src/sources/tests.rs:116-121]
[crates/gwiki/src/sources/tests.rs:124-140]
[crates/gwiki/src/sources/tests.rs:143-160]

## API Symbols

- `dedupes_by_canonical_identity_and_hash` (function) component `dedupes_by_canonical_identity_and_hash [function]` (`e90ad7dd-1e73-5888-a7ba-0bf11e3d78b9`) lines 8-50 [crates/gwiki/src/sources/tests.rs:8-50]
  - Signature: `fn dedupes_by_canonical_identity_and_hash() {`
  - Purpose: This test verifies that `SourceManifest::register()` deduplicates source records with identical content by canonical URL identity and content hash, preserving only the first registration's metadata in the index. [crates/gwiki/src/sources/tests.rs:8-50]
- `local_file_replay_metadata_round_trips_through_manifest` (function) component `local_file_replay_metadata_round_trips_through_manifest [function]` (`98234679-435b-5104-bd46-e7e1cfaba61f`) lines 53-113 [crates/gwiki/src/sources/tests.rs:53-113]
  - Signature: `fn local_file_replay_metadata_round_trips_through_manifest() {`
  - Purpose: Verifies that local file replay metadata with ingestion options (routing configuration) can be serialized to and deserialized from a SourceManifest without data loss. [crates/gwiki/src/sources/tests.rs:53-113]
- `canonical_location_sorts_query_before_trimming_slash` (function) component `canonical_location_sorts_query_before_trimming_slash [function]` (`71e75e80-b30f-5090-9cf0-dfac821ca024`) lines 116-121 [crates/gwiki/src/sources/tests.rs:116-121]
  - Signature: `fn canonical_location_sorts_query_before_trimming_slash() {`
  - Purpose: This test verifies that `canonicalize_location` normalizes URLs by lowercasing the domain, lexicographically sorting query parameters, removing trailing slashes, and stripping fragments. [crates/gwiki/src/sources/tests.rs:116-121]
- `existing_index_strips_unmarked_manifest_until_next_heading` (function) component `existing_index_strips_unmarked_manifest_until_next_heading [function]` (`2ae2fa17-e2ea-5fa2-ad13-a7bef2d414fe`) lines 124-140 [crates/gwiki/src/sources/tests.rs:124-140]
  - Signature: `fn existing_index_strips_unmarked_manifest_until_next_heading() {`
  - Purpose: This test verifies that `existing_index_without_manifest()` correctly strips the Source manifest section and returns the unmarked prefix content separately from the suffix beginning at the next heading. [crates/gwiki/src/sources/tests.rs:124-140]
- `existing_index_preserves_content_after_marked_manifest` (function) component `existing_index_preserves_content_after_marked_manifest [function]` (`cef27902-e350-5015-b565-f06bb54ffb9d`) lines 143-160 [crates/gwiki/src/sources/tests.rs:143-160]
  - Signature: `fn existing_index_preserves_content_after_marked_manifest() {`
  - Purpose: This test verifies that `existing_index_without_manifest()` correctly removes the marked generated manifest section from an index file while preserving the manual content before and after it. [crates/gwiki/src/sources/tests.rs:143-160]

