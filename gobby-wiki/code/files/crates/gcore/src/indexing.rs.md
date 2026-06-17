---
title: crates/gcore/src/indexing.rs
type: code_file
provenance:
- file: crates/gcore/src/indexing.rs
  ranges:
  - 17-26
  - 30-37
  - 43-46
  - 49-66
  - 70-74
  - 77-91
  - 93-100
  - 104-115
  - 119-126
  - 130-136
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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/indexing.rs:17-26](crates/gcore/src/indexing.rs#L17-L26), [crates/gcore/src/indexing.rs:30-37](crates/gcore/src/indexing.rs#L30-L37), [crates/gcore/src/indexing.rs:43-46](crates/gcore/src/indexing.rs#L43-L46), [crates/gcore/src/indexing.rs:49-66](crates/gcore/src/indexing.rs#L49-L66), [crates/gcore/src/indexing.rs:70-74](crates/gcore/src/indexing.rs#L70-L74), [crates/gcore/src/indexing.rs:77-91](crates/gcore/src/indexing.rs#L77-L91), [crates/gcore/src/indexing.rs:93-100](crates/gcore/src/indexing.rs#L93-L100), [crates/gcore/src/indexing.rs:104-115](crates/gcore/src/indexing.rs#L104-L115), [crates/gcore/src/indexing.rs:119-126](crates/gcore/src/indexing.rs#L119-L126), [crates/gcore/src/indexing.rs:130-136](crates/gcore/src/indexing.rs#L130-L136), [crates/gcore/src/indexing.rs:141-147](crates/gcore/src/indexing.rs#L141-L147), [crates/gcore/src/indexing.rs:150-173](crates/gcore/src/indexing.rs#L150-L173), [crates/gcore/src/indexing.rs:183-189](crates/gcore/src/indexing.rs#L183-L189), [crates/gcore/src/indexing.rs:191-208](crates/gcore/src/indexing.rs#L191-L208), [crates/gcore/src/indexing.rs:211-220](crates/gcore/src/indexing.rs#L211-L220), [crates/gcore/src/indexing.rs:223-241](crates/gcore/src/indexing.rs#L223-L241), [crates/gcore/src/indexing.rs:244-249](crates/gcore/src/indexing.rs#L244-L249), [crates/gcore/src/indexing.rs:252-262](crates/gcore/src/indexing.rs#L252-L262), [crates/gcore/src/indexing.rs:265-284](crates/gcore/src/indexing.rs#L265-L284), [crates/gcore/src/indexing.rs:287-309](crates/gcore/src/indexing.rs#L287-L309), [crates/gcore/src/indexing.rs:312-333](crates/gcore/src/indexing.rs#L312-L333), [crates/gcore/src/indexing.rs:336-357](crates/gcore/src/indexing.rs#L336-L357), [crates/gcore/src/indexing.rs:360-365](crates/gcore/src/indexing.rs#L360-L365), [crates/gcore/src/indexing.rs:368-397](crates/gcore/src/indexing.rs#L368-L397)

</details>

# crates/gcore/src/indexing.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Provides the generic indexing utilities shared by consumer crates when the `indexing` feature is enabled. It defines `WalkerSettings` for building an `ignore::WalkBuilder` with configurable gitignore handling, file-size limits, and extra ignore globs, plus helper functions for SHA-256 hashing and hex encoding. The file also defines chunk and chunk-identity types, derives index events from file hashes and relations, and includes tests that verify the walker defaults, hash output, opaque chunk metadata, identity rules, incremental event classification, and that the module stays free of domain-specific parser dependencies.
[crates/gcore/src/indexing.rs:17-26]
[crates/gcore/src/indexing.rs:30-37]
[crates/gcore/src/indexing.rs:43-46]
[crates/gcore/src/indexing.rs:49-66]
[crates/gcore/src/indexing.rs:70-74]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `WalkerSettings` | class | `pub struct WalkerSettings {` | `WalkerSettings [class]` | `d7ac6eae-f122-5d46-bb09-757ed4e27fc5` | 17-26 [crates/gcore/src/indexing.rs:17-26] | Indexed class `WalkerSettings` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:17-26] |
| `WalkerSettings::new` | method | `pub fn new(root: impl Into<PathBuf>) -> Self {` | `WalkerSettings::new [method]` | `4ceaa24c-a90c-5d5d-a607-fed9f6f177b1` | 30-37 [crates/gcore/src/indexing.rs:30-37] | Indexed method `WalkerSettings::new` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:30-37] |
| `WalkerSettings::into_walker` | method | `pub fn into_walker(self) -> WalkBuilder {` | `WalkerSettings::into_walker [method]` | `78390e00-a4c3-5fac-b1e5-3cc759cbab8e` | 43-46 [crates/gcore/src/indexing.rs:43-46] | Indexed method `WalkerSettings::into_walker` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:43-46] |
| `WalkerSettings::try_into_walker` | method | `pub fn try_into_walker(self) -> Result<WalkBuilder, ignore::Error> {` | `WalkerSettings::try_into_walker [method]` | `0485182d-7291-583d-9864-ae3dc9c71bd9` | 49-66 [crates/gcore/src/indexing.rs:49-66] | Indexed method `WalkerSettings::try_into_walker` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:49-66] |
| `content_hash` | function | `pub fn content_hash(data: &[u8]) -> String {` | `content_hash [function]` | `4da4f9c9-1b93-5b1d-bffa-bed6859dd496` | 70-74 [crates/gcore/src/indexing.rs:70-74] | Indexed function `content_hash` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:70-74] |
| `file_content_hash` | function | `pub fn file_content_hash(path: impl AsRef<Path>) -> io::Result<String> {` | `file_content_hash [function]` | `f33f529e-e4f0-5a7c-b476-38a8f44172be` | 77-91 [crates/gcore/src/indexing.rs:77-91] | Indexed function `file_content_hash` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:77-91] |
| `hex_digest` | function | `fn hex_digest(digest: impl AsRef<[u8]>) -> String {` | `hex_digest [function]` | `a6f6b0b5-d5f6-5a0d-8f9c-6a02925bc490` | 93-100 [crates/gcore/src/indexing.rs:93-100] | Indexed function `hex_digest` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:93-100] |
| `Chunk` | class | `pub struct Chunk {` | `Chunk [class]` | `4b89220e-2803-5a21-a2f6-26b1965fa989` | 104-115 [crates/gcore/src/indexing.rs:104-115] | Indexed class `Chunk` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:104-115] |
| `ChunkIdentity` | class | `pub struct ChunkIdentity {` | `ChunkIdentity [class]` | `57151e9e-9cbc-5484-8590-89f234d7c844` | 119-126 [crates/gcore/src/indexing.rs:119-126] | Indexed class `ChunkIdentity` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:119-126] |
| `Chunk::identity` | method | `pub fn identity(&self) -> ChunkIdentity {` | `Chunk::identity [method]` | `82a71d0e-03fc-5256-9ea8-1c7e691a0f15` | 130-136 [crates/gcore/src/indexing.rs:130-136] | Indexed method `Chunk::identity` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:130-136] |
| `IndexEvent` | type | `pub enum IndexEvent {` | `IndexEvent [type]` | `8372bebf-462b-5e98-bdd3-3ed294996e6a` | 141-147 [crates/gcore/src/indexing.rs:141-147] | Indexed type `IndexEvent` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:141-147] |
| `index_events_from_hashes` | function | `pub fn index_events_from_hashes(` | `index_events_from_hashes [function]` | `2e1d95e8-6fd6-5a1c-aa3a-d9474098f71a` | 150-173 [crates/gcore/src/indexing.rs:150-173] | Indexed function `index_events_from_hashes` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:150-173] |
| `write_file` | function | `fn write_file(root: &Path, rel: &str, contents: &[u8]) {` | `write_file [function]` | `dfefadbc-11dc-59f6-86e6-e78bc25da18c` | 183-189 [crates/gcore/src/indexing.rs:183-189] | Indexed function `write_file` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:183-189] |
| `rels` | function | `fn rels(root: &Path, settings: WalkerSettings) -> Vec<String> {` | `rels [function]` | `297a8e4d-3893-5dca-ae2c-8983b5b652b3` | 191-208 [crates/gcore/src/indexing.rs:191-208] | Indexed function `rels` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:191-208] |
| `walker_settings_new_has_consumer_extendable_defaults` | function | `fn walker_settings_new_has_consumer_extendable_defaults() {` | `walker_settings_new_has_consumer_extendable_defaults [function]` | `87060161-3797-5fa6-b869-c81e67502166` | 211-220 [crates/gcore/src/indexing.rs:211-220] | Indexed function `walker_settings_new_has_consumer_extendable_defaults` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:211-220] |
| `walker_settings_apply_generic_discovery_rules` | function | `fn walker_settings_apply_generic_discovery_rules() {` | `walker_settings_apply_generic_discovery_rules [function]` | `1e1eb17c-1931-5fa1-972d-f9b766c180e1` | 223-241 [crates/gcore/src/indexing.rs:223-241] | Indexed function `walker_settings_apply_generic_discovery_rules` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:223-241] |
| `content_hash_returns_sha256_hex` | function | `fn content_hash_returns_sha256_hex() {` | `content_hash_returns_sha256_hex [function]` | `d0415050-086b-5c9a-b45d-8c7f82c0fcdb` | 244-249 [crates/gcore/src/indexing.rs:244-249] | Indexed function `content_hash_returns_sha256_hex` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:244-249] |
| `file_content_hash_returns_sha256_hex` | function | `fn file_content_hash_returns_sha256_hex() -> std::io::Result<()> {` | `file_content_hash_returns_sha256_hex [function]` | `484caab4-bda1-53de-bb73-87861d7350b1` | 252-262 [crates/gcore/src/indexing.rs:252-262] | Indexed function `file_content_hash_returns_sha256_hex` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:252-262] |
| `chunk_metadata_is_opaque` | function | `fn chunk_metadata_is_opaque() {` | `chunk_metadata_is_opaque [function]` | `3922fe6c-53b6-5fc9-b554-c3c2248f7ce9` | 265-284 [crates/gcore/src/indexing.rs:265-284] | Indexed function `chunk_metadata_is_opaque` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:265-284] |
| `chunk_identity_uses_path_and_byte_range_only` | function | `fn chunk_identity_uses_path_and_byte_range_only() {` | `chunk_identity_uses_path_and_byte_range_only [function]` | `bee59801-0d74-5edb-9b50-eac220a2c961` | 287-309 [crates/gcore/src/indexing.rs:287-309] | Indexed function `chunk_identity_uses_path_and_byte_range_only` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:287-309] |
| `index_events_cover_incremental_cases` | function | `fn index_events_cover_incremental_cases() {` | `index_events_cover_incremental_cases [function]` | `d98ee6aa-4176-5971-9f2f-de9e01146477` | 312-333 [crates/gcore/src/indexing.rs:312-333] | Indexed function `index_events_cover_incremental_cases` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:312-333] |
| `index_events_from_hashes_classify_incremental_flow` | function | `fn index_events_from_hashes_classify_incremental_flow() {` | `index_events_from_hashes_classify_incremental_flow [function]` | `b48e4cbd-3e62-50a9-be6e-7e6ea6150141` | 336-357 [crates/gcore/src/indexing.rs:336-357] | Indexed function `index_events_from_hashes_classify_incremental_flow` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:336-357] |
| `no_domain_parser_dependency` | function | `fn no_domain_parser_dependency() {` | `no_domain_parser_dependency [function]` | `722eefa1-f7d5-53ca-86ab-a6d0c7606e94` | 360-365 [crates/gcore/src/indexing.rs:360-365] | Indexed function `no_domain_parser_dependency` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:360-365] |
| `manifest_keeps_indexing_feature_generic` | function | `fn manifest_keeps_indexing_feature_generic() {` | `manifest_keeps_indexing_feature_generic [function]` | `f69d1a62-483c-58ba-9826-1fe15b24d0b5` | 368-397 [crates/gcore/src/indexing.rs:368-397] | Indexed function `manifest_keeps_indexing_feature_generic` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:368-397] |
