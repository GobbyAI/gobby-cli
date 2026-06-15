---
title: crates/gwiki/src/store.rs
type: code_file
provenance:
- file: crates/gwiki/src/store.rs
  ranges:
  - 15-17
  - 19-21
  - 32-39
  - 42-63
  - 66-71
  - 74-118
  - 121-135
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/store.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This module is the store entry point for `gwiki`: it wires together the `helpers`, `memory`, `postgres`, and `types` submodules, re-exports the main store APIs and data types, and exposes small wrappers for reading the configured in-memory index limit and classifying link targets. Its tests verify the helper behavior for link classification and scoped ID capping, and the memory store’s validation rules for chunk/link path mismatches and source indexing by `document_path`.
[crates/gwiki/src/store.rs:15-17]
[crates/gwiki/src/store.rs:19-21]
[crates/gwiki/src/store.rs:32-39]
[crates/gwiki/src/store.rs:42-63]
[crates/gwiki/src/store.rs:66-71]

## API Symbols

- `configured_memory_index_limit_bytes` (function) component `configured_memory_index_limit_bytes [function]` (`b4a82717-6d65-51fb-89cd-7bec1c14edd0`) lines 15-17 [crates/gwiki/src/store.rs:15-17]
  - Signature: `pub fn configured_memory_index_limit_bytes() -> Option<u64> {`
  - Purpose: Indexed function `configured_memory_index_limit_bytes` in `crates/gwiki/src/store.rs`. [crates/gwiki/src/store.rs:15-17]
- `link_kind` (function) component `link_kind [function]` (`17b104d1-ddac-557b-87e9-27a7332aa0d0`) lines 19-21 [crates/gwiki/src/store.rs:19-21]
  - Signature: `pub(crate) fn link_kind(target: &str) -> &'static str {`
  - Purpose: Indexed function `link_kind` in `crates/gwiki/src/store.rs`. [crates/gwiki/src/store.rs:19-21]
- `link_kind_classifies_uri_schemes_and_fragments` (function) component `link_kind_classifies_uri_schemes_and_fragments [function]` (`3635b710-928e-52ad-ad11-21bd4a8a3821`) lines 32-39 [crates/gwiki/src/store.rs:32-39]
  - Signature: `fn link_kind_classifies_uri_schemes_and_fragments() {`
  - Purpose: Indexed function `link_kind_classifies_uri_schemes_and_fragments` in `crates/gwiki/src/store.rs`. [crates/gwiki/src/store.rs:32-39]
- `scoped_ids_are_capped_with_deterministic_hash_suffix` (function) component `scoped_ids_are_capped_with_deterministic_hash_suffix [function]` (`9ec7a45e-c25f-566f-af7d-ec2916bbeb43`) lines 42-63 [crates/gwiki/src/store.rs:42-63]
  - Signature: `fn scoped_ids_are_capped_with_deterministic_hash_suffix() {`
  - Purpose: Verifies that 'scoped_text_id' produces a deterministic, capped-length scoped ID no longer than 'MAX_ID_LEN' and ending with a fixed-length hash suffix of 'HASH_SUFFIX_LEN' characters. [crates/gwiki/src/store.rs:42-63]
- `scoped_id_capping_tolerates_short_hashes` (function) component `scoped_id_capping_tolerates_short_hashes [function]` (`7f31af68-9a9d-55cf-b210-616592e29a83`) lines 66-71 [crates/gwiki/src/store.rs:66-71]
  - Signature: `fn scoped_id_capping_tolerates_short_hashes() {`
  - Purpose: Verifies that 'cap_scoped_id_with_hash' truncates an overlong scoped ID to 'MAX_ID_LEN' while preserving a short hash suffix ('-abc') at the end. [crates/gwiki/src/store.rs:66-71]
- `memory_store_rejects_path_mismatches` (function) component `memory_store_rejects_path_mismatches [function]` (`c6663743-909d-5d51-9d8a-c5d1c2f430db`) lines 74-118 [crates/gwiki/src/store.rs:74-118]
  - Signature: `fn memory_store_rejects_path_mismatches() {`
  - Purpose: Verifies that 'MemoryWikiStore::replace_chunks' and 'replace_links' reject entries whose embedded 'path' differs from the target page path, returning 'StoreError::InvalidData' for 'chunk.path' and 'link.path' mismatches. [crates/gwiki/src/store.rs:74-118]
- `memory_store_keys_sources_by_document_path` (function) component `memory_store_keys_sources_by_document_path [function]` (`d610ff6c-0810-53db-99d9-710d3d014ee7`) lines 121-135 [crates/gwiki/src/store.rs:121-135]
  - Signature: `fn memory_store_keys_sources_by_document_path() {`
  - Purpose: It verifies that 'MemoryWikiStore::upsert_source' indexes a 'WikiSource' in 'store.sources' by its 'document_path' key rather than its raw 'path', and does not store the entry under the raw file path. [crates/gwiki/src/store.rs:121-135]

