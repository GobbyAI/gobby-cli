---
title: crates/gcore/src/ai/daemon/request.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/daemon/request.rs
  ranges:
  - 11-19
  - 21-41
  - 43-52
  - 54-79
  - 81-98
  - 100-104
  - 106-108
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/daemon/request.rs

Module: [[code/modules/crates/gcore/src/ai/daemon|crates/gcore/src/ai/daemon]]

## Purpose

This file provides request-building helpers for the AI daemon. It validates that only audio transcription and translation capabilities are accepted for voice work, wraps raw bytes into a single-file multipart upload with MIME and size checks, and conditionally adds non-empty text fields to multipart forms. It also assembles JSON bodies for text generation and embeddings requests, normalizing optional inputs, trimming empties, and applying a default generation profile only when provider and model are both absent.
[crates/gcore/src/ai/daemon/request.rs:11-19]
[crates/gcore/src/ai/daemon/request.rs:21-41]
[crates/gcore/src/ai/daemon/request.rs:43-52]
[crates/gcore/src/ai/daemon/request.rs:54-79]
[crates/gcore/src/ai/daemon/request.rs:81-98]

## API Symbols

- `audio_capability` (function) component `audio_capability [function]` (`2552589b-3ac5-5914-aa53-f5bed9b6574b`) lines 11-19 [crates/gcore/src/ai/daemon/request.rs:11-19]
  - Signature: `pub(super) fn audio_capability(capability: AiCapability) -> Result<AiCapability, AiError> {`
  - Purpose: Returns the input capability unchanged only if it is 'AiCapability::AudioTranscribe' or 'AiCapability::AudioTranslate', otherwise returns an 'AiError' indicating the capability is unavailable for daemon voice transcription. [crates/gcore/src/ai/daemon/request.rs:11-19]
- `multipart_form_with_file` (function) component `multipart_form_with_file [function]` (`74be47d1-89fd-5916-b38c-000ddc18bcd7`) lines 21-41 [crates/gcore/src/ai/daemon/request.rs:21-41]
  - Signature: `pub(super) fn multipart_form_with_file(`
  - Purpose: Builds a 'multipart::Form' containing a single '"file"' part from the provided 'Bytes', validating the payload length and MIME type and converting any failures into 'AiError::parse_failure'. [crates/gcore/src/ai/daemon/request.rs:21-41]
- `add_optional_text` (function) component `add_optional_text [function]` (`818e2b7b-c3ac-52fe-94c0-0a274f64f495`) lines 43-52 [crates/gcore/src/ai/daemon/request.rs:43-52]
  - Signature: `pub(super) fn add_optional_text(`
  - Purpose: Adds a multipart text field named 'name' with the provided non-empty 'value' converted to 'String', or returns the original 'Form' unchanged when 'value' is 'None' or empty. [crates/gcore/src/ai/daemon/request.rs:43-52]
- `text_request_body` (function) component `text_request_body [function]` (`13411b3b-9058-531e-ad27-b27d9e85e922`) lines 54-79 [crates/gcore/src/ai/daemon/request.rs:54-79]
  - Signature: `pub(super) fn text_request_body(`
  - Purpose: Constructs and returns a JSON request body for text generation with required 'prompt', optional 'system_prompt'/'provider'/'model'/'project_id', a default 'profile' only when both 'provider' and 'model' are absent, and a positive 'max_tokens' field when provided. [crates/gcore/src/ai/daemon/request.rs:54-79]
- `embeddings_request_body` (function) component `embeddings_request_body [function]` (`fb05eb92-1d9f-5ad6-9d35-33dfd0d3ddc8`) lines 81-98 [crates/gcore/src/ai/daemon/request.rs:81-98]
  - Signature: `pub(super) fn embeddings_request_body(`
  - Purpose: Builds a JSON object for an embeddings request containing the string array 'input', the 'is_query' flag, and optional 'project_id', 'provider', and 'model' fields. [crates/gcore/src/ai/daemon/request.rs:81-98]
- `insert_optional` (function) component `insert_optional [function]` (`43a2555f-0663-593c-a564-0a04e7a891c6`) lines 100-104 [crates/gcore/src/ai/daemon/request.rs:100-104]
  - Signature: `fn insert_optional(body: &mut Map<String, Value>, name: &str, value: Option<&str>) {`
  - Purpose: Inserts 'name' into 'body' as a 'Value::String' only when 'value' is 'Some' and non-empty, otherwise leaves 'body' unchanged. [crates/gcore/src/ai/daemon/request.rs:100-104]
- `non_empty` (function) component `non_empty [function]` (`ebe764cc-8b41-5a31-a4dc-62b4bfaf59ec`) lines 106-108 [crates/gcore/src/ai/daemon/request.rs:106-108]
  - Signature: `fn non_empty(value: Option<&str>) -> Option<&str> {`
  - Purpose: Returns the input 'Option<&str>' trimmed of leading and trailing whitespace, yielding 'None' if the option is 'None' or if the trimmed string is empty. [crates/gcore/src/ai/daemon/request.rs:106-108]

