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

This file implements AI vision extraction for images: `describe_image` sends an image to the configured vision-capable chat-completions endpoint, and the rest of the module builds the request and normalizes the response into a `VisionResult`. `request_body` base64-encodes the image into a data URI, inserts the vision prompt, and optionally sets the bound model. `parse_content` is the main response handler, first trying structured JSON, then a delimited text fallback, and finally a plain-text fallback, using helpers like `parse_json_content`, `strip_json_fence`, `parse_delimited_content`, `parse_section_label`, and `clean_optional_text` to extract `description` and `ocr_text`. The test helpers and cases at the end verify request construction and parsing edge cases such as empty JSON descriptions and unterminated JSON fences.
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
  - Purpose: Indexed function `describe_image` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:19-35]
- `request_body` (function) component `request_body [function]` (`8573a93a-a983-5869-8ee6-0e70c43302b7`) lines 37-63 [crates/gcore/src/ai/vision.rs:37-63]
  - Signature: `fn request_body(binding: &CapabilityBinding, bytes: Vec<u8>, mime: &str) -> Value {`
  - Purpose: Indexed function `request_body` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:37-63]
- `parse_content` (function) component `parse_content [function]` (`7670963e-2e4b-52fa-af31-078c4f7320bb`) lines 65-90 [crates/gcore/src/ai/vision.rs:65-90]
  - Signature: `fn parse_content(content: &str, model: Option<String>) -> VisionResult {`
  - Purpose: Indexed function `parse_content` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:65-90]
- `parse_json_content` (function) component `parse_json_content [function]` (`7e24670a-7ed6-5793-a947-7b97283d512e`) lines 92-104 [crates/gcore/src/ai/vision.rs:92-104]
  - Signature: `fn parse_json_content(content: &str) -> Option<(String, Option<String>)> {`
  - Purpose: Indexed function `parse_json_content` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:92-104]
- `VisionContent` (class) component `VisionContent [class]` (`bb746a09-7b5c-584a-bd28-525ac6a598e4`) lines 94-98 [crates/gcore/src/ai/vision.rs:94-98]
  - Signature: `struct VisionContent {`
  - Purpose: Indexed class `VisionContent` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:94-98]
- `strip_json_fence` (function) component `strip_json_fence [function]` (`35c80297-49e7-5e66-9f40-a5cfd322b377`) lines 106-121 [crates/gcore/src/ai/vision.rs:106-121]
  - Signature: `fn strip_json_fence(content: &str) -> &str {`
  - Purpose: Indexed function `strip_json_fence` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:106-121]
- `parse_delimited_content` (function) component `parse_delimited_content [function]` (`eaf22cda-d802-5c87-8320-da8bf0a3e9bd`) lines 123-156 [crates/gcore/src/ai/vision.rs:123-156]
  - Signature: `fn parse_delimited_content(content: &str) -> Option<(String, Option<String>)> {`
  - Purpose: Indexed function `parse_delimited_content` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:123-156]
- `parse_section_label` (function) component `parse_section_label [function]` (`187d6eec-5ed7-5079-8f91-59dca52e6761`) lines 158-173 [crates/gcore/src/ai/vision.rs:158-173]
  - Signature: `fn parse_section_label(line: &str) -> Option<(Section, &str)> {`
  - Purpose: Indexed function `parse_section_label` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:158-173]
- `clean_optional_text` (function) component `clean_optional_text [function]` (`98af5984-bc13-50fc-8075-266e6169d90a`) lines 175-179 [crates/gcore/src/ai/vision.rs:175-179]
  - Signature: `fn clean_optional_text(value: Option<String>) -> Option<String> {`
  - Purpose: Indexed function `clean_optional_text` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:175-179]
- `sends_image_url_and_parses` (function) component `sends_image_url_and_parses [function]` (`c5125678-2df4-5bbf-b65a-2e9b46a9de54`) lines 190-222 [crates/gcore/src/ai/vision.rs:190-222]
  - Signature: `fn sends_image_url_and_parses() {`
  - Purpose: Indexed function `sends_image_url_and_parses` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:190-222]
- `parses_present_empty_json_description` (function) component `parses_present_empty_json_description [function]` (`68e90422-1644-5453-b932-7a013349ed27`) lines 225-234 [crates/gcore/src/ai/vision.rs:225-234]
  - Signature: `fn parses_present_empty_json_description() {`
  - Purpose: Indexed function `parses_present_empty_json_description` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:225-234]
- `parses_unterminated_json_fence` (function) component `parses_unterminated_json_fence [function]` (`add5d0e2-954d-5f0c-a54c-25917626e112`) lines 237-246 [crates/gcore/src/ai/vision.rs:237-246]
  - Signature: `fn parses_unterminated_json_fence() {`
  - Purpose: Indexed function `parses_unterminated_json_fence` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:237-246]
- `spawn_server` (function) component `spawn_server [function]` (`3ad0205a-e7d7-51da-9e36-c4c467003126`) lines 248-250 [crates/gcore/src/ai/vision.rs:248-250]
  - Signature: `fn spawn_server(response: &'static str) -> (String, RequestHandle) {`
  - Purpose: Indexed function `spawn_server` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:248-250]
- `request_body_json` (function) component `request_body_json [function]` (`ca792c6f-b010-5711-9d72-fe94dda683f5`) lines 252-255 [crates/gcore/src/ai/vision.rs:252-255]
  - Signature: `fn request_body_json(request: &str) -> Value {`
  - Purpose: Indexed function `request_body_json` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:252-255]
- `has_header` (function) component `has_header [function]` (`98467993-79b7-59ed-aef8-bd1899fc8bad`) lines 257-264 [crates/gcore/src/ai/vision.rs:257-264]
  - Signature: `fn has_header(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: Indexed function `has_header` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:257-264]
- `test_context` (function) component `test_context [function]` (`567bf261-a3d2-5e8d-a35b-38c1f624a7a8`) lines 266-283 [crates/gcore/src/ai/vision.rs:266-283]
  - Signature: `fn test_context(api_base: &str, api_key: Option<&str>) -> AiContext {`
  - Purpose: Indexed function `test_context` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:266-283]
- `binding` (function) component `binding [function]` (`fcf5de2c-4dc1-5a01-871a-1991d0fd599b`) lines 285-298 [crates/gcore/src/ai/vision.rs:285-298]
  - Signature: `fn binding(api_base: &str, api_key: Option<&str>) -> CapabilityBinding {`
  - Purpose: Indexed function `binding` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:285-298]

