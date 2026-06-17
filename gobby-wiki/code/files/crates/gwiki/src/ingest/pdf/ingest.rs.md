---
title: crates/gwiki/src/ingest/pdf/ingest.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/ingest.rs
  ranges:
  - 23-37
  - 41-52
  - 55-108
  - 111-128
  - 131-146
  - 149-220
  - 223-247
  - 250-257
  - 260-266
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/pdf/ingest.rs:23-37](crates/gwiki/src/ingest/pdf/ingest.rs#L23-L37), [crates/gwiki/src/ingest/pdf/ingest.rs:41-52](crates/gwiki/src/ingest/pdf/ingest.rs#L41-L52), [crates/gwiki/src/ingest/pdf/ingest.rs:55-108](crates/gwiki/src/ingest/pdf/ingest.rs#L55-L108), [crates/gwiki/src/ingest/pdf/ingest.rs:111-128](crates/gwiki/src/ingest/pdf/ingest.rs#L111-L128), [crates/gwiki/src/ingest/pdf/ingest.rs:131-146](crates/gwiki/src/ingest/pdf/ingest.rs#L131-L146), [crates/gwiki/src/ingest/pdf/ingest.rs:149-220](crates/gwiki/src/ingest/pdf/ingest.rs#L149-L220), [crates/gwiki/src/ingest/pdf/ingest.rs:223-247](crates/gwiki/src/ingest/pdf/ingest.rs#L223-L247), [crates/gwiki/src/ingest/pdf/ingest.rs:250-257](crates/gwiki/src/ingest/pdf/ingest.rs#L250-L257), [crates/gwiki/src/ingest/pdf/ingest.rs:260-266](crates/gwiki/src/ingest/pdf/ingest.rs#L260-L266)

</details>

# crates/gwiki/src/ingest/pdf/ingest.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements the PDF ingestion flow for gwiki. It exposes entry points that ingest plain page snapshots or full PDF files, optionally re-indexing afterward, then routes through text-layer extraction or vision-assisted page processing to produce ingest results while collecting degradations and preserving raw assets as needed.

The helpers split the work into “with index” and “without index” variants, combine rendered/normalized page content into markdown, and provide rollback and cleanup routines for undoing a registered PDF source and deleting temporary PDF artifacts with a small detail formatter for cleanup reporting.
[crates/gwiki/src/ingest/pdf/ingest.rs:23-37]
[crates/gwiki/src/ingest/pdf/ingest.rs:41-52]
[crates/gwiki/src/ingest/pdf/ingest.rs:55-108]
[crates/gwiki/src/ingest/pdf/ingest.rs:111-128]
[crates/gwiki/src/ingest/pdf/ingest.rs:131-146]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ingest_pages` | function | `pub fn ingest_pages(` | `ingest_pages [function]` | `8ffb36c7-f2e2-56f3-a324-bb3c8f66a4dd` | 23-37 [crates/gwiki/src/ingest/pdf/ingest.rs:23-37] | Indexed function `ingest_pages` in `crates/gwiki/src/ingest/pdf/ingest.rs`. [crates/gwiki/src/ingest/pdf/ingest.rs:23-37] |
| `ingest_pdf_file` | function | `pub fn ingest_pdf_file(` | `ingest_pdf_file [function]` | `95c9dc97-74e0-5d87-a3c1-fe755428ff72` | 41-52 [crates/gwiki/src/ingest/pdf/ingest.rs:41-52] | Indexed function `ingest_pdf_file` in `crates/gwiki/src/ingest/pdf/ingest.rs`. [crates/gwiki/src/ingest/pdf/ingest.rs:41-52] |
| `ingest_pdf_file_without_index` | function | `pub(crate) fn ingest_pdf_file_without_index(` | `ingest_pdf_file_without_index [function]` | `523df09f-79ca-5ea6-acf0-539f5d68ecb6` | 55-108 [crates/gwiki/src/ingest/pdf/ingest.rs:55-108] | Indexed function `ingest_pdf_file_without_index` in `crates/gwiki/src/ingest/pdf/ingest.rs`. [crates/gwiki/src/ingest/pdf/ingest.rs:55-108] |
| `ingest_pages_with_vision` | function | `pub fn ingest_pages_with_vision(` | `ingest_pages_with_vision [function]` | `8ddf8eef-a485-5a2d-ba71-f896f29f42c6` | 111-128 [crates/gwiki/src/ingest/pdf/ingest.rs:111-128] | Indexed function `ingest_pages_with_vision` in `crates/gwiki/src/ingest/pdf/ingest.rs`. [crates/gwiki/src/ingest/pdf/ingest.rs:111-128] |
| `ingest_pages_with_vision_without_index` | function | `pub(crate) fn ingest_pages_with_vision_without_index(` | `ingest_pages_with_vision_without_index [function]` | `8cf7e35a-c5a2-5626-b253-f54d87a3b81a` | 131-146 [crates/gwiki/src/ingest/pdf/ingest.rs:131-146] | Indexed function `ingest_pages_with_vision_without_index` in `crates/gwiki/src/ingest/pdf/ingest.rs`. [crates/gwiki/src/ingest/pdf/ingest.rs:131-146] |
| `ingest_pages_with_vision_inner` | function | `fn ingest_pages_with_vision_inner(` | `ingest_pages_with_vision_inner [function]` | `50cddb42-fe4a-5472-a9b8-334b7a0e7c10` | 149-220 [crates/gwiki/src/ingest/pdf/ingest.rs:149-220] | Indexed function `ingest_pages_with_vision_inner` in `crates/gwiki/src/ingest/pdf/ingest.rs`. [crates/gwiki/src/ingest/pdf/ingest.rs:149-220] |
| `rollback_registered_pdf_source` | function | `fn rollback_registered_pdf_source<T>(` | `rollback_registered_pdf_source [function]` | `4d86afff-2599-5414-9cf3-ce1e3272844f` | 223-247 [crates/gwiki/src/ingest/pdf/ingest.rs:223-247] | Indexed function `rollback_registered_pdf_source` in `crates/gwiki/src/ingest/pdf/ingest.rs`. [crates/gwiki/src/ingest/pdf/ingest.rs:223-247] |
| `cleanup_pdf_file` | function | `fn cleanup_pdf_file(vault_root: &Path, relative_path: &Path, cleanup_errors: &mut Vec<String>) {` | `cleanup_pdf_file [function]` | `69f90f69-6002-56a2-a801-863cff9b6905` | 250-257 [crates/gwiki/src/ingest/pdf/ingest.rs:250-257] | Indexed function `cleanup_pdf_file` in `crates/gwiki/src/ingest/pdf/ingest.rs`. [crates/gwiki/src/ingest/pdf/ingest.rs:250-257] |
| `pdf_cleanup_detail` | function | `fn pdf_cleanup_detail(cleanup_errors: &[String]) -> String {` | `pdf_cleanup_detail [function]` | `0ecb051b-0d96-5dd6-8a20-889652d189cb` | 260-266 [crates/gwiki/src/ingest/pdf/ingest.rs:260-266] | Indexed function `pdf_cleanup_detail` in `crates/gwiki/src/ingest/pdf/ingest.rs`. [crates/gwiki/src/ingest/pdf/ingest.rs:260-266] |
