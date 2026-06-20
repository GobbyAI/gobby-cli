---
title: crates/gcore/src/ai/daemon/request.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/daemon/request.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/daemon/request.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/ai/daemon/request.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gcore/src/ai/daemon/request.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `audio_capability` | function | The 'audio_capability' function validates a given 'AiCapability', returning it unmodified if it is 'AudioTranscribe' or 'AudioTranslate', and returning an 'AiError::capability_unavailable' error for any other variant. [crates/gcore/src/ai/daemon/request.rs:11-19] |
| `multipart_form_with_file` | function | This function constructs a 'multipart::Form' containing a single file part initialized from the provided 'Bytes' buffer, file name, and MIME type, or returns an 'AiError' if the payload length overflows 'u64' or the MIME type is invalid. [crates/gcore/src/ai/daemon/request.rs:21-41] |
| `add_optional_text` | function | This function conditionally appends a text field with the specified static name and stringified value to a multipart form if the optional string slice is non-empty, otherwise returning the form unchanged. [crates/gcore/src/ai/daemon/request.rs:43-52] |
| `TextRequestOptions` | class | 'TextRequestOptions' is a module-private Rust struct parameterized by a lifetime that holds optional configuration settings for a text generation request, including the target provider, model, project ID, maximum token limit, active profile, candidate features, and reasoning effort. [crates/gcore/src/ai/daemon/request.rs:54-62] |
| `text_request_body` | function | The 'text_request_body' function constructs and returns a JSON 'Value' representing a text generation request body by populating a 'serde_json::Map' with the prompt, an optional system prompt, and conditional parameters from the provided 'TextRequestOptions' (such as provider, model, profile, candidates, reasoning effort, project ID, and token limits). [crates/gcore/src/ai/daemon/request.rs:64-105] |
| `embeddings_request_body` | function | This function constructs and returns a JSON object representing an embeddings request body, mapping the provided list of input strings, query flag, and optional project, provider, and model parameters into a 'serde_json::Value' map. [crates/gcore/src/ai/daemon/request.rs:107-124] |
| `insert_optional` | function | Inserts an optional string slice as a 'Value::String' into a mutable map under the specified key if the value is present and non-empty. [crates/gcore/src/ai/daemon/request.rs:126-130] |
| `non_empty` | function | The 'non_empty' function trims leading and trailing whitespace from an optional string slice and returns it as 'Some(&str)' if the resulting slice is not empty, otherwise returning 'None'. [crates/gcore/src/ai/daemon/request.rs:132-134] |

