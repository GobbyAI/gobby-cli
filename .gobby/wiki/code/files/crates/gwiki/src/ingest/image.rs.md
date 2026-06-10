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
  - 342-373
  - 376-378
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
[crates/gwiki/src/ingest/image.rs:98-108]
[crates/gwiki/src/ingest/image.rs:110-159]
[crates/gwiki/src/ingest/image.rs:161-169]
[crates/gwiki/src/ingest/image.rs:162-168]
[crates/gwiki/src/ingest/image.rs:171-202]
[crates/gwiki/src/ingest/image.rs:204-211]
[crates/gwiki/src/ingest/image.rs:213-222]
[crates/gwiki/src/ingest/image.rs:232-242]
[crates/gwiki/src/ingest/image.rs:245-276]
[crates/gwiki/src/ingest/image.rs:279-301]
[crates/gwiki/src/ingest/image.rs:305-339]
[crates/gwiki/src/ingest/image.rs:342-373]
[crates/gwiki/src/ingest/image.rs:376-378]

## API Symbols

- `ImageSnapshot` (class) component `ImageSnapshot [class]` (`49593152-39ab-5a75-8938-baa51af371ee`) lines 23-31 [crates/gwiki/src/ingest/image.rs:23-31]
  - Signature: `pub struct ImageSnapshot {`
  - Purpose: `ImageSnapshot` is a struct that encapsulates image binary data with metadata fields for source location, filename, fetch timestamp, optional MIME type, and optional dimensions (width/height). [crates/gwiki/src/ingest/image.rs:23-31]
- `ImageIngestResult` (class) component `ImageIngestResult [class]` (`d430a5ba-d38e-5621-98e1-f3c88139c74a`) lines 34-40 [crates/gwiki/src/ingest/image.rs:34-40]
  - Signature: `pub struct ImageIngestResult {`
  - Purpose: `ImageIngestResult` is a struct that encapsulates the output of image ingestion, containing source metadata, file paths for raw/asset/derived processing stages, and optional vision degradation metrics. [crates/gwiki/src/ingest/image.rs:34-40]
- `ingest_image` (function) component `ingest_image [function]` (`10bcabbd-5cb6-5f69-ad24-f183453e576e`) lines 42-55 [crates/gwiki/src/ingest/image.rs:42-55]
  - Signature: `pub fn ingest_image(`
  - Purpose: Ingests an image snapshot into a wiki index store by delegating to `ingest_image_with_vision` with the vision endpoint disabled. [crates/gwiki/src/ingest/image.rs:42-55]
- `ingest_image_with_production_vision` (function) component `ingest_image_with_production_vision [function]` (`82791c28-45b7-52da-ae75-b07532d649ec`) lines 57-68 [crates/gwiki/src/ingest/image.rs:57-68]
  - Signature: `pub fn ingest_image_with_production_vision(`
  - Purpose: Ingests an image snapshot using production vision AI and reindexes the wiki vault store. [crates/gwiki/src/ingest/image.rs:57-68]
- `ingest_image_with_production_vision_without_index` (function) component `ingest_image_with_production_vision_without_index [function]` (`4a6a3f49-e478-55b6-8ab9-67a5ab53a604`) lines 70-96 [crates/gwiki/src/ingest/image.rs:70-96]
  - Signature: `pub(crate) fn ingest_image_with_production_vision_without_index(`
  - Purpose: Routes image ingestion through either an available ProductionVisionClient or a degraded endpoint based on AI capability routing configuration, delegating the actual ingestion to `ingest_image_with_vision_without_index`. [crates/gwiki/src/ingest/image.rs:70-96]
- `ingest_image_with_vision` (function) component `ingest_image_with_vision [function]` (`b4e54fcc-008d-5ccc-8b67-52fc0b794c7b`) lines 98-108 [crates/gwiki/src/ingest/image.rs:98-108]
  - Signature: `pub fn ingest_image_with_vision(`
  - Purpose: Ingests an image using a vision endpoint within a given scope, then re-indexes the wiki store to reflect the changes. [crates/gwiki/src/ingest/image.rs:98-108]
- `ingest_image_with_vision_without_index` (function) component `ingest_image_with_vision_without_index [function]` (`f4eae93a-04b2-57fa-bc21-8c184365577d`) lines 110-159 [crates/gwiki/src/ingest/image.rs:110-159]
  - Signature: `pub(crate) fn ingest_image_with_vision_without_index(`
  - Purpose: Ingests an image into a vault by registering it as a source, persisting its asset and raw markdown representation, generating enriched markdown via vision API processing, and returning the complete ingestion result with artifact paths and metadata. [crates/gwiki/src/ingest/image.rs:110-159]
- `IngestResult` (class) component `IngestResult [class]` (`2d3e124f-79e7-586c-acb0-e73369e26c2a`) lines 161-169 [crates/gwiki/src/ingest/image.rs:161-169]
  - Signature: `impl From<ImageIngestResult> for IngestResult {`
  - Purpose: This implementation enables automatic conversion from `ImageIngestResult` to `IngestResult` by forwarding the `record` and `raw_path` fields directly while wrapping the `asset_path` in `Some`. [crates/gwiki/src/ingest/image.rs:161-169]
