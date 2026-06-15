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
  - 58-65
  - 67-69
  - 72-79
  - 81-85
  - 88-91
  - 93-140
  - 142-254
  - 256-264
  - 266-283
  - 285-303
  - 305-329
  - 331-358
  - 360-379
  - 388-390
  - '392'
  - 394-403
  - 405-412
  - '414'
  - 416-426
  - 428-444
  - 447-491
  - 494-522
  - 525-547
  - 550-592
  - 595-626
  - 629-659
  - 662-715
  - 718-729
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/vision.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the vision ingestion layer for image-derived wiki content. It models raw vision output with `VisionExtraction`, records fallback state with `VisionDegradation`, and exposes a `VisionClient` interface plus request/result types so callers can extract image text or degrade cleanly when vision is unavailable or empty. The core flow is `write_image_derived_markdown`, which runs extraction when possible, falls back to a degradation reason otherwise, renders markdown with front matter via `render_image_derived_markdown`, and writes it atomically with temp-file and directory-sync helpers. Supporting functions normalize and deduplicate vision metadata into safe front-matter keys, while the test clients and test cases exercise success, failure, empty-output handling, metadata sanitization, and atomic overwrite behavior.
[crates/gwiki/src/vision.rs:19-23]
[crates/gwiki/src/vision.rs:26-29]
[crates/gwiki/src/vision.rs:31-44]
[crates/gwiki/src/vision.rs:32-43]
[crates/gwiki/src/vision.rs:47-52]

## API Symbols

- `VisionExtraction` (class) component `VisionExtraction [class]` (`22cadf56-b6b1-50ce-b558-dce67f342d4c`) lines 19-23 [crates/gwiki/src/vision.rs:19-23]
  - Signature: `pub struct VisionExtraction {`
  - Purpose: 'VisionExtraction' is a data container holding a required 'description', optional 'ocr_text', and an arbitrary key-value 'metadata' vector for extracted vision results. [crates/gwiki/src/vision.rs:19-23]
- `VisionDegradation` (class) component `VisionDegradation [class]` (`ebc4963b-c395-5a64-9482-00e4933775e4`) lines 26-29 [crates/gwiki/src/vision.rs:26-29]
  - Signature: `pub struct VisionDegradation {`
  - Purpose: 'VisionDegradation' is a struct that captures a vision-modality degradation by recording the 'reason' as a 'ModalityDegradationReason' and the 'fallback' behavior as a 'String'. [crates/gwiki/src/vision.rs:26-29]
- `VisionDegradation` (class) component `VisionDegradation [class]` (`fbc1675d-865d-5235-a4d9-06e53fc8508b`) lines 31-44 [crates/gwiki/src/vision.rs:31-44]
  - Signature: `impl VisionDegradation {`
  - Purpose: 'VisionDegradation' constructs a degradation descriptor containing a 'ModalityDegradationReason' and fallback string, mapping 'AiRouting::Off' to 'Disabled' and all other routing modes to 'MissingEndpoint'. [crates/gwiki/src/vision.rs:31-44]
- `VisionDegradation.for_routing` (method) component `VisionDegradation.for_routing [method]` (`d9596e5c-6ed9-5431-ac9c-80310c7e6740`) lines 32-43 [crates/gwiki/src/vision.rs:32-43]
  - Signature: `pub(crate) fn for_routing(routing: AiRouting, fallback: &str) -> Self {`
  - Purpose: Constructs a 'Self' value by mapping 'AiRouting::Off' to 'ModalityDegradationReason::Disabled' and all other routing modes to 'ModalityDegradationReason::MissingEndpoint', while copying 'fallback' into the 'fallback' field as an owned 'String'. [crates/gwiki/src/vision.rs:32-43]
- `disabled_degradation` (function) component `disabled_degradation [function]` (`e6f398ef-3fd8-5f75-9eb7-964e1518eb14`) lines 47-52 [crates/gwiki/src/vision.rs:47-52]
  - Signature: `pub(crate) fn disabled_degradation() -> VisionDegradation {`
  - Purpose: Returns a 'VisionDegradation' value indicating the vision modality is disabled, with reason 'ModalityDegradationReason::Disabled' and the fallback message '"Keep PDF text layer only."' [crates/gwiki/src/vision.rs:47-52]
