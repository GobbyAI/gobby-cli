---
title: crates/gwiki/src/vision.rs
type: code_file
provenance:
- file: crates/gwiki/src/vision.rs
  ranges:
  - 17-21
  - 24-27
  - 29-34
  - 36-38
  - 41-48
  - 50-53
  - 56-59
  - 61-101
  - 103-212
  - 214-222
  - 224-241
  - 243-261
  - 263-287
  - 289-316
  - 318-337
  - 346-348
  - '350'
  - 352-361
  - 353-360
  - 363-370
  - 364-369
  - 372-388
  - 391-435
  - 438-466
  - 469-491
  - 494-533
  - 536-567
  - 570-623
  - 626-637
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/vision.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/vision.rs` exposes 29 indexed API symbols.
[crates/gwiki/src/vision.rs:17-21]
[crates/gwiki/src/vision.rs:24-27]
[crates/gwiki/src/vision.rs:29-34]
[crates/gwiki/src/vision.rs:36-38]
[crates/gwiki/src/vision.rs:41-48]
[crates/gwiki/src/vision.rs:50-53]
[crates/gwiki/src/vision.rs:56-59]
[crates/gwiki/src/vision.rs:61-101]
[crates/gwiki/src/vision.rs:103-212]
[crates/gwiki/src/vision.rs:214-222]
[crates/gwiki/src/vision.rs:224-241]
[crates/gwiki/src/vision.rs:243-261]
[crates/gwiki/src/vision.rs:263-287]
[crates/gwiki/src/vision.rs:289-316]
[crates/gwiki/src/vision.rs:318-337]
[crates/gwiki/src/vision.rs:346-348]
[crates/gwiki/src/vision.rs:350]
[crates/gwiki/src/vision.rs:352-361]
[crates/gwiki/src/vision.rs:353-360]
[crates/gwiki/src/vision.rs:363-370]
[crates/gwiki/src/vision.rs:364-369]
[crates/gwiki/src/vision.rs:372-388]
[crates/gwiki/src/vision.rs:391-435]
[crates/gwiki/src/vision.rs:438-466]
[crates/gwiki/src/vision.rs:469-491]
[crates/gwiki/src/vision.rs:494-533]
[crates/gwiki/src/vision.rs:536-567]
[crates/gwiki/src/vision.rs:570-623]
[crates/gwiki/src/vision.rs:626-637]

## API Symbols

- `VisionExtraction` (class) component `VisionExtraction [class]` (`a11e4e43-4470-59f8-8f79-1ea3ce63fe91`) lines 17-21 [crates/gwiki/src/vision.rs:17-21]
  - Signature: `pub struct VisionExtraction {`
  - Purpose: Indexed class `VisionExtraction` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:17-21]
- `VisionDegradation` (class) component `VisionDegradation [class]` (`31245175-5dee-5b9d-a9ab-e92ad9165578`) lines 24-27 [crates/gwiki/src/vision.rs:24-27]
  - Signature: `pub struct VisionDegradation {`
  - Purpose: Indexed class `VisionDegradation` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:24-27]
- `disabled_degradation` (function) component `disabled_degradation [function]` (`50eb9b59-f16e-5166-b6f9-baf596eabdc4`) lines 29-34 [crates/gwiki/src/vision.rs:29-34]
  - Signature: `pub(crate) fn disabled_degradation() -> VisionDegradation {`
  - Purpose: Indexed function `disabled_degradation` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:29-34]
- `VisionClient` (type) component `VisionClient [type]` (`f418aa63-3648-5d8c-b6f3-e7a7eb71b2a1`) lines 36-38 [crates/gwiki/src/vision.rs:36-38]
  - Signature: `pub trait VisionClient {`
  - Purpose: Indexed type `VisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:36-38]
- `VisionRequest` (class) component `VisionRequest [class]` (`4f86be69-1680-5190-bd88-408a73dbacc0`) lines 41-48 [crates/gwiki/src/vision.rs:41-48]
  - Signature: `pub struct VisionRequest<'a> {`
  - Purpose: Indexed class `VisionRequest` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:41-48]
- `VisionEndpoint` (type) component `VisionEndpoint [type]` (`ce37d58d-0499-5ca5-9cf7-20efcfbe7c1e`) lines 50-53 [crates/gwiki/src/vision.rs:50-53]
  - Signature: `pub enum VisionEndpoint<'a> {`
  - Purpose: Indexed type `VisionEndpoint` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:50-53]
- `VisionMarkdownResult` (class) component `VisionMarkdownResult [class]` (`8c063f84-cb44-58d3-bf2b-a4674d1883b3`) lines 56-59 [crates/gwiki/src/vision.rs:56-59]
  - Signature: `pub struct VisionMarkdownResult {`
  - Purpose: Indexed class `VisionMarkdownResult` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:56-59]
