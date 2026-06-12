---
title: crates/gwiki/src/ingest/video/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/video/tests.rs
  ranges:
  - 18-55
  - 57-62
  - 64-89
  - 91-111
  - '113'
  - 115-131
  - '133'
  - 135-144
  - '146'
  - 148-160
  - '162'
  - 164-170
  - 172-198
  - 201-273
  - 276-323
  - 326-329
  - 332-350
  - 354-446
  - 449-451
  - 454-461
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
  - Purpose: Constructs and returns a `VideoSnapshot` instance with mock data representing an 8-second MP4 lecture video, including predefined frame descriptions at 4-second intervals and time-aligned transcript segments. [crates/gwiki/src/ingest/video/tests.rs:18-55]
- `FakeVideoMediaExtractor` (class) component `FakeVideoMediaExtractor [class]` (`bc0764a2-32f9-571e-87ee-d99e82f20ccc`) lines 57-62 [crates/gwiki/src/ingest/video/tests.rs:57-62]
  - Signature: `struct FakeVideoMediaExtractor {`
  - Purpose: `FakeVideoMediaExtractor` is a test mock struct that stores raw audio bytes and timestamped video frames while supporting injectable failure conditions for testing extraction error scenarios. [crates/gwiki/src/ingest/video/tests.rs:57-62]
- `FakeVideoMediaExtractor` (class) component `FakeVideoMediaExtractor [class]` (`a0a23429-0424-57a3-b5fd-13ea091bbfdd`) lines 64-89 [crates/gwiki/src/ingest/video/tests.rs:64-89]
  - Signature: `impl VideoMediaExtractor for FakeVideoMediaExtractor {`
  - Purpose: FakeVideoMediaExtractor is a test mock implementation of VideoMediaExtractor that returns pre-configured audio and frame image bytes as temporary files, with optional configurable failure injection. [crates/gwiki/src/ingest/video/tests.rs:64-89]
- `FakeVideoMediaExtractor.extract_audio` (method) component `FakeVideoMediaExtractor.extract_audio [method]` (`6fe6a29e-fafe-53be-b386-2eeb025e3a01`) lines 65-72 [crates/gwiki/src/ingest/video/tests.rs:65-72]
  - Signature: `fn extract_audio(&self, _video: &Path) -> Result<tempfile::NamedTempFile, WikiError> {`
  - Purpose: This method creates and returns a temporary WAV file containing pre-stored audio bytes, or fails with a configuration error if the `fail_audio` flag is set. [crates/gwiki/src/ingest/video/tests.rs:65-72]
- `FakeVideoMediaExtractor.sample_frame_images` (method) component `FakeVideoMediaExtractor.sample_frame_images [method]` (`9146306b-2686-5e09-b94b-d5b169eb23dc`) lines 74-88 [crates/gwiki/src/ingest/video/tests.rs:74-88]
  - Signature: `fn sample_frame_images(`
  - Purpose: Returns pre-computed JPEG frames as temporary files paired with their start timestamps in milliseconds, or fails with a ConfigError if frame sampling is marked as failed. [crates/gwiki/src/ingest/video/tests.rs:74-88]
- `temp_file_with_bytes` (function) component `temp_file_with_bytes [function]` (`a3834ae2-950b-523b-92bb-d69eb0d6195a`) lines 91-111 [crates/gwiki/src/ingest/video/tests.rs:91-111]
  - Signature: `fn temp_file_with_bytes(suffix: &str, bytes: &[u8]) -> Result<tempfile::NamedTempFile, WikiError> {`
  - Purpose: Creates a temporary file with the specified suffix, writes the provided bytes to it, flushes the buffer, and returns the `NamedTempFile` or a `WikiError` if any I/O operation fails. [crates/gwiki/src/ingest/video/tests.rs:91-111]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`8a5f752e-85ed-5180-b3fe-34068e4b3548`) lines 113-113 [crates/gwiki/src/ingest/video/tests.rs:113]
  - Signature: `struct FakeTranscriptionClient;`
  - Purpose: FakeTranscriptionClient is a mock struct implementation of a transcription client used for testing purposes. [crates/gwiki/src/ingest/video/tests.rs:113]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`7634aaa1-d856-536e-985b-11ab648dec09`) lines 115-131 [crates/gwiki/src/ingest/video/tests.rs:115-131]
  - Signature: `impl TranscriptionClient for FakeTranscriptionClient {`
  - Purpose: FakeTranscriptionClient is a test double implementing TranscriptionClient that returns a hardcoded English transcription with a single segment spanning 1000-2000 milliseconds. [crates/gwiki/src/ingest/video/tests.rs:115-131]
