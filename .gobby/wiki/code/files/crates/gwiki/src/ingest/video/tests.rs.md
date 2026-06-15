---
title: crates/gwiki/src/ingest/video/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/video/tests.rs
  ranges:
  - 24-61
  - 63-68
  - 70-95
  - 97-117
  - '119'
  - 121-137
  - '139'
  - 141-150
  - '152'
  - 154-166
  - '168'
  - 170-176
  - 178-204
  - 207-210
  - 213-231
  - 234-236
  - 239-246
  - 248-280
  - 282-284
  - 286-291
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video/tests.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Purpose

Test support for video ingestion. This file builds a representative `VideoSnapshot`, then defines fake media, transcription, and vision clients that either return scripted in-memory data or deliberate `WikiError::Config` failures so tests can exercise success and error paths. It also includes helpers for writing temp files, assembling transcription outputs, running ingestion against a temporary source video and in-memory wiki store, and checking the derived asset/output files.
[crates/gwiki/src/ingest/video/tests.rs:24-61]
[crates/gwiki/src/ingest/video/tests.rs:63-68]
[crates/gwiki/src/ingest/video/tests.rs:70-95]
[crates/gwiki/src/ingest/video/tests.rs:71-78]
[crates/gwiki/src/ingest/video/tests.rs:80-94]

## API Symbols

- `sample_snapshot` (function) component `sample_snapshot [function]` (`7f890208-ece7-56bf-9039-d276a5b2d149`) lines 24-61 [crates/gwiki/src/ingest/video/tests.rs:24-61]
  - Signature: `fn sample_snapshot() -> VideoSnapshot {`
  - Purpose: Constructs and returns a hard-coded 'VideoSnapshot' for '/tmp/lecture.mp4' with MP4 bytes, timestamps, duration/frame interval metadata, two frame descriptions, two transcript segments, and empty 'frame_samples'/'frame_image_paths' with 'transcription' set to 'None'. [crates/gwiki/src/ingest/video/tests.rs:24-61]
- `FakeVideoMediaExtractor` (class) component `FakeVideoMediaExtractor [class]` (`0b6385cf-0bb7-598b-a599-5af579288a34`) lines 63-68 [crates/gwiki/src/ingest/video/tests.rs:63-68]
  - Signature: `struct FakeVideoMediaExtractor {`
  - Purpose: 'FakeVideoMediaExtractor' is a test double that stores in-memory audio payload bytes and timestamped video frame byte buffers, with optional static error strings to simulate failures when extracting audio or frames. [crates/gwiki/src/ingest/video/tests.rs:63-68]
- `FakeVideoMediaExtractor` (class) component `FakeVideoMediaExtractor [class]` (`7711b7c1-507e-591d-a920-0a18c679d718`) lines 70-95 [crates/gwiki/src/ingest/video/tests.rs:70-95]
  - Signature: `impl VideoMediaExtractor for FakeVideoMediaExtractor {`
  - Purpose: 'FakeVideoMediaExtractor' is a test double for 'VideoMediaExtractor' that returns preconfigured in-memory audio and frame image temp files, optionally failing each method with a 'WikiError::Config' when its corresponding failure flag is set. [crates/gwiki/src/ingest/video/tests.rs:70-95]
- `FakeVideoMediaExtractor.extract_audio` (method) component `FakeVideoMediaExtractor.extract_audio [method]` (`9851affb-1105-5123-ad66-9abcb51d5378`) lines 71-78 [crates/gwiki/src/ingest/video/tests.rs:71-78]
  - Signature: `fn extract_audio(&self, _video: &Path) -> Result<tempfile::NamedTempFile, WikiError> {`
  - Purpose: Returns a temporary '.wav' file containing 'self.audio_bytes', unless 'self.fail_audio' is set, in which case it returns a 'WikiError::Config' with the configured detail string. [crates/gwiki/src/ingest/video/tests.rs:71-78]
- `FakeVideoMediaExtractor.sample_frame_images` (method) component `FakeVideoMediaExtractor.sample_frame_images [method]` (`5a4cb586-a932-5132-92c7-c5ebfb5139fe`) lines 80-94 [crates/gwiki/src/ingest/video/tests.rs:80-94]
  - Signature: `fn sample_frame_images(`
  - Purpose: Returns either a 'WikiError::Config' if 'fail_frames' is set, or otherwise converts each '(start_ms, bytes)' entry in 'self.frames' into a '(u64, NamedTempFile)' pair by writing the bytes to a temporary '.jpg' file and collecting the results into a 'Vec'. [crates/gwiki/src/ingest/video/tests.rs:80-94]
