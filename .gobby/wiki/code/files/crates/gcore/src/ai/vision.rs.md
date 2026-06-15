---
title: crates/gcore/src/ai/vision.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/vision.rs
  ranges:
  - 14-17
  - 19-35
  - 37-63
  - 65-90
  - 92-104
  - 106-121
  - 123-156
  - 158-173
  - 175-179
  - 190-222
  - 225-234
  - 237-246
  - 248-250
  - 252-255
  - 257-264
  - 266-283
  - 285-298
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/vision.rs

Module: [[code/modules/crates/gcore/src/ai|crates/gcore/src/ai]]

## Purpose

This file implements the vision-extraction path for AI image descriptions: `describe_image` builds a chat-completions request from image bytes and MIME type, sends it through the AI transport, and turns the response into a `VisionResult`. The helper functions assemble the JSON payload with an inline base64 data URI, then parse model output either as compact JSON or as a simple labeled text block, with fallbacks that preserve the raw description when structured parsing fails. The small `Section` enum and section-label/text-cleaning helpers support the delimited-text parser, and the tests verify request construction, header/body handling, and the different parsing edge cases.
[crates/gcore/src/ai/vision.rs:14-17]
[crates/gcore/src/ai/vision.rs:19-35]
[crates/gcore/src/ai/vision.rs:37-63]
[crates/gcore/src/ai/vision.rs:65-90]
[crates/gcore/src/ai/vision.rs:92-104]

## API Symbols

- `Section` (type) component `Section [type]` (`5a39d581-a2c4-5414-b1fe-fa055ed01e26`) lines 14-17 [crates/gcore/src/ai/vision.rs:14-17]
  - Signature: `enum Section {`
  - Purpose: Indexed type `Section` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:14-17]
- `describe_image` (function) component `describe_image [function]` (`da280306-74aa-54d8-a56a-bc9f19ff9a9d`) lines 19-35 [crates/gcore/src/ai/vision.rs:19-35]
  - Signature: `pub fn describe_image(`
  - Purpose: Creates a vision-extraction chat-completions request from the provided image bytes and MIME type, posts it via the AI transport, extracts the response content and model, and returns the parsed 'VisionResult' or an 'AiError'. [crates/gcore/src/ai/vision.rs:19-35]
- `request_body` (function) component `request_body [function]` (`8573a93a-a983-5869-8ee6-0e70c43302b7`) lines 37-63 [crates/gcore/src/ai/vision.rs:37-63]
  - Signature: `fn request_body(binding: &CapabilityBinding, bytes: Vec<u8>, mime: &str) -> Value {`
  - Purpose: Constructs a JSON request payload containing a user message with 'VISION_PROMPT' text plus an inline base64 'data:' URI image derived from the provided bytes and MIME type, and conditionally adds 'binding.model' when it is non-empty. [crates/gcore/src/ai/vision.rs:37-63]
- `parse_content` (function) component `parse_content [function]` (`7670963e-2e4b-52fa-af31-078c4f7320bb`) lines 65-90 [crates/gcore/src/ai/vision.rs:65-90]
  - Signature: `fn parse_content(content: &str, model: Option<String>) -> VisionResult {`
  - Purpose: Attempts to parse 'content' as JSON or delimited text into a 'VisionResult' with empty metadata, and if both parsers fail returns a fallback result whose 'description' is the trimmed input and whose 'ocr_text' is 'None'. [crates/gcore/src/ai/vision.rs:65-90]
- `parse_json_content` (function) component `parse_json_content [function]` (`7e24670a-7ed6-5793-a947-7b97283d512e`) lines 92-104 [crates/gcore/src/ai/vision.rs:92-104]
  - Signature: `fn parse_json_content(content: &str) -> Option<(String, Option<String>)> {`
  - Purpose: Parses a JSON-formatted vision content string (after stripping any JSON fence) into a trimmed 'description' and an optional cleaned OCR text field, returning 'None' if parsing fails or 'description' is missing. [crates/gcore/src/ai/vision.rs:92-104]
- `VisionContent` (class) component `VisionContent [class]` (`bb746a09-7b5c-584a-bd28-525ac6a598e4`) lines 94-98 [crates/gcore/src/ai/vision.rs:94-98]
  - Signature: `struct VisionContent {`
  - Purpose: 'VisionContent' is a Rust struct that represents vision-related metadata with two optional string fields: 'description' and 'ocr_text', where 'ocr_text' deserializes from 'ocr' or 'ocrText' and defaults to 'None' when absent. [crates/gcore/src/ai/vision.rs:94-98]
- `strip_json_fence` (function) component `strip_json_fence [function]` (`35c80297-49e7-5e66-9f40-a5cfd322b377`) lines 106-121 [crates/gcore/src/ai/vision.rs:106-121]
  - Signature: `fn strip_json_fence(content: &str) -> &str {`
  - Purpose: Trims the input, removes an optional leading ''''' plus optional 'json' or 'JSON' language tag and following newlines, then strips a trailing ''''' if present and returns the remaining content trimmed. [crates/gcore/src/ai/vision.rs:106-121]
- `parse_delimited_content` (function) component `parse_delimited_content [function]` (`eaf22cda-d802-5c87-8320-da8bf0a3e9bd`) lines 123-156 [crates/gcore/src/ai/vision.rs:123-156]
  - Signature: `fn parse_delimited_content(content: &str) -> Option<(String, Option<String>)> {`
  - Purpose: Parses a delimited text block into a required trimmed description and an optional cleaned OCR-text field by tracking section labels line by line, collecting subsequent lines into the active section, and returning 'None' if the description is empty. [crates/gcore/src/ai/vision.rs:123-156]