- `write_image_derived_markdown` (function) component `write_image_derived_markdown [function]` (`14dd460e-97b8-5363-ab38-1a271fb661e4`) lines 61-101 [crates/gwiki/src/vision.rs:61-101]
  - Signature: `pub fn write_image_derived_markdown(`
  - Purpose: Indexed function `write_image_derived_markdown` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:61-101]
- `render_image_derived_markdown` (function) component `render_image_derived_markdown [function]` (`f3c78a61-f4a2-597c-9091-81a7676f0e16`) lines 103-212 [crates/gwiki/src/vision.rs:103-212]
  - Signature: `fn render_image_derived_markdown(`
  - Purpose: Indexed function `render_image_derived_markdown` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:103-212]
- `dedupe_vision_metadata` (function) component `dedupe_vision_metadata [function]` (`623f23b5-55aa-59d2-8d2b-964982fde79d`) lines 214-222 [crates/gwiki/src/vision.rs:214-222]
  - Signature: `fn dedupe_vision_metadata(metadata: &[(String, String)]) -> Vec<(String, String)> {`
  - Purpose: Indexed function `dedupe_vision_metadata` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:214-222]
- `bounded_vision_metadata_key` (function) component `bounded_vision_metadata_key [function]` (`17f7cbf5-339a-5c42-aa8e-099dfca3b2cb`) lines 224-241 [crates/gwiki/src/vision.rs:224-241]
  - Signature: `fn bounded_vision_metadata_key(key: &str) -> String {`
  - Purpose: Indexed function `bounded_vision_metadata_key` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:224-241]
- `vision_metadata_key` (function) component `vision_metadata_key [function]` (`7aa51ce7-c980-5ca0-8578-3fa992633435`) lines 243-261 [crates/gwiki/src/vision.rs:243-261]
  - Signature: `fn vision_metadata_key(key: &str) -> String {`
  - Purpose: Indexed function `vision_metadata_key` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:243-261]
- `write_vision_markdown_atomically` (function) component `write_vision_markdown_atomically [function]` (`8d8baa6d-6cf9-536f-bfd2-84c1f55d3942`) lines 263-287 [crates/gwiki/src/vision.rs:263-287]
  - Signature: `fn write_vision_markdown_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Indexed function `write_vision_markdown_atomically` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:263-287]
- `create_vision_temp_file` (function) component `create_vision_temp_file [function]` (`b958624e-a615-5f37-8df8-252275b89d89`) lines 289-316 [crates/gwiki/src/vision.rs:289-316]
  - Signature: `fn create_vision_temp_file(path: &Path) -> Result<NamedTempFile, WikiError> {`
  - Purpose: Indexed function `create_vision_temp_file` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:289-316]
- `sync_parent_dir` (function) component `sync_parent_dir [function]` (`37502ed2-e92d-5c56-8ab7-b41a74f32777`) lines 318-337 [crates/gwiki/src/vision.rs:318-337]
  - Signature: `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: Indexed function `sync_parent_dir` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:318-337]
- `FakeVisionClient` (class) component `FakeVisionClient [class]` (`5ab3ab3a-626a-5f72-b998-8e1e5918b3be`) lines 346-348 [crates/gwiki/src/vision.rs:346-348]
  - Signature: `struct FakeVisionClient {`
  - Purpose: Indexed class `FakeVisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:346-348]
- `FailingVisionClient` (class) component `FailingVisionClient [class]` (`4539b278-ba65-561d-8ce5-98fc0cab49ad`) lines 350-350 [crates/gwiki/src/vision.rs:350]
  - Signature: `struct FailingVisionClient;`
  - Purpose: Indexed class `FailingVisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:350]
- `FakeVisionClient` (class) component `FakeVisionClient [class]` (`a1a14553-cdd3-594f-a65c-6738fc89b684`) lines 352-361 [crates/gwiki/src/vision.rs:352-361]
  - Signature: `impl VisionClient for FakeVisionClient {`
  - Purpose: Indexed class `FakeVisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:352-361]
- `FakeVisionClient.extract` (method) component `FakeVisionClient.extract [method]` (`e83b825c-e353-5ad3-8791-7f3c9eb8d1e8`) lines 353-360 [crates/gwiki/src/vision.rs:353-360]
  - Signature: `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: Indexed method `FakeVisionClient.extract` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:353-360]
