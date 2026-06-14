---
title: crates/gcore/src/ai/text.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/text.rs
  ranges:
  - 9-15
  - 17-35
  - 37-67
  - 69-87
  - 98-120
  - 123-134
  - 136-138
  - 140-143
  - 145-152
  - 154-171
  - 173-186
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/text.rs

Module: [[code/modules/crates/gcore/src/ai|crates/gcore/src/ai]]

## Purpose

This file provides the text-generation path for AI chat completions. `generate_text` is a thin convenience wrapper over `generate_text_with_max_tokens`, which creates an `AiTransport`, resolves the chat-completions URL for the `TextGenerate` capability, builds the JSON payload, sends the authenticated POST request, and assembles a `TextResult` from the returned content, model name, token usage, and empty metadata. The helper `request_body` formats the request messages from optional system context plus the required user prompt, while conditionally adding the binding’s model and a positive `max_tokens` limit. `chat_completion_usage` normalizes usage data from different provider field names into `TokenUsage`. The test helpers and unit tests spin up a stub server, inspect request headers and JSON body, and verify the request/response behavior and `max_tokens` forwarding.
[crates/gcore/src/ai/text.rs:9-15]
[crates/gcore/src/ai/text.rs:17-35]
[crates/gcore/src/ai/text.rs:37-67]
[crates/gcore/src/ai/text.rs:69-87]
[crates/gcore/src/ai/text.rs:98-120]

## API Symbols

- `generate_text` (function) component `generate_text [function]` (`f9a32cf9-4865-5138-a433-c0f172863579`) lines 9-15 [crates/gcore/src/ai/text.rs:9-15]
  - Signature: `pub fn generate_text(`
  - Purpose: Indexed function `generate_text` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:9-15]
- `generate_text_with_max_tokens` (function) component `generate_text_with_max_tokens [function]` (`7b004b07-cf59-5266-9ea7-80d74e487ca4`) lines 17-35 [crates/gcore/src/ai/text.rs:17-35]
  - Signature: `pub fn generate_text_with_max_tokens(`
  - Purpose: Generates text by submitting an authenticated request to a chat completions API endpoint with a prompt and optional system context/token constraints, returning the generated text content alongside model identifier and token usage metrics. [crates/gcore/src/ai/text.rs:17-35]
- `request_body` (function) component `request_body [function]` (`c387c64f-53bb-5033-b20e-064f3d54844e`) lines 37-67 [crates/gcore/src/ai/text.rs:37-67]
  - Signature: `fn request_body(`
  - Purpose: Constructs a JSON request body containing a messages array from optional system and required user prompts, with conditionally included model and max_tokens fields. [crates/gcore/src/ai/text.rs:37-67]
- `chat_completion_usage` (function) component `chat_completion_usage [function]` (`178cb967-e3e0-51d3-9c54-c26a6c9b6b7e`) lines 69-87 [crates/gcore/src/ai/text.rs:69-87]
  - Signature: `fn chat_completion_usage(value: &Value) -> Option<TokenUsage> {`
  - Purpose: Extracts and normalizes token usage metrics from a JSON value into a `TokenUsage` struct, with fallback support for alternate field names across different API providers. [crates/gcore/src/ai/text.rs:69-87]
- `generates_text` (function) component `generates_text [function]` (`bd3408f4-9a83-5a88-9272-ec3b99641133`) lines 98-120 [crates/gcore/src/ai/text.rs:98-120]
  - Signature: `fn generates_text() {`
  - Purpose: Unit test that verifies the `generate_text` function constructs a properly-authenticated POST request to a chat completion API endpoint with system and user messages, and correctly deserializes the response model name and token usage. [crates/gcore/src/ai/text.rs:98-120]
- `forwards_generation_max_tokens` (function) component `forwards_generation_max_tokens [function]` (`5492543a-95a9-5200-bf21-1bddf5f8a06e`) lines 123-134 [crates/gcore/src/ai/text.rs:123-134]
  - Signature: `fn forwards_generation_max_tokens() {`
  - Purpose: Indexed function `forwards_generation_max_tokens` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:123-134]
- `spawn_server` (function) component `spawn_server [function]` (`f19aff3c-9f59-5289-8e66-e53454a81e6f`) lines 136-138 [crates/gcore/src/ai/text.rs:136-138]
  - Signature: `fn spawn_server(response: &'static str) -> (String, RequestHandle) {`
  - Purpose: Spawns a test server configured to return the provided static JSON response string, returning a tuple of the server URL and a RequestHandle, or panicking if server creation fails. [crates/gcore/src/ai/text.rs:136-138]
- `request_body_json` (function) component `request_body_json [function]` (`92f24c15-e2d7-500e-91ce-03b2f5dacbc8`) lines 140-143 [crates/gcore/src/ai/text.rs:140-143]
  - Signature: `fn request_body_json(request: &str) -> Value {`
  - Purpose: Parses the JSON body portion of an HTTP request string (separated from headers by `\r\n\r\n`) into a `serde_json::Value`. [crates/gcore/src/ai/text.rs:140-143]
- `has_header` (function) component `has_header [function]` (`2f8cf29c-4c28-556f-bac8-6f97f18f2929`) lines 145-152 [crates/gcore/src/ai/text.rs:145-152]
  - Signature: `fn has_header(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: Returns `true` if the request contains a header line whose name matches the given name (case-insensitive) and whose trimmed value exactly equals the given value. [crates/gcore/src/ai/text.rs:145-152]
- `test_context` (function) component `test_context [function]` (`c0da1480-fcf6-59e5-9ed1-064a2011ccb8`) lines 154-171 [crates/gcore/src/ai/text.rs:154-171]
  - Signature: `fn test_context(api_base: &str, api_key: Option<&str>) -> AiContext {`
  - Purpose: Instantiates a test AiContext with a single shared API binding replicated across all AI operations and concurrency/rate limiting set to 1. [crates/gcore/src/ai/text.rs:154-171]
- `binding` (function) component `binding [function]` (`f138a8a7-4e65-545b-a963-ce997bf8ffde`) lines 173-186 [crates/gcore/src/ai/text.rs:173-186]
  - Signature: `fn binding(api_base: &str, api_key: Option<&str>) -> CapabilityBinding {`
  - Purpose: This function constructs and returns a `CapabilityBinding` configured for direct routing to a GPT-4.1-mini model using the provided API base URL and optional authentication key. [crates/gcore/src/ai/text.rs:173-186]

