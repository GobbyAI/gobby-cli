---
title: crates/gcore/src/indexing.rs
type: code_file
provenance:
- file: crates/gcore/src/indexing.rs
  ranges:
  - 17-26
  - 28-67
  - 70-74
  - 77-91
  - 93-100
  - 104-115
  - 119-126
  - 128-137
  - 141-147
  - 150-173
  - 183-189
  - 191-208
  - 211-220
  - 223-241
  - 244-249
  - 252-262
  - 265-284
  - 287-309
  - 312-333
  - 336-357
  - 360-365
  - 368-397
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/indexing.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Generic indexing utilities shared by consumer crates. It defines `WalkerSettings` to configure an `ignore::WalkBuilder` with gitignore handling, file-size limits, and extra ignore patterns; hashing helpers for file content and whole files to drive incremental change detection; `Chunk` and `ChunkIdentity` to represent indexed file slices and their stable identity; and `IndexEvent` plus `index_events_from_hashes` to classify hash differences into indexing actions. The remaining helpers write indexed file output, build relationship data, and the tests verify the defaults, hashing behavior, opaque chunk metadata, identity rules, incremental event coverage, and that the feature stays parser-agnostic.
[crates/gcore/src/indexing.rs:17-26]
[crates/gcore/src/indexing.rs:28-67]
[crates/gcore/src/indexing.rs:30-37]
[crates/gcore/src/indexing.rs:43-46]
[crates/gcore/src/indexing.rs:49-66]

## API Symbols

- `WalkerSettings` (class) component `WalkerSettings [class]` (`d7ac6eae-f122-5d46-bb09-757ed4e27fc5`) lines 17-26 [crates/gcore/src/indexing.rs:17-26]
  - Signature: `pub struct WalkerSettings {`
  - Purpose: Indexed class `WalkerSettings` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:17-26]
- `WalkerSettings` (class) component `WalkerSettings [class]` (`0ffb7807-7c0e-5e36-9781-3c849bf9f7be`) lines 28-67 [crates/gcore/src/indexing.rs:28-67]
  - Signature: `impl WalkerSettings {`
  - Purpose: Indexed class `WalkerSettings` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:28-67]
- `WalkerSettings.new` (method) component `WalkerSettings.new [method]` (`4ceaa24c-a90c-5d5d-a607-fed9f6f177b1`) lines 30-37 [crates/gcore/src/indexing.rs:30-37]
  - Signature: `pub fn new(root: impl Into<PathBuf>) -> Self {`
  - Purpose: Indexed method `WalkerSettings.new` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:30-37]
- `WalkerSettings.into_walker` (method) component `WalkerSettings.into_walker [method]` (`78390e00-a4c3-5fac-b1e5-3cc759cbab8e`) lines 43-46 [crates/gcore/src/indexing.rs:43-46]
  - Signature: `pub fn into_walker(self) -> WalkBuilder {`
  - Purpose: Indexed method `WalkerSettings.into_walker` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:43-46]
- `WalkerSettings.try_into_walker` (method) component `WalkerSettings.try_into_walker [method]` (`0485182d-7291-583d-9864-ae3dc9c71bd9`) lines 49-66 [crates/gcore/src/indexing.rs:49-66]
  - Signature: `pub fn try_into_walker(self) -> Result<WalkBuilder, ignore::Error> {`
  - Purpose: Indexed method `WalkerSettings.try_into_walker` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:49-66]
- `content_hash` (function) component `content_hash [function]` (`4da4f9c9-1b93-5b1d-bffa-bed6859dd496`) lines 70-74 [crates/gcore/src/indexing.rs:70-74]
  - Signature: `pub fn content_hash(data: &[u8]) -> String {`
  - Purpose: Indexed function `content_hash` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:70-74]
- `file_content_hash` (function) component `file_content_hash [function]` (`f33f529e-e4f0-5a7c-b476-38a8f44172be`) lines 77-91 [crates/gcore/src/indexing.rs:77-91]
  - Signature: `pub fn file_content_hash(path: impl AsRef<Path>) -> io::Result<String> {`
  - Purpose: Indexed function `file_content_hash` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:77-91]
- `hex_digest` (function) component `hex_digest [function]` (`a6f6b0b5-d5f6-5a0d-8f9c-6a02925bc490`) lines 93-100 [crates/gcore/src/indexing.rs:93-100]
  - Signature: `fn hex_digest(digest: impl AsRef<[u8]>) -> String {`
  - Purpose: Indexed function `hex_digest` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:93-100]
- `Chunk` (class) component `Chunk [class]` (`4b89220e-2803-5a21-a2f6-26b1965fa989`) lines 104-115 [crates/gcore/src/indexing.rs:104-115]
  - Signature: `pub struct Chunk {`
  - Purpose: Indexed class `Chunk` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:104-115]
- `ChunkIdentity` (class) component `ChunkIdentity [class]` (`57151e9e-9cbc-5484-8590-89f234d7c844`) lines 119-126 [crates/gcore/src/indexing.rs:119-126]
  - Signature: `pub struct ChunkIdentity {`
  - Purpose: Indexed class `ChunkIdentity` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:119-126]
- `Chunk` (class) component `Chunk [class]` (`46e65fe0-99fb-577f-b50a-241d678809d0`) lines 128-137 [crates/gcore/src/indexing.rs:128-137]
  - Signature: `impl Chunk {`
  - Purpose: Indexed class `Chunk` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:128-137]
- `Chunk.identity` (method) component `Chunk.identity [method]` (`82a71d0e-03fc-5256-9ea8-1c7e691a0f15`) lines 130-136 [crates/gcore/src/indexing.rs:130-136]
  - Signature: `pub fn identity(&self) -> ChunkIdentity {`
  - Purpose: Indexed method `Chunk.identity` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:130-136]
