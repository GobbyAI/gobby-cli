---
title: crates/gwiki/src/ingest/document/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/document/render.rs
  ranges:
  - 11-33
  - 36-67
  - 69-93
  - 95-122
  - 124-211
  - 213-228
  - 230-241
  - 248-260
  - 263-274
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/document/render.rs

Module: [[code/modules/crates/gwiki/src/ingest/document|crates/gwiki/src/ingest/document]]

## Purpose

This file renders and persists derived Markdown for document ingests, while preserving the original asset path and failure context in the generated metadata. It provides one path for “raw” document snapshots and another for richer derived documents with scope, extraction, and degradation details, both built as Markdown strings with front matter plus a title and body note.

The write flow resolves a vault-relative output path, creates parent directories, renders the Markdown, and atomically writes it through a temp file before syncing the parent directory. The failure helpers map document/source kinds into degradation metadata and unit counts so errors are recorded consistently, with tests covering PDF text-layer failures and non-document “unsupported_source” cases.
[crates/gwiki/src/ingest/document/render.rs:11-33]
[crates/gwiki/src/ingest/document/render.rs:36-67]
[crates/gwiki/src/ingest/document/render.rs:69-93]
[crates/gwiki/src/ingest/document/render.rs:95-122]
[crates/gwiki/src/ingest/document/render.rs:124-211]

## API Symbols

- `render_raw_document_markdown` (function) component `render_raw_document_markdown [function]` (`57f61d7a-3731-520b-a579-76f4f505c22d`) lines 11-33 [crates/gwiki/src/ingest/document/render.rs:11-33]
  - Signature: `pub(crate) fn render_raw_document_markdown(`
  - Purpose: Builds a markdown string with metadata for the document snapshot, then appends an H1 title derived from 'snapshot.file_name' and a note indicating the original document is stored at 'asset_path'. [crates/gwiki/src/ingest/document/render.rs:11-33]
- `write_document_derived_markdown` (function) component `write_document_derived_markdown [function]` (`3c268ad6-387c-5585-8bb8-97ecb9fde676`) lines 36-67 [crates/gwiki/src/ingest/document/render.rs:36-67]
  - Signature: `pub(crate) fn write_document_derived_markdown(`
  - Purpose: Creates the derived markdown file path for a source record under 'vault_root', ensures its parent directory exists, renders document-derived markdown from the provided snapshot/extraction/degradation context, atomically writes it to disk, and returns the relative output path. [crates/gwiki/src/ingest/document/render.rs:36-67]
- `write_document_markdown_atomic` (function) component `write_document_markdown_atomic [function]` (`554261b9-ac01-5d3f-af7c-f6248e0a3034`) lines 69-93 [crates/gwiki/src/ingest/document/render.rs:69-93]
  - Signature: `fn write_document_markdown_atomic(path: &Path, contents: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Atomically writes 'contents' to 'path' by creating a temporary file beside it, writing and 'sync_all'ing the temp file, persisting it over the target path, and then syncing the parent directory, returning 'WikiError::Io' on any I/O failure. [crates/gwiki/src/ingest/document/render.rs:69-93]
- `create_document_temp_file` (function) component `create_document_temp_file [function]` (`3c09510a-fe5d-53e3-9cf1-861a3002dc5d`) lines 95-122 [crates/gwiki/src/ingest/document/render.rs:95-122]
  - Signature: `fn create_document_temp_file(path: &Path) -> Result<NamedTempFile, WikiError> {`
  - Purpose: Creates a temporary file in the target path’s parent directory using a '".{file_name}."' prefix and '.tmp' suffix, or returns a 'WikiError::Io' if the path has no valid parent or temp-file creation fails. [crates/gwiki/src/ingest/document/render.rs:95-122]
- `render_document_derived_markdown` (function) component `render_document_derived_markdown [function]` (`a3a6a5d5-1f3f-5fbd-b4f4-ad403beb4630`) lines 124-211 [crates/gwiki/src/ingest/document/render.rs:124-211]
  - Signature: `fn render_document_derived_markdown(`
  - Purpose: Builds a Markdown document string by emitting front-matter metadata from the scope, source record, snapshot, extraction, and degradation state, then appending an '# {title}' heading and body content prefix. [crates/gwiki/src/ingest/document/render.rs:124-211]
- `document_degradation_for_error` (function) component `document_degradation_for_error [function]` (`f10669b8-0540-5d77-9e5a-f0252c503b0e`) lines 213-228 [crates/gwiki/src/ingest/document/render.rs:213-228]
  - Signature: `pub(crate) fn document_degradation_for_error(`
  - Purpose: Maps the request’s 'SourceKind' to an appropriate 'DocumentFailureMode', computes the document unit count from the file name and kind, and returns a 'DocumentDegradation' whose message wraps the supplied error while noting the original asset is preserved. [crates/gwiki/src/ingest/document/render.rs:213-228]
- `document_unit_count_for_failure` (function) component `document_unit_count_for_failure [function]` (`6284fb14-9c85-5ee6-a5f8-27f0606ae33c`) lines 230-241 [crates/gwiki/src/ingest/document/render.rs:230-241]
  - Signature: `fn document_unit_count_for_failure(file_name: &str, kind: &SourceKind) -> DocumentUnitCount {`
  - Purpose: 'document_unit_count_for_failure' returns a zero-or-one 'DocumentUnitCount' sentinel for a failed document based on 'SourceKind', using 'pages(1)' for HTML, 'pages(0)' for PDF and most other kinds, 'slides(0)' for '.pptx', and 'sheets(0)' for spreadsheet Office formats ('.xlsx', '.xls', '.ods'). [crates/gwiki/src/ingest/document/render.rs:230-241]
- `document_degradation_maps_pdf_failure_to_pdf_mode` (function) component `document_degradation_maps_pdf_failure_to_pdf_mode [function]` (`fc3b8bc3-49e9-59e1-afac-ea15c601a0d9`) lines 248-260 [crates/gwiki/src/ingest/document/render.rs:248-260]
  - Signature: `fn document_degradation_maps_pdf_failure_to_pdf_mode() {`
  - Purpose: Verifies that a PDF 'DocumentRequest' with a text-layer failure is mapped by 'document_degradation_for_error' to a degradation reason of 'pdf_text_layer_error' with 'unit_count.key()' set to 'page_count'. [crates/gwiki/src/ingest/document/render.rs:248-260]
- `document_degradation_uses_unsupported_source_for_non_documents` (function) component `document_degradation_uses_unsupported_source_for_non_documents [function]` (`fc378d96-9650-50f1-a916-246f73e66981`) lines 263-274 [crates/gwiki/src/ingest/document/render.rs:263-274]
  - Signature: `fn document_degradation_uses_unsupported_source_for_non_documents() {`
  - Purpose: Verifies that 'document_degradation_for_error' returns a degradation whose reason is '"unsupported_source"' when a 'DocumentRequest' for non-document text input fails with a “not a document” error. [crates/gwiki/src/ingest/document/render.rs:263-274]

