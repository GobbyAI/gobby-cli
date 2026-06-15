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

This file implements image ingestion for gwiki. It defines `ImageSnapshot` as the in-memory input for a fetched image and `ImageIngestResult` as the output bundle with the source record, raw/asset/derived paths, and optional vision-degradation metadata. The ingest functions form a small pipeline: `ingest_image` performs ingestion with the default unavailable-vision fallback, `ingest_image_with_production_vision` and its `_without_index` variant route snapshots through production vision when available and otherwise degrade gracefully, and the non-indexed path writes the source manifest entry, raw image bytes, and markdown before optionally adding vision-derived content; the indexed wrappers then call `index_after_ingest`. Supporting helpers render the raw image markdown, supply the default degradation policy, and provide a conversion into the generic `IngestResult`. The tests verify the original bytes and metadata are preserved, scope indexing is correct, and production vision writes extracted description and OCR data.
[crates/gwiki/src/ingest/image.rs:23-31]
[crates/gwiki/src/ingest/image.rs:34-40]
[crates/gwiki/src/ingest/image.rs:43-56]
[crates/gwiki/src/ingest/image.rs:59-70]
[crates/gwiki/src/ingest/image.rs:72-103]

## API Symbols

- `ImageSnapshot` (class) component `ImageSnapshot [class]` (`49593152-39ab-5a75-8938-baa51af371ee`) lines 23-31 [crates/gwiki/src/ingest/image.rs:23-31]
  - Signature: `pub struct ImageSnapshot {`
  - Purpose: 'ImageSnapshot' is a serialized in-memory record of a fetched image, storing its source location, filename, fetch timestamp, raw bytes, optional MIME type, and optional pixel dimensions. [crates/gwiki/src/ingest/image.rs:23-31]
- `ImageIngestResult` (class) component `ImageIngestResult [class]` (`d430a5ba-d38e-5621-98e1-f3c88139c74a`) lines 34-40 [crates/gwiki/src/ingest/image.rs:34-40]
  - Signature: `pub struct ImageIngestResult {`
  - Purpose: 'ImageIngestResult' is a container for the outputs of an image ingestion step, bundling the generated 'SourceRecord' with the raw, asset, and derived file paths plus an optional 'VisionDegradation' classification. [crates/gwiki/src/ingest/image.rs:34-40]
- `ingest_image` (function) component `ingest_image [function]` (`ccee54f4-7a59-5c41-807c-84d9ea060a10`) lines 43-56 [crates/gwiki/src/ingest/image.rs:43-56]
  - Signature: `pub fn ingest_image(`
  - Purpose: 'ingest_image' is a thin wrapper that forwards the given vault root, index store, scope, and image snapshot to 'ingest_image_with_vision' using an unavailable vision endpoint configured with the default degradation policy. [crates/gwiki/src/ingest/image.rs:43-56]
- `ingest_image_with_production_vision` (function) component `ingest_image_with_production_vision [function]` (`75fb5927-0fdb-584c-9406-a731bf426c2f`) lines 59-70 [crates/gwiki/src/ingest/image.rs:59-70]
  - Signature: `pub fn ingest_image_with_production_vision(`
  - Purpose: Runs image ingestion via 'ingest_image_with_production_vision_without_index', then rebuilds the wiki index with 'index_after_ingest', returning the ingest result or propagating any 'WikiError'. [crates/gwiki/src/ingest/image.rs:59-70]
- `ingest_image_with_production_vision_without_index` (function) component `ingest_image_with_production_vision_without_index [function]` (`a9f9e868-fb7d-51eb-a304-712192b7363c`) lines 72-103 [crates/gwiki/src/ingest/image.rs:72-103]
  - Signature: `pub(crate) fn ingest_image_with_production_vision_without_index(`
  - Purpose: Routes an 'ImageSnapshot' through production vision extraction when the AI capability is available and routed via daemon/direct, otherwise degrades to an unavailable vision endpoint with a metadata-only fallback, then delegates to 'ingest_image_with_vision_without_index' to produce an 'ImageIngestResult'. [crates/gwiki/src/ingest/image.rs:72-103]
- `ingest_image_with_vision` (function) component `ingest_image_with_vision [function]` (`00589531-b7ac-54da-a6ca-02d9c8ea1804`) lines 106-116 [crates/gwiki/src/ingest/image.rs:106-116]
  - Signature: `pub fn ingest_image_with_vision(`
  - Purpose: Ingests an image via the vision pipeline without indexing, then updates the wiki index and returns the resulting 'ImageIngestResult' or propagates 'WikiError'. [crates/gwiki/src/ingest/image.rs:106-116]
- `ingest_image_with_vision_without_index` (function) component `ingest_image_with_vision_without_index [function]` (`f6fff319-9e6b-5d72-9655-068135e8ea16`) lines 118-167 [crates/gwiki/src/ingest/image.rs:118-167]
  - Signature: `pub(crate) fn ingest_image_with_vision_without_index(`
  - Purpose: Ingests an image snapshot without index lookup by registering a source manifest entry, writing the binary asset and raw markdown, generating vision-derived markdown via the provided endpoint, and returning the resulting record and output paths with any vision degradation metadata. [crates/gwiki/src/ingest/image.rs:118-167]
