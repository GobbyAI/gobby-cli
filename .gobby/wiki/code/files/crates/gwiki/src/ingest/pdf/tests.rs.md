---
title: crates/gwiki/src/ingest/pdf/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/tests.rs
  ranges:
  - '21'
  - 23-27
  - 29-60
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
  - 446-453
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/tests.rs

Module: [[code/modules/crates/gwiki/src/ingest/pdf|crates/gwiki/src/ingest/pdf]]

## Purpose

Test module for PDF ingestion and rendering behavior. It defines fake `VisionClient` implementations and a timestamp helper so the tests can exercise page ingestion end to end without real vision service calls, then verifies the main PDF pipeline pieces work together correctly: the default render DPI and fetched-at parsing, combining native text extraction with rendered-page vision OCR, naming rendered page assets from the file stem, escaping risky markdown constructs and internal page markers, preserving page references and source asset bytes, rolling back manifest and asset state on write failures, and recording uniform degradation metadata when vision extraction or render budgets fail.
[crates/gwiki/src/ingest/pdf/tests.rs:21]
[crates/gwiki/src/ingest/pdf/tests.rs:23-27]
[crates/gwiki/src/ingest/pdf/tests.rs:29-60]
[crates/gwiki/src/ingest/pdf/tests.rs:30-59]
[crates/gwiki/src/ingest/pdf/tests.rs:63-65]

## API Symbols

- `FakePdfVisionClient` (class) component `FakePdfVisionClient [class]` (`be728204-9652-54d8-be56-194cd549312e`) lines 21-21 [crates/gwiki/src/ingest/pdf/tests.rs:21]
  - Signature: `struct FakePdfVisionClient;`
  - Purpose: A unit struct providing a test fake implementation of a PDF vision client. [crates/gwiki/src/ingest/pdf/tests.rs:21]
- `fetched_at` (function) component `fetched_at [function]` (`c2dc37b0-0f30-574d-800d-4e6337a5dc7e`) lines 23-27 [crates/gwiki/src/ingest/pdf/tests.rs:23-27]
  - Signature: `fn fetched_at(value: &str) -> DateTime<Utc> {`
  - Purpose: Parses an RFC3339-formatted timestamp string into a UTC DateTime object, panicking if the input is invalid. [crates/gwiki/src/ingest/pdf/tests.rs:23-27]
- `FakePdfVisionClient` (class) component `FakePdfVisionClient [class]` (`20497d71-8f2f-5ac9-beb1-2c524f1c6e47`) lines 29-60 [crates/gwiki/src/ingest/pdf/tests.rs:29-60]
  - Signature: `impl VisionClient for FakePdfVisionClient {`
  - Purpose: A test double for `VisionClient` that asserts request invariants (PNG MIME type, specific dimensions, file path format) and returns deterministic mock vision extractions with filename-dependent OCR text. [crates/gwiki/src/ingest/pdf/tests.rs:29-60]
