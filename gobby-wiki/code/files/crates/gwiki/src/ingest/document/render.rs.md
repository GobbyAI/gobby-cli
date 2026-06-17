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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/document/render.rs:11-33](crates/gwiki/src/ingest/document/render.rs#L11-L33), [crates/gwiki/src/ingest/document/render.rs:36-67](crates/gwiki/src/ingest/document/render.rs#L36-L67), [crates/gwiki/src/ingest/document/render.rs:69-93](crates/gwiki/src/ingest/document/render.rs#L69-L93), [crates/gwiki/src/ingest/document/render.rs:95-122](crates/gwiki/src/ingest/document/render.rs#L95-L122), [crates/gwiki/src/ingest/document/render.rs:124-211](crates/gwiki/src/ingest/document/render.rs#L124-L211), [crates/gwiki/src/ingest/document/render.rs:213-228](crates/gwiki/src/ingest/document/render.rs#L213-L228), [crates/gwiki/src/ingest/document/render.rs:230-241](crates/gwiki/src/ingest/document/render.rs#L230-L241), [crates/gwiki/src/ingest/document/render.rs:248-260](crates/gwiki/src/ingest/document/render.rs#L248-L260), [crates/gwiki/src/ingest/document/render.rs:263-274](crates/gwiki/src/ingest/document/render.rs#L263-L274)

</details>

# crates/gwiki/src/ingest/document/render.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file builds and persists markdown representations of ingested documents. `render_raw_document_markdown` formats a snapshot plus source metadata into a simple raw-document markdown page, while `render_document_derived_markdown` produces the richer derived document output using the scope, source record, snapshot, title, extracted content, and any degradation details. `write_document_derived_markdown` resolves the derived path, creates parent directories, renders the markdown, and writes it atomically through a temp file helper. The remaining helpers support that pipeline by creating the temp file and mapping document failures into degradation data, unit counts, and mode-specific degradation cases for PDFs and unsupported source types.
[crates/gwiki/src/ingest/document/render.rs:11-33]
[crates/gwiki/src/ingest/document/render.rs:36-67]
[crates/gwiki/src/ingest/document/render.rs:69-93]
[crates/gwiki/src/ingest/document/render.rs:95-122]
[crates/gwiki/src/ingest/document/render.rs:124-211]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `render_raw_document_markdown` | function | `pub(crate) fn render_raw_document_markdown(` | `render_raw_document_markdown [function]` | `57f61d7a-3731-520b-a579-76f4f505c22d` | 11-33 [crates/gwiki/src/ingest/document/render.rs:11-33] | Indexed function `render_raw_document_markdown` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:11-33] |
| `write_document_derived_markdown` | function | `pub(crate) fn write_document_derived_markdown(` | `write_document_derived_markdown [function]` | `3c268ad6-387c-5585-8bb8-97ecb9fde676` | 36-67 [crates/gwiki/src/ingest/document/render.rs:36-67] | Indexed function `write_document_derived_markdown` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:36-67] |
| `write_document_markdown_atomic` | function | `fn write_document_markdown_atomic(path: &Path, contents: &[u8]) -> Result<(), WikiError> {` | `write_document_markdown_atomic [function]` | `554261b9-ac01-5d3f-af7c-f6248e0a3034` | 69-93 [crates/gwiki/src/ingest/document/render.rs:69-93] | Indexed function `write_document_markdown_atomic` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:69-93] |
| `create_document_temp_file` | function | `fn create_document_temp_file(path: &Path) -> Result<NamedTempFile, WikiError> {` | `create_document_temp_file [function]` | `3c09510a-fe5d-53e3-9cf1-861a3002dc5d` | 95-122 [crates/gwiki/src/ingest/document/render.rs:95-122] | Indexed function `create_document_temp_file` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:95-122] |
| `render_document_derived_markdown` | function | `fn render_document_derived_markdown(` | `render_document_derived_markdown [function]` | `a3a6a5d5-1f3f-5fbd-b4f4-ad403beb4630` | 124-211 [crates/gwiki/src/ingest/document/render.rs:124-211] | Indexed function `render_document_derived_markdown` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:124-211] |
| `document_degradation_for_error` | function | `pub(crate) fn document_degradation_for_error(` | `document_degradation_for_error [function]` | `f10669b8-0540-5d77-9e5a-f0252c503b0e` | 213-228 [crates/gwiki/src/ingest/document/render.rs:213-228] | Indexed function `document_degradation_for_error` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:213-228] |
| `document_unit_count_for_failure` | function | `fn document_unit_count_for_failure(file_name: &str, kind: &SourceKind) -> DocumentUnitCount {` | `document_unit_count_for_failure [function]` | `6284fb14-9c85-5ee6-a5f8-27f0606ae33c` | 230-241 [crates/gwiki/src/ingest/document/render.rs:230-241] | Indexed function `document_unit_count_for_failure` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:230-241] |
| `document_degradation_maps_pdf_failure_to_pdf_mode` | function | `fn document_degradation_maps_pdf_failure_to_pdf_mode() {` | `document_degradation_maps_pdf_failure_to_pdf_mode [function]` | `fc3b8bc3-49e9-59e1-afac-ea15c601a0d9` | 248-260 [crates/gwiki/src/ingest/document/render.rs:248-260] | Indexed function `document_degradation_maps_pdf_failure_to_pdf_mode` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:248-260] |
| `document_degradation_uses_unsupported_source_for_non_documents` | function | `fn document_degradation_uses_unsupported_source_for_non_documents() {` | `document_degradation_uses_unsupported_source_for_non_documents [function]` | `fc378d96-9650-50f1-a916-246f73e66981` | 263-274 [crates/gwiki/src/ingest/document/render.rs:263-274] | Indexed function `document_degradation_uses_unsupported_source_for_non_documents` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:263-274] |
