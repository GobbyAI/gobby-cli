---
title: crates/gcore/src/ai/daemon/operations.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/daemon/operations.rs
  ranges:
  - 20-72
  - 74-112
  - 114-120
  - 125-163
  - 165-199
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/daemon/operations.rs

Module: [[code/modules/crates/gcore/src/ai/daemon|crates/gcore/src/ai/daemon]]

## Purpose

Provides daemon-backed AI operations for transcription, vision description, text generation, and embeddings. Each function builds a request from the active AI context and binding, attaches the local CLI token, acquires the shared rate-limit permit, retries the HTTP call with backoff, and parses the daemon’s JSON response into the corresponding result type. The generation helpers are split into a convenience wrapper and a max-token variant, while the other functions handle file/image uploads or embedding payloads with capability- and model-specific options.
[crates/gcore/src/ai/daemon/operations.rs:20-72]
[crates/gcore/src/ai/daemon/operations.rs:74-112]
[crates/gcore/src/ai/daemon/operations.rs:114-120]
[crates/gcore/src/ai/daemon/operations.rs:125-163]
[crates/gcore/src/ai/daemon/operations.rs:165-199]

## API Symbols

- `transcribe_via_daemon` (function) component `transcribe_via_daemon [function]` (`d0c884c3-2413-5359-8687-746b3c4ea4f0`) lines 20-72 [crates/gcore/src/ai/daemon/operations.rs:20-72]
  - Signature: `pub fn transcribe_via_daemon(`
  - Purpose: Submits the given audio bytes as a multipart POST to the local transcription daemon with merged binding and per-call options, authenticated by a local CLI token and rate-limited with retry/backoff, then parses the JSON transcription result or returns an 'AiError'. [crates/gcore/src/ai/daemon/operations.rs:20-72]
- `describe_image_via_daemon` (function) component `describe_image_via_daemon [function]` (`319b3f75-14cc-571b-9975-5a387539338f`) lines 74-112 [crates/gcore/src/ai/daemon/operations.rs:74-112]
  - Signature: `pub fn describe_image_via_daemon(`
  - Purpose: Sends the given image bytes as a multipart POST to the vision-extraction daemon with local-token auth, optional provider/model/project_id fields, retry/backoff and rate limiting, then parses the JSON response into a 'VisionResult'. [crates/gcore/src/ai/daemon/operations.rs:74-112]
- `generate_via_daemon` (function) component `generate_via_daemon [function]` (`b31d70ad-af61-55f9-8d05-95f978bbac2a`) lines 114-120 [crates/gcore/src/ai/daemon/operations.rs:114-120]
  - Signature: `pub fn generate_via_daemon(`
  - Purpose: 'generate_via_daemon' is a thin wrapper that forwards 'cfg', 'prompt', and 'system' to 'generate_via_daemon_with_max_tokens' with both optional token-limit arguments set to 'None', returning its 'Result<TextResult, AiError>'. [crates/gcore/src/ai/daemon/operations.rs:114-120]
- `generate_via_daemon_with_max_tokens` (function) component `generate_via_daemon_with_max_tokens [function]` (`d0f0c56e-87d9-5ed4-bb4a-75194e163426`) lines 125-163 [crates/gcore/src/ai/daemon/operations.rs:125-163]
  - Signature: `pub fn generate_via_daemon_with_max_tokens(`
  - Purpose: Sends a text-generation request to the daemon using the configured provider/model, optional system prompt, max token limit, and profile, with local CLI token auth, rate limiting, retry/backoff, and JSON response parsing into 'TextResult'. [crates/gcore/src/ai/daemon/operations.rs:125-163]
- `embed_via_daemon` (function) component `embed_via_daemon [function]` (`9d5431ab-69e6-5fa2-8a27-24da33201ad1`) lines 165-199 [crates/gcore/src/ai/daemon/operations.rs:165-199]
  - Signature: `pub fn embed_via_daemon(`
  - Purpose: Sends an embeddings request to the local daemon using the configured provider/model and local CLI token, retries the HTTP call with backoff under a rate-limit permit, then parses the JSON response into a 'DaemonEmbeddingResult' matching the input length. [crates/gcore/src/ai/daemon/operations.rs:165-199]

