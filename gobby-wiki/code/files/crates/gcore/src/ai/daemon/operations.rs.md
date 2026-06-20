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

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/ai/daemon/operations.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gcore/src/ai/daemon/operations.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `transcribe_via_daemon` | function | The 'transcribe_via_daemon' function transmits audio data and associated metadata to a local daemon's voice transcription endpoint via a multipart HTTP POST request authorized with a local token, utilizing rate limiting and retry-with-backoff to return a transcription result. [crates/gcore/src/ai/daemon/operations.rs:20-72] |
| `describe_image_via_daemon` | function | This function sends image data and configuration metadata to a local daemon's vision extraction endpoint using an authenticated, rate-limited multipart HTTP POST request with retry-with-backoff logic, returning the parsed 'VisionResult'. [crates/gcore/src/ai/daemon/operations.rs:74-112] |
| `generate_via_daemon` | function | The 'generate_via_daemon' function delegates text generation to 'generate_via_daemon_with_max_tokens' using the provided context, prompt, and optional system prompt, returning a 'Result' of 'TextResult' or 'AiError' with default limits. [crates/gcore/src/ai/daemon/operations.rs:114-120] |
| `generate_via_daemon_with_max_tokens` | function | This function sends an authorized POST request containing the prompt, system instructions, and optional model constraints to a local daemon's text generation endpoint under a rate limiter with backoff retries, returning the parsed 'TextResult'. [crates/gcore/src/ai/daemon/operations.rs:125-167] |
| `embed_via_daemon` | function | The 'embed_via_daemon' function authenticates and sends a rate-limited HTTP POST request to a local daemon to generate text embeddings for a slice of input strings, retrying with backoff on failure, and parses the resulting JSON response into a 'DaemonEmbeddingResult'. [crates/gcore/src/ai/daemon/operations.rs:169-203] |

