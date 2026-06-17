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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/ai/daemon/request.rs:11-19](crates/gcore/src/ai/daemon/request.rs#L11-L19), [crates/gcore/src/ai/daemon/request.rs:21-41](crates/gcore/src/ai/daemon/request.rs#L21-L41), [crates/gcore/src/ai/daemon/request.rs:43-52](crates/gcore/src/ai/daemon/request.rs#L43-L52), [crates/gcore/src/ai/daemon/request.rs:54-79](crates/gcore/src/ai/daemon/request.rs#L54-L79), [crates/gcore/src/ai/daemon/request.rs:81-98](crates/gcore/src/ai/daemon/request.rs#L81-L98), [crates/gcore/src/ai/daemon/request.rs:100-104](crates/gcore/src/ai/daemon/request.rs#L100-L104), [crates/gcore/src/ai/daemon/request.rs:106-108](crates/gcore/src/ai/daemon/request.rs#L106-L108)

</details>

# crates/gcore/src/ai/daemon/request.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Builds request payloads and validation helpers for the AI daemon. It constrains audio calls to supported transcription/translation capabilities, wraps file bytes into multipart form parts with MIME and size checks, and adds optional text fields only when they are non-empty. It also assembles JSON bodies for text generation and embeddings requests, using small helpers to insert optional values and normalize empty strings, with a default text-generation profile when neither provider nor model is supplied.
[crates/gcore/src/ai/daemon/request.rs:11-19]
[crates/gcore/src/ai/daemon/request.rs:21-41]
[crates/gcore/src/ai/daemon/request.rs:43-52]
[crates/gcore/src/ai/daemon/request.rs:54-79]
[crates/gcore/src/ai/daemon/request.rs:81-98]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `audio_capability` | function | `pub(super) fn audio_capability(capability: AiCapability) -> Result<AiCapability, AiError> {` | `audio_capability [function]` | `2552589b-3ac5-5914-aa53-f5bed9b6574b` | 11-19 [crates/gcore/src/ai/daemon/request.rs:11-19] | Indexed function `audio_capability` in `crates/gcore/src/ai/daemon/request.rs`. [crates/gcore/src/ai/daemon/request.rs:11-19] |
| `multipart_form_with_file` | function | `pub(super) fn multipart_form_with_file(` | `multipart_form_with_file [function]` | `74be47d1-89fd-5916-b38c-000ddc18bcd7` | 21-41 [crates/gcore/src/ai/daemon/request.rs:21-41] | Indexed function `multipart_form_with_file` in `crates/gcore/src/ai/daemon/request.rs`. [crates/gcore/src/ai/daemon/request.rs:21-41] |
| `add_optional_text` | function | `pub(super) fn add_optional_text(` | `add_optional_text [function]` | `818e2b7b-c3ac-52fe-94c0-0a274f64f495` | 43-52 [crates/gcore/src/ai/daemon/request.rs:43-52] | Indexed function `add_optional_text` in `crates/gcore/src/ai/daemon/request.rs`. [crates/gcore/src/ai/daemon/request.rs:43-52] |
| `text_request_body` | function | `pub(super) fn text_request_body(` | `text_request_body [function]` | `13411b3b-9058-531e-ad27-b27d9e85e922` | 54-79 [crates/gcore/src/ai/daemon/request.rs:54-79] | Indexed function `text_request_body` in `crates/gcore/src/ai/daemon/request.rs`. [crates/gcore/src/ai/daemon/request.rs:54-79] |
| `embeddings_request_body` | function | `pub(super) fn embeddings_request_body(` | `embeddings_request_body [function]` | `fb05eb92-1d9f-5ad6-9d35-33dfd0d3ddc8` | 81-98 [crates/gcore/src/ai/daemon/request.rs:81-98] | Indexed function `embeddings_request_body` in `crates/gcore/src/ai/daemon/request.rs`. [crates/gcore/src/ai/daemon/request.rs:81-98] |
| `insert_optional` | function | `fn insert_optional(body: &mut Map<String, Value>, name: &str, value: Option<&str>) {` | `insert_optional [function]` | `43a2555f-0663-593c-a564-0a04e7a891c6` | 100-104 [crates/gcore/src/ai/daemon/request.rs:100-104] | Indexed function `insert_optional` in `crates/gcore/src/ai/daemon/request.rs`. [crates/gcore/src/ai/daemon/request.rs:100-104] |
| `non_empty` | function | `fn non_empty(value: Option<&str>) -> Option<&str> {` | `non_empty [function]` | `ebe764cc-8b41-5a31-a4dc-62b4bfaf59ec` | 106-108 [crates/gcore/src/ai/daemon/request.rs:106-108] | Indexed function `non_empty` in `crates/gcore/src/ai/daemon/request.rs`. [crates/gcore/src/ai/daemon/request.rs:106-108] |
