---
title: crates/gcore/src/ai
type: code_module
provenance:
- file: crates/gcore/src/ai/daemon.rs
- file: crates/gcore/src/ai/daemon/operations.rs
- file: crates/gcore/src/ai/daemon/request.rs
- file: crates/gcore/src/ai/daemon/response.rs
- file: crates/gcore/src/ai/daemon/tests.rs
- file: crates/gcore/src/ai/daemon/transport.rs
- file: crates/gcore/src/ai/daemon/types.rs
- file: crates/gcore/src/ai/embeddings.rs
- file: crates/gcore/src/ai/mod.rs
- file: crates/gcore/src/ai/probe.rs
- file: crates/gcore/src/ai/text.rs
- file: crates/gcore/src/ai/transcription.rs
- file: crates/gcore/src/ai/vision.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai

Parent: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

## crates/gcore/src/ai

This module is the central AI dispatch layer for `gcore`, responsible for routing AI capability requests — text generation, vision/image description, audio transcription and translation, and vector embeddings — to either a local daemon process or a direct remote API endpoint. It owns the shared transport primitives (retry logic, backoff, timeout constants, HTTP client wrappers) and re-exports the six sub-modules that implement each capability. The `mod.rs` file defines `AiTransport`, `effective_route`, and helpers such as `chat_completions_url`, `retry_with_backoff`, and `parse_json_response` that every sub-module calls through the `super::` path (mod.rs:1–100).

Routing decisions flow through `effective_route` → `effective_route_with_probe` → `daemon_route_or_fallback` / `direct_route_or_off` (mod.rs:31–65). When the configured `AiRouting` is `Auto`, the module calls into `probe::probe_daemon_capability` at runtime to check whether the daemon currently advertises the requested capability; if it does not, the module falls back to a direct API binding or returns `AiRouting::Off`. This probe-then-fallback design makes the system fail-safe: a missing or degraded daemon never blocks a configured direct route. The probe sub-module contacts daemon status endpoints with a tight 750 ms timeout (probe.rs:7) and maps each of the five probed capabilities to a fixed status path (probe.rs:9–17, 62–72).

Each capability sub-module follows a consistent pattern: accept an `&AiContext`, construct an `AiTransport`, resolve a URL (via `super::chat_completions_url` or a task-specific `endpoint_url`), build a request body, call `super::retry_with_backoff`, and parse the response. `transcription.rs` models two tasks (`Transcribe` / `Translate`) that map to `/v1/audio/transcriptions` and `/v1/audio/translations` (transcription.rs:34–37) and attach multipart audio payloads with an optional language field. `vision.rs` base64-encodes image bytes into a data URI and sends a fixed structured prompt requesting JSON output with `description` and `ocr_text` keys (vision.rs:10–11, 36–53). The `daemon.rs` child module and its sub-package expose convenience wrappers — `generate_via_daemon`, `transcribe_via_daemon`, `describe_image_via_daemon`, `embed_via_daemon` — that bypass the routing layer and talk directly to the daemon, primarily used by tests and internal tooling.

### Timeout & retry constants

| Constant | Value | Applies to |
|---|---|---|
| `TEXT_GENERATE_TIMEOUT` | 300 s | Text generation (mod.rs:22) |
| `VISION_TIMEOUT` | 60 s | Vision/image requests (mod.rs:23) |
| `EMBEDDINGS_TIMEOUT` | 10 s | Embeddings requests (mod.rs:24) |
| `STT_CHUNK_TIMEOUT` | 120 s | Audio transcription chunks (mod.rs:25) |
| `PROBE_TIMEOUT` | 750 ms | Daemon capability probe (probe.rs:7) |
| `MAX_RETRIES` | 2 | All retried operations (mod.rs:26) |
| `BASE_BACKOFF` | 250 ms | Initial retry wait (mod.rs:27) |
| `MAX_BACKOFF` | 30 s | Retry ceiling (mod.rs:28) |

### Daemon status routes by capability

| AiCapability | HTTP Method | Status Path |
|---|---|---|
| `AudioTranscribe` / `AudioTranslate` | GET | `/api/voice/status` (probe.rs:64) |
| `VisionExtract` | GET | `/api/llm/vision/status` (probe.rs:65) |
| `TextGenerate` | GET | `/api/llm/status` (probe.rs:66) |
| `Embed` | GET | `/api/embeddings/status` (probe.rs:67) |

### Public API surface by sub-module

| Sub-module | Key public symbols |
|---|---|
| `mod.rs` | `effective_route`, `AiTransport`, `retry_with_backoff`, `chat_completions_url`, `parse_json_response` (37 symbols) |
| `probe.rs` | `probe_daemon_capability`, `probe_daemon_capability_at`, `CapabilityProbeReport`, `CapabilityAvailability`, `CapabilityDegradation`, `capability_status_route` (31 symbols) |
| `vision.rs` | `describe_image`, `request_body`, `parse_content` (18 symbols) |
| `transcription.rs` | `transcribe`, `TranscriptionTask`, `endpoint_url`, `build_request` (13 symbols) |
| `embeddings.rs` | `embed`, `embeddings_request_body`, `parse_daemon_embeddings` (12 symbols) |
| `text.rs` | `generate_text`, `TextRequestOptions`, `text_request_body` (11 symbols) |
| `daemon.rs` | `generate_via_daemon`, `transcribe_via_daemon`, `describe_image_via_daemon`, `embed_via_daemon`, `spawn_server`, `EnvGuard` (no indexed exports; see component table) |

The module imports `AiContext` from `crate::ai_context`, result/error types from `crate::ai_types`, capability and routing enumerations from `crate::config`, and the daemon base URL resolver from `crate::daemon_url` (probe.rs:5; mod.rs:9–11). External callers — such as higher-level service handlers — invoke the public entry points (`describe_image`, `transcribe`, `embed`, `generate_text`) and rely on this module to transparently select the daemon or direct transport without needing to know about routing, retries, or backoff.
[crates/gcore/src/ai/daemon/operations.rs:20-72]
[crates/gcore/src/ai/daemon/request.rs:11-19]
[crates/gcore/src/ai/daemon/response.rs:7-9]
[crates/gcore/src/ai/daemon/tests.rs:15-24]
[crates/gcore/src/ai/daemon/transport.rs:8-12]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcore/src/ai/daemon\|crates/gcore/src/ai/daemon]] | ## crates/gcore/src/ai/daemon |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/src/ai/daemon.rs\|crates/gcore/src/ai/daemon.rs]] | `crates/gcore/src/ai/daemon.rs` has no indexed API symbols. |
| [[code/files/crates/gcore/src/ai/embeddings.rs\|crates/gcore/src/ai/embeddings.rs]] | `crates/gcore/src/ai/embeddings.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/mod.rs\|crates/gcore/src/ai/mod.rs]] | `crates/gcore/src/ai/mod.rs` exposes 37 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/probe.rs\|crates/gcore/src/ai/probe.rs]] | `crates/gcore/src/ai/probe.rs` exposes 31 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/text.rs\|crates/gcore/src/ai/text.rs]] | `crates/gcore/src/ai/text.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/transcription.rs\|crates/gcore/src/ai/transcription.rs]] | `crates/gcore/src/ai/transcription.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/vision.rs\|crates/gcore/src/ai/vision.rs]] | `crates/gcore/src/ai/vision.rs` exposes 18 indexed API symbols. |

