---
title: crates/gwiki/src/ingest/pdf/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/tests.rs
  ranges:
  - '21'
  - 23-27
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
  - 446-453
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/pdf/tests.rs:21](crates/gwiki/src/ingest/pdf/tests.rs#L21), [crates/gwiki/src/ingest/pdf/tests.rs:23-27](crates/gwiki/src/ingest/pdf/tests.rs#L23-L27), [crates/gwiki/src/ingest/pdf/tests.rs:30-59](crates/gwiki/src/ingest/pdf/tests.rs#L30-L59), [crates/gwiki/src/ingest/pdf/tests.rs:63-65](crates/gwiki/src/ingest/pdf/tests.rs#L63-L65), [crates/gwiki/src/ingest/pdf/tests.rs:69-74](crates/gwiki/src/ingest/pdf/tests.rs#L69-L74), [crates/gwiki/src/ingest/pdf/tests.rs:77-137](crates/gwiki/src/ingest/pdf/tests.rs#L77-L137), [crates/gwiki/src/ingest/pdf/tests.rs:140-175](crates/gwiki/src/ingest/pdf/tests.rs#L140-L175), [crates/gwiki/src/ingest/pdf/tests.rs:178-182](crates/gwiki/src/ingest/pdf/tests.rs#L178-L182), [crates/gwiki/src/ingest/pdf/tests.rs:185-231](crates/gwiki/src/ingest/pdf/tests.rs#L185-L231), [crates/gwiki/src/ingest/pdf/tests.rs:234-289](crates/gwiki/src/ingest/pdf/tests.rs#L234-L289), [crates/gwiki/src/ingest/pdf/tests.rs:292-324](crates/gwiki/src/ingest/pdf/tests.rs#L292-L324), [crates/gwiki/src/ingest/pdf/tests.rs:327-331](crates/gwiki/src/ingest/pdf/tests.rs#L327-L331), [crates/gwiki/src/ingest/pdf/tests.rs:334-442](crates/gwiki/src/ingest/pdf/tests.rs#L334-L442), [crates/gwiki/src/ingest/pdf/tests.rs:446-453](crates/gwiki/src/ingest/pdf/tests.rs#L446-L453)

</details>

# crates/gwiki/src/ingest/pdf/tests.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file contains PDF-ingest tests for the `gwiki` pipeline. It defines fake `VisionClient` implementations and a timestamp helper to exercise page rendering, OCR/vision integration, markdown sanitization, page reference preservation, rollback behavior on write failures, and degradation/budget reporting, while also checking public defaults like render DPI and fetched-at parsing.
[crates/gwiki/src/ingest/pdf/tests.rs:21]
[crates/gwiki/src/ingest/pdf/tests.rs:23-27]
[crates/gwiki/src/ingest/pdf/tests.rs:30-59]
[crates/gwiki/src/ingest/pdf/tests.rs:63-65]
[crates/gwiki/src/ingest/pdf/tests.rs:69-74]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `FakePdfVisionClient` | class | `struct FakePdfVisionClient;` | `FakePdfVisionClient [class]` | `be728204-9652-54d8-be56-194cd549312e` | 21-21 [crates/gwiki/src/ingest/pdf/tests.rs:21] | Indexed class `FakePdfVisionClient` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:21] |
| `fetched_at` | function | `fn fetched_at(value: &str) -> DateTime<Utc> {` | `fetched_at [function]` | `c2dc37b0-0f30-574d-800d-4e6337a5dc7e` | 23-27 [crates/gwiki/src/ingest/pdf/tests.rs:23-27] | Indexed function `fetched_at` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:23-27] |
| `FakePdfVisionClient::extract` | method | `fn extract(&self, request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {` | `FakePdfVisionClient::extract [method]` | `4842ab69-0b66-5814-a7fa-c1e4a28b580f` | 30-59 [crates/gwiki/src/ingest/pdf/tests.rs:30-59] | Indexed method `FakePdfVisionClient::extract` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:30-59] |
| `default_pdf_render_dpi_is_public_ingest_default` | function | `fn default_pdf_render_dpi_is_public_ingest_default() {` | `default_pdf_render_dpi_is_public_ingest_default [function]` | `de0178ec-0be4-5b54-968a-95dd771b403a` | 63-65 [crates/gwiki/src/ingest/pdf/tests.rs:63-65] | Indexed function `default_pdf_render_dpi_is_public_ingest_default` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:63-65] |
| `pdf_fetched_at_accepts_collect_timestamp_format` | function | `fn pdf_fetched_at_accepts_collect_timestamp_format() {` | `pdf_fetched_at_accepts_collect_timestamp_format [function]` | `651c7a0e-8cc1-53c2-bbe6-52a6ad8a624c` | 69-74 [crates/gwiki/src/ingest/pdf/tests.rs:69-74] | Indexed function `pdf_fetched_at_accepts_collect_timestamp_format` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:69-74] |
| `combines_text_layer_and_vision` | function | `fn combines_text_layer_and_vision() {` | `combines_text_layer_and_vision [function]` | `a57807e9-26ae-5cc9-9731-cb76d1c417f3` | 77-137 [crates/gwiki/src/ingest/pdf/tests.rs:77-137] | Indexed function `combines_text_layer_and_vision` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:77-137] |
| `pdf_rendered_page_file_names_use_file_stem_for_uppercase_extension` | function | `fn pdf_rendered_page_file_names_use_file_stem_for_uppercase_extension() {` | `pdf_rendered_page_file_names_use_file_stem_for_uppercase_extension [function]` | `a1621a35-c600-5cd5-a74c-fb33b24fbec1` | 140-175 [crates/gwiki/src/ingest/pdf/tests.rs:140-175] | Indexed function `pdf_rendered_page_file_names_use_file_stem_for_uppercase_extension` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:140-175] |
| `pdf_markdown_escapes_horizontal_rules` | function | `fn pdf_markdown_escapes_horizontal_rules() {` | `pdf_markdown_escapes_horizontal_rules [function]` | `cdd3baf6-20f1-55f7-82ad-536a53b02630` | 178-182 [crates/gwiki/src/ingest/pdf/tests.rs:178-182] | Indexed function `pdf_markdown_escapes_horizontal_rules` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:178-182] |
| `pdf_ingest_preserves_page_refs` | function | `fn pdf_ingest_preserves_page_refs() {` | `pdf_ingest_preserves_page_refs [function]` | `78e2f787-876d-5c9b-a1d3-960ac3859db5` | 185-231 [crates/gwiki/src/ingest/pdf/tests.rs:185-231] | Indexed function `pdf_ingest_preserves_page_refs` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:185-231] |
| `pdf_ingest_rolls_back_manifest_and_asset_when_raw_write_fails` | function | `fn pdf_ingest_rolls_back_manifest_and_asset_when_raw_write_fails() {` | `pdf_ingest_rolls_back_manifest_and_asset_when_raw_write_fails [function]` | `fbba5051-b8e0-5e5b-a2f5-de83b98d2bca` | 234-289 [crates/gwiki/src/ingest/pdf/tests.rs:234-289] | Indexed function `pdf_ingest_rolls_back_manifest_and_asset_when_raw_write_fails` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:234-289] |
| `pdf_page_body_sanitizes_internal_markers_and_fences` | function | `fn pdf_page_body_sanitizes_internal_markers_and_fences() {` | `pdf_page_body_sanitizes_internal_markers_and_fences [function]` | `915f2c72-e444-5f1b-bcea-44162ed440b8` | 292-324 [crates/gwiki/src/ingest/pdf/tests.rs:292-324] | Indexed function `pdf_page_body_sanitizes_internal_markers_and_fences` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:292-324] |
| `pdf_page_text_preserves_paragraph_breaks` | function | `fn pdf_page_text_preserves_paragraph_breaks() {` | `pdf_page_text_preserves_paragraph_breaks [function]` | `c1dd5924-cdc4-5bc6-900f-f73532afc037` | 327-331 [crates/gwiki/src/ingest/pdf/tests.rs:327-331] | Indexed function `pdf_page_text_preserves_paragraph_breaks` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:327-331] |
| `pdf_degradation_uses_uniform_metadata` | function | `fn pdf_degradation_uses_uniform_metadata() {` | `pdf_degradation_uses_uniform_metadata [function]` | `1e0be664-e79e-5c8c-984f-34315b94a355` | 334-442 [crates/gwiki/src/ingest/pdf/tests.rs:334-442] | Indexed function `pdf_degradation_uses_uniform_metadata` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:334-442] |
| `FailingPdfVisionClient` | class | `struct FailingPdfVisionClient;` | `FailingPdfVisionClient [class]` | `8492045a-b975-52a0-a290-1b5d37027d9f` | 335-335 [crates/gwiki/src/ingest/pdf/tests.rs:335] | Indexed class `FailingPdfVisionClient` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:335] |
| `FailingPdfVisionClient::extract` | method | `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {` | `FailingPdfVisionClient::extract [method]` | `1af04065-a24d-5ec0-9a7b-1978a0f5934b` | 338-343 [crates/gwiki/src/ingest/pdf/tests.rs:338-343] | Indexed method `FailingPdfVisionClient::extract` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:338-343] |
| `pdf_render_budget_degradation_records_limits` | function | `fn pdf_render_budget_degradation_records_limits() {` | `pdf_render_budget_degradation_records_limits [function]` | `907a1b8c-f67b-5e65-8df7-7f7a2aa6e62a` | 446-453 [crates/gwiki/src/ingest/pdf/tests.rs:446-453] | Indexed function `pdf_render_budget_degradation_records_limits` in `crates/gwiki/src/ingest/pdf/tests.rs`. [crates/gwiki/src/ingest/pdf/tests.rs:446-453] |
