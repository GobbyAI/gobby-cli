---
title: crates/gwiki/src/sources/manifest.rs
type: code_file
provenance:
- file: crates/gwiki/src/sources/manifest.rs
  ranges:
  - 23-25
  - 27-213
  - 215-253
  - 255-285
  - 287-291
  - 293-300
  - 302-311
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/sources/manifest.rs

Module: [[code/modules/crates/gwiki/src/sources|crates/gwiki/src/sources]]

## Purpose

`manifest.rs` manages the wiki vault’s source manifest as a persisted list of `SourceRecord` entries. It can read the manifest from the index file by scanning lines for generated source markers and deserializing the embedded JSON, or return an empty manifest when the file is missing. The registration methods turn `SourceDraft`s into records, compute or reuse content hashes, and deduplicate by canonical location plus content hash before writing changes back. Updates, removals, and writes all go through a manifest lock so the file is rewritten atomically while preserving non-generated prefix/suffix content around the rendered manifest block. The lock helpers and `SourceRecordParts` support that flow by coordinating exclusive access, retry timing, and record decomposition for persistence.
[crates/gwiki/src/sources/manifest.rs:23-25]
[crates/gwiki/src/sources/manifest.rs:27-213]
[crates/gwiki/src/sources/manifest.rs:28-66]
[crates/gwiki/src/sources/manifest.rs:68-71]
[crates/gwiki/src/sources/manifest.rs:73-92]

## API Symbols

- `SourceManifest` (class) component `SourceManifest [class]` (`838096cd-1be9-5ad6-83e2-5c01a2f67ac8`) lines 23-25 [crates/gwiki/src/sources/manifest.rs:23-25]
  - Signature: `pub struct SourceManifest {`
  - Purpose: `SourceManifest` is a public struct that encapsulates a collection of `SourceRecord` entries in a vector. [crates/gwiki/src/sources/manifest.rs:23-25]
- `SourceManifest` (class) component `SourceManifest [class]` (`0ba6eb85-a319-5ace-afbc-8150a665165f`) lines 27-213 [crates/gwiki/src/sources/manifest.rs:27-213]
  - Signature: `impl SourceManifest {`
  - Purpose: Indexed class `SourceManifest` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:27-213]
- `SourceManifest.read` (method) component `SourceManifest.read [method]` (`21efa115-c306-574d-a89a-dd384f131a47`) lines 28-66 [crates/gwiki/src/sources/manifest.rs:28-66]
  - Signature: `pub fn read(vault_root: &Path) -> Result<Self, WikiError> {`
  - Purpose: This method reads a vault index file and deserializes a collection of source records by extracting and parsing JSON entries delimited by markers from each line, returning a default instance if the file is absent. [crates/gwiki/src/sources/manifest.rs:28-66]
- `SourceManifest.register` (method) component `SourceManifest.register [method]` (`a63fd77c-0692-52fc-94a8-07f5f1aef241`) lines 68-71 [crates/gwiki/src/sources/manifest.rs:68-71]
  - Signature: `pub fn register(vault_root: &Path, draft: SourceDraft) -> Result<SourceRecord, WikiError> {`
  - Purpose: Registers a `SourceDraft` by computing its content hash and delegating to `register_with_content_hash`. [crates/gwiki/src/sources/manifest.rs:68-71]
- `SourceManifest.register_borrowed` (method) component `SourceManifest.register_borrowed [method]` (`4d78ce00-3e24-57f6-ab3f-5b51e95d20b6`) lines 73-92 [crates/gwiki/src/sources/manifest.rs:73-92]
  - Signature: `pub(crate) fn register_borrowed(`
  - Purpose: Computes a content hash for a borrowed source draft and registers its metadata components by delegating to `register_parts_with_content_hash`. [crates/gwiki/src/sources/manifest.rs:73-92]
- `SourceManifest.register_with_content_hash` (method) component `SourceManifest.register_with_content_hash [method]` (`49dd7a6b-43a0-5e34-90f7-bd5c78bcb64c`) lines 94-113 [crates/gwiki/src/sources/manifest.rs:94-113]
  - Signature: `pub fn register_with_content_hash(`
  - Purpose: Registers a SourceDraft with a provided content hash by decomposing it into SourceRecordParts and delegating to the parts-based registration method. [crates/gwiki/src/sources/manifest.rs:94-113]
- `SourceManifest.register_parts_with_content_hash` (method) component `SourceManifest.register_parts_with_content_hash [method]` (`722b360b-f71b-5232-a99c-cc119eb7fb8c`) lines 115-147 [crates/gwiki/src/sources/manifest.rs:115-147]
  - Signature: `fn register_parts_with_content_hash(`
  - Purpose: Registers a source record to a locked manifest with content-based deduplication by canonical location and content hash pair, returning either an existing matching record or a newly created and persisted one. [crates/gwiki/src/sources/manifest.rs:115-147]
