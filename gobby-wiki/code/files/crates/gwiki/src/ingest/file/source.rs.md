---
title: crates/gwiki/src/ingest/file/source.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file/source.rs
  ranges:
  - 9-25
  - 27-41
  - 43-55
  - 57-63
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/file/source.rs:9-25](crates/gwiki/src/ingest/file/source.rs#L9-L25), [crates/gwiki/src/ingest/file/source.rs:27-41](crates/gwiki/src/ingest/file/source.rs#L27-L41), [crates/gwiki/src/ingest/file/source.rs:43-55](crates/gwiki/src/ingest/file/source.rs#L43-L55), [crates/gwiki/src/ingest/file/source.rs:57-63](crates/gwiki/src/ingest/file/source.rs#L57-L63)

</details>

# crates/gwiki/src/ingest/file/source.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This module classifies input files, derives a stable source-relative location string, decides whether a file should be stored as an asset versus kept inline, and reads the file bytes with I/O errors wrapped as `WikiError`. `detect_source_kind` maps file extensions to `SourceKind` categories; `source_location` normalizes a path against the vault root and converts separators to `/`; `should_store_asset` uses the kind and size threshold to route large text files and all non-text media/doc types into asset storage; `read_source_file` performs the filesystem read for ingest.
[crates/gwiki/src/ingest/file/source.rs:9-25]
[crates/gwiki/src/ingest/file/source.rs:27-41]
[crates/gwiki/src/ingest/file/source.rs:43-55]
[crates/gwiki/src/ingest/file/source.rs:57-63]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `detect_source_kind` | function | `pub(super) fn detect_source_kind(path: &Path) -> SourceKind {` | `detect_source_kind [function]` | `4b8b28d2-e21b-5fbf-93fd-476a887f484a` | 9-25 [crates/gwiki/src/ingest/file/source.rs:9-25] | Indexed function `detect_source_kind` in `crates/gwiki/src/ingest/file/source.rs`. [crates/gwiki/src/ingest/file/source.rs:9-25] |
| `source_location` | function | `pub(super) fn source_location(vault_root: &Path, path: &Path) -> String {` | `source_location [function]` | `a690661d-5f6b-5079-a56c-140134e3a46f` | 27-41 [crates/gwiki/src/ingest/file/source.rs:27-41] | Indexed function `source_location` in `crates/gwiki/src/ingest/file/source.rs`. [crates/gwiki/src/ingest/file/source.rs:27-41] |
| `should_store_asset` | function | `pub(super) fn should_store_asset(kind: &SourceKind, byte_len: usize) -> bool {` | `should_store_asset [function]` | `f08a065e-0f26-563e-9397-30d9aa1b0543` | 43-55 [crates/gwiki/src/ingest/file/source.rs:43-55] | Indexed function `should_store_asset` in `crates/gwiki/src/ingest/file/source.rs`. [crates/gwiki/src/ingest/file/source.rs:43-55] |
| `read_source_file` | function | `pub(super) fn read_source_file(path: &Path) -> Result<Vec<u8>, WikiError> {` | `read_source_file [function]` | `acb81f97-9232-5b06-aef6-4f136b8fa6af` | 57-63 [crates/gwiki/src/ingest/file/source.rs:57-63] | Indexed function `read_source_file` in `crates/gwiki/src/ingest/file/source.rs`. [crates/gwiki/src/ingest/file/source.rs:57-63] |
