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
  - 170-176
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/image.rs:23-31](crates/gwiki/src/ingest/image.rs#L23-L31), [crates/gwiki/src/ingest/image.rs:34-40](crates/gwiki/src/ingest/image.rs#L34-L40), [crates/gwiki/src/ingest/image.rs:43-56](crates/gwiki/src/ingest/image.rs#L43-L56), [crates/gwiki/src/ingest/image.rs:59-70](crates/gwiki/src/ingest/image.rs#L59-L70), [crates/gwiki/src/ingest/image.rs:72-103](crates/gwiki/src/ingest/image.rs#L72-L103), [crates/gwiki/src/ingest/image.rs:106-116](crates/gwiki/src/ingest/image.rs#L106-L116), [crates/gwiki/src/ingest/image.rs:118-167](crates/gwiki/src/ingest/image.rs#L118-L167), [crates/gwiki/src/ingest/image.rs:170-176](crates/gwiki/src/ingest/image.rs#L170-L176), [crates/gwiki/src/ingest/image.rs:179-210](crates/gwiki/src/ingest/image.rs#L179-L210), [crates/gwiki/src/ingest/image.rs:213-218](crates/gwiki/src/ingest/image.rs#L213-L218), [crates/gwiki/src/ingest/image.rs:228-238](crates/gwiki/src/ingest/image.rs#L228-L238), [crates/gwiki/src/ingest/image.rs:241-272](crates/gwiki/src/ingest/image.rs#L241-L272), [crates/gwiki/src/ingest/image.rs:275-297](crates/gwiki/src/ingest/image.rs#L275-L297), [crates/gwiki/src/ingest/image.rs:301-335](crates/gwiki/src/ingest/image.rs#L301-L335), [crates/gwiki/src/ingest/image.rs:338-370](crates/gwiki/src/ingest/image.rs#L338-L370), [crates/gwiki/src/ingest/image.rs:373-375](crates/gwiki/src/ingest/image.rs#L373-L375)

</details>

# crates/gwiki/src/ingest/image.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the image-ingestion pipeline for gwiki. `ImageSnapshot` carries the fetched image data and metadata, while `ImageIngestResult` records the generated source record plus the raw, asset, and derived markdown paths and any vision degradation used. The public entry points route ingestion either through local/default vision or production vision, with the production path optionally indexing after ingest. The internal helpers split the work into vision-enabled and no-index variants, render raw image markdown, choose a default degradation, sample snapshots for tests, verify whether originals are stored and metadata is scope-indexed, and confirm production vision writes description/OCR content. The file also includes test utilities for AI context and a vision server stub.
[crates/gwiki/src/ingest/image.rs:23-31]
[crates/gwiki/src/ingest/image.rs:34-40]
[crates/gwiki/src/ingest/image.rs:43-56]
[crates/gwiki/src/ingest/image.rs:59-70]
[crates/gwiki/src/ingest/image.rs:72-103]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ImageSnapshot` | class | `pub struct ImageSnapshot {` | `ImageSnapshot [class]` | `49593152-39ab-5a75-8938-baa51af371ee` | 23-31 [crates/gwiki/src/ingest/image.rs:23-31] | Indexed class `ImageSnapshot` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:23-31] |
| `ImageIngestResult` | class | `pub struct ImageIngestResult {` | `ImageIngestResult [class]` | `d430a5ba-d38e-5621-98e1-f3c88139c74a` | 34-40 [crates/gwiki/src/ingest/image.rs:34-40] | Indexed class `ImageIngestResult` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:34-40] |
| `ingest_image` | function | `pub fn ingest_image(` | `ingest_image [function]` | `ccee54f4-7a59-5c41-807c-84d9ea060a10` | 43-56 [crates/gwiki/src/ingest/image.rs:43-56] | Indexed function `ingest_image` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:43-56] |
| `ingest_image_with_production_vision` | function | `pub fn ingest_image_with_production_vision(` | `ingest_image_with_production_vision [function]` | `75fb5927-0fdb-584c-9406-a731bf426c2f` | 59-70 [crates/gwiki/src/ingest/image.rs:59-70] | Indexed function `ingest_image_with_production_vision` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:59-70] |
| `ingest_image_with_production_vision_without_index` | function | `pub(crate) fn ingest_image_with_production_vision_without_index(` | `ingest_image_with_production_vision_without_index [function]` | `a9f9e868-fb7d-51eb-a304-712192b7363c` | 72-103 [crates/gwiki/src/ingest/image.rs:72-103] | Indexed function `ingest_image_with_production_vision_without_index` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:72-103] |
| `ingest_image_with_vision` | function | `pub fn ingest_image_with_vision(` | `ingest_image_with_vision [function]` | `00589531-b7ac-54da-a6ca-02d9c8ea1804` | 106-116 [crates/gwiki/src/ingest/image.rs:106-116] | Indexed function `ingest_image_with_vision` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:106-116] |
| `ingest_image_with_vision_without_index` | function | `pub(crate) fn ingest_image_with_vision_without_index(` | `ingest_image_with_vision_without_index [function]` | `f6fff319-9e6b-5d72-9655-068135e8ea16` | 118-167 [crates/gwiki/src/ingest/image.rs:118-167] | Indexed function `ingest_image_with_vision_without_index` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:118-167] |
| `IngestResult::from` | method | `fn from(result: ImageIngestResult) -> Self {` | `IngestResult::from [method]` | `e4c1ac75-e76a-5527-922d-c10103e12894` | 170-176 [crates/gwiki/src/ingest/image.rs:170-176] | Indexed method `IngestResult::from` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:170-176] |
| `render_raw_image_markdown` | function | `fn render_raw_image_markdown(` | `render_raw_image_markdown [function]` | `7eaf2504-b8f9-5858-a25f-d8894e98503d` | 179-210 [crates/gwiki/src/ingest/image.rs:179-210] | Indexed function `render_raw_image_markdown` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:179-210] |
| `default_vision_degradation` | function | `fn default_vision_degradation() -> VisionDegradation {` | `default_vision_degradation [function]` | `56ed51ef-b574-5871-a83d-fae0d7de936c` | 213-218 [crates/gwiki/src/ingest/image.rs:213-218] | Indexed function `default_vision_degradation` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:213-218] |
| `sample_snapshot` | function | `fn sample_snapshot() -> ImageSnapshot {` | `sample_snapshot [function]` | `4a938bf9-d313-56a9-8de9-3df0a6d4cf0d` | 228-238 [crates/gwiki/src/ingest/image.rs:228-238] | Indexed function `sample_snapshot` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:228-238] |
| `stores_original_image` | function | `fn stores_original_image() {` | `stores_original_image [function]` | `6b77f398-c0e7-52da-a670-2558a7f4fce3` | 241-272 [crates/gwiki/src/ingest/image.rs:241-272] | Indexed function `stores_original_image` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:241-272] |
| `image_metadata_is_scope_indexed` | function | `fn image_metadata_is_scope_indexed() {` | `image_metadata_is_scope_indexed [function]` | `5ffa300e-c791-5051-b6b4-348fd0e1ab65` | 275-297 [crates/gwiki/src/ingest/image.rs:275-297] | Indexed function `image_metadata_is_scope_indexed` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:275-297] |
| `production_vision_writes_description_and_ocr` | function | `fn production_vision_writes_description_and_ocr() {` | `production_vision_writes_description_and_ocr [function]` | `51ba5929-c913-5501-ba14-5cb6c13f7556` | 301-335 [crates/gwiki/src/ingest/image.rs:301-335] | Indexed function `production_vision_writes_description_and_ocr` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:301-335] |
| `test_ai_context` | function | `fn test_ai_context(api_base: &str) -> gobby_core::ai_context::AiContext {` | `test_ai_context [function]` | `bcaeb7c7-04cc-526c-9ca8-518e741a562e` | 338-370 [crates/gwiki/src/ingest/image.rs:338-370] | Indexed function `test_ai_context` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:338-370] |
| `spawn_vision_server` | function | `fn spawn_vision_server(response: &'static str) -> (String, crate::test_http::RequestHandle) {` | `spawn_vision_server [function]` | `88b38b87-9a88-5a32-82af-7819f05bcd6a` | 373-375 [crates/gwiki/src/ingest/image.rs:373-375] | Indexed function `spawn_vision_server` in `crates/gwiki/src/ingest/image.rs`. [crates/gwiki/src/ingest/image.rs:373-375] |