- `FakeTranscriptionClient.transcribe` (method) component `FakeTranscriptionClient.transcribe [method]` (`c2f5b665-933d-5f81-afa2-fc56cebe3e4b`) lines 116-130 [crates/gwiki/src/ingest/video/tests.rs:116-130]
  - Signature: `fn transcribe(`
  - Purpose: Returns a mock transcription result in English with a hardcoded 1000-2000ms timestamp range and static audio-first transcript text, ignoring the input request. [crates/gwiki/src/ingest/video/tests.rs:116-130]
- `FailingTranscriptionClient` (class) component `FailingTranscriptionClient [class]` (`c6035b26-69a5-5b46-a077-07fedb3d4c87`) lines 133-133 [crates/gwiki/src/ingest/video/tests.rs:133]
  - Signature: `struct FailingTranscriptionClient;`
  - Purpose: `FailingTranscriptionClient` is a zero-sized unit struct serving as a mock transcription client designed to simulate or test failure behavior. [crates/gwiki/src/ingest/video/tests.rs:133]
- `FailingTranscriptionClient` (class) component `FailingTranscriptionClient [class]` (`2b5129ed-040c-551b-8d54-da41506f32e7`) lines 135-144 [crates/gwiki/src/ingest/video/tests.rs:135-144]
  - Signature: `impl TranscriptionClient for FailingTranscriptionClient {`
  - Purpose: FailingTranscriptionClient implements TranscriptionClient to unconditionally return a `WikiError::Config` indicating speech-to-text provider failure. [crates/gwiki/src/ingest/video/tests.rs:135-144]
- `FailingTranscriptionClient.transcribe` (method) component `FailingTranscriptionClient.transcribe [method]` (`074f384b-69b7-5eb6-bba7-e0bb059f81f0`) lines 136-143 [crates/gwiki/src/ingest/video/tests.rs:136-143]
  - Signature: `fn transcribe(`
  - Purpose: This method unconditionally returns a `WikiError::Config` error indicating that the speech-to-text provider failed, ignoring the input `TranscriptionRequest`. [crates/gwiki/src/ingest/video/tests.rs:136-143]
- `FakeVisionClient` (class) component `FakeVisionClient [class]` (`0bd60ab9-5261-536e-a80e-788ea3c857c5`) lines 146-146 [crates/gwiki/src/ingest/video/tests.rs:146]
  - Signature: `struct FakeVisionClient;`
  - Purpose: FakeVisionClient is a mock struct that serves as a test double for a vision client implementation. [crates/gwiki/src/ingest/video/tests.rs:146]
- `FakeVisionClient` (class) component `FakeVisionClient [class]` (`a603bcad-4fcd-54f2-81b2-5ba9b97a405a`) lines 148-160 [crates/gwiki/src/ingest/video/tests.rs:148-160]
  - Signature: `impl VisionClient for FakeVisionClient {`
  - Purpose: `FakeVisionClient` is a mock implementation of the `VisionClient` trait that returns a stubbed `VisionExtraction` containing only a formatted description of the input frame's filename and byte size, with no OCR text or metadata. [crates/gwiki/src/ingest/video/tests.rs:148-160]
