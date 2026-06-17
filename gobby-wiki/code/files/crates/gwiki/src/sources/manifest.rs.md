---
title: crates/gwiki/src/sources/manifest.rs
type: code_file
provenance:
- file: crates/gwiki/src/sources/manifest.rs
  ranges:
  - 23-25
  - 28-66
  - 68-71
  - 73-92
  - 94-113
  - 115-147
  - 149-151
  - 153-183
  - 185-195
  - 197-208
  - 210-212
  - 215-253
  - 255-285
  - 287-291
  - 293-300
  - 302-311
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/sources/manifest.rs:23-25](crates/gwiki/src/sources/manifest.rs#L23-L25), [crates/gwiki/src/sources/manifest.rs:28-66](crates/gwiki/src/sources/manifest.rs#L28-L66), [crates/gwiki/src/sources/manifest.rs:68-71](crates/gwiki/src/sources/manifest.rs#L68-L71), [crates/gwiki/src/sources/manifest.rs:73-92](crates/gwiki/src/sources/manifest.rs#L73-L92), [crates/gwiki/src/sources/manifest.rs:94-113](crates/gwiki/src/sources/manifest.rs#L94-L113), [crates/gwiki/src/sources/manifest.rs:115-147](crates/gwiki/src/sources/manifest.rs#L115-L147), [crates/gwiki/src/sources/manifest.rs:149-151](crates/gwiki/src/sources/manifest.rs#L149-L151), [crates/gwiki/src/sources/manifest.rs:153-183](crates/gwiki/src/sources/manifest.rs#L153-L183), [crates/gwiki/src/sources/manifest.rs:185-195](crates/gwiki/src/sources/manifest.rs#L185-L195), [crates/gwiki/src/sources/manifest.rs:197-208](crates/gwiki/src/sources/manifest.rs#L197-L208), [crates/gwiki/src/sources/manifest.rs:210-212](crates/gwiki/src/sources/manifest.rs#L210-L212), [crates/gwiki/src/sources/manifest.rs:215-253](crates/gwiki/src/sources/manifest.rs#L215-L253), [crates/gwiki/src/sources/manifest.rs:255-285](crates/gwiki/src/sources/manifest.rs#L255-L285), [crates/gwiki/src/sources/manifest.rs:287-291](crates/gwiki/src/sources/manifest.rs#L287-L291), [crates/gwiki/src/sources/manifest.rs:293-300](crates/gwiki/src/sources/manifest.rs#L293-L300), [crates/gwiki/src/sources/manifest.rs:302-311](crates/gwiki/src/sources/manifest.rs#L302-L311)

</details>

# crates/gwiki/src/sources/manifest.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Manages the source manifest stored in a wiki vault’s index file: it can read existing `gwiki-source` markers back into `SourceRecord` entries, register new drafts into the manifest, update or remove records, and write the manifest atomically. The `SourceManifest` methods handle the lifecycle of entries and persistence, while the lock helpers (`with_manifest_lock`, `lock_source_manifest`, `try_lock_exclusive`, `source_manifest_lock_timeout`) serialize concurrent access so manifest updates do not race, and `SourceRecordParts` supports assembling record data for registration and rendering.
[crates/gwiki/src/sources/manifest.rs:23-25]
[crates/gwiki/src/sources/manifest.rs:28-66]
[crates/gwiki/src/sources/manifest.rs:68-71]
[crates/gwiki/src/sources/manifest.rs:73-92]
[crates/gwiki/src/sources/manifest.rs:94-113]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `SourceManifest` | class | `pub struct SourceManifest {` | `SourceManifest [class]` | `838096cd-1be9-5ad6-83e2-5c01a2f67ac8` | 23-25 [crates/gwiki/src/sources/manifest.rs:23-25] | Indexed class `SourceManifest` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:23-25] |
| `SourceManifest::read` | method | `pub fn read(vault_root: &Path) -> Result<Self, WikiError> {` | `SourceManifest::read [method]` | `21efa115-c306-574d-a89a-dd384f131a47` | 28-66 [crates/gwiki/src/sources/manifest.rs:28-66] | Indexed method `SourceManifest::read` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:28-66] |
| `SourceManifest::register` | method | `pub fn register(vault_root: &Path, draft: SourceDraft) -> Result<SourceRecord, WikiError> {` | `SourceManifest::register [method]` | `a63fd77c-0692-52fc-94a8-07f5f1aef241` | 68-71 [crates/gwiki/src/sources/manifest.rs:68-71] | Indexed method `SourceManifest::register` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:68-71] |
| `SourceManifest::register_borrowed` | method | `pub(crate) fn register_borrowed(` | `SourceManifest::register_borrowed [method]` | `4d78ce00-3e24-57f6-ab3f-5b51e95d20b6` | 73-92 [crates/gwiki/src/sources/manifest.rs:73-92] | Indexed method `SourceManifest::register_borrowed` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:73-92] |
| `SourceManifest::register_with_content_hash` | method | `pub fn register_with_content_hash(` | `SourceManifest::register_with_content_hash [method]` | `49dd7a6b-43a0-5e34-90f7-bd5c78bcb64c` | 94-113 [crates/gwiki/src/sources/manifest.rs:94-113] | Indexed method `SourceManifest::register_with_content_hash` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:94-113] |
| `SourceManifest::register_parts_with_content_hash` | method | `fn register_parts_with_content_hash(` | `SourceManifest::register_parts_with_content_hash [method]` | `722b360b-f71b-5232-a99c-cc119eb7fb8c` | 115-147 [crates/gwiki/src/sources/manifest.rs:115-147] | Indexed method `SourceManifest::register_parts_with_content_hash` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:115-147] |
| `SourceManifest::write` | method | `pub fn write(&self, vault_root: &Path) -> Result<(), WikiError> {` | `SourceManifest::write [method]` | `fa76f27c-224a-5a6c-8ba1-c3f4a0117359` | 149-151 [crates/gwiki/src/sources/manifest.rs:149-151] | Indexed method `SourceManifest::write` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:149-151] |
| `SourceManifest::write_unlocked` | method | `fn write_unlocked(&self, vault_root: &Path) -> Result<(), WikiError> {` | `SourceManifest::write_unlocked [method]` | `86daa3b3-b195-5bb7-8c8e-91c63037142c` | 153-183 [crates/gwiki/src/sources/manifest.rs:153-183] | Indexed method `SourceManifest::write_unlocked` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:153-183] |
| `SourceManifest::remove` | method | `pub fn remove(vault_root: &Path, id: &str) -> Result<Option<SourceRecord>, WikiError> {` | `SourceManifest::remove [method]` | `b69f4896-6357-5679-8ef6-b3f05d22c2a7` | 185-195 [crates/gwiki/src/sources/manifest.rs:185-195] | Indexed method `SourceManifest::remove` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:185-195] |
| `SourceManifest::update` | method | `pub fn update(` | `SourceManifest::update [method]` | `09c70535-b2f1-5d8c-a26b-cefa4e2e25b3` | 197-208 [crates/gwiki/src/sources/manifest.rs:197-208] | Indexed method `SourceManifest::update` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:197-208] |
| `SourceManifest::index_path` | method | `pub fn index_path(vault_root: &Path) -> PathBuf {` | `SourceManifest::index_path [method]` | `2dc6ff46-1f6f-5b0b-a679-b845877e7cde` | 210-212 [crates/gwiki/src/sources/manifest.rs:210-212] | Indexed method `SourceManifest::index_path` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:210-212] |
| `with_manifest_lock` | function | `fn with_manifest_lock<T>(` | `with_manifest_lock [function]` | `dcab3658-49b7-53f5-8248-d07e6a9f3e35` | 215-253 [crates/gwiki/src/sources/manifest.rs:215-253] | Indexed function `with_manifest_lock` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:215-253] |
| `lock_source_manifest` | function | `fn lock_source_manifest(lock: &File, lock_path: &Path) -> Result<(), WikiError> {` | `lock_source_manifest [function]` | `1fe0585a-5198-590d-b63c-0fe3dc6d0c88` | 255-285 [crates/gwiki/src/sources/manifest.rs:255-285] | Indexed function `lock_source_manifest` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:255-285] |
| `try_lock_exclusive` | function | `fn try_lock_exclusive(lock: &File) -> Result<(), fs4::TryLockError> {` | `try_lock_exclusive [function]` | `bb5c9d2b-b880-56ce-9d80-142eeb0eb048` | 287-291 [crates/gwiki/src/sources/manifest.rs:287-291] | Indexed function `try_lock_exclusive` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:287-291] |
| `source_manifest_lock_timeout` | function | `fn source_manifest_lock_timeout() -> Duration {` | `source_manifest_lock_timeout [function]` | `11efb02f-d9a8-57e5-9544-9e2d23c9ee47` | 293-300 [crates/gwiki/src/sources/manifest.rs:293-300] | Indexed function `source_manifest_lock_timeout` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:293-300] |
| `SourceRecordParts` | class | `struct SourceRecordParts {` | `SourceRecordParts [class]` | `c60f671f-3407-5aff-93d4-a72477521cca` | 302-311 [crates/gwiki/src/sources/manifest.rs:302-311] | Indexed class `SourceRecordParts` in `crates/gwiki/src/sources/manifest.rs`. [crates/gwiki/src/sources/manifest.rs:302-311] |
