---
title: crates/gcore/src/ai/vision.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/vision.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/vision.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/ai/vision.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gcore/src/ai/vision.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Section` | type | Indexed type `Section` in `crates/gcore/src/ai/vision.rs`. [crates/gcore/src/ai/vision.rs:15-18] |
| `describe_image` | function | Sends the provided image bytes and MIME type to the vision-extraction chat-completions endpoint via the configured transport, extracts the response content, and parses it into a 'VisionResult', returning any transport or parsing error as 'AiError'. [crates/gcore/src/ai/vision.rs:20-36] |
| `request_body` | function | Builds a vision-model request JSON body by base64-encoding the input bytes into a 'data:' URI, embedding it alongside a fixed prompt and 'VISION_MAX_TOKENS' in a user message, and conditionally adding 'binding.model' when present and non-empty. [crates/gcore/src/ai/vision.rs:38-65] |
| `parse_content` | function | 'parse_content' attempts to parse the input as structured JSON content, then as delimited content, and otherwise returns a 'VisionResult' with the trimmed raw content as 'description', 'ocr_text' set to 'None', the provided 'model', and an empty 'metadata' map. [crates/gcore/src/ai/vision.rs:67-92] |
| `parse_json_content` | function | Parses a JSON-formatted vision content payload from 'content' after stripping fences, requiring a non-empty 'description' field and returning it trimmed together with an optionally cleaned 'ocr_text' field (accepted under 'ocr' or 'ocrText' aliases), or 'None' on parse/validation failure. [crates/gcore/src/ai/vision.rs:94-106] |
| `VisionContent` | class | 'VisionContent' is a Serde-serializable struct that optionally stores an image 'description' and optional OCR text in 'ocr_text', deserialized from 'ocr' or 'ocrText' aliases by default. [crates/gcore/src/ai/vision.rs:96-100] |
| `strip_json_fence` | function | Trims the input, removes an optional opening ''''' fence plus an optional 'json'/'JSON' language tag and leading newlines, then strips a trailing ''''' fence if present and returns the remaining content trimmed. [crates/gcore/src/ai/vision.rs:108-123] |
| `parse_delimited_content` | function | Parses a line-delimited block into labeled 'Description' and 'Ocr' sections, accumulates their text, returns 'None' if the description is empty, and otherwise returns the trimmed description plus a cleaned optional OCR string. [crates/gcore/src/ai/vision.rs:125-158] |
| `parse_section_label` | function | Parses a line as a section header by trimming leading whitespace, splitting once on ':', normalizing the label to lowercase snake_case after stripping '#' and surrounding spaces, and returning 'Some((Section::Description, remainder))' for 'description', 'Some((Section::Ocr, remainder))' for 'ocr' or 'ocr_text', otherwise 'None'. [crates/gcore/src/ai/vision.rs:160-175] |
| `clean_optional_text` | function | Trims whitespace from the inner string, then returns 'None' if the result is empty or case-insensitively equal to '"null"', otherwise returns the cleaned 'Some(String)'. [crates/gcore/src/ai/vision.rs:177-181] |
| `spawn_server` | function | Spawns a test server that returns the provided static string as a JSON response, panicking if server startup fails, and returns the server URL plus a 'RequestHandle'. [crates/gcore/src/ai/vision.rs:252-254] |
| `request_body_json` | function | Extracts the HTTP message body by splitting the request string on the first '\r\n\r\n' separator and parses that body as JSON into a 'Value', panicking on missing body or invalid JSON. [crates/gcore/src/ai/vision.rs:256-259] |
| `has_header` | function | Returns 'true' if any line in 'request' parses as a 'name: value' header whose field name matches 'name' case-insensitively and whose trimmed value is exactly equal to 'value'. [crates/gcore/src/ai/vision.rs:261-268] |
| `test_context` | function | Constructs an 'AiContext' for testing by creating a shared binding from 'api_base' and optional 'api_key', cloning it across all capability bindings, setting single-threaded tuning and a limiter of 1, and leaving 'project_id' unset. [crates/gcore/src/ai/vision.rs:270-287] |
| `binding` | function | The 'binding' function constructs and returns a 'CapabilityBinding' struct configured with direct AI routing, a default model of "gpt-4.1-mini", and the provided 'api_base' and optional 'api_key' parameters converted into owned strings. [crates/gcore/src/ai/vision.rs:289-307] |

_Verified by 3 in-file unit tests._