- `IngestResult.from` (method) component `IngestResult.from [method]` (`5627cf5a-2f55-579a-8406-b3052ddc4422`) lines 162-168 [crates/gwiki/src/ingest/image.rs:162-168]
  - Signature: `fn from(result: ImageIngestResult) -> Self {`
  - Purpose: Converts an `ImageIngestResult` into `Self` by transferring the `record` and `raw_path` fields and wrapping the `asset_path` in a `Some()` option variant. [crates/gwiki/src/ingest/image.rs:162-168]
- `render_raw_image_markdown` (function) component `render_raw_image_markdown [function]` (`b283c3a7-2cd3-5b20-98dd-3c1f87a38818`) lines 171-202 [crates/gwiki/src/ingest/image.rs:171-202]
  - Signature: `fn render_raw_image_markdown(`
  - Purpose: Constructs and returns a markdown string containing image snapshot metadata (source location, hash, MIME type, dimensions) and a reference to the asset storage path. [crates/gwiki/src/ingest/image.rs:171-202]
- `default_vision_degradation` (function) component `default_vision_degradation [function]` (`e9cfc571-314e-5dd5-b7cd-1ba2e76dcb9f`) lines 204-211 [crates/gwiki/src/ingest/image.rs:204-211]
  - Signature: `fn default_vision_degradation() -> VisionDegradation {`
  - Purpose: Returns a `VisionDegradation` struct configured with a "missing_endpoint" reason and a fallback strategy to preserve raw image assets and metadata while skipping visual extraction. [crates/gwiki/src/ingest/image.rs:204-211]
- `vision_degradation` (function) component `vision_degradation [function]` (`e09e45b1-b518-5a8d-a0bc-9d61a8ddc0e5`) lines 213-222 [crates/gwiki/src/ingest/image.rs:213-222]
  - Signature: `fn vision_degradation(routing: AiRouting) -> VisionDegradation {`
  - Purpose: Maps an `AiRouting` configuration to a `VisionDegradation` response with a "disabled" or "missing_endpoint" reason and a fallback instruction to preserve raw image assets while surfacing only filename/metadata. [crates/gwiki/src/ingest/image.rs:213-222]
- `sample_snapshot` (function) component `sample_snapshot [function]` (`66cbcc5b-39f8-533e-953e-0d21d9dcc6eb`) lines 232-242 [crates/gwiki/src/ingest/image.rs:232-242]
  - Signature: `fn sample_snapshot() -> ImageSnapshot {`
  - Purpose: Returns a test `ImageSnapshot` struct initialized with hardcoded PNG image data (640×480 resolution) and metadata for a diagram located at `/tmp/diagram.png`. [crates/gwiki/src/ingest/image.rs:232-242]
- `stores_original_image` (function) component `stores_original_image [function]` (`8a91c013-ca46-5d32-9c14-d68c8a8146d7`) lines 245-276 [crates/gwiki/src/ingest/image.rs:245-276]
  - Signature: `fn stores_original_image() {`
  - Purpose: Tests that `ingest_image()` persists image bytes to the `raw/assets/` directory and creates corresponding metadata entries in both the markdown source file and SourceManifest with correct content hashing. [crates/gwiki/src/ingest/image.rs:245-276]
- `image_metadata_is_scope_indexed` (function) component `image_metadata_is_scope_indexed [function]` (`a8a57712-7e09-5f8f-9562-c010e91568cb`) lines 279-301 [crates/gwiki/src/ingest/image.rs:279-301]
  - Signature: `fn image_metadata_is_scope_indexed() {`
  - Purpose: Verifies that image ingestion indexes metadata including scope identity and image dimensions as a SourceNote document in the wiki store. [crates/gwiki/src/ingest/image.rs:279-301]
- `production_vision_writes_description_and_ocr` (function) component `production_vision_writes_description_and_ocr [function]` (`7201c396-bf17-5dbd-93fc-aa835f8148f4`) lines 305-339 [crates/gwiki/src/ingest/image.rs:305-339]
  - Signature: `fn production_vision_writes_description_and_ocr() {`
  - Purpose: Tests that `ingest_image_with_production_vision` correctly processes a mocked GPT-4.1-mini vision API response and indexes the resulting document with extracted image description and OCR text in a MemoryWikiStore. [crates/gwiki/src/ingest/image.rs:305-339]
- `test_ai_context` (function) component `test_ai_context [function]` (`5b31998d-7937-5382-81c7-c8b568069b13`) lines 342-373 [crates/gwiki/src/ingest/image.rs:342-373]
  - Signature: `fn test_ai_context(api_base: &str) -> gobby_core::ai_context::AiContext {`
  - Purpose: Initializes a test `AiContext` where all five AI capability bindings (embed, audio_transcribe, audio_translate, vision_extract, text_generate) are configured to route directly to a GPT-4.1-mini model at a given API endpoint with a concurrency limit of 1. [crates/gwiki/src/ingest/image.rs:342-373]
- `spawn_vision_server` (function) component `spawn_vision_server [function]` (`a00c1c29-09e3-5ee0-81d6-a916cde3f59c`) lines 376-378 [crates/gwiki/src/ingest/image.rs:376-378]
  - Signature: `fn spawn_vision_server(response: &'static str) -> (String, crate::test_http::RequestHandle) {`
  - Purpose: Spawns a test HTTP server that responds with the provided static JSON string and returns a tuple containing the server's address and a request handle for managing the server instance. [crates/gwiki/src/ingest/image.rs:376-378]

