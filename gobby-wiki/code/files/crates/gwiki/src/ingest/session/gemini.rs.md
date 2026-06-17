---
title: crates/gwiki/src/ingest/session/gemini.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/gemini.rs
  ranges:
  - '12'
  - 15-20
  - 22-83
  - 87-102
  - 104-119
  - 121-147
  - 149-175
  - 177-192
  - 194-198
  - 200-221
  - 223-227
  - 229-234
  - 236-241
  - 251-333
  - 336-356
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/session/gemini.rs:12](crates/gwiki/src/ingest/session/gemini.rs#L12), [crates/gwiki/src/ingest/session/gemini.rs:15-20](crates/gwiki/src/ingest/session/gemini.rs#L15-L20), [crates/gwiki/src/ingest/session/gemini.rs:22-83](crates/gwiki/src/ingest/session/gemini.rs#L22-L83), [crates/gwiki/src/ingest/session/gemini.rs:87-102](crates/gwiki/src/ingest/session/gemini.rs#L87-L102), [crates/gwiki/src/ingest/session/gemini.rs:104-119](crates/gwiki/src/ingest/session/gemini.rs#L104-L119), [crates/gwiki/src/ingest/session/gemini.rs:121-147](crates/gwiki/src/ingest/session/gemini.rs#L121-L147), [crates/gwiki/src/ingest/session/gemini.rs:149-175](crates/gwiki/src/ingest/session/gemini.rs#L149-L175), [crates/gwiki/src/ingest/session/gemini.rs:177-192](crates/gwiki/src/ingest/session/gemini.rs#L177-L192), [crates/gwiki/src/ingest/session/gemini.rs:194-198](crates/gwiki/src/ingest/session/gemini.rs#L194-L198), [crates/gwiki/src/ingest/session/gemini.rs:200-221](crates/gwiki/src/ingest/session/gemini.rs#L200-L221), [crates/gwiki/src/ingest/session/gemini.rs:223-227](crates/gwiki/src/ingest/session/gemini.rs#L223-L227), [crates/gwiki/src/ingest/session/gemini.rs:229-234](crates/gwiki/src/ingest/session/gemini.rs#L229-L234), [crates/gwiki/src/ingest/session/gemini.rs:236-241](crates/gwiki/src/ingest/session/gemini.rs#L236-L241), [crates/gwiki/src/ingest/session/gemini.rs:251-333](crates/gwiki/src/ingest/session/gemini.rs#L251-L333), [crates/gwiki/src/ingest/session/gemini.rs:336-356](crates/gwiki/src/ingest/session/gemini.rs#L336-L356)

</details>

# crates/gwiki/src/ingest/session/gemini.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines a `SessionTranscriptAdapter` for Gemini session archives that recognizes Gemini envelope types, parses each `SessionArchiveEnvelope` into `GeminiRecord`s, and builds a `ParsedSession` by tracking start time, model metadata, and message sequence. The helper functions split the parsing/rendering work across message, tool call, and tool result cases, handle content assembly and call IDs, and support delta appends for streamed content. The file also includes tests for parsing streamed JSON messages/tools and for a real-stream fixture path.
[crates/gwiki/src/ingest/session/gemini.rs:12]
[crates/gwiki/src/ingest/session/gemini.rs:15-20]
[crates/gwiki/src/ingest/session/gemini.rs:22-83]
[crates/gwiki/src/ingest/session/gemini.rs:87-102]
[crates/gwiki/src/ingest/session/gemini.rs:104-119]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `GeminiSessionAdapter` | class | `pub(super) struct GeminiSessionAdapter;` | `GeminiSessionAdapter [class]` | `60e3e444-06e9-5846-9fab-87c8cd3be1f4` | 12-12 [crates/gwiki/src/ingest/session/gemini.rs:12] | Indexed class `GeminiSessionAdapter` in `crates/gwiki/src/ingest/session/gemini.rs`. [crates/gwiki/src/ingest/session/gemini.rs:12] |
| `GeminiSessionAdapter::supports` | method | `fn supports(&self, envelope_type: &str) -> bool {` | `GeminiSessionAdapter::supports [method]` | `cfc52f54-c2b2-5f2d-9fea-a65d70d5a017` | 15-20 [crates/gwiki/src/ingest/session/gemini.rs:15-20] | Indexed method `GeminiSessionAdapter::supports` in `crates/gwiki/src/ingest/session/gemini.rs`. [crates/gwiki/src/ingest/session/gemini.rs:15-20] |
| `GeminiSessionAdapter::parse` | method | `fn parse(&self, envelopes: &[SessionArchiveEnvelope]) -> Result<ParsedSession, WikiError> {` | `GeminiSessionAdapter::parse [method]` | `d0474e50-1632-5ea5-be4e-ff6f2139415c` | 22-83 [crates/gwiki/src/ingest/session/gemini.rs:22-83] | Indexed method `GeminiSessionAdapter::parse` in `crates/gwiki/src/ingest/session/gemini.rs`. [crates/gwiki/src/ingest/session/gemini.rs:22-83] |
| `GeminiRecord` | class | `struct GeminiRecord {` | `GeminiRecord [class]` | `9fb32d49-8ab2-57a8-b047-80e238f0f643` | 87-102 [crates/gwiki/src/ingest/session/gemini.rs:87-102] | Indexed class `GeminiRecord` in `crates/gwiki/src/ingest/session/gemini.rs`. [crates/gwiki/src/ingest/session/gemini.rs:87-102] |
| `parsed_gemini_message` | function | `fn parsed_gemini_message(` | `parsed_gemini_message [function]` | `95493f75-b853-5753-bc28-c4230a65c4c6` | 104-119 [crates/gwiki/src/ingest/session/gemini.rs:104-119] | Indexed function `parsed_gemini_message` in `crates/gwiki/src/ingest/session/gemini.rs`. [crates/gwiki/src/ingest/session/gemini.rs:104-119] |
| `parsed_gemini_tool_call` | function | `fn parsed_gemini_tool_call(` | `parsed_gemini_tool_call [function]` | `0bb9488c-ff2b-5972-bf65-4756955170c4` | 121-147 [crates/gwiki/src/ingest/session/gemini.rs:121-147] | Indexed function `parsed_gemini_tool_call` in `crates/gwiki/src/ingest/session/gemini.rs`. [crates/gwiki/src/ingest/session/gemini.rs:121-147] |
| `parsed_gemini_tool_result` | function | `fn parsed_gemini_tool_result(` | `parsed_gemini_tool_result [function]` | `18530d67-6c0b-5c34-b897-01c9dd8dd55a` | 149-175 [crates/gwiki/src/ingest/session/gemini.rs:149-175] | Indexed function `parsed_gemini_tool_result` in `crates/gwiki/src/ingest/session/gemini.rs`. [crates/gwiki/src/ingest/session/gemini.rs:149-175] |
| `push_gemini_message` | function | `fn push_gemini_message(` | `push_gemini_message [function]` | `8d42e440-bc1b-5d40-a57d-e2b8467fe5ef` | 177-192 [crates/gwiki/src/ingest/session/gemini.rs:177-192] | Indexed function `push_gemini_message` in `crates/gwiki/src/ingest/session/gemini.rs`. [crates/gwiki/src/ingest/session/gemini.rs:177-192] |
| `render_gemini_content` | function | `fn render_gemini_content(content: &Value) -> Option<String> {` | `render_gemini_content [function]` | `a9a5237d-80c0-531d-9d27-64190bb73b1c` | 194-198 [crates/gwiki/src/ingest/session/gemini.rs:194-198] | Indexed function `render_gemini_content` in `crates/gwiki/src/ingest/session/gemini.rs`. [crates/gwiki/src/ingest/session/gemini.rs:194-198] |
| `append_gemini_content` | function | `fn append_gemini_content(value: &Value, parts: &mut Vec<String>) {` | `append_gemini_content [function]` | `b3664055-76a2-50cf-b260-78ed85f2db02` | 200-221 [crates/gwiki/src/ingest/session/gemini.rs:200-221] | Indexed function `append_gemini_content` in `crates/gwiki/src/ingest/session/gemini.rs`. [crates/gwiki/src/ingest/session/gemini.rs:200-221] |
| `render_gemini_content_block` | function | `fn render_gemini_content_block(block: &Value) -> Option<String> {` | `render_gemini_content_block [function]` | `8da72047-c2d5-5068-bf73-1fa0e93fc5dc` | 223-227 [crates/gwiki/src/ingest/session/gemini.rs:223-227] | Indexed function `render_gemini_content_block` in `crates/gwiki/src/ingest/session/gemini.rs`. [crates/gwiki/src/ingest/session/gemini.rs:223-227] |
| `append_call_id` | function | `fn append_call_id(content: &mut String, call_id: Option<&str>) {` | `append_call_id [function]` | `1ca79743-b53f-5269-9508-76688f12ab20` | 229-234 [crates/gwiki/src/ingest/session/gemini.rs:229-234] | Indexed function `append_call_id` in `crates/gwiki/src/ingest/session/gemini.rs`. [crates/gwiki/src/ingest/session/gemini.rs:229-234] |
| `render_jsonish_or_text` | function | `fn render_jsonish_or_text(value: &Value) -> String {` | `render_jsonish_or_text [function]` | `dc84d688-a6d4-5b7e-a7b3-7e85f13dac71` | 236-241 [crates/gwiki/src/ingest/session/gemini.rs:236-241] | Indexed function `render_jsonish_or_text` in `crates/gwiki/src/ingest/session/gemini.rs`. [crates/gwiki/src/ingest/session/gemini.rs:236-241] |
| `gemini_adapter_parses_stream_json_messages_and_tools` | function | `fn gemini_adapter_parses_stream_json_messages_and_tools() {` | `gemini_adapter_parses_stream_json_messages_and_tools [function]` | `7d505ed5-1dd5-5ba6-ab35-75aa828fd841` | 251-333 [crates/gwiki/src/ingest/session/gemini.rs:251-333] | Indexed function `gemini_adapter_parses_stream_json_messages_and_tools` in `crates/gwiki/src/ingest/session/gemini.rs`. [crates/gwiki/src/ingest/session/gemini.rs:251-333] |
| `gemini_adapter_parses_real_stream_when_fixture_is_set` | function | `fn gemini_adapter_parses_real_stream_when_fixture_is_set() {` | `gemini_adapter_parses_real_stream_when_fixture_is_set [function]` | `642a7df7-4916-5df9-a4bc-078ff1ca8f26` | 336-356 [crates/gwiki/src/ingest/session/gemini.rs:336-356] | Indexed function `gemini_adapter_parses_real_stream_when_fixture_is_set` in `crates/gwiki/src/ingest/session/gemini.rs`. [crates/gwiki/src/ingest/session/gemini.rs:336-356] |
