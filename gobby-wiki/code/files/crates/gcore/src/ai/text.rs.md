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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/ai/text.rs:9-15](crates/gcore/src/ai/text.rs#L9-L15), [crates/gcore/src/ai/text.rs:17-35](crates/gcore/src/ai/text.rs#L17-L35), [crates/gcore/src/ai/text.rs:37-67](crates/gcore/src/ai/text.rs#L37-L67), [crates/gcore/src/ai/text.rs:69-87](crates/gcore/src/ai/text.rs#L69-L87), [crates/gcore/src/ai/text.rs:98-120](crates/gcore/src/ai/text.rs#L98-L120), [crates/gcore/src/ai/text.rs:123-134](crates/gcore/src/ai/text.rs#L123-L134), [crates/gcore/src/ai/text.rs:136-138](crates/gcore/src/ai/text.rs#L136-L138), [crates/gcore/src/ai/text.rs:140-143](crates/gcore/src/ai/text.rs#L140-L143), [crates/gcore/src/ai/text.rs:145-152](crates/gcore/src/ai/text.rs#L145-L152), [crates/gcore/src/ai/text.rs:154-171](crates/gcore/src/ai/text.rs#L154-L171), [crates/gcore/src/ai/text.rs:173-186](crates/gcore/src/ai/text.rs#L173-L186)

</details>

# crates/gcore/src/ai/text.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Provides the text-generation client flow for `AiContext`: `generate_text` is a convenience wrapper over `generate_text_with_max_tokens`, which selects the text-generation capability, builds a chat-completions request, posts it through the AI transport, and returns a `TextResult` with extracted content, model, usage, and empty metadata. The private helpers assemble the JSON body from the binding, prompt, optional system message, and optional max token limit, parse token usage from either OpenAI-style or alternate usage fields, and support tests that verify generation, max-token forwarding, request-body shape, headers, context setup, and binding behavior.
[crates/gcore/src/ai/text.rs:9-15]
[crates/gcore/src/ai/text.rs:17-35]
[crates/gcore/src/ai/text.rs:37-67]
[crates/gcore/src/ai/text.rs:69-87]
[crates/gcore/src/ai/text.rs:98-120]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `generate_text` | function | `pub fn generate_text(` | `generate_text [function]` | `f9a32cf9-4865-5138-a433-c0f172863579` | 9-15 [crates/gcore/src/ai/text.rs:9-15] | Indexed function `generate_text` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:9-15] |
| `generate_text_with_max_tokens` | function | `pub fn generate_text_with_max_tokens(` | `generate_text_with_max_tokens [function]` | `7b004b07-cf59-5266-9ea7-80d74e487ca4` | 17-35 [crates/gcore/src/ai/text.rs:17-35] | Indexed function `generate_text_with_max_tokens` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:17-35] |
| `request_body` | function | `fn request_body(` | `request_body [function]` | `c387c64f-53bb-5033-b20e-064f3d54844e` | 37-67 [crates/gcore/src/ai/text.rs:37-67] | Indexed function `request_body` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:37-67] |
| `chat_completion_usage` | function | `fn chat_completion_usage(value: &Value) -> Option<TokenUsage> {` | `chat_completion_usage [function]` | `178cb967-e3e0-51d3-9c54-c26a6c9b6b7e` | 69-87 [crates/gcore/src/ai/text.rs:69-87] | Indexed function `chat_completion_usage` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:69-87] |
| `generates_text` | function | `fn generates_text() {` | `generates_text [function]` | `bd3408f4-9a83-5a88-9272-ec3b99641133` | 98-120 [crates/gcore/src/ai/text.rs:98-120] | Indexed function `generates_text` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:98-120] |
| `forwards_generation_max_tokens` | function | `fn forwards_generation_max_tokens() {` | `forwards_generation_max_tokens [function]` | `5492543a-95a9-5200-bf21-1bddf5f8a06e` | 123-134 [crates/gcore/src/ai/text.rs:123-134] | Indexed function `forwards_generation_max_tokens` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:123-134] |
| `spawn_server` | function | `fn spawn_server(response: &'static str) -> (String, RequestHandle) {` | `spawn_server [function]` | `f19aff3c-9f59-5289-8e66-e53454a81e6f` | 136-138 [crates/gcore/src/ai/text.rs:136-138] | Indexed function `spawn_server` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:136-138] |
| `request_body_json` | function | `fn request_body_json(request: &str) -> Value {` | `request_body_json [function]` | `92f24c15-e2d7-500e-91ce-03b2f5dacbc8` | 140-143 [crates/gcore/src/ai/text.rs:140-143] | Indexed function `request_body_json` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:140-143] |
| `has_header` | function | `fn has_header(request: &str, name: &str, value: &str) -> bool {` | `has_header [function]` | `2f8cf29c-4c28-556f-bac8-6f97f18f2929` | 145-152 [crates/gcore/src/ai/text.rs:145-152] | Indexed function `has_header` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:145-152] |
| `test_context` | function | `fn test_context(api_base: &str, api_key: Option<&str>) -> AiContext {` | `test_context [function]` | `c0da1480-fcf6-59e5-9ed1-064a2011ccb8` | 154-171 [crates/gcore/src/ai/text.rs:154-171] | Indexed function `test_context` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:154-171] |
| `binding` | function | `fn binding(api_base: &str, api_key: Option<&str>) -> CapabilityBinding {` | `binding [function]` | `f138a8a7-4e65-545b-a963-ce997bf8ffde` | 173-186 [crates/gcore/src/ai/text.rs:173-186] | Indexed function `binding` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:173-186] |
