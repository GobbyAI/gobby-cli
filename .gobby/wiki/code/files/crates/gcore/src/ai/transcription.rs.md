---
title: crates/gcore/src/ai/transcription.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/transcription.rs
  ranges:
  - 11-14
  - 16-37
  - 39-73
  - 75-99
  - 101-142
  - 152-178
  - 181-201
  - 203-205
  - 207-214
  - 216-233
  - 235-248
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/transcription.rs

Module: [[code/modules/crates/gcore/src/ai|crates/gcore/src/ai]]

## Purpose

This file implements audio transcription/translation request handling for the AI layer. `TranscriptionTask` maps the two task variants to their API string labels, required `AiCapability`, and endpoint paths, while `transcribe` uses that mapping to resolve the configured base URL, build an authenticated multipart upload, rate-limit and retry the HTTP call, and turn the JSON response into a `TranscriptionResult` or `AiError`. The remaining helpers support request construction and tests by validating endpoint wiring, multipart metadata, headers, and the test AI context/binding setup.
[crates/gcore/src/ai/transcription.rs:11-14]
[crates/gcore/src/ai/transcription.rs:16-37]
[crates/gcore/src/ai/transcription.rs:17-22]
[crates/gcore/src/ai/transcription.rs:24-29]
[crates/gcore/src/ai/transcription.rs:31-36]

## API Symbols

- `TranscriptionTask` (type) component `TranscriptionTask [type]` (`2d31804d-32b8-59c4-aad6-972384818f52`) lines 11-14 [crates/gcore/src/ai/transcription.rs:11-14]
  - Signature: `pub enum TranscriptionTask {`
  - Purpose: Indexed type `TranscriptionTask` in `crates/gcore/src/ai/transcription.rs`. [crates/gcore/src/ai/transcription.rs:11-14]
- `TranscriptionTask` (class) component `TranscriptionTask [class]` (`ad36e36d-7b45-52a7-9aa4-4e08f2e3344c`) lines 16-37 [crates/gcore/src/ai/transcription.rs:16-37]
  - Signature: `impl TranscriptionTask {`
  - Purpose: 'TranscriptionTask' maps the 'Transcribe' and 'Translate' variants to their API string labels, required 'AiCapability', and corresponding audio endpoint paths. [crates/gcore/src/ai/transcription.rs:16-37]
- `TranscriptionTask.as_str` (method) component `TranscriptionTask.as_str [method]` (`fbac3b0b-9e0f-510f-9fe6-4659a3d98cf0`) lines 17-22 [crates/gcore/src/ai/transcription.rs:17-22]
  - Signature: `pub fn as_str(self) -> &'static str {`
  - Purpose: Returns the static string literal corresponding to the enum variant, mapping 'Transcribe' to '"transcribe"' and 'Translate' to '"translate"'. [crates/gcore/src/ai/transcription.rs:17-22]
- `TranscriptionTask.capability` (method) component `TranscriptionTask.capability [method]` (`2774e0de-7150-5384-8c38-f6b5754db9dd`) lines 24-29 [crates/gcore/src/ai/transcription.rs:24-29]
  - Signature: `fn capability(self) -> AiCapability {`
  - Purpose: Returns the corresponding 'AiCapability' enum variant for 'self', mapping 'Transcribe' to 'AudioTranscribe' and 'Translate' to 'AudioTranslate'. [crates/gcore/src/ai/transcription.rs:24-29]
- `TranscriptionTask.endpoint_path` (method) component `TranscriptionTask.endpoint_path [method]` (`681da7cf-e4a4-585f-9d2b-447a0325f4ff`) lines 31-36 [crates/gcore/src/ai/transcription.rs:31-36]
  - Signature: `fn endpoint_path(self) -> &'static str {`
  - Purpose: Returns the static API endpoint path for the enum variant, mapping 'Transcribe' to '/v1/audio/transcriptions' and 'Translate' to '/v1/audio/translations'. [crates/gcore/src/ai/transcription.rs:31-36]
- `transcribe` (function) component `transcribe [function]` (`a229a57c-576d-5fb5-b2ef-097bdaa08ad7`) lines 39-73 [crates/gcore/src/ai/transcription.rs:39-73]
  - Signature: `pub fn transcribe(`
  - Purpose: 'transcribe' builds an AI transport request for the given audio bytes and metadata, rate-limits and retries the HTTP call with backoff, parses the JSON response, and converts it into a 'TranscriptionResult' or 'AiError'. [crates/gcore/src/ai/transcription.rs:39-73]
