---
title: crates/gcode/src/vector/code_symbols/embedding.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/embedding.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols/embedding.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Overview

`crates/gcode/src/vector/code_symbols/embedding.rs` exposes 28 indexed API symbols.

## How it fits

`crates/gcode/src/vector/code_symbols/embedding.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `dimension_probe_text` | function | Returns the 'DIMENSION_PROBE_TEXT' constant as a '&'static str'. [crates/gcode/src/vector/code_symbols/embedding.rs:21-23] |
| `EmbeddingSource` | type | Indexed type `EmbeddingSource` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:26-29] |
| `EmbeddingSource::from` | method | Converts an 'EmbeddingConfig' into 'Self' by wrapping it in the 'Self::Direct' variant. [crates/gcode/src/vector/code_symbols/embedding.rs:32-34] |
| `EmbeddingSource::from` | method | Constructs 'Self' by boxing the provided 'AiContext' and wrapping it in the 'Daemon' variant. [crates/gcode/src/vector/code_symbols/embedding.rs:38-40] |
| `EmbeddingBackend` | class | 'EmbeddingBackend' is a backend wrapper that owns an 'EmbeddingSource' and an optional 'reqwest::blocking::Client' for making direct embedding requests. [crates/gcode/src/vector/code_symbols/embedding.rs:44-47] |
| `EmbeddingBackend::new` | method | Constructs a 'Self' from an 'EmbeddingSource', eagerly creating and storing a direct embedding client only for 'EmbeddingSource::Direct' when 'api_base' is nonempty, otherwise returning 'VectorLifecycleError::MissingEmbeddingConfig' for an empty direct config or 'None' for daemon-backed sources. [crates/gcode/src/vector/code_symbols/embedding.rs:50-64] |
| `EmbeddingBackend::embed_text` | method | 'embed_text' converts the input string into a single-item batch, delegates to 'embed_text_batch', and returns the sole embedding vector or a 'VectorLifecycleError::EmbeddingResponse' if the batch response is empty. [crates/gcode/src/vector/code_symbols/embedding.rs:66-72] |
| `EmbeddingBackend::embed_query` | method | Embeds a single query string by optionally prepending a trimmed query prefix and then either calling the initialized direct embedding client or delegating to the daemon path, returning the first embedding vector or a 'VectorLifecycleError' if initialization, transport, or response extraction fails. [crates/gcode/src/vector/code_symbols/embedding.rs:74-101] |
| `EmbeddingBackend::embed_text_batch` | method | Dispatches a batch of input strings to either a direct embedding client or a daemon-backed embedding path and returns the resulting 'Vec<Vec<f32>>', converting missing-client and daemon errors into 'VectorLifecycleError::EmbeddingResponse'. [crates/gcode/src/vector/code_symbols/embedding.rs:103-120] |
| `embedding_source_from_context` | function | Resolves the embedding AI context from 'ctx' and converts the resulting resolved context plus direct config into an 'Option<EmbeddingSource>' via 'embedding_source_from_resolved_ai_context'. [crates/gcode/src/vector/code_symbols/embedding.rs:123-126] |
| `embedding_source_from_resolved_ai_context` | function | Returns an 'Option<EmbeddingSource>' by routing the given 'AiContext' for 'AiCapability::Embed', yielding 'None' for 'Off' or 'Auto', wrapping the context in 'EmbeddingSource::Daemon' for 'Daemon', and using 'direct_config' as 'EmbeddingSource::Direct' only for 'Direct'. [crates/gcode/src/vector/code_symbols/embedding.rs:128-140] |
| `ResolvedEmbeddingAiContext` | class | 'ResolvedEmbeddingAiContext' is a struct that pairs an 'AiContext' with an optional 'EmbeddingConfig' override or direct configuration. [crates/gcode/src/vector/code_symbols/embedding.rs:142-145] |
| `resolve_embedding_ai_context` | function | Resolves an embedding AI context by loading standalone and project-specific config, preferring a read-only Postgres-backed AI config source when available, otherwise falling back to a no-primary source and overriding embed bindings from 'ctx.embedding', then derives 'direct_config' from the resolved embed binding with a fallback to 'ctx.embedding'. [crates/gcode/src/vector/code_symbols/embedding.rs:147-179] |
| `embedding_client` | function | Returns a cached or newly built 'reqwest::blocking::Client' configured with 'config.timeout_seconds', using a global mutex-protected map keyed only by timeout and converting client निर्माण failures into 'VectorLifecycleError::EmbeddingResponse'. [crates/gcode/src/vector/code_symbols/embedding.rs:181-203] |
| `embed_text` | function | Calls 'gobby_core::ai::embeddings::embed_one' with a blocking 'reqwest::Client', an 'EmbeddingConfig', and input text to produce a single 'Vec<f32>' embedding, mapping any failure into 'VectorLifecycleError' via 'embedding_error'. [crates/gcode/src/vector/code_symbols/embedding.rs:205-211] |
| `probe_embedding_dim` | function | Creates an embedding client from the provided config and returns the dimensionality of the embedding produced for a fixed probe text, propagating any 'VectorLifecycleError' from client creation or embedding. [crates/gcode/src/vector/code_symbols/embedding.rs:213-216] |
| `embed_text_batch` | function | Wraps 'gobby_core::ai::embeddings::embed_batch' to compute embeddings for a batch of input strings using a blocking 'reqwest' client and 'EmbeddingConfig', converting any error into 'VectorLifecycleError'. [crates/gcode/src/vector/code_symbols/embedding.rs:218-224] |
| `embedding_error` | function | Converts an 'AiError' into a 'VectorLifecycleError', mapping HTTP status, rate-limit, and transport failures with available status/body into 'EmbeddingHttp' and all other errors into 'EmbeddingResponse' using the error’s string representation. [crates/gcode/src/vector/code_symbols/embedding.rs:226-247] |
| `embed_query` | function | Builds the query embedding input by optionally prepending a trimmed 'query_prefix' to 'text', initializes an embedding client from 'config', and returns the computed 'Vec<f32>' embedding or 'None' after logging any client or embedding failure to stderr. [crates/gcode/src/vector/code_symbols/embedding.rs:249-270] |
| `embed_query_with_source` | function | Creates an 'EmbeddingBackend' from the provided 'EmbeddingSource', logs any initialization or query-embedding error to stderr, and returns the query embedding as 'Some(Vec<f32>)' or 'None' on failure. [crates/gcode/src/vector/code_symbols/embedding.rs:272-287] |
| `vector_text_for_symbol` | function | Builds a newline-separated textual representation of a 'Symbol' containing its name, qualified name, kind, language, file path, and line range, plus non-empty signature, docstring, and summary fields when present. [crates/gcode/src/vector/code_symbols/embedding.rs:289-320] |
| `TestSource` | class | 'TestSource' is a data-only struct that stores a 'HashMap<&'static str, &'static str>' mapping static string keys to static string values. [crates/gcode/src/vector/code_symbols/embedding.rs:331-333] |
| `TestSource::with_values` | method | Constructs 'Self' by consuming an 'IntoIterator' of '(&'static str, &'static str)' pairs and collecting them into the 'values' field. [crates/gcode/src/vector/code_symbols/embedding.rs:336-340] |
| `TestSource::config_value` | method | Returns a cloned 'String' for 'key' from 'self.values' if present, otherwise 'None', by looking up the stored reference and converting it to an owned string. [crates/gcode/src/vector/code_symbols/embedding.rs:344-346] |

_1 more symbol(s) not shown — run `gcode outline crates/gcode/src/vector/code_symbols/embedding.rs` for the full list._

_Verified by 3 in-file unit tests._

