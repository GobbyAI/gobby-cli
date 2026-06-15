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

# crates/gwiki/src/ingest/pdf/ingest.rs

Module: [[code/modules/crates/gwiki/src/ingest/pdf|crates/gwiki/src/ingest/pdf]]

## Purpose

Orchestrates PDF ingestion for gwiki by routing simple page snapshots and full PDF files through shared ingestion logic, with optional vision/OCR rendering and post-ingest reindexing. The module normalizes page content, extracts or renders PDF pages when available, writes the source asset and raw markdown into the vault, records degradations when text extraction or rendering fails, and rolls back the staged source if markdown writing fails; separate helpers handle cleanup and rollback error reporting.
[crates/gwiki/src/ingest/pdf/ingest.rs:23-37]
[crates/gwiki/src/ingest/pdf/ingest.rs:41-52]
[crates/gwiki/src/ingest/pdf/ingest.rs:55-108]
[crates/gwiki/src/ingest/pdf/ingest.rs:111-128]
[crates/gwiki/src/ingest/pdf/ingest.rs:131-146]

## API Symbols

- `ingest_pages` (function) component `ingest_pages [function]` (`8ffb36c7-f2e2-56f3-a324-bb3c8f66a4dd`) lines 23-37 [crates/gwiki/src/ingest/pdf/ingest.rs:23-37]
  - Signature: `pub fn ingest_pages(`
  - Purpose: Delegates PDF page ingestion to 'ingest_pages_with_vision' with an empty vision prompt list and an unavailable vision endpoint, returning the resulting 'IngestResult' or 'WikiError'. [crates/gwiki/src/ingest/pdf/ingest.rs:23-37]
- `ingest_pdf_file` (function) component `ingest_pdf_file [function]` (`95c9dc97-74e0-5d87-a3c1-fe755428ff72`) lines 41-52 [crates/gwiki/src/ingest/pdf/ingest.rs:41-52]
  - Signature: `pub fn ingest_pdf_file(`
  - Purpose: Runs 'ingest_pdf_file_without_index' to ingest a PDF snapshot into the vault, then reindexes the vault via 'index_after_ingest' before returning the original 'IngestResult'. [crates/gwiki/src/ingest/pdf/ingest.rs:41-52]
- `ingest_pdf_file_without_index` (function) component `ingest_pdf_file_without_index [function]` (`523df09f-79ca-5ea6-acf0-539f5d68ecb6`) lines 55-108 [crates/gwiki/src/ingest/pdf/ingest.rs:55-108]
  - Signature: `pub(crate) fn ingest_pdf_file_without_index(`
  - Purpose: 'ingest_pdf_file_without_index' extracts text-layer pages from a PDF snapshot, optionally renders pages when a vision endpoint is available, records any extraction/rendering degradations, and delegates the assembled snapshot plus rendered pages to 'ingest_pages_with_vision_inner' to produce an 'IngestResult' or 'WikiError'. [crates/gwiki/src/ingest/pdf/ingest.rs:55-108]
- `ingest_pages_with_vision` (function) component `ingest_pages_with_vision [function]` (`8ddf8eef-a485-5a2d-ba71-f896f29f42c6`) lines 111-128 [crates/gwiki/src/ingest/pdf/ingest.rs:111-128]
  - Signature: `pub fn ingest_pages_with_vision(`
  - Purpose: Runs 'ingest_pages_with_vision_without_index' to ingest the rendered PDF pages into a wiki vault, then rebuilds the index via 'index_after_ingest', returning the resulting 'IngestResult' or propagating 'WikiError'. [crates/gwiki/src/ingest/pdf/ingest.rs:111-128]
- `ingest_pages_with_vision_without_index` (function) component `ingest_pages_with_vision_without_index [function]` (`8cf7e35a-c5a2-5626-b253-f54d87a3b81a`) lines 131-146 [crates/gwiki/src/ingest/pdf/ingest.rs:131-146]
  - Signature: `pub(crate) fn ingest_pages_with_vision_without_index(`
  - Purpose: Calls 'ingest_pages_with_vision_inner' to ingest rendered PDF pages with a vision endpoint while supplying an empty index vector, returning its 'Result<IngestResult, WikiError>'. [crates/gwiki/src/ingest/pdf/ingest.rs:131-146]
- `ingest_pages_with_vision_inner` (function) component `ingest_pages_with_vision_inner [function]` (`50cddb42-fe4a-5472-a9b8-334b7a0e7c10`) lines 149-220 [crates/gwiki/src/ingest/pdf/ingest.rs:149-220]
  - Signature: `fn ingest_pages_with_vision_inner(`
  - Purpose: Registers a PDF source in the manifest, persists the original asset, optionally records a 'PdfNoExtractableContent' degradation, merges page text with OCR/vision-rendered pages, renders the final markdown, and writes the raw markdown output, rolling back the registered source on write failures. [crates/gwiki/src/ingest/pdf/ingest.rs:149-220]
- `rollback_registered_pdf_source` (function) component `rollback_registered_pdf_source [function]` (`4d86afff-2599-5414-9cf3-ce1e3272844f`) lines 223-247 [crates/gwiki/src/ingest/pdf/ingest.rs:223-247]
  - Signature: `fn rollback_registered_pdf_source<T>(`
  - Purpose: 'rollback_registered_pdf_source' optionally cleans up a staged PDF asset, attempts to restore the previous source manifest, and returns either the original ingest error or a 'WikiError::Config' that includes rollback and cleanup failure details if rollback or cleanup reporting fails. [crates/gwiki/src/ingest/pdf/ingest.rs:223-247]
- `cleanup_pdf_file` (function) component `cleanup_pdf_file [function]` (`69f90f69-6002-56a2-a801-863cff9b6905`) lines 250-257 [crates/gwiki/src/ingest/pdf/ingest.rs:250-257]
  - Signature: `fn cleanup_pdf_file(vault_root: &Path, relative_path: &Path, cleanup_errors: &mut Vec<String>) {`
  - Purpose: Deletes the file at 'vault_root.join(relative_path)', ignores 'NotFound' errors, and appends any other removal error to 'cleanup_errors' as a formatted 'path: error' string. [crates/gwiki/src/ingest/pdf/ingest.rs:250-257]
- `pdf_cleanup_detail` (function) component `pdf_cleanup_detail [function]` (`0ecb051b-0d96-5dd6-8a20-889652d189cb`) lines 260-266 [crates/gwiki/src/ingest/pdf/ingest.rs:260-266]
  - Signature: `fn pdf_cleanup_detail(cleanup_errors: &[String]) -> String {`
  - Purpose: Returns an empty string when 'cleanup_errors' is empty, otherwise returns a semicolon-prefixed '"cleanup failures: ..."' string joining all errors with '"; "'. [crates/gwiki/src/ingest/pdf/ingest.rs:260-266]

