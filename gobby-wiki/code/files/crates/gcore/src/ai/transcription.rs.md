---
title: crates/gcore/src/ai/transcription.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/transcription.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/transcription.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/ai/transcription.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gcore/src/ai/transcription.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `TranscriptionTask` | type | Indexed type `TranscriptionTask` in `crates/gcore/src/ai/transcription.rs`. [crates/gcore/src/ai/transcription.rs:11-14] |
| `TranscriptionTask::as_str` | method | Returns the static string slice '"transcribe"' for 'Self::Transcribe' and '"translate"' for 'Self::Translate'. [crates/gcore/src/ai/transcription.rs:17-22] |
| `TranscriptionTask::capability` | method | Returns the corresponding 'AiCapability' enum variant for 'self', mapping 'Self::Transcribe' to 'AiCapability::AudioTranscribe' and 'Self::Translate' to 'AiCapability::AudioTranslate'. [crates/gcore/src/ai/transcription.rs:24-29] |
| `TranscriptionTask::endpoint_path` | method | Returns the static API route string for the selected audio endpoint, mapping 'Transcribe' to '"/v1/audio/transcriptions"' and 'Translate' to '"/v1/audio/translations"'. [crates/gcore/src/ai/transcription.rs:31-36] |
| `transcribe` | function | Creates an AI transport, rate-limits the call, and retries a multipart transcription request with backoff before parsing the JSON response into a 'TranscriptionResult'. [crates/gcore/src/ai/transcription.rs:39-73] |
| `endpoint_url` | function | Validates that the task’s capability binding has a non-empty 'api_base', returning an 'AiError' if missing, and otherwise constructs the transcription endpoint URL by concatenating the normalized base URL without trailing slashes and the task-specific endpoint path. [crates/gcore/src/ai/transcription.rs:75-99] |
| `build_request` | function | Builds a multipart POST request for a transcription upload by attaching the file with a validated MIME type and length, adding 'response_format=verbose_json' plus optional 'model' and 'language' fields from the transport binding or argument, applying the API key, and returning a timeout-configured 'RequestBuilder' or an 'AiError' on invalid size or MIME. [crates/gcore/src/ai/transcription.rs:101-142] |
| `spawn_server` | function | Spawns a test server that serves the given static string as a JSON response, returning the server address and a 'RequestHandle', and panicking if startup fails. [crates/gcore/src/ai/transcription.rs:203-205] |
| `has_header` | function | Returns 'true' if any line in 'request' contains a 'name: value' header whose name matches 'name' case-insensitively and whose trimmed value exactly equals 'value'. [crates/gcore/src/ai/transcription.rs:207-214] |
| `test_context` | function | Constructs an 'AiContext' for testing by creating a shared binding from 'api_base' and optional 'api_key', cloning it across all AI capability bindings, setting tuning to single concurrency with no keep-alive, initializing a limiter of 1, and leaving 'project_id' unset. [crates/gcore/src/ai/transcription.rs:216-233] |
| `binding` | function | The 'binding' function constructs and returns a 'CapabilityBinding' struct configured with direct routing, a specified API base URL, an optional API key, and a hardcoded model set to "whisper-1". [crates/gcore/src/ai/transcription.rs:235-253] |

_Verified by 2 in-file unit tests._

