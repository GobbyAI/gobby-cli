---
title: crates/gcore/src/ai/daemon/response.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/daemon/response.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/daemon/response.rs

Module: [[code/modules/crates/gcore/src/ai/daemon|crates/gcore/src/ai/daemon]]

## Overview

`crates/gcore/src/ai/daemon/response.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gcore/src/ai/daemon/response.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `parse_daemon_transcription` | function | Deserializes a JSON 'Value' into a 'TranscriptionResult' by delegating to 'TranscriptionResult::from_wire_json', returning an 'AiError' on deserialization failure. [crates/gcore/src/ai/daemon/response.rs:7-9] |
| `parse_daemon_embeddings` | function | Parses and validates a daemon embedding response JSON by extracting the model name, dimension, and embeddings array, ensuring the embedding count matches the expected input length. [crates/gcore/src/ai/daemon/response.rs:11-47] |
| `parse_daemon_embedding` | function | Parses a JSON array value into an f32 vector, validating that all elements are numeric and the resulting vector dimensionality matches the expected size. [crates/gcore/src/ai/daemon/response.rs:49-68] |

