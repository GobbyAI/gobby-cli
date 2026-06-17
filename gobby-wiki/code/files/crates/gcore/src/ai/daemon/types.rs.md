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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/ai/daemon/types.rs:4-9](crates/gcore/src/ai/daemon/types.rs#L4-L9), [crates/gcore/src/ai/daemon/types.rs:12-16](crates/gcore/src/ai/daemon/types.rs#L12-L16), [crates/gcore/src/ai/daemon/types.rs:19-26](crates/gcore/src/ai/daemon/types.rs#L19-L26)

</details>

# crates/gcore/src/ai/daemon/types.rs

Module: [[code/modules/crates/gcore/src/ai/daemon|crates/gcore/src/ai/daemon]]

## Purpose

Defines the daemon-facing AI request/result types used by `gcore`: `DaemonTranscriptionOptions` carries transcription settings such as capability, language, target language, and prompt, while `DaemonEmbeddingResult` packages returned embedding vectors with the model name and embedding dimension. The `Default` implementation for `DaemonTranscriptionOptions` sets audio transcription as the capability and leaves the optional text fields unset, giving callers a standard baseline configuration.
[crates/gcore/src/ai/daemon/types.rs:4-9]
[crates/gcore/src/ai/daemon/types.rs:12-16]
[crates/gcore/src/ai/daemon/types.rs:19-26]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `DaemonTranscriptionOptions` | class | `pub struct DaemonTranscriptionOptions<'a> {` | `DaemonTranscriptionOptions [class]` | `13725456-b5c6-537d-8349-0f3c9903d6b7` | 4-9 [crates/gcore/src/ai/daemon/types.rs:4-9] | Indexed class `DaemonTranscriptionOptions` in `crates/gcore/src/ai/daemon/types.rs`. [crates/gcore/src/ai/daemon/types.rs:4-9] |
| `DaemonEmbeddingResult` | class | `pub struct DaemonEmbeddingResult {` | `DaemonEmbeddingResult [class]` | `6ebbca9e-23bb-56f8-abca-2ebba5e8fba6` | 12-16 [crates/gcore/src/ai/daemon/types.rs:12-16] | Indexed class `DaemonEmbeddingResult` in `crates/gcore/src/ai/daemon/types.rs`. [crates/gcore/src/ai/daemon/types.rs:12-16] |
| `default` | function | `fn default() -> Self {` | `default [function]` | `cd56bd49-5236-58a0-83a2-239967ee67e6` | 19-26 [crates/gcore/src/ai/daemon/types.rs:19-26] | Indexed function `default` in `crates/gcore/src/ai/daemon/types.rs`. [crates/gcore/src/ai/daemon/types.rs:19-26] |
