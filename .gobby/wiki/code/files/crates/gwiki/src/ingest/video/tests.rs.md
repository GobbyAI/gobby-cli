---
title: crates/gwiki/src/ingest/video/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/video/tests.rs
  ranges:
  - 18-55
  - 57-62
  - 64-89
  - 65-72
  - 74-88
  - 91-111
  - '113'
  - 115-131
  - 116-130
  - '133'
  - 135-144
  - 136-143
  - '146'
  - 148-160
  - 149-159
  - '162'
  - 164-170
  - 165-169
  - 172-198
  - 201-273
  - 276-323
  - 326-329
  - 332-350
  - 333-340
  - 342-349
  - 354-446
  - 449-451
  - 454-461
  - 455-460
  - 464-617
  - 620-638
  - 641-656
  - 659-707
  - 710-765
  - 767-799
  - 801-803
  - 805-810
  - 813-843
  - 846-883
  - 886-922
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video/tests.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Purpose

`crates/gwiki/src/ingest/video/tests.rs` exposes 40 indexed API symbols.
[crates/gwiki/src/ingest/video/tests.rs:18-55]
[crates/gwiki/src/ingest/video/tests.rs:57-62]
[crates/gwiki/src/ingest/video/tests.rs:64-89]
[crates/gwiki/src/ingest/video/tests.rs:65-72]
[crates/gwiki/src/ingest/video/tests.rs:74-88]

## API Symbols

- `sample_snapshot` (function) component `sample_snapshot [function]` (`28f836b4-c6ff-5d8f-984d-d99c991de698`) lines 18-55 [crates/gwiki/src/ingest/video/tests.rs:18-55]
  - Signature: `fn sample_snapshot() -> VideoSnapshot {`
  - Purpose: Returns a `VideoSnapshot` struct instantiated with hardcoded sample metadata, frame descriptions, and transcript segments for an 8-second video file. [crates/gwiki/src/ingest/video/tests.rs:18-55]
- `FakeVideoMediaExtractor` (class) component `FakeVideoMediaExtractor [class]` (`bc0764a2-32f9-571e-87ee-d99e82f20ccc`) lines 57-62 [crates/gwiki/src/ingest/video/tests.rs:57-62]
  - Signature: `struct FakeVideoMediaExtractor {`
  - Purpose: A test mock struct that stores audio bytes and timestamped video frames while allowing injection of configurable failures for extraction testing. [crates/gwiki/src/ingest/video/tests.rs:57-62]
- `FakeVideoMediaExtractor` (class) component `FakeVideoMediaExtractor [class]` (`a0a23429-0424-57a3-b5fd-13ea091bbfdd`) lines 64-89 [crates/gwiki/src/ingest/video/tests.rs:64-89]
  - Signature: `impl VideoMediaExtractor for FakeVideoMediaExtractor {`
  - Purpose: `FakeVideoMediaExtractor` is a mock implementation of `VideoMediaExtractor` that returns pre-configured audio bytes and video frames as temporary WAV/JPG files, or controlled errors for testing purposes. [crates/gwiki/src/ingest/video/tests.rs:64-89]
- `FakeVideoMediaExtractor.extract_audio` (method) component `FakeVideoMediaExtractor.extract_audio [method]` (`6fe6a29e-fafe-53be-b386-2eeb025e3a01`) lines 65-72 [crates/gwiki/src/ingest/video/tests.rs:65-72]
  - Signature: `fn extract_audio(&self, _video: &Path) -> Result<tempfile::NamedTempFile, WikiError> {`
  - Purpose: Returns either a configuration error if audio extraction is disabled or a temporary .wav file containing pre-stored audio bytes, ignoring the input video path. [crates/gwiki/src/ingest/video/tests.rs:65-72]
- `FakeVideoMediaExtractor.sample_frame_images` (method) component `FakeVideoMediaExtractor.sample_frame_images [method]` (`9146306b-2686-5e09-b94b-d5b169eb23dc`) lines 74-88 [crates/gwiki/src/ingest/video/tests.rs:74-88]
  - Signature: `fn sample_frame_images(`
  - Purpose: # Summary

