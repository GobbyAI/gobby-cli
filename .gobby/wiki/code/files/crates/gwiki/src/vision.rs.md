---
title: crates/gwiki/src/vision.rs
type: code_file
provenance:
- file: crates/gwiki/src/vision.rs
  ranges:
  - 19-23
  - 26-29
  - 31-44
  - 47-52
  - 54-56
  - 59-66
  - 68-72
  - 75-78
  - 80-120
  - 122-234
  - 236-244
  - 246-263
  - 265-283
  - 285-309
  - 311-338
  - 340-359
  - 368-370
  - '372'
  - 374-383
  - 385-392
  - 394-410
  - 413-457
  - 460-488
  - 491-513
  - 516-558
  - 561-592
  - 595-648
  - 651-662
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/vision.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/vision.rs` exposes 31 indexed API symbols.
[crates/gwiki/src/vision.rs:19-23]
[crates/gwiki/src/vision.rs:26-29]
[crates/gwiki/src/vision.rs:31-44]
[crates/gwiki/src/vision.rs:32-43]
[crates/gwiki/src/vision.rs:47-52]

## API Symbols

- `VisionExtraction` (class) component `VisionExtraction [class]` (`22cadf56-b6b1-50ce-b558-dce67f342d4c`) lines 19-23 [crates/gwiki/src/vision.rs:19-23]
  - Signature: `pub struct VisionExtraction {`
  - Purpose: Indexed class `VisionExtraction` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:19-23]
- `VisionDegradation` (class) component `VisionDegradation [class]` (`ebc4963b-c395-5a64-9482-00e4933775e4`) lines 26-29 [crates/gwiki/src/vision.rs:26-29]
  - Signature: `pub struct VisionDegradation {`
  - Purpose: Indexed class `VisionDegradation` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:26-29]
- `VisionDegradation` (class) component `VisionDegradation [class]` (`fbc1675d-865d-5235-a4d9-06e53fc8508b`) lines 31-44 [crates/gwiki/src/vision.rs:31-44]
  - Signature: `impl VisionDegradation {`
  - Purpose: Indexed class `VisionDegradation` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:31-44]
- `VisionDegradation.for_routing` (method) component `VisionDegradation.for_routing [method]` (`d9596e5c-6ed9-5431-ac9c-80310c7e6740`) lines 32-43 [crates/gwiki/src/vision.rs:32-43]
  - Signature: `pub(crate) fn for_routing(routing: AiRouting, fallback: &str) -> Self {`
  - Purpose: Indexed method `VisionDegradation.for_routing` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:32-43]
- `disabled_degradation` (function) component `disabled_degradation [function]` (`e6f398ef-3fd8-5f75-9eb7-964e1518eb14`) lines 47-52 [crates/gwiki/src/vision.rs:47-52]
  - Signature: `pub(crate) fn disabled_degradation() -> VisionDegradation {`
  - Purpose: Indexed function `disabled_degradation` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:47-52]
- `VisionClient` (type) component `VisionClient [type]` (`41d30eec-0a2a-5cb9-98b4-a48342733271`) lines 54-56 [crates/gwiki/src/vision.rs:54-56]
  - Signature: `pub trait VisionClient {`
  - Purpose: Indexed type `VisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:54-56]
- `VisionRequest` (class) component `VisionRequest [class]` (`41db649c-349e-55a7-bb82-5fc3529ab87b`) lines 59-66 [crates/gwiki/src/vision.rs:59-66]
  - Signature: `pub struct VisionRequest<'a> {`
  - Purpose: Indexed class `VisionRequest` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:59-66]
- `VisionEndpoint` (type) component `VisionEndpoint [type]` (`56cef086-e855-5d1d-8731-33d9e8ab6f6b`) lines 68-72 [crates/gwiki/src/vision.rs:68-72]
  - Signature: `pub enum VisionEndpoint<'a> {`
  - Purpose: Indexed type `VisionEndpoint` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:68-72]
- `VisionMarkdownResult` (class) component `VisionMarkdownResult [class]` (`5ca7e511-534a-5ae6-91bb-8399a4c0e058`) lines 75-78 [crates/gwiki/src/vision.rs:75-78]
  - Signature: `pub struct VisionMarkdownResult {`
  - Purpose: Indexed class `VisionMarkdownResult` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:75-78]
- `write_image_derived_markdown` (function) component `write_image_derived_markdown [function]` (`edd4d80d-80b3-545c-9367-30a00704ae9d`) lines 80-120 [crates/gwiki/src/vision.rs:80-120]
  - Signature: `pub fn write_image_derived_markdown(`
  - Purpose: Indexed function `write_image_derived_markdown` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:80-120]
- `render_image_derived_markdown` (function) component `render_image_derived_markdown [function]` (`cb282ce4-57f7-595b-8741-5342b78b642e`) lines 122-234 [crates/gwiki/src/vision.rs:122-234]
  - Signature: `fn render_image_derived_markdown(`
  - Purpose: Indexed function `render_image_derived_markdown` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:122-234]
