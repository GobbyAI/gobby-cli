---
title: crates/gwiki/src/ingest/file/source.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file/source.rs
  ranges:
  - 9-24
  - 26-40
  - 42-54
  - 56-62
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/file/source.rs

Module: [[code/modules/crates/gwiki/src/ingest/file|crates/gwiki/src/ingest/file]]

## Purpose

This file provides the basic file-ingest helpers for source handling: it classifies a path into a `SourceKind` from its extension, builds a normalized display location relative to the vault when possible, decides whether a source should be stored as an asset based on kind and text size, and reads the raw bytes from disk while wrapping I/O failures in `WikiError::Io`. Together these functions support downstream ingest by turning paths into typed, storable source records.
[crates/gwiki/src/ingest/file/source.rs:9-24]
[crates/gwiki/src/ingest/file/source.rs:26-40]
[crates/gwiki/src/ingest/file/source.rs:42-54]
[crates/gwiki/src/ingest/file/source.rs:56-62]

## API Symbols

- `detect_source_kind` (function) component `detect_source_kind [function]` (`4b8b28d2-e21b-5fbf-93fd-476a887f484a`) lines 9-24 [crates/gwiki/src/ingest/file/source.rs:9-24]
  - Signature: `pub(super) fn detect_source_kind(path: &Path) -> SourceKind {`
  - Purpose: 'detect_source_kind' inspects a path’s lowercase file extension and maps it to a 'SourceKind' variant for known PDF, Office, HTML, audio, image, video, markdown, and text formats, defaulting to 'SourceKind::File' for anything unrecognized. [crates/gwiki/src/ingest/file/source.rs:9-24]
- `source_location` (function) component `source_location [function]` (`a97604f9-b13e-5dfe-91ed-c825c795fa7b`) lines 26-40 [crates/gwiki/src/ingest/file/source.rs:26-40]
  - Signature: `pub(super) fn source_location(vault_root: &Path, path: &Path) -> String {`
  - Purpose: Returns a forward-slash-normalized string for 'path' relative to 'vault_root' when possible, otherwise falls back to a canonicalized relative path or the original path. [crates/gwiki/src/ingest/file/source.rs:26-40]
- `should_store_asset` (function) component `should_store_asset [function]` (`f00d30dc-5524-5c25-a646-e704e2c67ae4`) lines 42-54 [crates/gwiki/src/ingest/file/source.rs:42-54]
  - Signature: `pub(super) fn should_store_asset(kind: &SourceKind, byte_len: usize) -> bool {`
  - Purpose: Returns 'true' for any non-text asset kind ('Audio', 'Image', 'Video', 'Pdf', 'Office', 'Html', 'File') and for 'Text' assets whose 'byte_len' exceeds 'TEXT_INLINE_LIMIT_BYTES', otherwise 'false'. [crates/gwiki/src/ingest/file/source.rs:42-54]
- `read_source_file` (function) component `read_source_file [function]` (`da8534d0-c9fa-5326-8645-1572a61675aa`) lines 56-62 [crates/gwiki/src/ingest/file/source.rs:56-62]
  - Signature: `pub(super) fn read_source_file(path: &Path) -> Result<Vec<u8>, WikiError> {`
  - Purpose: Reads the file at 'path' into a 'Vec<u8>' with 'std::fs::read', converting any I/O failure into 'WikiError::Io' annotated with the '"read source file"' action and the path. [crates/gwiki/src/ingest/file/source.rs:56-62]

