---
title: crates/gwiki/src/ingest/pdf/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/tests.rs
  ranges:
  - '21'
  - 23-27
  - 29-60
  - 30-59
  - 63-65
  - 69-74
  - 77-137
  - 140-175
  - 178-182
  - 185-231
  - 234-289
  - 292-324
  - 327-331
  - 334-442
  - '335'
  - 337-344
  - 338-343
  - 446-453
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/tests.rs

Module: [[code/modules/crates/gwiki/src/ingest/pdf|crates/gwiki/src/ingest/pdf]]

## Purpose

`crates/gwiki/src/ingest/pdf/tests.rs` exposes 18 indexed API symbols.
[crates/gwiki/src/ingest/pdf/tests.rs:21]
[crates/gwiki/src/ingest/pdf/tests.rs:23-27]
[crates/gwiki/src/ingest/pdf/tests.rs:29-60]
[crates/gwiki/src/ingest/pdf/tests.rs:30-59]
[crates/gwiki/src/ingest/pdf/tests.rs:63-65]

## API Symbols

- `FakePdfVisionClient` (class) component `FakePdfVisionClient [class]` (`be728204-9652-54d8-be56-194cd549312e`) lines 21-21 [crates/gwiki/src/ingest/pdf/tests.rs:21]
  - Signature: `struct FakePdfVisionClient;`
  - Purpose: FakePdfVisionClient is a Rust unit struct that serves as a mock implementation of a PDF vision client for testing purposes. [crates/gwiki/src/ingest/pdf/tests.rs:21]
- `fetched_at` (function) component `fetched_at [function]` (`c2dc37b0-0f30-574d-800d-4e6337a5dc7e`) lines 23-27 [crates/gwiki/src/ingest/pdf/tests.rs:23-27]
  - Signature: `fn fetched_at(value: &str) -> DateTime<Utc> {`
  - Purpose: Parses an RFC3339-formatted timestamp string and returns it as a UTC-timezone `DateTime`, panicking if the input is invalid. [crates/gwiki/src/ingest/pdf/tests.rs:23-27]
- `FakePdfVisionClient` (class) component `FakePdfVisionClient [class]` (`20497d71-8f2f-5ac9-beb1-2c524f1c6e47`) lines 29-60 [crates/gwiki/src/ingest/pdf/tests.rs:29-60]
  - Signature: `impl VisionClient for FakePdfVisionClient {`
  - Purpose: FakePdfVisionClient is a test mock implementing VisionClient that validates PNG image request parameters and returns deterministic vision extractions with page-specific OCR text. [crates/gwiki/src/ingest/pdf/tests.rs:29-60]
