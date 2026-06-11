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

`crates/gcore/src/ai/text.rs` exposes 11 indexed API symbols.
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
  - Purpose: Indexed function `generate_text_with_max_tokens` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:17-35]
- `request_body` (function) component `request_body [function]` (`c387c64f-53bb-5033-b20e-064f3d54844e`) lines 37-67 [crates/gcore/src/ai/text.rs:37-67]
  - Signature: `fn request_body(`
  - Purpose: Indexed function `request_body` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:37-67]
- `chat_completion_usage` (function) component `chat_completion_usage [function]` (`178cb967-e3e0-51d3-9c54-c26a6c9b6b7e`) lines 69-87 [crates/gcore/src/ai/text.rs:69-87]
  - Signature: `fn chat_completion_usage(value: &Value) -> Option<TokenUsage> {`
  - Purpose: Indexed function `chat_completion_usage` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:69-87]
- `generates_text` (function) component `generates_text [function]` (`bd3408f4-9a83-5a88-9272-ec3b99641133`) lines 98-120 [crates/gcore/src/ai/text.rs:98-120]
  - Signature: `fn generates_text() {`
  - Purpose: Indexed function `generates_text` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:98-120]
- `forwards_generation_max_tokens` (function) component `forwards_generation_max_tokens [function]` (`5492543a-95a9-5200-bf21-1bddf5f8a06e`) lines 123-134 [crates/gcore/src/ai/text.rs:123-134]
  - Signature: `fn forwards_generation_max_tokens() {`
  - Purpose: Indexed function `forwards_generation_max_tokens` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:123-134]
- `spawn_server` (function) component `spawn_server [function]` (`f19aff3c-9f59-5289-8e66-e53454a81e6f`) lines 136-138 [crates/gcore/src/ai/text.rs:136-138]
  - Signature: `fn spawn_server(response: &'static str) -> (String, RequestHandle) {`
  - Purpose: Indexed function `spawn_server` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:136-138]
- `request_body_json` (function) component `request_body_json [function]` (`92f24c15-e2d7-500e-91ce-03b2f5dacbc8`) lines 140-143 [crates/gcore/src/ai/text.rs:140-143]
  - Signature: `fn request_body_json(request: &str) -> Value {`
  - Purpose: Indexed function `request_body_json` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:140-143]
- `has_header` (function) component `has_header [function]` (`2f8cf29c-4c28-556f-bac8-6f97f18f2929`) lines 145-152 [crates/gcore/src/ai/text.rs:145-152]
  - Signature: `fn has_header(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: Indexed function `has_header` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:145-152]
- `test_context` (function) component `test_context [function]` (`c0da1480-fcf6-59e5-9ed1-064a2011ccb8`) lines 154-171 [crates/gcore/src/ai/text.rs:154-171]
  - Signature: `fn test_context(api_base: &str, api_key: Option<&str>) -> AiContext {`
  - Purpose: Indexed function `test_context` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:154-171]
- `binding` (function) component `binding [function]` (`f138a8a7-4e65-545b-a963-ce997bf8ffde`) lines 173-186 [crates/gcore/src/ai/text.rs:173-186]
  - Signature: `fn binding(api_base: &str, api_key: Option<&str>) -> CapabilityBinding {`
  - Purpose: Indexed function `binding` in `crates/gcore/src/ai/text.rs`. [crates/gcore/src/ai/text.rs:173-186]