- `temp_file_with_bytes` (function) component `temp_file_with_bytes [function]` (`51f60224-b068-5792-8c98-547680928136`) lines 97-117 [crates/gwiki/src/ingest/video/tests.rs:97-117]
  - Signature: `fn temp_file_with_bytes(suffix: &str, bytes: &[u8]) -> Result<tempfile::NamedTempFile, WikiError> {`
  - Purpose: Creates a temporary file with the given suffix, writes the provided bytes to it, flushes the contents to disk, and returns the 'NamedTempFile', converting any I/O failure into a 'WikiError::Io' annotated with the failed action and optional path. [crates/gwiki/src/ingest/video/tests.rs:97-117]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`8a25289c-22e2-5eb7-ba40-f3c281e36f90`) lines 119-119 [crates/gwiki/src/ingest/video/tests.rs:119]
  - Signature: `struct FakeTranscriptionClient;`
  - Purpose: 'FakeTranscriptionClient' is a placeholder 'struct' type representing a mock transcription client interface with no fields or behavior defined in the provided signature. [crates/gwiki/src/ingest/video/tests.rs:119]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`2ed13d73-a0f7-5688-8a7a-a64ec1c8e42f`) lines 121-137 [crates/gwiki/src/ingest/video/tests.rs:121-137]
  - Signature: `impl TranscriptionClient for FakeTranscriptionClient {`
  - Purpose: 'FakeTranscriptionClient' is a 'TranscriptionClient' test double whose 'transcribe' method ignores the request and always returns a fixed English 'TranscriptionOutput' containing one segment from 1,000 to 2,000 ms with the text “Audio-first transcript from extracted video audio.” [crates/gwiki/src/ingest/video/tests.rs:121-137]
- `FakeTranscriptionClient.transcribe` (method) component `FakeTranscriptionClient.transcribe [method]` (`5673efae-ac69-599a-a6ee-c12ce127d063`) lines 122-136 [crates/gwiki/src/ingest/video/tests.rs:122-136]
  - Signature: `fn transcribe(`
  - Purpose: Returns a fixed English 'TranscriptionOutput' with one segment spanning 1,000 to 2,000 and the text 'Audio-first transcript from extracted video audio.', ignoring the request and always succeeding. [crates/gwiki/src/ingest/video/tests.rs:122-136]
- `FailingTranscriptionClient` (class) component `FailingTranscriptionClient [class]` (`631de312-3768-55cc-a4b4-af0e1beea4c6`) lines 139-139 [crates/gwiki/src/ingest/video/tests.rs:139]
  - Signature: `struct FailingTranscriptionClient;`
  - Purpose: 'FailingTranscriptionClient' is a stub transcription client type intended to satisfy the transcription client interface while deliberately failing on use. [crates/gwiki/src/ingest/video/tests.rs:139]
- `FailingTranscriptionClient` (class) component `FailingTranscriptionClient [class]` (`aff9d74f-ff25-5b67-8002-bf4c70dfe1ad`) lines 141-150 [crates/gwiki/src/ingest/video/tests.rs:141-150]
  - Signature: `impl TranscriptionClient for FailingTranscriptionClient {`
  - Purpose: 'FailingTranscriptionClient' is a 'TranscriptionClient' implementation whose 'transcribe' method always returns 'Err(WikiError::Config { detail: "stt provider failed" })' instead of producing a transcription. [crates/gwiki/src/ingest/video/tests.rs:141-150]
- `FailingTranscriptionClient.transcribe` (method) component `FailingTranscriptionClient.transcribe [method]` (`4bdece68-3c18-5b28-b640-fe714d2a6625`) lines 142-149 [crates/gwiki/src/ingest/video/tests.rs:142-149]
  - Signature: `fn transcribe(`
  - Purpose: 'transcribe' is a stub implementation that ignores its 'TranscriptionRequest' input and always returns 'Err(WikiError::Config { detail: "stt provider failed" })'. [crates/gwiki/src/ingest/video/tests.rs:142-149]
- `FakeVisionClient` (class) component `FakeVisionClient [class]` (`75c94e04-1bb4-58c3-9d2f-c17395c8d100`) lines 152-152 [crates/gwiki/src/ingest/video/tests.rs:152]
  - Signature: `struct FakeVisionClient;`
  - Purpose: A 'FakeVisionClient' is a placeholder/mock client struct for vision-related operations, typically used in tests or offline code paths to simulate a real vision service. [crates/gwiki/src/ingest/video/tests.rs:152]