- `parse_section_label` (function) component `parse_section_label [function]` (`187d6eec-5ed7-5079-8f91-59dca52e6761`) lines 158-173 [crates/gcore/src/ai/vision.rs:158-173]
  - Signature: `fn parse_section_label(line: &str) -> Option<(Section, &str)> {`
  - Purpose: Parses a line as a section header by trimming leading whitespace, splitting once on ':', normalizing the label to lowercase snake_case after stripping surrounding spaces and leading '#', and returning 'Some((Section::Description, remainder))' for 'description', 'Some((Section::Ocr, remainder))' for 'ocr' or 'ocr_text', otherwise 'None'. [crates/gcore/src/ai/vision.rs:158-173]
- `clean_optional_text` (function) component `clean_optional_text [function]` (`98af5984-bc13-50fc-8075-266e6169d90a`) lines 175-179 [crates/gcore/src/ai/vision.rs:175-179]
  - Signature: `fn clean_optional_text(value: Option<String>) -> Option<String> {`
  - Purpose: Trims surrounding whitespace from an optional string and returns 'None' if the result is empty or case-insensitively equals '"null"', otherwise returns the cleaned 'Some(String)'. [crates/gcore/src/ai/vision.rs:175-179]
- `sends_image_url_and_parses` (function) component `sends_image_url_and_parses [function]` (`c5125678-2df4-5bbf-b65a-2e9b46a9de54`) lines 190-222 [crates/gcore/src/ai/vision.rs:190-222]
  - Signature: `fn sends_image_url_and_parses() {`
  - Purpose: Tests that 'describe_image' sends a 'data:image/png;base64' image URL to '/v1/chat/completions' with the configured bearer token and model, then correctly parses the JSON string response into 'description', 'ocr_text', and 'model', while also verifying 'parse_content'’s fallback behavior for plain text. [crates/gcore/src/ai/vision.rs:190-222]
- `parses_present_empty_json_description` (function) component `parses_present_empty_json_description [function]` (`68e90422-1644-5453-b932-7a013349ed27`) lines 225-234 [crates/gcore/src/ai/vision.rs:225-234]
  - Signature: `fn parses_present_empty_json_description() {`
  - Purpose: Verifies that 'parse_content' preserves an explicitly present empty 'description' string, maps 'ocr_text: null' to 'None', and records the provided model name in the parsed result. [crates/gcore/src/ai/vision.rs:225-234]
- `parses_unterminated_json_fence` (function) component `parses_unterminated_json_fence [function]` (`add5d0e2-954d-5f0c-a54c-25917626e112`) lines 237-246 [crates/gcore/src/ai/vision.rs:237-246]
  - Signature: `fn parses_unterminated_json_fence() {`
  - Purpose: Verifies that 'parse_content' correctly parses JSON wrapped in an unterminated ''''json' fence, extracting 'description' and 'ocr_text' fields and preserving the provided model name. [crates/gcore/src/ai/vision.rs:237-246]
- `spawn_server` (function) component `spawn_server [function]` (`3ad0205a-e7d7-51da-9e36-c4c467003126`) lines 248-250 [crates/gcore/src/ai/vision.rs:248-250]
  - Signature: `fn spawn_server(response: &'static str) -> (String, RequestHandle) {`
  - Purpose: Calls 'spawn_json_response(response)' to start a test server that serves the provided static response string, then unwraps the result with 'expect("spawn test server")' and returns the server address plus 'RequestHandle'. [crates/gcore/src/ai/vision.rs:248-250]
- `request_body_json` (function) component `request_body_json [function]` (`ca792c6f-b010-5711-9d72-fe94dda683f5`) lines 252-255 [crates/gcore/src/ai/vision.rs:252-255]
  - Signature: `fn request_body_json(request: &str) -> Value {`
  - Purpose: Extracts the substring after the first HTTP header/body separator ('\r\n\r\n') from the request string and parses it as JSON into a 'Value', panicking on missing body or invalid JSON. [crates/gcore/src/ai/vision.rs:252-255]
- `has_header` (function) component `has_header [function]` (`98467993-79b7-59ed-aef8-bd1899fc8bad`) lines 257-264 [crates/gcore/src/ai/vision.rs:257-264]
  - Signature: `fn has_header(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: Returns 'true' if any line in 'request' parses as a 'name: value' header whose field name matches 'name' case-insensitively and whose trimmed value is exactly 'value', otherwise 'false'. [crates/gcore/src/ai/vision.rs:257-264]
- `test_context` (function) component `test_context [function]` (`567bf261-a3d2-5e8d-a35b-38c1f624a7a8`) lines 266-283 [crates/gcore/src/ai/vision.rs:266-283]
  - Signature: `fn test_context(api_base: &str, api_key: Option<&str>) -> AiContext {`
  - Purpose: Constructs an 'AiContext' for testing by creating a shared binding from 'api_base' and optional 'api_key', assigning it to all AI capability bindings, and configuring single-concurrency tuning with a new limiter, no keep-alive, and no project ID. [crates/gcore/src/ai/vision.rs:266-283]
- `binding` (function) component `binding [function]` (`fcf5de2c-4dc1-5a01-871a-1991d0fd599b`) lines 285-298 [crates/gcore/src/ai/vision.rs:285-298]
  - Signature: `fn binding(api_base: &str, api_key: Option<&str>) -> CapabilityBinding {`
  - Purpose: Constructs and returns a 'CapabilityBinding' configured for direct AI routing with no transport, the provided 'api_base' and optional 'api_key', a fixed 'gpt-4.1-mini' model, and all other fields unset. [crates/gcore/src/ai/vision.rs:285-298]