- `dedupe_vision_metadata` (function) component `dedupe_vision_metadata [function]` (`3bd34873-678a-5190-b700-d1b6d000ca48`) lines 236-244 [crates/gwiki/src/vision.rs:236-244]
  - Signature: `fn dedupe_vision_metadata(metadata: &[(String, String)]) -> Vec<(String, String)> {`
  - Purpose: Indexed function `dedupe_vision_metadata` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:236-244]
- `bounded_vision_metadata_key` (function) component `bounded_vision_metadata_key [function]` (`b834be7d-3776-5a09-b42e-fa7ae9b98b94`) lines 246-263 [crates/gwiki/src/vision.rs:246-263]
  - Signature: `fn bounded_vision_metadata_key(key: &str) -> String {`
  - Purpose: Indexed function `bounded_vision_metadata_key` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:246-263]
- `vision_metadata_key` (function) component `vision_metadata_key [function]` (`25b5f411-d1ed-53b8-bf5d-98d08c29c569`) lines 265-283 [crates/gwiki/src/vision.rs:265-283]
  - Signature: `fn vision_metadata_key(key: &str) -> String {`
  - Purpose: Indexed function `vision_metadata_key` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:265-283]
- `write_vision_markdown_atomically` (function) component `write_vision_markdown_atomically [function]` (`d3b0c9c1-1bd3-5a3d-8734-f9c437e8c161`) lines 285-309 [crates/gwiki/src/vision.rs:285-309]
  - Signature: `fn write_vision_markdown_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Indexed function `write_vision_markdown_atomically` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:285-309]
- `create_vision_temp_file` (function) component `create_vision_temp_file [function]` (`33943d7d-0b18-5d65-8d57-ef71526dff91`) lines 311-338 [crates/gwiki/src/vision.rs:311-338]
  - Signature: `fn create_vision_temp_file(path: &Path) -> Result<NamedTempFile, WikiError> {`
  - Purpose: Indexed function `create_vision_temp_file` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:311-338]
- `sync_parent_dir` (function) component `sync_parent_dir [function]` (`7ac6b79d-b2e6-5a01-aa62-16da40c92bf9`) lines 340-359 [crates/gwiki/src/vision.rs:340-359]
  - Signature: `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: Indexed function `sync_parent_dir` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:340-359]
- `FakeVisionClient` (class) component `FakeVisionClient [class]` (`8feee643-bf3a-571d-b58d-e71b54cc1594`) lines 368-370 [crates/gwiki/src/vision.rs:368-370]
  - Signature: `struct FakeVisionClient {`
  - Purpose: Indexed class `FakeVisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:368-370]
- `FailingVisionClient` (class) component `FailingVisionClient [class]` (`5c76284f-1744-59ed-be8e-6a6d3ca18674`) lines 372-372 [crates/gwiki/src/vision.rs:372]
  - Signature: `struct FailingVisionClient;`
  - Purpose: Indexed class `FailingVisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:372]
- `FakeVisionClient` (class) component `FakeVisionClient [class]` (`d4d37d23-0bd0-541d-a891-e2c4398c0ec6`) lines 374-383 [crates/gwiki/src/vision.rs:374-383]
  - Signature: `impl VisionClient for FakeVisionClient {`
  - Purpose: Indexed class `FakeVisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:374-383]
- `FakeVisionClient.extract` (method) component `FakeVisionClient.extract [method]` (`8516cf08-ea20-5345-b78b-0cbf5b0d21a5`) lines 375-382 [crates/gwiki/src/vision.rs:375-382]
  - Signature: `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: Indexed method `FakeVisionClient.extract` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:375-382]
