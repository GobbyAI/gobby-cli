---
title: crates/gcore/src/ai/daemon
type: code_module
provenance:
- file: crates/gcore/src/ai/daemon/operations.rs
- file: crates/gcore/src/ai/daemon/request.rs
- file: crates/gcore/src/ai/daemon/response.rs
- file: crates/gcore/src/ai/daemon/tests.rs
- file: crates/gcore/src/ai/daemon/transport.rs
- file: crates/gcore/src/ai/daemon/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/daemon

Parent: [[code/modules/crates/gcore/src/ai|crates/gcore/src/ai]]

## Overview

## crates/gcore/src/ai/daemon

This module implements a local-daemon AI backend for `gcore`, routing transcription, vision, text-generation, and embedding operations to a long-running daemon process on the same machine. It is one concrete routing strategy under `crates/gcore/src/ai`, selected when a capability binding carries `AiRouting::Daemon` (tests.rs:75–82). Every operation follows the same skeleton: acquire a concurrency permit from `AiContext::limiter`, build an HTTP request using helpers in `request.rs`, authenticate with a file-system token via `transport.rs`, post to the daemon over localhost, and parse the JSON response through `response.rs`. Retries with exponential back-off are delegated to `super::super::retry_with_backoff` (operations.rs:43).

The transport layer (`transport.rs`) resolves the daemon's base URL from `crate::daemon_url::daemon_url()` and authenticates every request by reading a plain-text token from `~/.gobby/local_cli_token` (transport.rs:22–37), attaching it as the `X-Gobby-Local-Token` header (transport.rs:6, 44–46). If the token file is absent or empty, `read_local_cli_token` returns `AiError::not_configured`. The request layer (`request.rs`) guards audio operations through `audio_capability`, which rejects any capability other than `AudioTranscribe` or `AudioTranslate` with `AiError::capability_unavailable` (request.rs:11–18). Multipart audio payloads are constructed via `multipart_form_with_file` and augmented with optional provider, model, language, and prompt fields using `add_optional_text` (request.rs:21–52). JSON text and embedding bodies are assembled by `text_request_body` and `embeddings_request_body`, which insert optional keys such as provider, model, project ID, max tokens, profile, candidates, and reasoning effort (request.rs:55–100).

The test infrastructure in `tests.rs` spins up an in-process JSON HTTP server via `crate::test_http::spawn_json_response`, writes synthetic daemon bootstrap and token files under a `tempfile::TempDir` guarded by `EnvGuard` (which patches `HOME` and restores it on drop), and assembles a fully-wired `AiContext` through `test_context`/`binding` helpers (tests.rs:15–85). Sub-modules `embeddings`, `environment`, `multipart`, and `text` host the actual test cases. The module imports `crate::config::{AiRouting, AiTuning, CapabilityBinding, TEST_ENV_LOCK}`, `crate::ai_context::{AiBindings, AiContext, AiLimiter}`, and `crate::ai_types::AiError` as its primary cross-crate dependencies.

### Public Operation Functions

| Function | Daemon Endpoint | Notes |
|---|---|---|
| `transcribe_via_daemon` | `/api/voice/transcribe` | Multipart form; `AudioTranscribe` or `AudioTranslate` only |
| `describe_image_via_daemon` | `/api/llm/vision/extract` | Multipart form with image bytes |
| `generate_via_daemon` | `/api/llm/generate` | Default token limit and profile |
| `generate_via_daemon_with_max_tokens` | `/api/llm/generate` | Caller-supplied `max_tokens` |
| `generate_via_daemon_with_candidates` | `/api/llm/generate` | Accepts `&[FeatureCandidate]` slice |
| `generate_text_via_daemon` | `/api/llm/generate` | Simplified text-only variant |
| `embed_via_daemon` | `/api/embeddings` | Returns `DaemonEmbeddingResult` |

### Key Types

| Type | File | Role |
|---|---|---|
| `DaemonTranscriptionOptions` | `types.rs` | Capability, language, target\_lang, prompt for audio ops |
| `DaemonEmbeddingResult` | `types.rs` | Parsed embeddings response |
| `TextRequestOptions` | `request.rs` | Provider, model, project\_id, max\_tokens, profile, candidates, reasoning\_effort |

### Transport Constants and Config Files

| Artifact | Value / Path | Purpose |
|---|---|---|
| `LOCAL_TOKEN_HEADER` | `X-Gobby-Local-Token` | Auth header on every request (transport.rs:6) |
| `LOCAL_CLI_TOKEN_FILENAME` | `local_cli_token` | Token file read from `~/.gobby/` (transport.rs:5) |
| Bootstrap file | `~/.gobby/bootstrap.yaml` | Contains `daemon_port` and `bind_host` (tests.rs:51–55) |
| `TEXT_GENERATE_DEFAULT_PROFILE` | `feature_low` | Default profile for text generation (request.rs:8) |
[crates/gcore/src/ai/daemon/operations.rs:20-72]
[crates/gcore/src/ai/daemon/request.rs:11-19]
[crates/gcore/src/ai/daemon/response.rs:7-9]
[crates/gcore/src/ai/daemon/tests.rs:15-24]
[crates/gcore/src/ai/daemon/transport.rs:8-12]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/src/ai/daemon/operations.rs\|crates/gcore/src/ai/daemon/operations.rs]] | `crates/gcore/src/ai/daemon/operations.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/daemon/request.rs\|crates/gcore/src/ai/daemon/request.rs]] | `crates/gcore/src/ai/daemon/request.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/daemon/response.rs\|crates/gcore/src/ai/daemon/response.rs]] | `crates/gcore/src/ai/daemon/response.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/daemon/tests.rs\|crates/gcore/src/ai/daemon/tests.rs]] | `crates/gcore/src/ai/daemon/tests.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/daemon/transport.rs\|crates/gcore/src/ai/daemon/transport.rs]] | `crates/gcore/src/ai/daemon/transport.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/daemon/types.rs\|crates/gcore/src/ai/daemon/types.rs]] | `crates/gcore/src/ai/daemon/types.rs` exposes 3 indexed API symbols. |