- `vision_extraction_is_empty` (function) component `vision_extraction_is_empty [function]` (`fdba1df0-f62a-55fc-b259-040389ab0604`) lines 58-65 [crates/gwiki/src/vision.rs:58-65]
  - Signature: `fn vision_extraction_is_empty(extraction: &VisionExtraction) -> bool {`
  - Purpose: Returns 'true' only when 'VisionExtraction.description' is blank after trimming and 'ocr_text' is either absent or blank after trimming, otherwise 'false'. [crates/gwiki/src/vision.rs:58-65]
- `VisionClient` (type) component `VisionClient [type]` (`892cb9e1-fbcf-5e5c-8c11-2834b89a2303`) lines 67-69 [crates/gwiki/src/vision.rs:67-69]
  - Signature: `pub trait VisionClient {`
  - Purpose: Indexed type `VisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:67-69]
- `VisionRequest` (class) component `VisionRequest [class]` (`ad8e2a0d-6cea-5220-82b7-4ba82e145a53`) lines 72-79 [crates/gwiki/src/vision.rs:72-79]
  - Signature: `pub struct VisionRequest<'a> {`
  - Purpose: 'VisionRequest<'a>' is a borrowed request payload for an image asset, carrying its filename, optional MIME type, filesystem path, raw bytes, and optional width and height metadata. [crates/gwiki/src/vision.rs:72-79]
- `VisionEndpoint` (type) component `VisionEndpoint [type]` (`8151fde8-971f-514e-a350-a72ff2902e73`) lines 81-85 [crates/gwiki/src/vision.rs:81-85]
  - Signature: `pub enum VisionEndpoint<'a> {`
  - Purpose: Indexed type `VisionEndpoint` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:81-85]
- `VisionMarkdownResult` (class) component `VisionMarkdownResult [class]` (`e58815f9-2975-591f-bead-623763868e7f`) lines 88-91 [crates/gwiki/src/vision.rs:88-91]
  - Signature: `pub struct VisionMarkdownResult {`
  - Purpose: 'VisionMarkdownResult' is a Rust struct that records the 'PathBuf' of a generated markdown artifact along with an optional 'VisionDegradation' describing any quality loss or fallback used during vision-to-markdown conversion. [crates/gwiki/src/vision.rs:88-91]
- `write_image_derived_markdown` (function) component `write_image_derived_markdown [function]` (`80c0bdaa-187a-553c-ac25-7b6ba9bae651`) lines 93-140 [crates/gwiki/src/vision.rs:93-140]
  - Signature: `pub fn write_image_derived_markdown(`
  - Purpose: Creates the derived markdown file for an image record by attempting vision extraction when available, falling back to a degradation descriptor on failure or unavailability, writing the rendered markdown atomically under 'vault_root', and returning the relative path plus any degradation metadata. [crates/gwiki/src/vision.rs:93-140]
- `render_image_derived_markdown` (function) component `render_image_derived_markdown [function]` (`e2756036-f10c-578b-b1e9-61fe339ebab3`) lines 142-254 [crates/gwiki/src/vision.rs:142-254]
  - Signature: `fn render_image_derived_markdown(`
  - Purpose: Builds a markdown document string for an image-derived source record by assembling front matter metadata from the scope, record, request, optional degradation info, and deduplicated vision-extraction metadata, including a vision status flag. [crates/gwiki/src/vision.rs:142-254]
- `dedupe_vision_metadata` (function) component `dedupe_vision_metadata [function]` (`4e0432de-06b0-5b94-bab5-b4e966cbd7ca`) lines 256-264 [crates/gwiki/src/vision.rs:256-264]
  - Signature: `fn dedupe_vision_metadata(metadata: &[(String, String)]) -> Vec<(String, String)> {`
  - Purpose: Builds a deduplicated, lexicographically ordered 'Vec<(String, String)>' by iterating over at most 'MAX_VISION_METADATA_ENTRIES' input pairs, normalizing each key with 'bounded_vision_metadata_key' and 'vision_metadata_key', and keeping only the first value seen for each resulting key. [crates/gwiki/src/vision.rs:256-264]