- `SourceManifest.write` (method) component `SourceManifest.write [method]` (`fa76f27c-224a-5a6c-8ba1-c3f4a0117359`) lines 149-151 [crates/gwiki/src/sources/manifest.rs:149-151]
  - Signature: `pub fn write(&self, vault_root: &Path) -> Result<(), WikiError> {`
  - Purpose: Executes a thread-safe write to the vault by acquiring a manifest lock and delegating to an unlocked write implementation. [crates/gwiki/src/sources/manifest.rs:149-151]
- `SourceManifest.write_unlocked` (method) component `SourceManifest.write_unlocked [method]` (`86daa3b3-b195-5bb7-8c8e-91c63037142c`) lines 153-183 [crates/gwiki/src/sources/manifest.rs:153-183]
  - Signature: `fn write_unlocked(&self, vault_root: &Path) -> Result<(), WikiError> {`
  - Purpose: Atomically writes a wiki vault index file by preserving user-defined prefix and suffix content around a generated source manifest containing rendered entries between sentinel markers. [crates/gwiki/src/sources/manifest.rs:153-183]
- `SourceManifest.remove` (method) component `SourceManifest.remove [method]` (`b69f4896-6357-5679-8ef6-b3f05d22c2a7`) lines 185-195 [crates/gwiki/src/sources/manifest.rs:185-195]
  - Signature: `pub fn remove(vault_root: &Path, id: &str) -> Result<Option<SourceRecord>, WikiError> {`
  - Purpose: Atomically removes a SourceRecord entry from the vault manifest by ID, persists the change, and returns the removed entry or None if not found. [crates/gwiki/src/sources/manifest.rs:185-195]
- `SourceManifest.update` (method) component `SourceManifest.update [method]` (`09c70535-b2f1-5d8c-a26b-cefa4e2e25b3`) lines 197-208 [crates/gwiki/src/sources/manifest.rs:197-208]
  - Signature: `pub fn update(`
  - Purpose: Acquires a manifest lock, reads the SourceManifest, applies a mutation closure, and conditionally persists changes to disk if the closure returns true. [crates/gwiki/src/sources/manifest.rs:197-208]
- `SourceManifest.index_path` (method) component `SourceManifest.index_path [method]` (`2dc6ff46-1f6f-5b0b-a679-b845877e7cde`) lines 210-212 [crates/gwiki/src/sources/manifest.rs:210-212]
  - Signature: `pub fn index_path(vault_root: &Path) -> PathBuf {`
  - Purpose: Indexed method `SourceManifest.index_path` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:210-212]
- `with_manifest_lock` (function) component `with_manifest_lock [function]` (`dcab3658-49b7-53f5-8248-d07e6a9f3e35`) lines 215-253 [crates/gwiki/src/sources/manifest.rs:215-253]
  - Signature: `fn with_manifest_lock<T>(`
  - Purpose: Indexed function `with_manifest_lock` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:215-253]
- `lock_source_manifest` (function) component `lock_source_manifest [function]` (`1fe0585a-5198-590d-b63c-0fe3dc6d0c88`) lines 255-285 [crates/gwiki/src/sources/manifest.rs:255-285]
  - Signature: `fn lock_source_manifest(lock: &File, lock_path: &Path) -> Result<(), WikiError> {`
  - Purpose: Indexed function `lock_source_manifest` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:255-285]
- `try_lock_exclusive` (function) component `try_lock_exclusive [function]` (`bb5c9d2b-b880-56ce-9d80-142eeb0eb048`) lines 287-291 [crates/gwiki/src/sources/manifest.rs:287-291]
  - Signature: `fn try_lock_exclusive(lock: &File) -> Result<(), fs4::TryLockError> {`
  - Purpose: Indexed function `try_lock_exclusive` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:287-291]
- `source_manifest_lock_timeout` (function) component `source_manifest_lock_timeout [function]` (`11efb02f-d9a8-57e5-9544-9e2d23c9ee47`) lines 293-300 [crates/gwiki/src/sources/manifest.rs:293-300]
  - Signature: `fn source_manifest_lock_timeout() -> Duration {`
  - Purpose: Indexed function `source_manifest_lock_timeout` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:293-300]
- `SourceRecordParts` (class) component `SourceRecordParts [class]` (`c60f671f-3407-5aff-93d4-a72477521cca`) lines 302-311 [crates/gwiki/src/sources/manifest.rs:302-311]
  - Signature: `struct SourceRecordParts {`
  - Purpose: Indexed class `SourceRecordParts` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:302-311]