- `IngestResult` (class) component `IngestResult [class]` (`2485c664-3ffc-50bb-8e20-10aae599721b`) lines 169-177 [crates/gwiki/src/ingest/image.rs:169-177]
  - Signature: `impl From<ImageIngestResult> for IngestResult {`
  - Purpose: 'IngestResult' is a conversion target that builds an ingest result from 'ImageIngestResult' by copying 'record' and 'raw_path' and wrapping 'asset_path' in 'Some(...)'. [crates/gwiki/src/ingest/image.rs:169-177]
- `IngestResult.from` (method) component `IngestResult.from [method]` (`e4c1ac75-e76a-5527-922d-c10103e12894`) lines 170-176 [crates/gwiki/src/ingest/image.rs:170-176]
  - Signature: `fn from(result: ImageIngestResult) -> Self {`
  - Purpose: Converts an 'ImageIngestResult' into 'Self' by transferring 'record' and 'raw_path' unchanged and wrapping 'asset_path' in 'Some(...)'. [crates/gwiki/src/ingest/image.rs:170-176]
- `render_raw_image_markdown` (function) component `render_raw_image_markdown [function]` (`7eaf2504-b8f9-5858-a25f-d8894e98503d`) lines 179-210 [crates/gwiki/src/ingest/image.rs:179-210]
  - Signature: `fn render_raw_image_markdown(`
  - Purpose: Builds a Markdown document for an image snapshot by emitting metadata fields for source, hash, asset path, optional MIME type and dimensions, then appending a title and a note pointing to the stored image path. [crates/gwiki/src/ingest/image.rs:179-210]
- `default_vision_degradation` (function) component `default_vision_degradation [function]` (`56ed51ef-b574-5871-a83d-fae0d7de936c`) lines 213-218 [crates/gwiki/src/ingest/image.rs:213-218]
  - Signature: `fn default_vision_degradation() -> VisionDegradation {`
  - Purpose: Returns a 'VisionDegradation' configured for 'AiRouting::Auto' with the policy to keep raw image assets, expose only filename/metadata, and skip visual extraction. [crates/gwiki/src/ingest/image.rs:213-218]
- `sample_snapshot` (function) component `sample_snapshot [function]` (`4a938bf9-d313-56a9-8de9-3df0a6d4cf0d`) lines 228-238 [crates/gwiki/src/ingest/image.rs:228-238]
  - Signature: `fn sample_snapshot() -> ImageSnapshot {`
  - Purpose: Returns a sample 'ImageSnapshot' for '/tmp/diagram.png' with PNG bytes, MIME type 'image/png', filename 'diagram.png', fetched timestamp '2026-05-29T20:30:00Z', and dimensions '640x480'. [crates/gwiki/src/ingest/image.rs:228-238]
- `stores_original_image` (function) component `stores_original_image [function]` (`6b77f398-c0e7-52da-a670-2558a7f4fce3`) lines 241-272 [crates/gwiki/src/ingest/image.rs:241-272]
  - Signature: `fn stores_original_image() {`
  - Purpose: Verifies that 'ingest_image' writes the original image bytes under 'raw/assets/', records image source metadata in the generated markdown, and adds a single 'SourceKind::Image' manifest entry with the expected content hash. [crates/gwiki/src/ingest/image.rs:241-272]
- `image_metadata_is_scope_indexed` (function) component `image_metadata_is_scope_indexed [function]` (`5ffa300e-c791-5051-b6b4-348fd0e1ab65`) lines 275-297 [crates/gwiki/src/ingest/image.rs:275-297]
  - Signature: `fn image_metadata_is_scope_indexed() {`
  - Purpose: Verifies that 'ingest_image' indexes a derived 'SourceNote' document for a project-scoped image with the expected scope metadata, dimensions, and source entry recorded in 'MemoryWikiStore'. [crates/gwiki/src/ingest/image.rs:275-297]
- `production_vision_writes_description_and_ocr` (function) component `production_vision_writes_description_and_ocr [function]` (`51ba5929-c913-5501-ba14-5cb6c13f7556`) lines 301-335 [crates/gwiki/src/ingest/image.rs:301-335]
  - Signature: `fn production_vision_writes_description_and_ocr() {`
  - Purpose: Tests that 'ingest_image_with_production_vision' sends a base64 PNG to '/v1/chat/completions', returns no vision degradation, and indexes a derived document containing the extracted description, OCR text, and 'vision_model: gpt-4.1-mini'. [crates/gwiki/src/ingest/image.rs:301-335]
- `test_ai_context` (function) component `test_ai_context [function]` (`bcaeb7c7-04cc-526c-9ca8-518e741a562e`) lines 338-370 [crates/gwiki/src/ingest/image.rs:338-370]
  - Signature: `fn test_ai_context(api_base: &str) -> gobby_core::ai_context::AiContext {`
  - Purpose: Constructs a test 'AiContext' configured with a direct routing 'CapabilityBinding' for all AI capabilities pointing at the provided 'api_base', using model 'gpt-4.1-mini', single-concurrency tuning, and a limiter capacity of 1. [crates/gwiki/src/ingest/image.rs:338-370]
- `spawn_vision_server` (function) component `spawn_vision_server [function]` (`88b38b87-9a88-5a32-82af-7819f05bcd6a`) lines 373-375 [crates/gwiki/src/ingest/image.rs:373-375]
  - Signature: `fn spawn_vision_server(response: &'static str) -> (String, crate::test_http::RequestHandle) {`
  - Purpose: Spawns a test HTTP server that serves the provided static JSON response string and returns the server URL plus a 'RequestHandle'. [crates/gwiki/src/ingest/image.rs:373-375]