- `IndexEvent` (type) component `IndexEvent [type]` (`8372bebf-462b-5e98-bdd3-3ed294996e6a`) lines 141-147 [crates/gcore/src/indexing.rs:141-147]
  - Signature: `pub enum IndexEvent {`
  - Purpose: Indexed type `IndexEvent` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:141-147]
- `index_events_from_hashes` (function) component `index_events_from_hashes [function]` (`2e1d95e8-6fd6-5a1c-aa3a-d9474098f71a`) lines 150-173 [crates/gcore/src/indexing.rs:150-173]
  - Signature: `pub fn index_events_from_hashes(`
  - Purpose: Indexed function `index_events_from_hashes` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:150-173]
- `write_file` (function) component `write_file [function]` (`dfefadbc-11dc-59f6-86e6-e78bc25da18c`) lines 183-189 [crates/gcore/src/indexing.rs:183-189]
  - Signature: `fn write_file(root: &Path, rel: &str, contents: &[u8]) {`
  - Purpose: Indexed function `write_file` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:183-189]
- `rels` (function) component `rels [function]` (`297a8e4d-3893-5dca-ae2c-8983b5b652b3`) lines 191-208 [crates/gcore/src/indexing.rs:191-208]
  - Signature: `fn rels(root: &Path, settings: WalkerSettings) -> Vec<String> {`
  - Purpose: Indexed function `rels` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:191-208]
- `walker_settings_new_has_consumer_extendable_defaults` (function) component `walker_settings_new_has_consumer_extendable_defaults [function]` (`87060161-3797-5fa6-b869-c81e67502166`) lines 211-220 [crates/gcore/src/indexing.rs:211-220]
  - Signature: `fn walker_settings_new_has_consumer_extendable_defaults() {`
  - Purpose: Indexed function `walker_settings_new_has_consumer_extendable_defaults` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:211-220]
- `walker_settings_apply_generic_discovery_rules` (function) component `walker_settings_apply_generic_discovery_rules [function]` (`1e1eb17c-1931-5fa1-972d-f9b766c180e1`) lines 223-241 [crates/gcore/src/indexing.rs:223-241]
  - Signature: `fn walker_settings_apply_generic_discovery_rules() {`
  - Purpose: Indexed function `walker_settings_apply_generic_discovery_rules` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:223-241]
- `content_hash_returns_sha256_hex` (function) component `content_hash_returns_sha256_hex [function]` (`d0415050-086b-5c9a-b45d-8c7f82c0fcdb`) lines 244-249 [crates/gcore/src/indexing.rs:244-249]
  - Signature: `fn content_hash_returns_sha256_hex() {`
  - Purpose: Indexed function `content_hash_returns_sha256_hex` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:244-249]
- `file_content_hash_returns_sha256_hex` (function) component `file_content_hash_returns_sha256_hex [function]` (`484caab4-bda1-53de-bb73-87861d7350b1`) lines 252-262 [crates/gcore/src/indexing.rs:252-262]
  - Signature: `fn file_content_hash_returns_sha256_hex() -> std::io::Result<()> {`
  - Purpose: Indexed function `file_content_hash_returns_sha256_hex` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:252-262]
- `chunk_metadata_is_opaque` (function) component `chunk_metadata_is_opaque [function]` (`3922fe6c-53b6-5fc9-b554-c3c2248f7ce9`) lines 265-284 [crates/gcore/src/indexing.rs:265-284]
  - Signature: `fn chunk_metadata_is_opaque() {`
  - Purpose: Indexed function `chunk_metadata_is_opaque` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:265-284]
- `chunk_identity_uses_path_and_byte_range_only` (function) component `chunk_identity_uses_path_and_byte_range_only [function]` (`bee59801-0d74-5edb-9b50-eac220a2c961`) lines 287-309 [crates/gcore/src/indexing.rs:287-309]
  - Signature: `fn chunk_identity_uses_path_and_byte_range_only() {`
  - Purpose: Indexed function `chunk_identity_uses_path_and_byte_range_only` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:287-309]
- `index_events_cover_incremental_cases` (function) component `index_events_cover_incremental_cases [function]` (`d98ee6aa-4176-5971-9f2f-de9e01146477`) lines 312-333 [crates/gcore/src/indexing.rs:312-333]
  - Signature: `fn index_events_cover_incremental_cases() {`
  - Purpose: Indexed function `index_events_cover_incremental_cases` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:312-333]
- `index_events_from_hashes_classify_incremental_flow` (function) component `index_events_from_hashes_classify_incremental_flow [function]` (`b48e4cbd-3e62-50a9-be6e-7e6ea6150141`) lines 336-357 [crates/gcore/src/indexing.rs:336-357]
  - Signature: `fn index_events_from_hashes_classify_incremental_flow() {`
  - Purpose: Indexed function `index_events_from_hashes_classify_incremental_flow` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:336-357]
- `no_domain_parser_dependency` (function) component `no_domain_parser_dependency [function]` (`722eefa1-f7d5-53ca-86ab-a6d0c7606e94`) lines 360-365 [crates/gcore/src/indexing.rs:360-365]
  - Signature: `fn no_domain_parser_dependency() {`
  - Purpose: Indexed function `no_domain_parser_dependency` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:360-365]
- `manifest_keeps_indexing_feature_generic` (function) component `manifest_keeps_indexing_feature_generic [function]` (`f69d1a62-483c-58ba-9826-1fe15b24d0b5`) lines 368-397 [crates/gcore/src/indexing.rs:368-397]
  - Signature: `fn manifest_keeps_indexing_feature_generic() {`
  - Purpose: Indexed function `manifest_keeps_indexing_feature_generic` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:368-397]