- `FailingVisionClient` (class) component `FailingVisionClient [class]` (`eea13981-152d-5e52-ade4-babbcafe51a9`) lines 385-392 [crates/gwiki/src/vision.rs:385-392]
  - Signature: `impl VisionClient for FailingVisionClient {`
  - Purpose: Indexed class `FailingVisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:385-392]
- `FailingVisionClient.extract` (method) component `FailingVisionClient.extract [method]` (`9f2ca524-77d2-5ff7-9eb9-f92973fe8b48`) lines 386-391 [crates/gwiki/src/vision.rs:386-391]
  - Signature: `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: Indexed method `FailingVisionClient.extract` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:386-391]
- `record_for` (function) component `record_for [function]` (`73c6437e-a49c-5721-99d5-a7fd0aefbaf8`) lines 394-410 [crates/gwiki/src/vision.rs:394-410]
  - Signature: `fn record_for(temp: &Path) -> SourceRecord {`
  - Purpose: Indexed function `record_for` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:394-410]
- `vision_writes_derived_markdown` (function) component `vision_writes_derived_markdown [function]` (`d6e2298b-b1cb-5450-9a16-8151866165b0`) lines 413-457 [crates/gwiki/src/vision.rs:413-457]
  - Signature: `fn vision_writes_derived_markdown() {`
  - Purpose: Indexed function `vision_writes_derived_markdown` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:413-457]
- `vision_metadata_frontmatter_uses_sanitized_prefixed_keys` (function) component `vision_metadata_frontmatter_uses_sanitized_prefixed_keys [function]` (`9b9d0948-e2d9-5fcc-9441-58b13711ebf0`) lines 460-488 [crates/gwiki/src/vision.rs:460-488]
  - Signature: `fn vision_metadata_frontmatter_uses_sanitized_prefixed_keys() {`
  - Purpose: Indexed function `vision_metadata_frontmatter_uses_sanitized_prefixed_keys` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:460-488]
- `vision_metadata_bounds_entries_and_hashes_long_keys` (function) component `vision_metadata_bounds_entries_and_hashes_long_keys [function]` (`69e58e72-447e-5047-844e-7eb511250d66`) lines 491-513 [crates/gwiki/src/vision.rs:491-513]
  - Signature: `fn vision_metadata_bounds_entries_and_hashes_long_keys() {`
  - Purpose: Indexed function `vision_metadata_bounds_entries_and_hashes_long_keys` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:491-513]
- `missing_vision_degrades` (function) component `missing_vision_degrades [function]` (`fdd1355e-c8ad-5f4c-9df2-291a564e8f4b`) lines 516-558 [crates/gwiki/src/vision.rs:516-558]
  - Signature: `fn missing_vision_degrades() {`
  - Purpose: Indexed function `missing_vision_degrades` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:516-558]
- `vision_client_error_degrades` (function) component `vision_client_error_degrades [function]` (`53af2862-068d-5a94-a545-3f9dd864813f`) lines 561-592 [crates/gwiki/src/vision.rs:561-592]
  - Signature: `fn vision_client_error_degrades() {`
  - Purpose: Indexed function `vision_client_error_degrades` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:561-592]
- `vision_markdown_overwrites_atomically_without_temp_leftovers` (function) component `vision_markdown_overwrites_atomically_without_temp_leftovers [function]` (`806f27a4-a5aa-5413-a3cf-90108c4999ce`) lines 595-648 [crates/gwiki/src/vision.rs:595-648]
  - Signature: `fn vision_markdown_overwrites_atomically_without_temp_leftovers() {`
  - Purpose: Indexed function `vision_markdown_overwrites_atomically_without_temp_leftovers` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:595-648]
- `vision_temp_file_requires_parent_directory` (function) component `vision_temp_file_requires_parent_directory [function]` (`d67ece97-8986-5856-b5cd-0f256c226327`) lines 651-662 [crates/gwiki/src/vision.rs:651-662]
  - Signature: `fn vision_temp_file_requires_parent_directory() {`
  - Purpose: Indexed function `vision_temp_file_requires_parent_directory` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:651-662]