This method returns a vector of frame timestamps paired with temporary JPG files created from pre-stored frame bytes, or fails with a configuration error if a failure flag is set. [crates/gwiki/src/ingest/video/tests.rs:74-88]
- `temp_file_with_bytes` (function) component `temp_file_with_bytes [function]` (`a3834ae2-950b-523b-92bb-d69eb0d6195a`) lines 91-111 [crates/gwiki/src/ingest/video/tests.rs:91-111]
  - Signature: `fn temp_file_with_bytes(suffix: &str, bytes: &[u8]) -> Result<tempfile::NamedTempFile, WikiError> {`
  - Purpose: Creates a temporary file with the specified suffix, writes and flushes the provided bytes to it, and returns the file handle or a WikiError on I/O failure. [crates/gwiki/src/ingest/video/tests.rs:91-111]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`8a5f752e-85ed-5180-b3fe-34068e4b3548`) lines 113-113 [crates/gwiki/src/ingest/video/tests.rs:113]
  - Signature: `struct FakeTranscriptionClient;`
  - Purpose: FakeTranscriptionClient is a unit struct serving as a mock or test double implementation for transcription service functionality. [crates/gwiki/src/ingest/video/tests.rs:113]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`7634aaa1-d856-536e-985b-11ab648dec09`) lines 115-131 [crates/gwiki/src/ingest/video/tests.rs:115-131]
  - Signature: `impl TranscriptionClient for FakeTranscriptionClient {`
  - Purpose: A mock `TranscriptionClient` implementation that returns a hardcoded English transcript with a single fixed segment (1000-2000ms) for testing purposes. [crates/gwiki/src/ingest/video/tests.rs:115-131]
- `FakeTranscriptionClient.transcribe` (method) component `FakeTranscriptionClient.transcribe [method]` (`c2f5b665-933d-5f81-afa2-fc56cebe3e4b`) lines 116-130 [crates/gwiki/src/ingest/video/tests.rs:116-130]
  - Signature: `fn transcribe(`
  - Purpose: Returns a mock `TranscriptionOutput` with hardcoded English transcript spanning 1000-2000 milliseconds, disregarding the input `TranscriptionRequest`. [crates/gwiki/src/ingest/video/tests.rs:116-130]
- `FailingTranscriptionClient` (class) component `FailingTranscriptionClient [class]` (`c6035b26-69a5-5b46-a077-07fedb3d4c87`) lines 133-133 [crates/gwiki/src/ingest/video/tests.rs:133]
  - Signature: `struct FailingTranscriptionClient;`
  - Purpose: FailingTranscriptionClient is a zero-sized unit struct intended to serve as a mock implementation of a transcription service client for testing failure scenarios. [crates/gwiki/src/ingest/video/tests.rs:133]
- `FailingTranscriptionClient` (class) component `FailingTranscriptionClient [class]` (`2b5129ed-040c-551b-8d54-da41506f32e7`) lines 135-144 [crates/gwiki/src/ingest/video/tests.rs:135-144]
  - Signature: `impl TranscriptionClient for FailingTranscriptionClient {`
  - Purpose: FailingTranscriptionClient is a TranscriptionClient stub implementation that unconditionally returns a `WikiError::Config` with the message "stt provider failed" for any transcription request. [crates/gwiki/src/ingest/video/tests.rs:135-144]
- `FailingTranscriptionClient.transcribe` (method) component `FailingTranscriptionClient.transcribe [method]` (`074f384b-69b7-5eb6-bba7-e0bb059f81f0`) lines 136-143 [crates/gwiki/src/ingest/video/tests.rs:136-143]
  - Signature: `fn transcribe(`
  - Purpose: This method unconditionally returns a `WikiError::Config` error indicating that the speech-to-text provider is unavailable, serving as a stub or placeholder implementation. [crates/gwiki/src/ingest/video/tests.rs:136-143]
