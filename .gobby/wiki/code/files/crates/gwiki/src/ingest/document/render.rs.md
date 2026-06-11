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

`crates/gwiki/src/ingest/document/render.rs` exposes 9 indexed API symbols.
[crates/gwiki/src/ingest/document/render.rs:11-33]
[crates/gwiki/src/ingest/document/render.rs:36-67]
[crates/gwiki/src/ingest/document/render.rs:69-93]
[crates/gwiki/src/ingest/document/render.rs:95-122]
[crates/gwiki/src/ingest/document/render.rs:124-211]

## API Symbols

- `render_raw_document_markdown` (function) component `render_raw_document_markdown [function]` (`57f61d7a-3731-520b-a579-76f4f505c22d`) lines 11-33 [crates/gwiki/src/ingest/document/render.rs:11-33]
  - Signature: `pub(crate) fn render_raw_document_markdown(`
  - Purpose: Indexed function `render_raw_document_markdown` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:11-33]
- `write_document_derived_markdown` (function) component `write_document_derived_markdown [function]` (`3c268ad6-387c-5585-8bb8-97ecb9fde676`) lines 36-67 [crates/gwiki/src/ingest/document/render.rs:36-67]
  - Signature: `pub(crate) fn write_document_derived_markdown(`
  - Purpose: Indexed function `write_document_derived_markdown` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:36-67]
- `write_document_markdown_atomic` (function) component `write_document_markdown_atomic [function]` (`554261b9-ac01-5d3f-af7c-f6248e0a3034`) lines 69-93 [crates/gwiki/src/ingest/document/render.rs:69-93]
  - Signature: `fn write_document_markdown_atomic(path: &Path, contents: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Indexed function `write_document_markdown_atomic` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:69-93]
- `create_document_temp_file` (function) component `create_document_temp_file [function]` (`3c09510a-fe5d-53e3-9cf1-861a3002dc5d`) lines 95-122 [crates/gwiki/src/ingest/document/render.rs:95-122]
  - Signature: `fn create_document_temp_file(path: &Path) -> Result<NamedTempFile, WikiError> {`
  - Purpose: Indexed function `create_document_temp_file` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:95-122]
- `render_document_derived_markdown` (function) component `render_document_derived_markdown [function]` (`a3a6a5d5-1f3f-5fbd-b4f4-ad403beb4630`) lines 124-211 [crates/gwiki/src/ingest/document/render.rs:124-211]
  - Signature: `fn render_document_derived_markdown(`
  - Purpose: Indexed function `render_document_derived_markdown` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:124-211]
- `document_degradation_for_error` (function) component `document_degradation_for_error [function]` (`f10669b8-0540-5d77-9e5a-f0252c503b0e`) lines 213-228 [crates/gwiki/src/ingest/document/render.rs:213-228]
  - Signature: `pub(crate) fn document_degradation_for_error(`
  - Purpose: Indexed function `document_degradation_for_error` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:213-228]
- `document_unit_count_for_failure` (function) component `document_unit_count_for_failure [function]` (`6284fb14-9c85-5ee6-a5f8-27f0606ae33c`) lines 230-241 [crates/gwiki/src/ingest/document/render.rs:230-241]
  - Signature: `fn document_unit_count_for_failure(file_name: &str, kind: &SourceKind) -> DocumentUnitCount {`
  - Purpose: Indexed function `document_unit_count_for_failure` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:230-241]
- `document_degradation_maps_pdf_failure_to_pdf_mode` (function) component `document_degradation_maps_pdf_failure_to_pdf_mode [function]` (`fc3b8bc3-49e9-59e1-afac-ea15c601a0d9`) lines 248-260 [crates/gwiki/src/ingest/document/render.rs:248-260]
  - Signature: `fn document_degradation_maps_pdf_failure_to_pdf_mode() {`
  - Purpose: Indexed function `document_degradation_maps_pdf_failure_to_pdf_mode` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:248-260]
- `document_degradation_uses_unsupported_source_for_non_documents` (function) component `document_degradation_uses_unsupported_source_for_non_documents [function]` (`fc378d96-9650-50f1-a916-246f73e66981`) lines 263-274 [crates/gwiki/src/ingest/document/render.rs:263-274]
  - Signature: `fn document_degradation_uses_unsupported_source_for_non_documents() {`
  - Purpose: Indexed function `document_degradation_uses_unsupported_source_for_non_documents` in `crates/gwiki/src/ingest/document/render.rs`. [crates/gwiki/src/ingest/document/render.rs:263-274]

