---
title: crates/gwiki/src/ingest/session/droid.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/droid.rs
  ranges:
  - '12'
  - 15-17
  - 19-21
  - 23-77
  - 81-91
  - 94-97
  - 99-105
  - 107-114
  - 116-137
  - 139-148
  - 150-160
  - 162-166
  - 168-189
  - 191-202
  - 204-217
  - 219-223
  - 225-244
  - 246-277
  - 279-284
  - 286-297
  - 307-415
  - 418-432
  - 435-454
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/session/droid.rs:12](crates/gwiki/src/ingest/session/droid.rs#L12), [crates/gwiki/src/ingest/session/droid.rs:15-17](crates/gwiki/src/ingest/session/droid.rs#L15-L17), [crates/gwiki/src/ingest/session/droid.rs:19-21](crates/gwiki/src/ingest/session/droid.rs#L19-L21), [crates/gwiki/src/ingest/session/droid.rs:23-77](crates/gwiki/src/ingest/session/droid.rs#L23-L77), [crates/gwiki/src/ingest/session/droid.rs:81-91](crates/gwiki/src/ingest/session/droid.rs#L81-L91), [crates/gwiki/src/ingest/session/droid.rs:94-97](crates/gwiki/src/ingest/session/droid.rs#L94-L97), [crates/gwiki/src/ingest/session/droid.rs:99-105](crates/gwiki/src/ingest/session/droid.rs#L99-L105), [crates/gwiki/src/ingest/session/droid.rs:107-114](crates/gwiki/src/ingest/session/droid.rs#L107-L114), [crates/gwiki/src/ingest/session/droid.rs:116-137](crates/gwiki/src/ingest/session/droid.rs#L116-L137), [crates/gwiki/src/ingest/session/droid.rs:139-148](crates/gwiki/src/ingest/session/droid.rs#L139-L148), [crates/gwiki/src/ingest/session/droid.rs:150-160](crates/gwiki/src/ingest/session/droid.rs#L150-L160), [crates/gwiki/src/ingest/session/droid.rs:162-166](crates/gwiki/src/ingest/session/droid.rs#L162-L166), [crates/gwiki/src/ingest/session/droid.rs:168-189](crates/gwiki/src/ingest/session/droid.rs#L168-L189), [crates/gwiki/src/ingest/session/droid.rs:191-202](crates/gwiki/src/ingest/session/droid.rs#L191-L202), [crates/gwiki/src/ingest/session/droid.rs:204-217](crates/gwiki/src/ingest/session/droid.rs#L204-L217), [crates/gwiki/src/ingest/session/droid.rs:219-223](crates/gwiki/src/ingest/session/droid.rs#L219-L223), [crates/gwiki/src/ingest/session/droid.rs:225-244](crates/gwiki/src/ingest/session/droid.rs#L225-L244), [crates/gwiki/src/ingest/session/droid.rs:246-277](crates/gwiki/src/ingest/session/droid.rs#L246-L277), [crates/gwiki/src/ingest/session/droid.rs:279-284](crates/gwiki/src/ingest/session/droid.rs#L279-L284), [crates/gwiki/src/ingest/session/droid.rs:286-297](crates/gwiki/src/ingest/session/droid.rs#L286-L297), [crates/gwiki/src/ingest/session/droid.rs:307-415](crates/gwiki/src/ingest/session/droid.rs#L307-L415), [crates/gwiki/src/ingest/session/droid.rs:418-432](crates/gwiki/src/ingest/session/droid.rs#L418-L432), [crates/gwiki/src/ingest/session/droid.rs:435-454](crates/gwiki/src/ingest/session/droid.rs#L435-L454)

</details>

# crates/gwiki/src/ingest/session/droid.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements the Droid session transcript adapter for ingesting archived session data into a normalized `ParsedSession`. `DroidSessionAdapter` declares support for `message` and `session_start` envelopes, detects Droid archives by looking for a session start record, then parses envelopes into session metadata and ordered messages while rejecting archives that do not contain usable message content.

The helper functions break that work into small steps: identifying Droid record types, recognizing session-start and hidden-context records, extracting message roles, rendering content and tool use/result payloads, collecting tool names, and deciding when JSON-like content should be emitted as pretty JSON versus plain text. The tests cover persisted records, envelope-wrapped payloads, and real fixture archives to confirm the adapter handles both session metadata and tool interactions correctly.
[crates/gwiki/src/ingest/session/droid.rs:12]
[crates/gwiki/src/ingest/session/droid.rs:15-17]
[crates/gwiki/src/ingest/session/droid.rs:19-21]
[crates/gwiki/src/ingest/session/droid.rs:23-77]
[crates/gwiki/src/ingest/session/droid.rs:81-91]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `DroidSessionAdapter` | class | `pub(super) struct DroidSessionAdapter;` | `DroidSessionAdapter [class]` | `d1d653d4-549d-5d60-95e5-436601680da4` | 12-12 [crates/gwiki/src/ingest/session/droid.rs:12] | Indexed class `DroidSessionAdapter` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:12] |
| `DroidSessionAdapter::supports` | method | `fn supports(&self, envelope_type: &str) -> bool {` | `DroidSessionAdapter::supports [method]` | `00f7d870-7dd9-55b0-b637-e1ccdc6baed5` | 15-17 [crates/gwiki/src/ingest/session/droid.rs:15-17] | Indexed method `DroidSessionAdapter::supports` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:15-17] |
| `DroidSessionAdapter::supports_archive` | method | `fn supports_archive(&self, envelopes: &[SessionArchiveEnvelope]) -> bool {` | `DroidSessionAdapter::supports_archive [method]` | `260f3293-c8b7-5f7d-995a-e6a99718c2aa` | 19-21 [crates/gwiki/src/ingest/session/droid.rs:19-21] | Indexed method `DroidSessionAdapter::supports_archive` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:19-21] |
| `DroidSessionAdapter::parse` | method | `fn parse(&self, envelopes: &[SessionArchiveEnvelope]) -> Result<ParsedSession, WikiError> {` | `DroidSessionAdapter::parse [method]` | `601197eb-5801-588e-a6ba-1253bb1a8ec4` | 23-77 [crates/gwiki/src/ingest/session/droid.rs:23-77] | Indexed method `DroidSessionAdapter::parse` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:23-77] |
| `DroidRecord` | class | `struct DroidRecord {` | `DroidRecord [class]` | `2433a147-4015-5a42-acc2-8659bbe07199` | 81-91 [crates/gwiki/src/ingest/session/droid.rs:81-91] | Indexed class `DroidRecord` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:81-91] |
| `DroidMessage` | class | `struct DroidMessage {` | `DroidMessage [class]` | `e932bd63-afc2-5937-81f4-5f17135e0eb7` | 94-97 [crates/gwiki/src/ingest/session/droid.rs:94-97] | Indexed class `DroidMessage` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:94-97] |
| `droid_record_type` | function | `fn droid_record_type(envelope: &SessionArchiveEnvelope) -> &str {` | `droid_record_type [function]` | `01892012-c4ed-585c-adc5-180f9b12f90b` | 99-105 [crates/gwiki/src/ingest/session/droid.rs:99-105] | Indexed function `droid_record_type` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:99-105] |
| `is_droid_session_start` | function | `fn is_droid_session_start(envelope: &SessionArchiveEnvelope) -> bool {` | `is_droid_session_start [function]` | `f435dd21-d587-5e3d-b3da-3b91f58d4211` | 107-114 [crates/gwiki/src/ingest/session/droid.rs:107-114] | Indexed function `is_droid_session_start` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:107-114] |
| `parsed_droid_message` | function | `fn parsed_droid_message(` | `parsed_droid_message [function]` | `7bd45590-a4ad-518e-a889-e1bb50a10709` | 116-137 [crates/gwiki/src/ingest/session/droid.rs:116-137] | Indexed function `parsed_droid_message` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:116-137] |
| `is_hidden_context_record` | function | `fn is_hidden_context_record(record: &DroidRecord) -> bool {` | `is_hidden_context_record [function]` | `bfb3f3d4-4fba-5fc8-ae22-ab1d81f1ad9e` | 139-148 [crates/gwiki/src/ingest/session/droid.rs:139-148] | Indexed function `is_hidden_context_record` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:139-148] |
| `droid_message_role` | function | `fn droid_message_role(message: &DroidMessage) -> String {` | `droid_message_role [function]` | `d0a65821-1d91-53d2-bdf9-d95972c5e395` | 150-160 [crates/gwiki/src/ingest/session/droid.rs:150-160] | Indexed function `droid_message_role` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:150-160] |
| `render_droid_content` | function | `fn render_droid_content(content: &Value) -> Option<String> {` | `render_droid_content [function]` | `7a73119c-3fbd-5dbc-86a4-303b545c25f4` | 162-166 [crates/gwiki/src/ingest/session/droid.rs:162-166] | Indexed function `render_droid_content` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:162-166] |
| `append_droid_content` | function | `fn append_droid_content(value: &Value, parts: &mut Vec<String>) {` | `append_droid_content [function]` | `552f7a15-2cfa-55bd-87ab-1d6b1968f7f6` | 168-189 [crates/gwiki/src/ingest/session/droid.rs:168-189] | Indexed function `append_droid_content` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:168-189] |
| `render_droid_content_block` | function | `fn render_droid_content_block(block: &Value) -> Option<String> {` | `render_droid_content_block [function]` | `e31d540a-e753-55af-a17e-5221a9bf721d` | 191-202 [crates/gwiki/src/ingest/session/droid.rs:191-202] | Indexed function `render_droid_content_block` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:191-202] |
| `render_droid_tool_use` | function | `fn render_droid_tool_use(block: &Value) -> Option<String> {` | `render_droid_tool_use [function]` | `1dc704b4-a8d7-5c93-8314-3edc3903d7da` | 204-217 [crates/gwiki/src/ingest/session/droid.rs:204-217] | Indexed function `render_droid_tool_use` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:204-217] |
| `droid_tool_names` | function | `fn droid_tool_names(content: &Value) -> Vec<String> {` | `droid_tool_names [function]` | `7fb499f6-4444-596d-b51a-42a60d23e803` | 219-223 [crates/gwiki/src/ingest/session/droid.rs:219-223] | Indexed function `droid_tool_names` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:219-223] |
| `collect_droid_tool_names` | function | `fn collect_droid_tool_names(value: &Value, names: &mut Vec<String>) {` | `collect_droid_tool_names [function]` | `ad2f1d01-1567-5400-84c6-ad7885143905` | 225-244 [crates/gwiki/src/ingest/session/droid.rs:225-244] | Indexed function `collect_droid_tool_names` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:225-244] |
| `render_droid_tool_result` | function | `fn render_droid_tool_result(block: &Value) -> Option<String> {` | `render_droid_tool_result [function]` | `da96d7a6-f0dc-5bb8-8f2f-3f3ab591d6e2` | 246-277 [crates/gwiki/src/ingest/session/droid.rs:246-277] | Indexed function `render_droid_tool_result` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:246-277] |
| `render_jsonish_or_text` | function | `fn render_jsonish_or_text(value: &Value) -> String {` | `render_jsonish_or_text [function]` | `a6db41df-1270-5d2b-8bc1-3d92fc6a2fd5` | 279-284 [crates/gwiki/src/ingest/session/droid.rs:279-284] | Indexed function `render_jsonish_or_text` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:279-284] |
| `content_has_block_type` | function | `fn content_has_block_type(value: &Value, expected_type: &str) -> bool {` | `content_has_block_type [function]` | `bac00586-3208-549a-bf4d-8b6a68886acc` | 286-297 [crates/gwiki/src/ingest/session/droid.rs:286-297] | Indexed function `content_has_block_type` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:286-297] |
| `droid_adapter_parses_persisted_messages_and_tools` | function | `fn droid_adapter_parses_persisted_messages_and_tools() {` | `droid_adapter_parses_persisted_messages_and_tools [function]` | `41a61251-5b52-50b5-889d-854c192526e9` | 307-415 [crates/gwiki/src/ingest/session/droid.rs:307-415] | Indexed function `droid_adapter_parses_persisted_messages_and_tools` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:307-415] |
| `droid_adapter_accepts_envelope_wrapped_payload_records` | function | `fn droid_adapter_accepts_envelope_wrapped_payload_records() {` | `droid_adapter_accepts_envelope_wrapped_payload_records [function]` | `36f9a2b1-d3d7-57a5-8f99-32123854451c` | 418-432 [crates/gwiki/src/ingest/session/droid.rs:418-432] | Indexed function `droid_adapter_accepts_envelope_wrapped_payload_records` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:418-432] |
| `droid_adapter_parses_real_archive_when_fixture_is_set` | function | `fn droid_adapter_parses_real_archive_when_fixture_is_set() {` | `droid_adapter_parses_real_archive_when_fixture_is_set [function]` | `c99abb33-c55a-5f49-9c0a-fa3d1aba2b8a` | 435-454 [crates/gwiki/src/ingest/session/droid.rs:435-454] | Indexed function `droid_adapter_parses_real_archive_when_fixture_is_set` in `crates/gwiki/src/ingest/session/droid.rs`. [crates/gwiki/src/ingest/session/droid.rs:435-454] |
