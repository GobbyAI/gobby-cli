---
title: crates/gcore/src/ai/text.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/text.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/text.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/ai/text.rs` exposes 11 indexed API symbols.

## How it fits

`crates/gcore/src/ai/text.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `generate_text` | function | 'generate_text' is a thin wrapper that forwards the provided AI context, prompt, and optional system prompt to 'generate_text_with_max_tokens' with no explicit max-token limit, returning its 'Result<TextResult, AiError>'. [crates/gcore/src/ai/text.rs:9-15] |
| `generate_text_with_max_tokens` | function | The 'generate_text_with_max_tokens' function constructs and sends a JSON POST request to a configured chat completions endpoint with an optional system prompt and token limit, returning a structured 'TextResult' containing the generated text, model identifier, and token usage. [crates/gcore/src/ai/text.rs:17-36] |
| `request_body` | function | The 'request_body' function constructs a JSON 'Value' representing an LLM request payload by compiling an optional non-empty system instruction and a user prompt into a messages array, and optionally appending model and maximum token configurations. [crates/gcore/src/ai/text.rs:38-68] |
| `chat_completion_usage` | function | The 'chat_completion_usage' function extracts token usage metrics from a JSON-like 'Value' reference's '"usage"' object, parsing input, output, and total token fields into 'usize' values to populate and return an optional 'TokenUsage' struct. [crates/gcore/src/ai/text.rs:70-88] |
| `spawn_server` | function | The 'spawn_server' function spawns a test server configured with a static JSON response, returning a tuple containing its address as a 'String' and a 'RequestHandle', while panicking if the server fails to initialize. [crates/gcore/src/ai/text.rs:137-139] |
| `request_body_json` | function | The 'request_body_json' function extracts the body of an HTTP request string by splitting it at the '\r\n\r\n' delimiter and parses it into a 'serde_json::Value', panicking if the body is missing or contains invalid JSON. [crates/gcore/src/ai/text.rs:141-144] |
| `has_header` | function | The 'has_header' function parses a multiline request string to determine if any line contains a colon-separated header name matching 'name' (ignoring ASCII case) and a trimmed header value matching 'value' exactly. [crates/gcore/src/ai/text.rs:146-153] |
| `test_context` | function | The 'test_context' function constructs and returns an 'AiContext' configured for testing by applying a single generated API binding to all AI capabilities, setting concurrency and rate limits to one, and omitting a project identifier. [crates/gcore/src/ai/text.rs:155-172] |
| `binding` | function | The 'binding' function constructs and returns a 'CapabilityBinding' struct initialized with direct routing, the model set to '"gpt-4.1-mini"', and the provided 'api_base' and optional 'api_key' converted into owned strings. [crates/gcore/src/ai/text.rs:174-192] |

_Verified by 2 in-file unit tests._

