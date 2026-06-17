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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/store.rs:15-17](crates/gwiki/src/store.rs#L15-L17), [crates/gwiki/src/store.rs:19-21](crates/gwiki/src/store.rs#L19-L21), [crates/gwiki/src/store.rs:32-39](crates/gwiki/src/store.rs#L32-L39), [crates/gwiki/src/store.rs:42-63](crates/gwiki/src/store.rs#L42-L63), [crates/gwiki/src/store.rs:66-71](crates/gwiki/src/store.rs#L66-L71), [crates/gwiki/src/store.rs:74-118](crates/gwiki/src/store.rs#L74-L118), [crates/gwiki/src/store.rs:121-135](crates/gwiki/src/store.rs#L121-L135)

</details>

# crates/gwiki/src/store.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the wiki store facade for `gwiki`, re-exporting the memory and Postgres store implementations plus the shared store types and errors. It also exposes the memory index byte limit environment variable and delegates link classification and memory-index configuration to helper functions, while tests verify URI vs wiki link detection, deterministic capped ID generation, and memory store path validation/keying behavior.
[crates/gwiki/src/store.rs:15-17]
[crates/gwiki/src/store.rs:19-21]
[crates/gwiki/src/store.rs:32-39]
[crates/gwiki/src/store.rs:42-63]
[crates/gwiki/src/store.rs:66-71]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `configured_memory_index_limit_bytes` | function | `pub fn configured_memory_index_limit_bytes() -> Option<u64> {` | `configured_memory_index_limit_bytes [function]` | `b4a82717-6d65-51fb-89cd-7bec1c14edd0` | 15-17 [crates/gwiki/src/store.rs:15-17] | Indexed function `configured_memory_index_limit_bytes` in `crates/gwiki/src/store.rs`. [crates/gwiki/src/store.rs:15-17] |
| `link_kind` | function | `pub(crate) fn link_kind(target: &str) -> &'static str {` | `link_kind [function]` | `17b104d1-ddac-557b-87e9-27a7332aa0d0` | 19-21 [crates/gwiki/src/store.rs:19-21] | Indexed function `link_kind` in `crates/gwiki/src/store.rs`. [crates/gwiki/src/store.rs:19-21] |
| `link_kind_classifies_uri_schemes_and_fragments` | function | `fn link_kind_classifies_uri_schemes_and_fragments() {` | `link_kind_classifies_uri_schemes_and_fragments [function]` | `3635b710-928e-52ad-ad11-21bd4a8a3821` | 32-39 [crates/gwiki/src/store.rs:32-39] | Indexed function `link_kind_classifies_uri_schemes_and_fragments` in `crates/gwiki/src/store.rs`. [crates/gwiki/src/store.rs:32-39] |
| `scoped_ids_are_capped_with_deterministic_hash_suffix` | function | `fn scoped_ids_are_capped_with_deterministic_hash_suffix() {` | `scoped_ids_are_capped_with_deterministic_hash_suffix [function]` | `9ec7a45e-c25f-566f-af7d-ec2916bbeb43` | 42-63 [crates/gwiki/src/store.rs:42-63] | Indexed function `scoped_ids_are_capped_with_deterministic_hash_suffix` in `crates/gwiki/src/store.rs`. [crates/gwiki/src/store.rs:42-63] |
| `scoped_id_capping_tolerates_short_hashes` | function | `fn scoped_id_capping_tolerates_short_hashes() {` | `scoped_id_capping_tolerates_short_hashes [function]` | `7f31af68-9a9d-55cf-b210-616592e29a83` | 66-71 [crates/gwiki/src/store.rs:66-71] | Indexed function `scoped_id_capping_tolerates_short_hashes` in `crates/gwiki/src/store.rs`. [crates/gwiki/src/store.rs:66-71] |
| `memory_store_rejects_path_mismatches` | function | `fn memory_store_rejects_path_mismatches() {` | `memory_store_rejects_path_mismatches [function]` | `c6663743-909d-5d51-9d8a-c5d1c2f430db` | 74-118 [crates/gwiki/src/store.rs:74-118] | Indexed function `memory_store_rejects_path_mismatches` in `crates/gwiki/src/store.rs`. [crates/gwiki/src/store.rs:74-118] |
| `memory_store_keys_sources_by_document_path` | function | `fn memory_store_keys_sources_by_document_path() {` | `memory_store_keys_sources_by_document_path [function]` | `d610ff6c-0810-53db-99d9-710d3d014ee7` | 121-135 [crates/gwiki/src/store.rs:121-135] | Indexed function `memory_store_keys_sources_by_document_path` in `crates/gwiki/src/store.rs`. [crates/gwiki/src/store.rs:121-135] |
