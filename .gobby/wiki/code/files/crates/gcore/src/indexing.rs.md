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

This file defines the generic indexing primitives shared by consumer crates. It provides `WalkerSettings` for configuring an `ignore::WalkBuilder` over a root path with gitignore handling, file-size limits, and extra ignore overrides; SHA-256 helpers for hashing bytes and file contents; and `Chunk`/`ChunkIdentity` types for describing file slices by path and byte range, with `Chunk::identity()` reducing a chunk to its stable locator.

It also includes incremental indexing support via `IndexEvent` and `index_events_from_hashes`, which compares previous and current path-hash maps to classify files as added, changed, unchanged, deleted, or skipped. Supporting helpers like `write_file` and `rels` are used by tests, and the test module verifies walker defaults and ignore behavior, hashing correctness, chunk identity semantics, incremental event classification, and that the indexing feature stays generic without domain parser dependencies.
[crates/gcore/src/indexing.rs:17-26]
[crates/gcore/src/indexing.rs:28-67]
[crates/gcore/src/indexing.rs:30-37]
[crates/gcore/src/indexing.rs:43-46]
[crates/gcore/src/indexing.rs:49-66]

## API Symbols

- `WalkerSettings` (class) component `WalkerSettings [class]` (`d7ac6eae-f122-5d46-bb09-757ed4e27fc5`) lines 17-26 [crates/gcore/src/indexing.rs:17-26]
  - Signature: `pub struct WalkerSettings {`
  - Purpose: 'WalkerSettings' configures a filesystem walker with a root path, a flag controlling whether Git ignore rules are honored, an optional maximum yielded file size in bytes, and a list of additional ignore glob patterns. [crates/gcore/src/indexing.rs:17-26]
- `WalkerSettings` (class) component `WalkerSettings [class]` (`0ffb7807-7c0e-5e36-9781-3c849bf9f7be`) lines 28-67 [crates/gcore/src/indexing.rs:28-67]
  - Signature: `impl WalkerSettings {`
  - Purpose: 'WalkerSettings' is a configuration wrapper for constructing an 'ignore::WalkBuilder' from a root path, controlling Git ignore behavior, optional maximum file size, and additional ignore override globs, with a fallible builder path for invalid patterns. [crates/gcore/src/indexing.rs:28-67]
- `WalkerSettings.new` (method) component `WalkerSettings.new [method]` (`4ceaa24c-a90c-5d5d-a607-fed9f6f177b1`) lines 30-37 [crates/gcore/src/indexing.rs:30-37]
  - Signature: `pub fn new(root: impl Into<PathBuf>) -> Self {`
  - Purpose: Constructs a new instance with 'root' set from the provided path, 'respect_gitignore' enabled, no maximum file size limit, and an empty 'extra_ignores' list. [crates/gcore/src/indexing.rs:30-37]
- `WalkerSettings.into_walker` (method) component `WalkerSettings.into_walker [method]` (`78390e00-a4c3-5fac-b1e5-3cc759cbab8e`) lines 43-46 [crates/gcore/src/indexing.rs:43-46]
  - Signature: `pub fn into_walker(self) -> WalkBuilder {`
  - Purpose: Consumes 'self', converts it via 'try_into_walker', and panics with '"invalid extra ignore pattern"' if the conversion fails. [crates/gcore/src/indexing.rs:43-46]
- `WalkerSettings.try_into_walker` (method) component `WalkerSettings.try_into_walker [method]` (`0485182d-7291-583d-9864-ae3dc9c71bd9`) lines 49-66 [crates/gcore/src/indexing.rs:49-66]
  - Signature: `pub fn try_into_walker(self) -> Result<WalkBuilder, ignore::Error> {`
  - Purpose: Builds a 'WalkBuilder' rooted at 'self.root', configures Git ignore/global/exclude handling and 'max_filesize' from the instance settings, optionally installs override rules that negate each 'extra_ignores' pattern, and returns the configured builder or an 'ignore::Error'. [crates/gcore/src/indexing.rs:49-66]
- `content_hash` (function) component `content_hash [function]` (`4da4f9c9-1b93-5b1d-bffa-bed6859dd496`) lines 70-74 [crates/gcore/src/indexing.rs:70-74]
  - Signature: `pub fn content_hash(data: &[u8]) -> String {`
  - Purpose: Computes the SHA-256 digest of the input byte slice and returns it as a hexadecimal string. [crates/gcore/src/indexing.rs:70-74]
- `file_content_hash` (function) component `file_content_hash [function]` (`f33f529e-e4f0-5a7c-b476-38a8f44172be`) lines 77-91 [crates/gcore/src/indexing.rs:77-91]
  - Signature: `pub fn file_content_hash(path: impl AsRef<Path>) -> io::Result<String> {`
  - Purpose: Opens the file at 'path', streams its contents into a SHA-256 hasher in 64 KiB chunks, and returns the resulting hex-encoded digest as an 'io::Result<String>'. [crates/gcore/src/indexing.rs:77-91]
