---
title: crates/gwiki/src/ingest/image.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/image.rs
  ranges:
  - 23-31
  - 34-40
  - 43-56
  - 59-70
  - 72-103
  - 106-116
  - 118-167
  - 169-177
  - 179-210
  - 213-218
  - 228-238
  - 241-272
  - 275-297
  - 301-335
  - 338-370
  - 373-375
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/image.rs

Module: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Purpose

Defines the image ingestion pipeline for gwiki, centered on an `ImageSnapshot` input and an `ImageIngestResult` that records the generated source record plus raw, asset, and derived output paths and any vision degradation used. The top-level `ingest_image` path falls back to default degradation, while the production and non-production vision variants split index updates from ingestion work; shared helpers then render raw image markdown, decide whether original images are stored, determine scope-indexed metadata, and build the final `IngestResult` from the produced files and vision output.
[crates/gwiki/src/ingest/image.rs:23-31]
[crates/gwiki/src/ingest/image.rs:34-40]
[crates/gwiki/src/ingest/image.rs:43-56]
[crates/gwiki/src/ingest/image.rs:59-70]
[crates/gwiki/src/ingest/image.rs:72-103]

## API Symbols

- `ImageSnapshot` (class) component `ImageSnapshot [class]` (`49593152-39ab-5a75-8938-baa51af371ee`) lines 23-31 [crates/gwiki/src/ingest/image.rs:23-31]
  - Signature: `pub struct ImageSnapshot {`
  - Purpose: Indexed class `ImageSnapshot` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:23-31]
- `ImageIngestResult` (class) component `ImageIngestResult [class]` (`d430a5ba-d38e-5621-98e1-f3c88139c74a`) lines 34-40 [crates/gwiki/src/ingest/image.rs:34-40]
  - Signature: `pub struct ImageIngestResult {`
  - Purpose: Indexed class `ImageIngestResult` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:34-40]
- `ingest_image` (function) component `ingest_image [function]` (`ccee54f4-7a59-5c41-807c-84d9ea060a10`) lines 43-56 [crates/gwiki/src/ingest/image.rs:43-56]
  - Signature: `pub fn ingest_image(`
  - Purpose: Indexed function `ingest_image` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:43-56]
- `ingest_image_with_production_vision` (function) component `ingest_image_with_production_vision [function]` (`75fb5927-0fdb-584c-9406-a731bf426c2f`) lines 59-70 [crates/gwiki/src/ingest/image.rs:59-70]
  - Signature: `pub fn ingest_image_with_production_vision(`
  - Purpose: Indexed function `ingest_image_with_production_vision` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:59-70]
- `ingest_image_with_production_vision_without_index` (function) component `ingest_image_with_production_vision_without_index [function]` (`a9f9e868-fb7d-51eb-a304-712192b7363c`) lines 72-103 [crates/gwiki/src/ingest/image.rs:72-103]
  - Signature: `pub(crate) fn ingest_image_with_production_vision_without_index(`
  - Purpose: Indexed function `ingest_image_with_production_vision_without_index` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:72-103]
- `ingest_image_with_vision` (function) component `ingest_image_with_vision [function]` (`00589531-b7ac-54da-a6ca-02d9c8ea1804`) lines 106-116 [crates/gwiki/src/ingest/image.rs:106-116]
  - Signature: `pub fn ingest_image_with_vision(`
  - Purpose: Indexed function `ingest_image_with_vision` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:106-116]
- `ingest_image_with_vision_without_index` (function) component `ingest_image_with_vision_without_index [function]` (`f6fff319-9e6b-5d72-9655-068135e8ea16`) lines 118-167 [crates/gwiki/src/ingest/image.rs:118-167]
  - Signature: `pub(crate) fn ingest_image_with_vision_without_index(`
  - Purpose: Indexed function `ingest_image_with_vision_without_index` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:118-167]
- `IngestResult` (class) component `IngestResult [class]` (`2485c664-3ffc-50bb-8e20-10aae599721b`) lines 169-177 [crates/gwiki/src/ingest/image.rs:169-177]
  - Signature: `impl From<ImageIngestResult> for IngestResult {`
  - Purpose: Indexed class `IngestResult` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:169-177]
- `IngestResult.from` (method) component `IngestResult.from [method]` (`e4c1ac75-e76a-5527-922d-c10103e12894`) lines 170-176 [crates/gwiki/src/ingest/image.rs:170-176]
  - Signature: `fn from(result: ImageIngestResult) -> Self {`
  - Purpose: Indexed method `IngestResult.from` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:170-176]
- `render_raw_image_markdown` (function) component `render_raw_image_markdown [function]` (`7eaf2504-b8f9-5858-a25f-d8894e98503d`) lines 179-210 [crates/gwiki/src/ingest/image.rs:179-210]
  - Signature: `fn render_raw_image_markdown(`
  - Purpose: Indexed function `render_raw_image_markdown` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:179-210]
- `default_vision_degradation` (function) component `default_vision_degradation [function]` (`56ed51ef-b574-5871-a83d-fae0d7de936c`) lines 213-218 [crates/gwiki/src/ingest/image.rs:213-218]
  - Signature: `fn default_vision_degradation() -> VisionDegradation {`
  - Purpose: Indexed function `default_vision_degradation` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:213-218]
- `sample_snapshot` (function) component `sample_snapshot [function]` (`4a938bf9-d313-56a9-8de9-3df0a6d4cf0d`) lines 228-238 [crates/gwiki/src/ingest/image.rs:228-238]
  - Signature: `fn sample_snapshot() -> ImageSnapshot {`
  - Purpose: Indexed function `sample_snapshot` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:228-238]
- `stores_original_image` (function) component `stores_original_image [function]` (`6b77f398-c0e7-52da-a670-2558a7f4fce3`) lines 241-272 [crates/gwiki/src/ingest/image.rs:241-272]
  - Signature: `fn stores_original_image() {`
  - Purpose: Indexed function `stores_original_image` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:241-272]
- `image_metadata_is_scope_indexed` (function) component `image_metadata_is_scope_indexed [function]` (`5ffa300e-c791-5051-b6b4-348fd0e1ab65`) lines 275-297 [crates/gwiki/src/ingest/image.rs:275-297]
  - Signature: `fn image_metadata_is_scope_indexed() {`
  - Purpose: Indexed function `image_metadata_is_scope_indexed` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:275-297]
- `production_vision_writes_description_and_ocr` (function) component `production_vision_writes_description_and_ocr [function]` (`51ba5929-c913-5501-ba14-5cb6c13f7556`) lines 301-335 [crates/gwiki/src/ingest/image.rs:301-335]
  - Signature: `fn production_vision_writes_description_and_ocr() {`
  - Purpose: Indexed function `production_vision_writes_description_and_ocr` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:301-335]
- `test_ai_context` (function) component `test_ai_context [function]` (`bcaeb7c7-04cc-526c-9ca8-518e741a562e`) lines 338-370 [crates/gwiki/src/ingest/image.rs:338-370]
  - Signature: `fn test_ai_context(api_base: &str) -> gobby_core::ai_context::AiContext {`
  - Purpose: Indexed function `test_ai_context` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:338-370]
- `spawn_vision_server` (function) component `spawn_vision_server [function]` (`88b38b87-9a88-5a32-82af-7819f05bcd6a`) lines 373-375 [crates/gwiki/src/ingest/image.rs:373-375]
  - Signature: `fn spawn_vision_server(response: &'static str) -> (String, crate::test_http::RequestHandle) {`
  - Purpose: Indexed function `spawn_vision_server` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:373-375]

