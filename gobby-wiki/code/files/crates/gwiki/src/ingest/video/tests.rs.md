---
title: crates/gwiki/src/ingest/video/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/video/tests.rs
  ranges:
  - 25-62
  - 64-69
  - 72-79
  - 81-95
  - 98-118
  - '120'
  - 123-137
  - '140'
  - 143-150
  - '153'
  - 156-166
  - '169'
  - 172-176
  - 179-205
  - 208-211
  - 215-222
  - 224-231
  - 235-237
  - 241-246
  - 249-281
  - 283-285
  - 287-292
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/video/tests.rs:25-62](crates/gwiki/src/ingest/video/tests.rs#L25-L62), [crates/gwiki/src/ingest/video/tests.rs:64-69](crates/gwiki/src/ingest/video/tests.rs#L64-L69), [crates/gwiki/src/ingest/video/tests.rs:72-79](crates/gwiki/src/ingest/video/tests.rs#L72-L79), [crates/gwiki/src/ingest/video/tests.rs:81-95](crates/gwiki/src/ingest/video/tests.rs#L81-L95), [crates/gwiki/src/ingest/video/tests.rs:98-118](crates/gwiki/src/ingest/video/tests.rs#L98-L118), [crates/gwiki/src/ingest/video/tests.rs:120](crates/gwiki/src/ingest/video/tests.rs#L120), [crates/gwiki/src/ingest/video/tests.rs:123-137](crates/gwiki/src/ingest/video/tests.rs#L123-L137), [crates/gwiki/src/ingest/video/tests.rs:140](crates/gwiki/src/ingest/video/tests.rs#L140), [crates/gwiki/src/ingest/video/tests.rs:143-150](crates/gwiki/src/ingest/video/tests.rs#L143-L150), [crates/gwiki/src/ingest/video/tests.rs:153](crates/gwiki/src/ingest/video/tests.rs#L153), [crates/gwiki/src/ingest/video/tests.rs:156-166](crates/gwiki/src/ingest/video/tests.rs#L156-L166), [crates/gwiki/src/ingest/video/tests.rs:169](crates/gwiki/src/ingest/video/tests.rs#L169), [crates/gwiki/src/ingest/video/tests.rs:172-176](crates/gwiki/src/ingest/video/tests.rs#L172-L176), [crates/gwiki/src/ingest/video/tests.rs:179-205](crates/gwiki/src/ingest/video/tests.rs#L179-L205), [crates/gwiki/src/ingest/video/tests.rs:208-211](crates/gwiki/src/ingest/video/tests.rs#L208-L211), [crates/gwiki/src/ingest/video/tests.rs:215-222](crates/gwiki/src/ingest/video/tests.rs#L215-L222), [crates/gwiki/src/ingest/video/tests.rs:224-231](crates/gwiki/src/ingest/video/tests.rs#L224-L231), [crates/gwiki/src/ingest/video/tests.rs:235-237](crates/gwiki/src/ingest/video/tests.rs#L235-L237), [crates/gwiki/src/ingest/video/tests.rs:241-246](crates/gwiki/src/ingest/video/tests.rs#L241-L246), [crates/gwiki/src/ingest/video/tests.rs:249-281](crates/gwiki/src/ingest/video/tests.rs#L249-L281), [crates/gwiki/src/ingest/video/tests.rs:283-285](crates/gwiki/src/ingest/video/tests.rs#L283-L285), [crates/gwiki/src/ingest/video/tests.rs:287-292](crates/gwiki/src/ingest/video/tests.rs#L287-L292)

</details>

# crates/gwiki/src/ingest/video/tests.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Purpose

Test support for the video ingestion pipeline. It builds a representative `VideoSnapshot`, temporary media files, and a set of fake or scripted media, transcription, and vision clients to drive success and failure cases without real AI backends. The helpers and fixtures are used by the nested test modules to exercise ingestion with extracted audio, sampled frames, transcript output, derived artifact reading, and asset-preservation assertions.
[crates/gwiki/src/ingest/video/tests.rs:25-62]
[crates/gwiki/src/ingest/video/tests.rs:64-69]
[crates/gwiki/src/ingest/video/tests.rs:72-79]
[crates/gwiki/src/ingest/video/tests.rs:81-95]
[crates/gwiki/src/ingest/video/tests.rs:98-118]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `sample_snapshot` | function | `fn sample_snapshot() -> VideoSnapshot {` | `sample_snapshot [function]` | `9f7f0716-cf91-59b0-8c44-a1c733edaddd` | 25-62 [crates/gwiki/src/ingest/video/tests.rs:25-62] | Indexed function `sample_snapshot` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:25-62] |
| `FakeVideoMediaExtractor` | class | `struct FakeVideoMediaExtractor {` | `FakeVideoMediaExtractor [class]` | `c0237e41-b6e0-50e4-9fa5-e38a5bbe2e64` | 64-69 [crates/gwiki/src/ingest/video/tests.rs:64-69] | Indexed class `FakeVideoMediaExtractor` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:64-69] |
| `FakeVideoMediaExtractor::extract_audio` | method | `fn extract_audio(&self, _video: &Path) -> Result<tempfile::NamedTempFile, WikiError> {` | `FakeVideoMediaExtractor::extract_audio [method]` | `0781d180-346a-5585-bc83-52b0864f61d5` | 72-79 [crates/gwiki/src/ingest/video/tests.rs:72-79] | Indexed method `FakeVideoMediaExtractor::extract_audio` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:72-79] |
| `FakeVideoMediaExtractor::sample_frame_images` | method | `fn sample_frame_images(` | `FakeVideoMediaExtractor::sample_frame_images [method]` | `c2bec767-6944-538d-8ba2-fdd8cd095068` | 81-95 [crates/gwiki/src/ingest/video/tests.rs:81-95] | Indexed method `FakeVideoMediaExtractor::sample_frame_images` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:81-95] |
| `temp_file_with_bytes` | function | `fn temp_file_with_bytes(suffix: &str, bytes: &[u8]) -> Result<tempfile::NamedTempFile, WikiError> {` | `temp_file_with_bytes [function]` | `13047d50-d234-5c7d-900a-c8397f01009d` | 98-118 [crates/gwiki/src/ingest/video/tests.rs:98-118] | Indexed function `temp_file_with_bytes` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:98-118] |
| `FakeTranscriptionClient` | class | `struct FakeTranscriptionClient;` | `FakeTranscriptionClient [class]` | `8f7d7215-c8b8-5c76-96d5-8ca8cc87b0c0` | 120-120 [crates/gwiki/src/ingest/video/tests.rs:120] | Indexed class `FakeTranscriptionClient` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:120] |
| `FakeTranscriptionClient::transcribe` | method | `fn transcribe(` | `FakeTranscriptionClient::transcribe [method]` | `2cafd9f9-3beb-5912-ab84-6a1c4084c649` | 123-137 [crates/gwiki/src/ingest/video/tests.rs:123-137] | Indexed method `FakeTranscriptionClient::transcribe` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:123-137] |
| `FailingTranscriptionClient` | class | `struct FailingTranscriptionClient;` | `FailingTranscriptionClient [class]` | `e2e0a18d-28e5-554f-b6b9-5a9d8faba7d7` | 140-140 [crates/gwiki/src/ingest/video/tests.rs:140] | Indexed class `FailingTranscriptionClient` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:140] |
| `FailingTranscriptionClient::transcribe` | method | `fn transcribe(` | `FailingTranscriptionClient::transcribe [method]` | `5c179191-eae3-5877-9634-e4372aef21a3` | 143-150 [crates/gwiki/src/ingest/video/tests.rs:143-150] | Indexed method `FailingTranscriptionClient::transcribe` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:143-150] |
| `FakeVisionClient` | class | `struct FakeVisionClient;` | `FakeVisionClient [class]` | `f525d93f-ea05-5111-9a6c-e4b21da392ed` | 153-153 [crates/gwiki/src/ingest/video/tests.rs:153] | Indexed class `FakeVisionClient` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:153] |
| `FakeVisionClient::extract` | method | `fn extract(&self, request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {` | `FakeVisionClient::extract [method]` | `8dfa8191-25e9-571d-bfb3-24cf718c1a60` | 156-166 [crates/gwiki/src/ingest/video/tests.rs:156-166] | Indexed method `FakeVisionClient::extract` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:156-166] |
| `FailingVisionClient` | class | `struct FailingVisionClient;` | `FailingVisionClient [class]` | `0b8a50f9-44c9-5f1b-861b-8ef138e58577` | 169-169 [crates/gwiki/src/ingest/video/tests.rs:169] | Indexed class `FailingVisionClient` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:169] |
| `FailingVisionClient::extract` | method | `fn extract(&self, _request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {` | `FailingVisionClient::extract [method]` | `01991d05-354f-5a94-9d0f-06cf4a41359a` | 172-176 [crates/gwiki/src/ingest/video/tests.rs:172-176] | Indexed method `FailingVisionClient::extract` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:172-176] |
| `transcript_output` | function | `fn transcript_output(` | `transcript_output [function]` | `1b3b06fa-72fb-5786-83e0-9822f8e7db8e` | 179-205 [crates/gwiki/src/ingest/video/tests.rs:179-205] | Indexed function `transcript_output` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:179-205] |
| `ScriptedTranscriptionClient` | class | `struct ScriptedTranscriptionClient {` | `ScriptedTranscriptionClient [class]` | `3efb0e7e-7ccf-5ad0-b410-77457c3320e5` | 208-211 [crates/gwiki/src/ingest/video/tests.rs:208-211] | Indexed class `ScriptedTranscriptionClient` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:208-211] |
| `ScriptedTranscriptionClient::transcribe` | method | `fn transcribe(` | `ScriptedTranscriptionClient::transcribe [method]` | `ff631682-e97e-509f-9b21-633159e7311a` | 215-222 [crates/gwiki/src/ingest/video/tests.rs:215-222] | Indexed method `ScriptedTranscriptionClient::transcribe` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:215-222] |
| `ScriptedTranscriptionClient::translate_to_english` | method | `fn translate_to_english(` | `ScriptedTranscriptionClient::translate_to_english [method]` | `6f128ce2-292f-5abb-9f94-0ab4e954ab40` | 224-231 [crates/gwiki/src/ingest/video/tests.rs:224-231] | Indexed method `ScriptedTranscriptionClient::translate_to_english` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:224-231] |
| `ScriptedChunkTranscriptionClient` | class | `struct ScriptedChunkTranscriptionClient {` | `ScriptedChunkTranscriptionClient [class]` | `52cf4f71-8e95-55da-9466-5f7480644d80` | 235-237 [crates/gwiki/src/ingest/video/tests.rs:235-237] | Indexed class `ScriptedChunkTranscriptionClient` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:235-237] |
| `ScriptedChunkTranscriptionClient::transcribe` | method | `fn transcribe(` | `ScriptedChunkTranscriptionClient::transcribe [method]` | `b4ad2eec-9b58-52bb-938b-19f02af663e2` | 241-246 [crates/gwiki/src/ingest/video/tests.rs:241-246] | Indexed method `ScriptedChunkTranscriptionClient::transcribe` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:241-246] |
| `ingest_with_media` | function | `fn ingest_with_media(` | `ingest_with_media [function]` | `77806cb4-7580-51a9-a4ba-4e796cc9d9b5` | 249-281 [crates/gwiki/src/ingest/video/tests.rs:249-281] | Indexed function `ingest_with_media` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:249-281] |
| `read_derived` | function | `fn read_derived(vault_root: &Path, result: &VideoIngestResult) -> String {` | `read_derived [function]` | `81f01164-89be-5be6-b734-62ada4905806` | 283-285 [crates/gwiki/src/ingest/video/tests.rs:283-285] | Indexed function `read_derived` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:283-285] |
| `assert_asset_preserved` | function | `fn assert_asset_preserved(vault_root: &Path, result: &VideoIngestResult, expected: &[u8]) {` | `assert_asset_preserved [function]` | `1b3fa2e6-fe7d-5b19-b4a0-f0bd28009a30` | 287-292 [crates/gwiki/src/ingest/video/tests.rs:287-292] | Indexed function `assert_asset_preserved` in `crates/gwiki/src/ingest/video/tests.rs`. [crates/gwiki/src/ingest/video/tests.rs:287-292] |
