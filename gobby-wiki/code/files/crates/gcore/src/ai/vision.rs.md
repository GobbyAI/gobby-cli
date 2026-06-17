---
title: crates/gcore/src/ai/vision.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/vision.rs
  ranges:
  - 15-18
  - 20-36
  - 38-65
  - 67-92
  - 94-106
  - 108-123
  - 125-158
  - 160-175
  - 177-181
  - 192-226
  - 229-238
  - 241-250
  - 252-254
  - 256-259
  - 261-268
  - 270-287
  - 289-302
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/ai/vision.rs:15-18](crates/gcore/src/ai/vision.rs#L15-L18), [crates/gcore/src/ai/vision.rs:20-36](crates/gcore/src/ai/vision.rs#L20-L36), [crates/gcore/src/ai/vision.rs:38-65](crates/gcore/src/ai/vision.rs#L38-L65), [crates/gcore/src/ai/vision.rs:67-92](crates/gcore/src/ai/vision.rs#L67-L92), [crates/gcore/src/ai/vision.rs:94-106](crates/gcore/src/ai/vision.rs#L94-L106), [crates/gcore/src/ai/vision.rs:108-123](crates/gcore/src/ai/vision.rs#L108-L123), [crates/gcore/src/ai/vision.rs:125-158](crates/gcore/src/ai/vision.rs#L125-L158), [crates/gcore/src/ai/vision.rs:160-175](crates/gcore/src/ai/vision.rs#L160-L175), [crates/gcore/src/ai/vision.rs:177-181](crates/gcore/src/ai/vision.rs#L177-L181), [crates/gcore/src/ai/vision.rs:192-226](crates/gcore/src/ai/vision.rs#L192-L226), [crates/gcore/src/ai/vision.rs:229-238](crates/gcore/src/ai/vision.rs#L229-L238), [crates/gcore/src/ai/vision.rs:241-250](crates/gcore/src/ai/vision.rs#L241-L250), [crates/gcore/src/ai/vision.rs:252-254](crates/gcore/src/ai/vision.rs#L252-L254), [crates/gcore/src/ai/vision.rs:256-259](crates/gcore/src/ai/vision.rs#L256-L259), [crates/gcore/src/ai/vision.rs:261-268](crates/gcore/src/ai/vision.rs#L261-L268), [crates/gcore/src/ai/vision.rs:270-287](crates/gcore/src/ai/vision.rs#L270-L287), [crates/gcore/src/ai/vision.rs:289-302](crates/gcore/src/ai/vision.rs#L289-L302)

</details>

# crates/gcore/src/ai/vision.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Builds and exercises the vision-extraction path for AI image descriptions: `describe_image` sends an image to the configured vision capability, `request_body` packages the prompt plus base64 image data into a chat-completions request, and `parse_content` turns the model reply into a `VisionResult`. The parsing helpers accept either compact JSON or a delimited fallback format, normalize section labels and optional text, and `strip_json_fence`/`parse_json_content` handle fenced or unterminated JSON responses. The tests cover sending the image URL and parsing the expected response variations and edge cases.
[crates/gcore/src/ai/vision.rs:15-18]
[crates/gcore/src/ai/vision.rs:20-36]
[crates/gcore/src/ai/vision.rs:38-65]
[crates/gcore/src/ai/vision.rs:67-92]
[crates/gcore/src/ai/vision.rs:94-106]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Section` | type | `enum Section {` | `Section [type]` | `6c0e4673-aa3c-5dbc-892e-9df13cabb90c` | 15-18 [crates/gcore/src/ai/vision.rs:15-18] | Indexed type `Section` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:15-18] |
| `describe_image` | function | `pub fn describe_image(` | `describe_image [function]` | `51540fee-1bc2-5d73-81f6-48d30fc68b8e` | 20-36 [crates/gcore/src/ai/vision.rs:20-36] | Indexed function `describe_image` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:20-36] |
| `request_body` | function | `fn request_body(binding: &CapabilityBinding, bytes: Vec<u8>, mime: &str) -> Value {` | `request_body [function]` | `7cf56b74-e4a3-5584-8fd6-8848b1117ad7` | 38-65 [crates/gcore/src/ai/vision.rs:38-65] | Indexed function `request_body` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:38-65] |
| `parse_content` | function | `fn parse_content(content: &str, model: Option<String>) -> VisionResult {` | `parse_content [function]` | `4bb68168-c352-5956-9e56-33471b9df276` | 67-92 [crates/gcore/src/ai/vision.rs:67-92] | Indexed function `parse_content` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:67-92] |
| `parse_json_content` | function | `fn parse_json_content(content: &str) -> Option<(String, Option<String>)> {` | `parse_json_content [function]` | `98a8097b-d775-5fac-a520-11fcb3f8e537` | 94-106 [crates/gcore/src/ai/vision.rs:94-106] | Indexed function `parse_json_content` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:94-106] |
| `VisionContent` | class | `struct VisionContent {` | `VisionContent [class]` | `9c98e37f-10f2-5445-b1ad-0c01e6622037` | 96-100 [crates/gcore/src/ai/vision.rs:96-100] | Indexed class `VisionContent` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:96-100] |
| `strip_json_fence` | function | `fn strip_json_fence(content: &str) -> &str {` | `strip_json_fence [function]` | `01a3babd-c811-556b-b5ed-91c61fbf1c9f` | 108-123 [crates/gcore/src/ai/vision.rs:108-123] | Indexed function `strip_json_fence` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:108-123] |
| `parse_delimited_content` | function | `fn parse_delimited_content(content: &str) -> Option<(String, Option<String>)> {` | `parse_delimited_content [function]` | `495bfcf5-7b22-502e-a39f-fe468c7ff6f1` | 125-158 [crates/gcore/src/ai/vision.rs:125-158] | Indexed function `parse_delimited_content` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:125-158] |
| `parse_section_label` | function | `fn parse_section_label(line: &str) -> Option<(Section, &str)> {` | `parse_section_label [function]` | `e46cc011-20f7-5a16-a1cc-6d7a789fb796` | 160-175 [crates/gcore/src/ai/vision.rs:160-175] | Indexed function `parse_section_label` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:160-175] |
| `clean_optional_text` | function | `fn clean_optional_text(value: Option<String>) -> Option<String> {` | `clean_optional_text [function]` | `50c8e26a-457b-576b-ad43-af315a4435dd` | 177-181 [crates/gcore/src/ai/vision.rs:177-181] | Indexed function `clean_optional_text` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:177-181] |
| `sends_image_url_and_parses` | function | `fn sends_image_url_and_parses() {` | `sends_image_url_and_parses [function]` | `9ed8c125-7f03-5f24-8438-758d8a25cff2` | 192-226 [crates/gcore/src/ai/vision.rs:192-226] | Indexed function `sends_image_url_and_parses` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:192-226] |
| `parses_present_empty_json_description` | function | `fn parses_present_empty_json_description() {` | `parses_present_empty_json_description [function]` | `d750e1cf-12cb-59ec-8d42-bc175d87ed91` | 229-238 [crates/gcore/src/ai/vision.rs:229-238] | Indexed function `parses_present_empty_json_description` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:229-238] |
| `parses_unterminated_json_fence` | function | `fn parses_unterminated_json_fence() {` | `parses_unterminated_json_fence [function]` | `dd9d0da2-869f-5366-98a3-c870e10fc6fb` | 241-250 [crates/gcore/src/ai/vision.rs:241-250] | Indexed function `parses_unterminated_json_fence` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:241-250] |
| `spawn_server` | function | `fn spawn_server(response: &'static str) -> (String, RequestHandle) {` | `spawn_server [function]` | `09d9ab42-5c47-57ee-aff4-0e77c2ae631f` | 252-254 [crates/gcore/src/ai/vision.rs:252-254] | Indexed function `spawn_server` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:252-254] |
| `request_body_json` | function | `fn request_body_json(request: &str) -> Value {` | `request_body_json [function]` | `b056efc2-aa04-59b0-8820-273b37676fd6` | 256-259 [crates/gcore/src/ai/vision.rs:256-259] | Indexed function `request_body_json` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:256-259] |
| `has_header` | function | `fn has_header(request: &str, name: &str, value: &str) -> bool {` | `has_header [function]` | `c273aad5-c98d-5b46-b21d-374b330fbb6f` | 261-268 [crates/gcore/src/ai/vision.rs:261-268] | Indexed function `has_header` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:261-268] |
| `test_context` | function | `fn test_context(api_base: &str, api_key: Option<&str>) -> AiContext {` | `test_context [function]` | `942a8b59-ae39-556e-9615-e94d039b35f8` | 270-287 [crates/gcore/src/ai/vision.rs:270-287] | Indexed function `test_context` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:270-287] |
| `binding` | function | `fn binding(api_base: &str, api_key: Option<&str>) -> CapabilityBinding {` | `binding [function]` | `6346ebd5-6eef-5b53-97b8-f326c554e034` | 289-302 [crates/gcore/src/ai/vision.rs:289-302] | Indexed function `binding` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:289-302] |
