---
title: crates/gcore/src/ai/daemon/operations.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/daemon/operations.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/daemon/operations.rs

Module: [[code/modules/crates/gcore/src/ai/daemon|crates/gcore/src/ai/daemon]]

## Overview

`crates/gcore/src/ai/daemon/operations.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gcore/src/ai/daemon/operations.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `transcribe_via_daemon` | function | # Summary Executes audio transcription by posting a multipart form containing audio bytes and transcription parameters (language, model, provider, prompt) to a local daemon service endpoint with retry-with-backoff, rate limiting, and local token authentication. [crates/gcore/src/ai/daemon/operations.rs:20-72] |
| `describe_image_via_daemon` | function | Sends image bytes to a daemon vision extraction service via authenticated multipart HTTP POST request with exponential backoff retry, deserializing the JSON response into a VisionResult. [crates/gcore/src/ai/daemon/operations.rs:74-112] |
| `generate_via_daemon` | function | Generates text via a daemon process by delegating to 'generate_via_daemon_with_max_tokens' with the provided AI context, prompt, and optional system message, returning 'Result<TextResult, AiError>'. [crates/gcore/src/ai/daemon/operations.rs:114-120] |
| `generate_via_daemon_with_max_tokens` | function | Generates text through a daemon process with configurable maximum token limits, optional system prompt, and profile, returning a 'Result<TextResult, AiError>'. [crates/gcore/src/ai/daemon/operations.rs:125-133] |
| `generate_via_daemon_with_candidates` | function | Generates text via a daemon process with generation constrained by feature candidates, given a prompt, optional system message, and token limits. [crates/gcore/src/ai/daemon/operations.rs:140-148] |
| `generate_text_via_daemon` | function | This function generates text by sending an authenticated HTTP POST request to a daemon service, routing to specified feature candidates or configuration-bound provider/model pairs with rate limiting and automatic retry-with-backoff. [crates/gcore/src/ai/daemon/operations.rs:150-205] |
| `embed_via_daemon` | function | Generates embeddings for a batch of input strings by posting an authenticated request to a local daemon endpoint with rate-limiting and exponential backoff retry logic. [crates/gcore/src/ai/daemon/operations.rs:207-241] |

