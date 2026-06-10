---
title: crates/gwiki/src/transcribe.rs
type: code_file
provenance:
- file: crates/gwiki/src/transcribe.rs
  ranges:
  - 12-16
  - 19-22
  - 25-37
  - 40-43
  - 45-71
  - 51-59
  - 61-70
  - 74-79
  - 81-89
  - 92-95
  - 98-101
  - 103-138
  - 140-164
  - 166-193
  - 195-214
  - 216-346
  - 348-354
  - 356-362
  - 371-373
  - 375-406
  - 376-405
  - 408-424
  - 427-483
  - 486-545
  - 548-585
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/transcribe.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/transcribe.rs` exposes 25 indexed API symbols.
[crates/gwiki/src/transcribe.rs:12-16]
[crates/gwiki/src/transcribe.rs:19-22]
[crates/gwiki/src/transcribe.rs:25-37]
[crates/gwiki/src/transcribe.rs:40-43]
[crates/gwiki/src/transcribe.rs:45-71]
[crates/gwiki/src/transcribe.rs:51-59]
[crates/gwiki/src/transcribe.rs:61-70]
[crates/gwiki/src/transcribe.rs:74-79]
[crates/gwiki/src/transcribe.rs:81-89]
[crates/gwiki/src/transcribe.rs:92-95]
[crates/gwiki/src/transcribe.rs:98-101]
[crates/gwiki/src/transcribe.rs:103-138]
[crates/gwiki/src/transcribe.rs:140-164]
[crates/gwiki/src/transcribe.rs:166-193]
[crates/gwiki/src/transcribe.rs:195-214]
[crates/gwiki/src/transcribe.rs:216-346]
[crates/gwiki/src/transcribe.rs:348-354]
[crates/gwiki/src/transcribe.rs:356-362]
[crates/gwiki/src/transcribe.rs:371-373]
[crates/gwiki/src/transcribe.rs:375-406]
[crates/gwiki/src/transcribe.rs:376-405]
[crates/gwiki/src/transcribe.rs:408-424]
[crates/gwiki/src/transcribe.rs:427-483]
[crates/gwiki/src/transcribe.rs:486-545]
[crates/gwiki/src/transcribe.rs:548-585]

## API Symbols

- `TranscriptSegment` (class) component `TranscriptSegment [class]` (`d49718ee-5325-59b8-8dc3-487d2fc19f71`) lines 12-16 [crates/gwiki/src/transcribe.rs:12-16]
  - Signature: `pub struct TranscriptSegment {`
  - Purpose: `TranscriptSegment` is a struct that represents a time-bounded segment of transcribed text, defined by millisecond-precision start and end timestamps with associated text content. [crates/gwiki/src/transcribe.rs:12-16]
- `TranscriptionRange` (class) component `TranscriptionRange [class]` (`84cb7686-5bbd-5688-9d03-6bb0385017cf`) lines 19-22 [crates/gwiki/src/transcribe.rs:19-22]
  - Signature: `pub struct TranscriptionRange {`
  - Purpose: `TranscriptionRange` is a public struct that defines a time interval for transcription data using two u64 fields representing start and end positions in milliseconds. [crates/gwiki/src/transcribe.rs:19-22]
- `TranscriptionOutput` (class) component `TranscriptionOutput [class]` (`ada2bef7-e696-583f-bf44-0602f2f8c2ed`) lines 25-37 [crates/gwiki/src/transcribe.rs:25-37]
  - Signature: `pub struct TranscriptionOutput {`
  - Purpose: TranscriptionOutput is a struct that encapsulates transcribed audio segments with optional language and translation metadata, status flags indicating partial completion and translation degradation, and range-based tracking of processed versus missing audio intervals. [crates/gwiki/src/transcribe.rs:25-37]
- `TranscriptionDegradation` (class) component `TranscriptionDegradation [class]` (`ec999007-75bd-58da-8dc6-3d0c57444595`) lines 40-43 [crates/gwiki/src/transcribe.rs:40-43]
  - Signature: `pub struct TranscriptionDegradation {`
  - Purpose: `TranscriptionDegradation` is a struct that encapsulates a failure reason and fallback string for degraded or failed transcription operations. [crates/gwiki/src/transcribe.rs:40-43]
- `TranscriptionClient` (type) component `TranscriptionClient [type]` (`e3467c41-9ce4-5337-920b-d8505743e3fd`) lines 45-71 [crates/gwiki/src/transcribe.rs:45-71]
  - Signature: `pub trait TranscriptionClient {`
  - Purpose: Indexed type `TranscriptionClient` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:45-71]
- `TranscriptionClient.translate_to_english` (method) component `TranscriptionClient.translate_to_english [method]` (`2c8af3ed-b682-5053-b85d-4c90aa4ea1cd`) lines 51-59 [crates/gwiki/src/transcribe.rs:51-59]
  - Signature: `fn translate_to_english(`
  - Purpose: Stub method that unconditionally returns a `WikiError::Config` indicating audio translation functionality is not configured. [crates/gwiki/src/transcribe.rs:51-59]
- `TranscriptionClient.translate_segments` (method) component `TranscriptionClient.translate_segments [method]` (`36618428-521e-5c1d-bc2b-a3f9d009b291`) lines 61-70 [crates/gwiki/src/transcribe.rs:61-70]
  - Signature: `fn translate_segments(`
  - Purpose: A stub implementation that unconditionally returns a `WikiError::Config` to indicate text translation functionality is not configured. [crates/gwiki/src/transcribe.rs:61-70]
- `TranscriptionRequest` (class) component `TranscriptionRequest [class]` (`77623651-d2bf-5ee5-8bc7-fc569336d214`) lines 74-79 [crates/gwiki/src/transcribe.rs:74-79]
  - Signature: `pub struct TranscriptionRequest<'a> {`
  - Purpose: TranscriptionRequest is a lifetime-bound struct that encapsulates borrowed references to file metadata (name, MIME type, path) and raw byte content for audio transcription operations. [crates/gwiki/src/transcribe.rs:74-79]
- `TranscriptionEndpoint` (type) component `TranscriptionEndpoint [type]` (`035c599b-8e9d-528f-9e0a-52f8353c3710`) lines 81-89 [crates/gwiki/src/transcribe.rs:81-89]
  - Signature: `pub enum TranscriptionEndpoint<'a> {`
  - Purpose: Indexed type `TranscriptionEndpoint` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:81-89]
- `TranscriptionMarkdownResult` (class) component `TranscriptionMarkdownResult [class]` (`0b81dbea-7523-591d-ad3d-0d400d9fc107`) lines 92-95 [crates/gwiki/src/transcribe.rs:92-95]
  - Signature: `pub struct TranscriptionMarkdownResult {`
  - Purpose: `TranscriptionMarkdownResult` is a struct that represents the result of a transcription-to-markdown operation, containing the output file path and optional quality degradation metadata. [crates/gwiki/src/transcribe.rs:92-95]
- `TranscriptionMarkdownInput` (type) component `TranscriptionMarkdownInput [type]` (`d248c529-78b8-5dff-ab9b-c210afe4ea90`) lines 98-101 [crates/gwiki/src/transcribe.rs:98-101]
  - Signature: `pub enum TranscriptionMarkdownInput {`
  - Purpose: Indexed type `TranscriptionMarkdownInput` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:98-101]
- `write_audio_transcript_markdown` (function) component `write_audio_transcript_markdown [function]` (`2ef41e6f-9679-5994-858a-a82f38f73b5f`) lines 103-138 [crates/gwiki/src/transcribe.rs:103-138]
  - Signature: `pub fn write_audio_transcript_markdown(`
  - Purpose: Renders and atomically writes audio transcript markdown to a vault-derived path, supporting both successful transcription and degradation fallback inputs while creating necessary parent directories. [crates/gwiki/src/transcribe.rs:103-138]
- `write_transcript_markdown_atomically` (function) component `write_transcript_markdown_atomically [function]` (`d58e9901-21bd-519d-ac06-10ec045feb11`) lines 140-164 [crates/gwiki/src/transcribe.rs:140-164]
  - Signature: `fn write_transcript_markdown_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Atomically writes transcript markdown content to a file by writing to a temporary file, syncing to disk, atomically renaming it to the target path, and syncing the parent directory. [crates/gwiki/src/transcribe.rs:140-164]
- `create_transcript_temp_file` (function) component `create_transcript_temp_file [function]` (`78991398-e465-52fb-963d-2c174bf1b0ed`) lines 166-193 [crates/gwiki/src/transcribe.rs:166-193]
  - Signature: `fn create_transcript_temp_file(path: &Path) -> Result<NamedTempFile, WikiError> {`
  - Purpose: Creates a named temporary file in the parent directory of the given path with a naming scheme of `.{originalfilename}.tmp`, returning either the `NamedTempFile` or a `WikiError` on failure. [crates/gwiki/src/transcribe.rs:166-193]
- `sync_parent_dir` (function) component `sync_parent_dir [function]` (`48529d42-ae55-5348-95b5-5159dbe18ce3`) lines 195-214 [crates/gwiki/src/transcribe.rs:195-214]
  - Signature: `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: On Unix systems, fsync-flushes the parent directory of the given path to persist directory metadata to disk; returns a `WikiError` on I/O failure or is a no-op on non-Unix systems. [crates/gwiki/src/transcribe.rs:195-214]
- `render_audio_transcript_markdown` (function) component `render_audio_transcript_markdown [function]` (`08afca78-922a-529a-a171-cff14243b5e4`) lines 216-346 [crates/gwiki/src/transcribe.rs:216-346]
  - Signature: `fn render_audio_transcript_markdown(`
  - Purpose: # Summary

`render_audio_transcript_markdown` constructs and returns a markdown string containing aggregated metadata fields for an audio file, its transcription status, and associated source/scope information. [crates/gwiki/src/transcribe.rs:216-346]
- `format_timestamp_ms` (function) component `format_timestamp_ms [function]` (`d146c789-f60c-50d1-8e50-f47729972a67`) lines 348-354 [crates/gwiki/src/transcribe.rs:348-354]
  - Signature: `fn format_timestamp_ms(timestamp_ms: u64) -> String {`
  - Purpose: Converts a millisecond timestamp to a zero-padded HH:MM:SS duration string. [crates/gwiki/src/transcribe.rs:348-354]
- `format_ranges_ms` (function) component `format_ranges_ms [function]` (`e21bb638-9262-5168-ab38-8c6b856bd87e`) lines 356-362 [crates/gwiki/src/transcribe.rs:356-362]
  - Signature: `fn format_ranges_ms(ranges: &[TranscriptionRange]) -> String {`
  - Purpose: Converts a slice of `TranscriptionRange` objects into a comma-separated string where each range is formatted as `start_ms-end_ms`. [crates/gwiki/src/transcribe.rs:356-362]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`35b75b6f-8833-5927-96e0-8bc4353a4730`) lines 371-373 [crates/gwiki/src/transcribe.rs:371-373]
  - Signature: `struct FakeTranscriptionClient {`
  - Purpose: `FakeTranscriptionClient` is a mock struct that uses interior-mutable `Cell<usize>` to track the number of transcription client method invocations without requiring a mutable reference. [crates/gwiki/src/transcribe.rs:371-373]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`2ac604e4-e64a-5fdd-8bce-672fd064bd1a`) lines 375-406 [crates/gwiki/src/transcribe.rs:375-406]
  - Signature: `impl TranscriptionClient for FakeTranscriptionClient {`
  - Purpose: FakeTranscriptionClient is a test double implementing TranscriptionClient that increments a call counter and returns a deterministic TranscriptionOutput with two hardcoded English transcript segments for unit testing purposes. [crates/gwiki/src/transcribe.rs:375-406]
- `FakeTranscriptionClient.transcribe` (method) component `FakeTranscriptionClient.transcribe [method]` (`c17e17a6-c969-51e1-8628-6fb96f9a0534`) lines 376-405 [crates/gwiki/src/transcribe.rs:376-405]
  - Signature: `fn transcribe(`
  - Purpose: This method is a stub transcription handler that returns a hardcoded `TranscriptionOutput` with two timestamped text segments while incrementing an internal call counter. [crates/gwiki/src/transcribe.rs:376-405]
- `record_for` (function) component `record_for [function]` (`90f980ab-3199-5b4a-85c1-77193de8d5b4`) lines 408-424 [crates/gwiki/src/transcribe.rs:408-424]
  - Signature: `fn record_for(temp: &Path) -> SourceRecord {`
  - Purpose: Registers a manually-ingested audio source with pending compile status to the SourceManifest at the specified path and returns the resulting SourceRecord, panicking if registration fails. [crates/gwiki/src/transcribe.rs:408-424]
- `writes_timestamped_transcript` (function) component `writes_timestamped_transcript [function]` (`f3a55a01-d749-5f91-8d36-e57275457949`) lines 427-483 [crates/gwiki/src/transcribe.rs:427-483]
  - Signature: `fn writes_timestamped_transcript() {`
  - Purpose: This test verifies that `write_audio_transcript_markdown()` correctly generates a markdown file containing timestamped transcription entries with proper scope and source metadata for a transcribed audio asset. [crates/gwiki/src/transcribe.rs:427-483]
- `renders_precomputed_output_without_transcribing` (function) component `renders_precomputed_output_without_transcribing [function]` (`b0ab1d21-369e-5f20-a6e5-f0e7d1ef4520`) lines 486-545 [crates/gwiki/src/transcribe.rs:486-545]
  - Signature: `fn renders_precomputed_output_without_transcribing() {`
  - Purpose: Indexed function `renders_precomputed_output_without_transcribing` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:486-545]
- `missing_transcription_degrades` (function) component `missing_transcription_degrades [function]` (`b6936faf-984f-516e-9fe8-40c880b7b29f`) lines 548-585 [crates/gwiki/src/transcribe.rs:548-585]
  - Signature: `fn missing_transcription_degrades() {`
  - Purpose: Indexed function `missing_transcription_degrades` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:548-585]

