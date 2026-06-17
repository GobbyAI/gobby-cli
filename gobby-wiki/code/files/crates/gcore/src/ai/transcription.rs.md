---
title: crates/gcore/src/ai/transcription.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/transcription.rs
  ranges:
  - 11-14
  - 17-22
  - 24-29
  - 31-36
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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/ai/transcription.rs:11-14](crates/gcore/src/ai/transcription.rs#L11-L14), [crates/gcore/src/ai/transcription.rs:17-22](crates/gcore/src/ai/transcription.rs#L17-L22), [crates/gcore/src/ai/transcription.rs:24-29](crates/gcore/src/ai/transcription.rs#L24-L29), [crates/gcore/src/ai/transcription.rs:31-36](crates/gcore/src/ai/transcription.rs#L31-L36), [crates/gcore/src/ai/transcription.rs:39-73](crates/gcore/src/ai/transcription.rs#L39-L73), [crates/gcore/src/ai/transcription.rs:75-99](crates/gcore/src/ai/transcription.rs#L75-L99), [crates/gcore/src/ai/transcription.rs:101-142](crates/gcore/src/ai/transcription.rs#L101-L142), [crates/gcore/src/ai/transcription.rs:152-178](crates/gcore/src/ai/transcription.rs#L152-L178), [crates/gcore/src/ai/transcription.rs:181-201](crates/gcore/src/ai/transcription.rs#L181-L201), [crates/gcore/src/ai/transcription.rs:203-205](crates/gcore/src/ai/transcription.rs#L203-L205), [crates/gcore/src/ai/transcription.rs:207-214](crates/gcore/src/ai/transcription.rs#L207-L214), [crates/gcore/src/ai/transcription.rs:216-233](crates/gcore/src/ai/transcription.rs#L216-L233), [crates/gcore/src/ai/transcription.rs:235-248](crates/gcore/src/ai/transcription.rs#L235-L248)

</details>

# crates/gcore/src/ai/transcription.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This file implements audio transcription and translation requests for the AI layer. `TranscriptionTask` selects between transcribe and translate, and its helpers map that choice to the public task string, required capability, and API endpoint path.

`transcribe` is the main entry point: it builds the transport, resolves the endpoint URL from config, acquires rate-limit permission, constructs a multipart request with optional language input, retries on failure, and parses the JSON response into a `TranscriptionResult`. The remaining functions support that flow and the tests, covering endpoint selection, multipart/auth wiring, server setup, and request/header assertions.
[crates/gcore/src/ai/transcription.rs:11-14]
[crates/gcore/src/ai/transcription.rs:17-22]
[crates/gcore/src/ai/transcription.rs:24-29]
[crates/gcore/src/ai/transcription.rs:31-36]
[crates/gcore/src/ai/transcription.rs:39-73]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `TranscriptionTask` | type | `pub enum TranscriptionTask {` | `TranscriptionTask [type]` | `2d31804d-32b8-59c4-aad6-972384818f52` | 11-14 [crates/gcore/src/ai/transcription.rs:11-14] | Indexed type `TranscriptionTask` in `crates/gcore/src/ai/transcription.rs`. [crates/gcore/src/ai/transcription.rs:11-14] |
| `TranscriptionTask::as_str` | method | `pub fn as_str(self) -> &'static str {` | `TranscriptionTask::as_str [method]` | `fbac3b0b-9e0f-510f-9fe6-4659a3d98cf0` | 17-22 [crates/gcore/src/ai/transcription.rs:17-22] | Indexed method `TranscriptionTask::as_str` in `crates/gcore/src/ai/transcription.rs`. [crates/gcore/src/ai/transcription.rs:17-22] |
| `TranscriptionTask::capability` | method | `fn capability(self) -> AiCapability {` | `TranscriptionTask::capability [method]` | `2774e0de-7150-5384-8c38-f6b5754db9dd` | 24-29 [crates/gcore/src/ai/transcription.rs:24-29] | Indexed method `TranscriptionTask::capability` in `crates/gcore/src/ai/transcription.rs`. [crates/gcore/src/ai/transcription.rs:24-29] |
| `TranscriptionTask::endpoint_path` | method | `fn endpoint_path(self) -> &'static str {` | `TranscriptionTask::endpoint_path [method]` | `681da7cf-e4a4-585f-9d2b-447a0325f4ff` | 31-36 [crates/gcore/src/ai/transcription.rs:31-36] | Indexed method `TranscriptionTask::endpoint_path` in `crates/gcore/src/ai/transcription.rs`. [crates/gcore/src/ai/transcription.rs:31-36] |
| `transcribe` | function | `pub fn transcribe(` | `transcribe [function]` | `a229a57c-576d-5fb5-b2ef-097bdaa08ad7` | 39-73 [crates/gcore/src/ai/transcription.rs:39-73] | Indexed function `transcribe` in `crates/gcore/src/ai/transcription.rs`. [crates/gcore/src/ai/transcription.rs:39-73] |
| `endpoint_url` | function | `fn endpoint_url(cfg: &AiContext, task: TranscriptionTask) -> Result<String, AiError> {` | `endpoint_url [function]` | `13438c66-b78b-5d57-b362-796b20d701d3` | 75-99 [crates/gcore/src/ai/transcription.rs:75-99] | Indexed function `endpoint_url` in `crates/gcore/src/ai/transcription.rs`. [crates/gcore/src/ai/transcription.rs:75-99] |
| `build_request` | function | `fn build_request(` | `build_request [function]` | `9273aba4-408f-5e69-ada2-d90694cb3dda` | 101-142 [crates/gcore/src/ai/transcription.rs:101-142] | Indexed function `build_request` in `crates/gcore/src/ai/transcription.rs`. [crates/gcore/src/ai/transcription.rs:101-142] |
| `builds_multipart_and_parses_segments` | function | `fn builds_multipart_and_parses_segments() {` | `builds_multipart_and_parses_segments [function]` | `916ed16f-6c97-580d-927c-1f9c9c38530d` | 152-178 [crates/gcore/src/ai/transcription.rs:152-178] | Indexed function `builds_multipart_and_parses_segments` in `crates/gcore/src/ai/transcription.rs`. [crates/gcore/src/ai/transcription.rs:152-178] |
| `wire_multipart_filename_and_auth` | function | `fn wire_multipart_filename_and_auth() {` | `wire_multipart_filename_and_auth [function]` | `2ad058a8-82bf-5c5c-beac-802c8ecb5b06` | 181-201 [crates/gcore/src/ai/transcription.rs:181-201] | Indexed function `wire_multipart_filename_and_auth` in `crates/gcore/src/ai/transcription.rs`. [crates/gcore/src/ai/transcription.rs:181-201] |
| `spawn_server` | function | `fn spawn_server(response: &'static str) -> (String, RequestHandle) {` | `spawn_server [function]` | `e33b4635-422b-5e37-9fec-12eebb60586f` | 203-205 [crates/gcore/src/ai/transcription.rs:203-205] | Indexed function `spawn_server` in `crates/gcore/src/ai/transcription.rs`. [crates/gcore/src/ai/transcription.rs:203-205] |
| `has_header` | function | `fn has_header(request: &str, name: &str, value: &str) -> bool {` | `has_header [function]` | `f90102be-9d77-5eaf-a26b-b640da9b3891` | 207-214 [crates/gcore/src/ai/transcription.rs:207-214] | Indexed function `has_header` in `crates/gcore/src/ai/transcription.rs`. [crates/gcore/src/ai/transcription.rs:207-214] |
| `test_context` | function | `fn test_context(api_base: &str, api_key: Option<&str>) -> AiContext {` | `test_context [function]` | `7cfc1bed-9dcb-5632-9987-bb6a565ab7b0` | 216-233 [crates/gcore/src/ai/transcription.rs:216-233] | Indexed function `test_context` in `crates/gcore/src/ai/transcription.rs`. [crates/gcore/src/ai/transcription.rs:216-233] |
| `binding` | function | `fn binding(api_base: &str, api_key: Option<&str>) -> CapabilityBinding {` | `binding [function]` | `ac0ebe19-faba-55c3-b5a0-6ad6eb79c1be` | 235-248 [crates/gcore/src/ai/transcription.rs:235-248] | Indexed function `binding` in `crates/gcore/src/ai/transcription.rs`. [crates/gcore/src/ai/transcription.rs:235-248] |