- `hex_digest` (function) component `hex_digest [function]` (`a6f6b0b5-d5f6-5a0d-8f9c-6a02925bc490`) lines 93-100 [crates/gcore/src/indexing.rs:93-100]
  - Signature: `fn hex_digest(digest: impl AsRef<[u8]>) -> String {`
  - Purpose: Converts the input byte slice into a lowercase hexadecimal 'String' by preallocating '2 * len' capacity and formatting each byte as two hex digits. [crates/gcore/src/indexing.rs:93-100]
- `Chunk` (class) component `Chunk [class]` (`4b89220e-2803-5a21-a2f6-26b1965fa989`) lines 104-115 [crates/gcore/src/indexing.rs:104-115]
  - Signature: `pub struct Chunk {`
  - Purpose: 'Chunk' is a data-carrying struct that identifies a file slice by path and inclusive/exclusive byte offsets, with optional heading text and opaque JSON metadata. [crates/gcore/src/indexing.rs:104-115]
- `ChunkIdentity` (class) component `ChunkIdentity [class]` (`57151e9e-9cbc-5484-8590-89f234d7c844`) lines 119-126 [crates/gcore/src/indexing.rs:119-126]
  - Signature: `pub struct ChunkIdentity {`
  - Purpose: 'ChunkIdentity' is a file-chunk locator that identifies a segment of a source file by its 'PathBuf' and inclusive/exclusive byte range ('byte_start' to 'byte_end'). [crates/gcore/src/indexing.rs:119-126]
- `Chunk` (class) component `Chunk [class]` (`46e65fe0-99fb-577f-b50a-241d678809d0`) lines 128-137 [crates/gcore/src/indexing.rs:128-137]
  - Signature: `impl Chunk {`
  - Purpose: 'Chunk' exposes an 'identity()' method that constructs and returns a 'ChunkIdentity' from the chunk’s 'file_path', 'byte_start', and 'byte_end', providing a domain-independent identifier for the chunk. [crates/gcore/src/indexing.rs:128-137]
- `Chunk.identity` (method) component `Chunk.identity [method]` (`82a71d0e-03fc-5256-9ea8-1c7e691a0f15`) lines 130-136 [crates/gcore/src/indexing.rs:130-136]
  - Signature: `pub fn identity(&self) -> ChunkIdentity {`
  - Purpose: Returns a 'ChunkIdentity' cloned from the chunk’s 'file_path' and copied 'byte_start'/'byte_end' offsets, preserving its source span. [crates/gcore/src/indexing.rs:130-136]
- `IndexEvent` (type) component `IndexEvent [type]` (`8372bebf-462b-5e98-bdd3-3ed294996e6a`) lines 141-147 [crates/gcore/src/indexing.rs:141-147]
  - Signature: `pub enum IndexEvent {`
  - Purpose: Indexed type `IndexEvent` in `crates/gcore/src/indexing.rs`. [crates/gcore/src/indexing.rs:141-147]
- `index_events_from_hashes` (function) component `index_events_from_hashes [function]` (`2e1d95e8-6fd6-5a1c-aa3a-d9474098f71a`) lines 150-173 [crates/gcore/src/indexing.rs:150-173]
  - Signature: `pub fn index_events_from_hashes(`
  - Purpose: It computes a deduplicated, sorted set of paths from two hash snapshots and returns an 'IndexEvent' for each path classified as 'Added', 'Changed', 'Unchanged', or 'Deleted' based on the presence and equality of the previous and current hashes. [crates/gcore/src/indexing.rs:150-173]
- `write_file` (function) component `write_file [function]` (`dfefadbc-11dc-59f6-86e6-e78bc25da18c`) lines 183-189 [crates/gcore/src/indexing.rs:183-189]
  - Signature: `fn write_file(root: &Path, rel: &str, contents: &[u8]) {`
  - Purpose: Creates any missing parent directories under 'root' for 'rel', then writes 'contents' to the joined path, panicking on directory creation or write failure. [crates/gcore/src/indexing.rs:183-189]
- `rels` (function) component `rels [function]` (`297a8e4d-3893-5dca-ae2c-8983b5b652b3`) lines 191-208 [crates/gcore/src/indexing.rs:191-208]
  - Signature: `fn rels(root: &Path, settings: WalkerSettings) -> Vec<String> {`
  - Purpose: 'rels' walks the configured tree under 'root', collects each file path relative to 'root' as a 'String', sorts the resulting list lexicographically, and returns it. [crates/gcore/src/indexing.rs:191-208]
- `walker_settings_new_has_consumer_extendable_defaults` (function) component `walker_settings_new_has_consumer_extendable_defaults [function]` (`87060161-3797-5fa6-b869-c81e67502166`) lines 211-220 [crates/gcore/src/indexing.rs:211-220]
  - Signature: `fn walker_settings_new_has_consumer_extendable_defaults() {`
  - Purpose: Verifies that 'WalkerSettings::new(&root)' preserves the provided root path and initializes consumer-extensible defaults: 'respect_gitignore' enabled, 'max_filesize' unset, and 'extra_ignores' empty. [crates/gcore/src/indexing.rs:211-220]
