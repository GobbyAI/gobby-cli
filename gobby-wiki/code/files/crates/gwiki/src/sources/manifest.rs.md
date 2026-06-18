---
title: crates/gwiki/src/sources/manifest.rs
type: code_file
provenance:
- file: crates/gwiki/src/sources/manifest.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/sources/manifest.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/sources/manifest.rs` exposes 16 indexed API symbols.

## How it fits

`crates/gwiki/src/sources/manifest.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SourceManifest` | class | 'SourceManifest' is a data container struct that holds a vector of 'SourceRecord' entries representing a manifest of sources. [crates/gwiki/src/sources/manifest.rs:23-25] |
| `SourceManifest::read` | method | Reads the raw source index file at the vault root if it exists, parses each line’s 'SOURCE_MARKER'-delimited JSON record into 'entries', returns 'Self::default()' when the index file is absent, and converts I/O or malformed marker/JSON failures into 'WikiError'. [crates/gwiki/src/sources/manifest.rs:28-66] |
| `SourceManifest::register` | method | Computes a content hash from 'draft.content' and delegates to 'Self::register_with_content_hash(vault_root, draft, content_hash)' to produce a 'Result<SourceRecord, WikiError>'. [crates/gwiki/src/sources/manifest.rs:68-71] |
| `SourceManifest::register_borrowed` | method | Computes a content hash from a borrowed source draft’s content and delegates to 'register_parts_with_content_hash' to create a 'SourceRecord' from the draft’s metadata and the given vault root, returning any 'WikiError'. [crates/gwiki/src/sources/manifest.rs:73-92] |
| `SourceManifest::register_with_content_hash` | method | 'register_with_content_hash' converts a 'SourceDraft' into 'SourceRecordParts' by moving its metadata fields, then delegates to 'Self::register_parts_with_content_hash' with the vault root and provided 'content_hash' to produce a 'Result<SourceRecord, WikiError>'. [crates/gwiki/src/sources/manifest.rs:94-113] |
| `SourceManifest::register_parts_with_content_hash` | method | Acquires the manifest lock, reads the manifest, deduplicates by '(canonical_location, content_hash)', and otherwise constructs a new 'SourceRecord' from the draft, appends it to the manifest, persists the manifest, and returns the existing or newly registered record. [crates/gwiki/src/sources/manifest.rs:115-147] |
| `SourceManifest::write` | method | Acquires the manifest lock for 'vault_root' and then delegates to 'self.write_unlocked(vault_root)', returning its 'Result<(), WikiError>'. [crates/gwiki/src/sources/manifest.rs:149-151] |
| `SourceManifest::write_unlocked` | method | Creates the 'raw' directory under 'vault_root', rebuilds the index file by preserving any existing prefix/suffix outside the generated source manifest while rendering 'self.entries' between manifest markers, and atomically writes the result to the index path. [crates/gwiki/src/sources/manifest.rs:153-183] |
| `SourceManifest::remove` | method | Removes the entry with the matching 'id' from the manifest under the vault-root lock, persists the updated manifest, and returns 'Ok(Some(SourceRecord))' if found or 'Ok(None)' if no matching entry exists. [crates/gwiki/src/sources/manifest.rs:185-195] |
| `SourceManifest::update` | method | Acquires the manifest lock for 'vault_root', reads the current 'SourceManifest', applies the provided mutable action, and writes the manifest back atomically only if the action returns 'true', propagating any 'WikiError'. [crates/gwiki/src/sources/manifest.rs:197-208] |
| `SourceManifest::index_path` | method | Returns the path 'vault_root/raw/INDEX.md' by appending 'raw' and then 'INDEX.md' to the given 'vault_root' path. [crates/gwiki/src/sources/manifest.rs:210-212] |
| `with_manifest_lock` | function | Acquires an exclusive file lock at '<vault_root>/<STATE_ROOT>/source-manifest.lock', runs the provided closure under that lock, and ensures the lock is released afterward while propagating either the closure’s result or any I/O/locking error. [crates/gwiki/src/sources/manifest.rs:215-255] |
| `lock_source_manifest` | function | Attempts to acquire an exclusive lock on 'lock' with repeated retries until 'source_manifest_lock_timeout()' elapses, returning a timed-out 'WikiError::Io' on contention or propagating any other locking error. [crates/gwiki/src/sources/manifest.rs:257-287] |
| `try_lock_exclusive` | function | Attempts to acquire an exclusive filesystem lock on the given 'File' by delegating to 'fs4::FileExt::try_lock', returning 'Ok(())' on success or 'fs4::TryLockError' if the lock cannot be obtained. [crates/gwiki/src/sources/manifest.rs:289-293] |
| `source_manifest_lock_timeout` | function | Returns the source-manifest lock timeout as a 'Duration', using the positive 'u64' value of 'SOURCE_MANIFEST_LOCK_TIMEOUT_ENV' interpreted in milliseconds when present and valid, otherwise falling back to 'DEFAULT_SOURCE_MANIFEST_LOCK_TIMEOUT'. [crates/gwiki/src/sources/manifest.rs:295-302] |
| `SourceRecordParts` | class | 'SourceRecordParts' is a data-only struct that captures a source record’s location, kind, fetch timestamp, optional title/citation/license metadata, ingestion method, and compile status. [crates/gwiki/src/sources/manifest.rs:304-313] |

