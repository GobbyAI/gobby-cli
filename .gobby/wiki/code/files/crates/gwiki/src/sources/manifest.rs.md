---
title: crates/gwiki/src/sources/manifest.rs
type: code_file
provenance:
- file: crates/gwiki/src/sources/manifest.rs
  ranges:
  - 23-25
  - 27-225
  - 28-66
  - 68-71
  - 73-92
  - 94-113
  - 115-147
  - 149-151
  - 153-183
  - 185-195
  - 197-208
  - 215-220
  - 222-224
  - 227-265
  - 267-297
  - 299-303
  - 305-312
  - 314-323
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/sources/manifest.rs

Module: [[code/modules/crates/gwiki/src/sources|crates/gwiki/src/sources]]

## Purpose

`crates/gwiki/src/sources/manifest.rs` exposes 18 indexed API symbols.
[crates/gwiki/src/sources/manifest.rs:23-25]
[crates/gwiki/src/sources/manifest.rs:27-225]
[crates/gwiki/src/sources/manifest.rs:28-66]
[crates/gwiki/src/sources/manifest.rs:68-71]
[crates/gwiki/src/sources/manifest.rs:73-92]
[crates/gwiki/src/sources/manifest.rs:94-113]
[crates/gwiki/src/sources/manifest.rs:115-147]
[crates/gwiki/src/sources/manifest.rs:149-151]
[crates/gwiki/src/sources/manifest.rs:153-183]
[crates/gwiki/src/sources/manifest.rs:185-195]
[crates/gwiki/src/sources/manifest.rs:197-208]
[crates/gwiki/src/sources/manifest.rs:215-220]
[crates/gwiki/src/sources/manifest.rs:222-224]
[crates/gwiki/src/sources/manifest.rs:227-265]
[crates/gwiki/src/sources/manifest.rs:267-297]
[crates/gwiki/src/sources/manifest.rs:299-303]
[crates/gwiki/src/sources/manifest.rs:305-312]
[crates/gwiki/src/sources/manifest.rs:314-323]

## API Symbols

- `SourceManifest` (class) component `SourceManifest [class]` (`838096cd-1be9-5ad6-83e2-5c01a2f67ac8`) lines 23-25 [crates/gwiki/src/sources/manifest.rs:23-25]
  - Signature: `pub struct SourceManifest {`
  - Purpose: `SourceManifest` is a public struct that encapsulates a collection of `SourceRecord` entries in a vector. [crates/gwiki/src/sources/manifest.rs:23-25]
- `SourceManifest` (class) component `SourceManifest [class]` (`0ba6eb85-a319-5ace-afbc-8150a665165f`) lines 27-225 [crates/gwiki/src/sources/manifest.rs:27-225]
  - Signature: `impl SourceManifest {`
  - Purpose: SourceManifest deserializes and manages a persistent index of source records identified by content hashes within a wiki vault, supporting both read operations and registration of new source entries. [crates/gwiki/src/sources/manifest.rs:27-225]
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
- `SourceManifest.with_lock` (method) component `SourceManifest.with_lock [method]` (`6d7cc5d8-56b1-5071-816e-f4728ecd2c25`) lines 215-220 [crates/gwiki/src/sources/manifest.rs:215-220]
  - Signature: `pub(crate) fn with_lock<T>(`
  - Purpose: This method is a generic wrapper that acquires a manifest lock on the vault root and executes the provided closure, returning its result or a `WikiError`. [crates/gwiki/src/sources/manifest.rs:215-220]
- `SourceManifest.index_path` (method) component `SourceManifest.index_path [method]` (`9119e70b-9471-5c31-910f-79c8d5239592`) lines 222-224 [crates/gwiki/src/sources/manifest.rs:222-224]
  - Signature: `pub fn index_path(vault_root: &Path) -> PathBuf {`
  - Purpose: Constructs and returns a `PathBuf` to the INDEX.md file located in the `raw` subdirectory of the given vault root path. [crates/gwiki/src/sources/manifest.rs:222-224]
- `with_manifest_lock` (function) component `with_manifest_lock [function]` (`d74ab81c-30bf-5a20-abb3-ffb76194271c`) lines 227-265 [crates/gwiki/src/sources/manifest.rs:227-265]
  - Signature: `fn with_manifest_lock<T>(`
  - Purpose: Executes a provided closure while holding an exclusive file lock on the source manifest, ensuring serialized access and propagating the action's result regardless of lock release outcome. [crates/gwiki/src/sources/manifest.rs:227-265]
- `lock_source_manifest` (function) component `lock_source_manifest [function]` (`1df8e5d9-5ef9-5fcc-a658-d83a464b65e0`) lines 267-297 [crates/gwiki/src/sources/manifest.rs:267-297]
  - Signature: `fn lock_source_manifest(lock: &File, lock_path: &Path) -> Result<(), WikiError> {`
  - Purpose: Acquires an exclusive file lock through polling with a fixed retry interval until success, timeout expiration, or I/O error. [crates/gwiki/src/sources/manifest.rs:267-297]
- `try_lock_exclusive` (function) component `try_lock_exclusive [function]` (`29c38770-3b47-5c9e-b32c-39baa61e01f6`) lines 299-303 [crates/gwiki/src/sources/manifest.rs:299-303]
  - Signature: `fn try_lock_exclusive(lock: &File) -> Result<(), fs4::TryLockError> {`
  - Purpose: Attempts a non-blocking exclusive file lock, returning success or a `TryLockError` if the operation fails. [crates/gwiki/src/sources/manifest.rs:299-303]
- `source_manifest_lock_timeout` (function) component `source_manifest_lock_timeout [function]` (`69439b8a-4fa9-5235-ad2e-c053988fd452`) lines 305-312 [crates/gwiki/src/sources/manifest.rs:305-312]
  - Signature: `fn source_manifest_lock_timeout() -> Duration {`
  - Purpose: Returns a `Duration` by parsing the `SOURCE_MANIFEST_LOCK_TIMEOUT_ENV` environment variable as milliseconds, or defaults to `DEFAULT_SOURCE_MANIFEST_LOCK_TIMEOUT` if the variable is unset, non-numeric, or non-positive. [crates/gwiki/src/sources/manifest.rs:305-312]
- `SourceRecordParts` (class) component `SourceRecordParts [class]` (`16b3e5a7-dcd4-5fb5-a368-e9c62c709927`) lines 314-323 [crates/gwiki/src/sources/manifest.rs:314-323]
  - Signature: `struct SourceRecordParts {`
  - Purpose: SourceRecordParts is a Rust struct that encapsulates metadata for a source record, including its location, kind, fetch timestamp, optional bibliographic fields (title, citation, license), ingestion method, and compilation status. [crates/gwiki/src/sources/manifest.rs:314-323]