- `walker_settings_apply_generic_discovery_rules` (function) component `walker_settings_apply_generic_discovery_rules [function]` (`1e1eb17c-1931-5fa1-972d-f9b766c180e1`) lines 223-241 [crates/gcore/src/indexing.rs:223-241]
  - Signature: `fn walker_settings_apply_generic_discovery_rules() {`
  - Purpose: Verifies that 'WalkerSettings' discovery respects '.gitignore', enforces 'max_filesize', and applies 'extra_ignores' so only 'keep.txt' is returned. [crates/gcore/src/indexing.rs:223-241]
- `content_hash_returns_sha256_hex` (function) component `content_hash_returns_sha256_hex [function]` (`d0415050-086b-5c9a-b45d-8c7f82c0fcdb`) lines 244-249 [crates/gcore/src/indexing.rs:244-249]
  - Signature: `fn content_hash_returns_sha256_hex() {`
  - Purpose: Verifies that 'content_hash(b"hello")' returns the expected SHA-256 hex digest string '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'. [crates/gcore/src/indexing.rs:244-249]
- `file_content_hash_returns_sha256_hex` (function) component `file_content_hash_returns_sha256_hex [function]` (`484caab4-bda1-53de-bb73-87861d7350b1`) lines 252-262 [crates/gcore/src/indexing.rs:252-262]
  - Signature: `fn file_content_hash_returns_sha256_hex() -> std::io::Result<()> {`
  - Purpose: Verifies that 'file_content_hash' returns the expected SHA-256 hex digest for a file containing 'b"hello"' by asserting it equals '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'. [crates/gcore/src/indexing.rs:252-262]
- `chunk_metadata_is_opaque` (function) component `chunk_metadata_is_opaque [function]` (`3922fe6c-53b6-5fc9-b554-c3c2248f7ce9`) lines 265-284 [crates/gcore/src/indexing.rs:265-284]
  - Signature: `fn chunk_metadata_is_opaque() {`
  - Purpose: Verifies that a 'Chunk' preserves its 'metadata' field verbatim, treating the JSON metadata as an opaque value rather than transforming or interpreting it. [crates/gcore/src/indexing.rs:265-284]
- `chunk_identity_uses_path_and_byte_range_only` (function) component `chunk_identity_uses_path_and_byte_range_only [function]` (`bee59801-0d74-5edb-9b50-eac220a2c961`) lines 287-309 [crates/gcore/src/indexing.rs:287-309]
  - Signature: `fn chunk_identity_uses_path_and_byte_range_only() {`
  - Purpose: Verifies that 'Chunk::identity()' depends only on 'file_path' and the '[byte_start, byte_end)' range, ignoring 'heading' and 'metadata', by asserting equal identity for identical path/range and different identity when the byte range changes. [crates/gcore/src/indexing.rs:287-309]
- `index_events_cover_incremental_cases` (function) component `index_events_cover_incremental_cases [function]` (`d98ee6aa-4176-5971-9f2f-de9e01146477`) lines 312-333 [crates/gcore/src/indexing.rs:312-333]
  - Signature: `fn index_events_cover_incremental_cases() {`
  - Purpose: Verifies that 'IndexEvent' correctly represents the incremental cases 'Added', 'Changed', 'Unchanged', 'Deleted', and 'Skipped', including matching the skipped event’s 'path' and 'reason' fields. [crates/gcore/src/indexing.rs:312-333]
- `index_events_from_hashes_classify_incremental_flow` (function) component `index_events_from_hashes_classify_incremental_flow [function]` (`b48e4cbd-3e62-50a9-be6e-7e6ea6150141`) lines 336-357 [crates/gcore/src/indexing.rs:336-357]
  - Signature: `fn index_events_from_hashes_classify_incremental_flow() {`
  - Purpose: Verifies that 'index_events_from_hashes' correctly classifies files across previous and current hash maps as 'Added', 'Changed', 'Deleted', or 'Unchanged' based on path presence and content hash differences. [crates/gcore/src/indexing.rs:336-357]
- `no_domain_parser_dependency` (function) component `no_domain_parser_dependency [function]` (`722eefa1-f7d5-53ca-86ab-a6d0c7606e94`) lines 360-365 [crates/gcore/src/indexing.rs:360-365]
  - Signature: `fn no_domain_parser_dependency() {`
  - Purpose: Reads the crate’s 'Cargo.toml' from 'CARGO_MANIFEST_DIR' and asserts that it does not contain the string 'tree-sitter', enforcing the absence of a domain parser dependency. [crates/gcore/src/indexing.rs:360-365]
- `manifest_keeps_indexing_feature_generic` (function) component `manifest_keeps_indexing_feature_generic [function]` (`f69d1a62-483c-58ba-9826-1fe15b24d0b5`) lines 368-397 [crates/gcore/src/indexing.rs:368-397]
  - Signature: `fn manifest_keeps_indexing_feature_generic() {`
  - Purpose: Verifies that 'Cargo.toml' contains exactly one '[features]' section and that the 'indexing' feature includes 'dep:ignore' and 'dep:sha2' while excluding 'tree-sitter', 'markdown', and 'wiki' dependencies. [crates/gcore/src/indexing.rs:368-397]

