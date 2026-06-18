---
title: crates/gcore/src/indexing.rs
type: code_file
provenance:
- file: crates/gcore/src/indexing.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/indexing.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/indexing.rs` exposes 24 indexed API symbols.

## How it fits

`crates/gcore/src/indexing.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `WalkerSettings` | class | Indexed class `WalkerSettings` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:17-26] |
| `WalkerSettings::new` | method | Indexed method `WalkerSettings::new` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:30-37] |
| `WalkerSettings::into_walker` | method | Indexed method `WalkerSettings::into_walker` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:43-46] |
| `WalkerSettings::try_into_walker` | method | Indexed method `WalkerSettings::try_into_walker` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:49-66] |
| `content_hash` | function | Indexed function `content_hash` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:70-74] |
| `file_content_hash` | function | Indexed function `file_content_hash` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:77-91] |
| `hex_digest` | function | Indexed function `hex_digest` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:93-100] |
| `Chunk` | class | Indexed class `Chunk` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:104-115] |
| `ChunkIdentity` | class | Indexed class `ChunkIdentity` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:119-126] |
| `Chunk::identity` | method | Indexed method `Chunk::identity` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:130-136] |
| `IndexEvent` | type | Indexed type `IndexEvent` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:141-147] |
| `index_events_from_hashes` | function | Indexed function `index_events_from_hashes` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:150-173] |
| `write_file` | function | Indexed function `write_file` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:183-189] |
| `rels` | function | Indexed function `rels` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:191-208] |
| `walker_settings_new_has_consumer_extendable_defaults` | function | Indexed function `walker_settings_new_has_consumer_extendable_defaults` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:211-220] |
| `walker_settings_apply_generic_discovery_rules` | function | Indexed function `walker_settings_apply_generic_discovery_rules` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:223-241] |
| `content_hash_returns_sha256_hex` | function | Indexed function `content_hash_returns_sha256_hex` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:244-249] |
| `file_content_hash_returns_sha256_hex` | function | Indexed function `file_content_hash_returns_sha256_hex` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:252-262] |
| `chunk_metadata_is_opaque` | function | Indexed function `chunk_metadata_is_opaque` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:265-284] |
| `chunk_identity_uses_path_and_byte_range_only` | function | Indexed function `chunk_identity_uses_path_and_byte_range_only` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:287-309] |
| `index_events_cover_incremental_cases` | function | Indexed function `index_events_cover_incremental_cases` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:312-333] |
| `index_events_from_hashes_classify_incremental_flow` | function | Indexed function `index_events_from_hashes_classify_incremental_flow` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:336-357] |
| `no_domain_parser_dependency` | function | Indexed function `no_domain_parser_dependency` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:360-365] |
| `manifest_keeps_indexing_feature_generic` | function | Indexed function `manifest_keeps_indexing_feature_generic` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:368-397] |