- `FakePdfVisionClient.extract` (method) component `FakePdfVisionClient.extract [method]` (`4842ab69-0b66-5814-a7fa-c1e4a28b580f`) lines 30-59 [crates/gwiki/src/ingest/pdf/tests.rs:30-59]
  - Signature: `fn extract(&self, request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: **Asserts PNG image specifications (1200×1600 dimensions and valid asset path), then returns mock VisionExtraction with conditional OCR text based on whether the filename contains "page-2".** [crates/gwiki/src/ingest/pdf/tests.rs:30-59]
- `default_pdf_render_dpi_is_public_ingest_default` (function) component `default_pdf_render_dpi_is_public_ingest_default [function]` (`de0178ec-0be4-5b54-968a-95dd771b403a`) lines 63-65 [crates/gwiki/src/ingest/pdf/tests.rs:63-65]
  - Signature: `fn default_pdf_render_dpi_is_public_ingest_default() {`
  - Purpose: This is a unit test that verifies the `DEFAULT_PDF_RENDER_DPI` constant equals 150. [crates/gwiki/src/ingest/pdf/tests.rs:63-65]
- `pdf_fetched_at_accepts_collect_timestamp_format` (function) component `pdf_fetched_at_accepts_collect_timestamp_format [function]` (`651c7a0e-8cc1-53c2-bbe6-52a6ad8a624c`) lines 69-74 [crates/gwiki/src/ingest/pdf/tests.rs:69-74]
  - Signature: `fn pdf_fetched_at_accepts_collect_timestamp_format() {`
  - Purpose: This test validates that the `pdf_fetched_at` function correctly parses Unix millisecond timestamps prefixed with "unix-ms:" and rejects invalid timestamp formats. [crates/gwiki/src/ingest/pdf/tests.rs:69-74]
- `combines_text_layer_and_vision` (function) component `combines_text_layer_and_vision [function]` (`a57807e9-26ae-5cc9-9731-cb76d1c417f3`) lines 77-137 [crates/gwiki/src/ingest/pdf/tests.rs:77-137]
  - Signature: `fn combines_text_layer_and_vision() {`
  - Purpose: This test function validates that the PDF ingestion process correctly combines native text layer extraction with vision-based content analysis from rendered pages into a unified markdown output. [crates/gwiki/src/ingest/pdf/tests.rs:77-137]
- `pdf_rendered_page_file_names_use_file_stem_for_uppercase_extension` (function) component `pdf_rendered_page_file_names_use_file_stem_for_uppercase_extension [function]` (`a1621a35-c600-5cd5-a74c-fb33b24fbec1`) lines 140-175 [crates/gwiki/src/ingest/pdf/tests.rs:140-175]
  - Signature: `fn pdf_rendered_page_file_names_use_file_stem_for_uppercase_extension() {`
  - Purpose: This function validates that rendered PDF page filenames are generated using the lowercase file stem (excluding the uppercase file extension) during vision-based PDF ingestion and markdown generation. [crates/gwiki/src/ingest/pdf/tests.rs:140-175]
- `pdf_markdown_escapes_horizontal_rules` (function) component `pdf_markdown_escapes_horizontal_rules [function]` (`cdd3baf6-20f1-55f7-82ad-536a53b02630`) lines 178-182 [crates/gwiki/src/ingest/pdf/tests.rs:178-182]
  - Signature: `fn pdf_markdown_escapes_horizontal_rules() {`
  - Purpose: This test verifies that `sanitize_pdf_page_markdown` escapes markdown horizontal rule constructs (`---`, `- - -`, `___`, `* * *`) with backslashes while preserving non-rule sequences. [crates/gwiki/src/ingest/pdf/tests.rs:178-182]
- `pdf_ingest_preserves_page_refs` (function) component `pdf_ingest_preserves_page_refs [function]` (`78e2f787-876d-5c9b-a1d3-960ac3859db5`) lines 185-231 [crates/gwiki/src/ingest/pdf/tests.rs:185-231]
  - Signature: `fn pdf_ingest_preserves_page_refs() {`
  - Purpose: # Summary

Verifies that PDF ingestion preserves page-level references through HTML comments in the generated markdown while storing the source PDF asset and maintaining content hash integrity in the source manifest. [crates/gwiki/src/ingest/pdf/tests.rs:185-231]
- `pdf_ingest_rolls_back_manifest_and_asset_when_raw_write_fails` (function) component `pdf_ingest_rolls_back_manifest_and_asset_when_raw_write_fails [function]` (`fbba5051-b8e0-5e5b-a2f5-de83b98d2bca`) lines 234-289 [crates/gwiki/src/ingest/pdf/tests.rs:234-289]
  - Signature: `fn pdf_ingest_rolls_back_manifest_and_asset_when_raw_write_fails() {`
  - Purpose: # Summary

This test verifies that failed PDF ingestion due to a raw file write conflict triggers transactional rollback of both the source manifest and any created assets. [crates/gwiki/src/ingest/pdf/tests.rs:234-289]
- `pdf_page_body_sanitizes_internal_markers_and_fences` (function) component `pdf_page_body_sanitizes_internal_markers_and_fences [function]` (`915f2c72-e444-5f1b-bcea-44162ed440b8`) lines 292-324 [crates/gwiki/src/ingest/pdf/tests.rs:292-324]
  - Signature: `fn pdf_page_body_sanitizes_internal_markers_and_fences() {`
  - Purpose: This test verifies that `render_pdf_markdown` sanitizes PDF page markdown by correcting internal page markers to the actual page number, escaping extraneous markers with spaces, and backslash-escaping markdown fence delimiters. [crates/gwiki/src/ingest/pdf/tests.rs:292-324]
- `pdf_page_text_preserves_paragraph_breaks` (function) component `pdf_page_text_preserves_paragraph_breaks [function]` (`c1dd5924-cdc4-5bc6-900f-f73532afc037`) lines 327-331 [crates/gwiki/src/ingest/pdf/tests.rs:327-331]
  - Signature: `fn pdf_page_text_preserves_paragraph_breaks() {`
  - Purpose: This unit test verifies that `normalize_page_text()` collapses intra-paragraph line breaks while preserving inter-paragraph blank lines (double newlines). [crates/gwiki/src/ingest/pdf/tests.rs:327-331]
- `pdf_degradation_uses_uniform_metadata` (function) component `pdf_degradation_uses_uniform_metadata [function]` (`1e0be664-e79e-5c8c-984f-34315b94a355`) lines 334-442 [crates/gwiki/src/ingest/pdf/tests.rs:334-442]
  - Signature: `fn pdf_degradation_uses_uniform_metadata() {`
  - Purpose: This test verifies that PDF ingestion with a failing vision provider correctly generates uniform degradation metadata (including error classification, file metrics, and page count) while preserving the original PDF asset bytes. [crates/gwiki/src/ingest/pdf/tests.rs:334-442]
- `FailingPdfVisionClient` (class) component `FailingPdfVisionClient [class]` (`8492045a-b975-52a0-a290-1b5d37027d9f`) lines 335-335 [crates/gwiki/src/ingest/pdf/tests.rs:335]
  - Signature: `struct FailingPdfVisionClient;`
  - Purpose: `FailingPdfVisionClient` is a unit struct (zero-sized type) that serves as a mock implementation of a PDF vision client designed to fail for testing purposes. [crates/gwiki/src/ingest/pdf/tests.rs:335]
- `FailingPdfVisionClient` (class) component `FailingPdfVisionClient [class]` (`e272fd09-cbe3-5148-9d16-06a9976ed587`) lines 337-344 [crates/gwiki/src/ingest/pdf/tests.rs:337-344]
  - Signature: `impl VisionClient for FailingPdfVisionClient {`
  - Purpose: **FailingPdfVisionClient** is a `VisionClient` implementation that unconditionally returns a `WikiError::InvalidInput` for any vision extraction request, serving as a deliberate failure stub. [crates/gwiki/src/ingest/pdf/tests.rs:337-344]
- `FailingPdfVisionClient.extract` (method) component `FailingPdfVisionClient.extract [method]` (`1af04065-a24d-5ec0-9a7b-1978a0f5934b`) lines 338-343 [crates/gwiki/src/ingest/pdf/tests.rs:338-343]
  - Signature: `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: This method unconditionally returns a `WikiError::InvalidInput` with the message "vision provider failed," regardless of the input `VisionRequest`. [crates/gwiki/src/ingest/pdf/tests.rs:338-343]
- `pdf_render_budget_degradation_records_limits` (function) component `pdf_render_budget_degradation_records_limits [function]` (`0f613e1b-3655-5fd0-a9ac-5b49034292b1`) lines 446-453 [crates/gwiki/src/ingest/pdf/tests.rs:446-453]
  - Signature: `fn pdf_render_budget_degradation_records_limits() {`
  - Purpose: This test verifies that `pdf_render_budget_degradation(40, 1024)` correctly records a budget-exceeded degradation event with unit count of 40 and generates a fallback message specifying page and byte rendering limits. [crates/gwiki/src/ingest/pdf/tests.rs:446-453]

