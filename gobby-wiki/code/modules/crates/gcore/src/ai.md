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

The `crates/gcore/src/ai` module centralizes AI capability routing and direct provider calls for text, vision, embeddings, and speech tasks. Its root module imports `AiContext`, AI result/error types, and capability binding/routing config, then exposes submodules for daemon, embeddings, probe, text, transcription, and vision (`crates/gcore/src/ai/mod.rs:1-100`). Routing is capability-aware: `effective_route` preserves explicit `Off`, `Direct`, and `Daemon` choices, while `Auto` probes daemon availability and falls back to a configured direct route or `Off` (`crates/gcore/src/ai/mod.rs:1-100`).

The daemon child module is the blocking HTTP adapter between `AiContext` capability bindings and the local Gobby daemon. It sends voice transcription, vision extraction, text generation, and embedding work to daemon endpoints, while its request layer validates audio capability support, builds multipart uploads, adds optional text fields, and constructs text JSON bodies with provider/model/project/profile/candidate metadata (`operations.rs:1-13`, `request.rs:1-100`).

Direct capability flows use shared transport helpers from the root module. Vision encodes image bytes as a base64 data URI, sends a chat-completions-style request, and parses either JSON or delimited content into `VisionResult` (`crates/gcore/src/ai/vision.rs:1-100`). Transcription maps `TranscriptionTask` to `AudioTranscribe` or `AudioTranslate`, chooses `/v1/audio/transcriptions` or `/v1/audio/translations`, builds multipart requests, retries with backoff, and parses a `TranscriptionResult` (`crates/gcore/src/ai/transcription.rs:1-100`).

Probe support is the bridge between routing and daemon health. It imports `AiCapability` plus `daemon_url`, defines daemon status routes for five capabilities, and reports availability or degradation reasons such as missing endpoint, unauthorized, unreachable, or invalid body (`crates/gcore/src/ai/probe.rs:1-100`). That probe result feeds `effective_route` so callers get daemon routing only when the daemon advertises the requested capability (`crates/gcore/src/ai/mod.rs:1-100`).

| Public symbol / fact | Purpose | Source |
| --- | --- | --- |
| `effective_route` | Resolve configured AI routing for a capability | `crates/gcore/src/ai/mod.rs:1-100` |
| `CapabilityProbeReport::availability` | Look up probed daemon availability by capability | `crates/gcore/src/ai/probe.rs:1-100` |
| `capability_status_route` | Map AI capability to daemon status endpoint | `crates/gcore/src/ai/probe.rs:1-100` |
| `probe_daemon_capability` | Probe capability availability at the configured daemon URL | `crates/gcore/src/ai/probe.rs:1-100` |
| `describe_image` | Perform direct vision extraction | `crates/gcore/src/ai/vision.rs:1-100` |
| `transcribe` | Perform direct audio transcription or translation | `crates/gcore/src/ai/transcription.rs:1-100` |

| Capability | Status route | Source |
| --- | --- | --- |
| `AudioTranscribe` / `AudioTranslate` | `/api/voice/status` | `crates/gcore/src/ai/probe.rs:1-100` |
| `VisionExtract` | `/api/llm/vision/status` | `crates/gcore/src/ai/probe.rs:1-100` |
| `TextGenerate` | `/api/llm/status` | `crates/gcore/src/ai/probe.rs:1-100` |
| `Embed` | `/api/embeddings/status` | `crates/gcore/src/ai/probe.rs:1-100` |
[crates/gcore/src/ai/daemon/operations.rs:20-72]
[crates/gcore/src/ai/daemon/request.rs:11-19]
[crates/gcore/src/ai/daemon/transport.rs:8-12]
[crates/gcore/src/ai/daemon/types.rs:4-9]
[crates/gcore/src/ai/daemon.rs:1-15]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcore/src/ai/daemon\|crates/gcore/src/ai/daemon]] | The `crates/gcore/src/ai/daemon` module is the blocking HTTP adapter between `AiContext` capability bindings and a local Gobby daemon. Its operations layer sends AI work to daemon endpoints for voice transcription, vision extraction, text generation, and embeddings, importing request builders, response parsers, transport helpers, and daemon-specific result/option types from sibling files (`operations.rs:1-13`). The request layer validates supported audio capabilities, builds multipart file uploads, adds optional text fields, and constructs text request JSON with… |

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