- `bounded_vision_metadata_key` (function) component `bounded_vision_metadata_key [function]` (`e25f53e2-0c6e-53d9-88a7-48d538da4e37`) lines 266-283 [crates/gwiki/src/vision.rs:266-283]
  - Signature: `fn bounded_vision_metadata_key(key: &str) -> String {`
  - Purpose: Returns the original key unchanged if it contains at most 'MAX_VISION_METADATA_KEY_CHARS' characters; otherwise it builds a prefix of that many characters and appends '-' plus the first 'VISION_METADATA_KEY_HASH_CHARS' of the key’s content hash. [crates/gwiki/src/vision.rs:266-283]
- `vision_metadata_key` (function) component `vision_metadata_key [function]` (`15844d39-593a-50e6-a67e-2d262022194a`) lines 285-303 [crates/gwiki/src/vision.rs:285-303]
  - Signature: `fn vision_metadata_key(key: &str) -> String {`
  - Purpose: Normalizes an input key to a single-line, lowercase ASCII identifier containing only alphanumerics, '_', and '-', strips leading/trailing underscores, and returns '"vision_metadata"' if nothing remains or '"vision_{sanitized}"' otherwise. [crates/gwiki/src/vision.rs:285-303]
- `write_vision_markdown_atomically` (function) component `write_vision_markdown_atomically [function]` (`278fd5c4-cf87-5f99-869b-27dcc62d7907`) lines 305-329 [crates/gwiki/src/vision.rs:305-329]
  - Signature: `fn write_vision_markdown_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Writes 'contents' to a temporary file, fsyncs it, atomically replaces 'path' with the temp file, and then syncs the parent directory, converting any I/O failure into a 'WikiError::Io'. [crates/gwiki/src/vision.rs:305-329]
- `create_vision_temp_file` (function) component `create_vision_temp_file [function]` (`6a1e3093-e5c5-5dd1-bbdd-26f4854ca94d`) lines 331-358 [crates/gwiki/src/vision.rs:331-358]
  - Signature: `fn create_vision_temp_file(path: &Path) -> Result<NamedTempFile, WikiError> {`
  - Purpose: Creates a temporary file in 'path'’s parent directory with a '.{file_name}.' prefix and '.tmp' suffix, or returns 'WikiError::Io' if 'path' has no valid parent directory or tempfile creation fails. [crates/gwiki/src/vision.rs:331-358]
- `sync_parent_dir` (function) component `sync_parent_dir [function]` (`edbe999e-78fb-5e95-8436-cf97fce72a94`) lines 360-379 [crates/gwiki/src/vision.rs:360-379]
  - Signature: `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: On Unix, it opens the parent directory of 'path' and calls 'sync_all' to flush directory metadata to disk, mapping any I/O error into 'WikiError::Io', while on non-Unix it returns 'Ok(())' without doing anything. [crates/gwiki/src/vision.rs:360-379]
- `FakeVisionClient` (class) component `FakeVisionClient [class]` (`f2eee0d9-de54-51aa-b3d5-d792fe751c7d`) lines 388-390 [crates/gwiki/src/vision.rs:388-390]
  - Signature: `struct FakeVisionClient {`
  - Purpose: 'FakeVisionClient' is a test stub struct that tracks the number of vision-client invocations in a 'Cell<usize>' for interior-mutable call counting. [crates/gwiki/src/vision.rs:388-390]
- `FailingVisionClient` (class) component `FailingVisionClient [class]` (`2c37c20d-e103-56a5-bebe-3c39bfecc4d5`) lines 392-392 [crates/gwiki/src/vision.rs:392]
  - Signature: `struct FailingVisionClient;`
  - Purpose: 'FailingVisionClient' is an empty struct type that serves as a deliberately failing vision-client implementation, typically used to simulate error paths in tests or fallback logic. [crates/gwiki/src/vision.rs:392]
- `FakeVisionClient` (class) component `FakeVisionClient [class]` (`83245e01-5859-5737-9dd2-a4d2d79fcadc`) lines 394-403 [crates/gwiki/src/vision.rs:394-403]
  - Signature: `impl VisionClient for FakeVisionClient {`
  - Purpose: 'FakeVisionClient' is a test double implementing 'VisionClient' whose 'extract' method increments an internal call counter and returns a fixed 'VisionExtraction' containing a canned description, OCR text, and 'model=fake-vision' metadata. [crates/gwiki/src/vision.rs:394-403]
- `FakeVisionClient.extract` (method) component `FakeVisionClient.extract [method]` (`02b04b86-d3cb-5df4-b4b8-168a572701f3`) lines 395-402 [crates/gwiki/src/vision.rs:395-402]
  - Signature: `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: Increments the internal call counter and returns a fixed 'VisionExtraction' containing a circuit-diagram description, optional OCR text '"VCC GND Sensor"', and 'model=fake-vision' metadata. [crates/gwiki/src/vision.rs:395-402]
- `FailingVisionClient` (class) component `FailingVisionClient [class]` (`b448b45c-d1fc-5f0f-8450-825f1b31ec29`) lines 405-412 [crates/gwiki/src/vision.rs:405-412]
  - Signature: `impl VisionClient for FailingVisionClient {`
  - Purpose: 'FailingVisionClient' is a 'VisionClient' implementation whose 'extract' method always returns a 'WikiError::Daemon' for '/api/chat/attachments' with the message '"temporarily unavailable"'. [crates/gwiki/src/vision.rs:405-412]
- `FailingVisionClient.extract` (method) component `FailingVisionClient.extract [method]` (`b7c876c5-6c43-5eed-8e3b-1d663072c7c5`) lines 406-411 [crates/gwiki/src/vision.rs:406-411]
  - Signature: `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: 'extract' always returns 'Err(WikiError::Daemon { endpoint: "/api/chat/attachments", message: "temporarily unavailable" })', indicating the vision extraction API is currently unavailable. [crates/gwiki/src/vision.rs:406-411]
- `EmptyVisionClient` (class) component `EmptyVisionClient [class]` (`dbf51d43-bffa-50e5-80c8-425cab1f13c6`) lines 414-414 [crates/gwiki/src/vision.rs:414]
  - Signature: `struct EmptyVisionClient;`
  - Purpose: 'EmptyVisionClient' is an empty marker struct representing a no-op or placeholder vision client implementation with no stored state. [crates/gwiki/src/vision.rs:414]
- `EmptyVisionClient` (class) component `EmptyVisionClient [class]` (`7d54e79c-6882-54c1-a4e8-36280d845c80`) lines 416-426 [crates/gwiki/src/vision.rs:416-426]
  - Signature: `impl VisionClient for EmptyVisionClient {`
  - Purpose: 'EmptyVisionClient' is a 'VisionClient' implementation whose 'extract' method ignores the request and returns a synthetic 'VisionExtraction' containing only blank description text, no OCR output, and a 'model=haiku' metadata entry. [crates/gwiki/src/vision.rs:416-426]
- `EmptyVisionClient.extract` (method) component `EmptyVisionClient.extract [method]` (`a77a7f6a-fa7f-513c-89d1-5ee6471dd172`) lines 417-425 [crates/gwiki/src/vision.rs:417-425]
  - Signature: `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: Returns a 'VisionExtraction' representing an HTTP 200 blank-content vision response, with whitespace-only 'description', no 'ocr_text', and 'metadata' containing '("model", "haiku")'. [crates/gwiki/src/vision.rs:417-425]
- `record_for` (function) component `record_for [function]` (`d17f288f-afbf-55d0-8be0-cdcad6f76d78`) lines 428-444 [crates/gwiki/src/vision.rs:428-444]
  - Signature: `fn record_for(temp: &Path) -> SourceRecord {`
  - Purpose: Registers a 'SourceDraft' for '/tmp/circuit.png' as a manually ingested pending image source with the given bytes, metadata, and citation, then unwraps the resulting 'SourceRecord' from 'SourceManifest::register'. [crates/gwiki/src/vision.rs:428-444]
- `vision_writes_derived_markdown` (function) component `vision_writes_derived_markdown [function]` (`4ba74aa2-2e9e-5ab4-8bfc-1eab23b4ca34`) lines 447-491 [crates/gwiki/src/vision.rs:447-491]
  - Signature: `fn vision_writes_derived_markdown() {`
  - Purpose: Tests that 'write_image_derived_markdown' invokes the vision client once and writes a derived markdown file at 'knowledge/sources/<record-id>.md' containing image metadata, scope fields, the vision model, OCR/description sections, and the source asset reference without degradation. [crates/gwiki/src/vision.rs:447-491]
- `vision_metadata_frontmatter_uses_sanitized_prefixed_keys` (function) component `vision_metadata_frontmatter_uses_sanitized_prefixed_keys [function]` (`ba2cf257-d418-5a15-95c4-b1f318e22d2f`) lines 494-522 [crates/gwiki/src/vision.rs:494-522]
  - Signature: `fn vision_metadata_frontmatter_uses_sanitized_prefixed_keys() {`
  - Purpose: Verifies that image-derived markdown frontmatter sanitizes and prefixes vision metadata keys, preserves the first normalized 'vision_model_name' entry, and omits duplicate or unsanitized variants. [crates/gwiki/src/vision.rs:494-522]
- `vision_metadata_bounds_entries_and_hashes_long_keys` (function) component `vision_metadata_bounds_entries_and_hashes_long_keys [function]` (`78e39401-8ca1-585c-9453-dcc0d0659bde`) lines 525-547 [crates/gwiki/src/vision.rs:525-547]
  - Signature: `fn vision_metadata_bounds_entries_and_hashes_long_keys() {`
  - Purpose: Verifies that 'dedupe_vision_metadata' preserves a overlong key by truncating and hashing it into the expected 'vision_<truncated>-<hash>' form while also capping the result set at 'MAX_VISION_METADATA_ENTRIES'. [crates/gwiki/src/vision.rs:525-547]
- `missing_vision_degrades` (function) component `missing_vision_degrades [function]` (`58593558-9a9e-5619-8cec-7049ebc75353`) lines 550-592 [crates/gwiki/src/vision.rs:550-592]
  - Signature: `fn missing_vision_degrades() {`
  - Purpose: Verifies that when the vision endpoint is unavailable, 'write_image_derived_markdown' returns a 'MissingEndpoint' degradation, preserves the original image asset bytes, and emits derived markdown marked 'vision_status: unavailable' with the fallback metadata and original asset path. [crates/gwiki/src/vision.rs:550-592]
- `vision_client_error_degrades` (function) component `vision_client_error_degrades [function]` (`84dd663b-0c0f-5f1f-926f-18bac479de67`) lines 595-626 [crates/gwiki/src/vision.rs:595-626]
  - Signature: `fn vision_client_error_degrades() {`
  - Purpose: Verifies that when 'write_image_derived_markdown' is invoked with an available-but-failing vision client, it records a 'VisionError' degradation with an attachment-URL fallback and emits derived markdown marked 'vision_status: unavailable' and 'vision_degradation: vision_error' including source references. [crates/gwiki/src/vision.rs:595-626]
- `empty_vision_extraction_degrades` (function) component `empty_vision_extraction_degrades [function]` (`7ea5843a-2eab-5dbe-9b84-bf57abf0538a`) lines 629-659 [crates/gwiki/src/vision.rs:629-659]
  - Signature: `fn empty_vision_extraction_degrades() {`
  - Purpose: Verifies that when vision extraction returns empty/unusable output, 'write_image_derived_markdown' records a 'VisionError' degradation, marks 'vision_status: unavailable' and 'vision_degradation: vision_error' in the generated markdown, and omits extracted-content fields like 'vision_status: extracted' and the '## Vision Description' section. [crates/gwiki/src/vision.rs:629-659]
- `vision_markdown_overwrites_atomically_without_temp_leftovers` (function) component `vision_markdown_overwrites_atomically_without_temp_leftovers [function]` (`981f0ff4-4388-5518-bcbc-dbfb0339858b`) lines 662-715 [crates/gwiki/src/vision.rs:662-715]
  - Signature: `fn vision_markdown_overwrites_atomically_without_temp_leftovers() {`
  - Purpose: Verifies that 'write_image_derived_markdown' can overwrite an existing vision markdown file atomically, updating the stored degradation reason to 'missing_endpoint' while leaving no temporary leftovers in 'knowledge/sources'. [crates/gwiki/src/vision.rs:662-715]
- `vision_temp_file_requires_parent_directory` (function) component `vision_temp_file_requires_parent_directory [function]` (`c59a2b73-be81-5547-b1f9-ad615eaea71f`) lines 718-729 [crates/gwiki/src/vision.rs:718-729]
  - Signature: `fn vision_temp_file_requires_parent_directory() {`
  - Purpose: Verifies that 'create_vision_temp_file' rejects a parentless target path ('vision.md') by returning a 'WikiError::Io' whose underlying 'std::io::ErrorKind' is 'InvalidInput'. [crates/gwiki/src/vision.rs:718-729]

