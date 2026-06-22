---
title: crates/gcore/src/ai/daemon/types.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/daemon/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/daemon/types.rs

Module: [[code/modules/crates/gcore/src/ai/daemon|crates/gcore/src/ai/daemon]]

## Overview

`crates/gcore/src/ai/daemon/types.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gcore/src/ai/daemon/types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DaemonTranscriptionOptions` | class | 'DaemonTranscriptionOptions<'a>' is a configuration struct with lifetime parameter ''a' that bundles a required 'AiCapability' field and three optional borrowed string references for source language, target language, and custom prompt specification. [crates/gcore/src/ai/daemon/types.rs:4-9] |
| `DaemonEmbeddingResult` | class | 'DaemonEmbeddingResult' is a struct containing vector embeddings as a collection of f32 float arrays, along with metadata specifying the model used and embedding dimensionality. [crates/gcore/src/ai/daemon/types.rs:12-16] |
| `default` | function | This function returns a default instance with 'AiCapability::AudioTranscribe' as the capability while initializing 'language', 'target_lang', and 'prompt' fields to 'None'. [crates/gcore/src/ai/daemon/types.rs:19-26] |