- `FakeVisionClient` (class) component `FakeVisionClient [class]` (`0bd60ab9-5261-536e-a80e-788ea3c857c5`) lines 146-146 [crates/gwiki/src/ingest/video/tests.rs:146]
  - Signature: `struct FakeVisionClient;`
  - Purpose: `FakeVisionClient` is a unit struct (fieldless struct) likely used as a mock or test double for vision client functionality. [crates/gwiki/src/ingest/video/tests.rs:146]
- `FakeVisionClient` (class) component `FakeVisionClient [class]` (`a603bcad-4fcd-54f2-81b2-5ba9b97a405a`) lines 148-160 [crates/gwiki/src/ingest/video/tests.rs:148-160]
  - Signature: `impl VisionClient for FakeVisionClient {`
  - Purpose: `FakeVisionClient` is a mock implementation of the `VisionClient` trait that returns a stub `VisionExtraction` containing only the request's filename and byte length, with no OCR text or metadata. [crates/gwiki/src/ingest/video/tests.rs:148-160]
- `FakeVisionClient.extract` (method) component `FakeVisionClient.extract [method]` (`79609895-2dcb-52d1-9033-b874fb68b239`) lines 149-159 [crates/gwiki/src/ingest/video/tests.rs:149-159]
  - Signature: `fn extract(&self, request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: # Summary

Extracts vision data from a request, producing a `VisionExtraction` containing only the frame filename and byte count as description, with no OCR text or metadata. [crates/gwiki/src/ingest/video/tests.rs:149-159]
- `FailingVisionClient` (class) component `FailingVisionClient [class]` (`b104f54a-e209-5f01-bcc7-d4d1bf64f502`) lines 162-162 [crates/gwiki/src/ingest/video/tests.rs:162]
  - Signature: `struct FailingVisionClient;`
  - Purpose: `FailingVisionClient` is a zero-sized struct that serves as a test fixture or mock implementation of a vision client designed to produce failure cases. [crates/gwiki/src/ingest/video/tests.rs:162]
- `FailingVisionClient` (class) component `FailingVisionClient [class]` (`de4eecf8-ad8d-5b21-9473-0a4eb960ea34`) lines 164-170 [crates/gwiki/src/ingest/video/tests.rs:164-170]
  - Signature: `impl VisionClient for FailingVisionClient {`
  - Purpose: `FailingVisionClient` implements the `VisionClient` trait to unconditionally return a `WikiError::Config` with "vision provider failed" on any `extract` operation, serving as a stub for error-path testing. [crates/gwiki/src/ingest/video/tests.rs:164-170]
- `FailingVisionClient.extract` (method) component `FailingVisionClient.extract [method]` (`4bc6d4ed-8301-5a02-90e9-be584007143c`) lines 165-169 [crates/gwiki/src/ingest/video/tests.rs:165-169]
  - Signature: `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: This method is a stub implementation that unconditionally returns a `WikiError::Config` error indicating vision provider failure, regardless of the input request. [crates/gwiki/src/ingest/video/tests.rs:165-169]
- `transcript_output` (function) component `transcript_output [function]` (`547464b0-b252-56cc-a798-5164906d7626`) lines 172-198 [crates/gwiki/src/ingest/video/tests.rs:172-198]
  - Signature: `fn transcript_output(`
  - Purpose: Constructs a `TranscriptionOutput` by converting borrowed segment tuples into owned `TranscriptSegment` structs while populating language and task metadata fields based on translation status and source language parameters. [crates/gwiki/src/ingest/video/tests.rs:172-198]
- `video_produces_transcript_and_frames` (function) component `video_produces_transcript_and_frames [function]` (`e9605554-53ea-5ac0-b5dc-c3b7f3949db5`) lines 201-273 [crates/gwiki/src/ingest/video/tests.rs:201-273]
  - Signature: `fn video_produces_transcript_and_frames() {`
  - Purpose: This test verifies that `ingest_video_file_with_processing()` correctly extracts and stores video frames and transcript segments with properly prefixed asset storage references. [crates/gwiki/src/ingest/video/tests.rs:201-273]
- `frame_interval_zero_disables_frames` (function) component `frame_interval_zero_disables_frames [function]` (`ae72fad5-9e80-5735-9934-af36d7695c41`) lines 276-323 [crates/gwiki/src/ingest/video/tests.rs:276-323]
  - Signature: `fn frame_interval_zero_disables_frames() {`
  - Purpose: Tests that setting `frame_interval_seconds` to zero disables video frame extraction during file ingestion while preserving transcription processing. [crates/gwiki/src/ingest/video/tests.rs:276-323]
- `ScriptedTranscriptionClient` (class) component `ScriptedTranscriptionClient [class]` (`f34e3ae0-b8f4-53d2-8da9-44382bf277dc`) lines 326-329 [crates/gwiki/src/ingest/video/tests.rs:326-329]
  - Signature: `struct ScriptedTranscriptionClient {`
  - Purpose: `ScriptedTranscriptionClient` is a test mock struct that uses `RefCell` for interior mutability to store a vector of transcription results and an `Rc`-wrapped shared list of static string references for recording method invocations. [crates/gwiki/src/ingest/video/tests.rs:326-329]
- `ScriptedTranscriptionClient` (class) component `ScriptedTranscriptionClient [class]` (`02593ae8-1a2f-50d9-82a1-1dea8d53fdc2`) lines 332-350 [crates/gwiki/src/ingest/video/tests.rs:332-350]
  - Signature: `impl TranscriptionClient for ScriptedTranscriptionClient {`
  - Purpose: ScriptedTranscriptionClient is a test mock implementation of TranscriptionClient that records `translate_to_english` calls via interior mutability and returns pre-configured outputs from a scripted queue, while explicitly rejecting direct transcription requests. [crates/gwiki/src/ingest/video/tests.rs:332-350]
- `ScriptedTranscriptionClient.transcribe` (method) component `ScriptedTranscriptionClient.transcribe [method]` (`847c1a28-b1ce-5592-ab9f-5825914b7c91`) lines 333-340 [crates/gwiki/src/ingest/video/tests.rs:333-340]
  - Signature: `fn transcribe(`
  - Purpose: This fallback implementation unconditionally returns a `WikiError::Config` error, indicating an unexpected invocation that should not occur in normal operation. [crates/gwiki/src/ingest/video/tests.rs:333-340]
- `ScriptedTranscriptionClient.translate_to_english` (method) component `ScriptedTranscriptionClient.translate_to_english [method]` (`71cd094a-16cc-5dd6-8843-fc486168dab4`) lines 342-349 [crates/gwiki/src/ingest/video/tests.rs:342-349]
  - Signature: `fn translate_to_english(`
  - Purpose: This method records the invocation in a call history tracker and returns the first pre-buffered `TranscriptionOutput` by dequeuing it from an internal buffer, ignoring the actual request and language hint parameters. [crates/gwiki/src/ingest/video/tests.rs:342-349]
- `video_long_english_translation_reuses_chunk_branch` (function) component `video_long_english_translation_reuses_chunk_branch [function]` (`0aa4f156-daae-5d72-a3f8-b83095fb513b`) lines 354-446 [crates/gwiki/src/ingest/video/tests.rs:354-446]
  - Signature: `fn video_long_english_translation_reuses_chunk_branch() {`
  - Purpose: Tests the video ingestion pipeline's handling of overlapping audio chunks that exceed maximum upload size during English transcription, with simulated success and failure responses. [crates/gwiki/src/ingest/video/tests.rs:354-446]
- `ScriptedChunkTranscriptionClient` (class) component `ScriptedChunkTranscriptionClient [class]` (`895d57e3-7ad0-5a75-8a35-cc62da58f7c0`) lines 449-451 [crates/gwiki/src/ingest/video/tests.rs:449-451]
  - Signature: `struct ScriptedChunkTranscriptionClient {`
  - Purpose: ScriptedChunkTranscriptionClient is a struct that provides interior mutability through RefCell to store a vector of transcription operation Results, allowing mutation of the output collection without requiring mutable references. [crates/gwiki/src/ingest/video/tests.rs:449-451]
- `ScriptedChunkTranscriptionClient` (class) component `ScriptedChunkTranscriptionClient [class]` (`b77dc663-8a9c-5d29-a57c-6ea055071c98`) lines 454-461 [crates/gwiki/src/ingest/video/tests.rs:454-461]
  - Signature: `impl TranscriptionClient for ScriptedChunkTranscriptionClient {`
  - Purpose: ScriptedChunkTranscriptionClient is a mock implementation of TranscriptionClient that returns pre-scripted TranscriptionOutputs sequentially from an internal queue, ignoring the input request parameters. [crates/gwiki/src/ingest/video/tests.rs:454-461]
- `ScriptedChunkTranscriptionClient.transcribe` (method) component `ScriptedChunkTranscriptionClient.transcribe [method]` (`0e1f4984-bc24-5a06-92a9-b83da3b5ee3c`) lines 455-460 [crates/gwiki/src/ingest/video/tests.rs:455-460]
  - Signature: `fn transcribe(`
  - Purpose: Removes and returns the first `TranscriptionOutput` from an internal queue, disregarding the provided `TranscriptionRequest` parameter. [crates/gwiki/src/ingest/video/tests.rs:455-460]
- `production_ingest_applies_degradation_matrix` (function) component `production_ingest_applies_degradation_matrix [function]` (`25fc4dd3-52da-590c-940d-eb8b45c68bf5`) lines 464-617 [crates/gwiki/src/ingest/video/tests.rs:464-617]
  - Signature: `fn production_ingest_applies_degradation_matrix() {`
  - Purpose: This test validates that the production video ingestion pipeline correctly applies degradation markers to derived metadata when media extraction services (ffmpeg, frame extraction, vision) fail, while preserving the original asset and completing partial processing with available services. [crates/gwiki/src/ingest/video/tests.rs:464-617]
- `video_media_degradation_classifies_only_unavailable_ffmpeg_errors` (function) component `video_media_degradation_classifies_only_unavailable_ffmpeg_errors [function]` (`2ac4734d-0a13-58fa-a225-8e35329ea7e6`) lines 620-638 [crates/gwiki/src/ingest/video/tests.rs:620-638]
  - Signature: `fn video_media_degradation_classifies_only_unavailable_ffmpeg_errors() {`
  - Purpose: This test validates that `video_media_degradation` correctly classifies ffmpeg unavailability errors (missing executable) as `"ffmpeg_unavailable"` while other extraction failures return `"extraction_failed"`. [crates/gwiki/src/ingest/video/tests.rs:620-638]
- `frame_vision_failure_keeps_sample_without_description` (function) component `frame_vision_failure_keeps_sample_without_description [function]` (`cd99e40c-1b79-5bb7-b2ca-50f931bdcc45`) lines 641-656 [crates/gwiki/src/ingest/video/tests.rs:641-656]
  - Signature: `fn frame_vision_failure_keeps_sample_without_description() {`
  - Purpose: Asserts that `describe_frame_images()` persists frame samples to disk and populates the result's paths while leaving descriptions empty when the vision endpoint fails. [crates/gwiki/src/ingest/video/tests.rs:641-656]
- `persisted_frame_sources_are_removed_after_successful_loop` (function) component `persisted_frame_sources_are_removed_after_successful_loop [function]` (`c26036ec-d3f9-5685-a445-2c62c4ae7dbf`) lines 659-707 [crates/gwiki/src/ingest/video/tests.rs:659-707]
  - Signature: `fn persisted_frame_sources_are_removed_after_successful_loop() {`
  - Purpose: Verifies that `persist_video_frame_assets` removes temporary source frame files after successfully persisting video frame samples to the vault. [crates/gwiki/src/ingest/video/tests.rs:659-707]
- `persisted_frame_read_failure_drops_remaining_kept_temp_frames` (function) component `persisted_frame_read_failure_drops_remaining_kept_temp_frames [function]` (`fe46f63f-87ee-5162-b3b0-726f2450a800`) lines 710-765 [crates/gwiki/src/ingest/video/tests.rs:710-765]
  - Signature: `fn persisted_frame_read_failure_drops_remaining_kept_temp_frames() {`
  - Purpose: Verifies that `persist_video_frame_assets()` cleans up remaining kept temporary frame files when video frame asset persistence fails due to a read error on one of the frames. [crates/gwiki/src/ingest/video/tests.rs:710-765]
- `ingest_with_media` (function) component `ingest_with_media [function]` (`886701b0-1a31-5b4c-8e77-b243e3b8f736`) lines 767-799 [crates/gwiki/src/ingest/video/tests.rs:767-799]
  - Signature: `fn ingest_with_media(`
  - Purpose: Ingests a video file into an in-memory wiki store by writing source bytes and processing the file snapshot through transcription and vision endpoints. [crates/gwiki/src/ingest/video/tests.rs:767-799]
- `read_derived` (function) component `read_derived [function]` (`8ee2d07c-6db2-55a0-83ea-57e8e95e69b0`) lines 801-803 [crates/gwiki/src/ingest/video/tests.rs:801-803]
  - Signature: `fn read_derived(vault_root: &Path, result: &VideoIngestResult) -> String {`
  - Purpose: Reads the derived video file at the path constructed from `vault_root` joined with `result.derived_path` into a String, panicking if the file read fails. [crates/gwiki/src/ingest/video/tests.rs:801-803]
- `assert_asset_preserved` (function) component `assert_asset_preserved [function]` (`0112e846-ae5c-5943-9155-b825f5da1b6e`) lines 805-810 [crates/gwiki/src/ingest/video/tests.rs:805-810]
  - Signature: `fn assert_asset_preserved(vault_root: &Path, result: &VideoIngestResult, expected: &[u8]) {`
  - Purpose: Asserts that the video asset file at the path specified in the ingest result matches the expected byte sequence. [crates/gwiki/src/ingest/video/tests.rs:805-810]
- `stores_original_video` (function) component `stores_original_video [function]` (`77753645-33aa-5eb6-addd-cf1b2d84b23d`) lines 813-843 [crates/gwiki/src/ingest/video/tests.rs:813-843]
  - Signature: `fn stores_original_video() {`
  - Purpose: Tests that `ingest_video` correctly stores video files to the raw/assets directory, generates markdown metadata with video properties, and creates a manifest entry with the correct content hash. [crates/gwiki/src/ingest/video/tests.rs:813-843]
- `stores_file_backed_video` (function) component `stores_file_backed_video [function]` (`3836250a-4708-52e4-b189-353890de8382`) lines 846-883 [crates/gwiki/src/ingest/video/tests.rs:846-883]
  - Signature: `fn stores_file_backed_video() {`
  - Purpose: Tests that `ingest_video_file` correctly stores the file-backed video bytes to the asset path, records the content hash in the source manifest, and registers the derived source in the wiki store. [crates/gwiki/src/ingest/video/tests.rs:846-883]
- `video_derivatives_keep_provenance` (function) component `video_derivatives_keep_provenance [function]` (`69f4c775-a8b9-5257-8d30-c4b1054bdb4b`) lines 886-922 [crates/gwiki/src/ingest/video/tests.rs:886-922]
  - Signature: `fn video_derivatives_keep_provenance() {`
  - Purpose: Tests that `ingest_video()` preserves provenance metadata including source references, scope identity, video frame sampling intervals, and transcript-to-frame alignment information in the resulting SourceNote document. [crates/gwiki/src/ingest/video/tests.rs:886-922]

