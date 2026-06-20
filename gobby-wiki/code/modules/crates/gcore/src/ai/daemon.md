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

The `crates/gcore/src/ai/daemon` module is the blocking HTTP adapter between `AiContext` capability bindings and a local Gobby daemon. Its operations layer sends AI work to daemon endpoints for voice transcription, vision extraction, text generation, and embeddings, importing request builders, response parsers, transport helpers, and daemon-specific result/option types from sibling files (`operations.rs:1-13`). The request layer validates supported audio capabilities, builds multipart file uploads, adds optional text fields, and constructs text request JSON with provider/model/project/profile/candidate metadata (`request.rs:1-100`).

Runtime flow starts from functions such as `transcribe_via_daemon`, which reads the requested capability from `DaemonTranscriptionOptions`, resolves the capability binding from `AiContext`, creates a reqwest client, reads the local CLI token, builds the daemon URL, applies binding defaults such as language/model/provider, acquires the AI limiter, and executes the call through the shared retry/backoff path (`operations.rs:15-60`). Transport centralizes daemon URL construction, local token loading from `.gobby/local_cli_token`, and injection of the `X-Gobby-Local-Token` header (`transport.rs:1-47`).

The module collaborates outward with `crate::ai_context` for bindings, concurrency limits, and project IDs; `crate::config` for capabilities, routing, tuning, and feature candidates; `crate::ai_types` for shared result/error types; `crate::daemon_url` and `crate::gobby_home` for local daemon discovery; and `reqwest` for blocking HTTP and multipart transport (`operations.rs:1-13`, `request.rs:1-7`, `transport.rs:1-47`). Its tests stand up local JSON-response servers, synthesize daemon bootstrap/token files, inspect request JSON/headers/multipart fields, and build `AiContext` values routed to `AiRouting::Daemon` (`tests.rs:1-100`).

| Fact | Value | Source |
| --- | --- | --- |
| Voice endpoint | `/api/voice/transcribe` | `operations.rs:10-13` |
| Vision endpoint | `/api/llm/vision/extract` | `operations.rs:10-13` |
| Text generation endpoint | `/api/llm/generate` | `operations.rs:10-13` |
| Embeddings endpoint | `/api/embeddings` | `operations.rs:10-13` |
| Local token file | `.gobby/local_cli_token` | `transport.rs:5-32`, `tests.rs:42-53` |
| Local token header | `X-Gobby-Local-Token` | `transport.rs:5-6`, `transport.rs:43-47` |
| Bootstrap keys used in tests | `daemon_port`, `bind_host` | `tests.rs:42-50` |

| Symbol | Kind | Role |
| --- | --- | --- |
| `DaemonTranscriptionOptions` | class | Options for daemon audio transcription/translation calls |
| `DaemonEmbeddingResult` | class | Daemon embedding result type |
| `transcribe_via_daemon` | function | Sends audio work to the daemon |
| `multipart_form_with_file` | function | Builds multipart upload forms |
| `text_request_body` | function | Builds text-generation JSON bodies |
| `read_local_cli_token` | function | Loads the local daemon auth token |
| `with_local_token` | function | Adds daemon auth header to requests |
| `spawn_server` | test helper | Starts a local JSON test server |
| `write_daemon_files` | test helper | Writes daemon bootstrap/token fixtures |
[crates/gcore/src/ai/daemon/operations.rs:20-72]
[crates/gcore/src/ai/daemon/request.rs:11-19]
[crates/gcore/src/ai/daemon/response.rs:7-9]
[crates/gcore/src/ai/daemon/tests.rs:15-24]
[crates/gcore/src/ai/daemon/transport.rs:8-12]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/src/ai/daemon/operations.rs\|crates/gcore/src/ai/daemon/operations.rs]] | `crates/gcore/src/ai/daemon/operations.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/daemon/request.rs\|crates/gcore/src/ai/daemon/request.rs]] | `crates/gcore/src/ai/daemon/request.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/daemon/response.rs\|crates/gcore/src/ai/daemon/response.rs]] | `crates/gcore/src/ai/daemon/response.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/daemon/tests.rs\|crates/gcore/src/ai/daemon/tests.rs]] | `crates/gcore/src/ai/daemon/tests.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/daemon/transport.rs\|crates/gcore/src/ai/daemon/transport.rs]] | `crates/gcore/src/ai/daemon/transport.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/daemon/types.rs\|crates/gcore/src/ai/daemon/types.rs]] | `crates/gcore/src/ai/daemon/types.rs` exposes 3 indexed API symbols. |