- `FailingVisionClient` (class) component `FailingVisionClient [class]` (`d429e51d-09af-564c-b173-aae29fb3f58d`) lines 363-370 [crates/gwiki/src/vision.rs:363-370]
  - Signature: `impl VisionClient for FailingVisionClient {`
  - Purpose: Indexed class `FailingVisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:363-370]
- `FailingVisionClient.extract` (method) component `FailingVisionClient.extract [method]` (`c85dc217-fc85-5a1d-b2c8-79e14ed910a1`) lines 364-369 [crates/gwiki/src/vision.rs:364-369]
  - Signature: `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: Indexed method `FailingVisionClient.extract` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:364-369]
- `record_for` (function) component `record_for [function]` (`63edc6da-bf86-595d-920d-dceefa42de04`) lines 372-388 [crates/gwiki/src/vision.rs:372-388]
  - Signature: `fn record_for(temp: &Path) -> SourceRecord {`
  - Purpose: Indexed function `record_for` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:372-388]
- `vision_writes_derived_markdown` (function) component `vision_writes_derived_markdown [function]` (`7c7074e6-bcda-5820-9ed8-1f4a31ba6cc4`) lines 391-435 [crates/gwiki/src/vision.rs:391-435]
  - Signature: `fn vision_writes_derived_markdown() {`
  - Purpose: Indexed function `vision_writes_derived_markdown` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:391-435]
- `vision_metadata_frontmatter_uses_sanitized_prefixed_keys` (function) component `vision_metadata_frontmatter_uses_sanitized_prefixed_keys [function]` (`266db8e1-18c9-5ccc-a435-90d4d0b26f30`) lines 438-466 [crates/gwiki/src/vision.rs:438-466]
  - Signature: `fn vision_metadata_frontmatter_uses_sanitized_prefixed_keys() {`
  - Purpose: Indexed function `vision_metadata_frontmatter_uses_sanitized_prefixed_keys` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:438-466]
- `vision_metadata_bounds_entries_and_hashes_long_keys` (function) component `vision_metadata_bounds_entries_and_hashes_long_keys [function]` (`00e7e4c1-4ea8-5810-b6c0-11b3efadd566`) lines 469-491 [crates/gwiki/src/vision.rs:469-491]
  - Signature: `fn vision_metadata_bounds_entries_and_hashes_long_keys() {`
  - Purpose: Indexed function `vision_metadata_bounds_entries_and_hashes_long_keys` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:469-491]
- `missing_vision_degrades` (function) component `missing_vision_degrades [function]` (`ca4a3312-57a7-5c9f-a8f3-538d7af36b51`) lines 494-533 [crates/gwiki/src/vision.rs:494-533]
  - Signature: `fn missing_vision_degrades() {`
  - Purpose: Indexed function `missing_vision_degrades` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:494-533]
- `vision_client_error_degrades` (function) component `vision_client_error_degrades [function]` (`35cff95b-d1fb-5745-9523-ee5557811fbb`) lines 536-567 [crates/gwiki/src/vision.rs:536-567]
  - Signature: `fn vision_client_error_degrades() {`
  - Purpose: Indexed function `vision_client_error_degrades` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:536-567]
- `vision_markdown_overwrites_atomically_without_temp_leftovers` (function) component `vision_markdown_overwrites_atomically_without_temp_leftovers [function]` (`d414c110-9001-5395-8316-09f2f167ce8b`) lines 570-623 [crates/gwiki/src/vision.rs:570-623]
  - Signature: `fn vision_markdown_overwrites_atomically_without_temp_leftovers() {`
  - Purpose: Indexed function `vision_markdown_overwrites_atomically_without_temp_leftovers` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:570-623]
- `vision_temp_file_requires_parent_directory` (function) component `vision_temp_file_requires_parent_directory [function]` (`b440e89d-c210-5932-b69f-883234b13bca`) lines 626-637 [crates/gwiki/src/vision.rs:626-637]
  - Signature: `fn vision_temp_file_requires_parent_directory() {`
  - Purpose: Indexed function `vision_temp_file_requires_parent_directory` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:626-637]

