---
title: crates/gwiki/src/ingest/session/grok.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/grok.rs
  ranges:
  - '12'
  - 15-20
  - 22-32
  - 34-104
  - 108-118
  - 121-125
  - 127-139
  - 141-153
  - 155-188
  - 190-212
  - 214-232
  - 234-250
  - 252-256
  - 258-279
  - 281-285
  - 287-292
  - 294-299
  - 309-376
  - 379-408
  - 411-430
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/session/grok.rs:12](crates/gwiki/src/ingest/session/grok.rs#L12), [crates/gwiki/src/ingest/session/grok.rs:15-20](crates/gwiki/src/ingest/session/grok.rs#L15-L20), [crates/gwiki/src/ingest/session/grok.rs:22-32](crates/gwiki/src/ingest/session/grok.rs#L22-L32), [crates/gwiki/src/ingest/session/grok.rs:34-104](crates/gwiki/src/ingest/session/grok.rs#L34-L104), [crates/gwiki/src/ingest/session/grok.rs:108-118](crates/gwiki/src/ingest/session/grok.rs#L108-L118), [crates/gwiki/src/ingest/session/grok.rs:121-125](crates/gwiki/src/ingest/session/grok.rs#L121-L125), [crates/gwiki/src/ingest/session/grok.rs:127-139](crates/gwiki/src/ingest/session/grok.rs#L127-L139), [crates/gwiki/src/ingest/session/grok.rs:141-153](crates/gwiki/src/ingest/session/grok.rs#L141-L153), [crates/gwiki/src/ingest/session/grok.rs:155-188](crates/gwiki/src/ingest/session/grok.rs#L155-L188), [crates/gwiki/src/ingest/session/grok.rs:190-212](crates/gwiki/src/ingest/session/grok.rs#L190-L212), [crates/gwiki/src/ingest/session/grok.rs:214-232](crates/gwiki/src/ingest/session/grok.rs#L214-L232), [crates/gwiki/src/ingest/session/grok.rs:234-250](crates/gwiki/src/ingest/session/grok.rs#L234-L250), [crates/gwiki/src/ingest/session/grok.rs:252-256](crates/gwiki/src/ingest/session/grok.rs#L252-L256), [crates/gwiki/src/ingest/session/grok.rs:258-279](crates/gwiki/src/ingest/session/grok.rs#L258-L279), [crates/gwiki/src/ingest/session/grok.rs:281-285](crates/gwiki/src/ingest/session/grok.rs#L281-L285), [crates/gwiki/src/ingest/session/grok.rs:287-292](crates/gwiki/src/ingest/session/grok.rs#L287-L292), [crates/gwiki/src/ingest/session/grok.rs:294-299](crates/gwiki/src/ingest/session/grok.rs#L294-L299), [crates/gwiki/src/ingest/session/grok.rs:309-376](crates/gwiki/src/ingest/session/grok.rs#L309-L376), [crates/gwiki/src/ingest/session/grok.rs:379-408](crates/gwiki/src/ingest/session/grok.rs#L379-L408), [crates/gwiki/src/ingest/session/grok.rs:411-430](crates/gwiki/src/ingest/session/grok.rs#L411-L430)

</details>

# crates/gwiki/src/ingest/session/grok.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements a `SessionTranscriptAdapter` for Grok archives, turning Grok session envelopes into a `ParsedSession` with metadata, timestamps, and normalized messages. `GrokSessionAdapter` first decides whether an envelope type or archive looks like Grok, then `parse` deserializes each supported record into `GrokRecord`/`GrokToolCall` and dispatches to helpers that build chat messages, streaming text chunks, tool calls and results, errors, and content rendering, merging adjacent message parts when needed. The file also includes tests covering local chat history, streaming JSON text chunks, and a real archive fixture path.
[crates/gwiki/src/ingest/session/grok.rs:12]
[crates/gwiki/src/ingest/session/grok.rs:15-20]
[crates/gwiki/src/ingest/session/grok.rs:22-32]
[crates/gwiki/src/ingest/session/grok.rs:34-104]
[crates/gwiki/src/ingest/session/grok.rs:108-118]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `GrokSessionAdapter` | class | `pub(super) struct GrokSessionAdapter;` | `GrokSessionAdapter [class]` | `724b03e2-ae94-5977-9f2a-e9b3d50529fc` | 12-12 [crates/gwiki/src/ingest/session/grok.rs:12] | Indexed class `GrokSessionAdapter` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:12] |
| `GrokSessionAdapter::supports` | method | `fn supports(&self, envelope_type: &str) -> bool {` | `GrokSessionAdapter::supports [method]` | `58ff2c03-d108-580f-896d-48445a1037fb` | 15-20 [crates/gwiki/src/ingest/session/grok.rs:15-20] | Indexed method `GrokSessionAdapter::supports` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:15-20] |
| `GrokSessionAdapter::supports_archive` | method | `fn supports_archive(&self, envelopes: &[SessionArchiveEnvelope]) -> bool {` | `GrokSessionAdapter::supports_archive [method]` | `431f1442-e4fd-5de7-b025-dcba678c4d8b` | 22-32 [crates/gwiki/src/ingest/session/grok.rs:22-32] | Indexed method `GrokSessionAdapter::supports_archive` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:22-32] |
| `GrokSessionAdapter::parse` | method | `fn parse(&self, envelopes: &[SessionArchiveEnvelope]) -> Result<ParsedSession, WikiError> {` | `GrokSessionAdapter::parse [method]` | `86cd130b-5c1b-5c01-bc71-5fe8f8b24cec` | 34-104 [crates/gwiki/src/ingest/session/grok.rs:34-104] | Indexed method `GrokSessionAdapter::parse` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:34-104] |
| `GrokRecord` | class | `struct GrokRecord {` | `GrokRecord [class]` | `4abc683e-a4ed-5a41-8d97-630feef26e0c` | 108-118 [crates/gwiki/src/ingest/session/grok.rs:108-118] | Indexed class `GrokRecord` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:108-118] |
| `GrokToolCall` | class | `struct GrokToolCall {` | `GrokToolCall [class]` | `f958a1e5-2344-52b0-b553-8f546fbb1032` | 121-125 [crates/gwiki/src/ingest/session/grok.rs:121-125] | Indexed class `GrokToolCall` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:121-125] |
| `parsed_grok_chat_message` | function | `fn parsed_grok_chat_message(` | `parsed_grok_chat_message [function]` | `04ad594c-49ca-517a-a50f-5da744ed3985` | 127-139 [crates/gwiki/src/ingest/session/grok.rs:127-139] | Indexed function `parsed_grok_chat_message` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:127-139] |
| `parsed_grok_stream_text` | function | `fn parsed_grok_stream_text(` | `parsed_grok_stream_text [function]` | `c952fe21-a159-5da1-85da-bb6f89a70867` | 141-153 [crates/gwiki/src/ingest/session/grok.rs:141-153] | Indexed function `parsed_grok_stream_text` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:141-153] |
| `parsed_grok_tool_calls` | function | `fn parsed_grok_tool_calls(` | `parsed_grok_tool_calls [function]` | `06a2334d-2b93-5559-9845-2762ec64f38b` | 155-188 [crates/gwiki/src/ingest/session/grok.rs:155-188] | Indexed function `parsed_grok_tool_calls` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:155-188] |
| `parsed_grok_tool_result` | function | `fn parsed_grok_tool_result(` | `parsed_grok_tool_result [function]` | `ff99685e-51c0-535c-a145-76968a52c1d9` | 190-212 [crates/gwiki/src/ingest/session/grok.rs:190-212] | Indexed function `parsed_grok_tool_result` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:190-212] |
| `parsed_grok_error` | function | `fn parsed_grok_error(` | `parsed_grok_error [function]` | `cc11ff77-8a51-5972-8154-20080cc11104` | 214-232 [crates/gwiki/src/ingest/session/grok.rs:214-232] | Indexed function `parsed_grok_error` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:214-232] |
| `push_or_append_message` | function | `fn push_or_append_message(` | `push_or_append_message [function]` | `118444db-6f7a-562a-89a4-2dd7cb585a42` | 234-250 [crates/gwiki/src/ingest/session/grok.rs:234-250] | Indexed function `push_or_append_message` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:234-250] |
| `render_grok_content` | function | `fn render_grok_content(content: &Value) -> Option<String> {` | `render_grok_content [function]` | `48cf894e-351a-5151-a9fe-2b7832227d51` | 252-256 [crates/gwiki/src/ingest/session/grok.rs:252-256] | Indexed function `render_grok_content` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:252-256] |
| `append_grok_content` | function | `fn append_grok_content(value: &Value, parts: &mut Vec<String>) {` | `append_grok_content [function]` | `4c7c414b-756c-5185-ba61-077a1eee9cc5` | 258-279 [crates/gwiki/src/ingest/session/grok.rs:258-279] | Indexed function `append_grok_content` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:258-279] |
| `render_grok_content_block` | function | `fn render_grok_content_block(block: &Value) -> Option<String> {` | `render_grok_content_block [function]` | `462d0105-beb6-53e0-b0ec-c401258959a9` | 281-285 [crates/gwiki/src/ingest/session/grok.rs:281-285] | Indexed function `render_grok_content_block` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:281-285] |
| `append_call_id` | function | `fn append_call_id(content: &mut String, call_id: Option<&str>) {` | `append_call_id [function]` | `6f81fd48-8446-5c8c-b035-8893d9f877e7` | 287-292 [crates/gwiki/src/ingest/session/grok.rs:287-292] | Indexed function `append_call_id` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:287-292] |
| `render_jsonish_or_text` | function | `fn render_jsonish_or_text(value: &Value) -> String {` | `render_jsonish_or_text [function]` | `1ca4fb54-43ef-5c18-a6bd-9216cf05f539` | 294-299 [crates/gwiki/src/ingest/session/grok.rs:294-299] | Indexed function `render_jsonish_or_text` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:294-299] |
| `grok_adapter_parses_local_chat_history_messages_and_tools` | function | `fn grok_adapter_parses_local_chat_history_messages_and_tools() {` | `grok_adapter_parses_local_chat_history_messages_and_tools [function]` | `8ebc6c0e-f6cd-5ece-81a4-3f109dda7274` | 309-376 [crates/gwiki/src/ingest/session/grok.rs:309-376] | Indexed function `grok_adapter_parses_local_chat_history_messages_and_tools` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:309-376] |
| `grok_adapter_parses_streaming_json_text_chunks` | function | `fn grok_adapter_parses_streaming_json_text_chunks() {` | `grok_adapter_parses_streaming_json_text_chunks [function]` | `bc408ed0-bbfa-5aea-bd97-c146a952cb55` | 379-408 [crates/gwiki/src/ingest/session/grok.rs:379-408] | Indexed function `grok_adapter_parses_streaming_json_text_chunks` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:379-408] |
| `grok_adapter_parses_real_archive_when_fixture_is_set` | function | `fn grok_adapter_parses_real_archive_when_fixture_is_set() {` | `grok_adapter_parses_real_archive_when_fixture_is_set [function]` | `82053cf0-1566-53e0-86f9-2c2bdb24b368` | 411-430 [crates/gwiki/src/ingest/session/grok.rs:411-430] | Indexed function `grok_adapter_parses_real_archive_when_fixture_is_set` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:411-430] |
