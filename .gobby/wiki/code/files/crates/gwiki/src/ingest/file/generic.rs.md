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

# crates/gwiki/src/ingest/file/generic.rs

Module: [[code/modules/crates/gwiki/src/ingest/file|crates/gwiki/src/ingest/file]]

## Purpose

Ingests a generic local file into the wiki pipeline without using an index: it reads the source bytes, derives a markdown title from the filename, registers the file as a borrowed draft in the source manifest with manual ingestion and pending compile status, optionally stores the file as an asset, renders raw markdown for the file using the recorded hash and asset path, writes that markdown to disk, and returns the ingest result with no degradations. [crates/gwiki/src/ingest/file/generic.rs:11-57]

## API Symbols

- `ingest_generic_file_without_index` (function) component `ingest_generic_file_without_index [function]` (`aa6e9d33-cb14-5cc9-9e17-40e1c671966c`) lines 11-57 [crates/gwiki/src/ingest/file/generic.rs:11-57]
  - Signature: `pub(super) fn ingest_generic_file_without_index(`
  - Purpose: Reads a source file, registers it as a borrowed draft in the source manifest with a markdown-derived title and pending compile status, optionally stores the file as an asset, renders raw markdown for it, writes that markdown to disk, and returns the ingest result with no degradations. [crates/gwiki/src/ingest/file/generic.rs:11-57]

