---
title: crates/gcore/src/ai/embeddings.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/embeddings.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/embeddings.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/ai/embeddings.rs` exposes 12 indexed API symbols.

## How it fits

`crates/gcore/src/ai/embeddings.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `embed_one` | function | Sends a text string to an embedding API using the provided client and configuration, extracts and parses the first embedding vector from the response, and returns it as 'Vec<f32>'. [crates/gcore/src/ai/embeddings.rs:19-38] |
| `embed_batch` | function | Embeds a batch of strings via an API request and returns their corresponding float32 vector representations reordered by response indices with full response integrity validation. [crates/gcore/src/ai/embeddings.rs:42-92] |
| `send_request` | function | Sends a POST request with optional bearer token authentication to a configured embeddings API endpoint with a JSON body, returning the parsed JSON response or an AiError. [crates/gcore/src/ai/embeddings.rs:94-105] |
| `parse_embedding` | function | Parses a JSON embedding array field into a non-empty 'Vec<f32>', validating that all elements are finite numbers within f32 range, or returns an 'AiError'. [crates/gcore/src/ai/embeddings.rs:107-133] |
| `config` | function | Constructs an 'EmbeddingConfig' struct with a provided API base URL and optional API key, defaulting the model to "embed-small", timeout to 5 seconds, and query_prefix to None. [crates/gcore/src/ai/embeddings.rs:140-148] |

_Verified by 7 in-file unit tests._