- `FakeVisionClient.extract` (method) component `FakeVisionClient.extract [method]` (`79609895-2dcb-52d1-9033-b874fb68b239`) lines 149-159 [crates/gwiki/src/ingest/video/tests.rs:149-159]
  - Signature: `fn extract(&self, request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: Returns a `VisionExtraction` containing only the request's filename and byte count, with no OCR text or metadata. [crates/gwiki/src/ingest/video/tests.rs:149-159]
- `FailingVisionClient` (class) component `FailingVisionClient [class]` (`b104f54a-e209-5f01-bcc7-d4d1bf64f502`) lines 162-162 [crates/gwiki/src/ingest/video/tests.rs:162]
  - Signature: `struct FailingVisionClient;`
  - Purpose: # FailingVisionClient

A zero-sized Rust struct providing a mock vision client implementation designed to fail operations for testing purposes. [crates/gwiki/src/ingest/video/tests.rs:162]
- `FailingVisionClient` (class) component `FailingVisionClient [class]` (`de4eecf8-ad8d-5b21-9473-0a4eb960ea34`) lines 164-170 [crates/gwiki/src/ingest/video/tests.rs:164-170]
  - Signature: `impl VisionClient for FailingVisionClient {`
  - Purpose: `FailingVisionClient` is a `VisionClient` implementation that unconditionally returns a `WikiError::Config` with the message "vision provider failed" from its `extract` method. [crates/gwiki/src/ingest/video/tests.rs:164-170]
- `FailingVisionClient.extract` (method) component `FailingVisionClient.extract [method]` (`4bc6d4ed-8301-5a02-90e9-be584007143c`) lines 165-169 [crates/gwiki/src/ingest/video/tests.rs:165-169]
  - Signature: `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: The `extract` method is a stub that unconditionally returns a `WikiError::Config` error with the detail message "vision provider failed", regardless of the input `VisionRequest`. [crates/gwiki/src/ingest/video/tests.rs:165-169]
- `transcript_output` (function) component `transcript_output [function]` (`547464b0-b252-56cc-a798-5164906d7626`) lines 172-198 [crates/gwiki/src/ingest/video/tests.rs:172-198]
  - Signature: `fn transcript_output(`
  - Purpose: Converts millisecond-bounded text segments into a structured TranscriptionOutput with source language metadata and conditional English target language assignment based on the translation flag. [crates/gwiki/src/ingest/video/tests.rs:172-198]
- `video_produces_transcript_and_frames` (function) component `video_produces_transcript_and_frames [function]` (`e9605554-53ea-5ac0-b5dc-c3b7f3949db5`) lines 201-273 [crates/gwiki/src/ingest/video/tests.rs:201-273]
  - Signature: `fn video_produces_transcript_and_frames() {`
  - Purpose: This test verifies that video file ingestion with transcription and vision processing produces transcript-aligned frame samples with correct asset path references. [crates/gwiki/src/ingest/video/tests.rs:201-273]
- `frame_interval_zero_disables_frames` (function) component `frame_interval_zero_disables_frames [function]` (`ae72fad5-9e80-5735-9934-af36d7695c41`) lines 276-323 [crates/gwiki/src/ingest/video/tests.rs:276-323]
  - Signature: `fn frame_interval_zero_disables_frames() {`
  - Purpose: This test verifies that setting `frame_interval_seconds` to zero disables video frame sampling and all frame-related processing (frame samples, images, descriptions) while preserving audio transcription during media ingestion. [crates/gwiki/src/ingest/video/tests.rs:276-323]
- `ScriptedTranscriptionClient` (class) component `ScriptedTranscriptionClient [class]` (`f34e3ae0-b8f4-53d2-8da9-44382bf277dc`) lines 326-329 [crates/gwiki/src/ingest/video/tests.rs:326-329]
  - Signature: `struct ScriptedTranscriptionClient {`
  - Purpose: ScriptedTranscriptionClient is a mock transcription client that stores pre-scripted transcription results and records method invocations through interior-mutable RefCell and reference-counted Rc state containers. [crates/gwiki/src/ingest/video/tests.rs:326-329]
- `ScriptedTranscriptionClient` (class) component `ScriptedTranscriptionClient [class]` (`02593ae8-1a2f-50d9-82a1-1dea8d53fdc2`) lines 332-350 [crates/gwiki/src/ingest/video/tests.rs:332-350]
  - Signature: `impl TranscriptionClient for ScriptedTranscriptionClient {`
  - Purpose: **ScriptedTranscriptionClient is a test mock that rejects transcription operations and returns pre-queued English translations while recording method invocations.** [crates/gwiki/src/ingest/video/tests.rs:332-350]
- `ScriptedTranscriptionClient.transcribe` (method) component `ScriptedTranscriptionClient.transcribe [method]` (`847c1a28-b1ce-5592-ab9f-5825914b7c91`) lines 333-340 [crates/gwiki/src/ingest/video/tests.rs:333-340]
  - Signature: `fn transcribe(`
  - Purpose: This method is a fallback stub that unconditionally returns a `WikiError::Config` with the message "unexpected transcribe fallback", indicating that transcription requests should not reach this implementation. [crates/gwiki/src/ingest/video/tests.rs:333-340]
- `ScriptedTranscriptionClient.translate_to_english` (method) component `ScriptedTranscriptionClient.translate_to_english [method]` (`71cd094a-16cc-5dd6-8843-fc486168dab4`) lines 342-349 [crates/gwiki/src/ingest/video/tests.rs:342-349]
  - Signature: `fn translate_to_english(`
  - Purpose: This mock method records the invocation in a call tracker and dequeues the first pre-queued `Result<TranscriptionOutput, WikiError>` from an internal collection, ignoring the request and language hint parameters. [crates/gwiki/src/ingest/video/tests.rs:342-349]
- `video_long_english_translation_reuses_chunk_branch` (function) component `video_long_english_translation_reuses_chunk_branch [function]` (`0aa4f156-daae-5d72-a3f8-b83095fb513b`) lines 354-446 [crates/gwiki/src/ingest/video/tests.rs:354-446]
  - Signature: `fn video_long_english_translation_reuses_chunk_branch() {`
  - Purpose: This test validates the video ingestion pipeline's handling of overlapping audio chunks during English translation, verifying correct behavior when audio exceeds upload size limits and chunk transcription partially fails. [crates/gwiki/src/ingest/video/tests.rs:354-446]
- `ScriptedChunkTranscriptionClient` (class) component `ScriptedChunkTranscriptionClient [class]` (`1464dc9d-e3b8-54c1-94bb-7c970a24ae49`) lines 449-451 [crates/gwiki/src/ingest/video/tests.rs:449-451]
  - Signature: `struct ScriptedChunkTranscriptionClient {`
  - Purpose: `ScriptedChunkTranscriptionClient` is a struct that encapsulates interior-mutable storage for a dynamically-sized vector of transcription results, each being either a `TranscriptionOutput` success or a `WikiError` failure. [crates/gwiki/src/ingest/video/tests.rs:449-451]
- `ScriptedChunkTranscriptionClient` (class) component `ScriptedChunkTranscriptionClient [class]` (`0eb69051-4979-5da3-b89a-8d20dcec381b`) lines 454-461 [crates/gwiki/src/ingest/video/tests.rs:454-461]
  - Signature: `impl TranscriptionClient for ScriptedChunkTranscriptionClient {`
  - Purpose: A `TranscriptionClient` implementation that sequentially returns pre-queued `TranscriptionOutput` values in FIFO order, disregarding the actual input request. [crates/gwiki/src/ingest/video/tests.rs:454-461]
- `ScriptedChunkTranscriptionClient.transcribe` (method) component `ScriptedChunkTranscriptionClient.transcribe [method]` (`616c329d-4177-548a-b3ea-acc4b7d7a671`) lines 455-460 [crates/gwiki/src/ingest/video/tests.rs:455-460]
  - Signature: `fn transcribe(`
  - Purpose: Removes and returns the first element from an internally mutable outputs collection, ignoring the provided TranscriptionRequest parameter. [crates/gwiki/src/ingest/video/tests.rs:455-460]
- `production_ingest_applies_degradation_matrix` (function) component `production_ingest_applies_degradation_matrix [function]` (`8cf190f9-bad1-5a10-bc1a-1e9f953f3aa6`) lines 464-617 [crates/gwiki/src/ingest/video/tests.rs:464-617]
  - Signature: `fn production_ingest_applies_degradation_matrix() {`
  - Purpose: This test validates that the production media ingestion pipeline correctly applies a degradation matrix by verifying graceful degradation when video processing components (ffmpeg, frame extraction, vision) fail, while preserving the original asset and recording specific failures in derived metadata. [crates/gwiki/src/ingest/video/tests.rs:464-617]
- `video_media_degradation_classifies_only_unavailable_ffmpeg_errors` (function) component `video_media_degradation_classifies_only_unavailable_ffmpeg_errors [function]` (`0cf6073c-f8fc-50a3-9a1a-0b48baa93ec4`) lines 620-638 [crates/gwiki/src/ingest/video/tests.rs:620-638]
  - Signature: `fn video_media_degradation_classifies_only_unavailable_ffmpeg_errors() {`
  - Purpose: This test verifies that `video_media_degradation` classifies only the missing ffmpeg executable error as `ffmpeg_unavailable`, while other ffmpeg extraction failures are classified as `extraction_failed`. [crates/gwiki/src/ingest/video/tests.rs:620-638]
- `frame_vision_failure_keeps_sample_without_description` (function) component `frame_vision_failure_keeps_sample_without_description [function]` (`dd3d356f-1fcf-55b8-bad0-1fbb2a9cd1d5`) lines 641-656 [crates/gwiki/src/ingest/video/tests.rs:641-656]
  - Signature: `fn frame_vision_failure_keeps_sample_without_description() {`
  - Purpose: Verifies that `describe_frame_images` persists frame samples with empty descriptions when the vision endpoint fails. [crates/gwiki/src/ingest/video/tests.rs:641-656]
- `persisted_frame_sources_are_removed_after_successful_loop` (function) component `persisted_frame_sources_are_removed_after_successful_loop [function]` (`f1e9a1f7-f166-5142-ac72-764d7ee39ff2`) lines 659-707 [crates/gwiki/src/ingest/video/tests.rs:659-707]
  - Signature: `fn persisted_frame_sources_are_removed_after_successful_loop() {`
  - Purpose: Tests that temporary video frame source files are deleted after successfully persisting their content to the vault via `persist_video_frame_assets()`. [crates/gwiki/src/ingest/video/tests.rs:659-707]
- `persisted_frame_read_failure_drops_remaining_kept_temp_frames` (function) component `persisted_frame_read_failure_drops_remaining_kept_temp_frames [function]` (`a5edac93-13d8-5d97-8a14-c3f378fed35c`) lines 710-765 [crates/gwiki/src/ingest/video/tests.rs:710-765]
  - Signature: `fn persisted_frame_read_failure_drops_remaining_kept_temp_frames() {`
  - Purpose: Tests that when persisting video frame assets fails due to an unreadable frame asset, any retained temporary frame files are properly cleaned up. [crates/gwiki/src/ingest/video/tests.rs:710-765]
- `ingest_with_media` (function) component `ingest_with_media [function]` (`14dc0b77-aa41-552a-8225-43d99624d4cb`) lines 767-799 [crates/gwiki/src/ingest/video/tests.rs:767-799]
  - Signature: `fn ingest_with_media(`
  - Purpose: Creates a video file snapshot with mock source data and metadata, then delegates to `ingest_video_file_with_processing` to extract transcription and visual information via provided endpoints. [crates/gwiki/src/ingest/video/tests.rs:767-799]
- `read_derived` (function) component `read_derived [function]` (`c07db945-5200-5fa4-9820-a9f82b6d1b50`) lines 801-803 [crates/gwiki/src/ingest/video/tests.rs:801-803]
  - Signature: `fn read_derived(vault_root: &Path, result: &VideoIngestResult) -> String {`
  - Purpose: Reads the contents of a derived video file located at the path constructed by joining the vault root with the `derived_path` field from a `VideoIngestResult`, panicking if the read fails. [crates/gwiki/src/ingest/video/tests.rs:801-803]
- `assert_asset_preserved` (function) component `assert_asset_preserved [function]` (`3d56c967-3261-504b-adaa-7baee72ec3b3`) lines 805-810 [crates/gwiki/src/ingest/video/tests.rs:805-810]
  - Signature: `fn assert_asset_preserved(vault_root: &Path, result: &VideoIngestResult, expected: &[u8]) {`
  - Purpose: Asserts that a video asset file read from the vault filesystem matches the expected byte contents. [crates/gwiki/src/ingest/video/tests.rs:805-810]
- `stores_original_video` (function) component `stores_original_video [function]` (`ebd3a24f-e915-5078-a16a-46c06578e2e3`) lines 813-843 [crates/gwiki/src/ingest/video/tests.rs:813-843]
  - Signature: `fn stores_original_video() {`
  - Purpose: This test verifies that `ingest_video()` correctly persists the original video file to the filesystem, generates markdown metadata with video properties, and creates a source manifest entry with matching content hash. [crates/gwiki/src/ingest/video/tests.rs:813-843]
- `stores_file_backed_video` (function) component `stores_file_backed_video [function]` (`20cdcda4-4cc2-5909-88a4-4b3e55563ae5`) lines 846-883 [crates/gwiki/src/ingest/video/tests.rs:846-883]
  - Signature: `fn stores_file_backed_video() {`
  - Purpose: This test verifies that `ingest_video_file` correctly preserves file-backed video content, records accurate content hashes in the source manifest, and registers the derived source in the memory store. [crates/gwiki/src/ingest/video/tests.rs:846-883]
- `video_derivatives_keep_provenance` (function) component `video_derivatives_keep_provenance [function]` (`f5a59646-decf-5327-80f2-95c90cd74d8e`) lines 886-922 [crates/gwiki/src/ingest/video/tests.rs:886-922]
  - Signature: `fn video_derivatives_keep_provenance() {`
  - Purpose: Verifies that video ingestion produces a SourceNote document preserving complete provenance metadata including source asset paths, project scope identity, frame sampling interval, and transcription segment alignment information. [crates/gwiki/src/ingest/video/tests.rs:886-922]

