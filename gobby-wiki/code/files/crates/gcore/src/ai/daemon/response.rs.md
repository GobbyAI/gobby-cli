---
title: crates/gcore/src/ai/daemon/response.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/daemon/response.rs
  ranges:
  - 7-9
  - 11-47
  - 49-68
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/ai/daemon/response.rs:7-9](crates/gcore/src/ai/daemon/response.rs#L7-L9), [crates/gcore/src/ai/daemon/response.rs:11-47](crates/gcore/src/ai/daemon/response.rs#L11-L47), [crates/gcore/src/ai/daemon/response.rs:49-68](crates/gcore/src/ai/daemon/response.rs#L49-L68)

</details>

# crates/gcore/src/ai/daemon/response.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Parses AI daemon JSON responses into typed results for transcription and embeddings. `parse_daemon_transcription` delegates transcription decoding to `TranscriptionResult::from_wire_json`, while `parse_daemon_embeddings` validates the embedding response shape by checking `model`, `dim`, and the number of returned vectors before converting each embedding array into a `Vec<f32>` with `parse_daemon_embedding`. The helper `parse_daemon_embedding` enforces that each embedding is an array of numbers and that its length matches the declared dimension, returning `AiError` parse failures for malformed input.
[crates/gcore/src/ai/daemon/response.rs:7-9]
[crates/gcore/src/ai/daemon/response.rs:11-47]
[crates/gcore/src/ai/daemon/response.rs:49-68]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `parse_daemon_transcription` | function | `pub(super) fn parse_daemon_transcription(value: Value) -> Result<TranscriptionResult, AiError> {` | `parse_daemon_transcription [function]` | `7dd0f73d-1187-5b41-a71c-eaee2dc16c71` | 7-9 [crates/gcore/src/ai/daemon/response.rs:7-9] | Indexed function `parse_daemon_transcription` in `crates/gcore/src/ai/daemon/response.rs`. [crates/gcore/src/ai/daemon/response.rs:7-9] |
| `parse_daemon_embeddings` | function | `pub(super) fn parse_daemon_embeddings(` | `parse_daemon_embeddings [function]` | `19bdcb6c-45a0-5843-b12d-1977dbf80453` | 11-47 [crates/gcore/src/ai/daemon/response.rs:11-47] | Indexed function `parse_daemon_embeddings` in `crates/gcore/src/ai/daemon/response.rs`. [crates/gcore/src/ai/daemon/response.rs:11-47] |
| `parse_daemon_embedding` | function | `fn parse_daemon_embedding(value: &Value, dim: usize) -> Result<Vec<f32>, AiError> {` | `parse_daemon_embedding [function]` | `7d800a4d-337f-5319-a8e0-bc737aaa1510` | 49-68 [crates/gcore/src/ai/daemon/response.rs:49-68] | Indexed function `parse_daemon_embedding` in `crates/gcore/src/ai/daemon/response.rs`. [crates/gcore/src/ai/daemon/response.rs:49-68] |