- `FakeVisionClient` (class) component `FakeVisionClient [class]` (`ea225e83-6a31-509c-b0e8-b87f829e49c1`) lines 154-166 [crates/gwiki/src/ingest/video/tests.rs:154-166]
  - Signature: `impl VisionClient for FakeVisionClient {`
  - Purpose: 'FakeVisionClient' is a 'VisionClient' test stub that implements 'extract' by returning a synthetic 'VisionExtraction' whose description reports the request file name and byte length, with no OCR text and empty metadata. [crates/gwiki/src/ingest/video/tests.rs:154-166]
- `FakeVisionClient.extract` (method) component `FakeVisionClient.extract [method]` (`3288d15f-8991-512b-ac48-fcf4024598f7`) lines 155-165 [crates/gwiki/src/ingest/video/tests.rs:155-165]
  - Signature: `fn extract(&self, request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: 'extract' constructs and returns a 'VisionExtraction' wrapped in 'Ok', with 'description' set to '"frame {file_name} has {bytes.len()} bytes"', 'ocr_text' set to 'None', and 'metadata' initialized empty. [crates/gwiki/src/ingest/video/tests.rs:155-165]
- `FailingVisionClient` (class) component `FailingVisionClient [class]` (`2ad52397-96f3-5a7c-9839-ba02dea09de3`) lines 168-168 [crates/gwiki/src/ingest/video/tests.rs:168]
  - Signature: `struct FailingVisionClient;`
  - Purpose: A zero-field 'struct' named 'FailingVisionClient' that represents a deliberately failing vision client stub. [crates/gwiki/src/ingest/video/tests.rs:168]
- `FailingVisionClient` (class) component `FailingVisionClient [class]` (`9880485c-3e85-5307-99d9-d52577442f09`) lines 170-176 [crates/gwiki/src/ingest/video/tests.rs:170-176]
  - Signature: `impl VisionClient for FailingVisionClient {`
  - Purpose: 'FailingVisionClient' is a 'VisionClient' implementation whose 'extract' method unconditionally returns 'Err(WikiError::Config { detail: "vision provider failed" })' for any 'VisionRequest'. [crates/gwiki/src/ingest/video/tests.rs:170-176]
- `FailingVisionClient.extract` (method) component `FailingVisionClient.extract [method]` (`b1fe9d97-dbe1-5491-a916-6ef662a25a45`) lines 171-175 [crates/gwiki/src/ingest/video/tests.rs:171-175]
  - Signature: `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: This method ignores its 'VisionRequest' argument and always returns 'Err(WikiError::Config { detail: "vision provider failed" })'. [crates/gwiki/src/ingest/video/tests.rs:171-175]
- `transcript_output` (function) component `transcript_output [function]` (`45493ef2-817d-5942-8033-a08e99f45475`) lines 178-204 [crates/gwiki/src/ingest/video/tests.rs:178-204]
  - Signature: `fn transcript_output(`
  - Purpose: 'transcript_output' constructs a 'TranscriptionOutput' from timestamped text segments, setting language metadata based on whether the transcript was translated to English, copying the source language and task, marking the result as non-partial and non-degraded, and initializing range-tracking fields empty. [crates/gwiki/src/ingest/video/tests.rs:178-204]
- `ScriptedTranscriptionClient` (class) component `ScriptedTranscriptionClient [class]` (`1ccc660d-28d5-585f-b643-564dfdf6399c`) lines 207-210 [crates/gwiki/src/ingest/video/tests.rs:207-210]
  - Signature: `struct ScriptedTranscriptionClient {`
  - Purpose: 'ScriptedTranscriptionClient' is a mutable scripted test client that stores a queue of 'Result<TranscriptionOutput, WikiError>' values in 'english' and logs invocation names in a shared 'Rc<RefCell<Vec<&'static str>>>' 'calls' buffer. [crates/gwiki/src/ingest/video/tests.rs:207-210]
- `ScriptedTranscriptionClient` (class) component `ScriptedTranscriptionClient [class]` (`2d49577f-5adf-5ded-9241-35e0cea907ce`) lines 213-231 [crates/gwiki/src/ingest/video/tests.rs:213-231]
  - Signature: `impl TranscriptionClient for ScriptedTranscriptionClient {`
  - Purpose: 'ScriptedTranscriptionClient' is a test double for 'TranscriptionClient' that always fails 'transcribe' with a 'WikiError::Config' fallback error while recording 'translate_to_english' calls and returning the next scripted English 'TranscriptionOutput' from an internal queue. [crates/gwiki/src/ingest/video/tests.rs:213-231]
- `ScriptedTranscriptionClient.transcribe` (method) component `ScriptedTranscriptionClient.transcribe [method]` (`dc8380a2-8117-52d5-a06f-5a9b2ccef80b`) lines 214-221 [crates/gwiki/src/ingest/video/tests.rs:214-221]
  - Signature: `fn transcribe(`
  - Purpose: 'transcribe' is a fallback implementation that ignores its 'TranscriptionRequest' argument and always returns 'Err(WikiError::Config { detail: "unexpected transcribe fallback" })'. [crates/gwiki/src/ingest/video/tests.rs:214-221]
- `ScriptedTranscriptionClient.translate_to_english` (method) component `ScriptedTranscriptionClient.translate_to_english [method]` (`275249fd-5fa4-59e9-a6c0-9db59a1cf8c0`) lines 223-230 [crates/gwiki/src/ingest/video/tests.rs:223-230]
  - Signature: `fn translate_to_english(`
  - Purpose: Records the '"translate_to_english"' call in 'self.calls', ignores the request and language hint parameters, and returns the first stored 'TranscriptionOutput' from 'self.english' by removing index '0' as a 'Result'. [crates/gwiki/src/ingest/video/tests.rs:223-230]
- `ScriptedChunkTranscriptionClient` (class) component `ScriptedChunkTranscriptionClient [class]` (`16d40908-7987-5991-b6d7-2e57d20ee65f`) lines 234-236 [crates/gwiki/src/ingest/video/tests.rs:234-236]
  - Signature: `struct ScriptedChunkTranscriptionClient {`
  - Purpose: A 'ScriptedChunkTranscriptionClient' is a struct that stores a mutable scripted queue of transcription results, 'Vec<Result<TranscriptionOutput, WikiError>>', inside a 'RefCell' for interior mutability. [crates/gwiki/src/ingest/video/tests.rs:234-236]
- `ScriptedChunkTranscriptionClient` (class) component `ScriptedChunkTranscriptionClient [class]` (`3c5fff66-02f3-52a8-a815-b6b27b8142fa`) lines 239-246 [crates/gwiki/src/ingest/video/tests.rs:239-246]
  - Signature: `impl TranscriptionClient for ScriptedChunkTranscriptionClient {`
  - Purpose: 'ScriptedChunkTranscriptionClient' is a 'TranscriptionClient' implementation whose 'transcribe' method ignores the incoming request and returns the first preloaded 'TranscriptionOutput' by mutably removing index '0' from its internal 'outputs' collection. [crates/gwiki/src/ingest/video/tests.rs:239-246]
- `ScriptedChunkTranscriptionClient.transcribe` (method) component `ScriptedChunkTranscriptionClient.transcribe [method]` (`12d8ba5e-63e3-572c-9c4f-dbb24144a27e`) lines 240-245 [crates/gwiki/src/ingest/video/tests.rs:240-245]
  - Signature: `fn transcribe(`
  - Purpose: It ignores the 'TranscriptionRequest' and returns the first queued transcription output by mutably borrowing 'self.outputs' and removing element '0'. [crates/gwiki/src/ingest/video/tests.rs:240-245]
- `ingest_with_media` (function) component `ingest_with_media [function]` (`e1c3db54-991c-57f5-ac71-66745dded5c5`) lines 248-280 [crates/gwiki/src/ingest/video/tests.rs:248-280]
  - Signature: `fn ingest_with_media(`
  - Purpose: Creates a temporary source video file and delegates to 'ingest_video_file_with_processing' to ingest a synthesized 'VideoFileSnapshot' into a default in-memory wiki store using the provided transcription, vision, and media extractors, returning the resulting 'VideoIngestResult' or 'WikiError'. [crates/gwiki/src/ingest/video/tests.rs:248-280]
- `read_derived` (function) component `read_derived [function]` (`4a5dbf5d-a09b-52cb-9b90-14f849bf1d8c`) lines 282-284 [crates/gwiki/src/ingest/video/tests.rs:282-284]
  - Signature: `fn read_derived(vault_root: &Path, result: &VideoIngestResult) -> String {`
  - Purpose: Reads the derived video file at 'vault_root.join(result.derived_path)' into a UTF-8 'String', panicking with '"read derived video"' if the file cannot be read. [crates/gwiki/src/ingest/video/tests.rs:282-284]
- `assert_asset_preserved` (function) component `assert_asset_preserved [function]` (`bb72cb2c-1370-5e9d-8d28-9892eb7513ae`) lines 286-291 [crates/gwiki/src/ingest/video/tests.rs:286-291]
  - Signature: `fn assert_asset_preserved(vault_root: &Path, result: &VideoIngestResult, expected: &[u8]) {`
  - Purpose: Asserts that the bytes of the ingested video asset at 'vault_root.join(result.asset_path)' exactly match the provided 'expected' byte slice. [crates/gwiki/src/ingest/video/tests.rs:286-291]