- `endpoint_url` (function) component `endpoint_url [function]` (`13438c66-b78b-5d57-b362-796b20d701d3`) lines 75-99 [crates/gcore/src/ai/transcription.rs:75-99]
  - Signature: `fn endpoint_url(cfg: &AiContext, task: TranscriptionTask) -> Result<String, AiError> {`
  - Purpose: Returns the configured 'api_base' for the task’s capability after trimming and validating it as non-empty, then appends the task’s endpoint path with any trailing slash removed, or returns an 'AiError::not_configured' if 'api_base' is missing. [crates/gcore/src/ai/transcription.rs:75-99]
- `build_request` (function) component `build_request [function]` (`9273aba4-408f-5e69-ada2-d90694cb3dda`) lines 101-142 [crates/gcore/src/ai/transcription.rs:101-142]
  - Signature: `fn build_request(`
  - Purpose: Builds an authenticated multipart POST 'RequestBuilder' for a transcription upload by validating the payload size and MIME type, attaching the file plus 'response_format=verbose_json', optionally adding 'model' and 'language', and applying the transport’s API key and capability-specific timeout. [crates/gcore/src/ai/transcription.rs:101-142]
- `builds_multipart_and_parses_segments` (function) component `builds_multipart_and_parses_segments [function]` (`916ed16f-6c97-580d-927c-1f9c9c38530d`) lines 152-178 [crates/gcore/src/ai/transcription.rs:152-178]
  - Signature: `fn builds_multipart_and_parses_segments() {`
  - Purpose: Verifies that 'transcribe' sends a multipart 'POST /v1/audio/translations' request with the expected form fields and file metadata, then parses the verbose JSON response into a result whose language and segment timestamps are converted to milliseconds correctly. [crates/gcore/src/ai/transcription.rs:152-178]
- `wire_multipart_filename_and_auth` (function) component `wire_multipart_filename_and_auth [function]` (`2ad058a8-82bf-5c5c-beac-802c8ecb5b06`) lines 181-201 [crates/gcore/src/ai/transcription.rs:181-201]
  - Signature: `fn wire_multipart_filename_and_auth() {`
  - Purpose: Sends a transcription request with multipart file metadata and bearer auth, then verifies the HTTP request is a 'POST /v1/audio/transcriptions' containing 'Authorization: Bearer test-token', the multipart filename 'meeting.m4a', and 'Content-Type: audio/mp4'. [crates/gcore/src/ai/transcription.rs:181-201]
- `spawn_server` (function) component `spawn_server [function]` (`e33b4635-422b-5e37-9fec-12eebb60586f`) lines 203-205 [crates/gcore/src/ai/transcription.rs:203-205]
  - Signature: `fn spawn_server(response: &'static str) -> (String, RequestHandle) {`
  - Purpose: Calls 'spawn_json_response(response)' and unwraps the result with 'expect("spawn test server")', returning the server address string and a 'RequestHandle'. [crates/gcore/src/ai/transcription.rs:203-205]
- `has_header` (function) component `has_header [function]` (`f90102be-9d77-5eaf-a26b-b640da9b3891`) lines 207-214 [crates/gcore/src/ai/transcription.rs:207-214]
  - Signature: `fn has_header(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: Returns 'true' if any line in the request parses as a 'name: value' header whose field name matches 'name' case-insensitively and whose trimmed value equals 'value', otherwise 'false'. [crates/gcore/src/ai/transcription.rs:207-214]
- `test_context` (function) component `test_context [function]` (`7cfc1bed-9dcb-5632-9987-bb6a565ab7b0`) lines 216-233 [crates/gcore/src/ai/transcription.rs:216-233]
  - Signature: `fn test_context(api_base: &str, api_key: Option<&str>) -> AiContext {`
  - Purpose: Constructs an 'AiContext' for tests by creating a shared binding from 'api_base' and optional 'api_key', assigning it to all AI capabilities, and configuring a single-concurrency tuning and limiter with no project ID. [crates/gcore/src/ai/transcription.rs:216-233]
- `binding` (function) component `binding [function]` (`ac0ebe19-faba-55c3-b5a0-6ad6eb79c1be`) lines 235-248 [crates/gcore/src/ai/transcription.rs:235-248]
  - Signature: `fn binding(api_base: &str, api_key: Option<&str>) -> CapabilityBinding {`
  - Purpose: Returns a 'CapabilityBinding' configured for direct AI routing with no transport, the provided 'api_base' and optional 'api_key', a fixed 'model' of '"whisper-1"', and all other fields unset. [crates/gcore/src/ai/transcription.rs:235-248]

