---
title: crates/gwiki/src/ingest/file/generic.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file/generic.rs
  ranges:
  - 11-57
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/file/generic.rs:11-57](crates/gwiki/src/ingest/file/generic.rs#L11-L57)

</details>

# crates/gwiki/src/ingest/file/generic.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Provides the no-index ingestion path for a generic local file. It reads the file bytes, registers a borrowed source record with metadata like location, kind, fetched time, title, and manual ingestion status, then decides whether to persist the file as an asset based on size/kind. It finishes by rendering raw markdown from the file contents and record hash, writing that markdown out, and returning the ingest result with no degradations. [crates/gwiki/src/ingest/file/generic.rs:11-57]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ingest_generic_file_without_index` | function | `pub(super) fn ingest_generic_file_without_index(` | `ingest_generic_file_without_index [function]` | `aa6e9d33-cb14-5cc9-9e17-40e1c671966c` | 11-57 [crates/gwiki/src/ingest/file/generic.rs:11-57] | Indexed function `ingest_generic_file_without_index` in `crates/gwiki/src/ingest/file/generic.rs`. [crates/gwiki/src/ingest/file/generic.rs:11-57] |
