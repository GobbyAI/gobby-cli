---
title: crates/gwiki/src/ingest/image.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/image.rs
  ranges:
  - 23-31
  - 34-40
  - 42-55
  - 57-68
  - 70-96
  - 98-108
  - 110-159
  - 161-169
  - 162-168
  - 171-202
  - 204-211
  - 213-222
  - 232-242
  - 245-276
  - 279-301
  - 305-339
  - 342-374
  - 377-379
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/image.rs

Module: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Purpose

`crates/gwiki/src/ingest/image.rs` exposes 18 indexed API symbols.
[crates/gwiki/src/ingest/image.rs:23-31]
[crates/gwiki/src/ingest/image.rs:34-40]
[crates/gwiki/src/ingest/image.rs:42-55]
[crates/gwiki/src/ingest/image.rs:57-68]
[crates/gwiki/src/ingest/image.rs:70-96]

## API Symbols

- `ImageSnapshot` (class) component `ImageSnapshot [class]` (`49593152-39ab-5a75-8938-baa51af371ee`) lines 23-31 [crates/gwiki/src/ingest/image.rs:23-31]
  - Signature: `pub struct ImageSnapshot {`
  - Purpose: Indexed class `ImageSnapshot` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:23-31]
- `ImageIngestResult` (class) component `ImageIngestResult [class]` (`d430a5ba-d38e-5621-98e1-f3c88139c74a`) lines 34-40 [crates/gwiki/src/ingest/image.rs:34-40]
  - Signature: `pub struct ImageIngestResult {`
  - Purpose: Indexed class `ImageIngestResult` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:34-40]
- `ingest_image` (function) component `ingest_image [function]` (`10bcabbd-5cb6-5f69-ad24-f183453e576e`) lines 42-55 [crates/gwiki/src/ingest/image.rs:42-55]
  - Signature: `pub fn ingest_image(`
  - Purpose: Indexed function `ingest_image` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:42-55]
- `ingest_image_with_production_vision` (function) component `ingest_image_with_production_vision [function]` (`82791c28-45b7-52da-ae75-b07532d649ec`) lines 57-68 [crates/gwiki/src/ingest/image.rs:57-68]
  - Signature: `pub fn ingest_image_with_production_vision(`
  - Purpose: Indexed function `ingest_image_with_production_vision` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:57-68]
- `ingest_image_with_production_vision_without_index` (function) component `ingest_image_with_production_vision_without_index [function]` (`4a6a3f49-e478-55b6-8ab9-67a5ab53a604`) lines 70-96 [crates/gwiki/src/ingest/image.rs:70-96]
  - Signature: `pub(crate) fn ingest_image_with_production_vision_without_index(`
  - Purpose: Indexed function `ingest_image_with_production_vision_without_index` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:70-96]
- `ingest_image_with_vision` (function) component `ingest_image_with_vision [function]` (`b4e54fcc-008d-5ccc-8b67-52fc0b794c7b`) lines 98-108 [crates/gwiki/src/ingest/image.rs:98-108]
  - Signature: `pub fn ingest_image_with_vision(`
  - Purpose: Indexed function `ingest_image_with_vision` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:98-108]
- `ingest_image_with_vision_without_index` (function) component `ingest_image_with_vision_without_index [function]` (`f4eae93a-04b2-57fa-bc21-8c184365577d`) lines 110-159 [crates/gwiki/src/ingest/image.rs:110-159]
  - Signature: `pub(crate) fn ingest_image_with_vision_without_index(`
  - Purpose: Indexed function `ingest_image_with_vision_without_index` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:110-159]
- `IngestResult` (class) component `IngestResult [class]` (`2d3e124f-79e7-586c-acb0-e73369e26c2a`) lines 161-169 [crates/gwiki/src/ingest/image.rs:161-169]
  - Signature: `impl From<ImageIngestResult> for IngestResult {`
  - Purpose: Indexed class `IngestResult` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:161-169]