- `FakePdfVisionClient.extract` (method) component `FakePdfVisionClient.extract [method]` (`4842ab69-0b66-5814-a7fa-c1e4a28b580f`) lines 30-59 [crates/gwiki/src/ingest/pdf/tests.rs:30-59]
  - Signature: `fn extract(&self, request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: Validates PNG image specifications (1200×1600 dimensions, .png extension, matching filename) and returns a mock VisionExtraction with page-number-dependent OCR text ("$42" invoice total for "page-2" files, "Growth" chart label otherwise). [crates/gwiki/src/ingest/pdf/tests.rs:30-59]
- `default_pdf_render_dpi_is_public_ingest_default` (function) component `default_pdf_render_dpi_is_public_ingest_default [function]` (`de0178ec-0be4-5b54-968a-95dd771b403a`) lines 63-65 [crates/gwiki/src/ingest/pdf/tests.rs:63-65]
  - Signature: `fn default_pdf_render_dpi_is_public_ingest_default() {`
  - Purpose: A unit test that asserts the `DEFAULT_PDF_RENDER_DPI` constant equals 150. [crates/gwiki/src/ingest/pdf/tests.rs:63-65]
- `pdf_fetched_at_accepts_collect_timestamp_format` (function) component `pdf_fetched_at_accepts_collect_timestamp_format [function]` (`651c7a0e-8cc1-53c2-bbe6-52a6ad8a624c`) lines 69-74 [crates/gwiki/src/ingest/pdf/tests.rs:69-74]
  - Signature: `fn pdf_fetched_at_accepts_collect_timestamp_format() {`
  - Purpose: Validates that `pdf_fetched_at` correctly parses Unix millisecond timestamps in the "unix-ms" format and rejects invalid timestamp strings. [crates/gwiki/src/ingest/pdf/tests.rs:69-74]
- `combines_text_layer_and_vision` (function) component `combines_text_layer_and_vision [function]` (`a57807e9-26ae-5cc9-9731-cb76d1c417f3`) lines 77-137 [crates/gwiki/src/ingest/pdf/tests.rs:77-137]
  - Signature: `fn combines_text_layer_and_vision() {`
  - Purpose: Test validating that PDF page ingestion correctly integrates native text-layer extraction with vision-model analysis of rendered page images. [crates/gwiki/src/ingest/pdf/tests.rs:77-137]
- `pdf_rendered_page_file_names_use_file_stem_for_uppercase_extension` (function) component `pdf_rendered_page_file_names_use_file_stem_for_uppercase_extension [function]` (`a1621a35-c600-5cd5-a74c-fb33b24fbec1`) lines 140-175 [crates/gwiki/src/ingest/pdf/tests.rs:140-175]
  - Signature: `fn pdf_rendered_page_file_names_use_file_stem_for_uppercase_extension() {`
  - Purpose: Verifies that `ingest_pages_with_vision` generates rendered PDF page filenames using the file stem (without extension) rather than preserving uppercase file extensions from the source PDF filename. [crates/gwiki/src/ingest/pdf/tests.rs:140-175]
- `pdf_markdown_escapes_horizontal_rules` (function) component `pdf_markdown_escapes_horizontal_rules [function]` (`cdd3baf6-20f1-55f7-82ad-536a53b02630`) lines 178-182 [crates/gwiki/src/ingest/pdf/tests.rs:178-182]
  - Signature: `fn pdf_markdown_escapes_horizontal_rules() {`
  - Purpose: This test verifies that `sanitize_pdf_page_markdown()` escapes standalone markdown horizontal rule patterns (`---`, `- - -`, `___`, `* * *`) by prepending backslashes to prevent their interpretation as syntax. [crates/gwiki/src/ingest/pdf/tests.rs:178-182]
- `pdf_ingest_preserves_page_refs` (function) component `pdf_ingest_preserves_page_refs [function]` (`78e2f787-876d-5c9b-a1d3-960ac3859db5`) lines 185-231 [crates/gwiki/src/ingest/pdf/tests.rs:185-231]
  - Signature: `fn pdf_ingest_preserves_page_refs() {`
  - Purpose: This test verifies that PDF ingestion generates markdown output with preserved page boundary markers (`gwiki-page` comments), maintains the original PDF asset bytes, and records the content hash in the source manifest. [crates/gwiki/src/ingest/pdf/tests.rs:185-231]
- `pdf_ingest_rolls_back_manifest_and_asset_when_raw_write_fails` (function) component `pdf_ingest_rolls_back_manifest_and_asset_when_raw_write_fails [function]` (`fbba5051-b8e0-5e5b-a2f5-de83b98d2bca`) lines 234-289 [crates/gwiki/src/ingest/pdf/tests.rs:234-289]
  - Signature: `fn pdf_ingest_rolls_back_manifest_and_asset_when_raw_write_fails() {`
  - Purpose: This test verifies that PDF page ingestion atomically rolls back manifest registrations and asset state when raw file writes fail due to path conflicts. [crates/gwiki/src/ingest/pdf/tests.rs:234-289]
- `pdf_page_body_sanitizes_internal_markers_and_fences` (function) component `pdf_page_body_sanitizes_internal_markers_and_fences [function]` (`915f2c72-e444-5f1b-bcea-44162ed440b8`) lines 292-324 [crates/gwiki/src/ingest/pdf/tests.rs:292-324]
  - Signature: `fn pdf_page_body_sanitizes_internal_markers_and_fences() {`
  - Purpose: This test verifies that `render_pdf_markdown` sanitizes embedded gwiki-page comment markers, defangs stale markers with spacing injection, and escapes markdown fence delimiters in PDF page content. [crates/gwiki/src/ingest/pdf/tests.rs:292-324]
- `pdf_page_text_preserves_paragraph_breaks` (function) component `pdf_page_text_preserves_paragraph_breaks [function]` (`c1dd5924-cdc4-5bc6-900f-f73532afc037`) lines 327-331 [crates/gwiki/src/ingest/pdf/tests.rs:327-331]
  - Signature: `fn pdf_page_text_preserves_paragraph_breaks() {`
  - Purpose: Tests that `normalize_page_text()` collapses line breaks within paragraphs while preserving double-newline paragraph delimiters. [crates/gwiki/src/ingest/pdf/tests.rs:327-331]
- `pdf_degradation_uses_uniform_metadata` (function) component `pdf_degradation_uses_uniform_metadata [function]` (`1e0be664-e79e-5c8c-984f-34315b94a355`) lines 334-442 [crates/gwiki/src/ingest/pdf/tests.rs:334-442]
  - Signature: `fn pdf_degradation_uses_uniform_metadata() {`
  - Purpose: This test verifies that PDF ingestion records uniform degradation metadata (including media_degradation field, document degradation section, and file metrics) when vision extraction fails, while preserving the original PDF bytes as an asset. [crates/gwiki/src/ingest/pdf/tests.rs:334-442]
- `FailingPdfVisionClient` (class) component `FailingPdfVisionClient [class]` (`8492045a-b975-52a0-a290-1b5d37027d9f`) lines 335-335 [crates/gwiki/src/ingest/pdf/tests.rs:335]
  - Signature: `struct FailingPdfVisionClient;`
  - Purpose: `FailingPdfVisionClient` is an empty unit struct designed to serve as a mock implementation of a PDF vision client that intentionally fails or simulates failure scenarios. [crates/gwiki/src/ingest/pdf/tests.rs:335]
- `FailingPdfVisionClient` (class) component `FailingPdfVisionClient [class]` (`e272fd09-cbe3-5148-9d16-06a9976ed587`) lines 337-344 [crates/gwiki/src/ingest/pdf/tests.rs:337-344]
  - Signature: `impl VisionClient for FailingPdfVisionClient {`
  - Purpose: FailingPdfVisionClient is a VisionClient implementation that unconditionally returns a WikiError::InvalidInput for any extract request, serving as a test double for vision provider failures. [crates/gwiki/src/ingest/pdf/tests.rs:337-344]
- `FailingPdfVisionClient.extract` (method) component `FailingPdfVisionClient.extract [method]` (`1af04065-a24d-5ec0-9a7b-1978a0f5934b`) lines 338-343 [crates/gwiki/src/ingest/pdf/tests.rs:338-343]
  - Signature: `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: This method is a stub that unconditionally returns a `WikiError::InvalidInput` with the field `"vision"` and message `"vision provider failed"`, indicating an unimplemented vision extraction provider. [crates/gwiki/src/ingest/pdf/tests.rs:338-343]
- `pdf_render_budget_degradation_records_limits` (function) component `pdf_render_budget_degradation_records_limits [function]` (`907a1b8c-f67b-5e65-8df7-7f7a2aa6e62a`) lines 446-453 [crates/gwiki/src/ingest/pdf/tests.rs:446-453]
  - Signature: `fn pdf_render_budget_degradation_records_limits() {`
  - Purpose: Tests that `pdf_render_budget_degradation(40, 1024)` returns a degradation record with reason "pdf_render_budget_exceeded", unit count of 40, and fallback containing the 32-page and 1024-byte render limits. [crates/gwiki/src/ingest/pdf/tests.rs:446-453]

