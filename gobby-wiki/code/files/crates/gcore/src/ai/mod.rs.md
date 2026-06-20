---
title: crates/gcore/src/ai/mod.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/mod.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/ai/mod.rs` exposes 37 indexed API symbols.

## How it fits

`crates/gcore/src/ai/mod.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `effective_route` | function | Returns the effective 'AiRouting' for a given 'AiCapability' by delegating to 'effective_route_with_probe' and determining daemon capability availability via 'probe::probe_daemon_capability(capability).available'. [crates/gcore/src/ai/mod.rs:31-35] |
| `effective_route_with_probe` | function | Returns the routing for a given capability from 'context.binding(capability)', preserving 'Off', 'Direct', and 'Daemon' as-is, and resolving 'Auto' by calling 'daemon_route_or_fallback' with the provided daemon-availability probe. [crates/gcore/src/ai/mod.rs:37-48] |
| `daemon_route_or_fallback` | function | Returns 'AiRouting::Daemon' only when 'daemon_available(capability)' is true, otherwise delegates to 'direct_route_or_off(context, capability)' to choose a direct route or 'Off' as a fail-safe fallback. [crates/gcore/src/ai/mod.rs:50-62] |
| `direct_route_or_off` | function | Returns 'AiRouting::Direct' when the bound capability’s 'api_base' is present and non-empty after trimming whitespace, otherwise returns 'AiRouting::Off'. [crates/gcore/src/ai/mod.rs:64-76] |
| `AiTransport` | class | 'AiTransport<'a>' is a transport wrapper that holds a borrowed 'AiContext' and an owned 'Client' for issuing AI-related requests. [crates/gcore/src/ai/mod.rs:79-82] |
| `new` | function | Constructs a new instance by creating a 'reqwest::Client' with default builder settings, converting any build failure into 'AiError', and storing it together with the provided 'AiContext' reference. [crates/gcore/src/ai/mod.rs:85-89] |
| `post_json` | function | 'post_json' serializes 'body' to JSON, builds an authenticated request for the given 'capability' and 'url', sends it with rate limiting and retry-with-backoff behavior, and returns the parsed 'serde_json::Value' response or an 'AiError'. [crates/gcore/src/ai/mod.rs:91-108] |
| `post_multipart` | function | Acquires a rate-limit permit, converts the input buffer to 'Bytes', then performs a retried multipart HTTP POST built from the given capability, URL, file part metadata, and form fields, returning the parsed JSON response or an 'AiError'. [crates/gcore/src/ai/mod.rs:110-135] |
| `parse_transcription` | function | Deserializes a 'serde_json::Value' into a 'TranscriptionResult' by delegating to 'TranscriptionResult::from_wire_json', returning an 'AiError' on failure. [crates/gcore/src/ai/mod.rs:137-142] |
| `parse_vision` | function | Converts a 'serde_json::Value' into a 'VisionResult' by delegating to 'VisionResult::from_wire_json', returning an 'AiError' on failure. [crates/gcore/src/ai/mod.rs:144-146] |
| `parse_text` | function | Delegates deserialization of a 'serde_json::Value' into a 'TextResult' by calling 'TextResult::from_wire_json', returning any resulting 'AiError'. [crates/gcore/src/ai/mod.rs:148-150] |
| `build_json_request` | function | Builds a POST JSON 'RequestBuilder' for the given capability and URL by applying the capability-specific timeout, serializing 'body' as the request payload, and wrapping the builder with 'apply_api_key' using the resolved context binding. [crates/gcore/src/ai/mod.rs:152-169] |
| `build_multipart_request` | function | Builds a 'reqwest' multipart POST request for the given capability and URL by attaching a length-checked file part plus arbitrary text fields, then applies the capability-specific API key and returns the configured 'RequestBuilder' or an 'AiError' if the payload size cannot be represented as 'u64'. [crates/gcore/src/ai/mod.rs:171-201] |
| `apply_api_key` | function | Adds an 'Authorization: Bearer <api_key>' header to the 'RequestBuilder' when 'binding.api_key' is present, otherwise returns the request unchanged. [crates/gcore/src/ai/mod.rs:204-209] |
| `timeout_for` | function | 'timeout_for' returns the 'Duration' timeout constant associated with the given 'AiCapability', mapping audio transcription/translation to 'STT_CHUNK_TIMEOUT', embeddings to 'EMBEDDINGS_TIMEOUT', vision extraction to 'VISION_TIMEOUT', and text generation to 'TEXT_GENERATE_TIMEOUT'. [crates/gcore/src/ai/mod.rs:211-218] |
| `retry_with_backoff` | function | 'retry_with_backoff' repeatedly invokes an operation up to 'MAX_RETRIES' times, sleeping for an error-dependent backoff delay between attempts only when the failure is retryable, and returns either the first successful result or the final non-retryable/exhausted 'AiError'. [crates/gcore/src/ai/mod.rs:220-235] |
| `is_retryable` | function | Returns 'true' for rate limits and for transport/HTTP failures that are timeout '408', too-many-requests '429', or any '5xx' status, and 'false' for capability-unavailable, not-configured, and parse failures. [crates/gcore/src/ai/mod.rs:237-248] |
| `retry_delay` | function | Returns a retry 'Duration' by honoring 'error.retry_after()' when present, capped at 'MAX_BACKOFF', otherwise computing capped exponential backoff from 'BASE_BACKOFF << min(retry_index, 16)' plus jitter. [crates/gcore/src/ai/mod.rs:250-258] |
| `jitter` | function | Returns a 'Duration' representing a random jitter from '0' to '49' milliseconds by generating a random 'u8', taking it modulo '50', and converting the result to milliseconds. [crates/gcore/src/ai/mod.rs:260-262] |
| `parse_json_response` | function | Consumes an HTTP 'Response', extracts any 'Retry-After' header, reads the body, maps 429/5xx/408/other non-success statuses into specific 'AiError' variants with the response body attached, and otherwise parses the body as 'serde_json::Value' or returns a JSON parse failure. [crates/gcore/src/ai/mod.rs:264-297] |
| `parse_retry_after` | function | Parses a 'Retry-After' header value as either a nonnegative second count or an HTTP date, returning the elapsed delay until that date, both capped at 'MAX_BACKOFF', or 'None' if parsing fails. [crates/gcore/src/ai/mod.rs:299-310] |
| `reqwest_error` | function | Converts a 'reqwest::Error' into an 'AiError::transport_failure', propagating the HTTP status code as 'Option<u16>', leaving the second parameter 'None', and using the error’s string representation as the message. [crates/gcore/src/ai/mod.rs:312-318] |
| `duration_to_ms` | function | Converts a 'Duration' to milliseconds as a 'u64', saturating at 'u64::MAX' if 'duration.as_millis()' exceeds that limit. [crates/gcore/src/ai/mod.rs:320-322] |
| `chat_completions_url` | function | Returns the configured capability’s non-empty 'api_base' from 'AiContext', errors with 'AiError::not_configured' if missing or blank, and otherwise constructs the direct chat completions endpoint as '"{chat_api_root(api_base)}/v1/chat/completions"'. [crates/gcore/src/ai/mod.rs:324-342] |

_4 more symbol(s) not shown — run `gcode outline crates/gcore/src/ai/mod.rs` for the full list._

_Verified by 9 in-file unit tests._

