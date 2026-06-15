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

# crates/gcore/src/ai/daemon/response.rs

Module: [[code/modules/crates/gcore/src/ai/daemon|crates/gcore/src/ai/daemon]]

## Purpose

Parses JSON responses from the AI daemon into strongly typed results. It forwards transcription payloads to `TranscriptionResult::from_wire_json`, and for embeddings it validates the top-level `model`, `dim`, and `embeddings` fields, checks the number of returned vectors matches the number of inputs, and converts each embedding array into a `Vec<f32>` with dimension and type validation before building `DaemonEmbeddingResult`.
[crates/gcore/src/ai/daemon/response.rs:7-9]
[crates/gcore/src/ai/daemon/response.rs:11-47]
[crates/gcore/src/ai/daemon/response.rs:49-68]

## API Symbols

- `parse_daemon_transcription` (function) component `parse_daemon_transcription [function]` (`7dd0f73d-1187-5b41-a71c-eaee2dc16c71`) lines 7-9 [crates/gcore/src/ai/daemon/response.rs:7-9]
  - Signature: `pub(super) fn parse_daemon_transcription(value: Value) -> Result<TranscriptionResult, AiError> {`
  - Purpose: Delegates deserialization of a wire-format 'serde_json::Value' into a 'TranscriptionResult', returning the result or an 'AiError'. [crates/gcore/src/ai/daemon/response.rs:7-9]
- `parse_daemon_embeddings` (function) component `parse_daemon_embeddings [function]` (`19bdcb6c-45a0-5843-b12d-1977dbf80453`) lines 11-47 [crates/gcore/src/ai/daemon/response.rs:11-47]
  - Signature: `pub(super) fn parse_daemon_embeddings(`
  - Purpose: Parses a daemon embedding JSON response by extracting 'model' and 'dim', validating that 'embeddings' is an array of the expected length, converting each entry with 'parse_daemon_embedding', and returning a 'DaemonEmbeddingResult' or a parse error. [crates/gcore/src/ai/daemon/response.rs:11-47]
- `parse_daemon_embedding` (function) component `parse_daemon_embedding [function]` (`7d800a4d-337f-5319-a8e0-bc737aaa1510`) lines 49-68 [crates/gcore/src/ai/daemon/response.rs:49-68]
  - Signature: `fn parse_daemon_embedding(value: &Value, dim: usize) -> Result<Vec<f32>, AiError> {`
  - Purpose: Validates that a JSON 'Value' is an array of numeric elements, converts each element to 'f32', and returns an error if the value is not an array, contains a non-number, or its length differs from 'dim'. [crates/gcore/src/ai/daemon/response.rs:49-68]

