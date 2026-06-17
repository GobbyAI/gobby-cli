---
title: crates/gwiki/src/vision.rs
type: code_file
provenance:
- file: crates/gwiki/src/vision.rs
  ranges:
  - 19-23
  - 26-29
  - 32-43
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
  - 395-402
  - 406-411
  - '414'
  - 417-425
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/vision.rs:19-23](crates/gwiki/src/vision.rs#L19-L23), [crates/gwiki/src/vision.rs:26-29](crates/gwiki/src/vision.rs#L26-L29), [crates/gwiki/src/vision.rs:32-43](crates/gwiki/src/vision.rs#L32-L43), [crates/gwiki/src/vision.rs:47-52](crates/gwiki/src/vision.rs#L47-L52), [crates/gwiki/src/vision.rs:58-65](crates/gwiki/src/vision.rs#L58-L65), [crates/gwiki/src/vision.rs:67-69](crates/gwiki/src/vision.rs#L67-L69), [crates/gwiki/src/vision.rs:72-79](crates/gwiki/src/vision.rs#L72-L79), [crates/gwiki/src/vision.rs:81-85](crates/gwiki/src/vision.rs#L81-L85), [crates/gwiki/src/vision.rs:88-91](crates/gwiki/src/vision.rs#L88-L91), [crates/gwiki/src/vision.rs:93-140](crates/gwiki/src/vision.rs#L93-L140), [crates/gwiki/src/vision.rs:142-254](crates/gwiki/src/vision.rs#L142-L254), [crates/gwiki/src/vision.rs:256-264](crates/gwiki/src/vision.rs#L256-L264), [crates/gwiki/src/vision.rs:266-283](crates/gwiki/src/vision.rs#L266-L283), [crates/gwiki/src/vision.rs:285-303](crates/gwiki/src/vision.rs#L285-L303), [crates/gwiki/src/vision.rs:305-329](crates/gwiki/src/vision.rs#L305-L329), [crates/gwiki/src/vision.rs:331-358](crates/gwiki/src/vision.rs#L331-L358), [crates/gwiki/src/vision.rs:360-379](crates/gwiki/src/vision.rs#L360-L379), [crates/gwiki/src/vision.rs:388-390](crates/gwiki/src/vision.rs#L388-L390), [crates/gwiki/src/vision.rs:392](crates/gwiki/src/vision.rs#L392), [crates/gwiki/src/vision.rs:395-402](crates/gwiki/src/vision.rs#L395-L402), [crates/gwiki/src/vision.rs:406-411](crates/gwiki/src/vision.rs#L406-L411), [crates/gwiki/src/vision.rs:414](crates/gwiki/src/vision.rs#L414), [crates/gwiki/src/vision.rs:417-425](crates/gwiki/src/vision.rs#L417-L425), [crates/gwiki/src/vision.rs:428-444](crates/gwiki/src/vision.rs#L428-L444), [crates/gwiki/src/vision.rs:447-491](crates/gwiki/src/vision.rs#L447-L491), [crates/gwiki/src/vision.rs:494-522](crates/gwiki/src/vision.rs#L494-L522), [crates/gwiki/src/vision.rs:525-547](crates/gwiki/src/vision.rs#L525-L547), [crates/gwiki/src/vision.rs:550-592](crates/gwiki/src/vision.rs#L550-L592), [crates/gwiki/src/vision.rs:595-626](crates/gwiki/src/vision.rs#L595-L626), [crates/gwiki/src/vision.rs:629-659](crates/gwiki/src/vision.rs#L629-L659), [crates/gwiki/src/vision.rs:662-715](crates/gwiki/src/vision.rs#L662-L715), [crates/gwiki/src/vision.rs:718-729](crates/gwiki/src/vision.rs#L718-L729)

</details>

# crates/gwiki/src/vision.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the vision-ingestion pipeline for wiki sources: it defines `VisionExtraction` and `VisionDegradation` to carry model results and fallback reasons, plus a `VisionClient`/`VisionRequest` interface for extracting descriptions, OCR text, and metadata from image or PDF inputs. The rest of the module turns successful extractions into derived markdown, normalizes and bounds vision metadata keys, writes updates atomically through temp files and parent-directory sync, and includes fake/failing/empty client implementations and tests to verify degradation behavior, metadata sanitization, and overwrite safety.
[crates/gwiki/src/vision.rs:19-23]
[crates/gwiki/src/vision.rs:26-29]
[crates/gwiki/src/vision.rs:32-43]
[crates/gwiki/src/vision.rs:47-52]
[crates/gwiki/src/vision.rs:58-65]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `VisionExtraction` | class | `pub struct VisionExtraction {` | `VisionExtraction [class]` | `22cadf56-b6b1-50ce-b558-dce67f342d4c` | 19-23 [crates/gwiki/src/vision.rs:19-23] | Indexed class `VisionExtraction` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:19-23] |
| `VisionDegradation` | class | `pub struct VisionDegradation {` | `VisionDegradation [class]` | `ebc4963b-c395-5a64-9482-00e4933775e4` | 26-29 [crates/gwiki/src/vision.rs:26-29] | Indexed class `VisionDegradation` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:26-29] |
| `VisionDegradation::for_routing` | method | `pub(crate) fn for_routing(routing: AiRouting, fallback: &str) -> Self {` | `VisionDegradation::for_routing [method]` | `d9596e5c-6ed9-5431-ac9c-80310c7e6740` | 32-43 [crates/gwiki/src/vision.rs:32-43] | Indexed method `VisionDegradation::for_routing` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:32-43] |
| `disabled_degradation` | function | `pub(crate) fn disabled_degradation() -> VisionDegradation {` | `disabled_degradation [function]` | `e6f398ef-3fd8-5f75-9eb7-964e1518eb14` | 47-52 [crates/gwiki/src/vision.rs:47-52] | Indexed function `disabled_degradation` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:47-52] |
| `vision_extraction_is_empty` | function | `fn vision_extraction_is_empty(extraction: &VisionExtraction) -> bool {` | `vision_extraction_is_empty [function]` | `fdba1df0-f62a-55fc-b259-040389ab0604` | 58-65 [crates/gwiki/src/vision.rs:58-65] | Indexed function `vision_extraction_is_empty` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:58-65] |
| `VisionClient` | type | `pub trait VisionClient {` | `VisionClient [type]` | `892cb9e1-fbcf-5e5c-8c11-2834b89a2303` | 67-69 [crates/gwiki/src/vision.rs:67-69] | Indexed type `VisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:67-69] |
| `VisionRequest` | class | `pub struct VisionRequest<'a> {` | `VisionRequest [class]` | `ad8e2a0d-6cea-5220-82b7-4ba82e145a53` | 72-79 [crates/gwiki/src/vision.rs:72-79] | Indexed class `VisionRequest` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:72-79] |
| `VisionEndpoint` | type | `pub enum VisionEndpoint<'a> {` | `VisionEndpoint [type]` | `8151fde8-971f-514e-a350-a72ff2902e73` | 81-85 [crates/gwiki/src/vision.rs:81-85] | Indexed type `VisionEndpoint` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:81-85] |
| `VisionMarkdownResult` | class | `pub struct VisionMarkdownResult {` | `VisionMarkdownResult [class]` | `e58815f9-2975-591f-bead-623763868e7f` | 88-91 [crates/gwiki/src/vision.rs:88-91] | Indexed class `VisionMarkdownResult` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:88-91] |
| `write_image_derived_markdown` | function | `pub fn write_image_derived_markdown(` | `write_image_derived_markdown [function]` | `80c0bdaa-187a-553c-ac25-7b6ba9bae651` | 93-140 [crates/gwiki/src/vision.rs:93-140] | Indexed function `write_image_derived_markdown` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:93-140] |
| `render_image_derived_markdown` | function | `fn render_image_derived_markdown(` | `render_image_derived_markdown [function]` | `e2756036-f10c-578b-b1e9-61fe339ebab3` | 142-254 [crates/gwiki/src/vision.rs:142-254] | Indexed function `render_image_derived_markdown` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:142-254] |
| `dedupe_vision_metadata` | function | `fn dedupe_vision_metadata(metadata: &[(String, String)]) -> Vec<(String, String)> {` | `dedupe_vision_metadata [function]` | `4e0432de-06b0-5b94-bab5-b4e966cbd7ca` | 256-264 [crates/gwiki/src/vision.rs:256-264] | Indexed function `dedupe_vision_metadata` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:256-264] |
| `bounded_vision_metadata_key` | function | `fn bounded_vision_metadata_key(key: &str) -> String {` | `bounded_vision_metadata_key [function]` | `e25f53e2-0c6e-53d9-88a7-48d538da4e37` | 266-283 [crates/gwiki/src/vision.rs:266-283] | Indexed function `bounded_vision_metadata_key` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:266-283] |
| `vision_metadata_key` | function | `fn vision_metadata_key(key: &str) -> String {` | `vision_metadata_key [function]` | `15844d39-593a-50e6-a67e-2d262022194a` | 285-303 [crates/gwiki/src/vision.rs:285-303] | Indexed function `vision_metadata_key` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:285-303] |
| `write_vision_markdown_atomically` | function | `fn write_vision_markdown_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {` | `write_vision_markdown_atomically [function]` | `278fd5c4-cf87-5f99-869b-27dcc62d7907` | 305-329 [crates/gwiki/src/vision.rs:305-329] | Indexed function `write_vision_markdown_atomically` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:305-329] |
| `create_vision_temp_file` | function | `fn create_vision_temp_file(path: &Path) -> Result<NamedTempFile, WikiError> {` | `create_vision_temp_file [function]` | `6a1e3093-e5c5-5dd1-bbdd-26f4854ca94d` | 331-358 [crates/gwiki/src/vision.rs:331-358] | Indexed function `create_vision_temp_file` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:331-358] |
| `sync_parent_dir` | function | `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {` | `sync_parent_dir [function]` | `edbe999e-78fb-5e95-8436-cf97fce72a94` | 360-379 [crates/gwiki/src/vision.rs:360-379] | Indexed function `sync_parent_dir` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:360-379] |
| `FakeVisionClient` | class | `struct FakeVisionClient {` | `FakeVisionClient [class]` | `f2eee0d9-de54-51aa-b3d5-d792fe751c7d` | 388-390 [crates/gwiki/src/vision.rs:388-390] | Indexed class `FakeVisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:388-390] |
| `FailingVisionClient` | class | `struct FailingVisionClient;` | `FailingVisionClient [class]` | `2c37c20d-e103-56a5-bebe-3c39bfecc4d5` | 392-392 [crates/gwiki/src/vision.rs:392] | Indexed class `FailingVisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:392] |
| `FakeVisionClient::extract` | method | `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {` | `FakeVisionClient::extract [method]` | `02b04b86-d3cb-5df4-b4b8-168a572701f3` | 395-402 [crates/gwiki/src/vision.rs:395-402] | Indexed method `FakeVisionClient::extract` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:395-402] |
| `FailingVisionClient::extract` | method | `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {` | `FailingVisionClient::extract [method]` | `b7c876c5-6c43-5eed-8e3b-1d663072c7c5` | 406-411 [crates/gwiki/src/vision.rs:406-411] | Indexed method `FailingVisionClient::extract` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:406-411] |
| `EmptyVisionClient` | class | `struct EmptyVisionClient;` | `EmptyVisionClient [class]` | `dbf51d43-bffa-50e5-80c8-425cab1f13c6` | 414-414 [crates/gwiki/src/vision.rs:414] | Indexed class `EmptyVisionClient` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:414] |
| `EmptyVisionClient::extract` | method | `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {` | `EmptyVisionClient::extract [method]` | `a77a7f6a-fa7f-513c-89d1-5ee6471dd172` | 417-425 [crates/gwiki/src/vision.rs:417-425] | Indexed method `EmptyVisionClient::extract` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:417-425] |
| `record_for` | function | `fn record_for(temp: &Path) -> SourceRecord {` | `record_for [function]` | `d17f288f-afbf-55d0-8be0-cdcad6f76d78` | 428-444 [crates/gwiki/src/vision.rs:428-444] | Indexed function `record_for` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:428-444] |
| `vision_writes_derived_markdown` | function | `fn vision_writes_derived_markdown() {` | `vision_writes_derived_markdown [function]` | `4ba74aa2-2e9e-5ab4-8bfc-1eab23b4ca34` | 447-491 [crates/gwiki/src/vision.rs:447-491] | Indexed function `vision_writes_derived_markdown` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:447-491] |
| `vision_metadata_frontmatter_uses_sanitized_prefixed_keys` | function | `fn vision_metadata_frontmatter_uses_sanitized_prefixed_keys() {` | `vision_metadata_frontmatter_uses_sanitized_prefixed_keys [function]` | `ba2cf257-d418-5a15-95c4-b1f318e22d2f` | 494-522 [crates/gwiki/src/vision.rs:494-522] | Indexed function `vision_metadata_frontmatter_uses_sanitized_prefixed_keys` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:494-522] |
| `vision_metadata_bounds_entries_and_hashes_long_keys` | function | `fn vision_metadata_bounds_entries_and_hashes_long_keys() {` | `vision_metadata_bounds_entries_and_hashes_long_keys [function]` | `78e39401-8ca1-585c-9453-dcc0d0659bde` | 525-547 [crates/gwiki/src/vision.rs:525-547] | Indexed function `vision_metadata_bounds_entries_and_hashes_long_keys` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:525-547] |
| `missing_vision_degrades` | function | `fn missing_vision_degrades() {` | `missing_vision_degrades [function]` | `58593558-9a9e-5619-8cec-7049ebc75353` | 550-592 [crates/gwiki/src/vision.rs:550-592] | Indexed function `missing_vision_degrades` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:550-592] |
| `vision_client_error_degrades` | function | `fn vision_client_error_degrades() {` | `vision_client_error_degrades [function]` | `84dd663b-0c0f-5f1f-926f-18bac479de67` | 595-626 [crates/gwiki/src/vision.rs:595-626] | Indexed function `vision_client_error_degrades` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:595-626] |
| `empty_vision_extraction_degrades` | function | `fn empty_vision_extraction_degrades() {` | `empty_vision_extraction_degrades [function]` | `7ea5843a-2eab-5dbe-9b84-bf57abf0538a` | 629-659 [crates/gwiki/src/vision.rs:629-659] | Indexed function `empty_vision_extraction_degrades` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:629-659] |
| `vision_markdown_overwrites_atomically_without_temp_leftovers` | function | `fn vision_markdown_overwrites_atomically_without_temp_leftovers() {` | `vision_markdown_overwrites_atomically_without_temp_leftovers [function]` | `981f0ff4-4388-5518-bcbc-dbfb0339858b` | 662-715 [crates/gwiki/src/vision.rs:662-715] | Indexed function `vision_markdown_overwrites_atomically_without_temp_leftovers` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:662-715] |
| `vision_temp_file_requires_parent_directory` | function | `fn vision_temp_file_requires_parent_directory() {` | `vision_temp_file_requires_parent_directory [function]` | `c59a2b73-be81-5547-b1f9-ad615eaea71f` | 718-729 [crates/gwiki/src/vision.rs:718-729] | Indexed function `vision_temp_file_requires_parent_directory` in `crates/gwiki/src/vision.rs`. [crates/gwiki/src/vision.rs:718-729] |