- `IngestResult.from` (method) component `IngestResult.from [method]` (`5627cf5a-2f55-579a-8406-b3052ddc4422`) lines 162-168 [crates/gwiki/src/ingest/image.rs:162-168]
  - Signature: `fn from(result: ImageIngestResult) -> Self {`
  - Purpose: Indexed method `IngestResult.from` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:162-168]
- `render_raw_image_markdown` (function) component `render_raw_image_markdown [function]` (`b283c3a7-2cd3-5b20-98dd-3c1f87a38818`) lines 171-202 [crates/gwiki/src/ingest/image.rs:171-202]
  - Signature: `fn render_raw_image_markdown(`
  - Purpose: Indexed function `render_raw_image_markdown` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:171-202]
- `default_vision_degradation` (function) component `default_vision_degradation [function]` (`e9cfc571-314e-5dd5-b7cd-1ba2e76dcb9f`) lines 204-211 [crates/gwiki/src/ingest/image.rs:204-211]
  - Signature: `fn default_vision_degradation() -> VisionDegradation {`
  - Purpose: Indexed function `default_vision_degradation` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:204-211]
- `vision_degradation` (function) component `vision_degradation [function]` (`e09e45b1-b518-5a8d-a0bc-9d61a8ddc0e5`) lines 213-222 [crates/gwiki/src/ingest/image.rs:213-222]
  - Signature: `fn vision_degradation(routing: AiRouting) -> VisionDegradation {`
  - Purpose: Indexed function `vision_degradation` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:213-222]
- `sample_snapshot` (function) component `sample_snapshot [function]` (`66cbcc5b-39f8-533e-953e-0d21d9dcc6eb`) lines 232-242 [crates/gwiki/src/ingest/image.rs:232-242]
  - Signature: `fn sample_snapshot() -> ImageSnapshot {`
  - Purpose: Indexed function `sample_snapshot` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:232-242]
- `stores_original_image` (function) component `stores_original_image [function]` (`8a91c013-ca46-5d32-9c14-d68c8a8146d7`) lines 245-276 [crates/gwiki/src/ingest/image.rs:245-276]
  - Signature: `fn stores_original_image() {`
  - Purpose: Indexed function `stores_original_image` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:245-276]
- `image_metadata_is_scope_indexed` (function) component `image_metadata_is_scope_indexed [function]` (`a8a57712-7e09-5f8f-9562-c010e91568cb`) lines 279-301 [crates/gwiki/src/ingest/image.rs:279-301]
  - Signature: `fn image_metadata_is_scope_indexed() {`
  - Purpose: Indexed function `image_metadata_is_scope_indexed` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:279-301]
- `production_vision_writes_description_and_ocr` (function) component `production_vision_writes_description_and_ocr [function]` (`7201c396-bf17-5dbd-93fc-aa835f8148f4`) lines 305-339 [crates/gwiki/src/ingest/image.rs:305-339]
  - Signature: `fn production_vision_writes_description_and_ocr() {`
  - Purpose: Indexed function `production_vision_writes_description_and_ocr` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:305-339]
- `test_ai_context` (function) component `test_ai_context [function]` (`5b31998d-7937-5382-81c7-c8b568069b13`) lines 342-374 [crates/gwiki/src/ingest/image.rs:342-374]
  - Signature: `fn test_ai_context(api_base: &str) -> gobby_core::ai_context::AiContext {`
  - Purpose: Indexed function `test_ai_context` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:342-374]
- `spawn_vision_server` (function) component `spawn_vision_server [function]` (`b7069cca-c2e5-5b57-bdbd-21d7df648cdb`) lines 377-379 [crates/gwiki/src/ingest/image.rs:377-379]
  - Signature: `fn spawn_vision_server(response: &'static str) -> (String, crate::test_http::RequestHandle) {`
  - Purpose: Indexed function `spawn_vision_server` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:377-379]

