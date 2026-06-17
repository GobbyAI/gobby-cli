---
title: crates/gwiki/src/ingest/session/qwen.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/qwen.rs
  ranges:
  - '12'
  - 15-20
  - 22-24
  - 26-77
  - 81-89
  - 92-96
  - 98-104
  - 106-126
  - 128-145
  - 147-159
  - 161-169
  - 171-196
  - 198-211
  - 213-228
  - 230-236
  - 238-243
  - 245-247
  - 257-382
  - 385-407
  - 410-430
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/session/qwen.rs:12](crates/gwiki/src/ingest/session/qwen.rs#L12), [crates/gwiki/src/ingest/session/qwen.rs:15-20](crates/gwiki/src/ingest/session/qwen.rs#L15-L20), [crates/gwiki/src/ingest/session/qwen.rs:22-24](crates/gwiki/src/ingest/session/qwen.rs#L22-L24), [crates/gwiki/src/ingest/session/qwen.rs:26-77](crates/gwiki/src/ingest/session/qwen.rs#L26-L77), [crates/gwiki/src/ingest/session/qwen.rs:81-89](crates/gwiki/src/ingest/session/qwen.rs#L81-L89), [crates/gwiki/src/ingest/session/qwen.rs:92-96](crates/gwiki/src/ingest/session/qwen.rs#L92-L96), [crates/gwiki/src/ingest/session/qwen.rs:98-104](crates/gwiki/src/ingest/session/qwen.rs#L98-L104), [crates/gwiki/src/ingest/session/qwen.rs:106-126](crates/gwiki/src/ingest/session/qwen.rs#L106-L126), [crates/gwiki/src/ingest/session/qwen.rs:128-145](crates/gwiki/src/ingest/session/qwen.rs#L128-L145), [crates/gwiki/src/ingest/session/qwen.rs:147-159](crates/gwiki/src/ingest/session/qwen.rs#L147-L159), [crates/gwiki/src/ingest/session/qwen.rs:161-169](crates/gwiki/src/ingest/session/qwen.rs#L161-L169), [crates/gwiki/src/ingest/session/qwen.rs:171-196](crates/gwiki/src/ingest/session/qwen.rs#L171-L196), [crates/gwiki/src/ingest/session/qwen.rs:198-211](crates/gwiki/src/ingest/session/qwen.rs#L198-L211), [crates/gwiki/src/ingest/session/qwen.rs:213-228](crates/gwiki/src/ingest/session/qwen.rs#L213-L228), [crates/gwiki/src/ingest/session/qwen.rs:230-236](crates/gwiki/src/ingest/session/qwen.rs#L230-L236), [crates/gwiki/src/ingest/session/qwen.rs:238-243](crates/gwiki/src/ingest/session/qwen.rs#L238-L243), [crates/gwiki/src/ingest/session/qwen.rs:245-247](crates/gwiki/src/ingest/session/qwen.rs#L245-L247), [crates/gwiki/src/ingest/session/qwen.rs:257-382](crates/gwiki/src/ingest/session/qwen.rs#L257-L382), [crates/gwiki/src/ingest/session/qwen.rs:385-407](crates/gwiki/src/ingest/session/qwen.rs#L385-L407), [crates/gwiki/src/ingest/session/qwen.rs:410-430](crates/gwiki/src/ingest/session/qwen.rs#L410-L430)

</details>

# crates/gwiki/src/ingest/session/qwen.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the Qwen session transcript adapter for ingesting archived chat payloads into the wiki’s parsed session format. `QwenSessionAdapter` पहचान/filters supported envelopes and archives, parses each Qwen record into session metadata and visible messages, and uses helper functions and data models to normalize record types, roles, tool calls/responses, and rendered parts while skipping non-visible thought content; the tests verify wrapped payloads, tool/message handling, and real archive parsing.
[crates/gwiki/src/ingest/session/qwen.rs:12]
[crates/gwiki/src/ingest/session/qwen.rs:15-20]
[crates/gwiki/src/ingest/session/qwen.rs:22-24]
[crates/gwiki/src/ingest/session/qwen.rs:26-77]
[crates/gwiki/src/ingest/session/qwen.rs:81-89]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `QwenSessionAdapter` | class | `pub(super) struct QwenSessionAdapter;` | `QwenSessionAdapter [class]` | `eee4b49d-4b4d-5ca1-9e41-366740fd40f5` | 12-12 [crates/gwiki/src/ingest/session/qwen.rs:12] | Indexed class `QwenSessionAdapter` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:12] |
| `QwenSessionAdapter::supports` | method | `fn supports(&self, envelope_type: &str) -> bool {` | `QwenSessionAdapter::supports [method]` | `b2c51b10-415a-5e11-bde5-2e4c614df85b` | 15-20 [crates/gwiki/src/ingest/session/qwen.rs:15-20] | Indexed method `QwenSessionAdapter::supports` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:15-20] |
| `QwenSessionAdapter::supports_archive` | method | `fn supports_archive(&self, envelopes: &[SessionArchiveEnvelope]) -> bool {` | `QwenSessionAdapter::supports_archive [method]` | `63a00279-9589-56a3-b895-8839949cb38b` | 22-24 [crates/gwiki/src/ingest/session/qwen.rs:22-24] | Indexed method `QwenSessionAdapter::supports_archive` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:22-24] |
| `QwenSessionAdapter::parse` | method | `fn parse(&self, envelopes: &[SessionArchiveEnvelope]) -> Result<ParsedSession, WikiError> {` | `QwenSessionAdapter::parse [method]` | `ad509413-7c8a-5cda-a519-a960e1f6a80b` | 26-77 [crates/gwiki/src/ingest/session/qwen.rs:26-77] | Indexed method `QwenSessionAdapter::parse` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:26-77] |
| `QwenRecord` | class | `struct QwenRecord {` | `QwenRecord [class]` | `32f15781-c79e-5991-ae9a-3fafc5d8b993` | 81-89 [crates/gwiki/src/ingest/session/qwen.rs:81-89] | Indexed class `QwenRecord` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:81-89] |
| `QwenMessage` | class | `struct QwenMessage {` | `QwenMessage [class]` | `a01392ab-8445-5f80-b751-8a71e89c3f7f` | 92-96 [crates/gwiki/src/ingest/session/qwen.rs:92-96] | Indexed class `QwenMessage` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:92-96] |
| `qwen_record_type` | function | `fn qwen_record_type(envelope: &SessionArchiveEnvelope) -> &str {` | `qwen_record_type [function]` | `0fc01ea2-2c00-5d28-aa42-de340b4ab468` | 98-104 [crates/gwiki/src/ingest/session/qwen.rs:98-104] | Indexed function `qwen_record_type` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:98-104] |
| `is_qwen_record` | function | `fn is_qwen_record(envelope: &SessionArchiveEnvelope) -> bool {` | `is_qwen_record [function]` | `f9afaeef-d0fd-578c-9900-a429bc1266f1` | 106-126 [crates/gwiki/src/ingest/session/qwen.rs:106-126] | Indexed function `is_qwen_record` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:106-126] |
| `parsed_qwen_message` | function | `fn parsed_qwen_message(` | `parsed_qwen_message [function]` | `853a2bf5-c5be-5094-be42-d6f0e8bca17f` | 128-145 [crates/gwiki/src/ingest/session/qwen.rs:128-145] | Indexed function `parsed_qwen_message` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:128-145] |
| `qwen_message_role` | function | `fn qwen_message_role(record_type: &str, message: &QwenMessage) -> String {` | `qwen_message_role [function]` | `afe56666-cbc5-5f26-8e0b-b203571e287b` | 147-159 [crates/gwiki/src/ingest/session/qwen.rs:147-159] | Indexed function `qwen_message_role` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:147-159] |
| `render_qwen_parts` | function | `fn render_qwen_parts(parts: &[Value]) -> Option<String> {` | `render_qwen_parts [function]` | `0c628b48-4adf-5d09-99a3-f34bbd62874e` | 161-169 [crates/gwiki/src/ingest/session/qwen.rs:161-169] | Indexed function `render_qwen_parts` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:161-169] |
| `render_qwen_part` | function | `fn render_qwen_part(part: &Value) -> Option<String> {` | `render_qwen_part [function]` | `efd17c82-2b54-55af-a421-a2904d162756` | 171-196 [crates/gwiki/src/ingest/session/qwen.rs:171-196] | Indexed function `render_qwen_part` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:171-196] |
| `render_qwen_function_call` | function | `fn render_qwen_function_call(function_call: &Value) -> Option<String> {` | `render_qwen_function_call [function]` | `4d95167e-1794-5555-a256-ba821d59a5b0` | 198-211 [crates/gwiki/src/ingest/session/qwen.rs:198-211] | Indexed function `render_qwen_function_call` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:198-211] |
| `render_qwen_function_response` | function | `fn render_qwen_function_response(function_response: &Value) -> Option<String> {` | `render_qwen_function_response [function]` | `212112ec-025c-56bf-a5ba-041347a6564b` | 213-228 [crates/gwiki/src/ingest/session/qwen.rs:213-228] | Indexed function `render_qwen_function_response` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:213-228] |
| `qwen_tool_names` | function | `fn qwen_tool_names(parts: &[Value]) -> Vec<String> {` | `qwen_tool_names [function]` | `584feb0e-2147-5167-8ed3-3268597d288f` | 230-236 [crates/gwiki/src/ingest/session/qwen.rs:230-236] | Indexed function `qwen_tool_names` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:230-236] |
| `render_jsonish_or_text` | function | `fn render_jsonish_or_text(value: &Value) -> String {` | `render_jsonish_or_text [function]` | `b6548d52-a57d-583d-aeac-f7dbdd1953d7` | 238-243 [crates/gwiki/src/ingest/session/qwen.rs:238-243] | Indexed function `render_jsonish_or_text` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:238-243] |
| `qwen_part_has_function_response` | function | `fn qwen_part_has_function_response(part: &Value) -> bool {` | `qwen_part_has_function_response [function]` | `79b9b42f-3f66-52c2-a78d-db135e5026fa` | 245-247 [crates/gwiki/src/ingest/session/qwen.rs:245-247] | Indexed function `qwen_part_has_function_response` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:245-247] |
| `qwen_adapter_parses_messages_tools_and_skips_thoughts` | function | `fn qwen_adapter_parses_messages_tools_and_skips_thoughts() {` | `qwen_adapter_parses_messages_tools_and_skips_thoughts [function]` | `07c99793-ff85-5c3b-9382-2cec4a8db490` | 257-382 [crates/gwiki/src/ingest/session/qwen.rs:257-382] | Indexed function `qwen_adapter_parses_messages_tools_and_skips_thoughts` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:257-382] |
| `qwen_adapter_accepts_envelope_wrapped_payload_records` | function | `fn qwen_adapter_accepts_envelope_wrapped_payload_records() {` | `qwen_adapter_accepts_envelope_wrapped_payload_records [function]` | `b5ab2227-52c0-5694-bdc2-706459e63840` | 385-407 [crates/gwiki/src/ingest/session/qwen.rs:385-407] | Indexed function `qwen_adapter_accepts_envelope_wrapped_payload_records` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:385-407] |
| `qwen_adapter_parses_real_archive_when_fixture_is_set` | function | `fn qwen_adapter_parses_real_archive_when_fixture_is_set() {` | `qwen_adapter_parses_real_archive_when_fixture_is_set [function]` | `6c625a5c-b044-5a7a-af33-9cf940bc5cad` | 410-430 [crates/gwiki/src/ingest/session/qwen.rs:410-430] | Indexed function `qwen_adapter_parses_real_archive_when_fixture_is_set` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:410-430] |
