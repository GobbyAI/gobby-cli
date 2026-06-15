---
title: crates/gcore/src/ai/daemon/types.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/daemon/types.rs
  ranges:
  - 4-9
  - 12-16
  - 19-26
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/daemon/types.rs

Module: [[code/modules/crates/gcore/src/ai/daemon|crates/gcore/src/ai/daemon]]

## Purpose

Defines shared daemon AI data types: `DaemonTranscriptionOptions` packages an `AiCapability` with optional borrowed language, target-language, and prompt fields for transcription requests, and its `Default` impl selects `AudioTranscribe` with no extra text parameters. `DaemonEmbeddingResult` holds embedding batches along with the model name and vector dimensionality, so the daemon can return structured embedding outputs.
[crates/gcore/src/ai/daemon/types.rs:4-9]
[crates/gcore/src/ai/daemon/types.rs:12-16]
[crates/gcore/src/ai/daemon/types.rs:19-26]

## API Symbols

- `DaemonTranscriptionOptions` (class) component `DaemonTranscriptionOptions [class]` (`13725456-b5c6-537d-8349-0f3c9903d6b7`) lines 4-9 [crates/gcore/src/ai/daemon/types.rs:4-9]
  - Signature: `pub struct DaemonTranscriptionOptions<'a> {`
  - Purpose: 'DaemonTranscriptionOptions<'a>' is a transcription request options struct carrying an 'AiCapability' plus optional borrowed string parameters for source language, target language, and prompt text. [crates/gcore/src/ai/daemon/types.rs:4-9]
- `DaemonEmbeddingResult` (class) component `DaemonEmbeddingResult [class]` (`6ebbca9e-23bb-56f8-abca-2ebba5e8fba6`) lines 12-16 [crates/gcore/src/ai/daemon/types.rs:12-16]
  - Signature: `pub struct DaemonEmbeddingResult {`
  - Purpose: 'DaemonEmbeddingResult' is a result struct containing a batch of embedding vectors as 'Vec<Vec<f32>>', the embedding model identifier as 'String', and the embedding dimensionality as 'usize'. [crates/gcore/src/ai/daemon/types.rs:12-16]
- `default` (function) component `default [function]` (`cd56bd49-5236-58a0-83a2-239967ee67e6`) lines 19-26 [crates/gcore/src/ai/daemon/types.rs:19-26]
  - Signature: `fn default() -> Self {`
  - Purpose: Returns a default instance initialized for 'AiCapability::AudioTranscribe' with 'language', 'target_lang', and 'prompt' all set to 'None'. [crates/gcore/src/ai/daemon/types.rs:19-26]

