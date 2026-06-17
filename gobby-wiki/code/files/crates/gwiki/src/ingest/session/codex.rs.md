---
title: crates/gwiki/src/ingest/session/codex.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/codex.rs
  ranges:
  - '12'
  - 15-20
  - 22-96
  - 100-105
  - 108-110
  - 113-117
  - 120-131
  - 133-156
  - 158-180
  - 182-204
  - 206-226
  - 228-242
  - 244-258
  - 260-274
  - 276-280
  - 282-303
  - 305-309
  - 311-316
  - 318-323
  - 325-330
  - 332-339
  - 352-471
  - 474-541
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/session/codex.rs:12](crates/gwiki/src/ingest/session/codex.rs#L12), [crates/gwiki/src/ingest/session/codex.rs:15-20](crates/gwiki/src/ingest/session/codex.rs#L15-L20), [crates/gwiki/src/ingest/session/codex.rs:22-96](crates/gwiki/src/ingest/session/codex.rs#L22-L96), [crates/gwiki/src/ingest/session/codex.rs:100-105](crates/gwiki/src/ingest/session/codex.rs#L100-L105), [crates/gwiki/src/ingest/session/codex.rs:108-110](crates/gwiki/src/ingest/session/codex.rs#L108-L110), [crates/gwiki/src/ingest/session/codex.rs:113-117](crates/gwiki/src/ingest/session/codex.rs#L113-L117), [crates/gwiki/src/ingest/session/codex.rs:120-131](crates/gwiki/src/ingest/session/codex.rs#L120-L131), [crates/gwiki/src/ingest/session/codex.rs:133-156](crates/gwiki/src/ingest/session/codex.rs#L133-L156), [crates/gwiki/src/ingest/session/codex.rs:158-180](crates/gwiki/src/ingest/session/codex.rs#L158-L180), [crates/gwiki/src/ingest/session/codex.rs:182-204](crates/gwiki/src/ingest/session/codex.rs#L182-L204), [crates/gwiki/src/ingest/session/codex.rs:206-226](crates/gwiki/src/ingest/session/codex.rs#L206-L226), [crates/gwiki/src/ingest/session/codex.rs:228-242](crates/gwiki/src/ingest/session/codex.rs#L228-L242), [crates/gwiki/src/ingest/session/codex.rs:244-258](crates/gwiki/src/ingest/session/codex.rs#L244-L258), [crates/gwiki/src/ingest/session/codex.rs:260-274](crates/gwiki/src/ingest/session/codex.rs#L260-L274), [crates/gwiki/src/ingest/session/codex.rs:276-280](crates/gwiki/src/ingest/session/codex.rs#L276-L280), [crates/gwiki/src/ingest/session/codex.rs:282-303](crates/gwiki/src/ingest/session/codex.rs#L282-L303), [crates/gwiki/src/ingest/session/codex.rs:305-309](crates/gwiki/src/ingest/session/codex.rs#L305-L309), [crates/gwiki/src/ingest/session/codex.rs:311-316](crates/gwiki/src/ingest/session/codex.rs#L311-L316), [crates/gwiki/src/ingest/session/codex.rs:318-323](crates/gwiki/src/ingest/session/codex.rs#L318-L323), [crates/gwiki/src/ingest/session/codex.rs:325-330](crates/gwiki/src/ingest/session/codex.rs#L325-L330), [crates/gwiki/src/ingest/session/codex.rs:332-339](crates/gwiki/src/ingest/session/codex.rs#L332-L339), [crates/gwiki/src/ingest/session/codex.rs:352-471](crates/gwiki/src/ingest/session/codex.rs#L352-L471), [crates/gwiki/src/ingest/session/codex.rs:474-541](crates/gwiki/src/ingest/session/codex.rs#L474-L541)

</details>

# crates/gwiki/src/ingest/session/codex.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines `CodexSessionAdapter`, an implementation of `SessionTranscriptAdapter` that recognizes Codex archive envelope types and converts them into a normalized `ParsedSession`. Its `parse` logic walks supported envelopes, extracts session metadata such as start time, model, branch, and session type, and dispatches Codex-specific payloads through helper parsers for event messages, response items, function calls/outputs, and tool-search calls/outputs. The rendering helpers format content and JSON-ish values into text blocks, and the tests cover parsing both synthetic message/tool-item cases and a real archive fixture when enabled.
[crates/gwiki/src/ingest/session/codex.rs:12]
[crates/gwiki/src/ingest/session/codex.rs:15-20]
[crates/gwiki/src/ingest/session/codex.rs:22-96]
[crates/gwiki/src/ingest/session/codex.rs:100-105]
[crates/gwiki/src/ingest/session/codex.rs:108-110]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CodexSessionAdapter` | class | `pub(super) struct CodexSessionAdapter;` | `CodexSessionAdapter [class]` | `15267d70-ca9b-5ff1-99b3-78619085b140` | 12-12 [crates/gwiki/src/ingest/session/codex.rs:12] | Indexed class `CodexSessionAdapter` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:12] |
| `CodexSessionAdapter::supports` | method | `fn supports(&self, envelope_type: &str) -> bool {` | `CodexSessionAdapter::supports [method]` | `893b9cf9-0451-5249-a4fc-2707cdf6d4b5` | 15-20 [crates/gwiki/src/ingest/session/codex.rs:15-20] | Indexed method `CodexSessionAdapter::supports` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:15-20] |
| `CodexSessionAdapter::parse` | method | `fn parse(&self, envelopes: &[SessionArchiveEnvelope]) -> Result<ParsedSession, WikiError> {` | `CodexSessionAdapter::parse [method]` | `a273032b-c75f-527c-81f2-0c4bc7035c34` | 22-96 [crates/gwiki/src/ingest/session/codex.rs:22-96] | Indexed method `CodexSessionAdapter::parse` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:22-96] |
| `CodexSessionMeta` | class | `struct CodexSessionMeta {` | `CodexSessionMeta [class]` | `d81b7fc0-a29e-5ef0-97bd-739906ac9aa9` | 100-105 [crates/gwiki/src/ingest/session/codex.rs:100-105] | Indexed class `CodexSessionMeta` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:100-105] |
| `CodexGitMetadata` | class | `struct CodexGitMetadata {` | `CodexGitMetadata [class]` | `63bcf4e5-71fe-5bfc-8da7-bddab2fa3a11` | 108-110 [crates/gwiki/src/ingest/session/codex.rs:108-110] | Indexed class `CodexGitMetadata` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:108-110] |
| `CodexEventPayload` | class | `struct CodexEventPayload {` | `CodexEventPayload [class]` | `04dd0d53-f2d6-5b8a-b34b-e0d3b5e5b3b5` | 113-117 [crates/gwiki/src/ingest/session/codex.rs:113-117] | Indexed class `CodexEventPayload` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:113-117] |
| `CodexResponseItem` | class | `struct CodexResponseItem {` | `CodexResponseItem [class]` | `3a3d1367-2011-596b-9f21-1f8518181150` | 120-131 [crates/gwiki/src/ingest/session/codex.rs:120-131] | Indexed class `CodexResponseItem` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:120-131] |
| `parsed_codex_event_message` | function | `fn parsed_codex_event_message(` | `parsed_codex_event_message [function]` | `ee11657a-dbc9-5ac9-bbc9-968f6aad4d07` | 133-156 [crates/gwiki/src/ingest/session/codex.rs:133-156] | Indexed function `parsed_codex_event_message` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:133-156] |
| `parsed_codex_response_item` | function | `fn parsed_codex_response_item(` | `parsed_codex_response_item [function]` | `17b87d33-9141-5cf7-8fa9-2c18da3c0ea2` | 158-180 [crates/gwiki/src/ingest/session/codex.rs:158-180] | Indexed function `parsed_codex_response_item` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:158-180] |
| `parsed_codex_response_message` | function | `fn parsed_codex_response_message(` | `parsed_codex_response_message [function]` | `11de5e8a-050f-5853-a051-c886610a1e1c` | 182-204 [crates/gwiki/src/ingest/session/codex.rs:182-204] | Indexed function `parsed_codex_response_message` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:182-204] |
| `parsed_codex_function_call` | function | `fn parsed_codex_function_call(` | `parsed_codex_function_call [function]` | `e3427821-de25-57e6-b9d5-89c7e84d97d1` | 206-226 [crates/gwiki/src/ingest/session/codex.rs:206-226] | Indexed function `parsed_codex_function_call` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:206-226] |
| `parsed_codex_function_output` | function | `fn parsed_codex_function_output(` | `parsed_codex_function_output [function]` | `940fb53d-f326-57a9-8110-f88971092b8d` | 228-242 [crates/gwiki/src/ingest/session/codex.rs:228-242] | Indexed function `parsed_codex_function_output` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:228-242] |
| `parsed_codex_tool_search_call` | function | `fn parsed_codex_tool_search_call(` | `parsed_codex_tool_search_call [function]` | `adf9c99c-c2dc-5382-80ca-0d88110be284` | 244-258 [crates/gwiki/src/ingest/session/codex.rs:244-258] | Indexed function `parsed_codex_tool_search_call` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:244-258] |
| `parsed_codex_tool_search_output` | function | `fn parsed_codex_tool_search_output(` | `parsed_codex_tool_search_output [function]` | `877faf57-d9a3-579a-938c-bcd9f4aaf72f` | 260-274 [crates/gwiki/src/ingest/session/codex.rs:260-274] | Indexed function `parsed_codex_tool_search_output` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:260-274] |
| `render_codex_content` | function | `fn render_codex_content(content: &Value) -> Option<String> {` | `render_codex_content [function]` | `8519de77-8278-5306-be4a-f998dbbc1985` | 276-280 [crates/gwiki/src/ingest/session/codex.rs:276-280] | Indexed function `render_codex_content` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:276-280] |
| `append_codex_content` | function | `fn append_codex_content(value: &Value, parts: &mut Vec<String>) {` | `append_codex_content [function]` | `46402732-b1de-5b33-bd48-5c3972b36b35` | 282-303 [crates/gwiki/src/ingest/session/codex.rs:282-303] | Indexed function `append_codex_content` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:282-303] |
| `render_codex_content_block` | function | `fn render_codex_content_block(block: &Value) -> Option<String> {` | `render_codex_content_block [function]` | `e288533e-f1e7-53c1-b569-16fcd384cab6` | 305-309 [crates/gwiki/src/ingest/session/codex.rs:305-309] | Indexed function `render_codex_content_block` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:305-309] |
| `append_call_id` | function | `fn append_call_id(content: &mut String, call_id: Option<&str>) {` | `append_call_id [function]` | `3ba443d6-6091-5952-96b3-723bd726b56d` | 311-316 [crates/gwiki/src/ingest/session/codex.rs:311-316] | Indexed function `append_call_id` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:311-316] |
| `append_value_body` | function | `fn append_value_body(content: &mut String, value: Option<&Value>) -> Option<()> {` | `append_value_body [function]` | `2960b4c5-d8cb-579d-a0d5-3c1e3a8e8777` | 318-323 [crates/gwiki/src/ingest/session/codex.rs:318-323] | Indexed function `append_value_body` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:318-323] |
| `render_jsonish_or_text` | function | `fn render_jsonish_or_text(value: &Value) -> String {` | `render_jsonish_or_text [function]` | `00ca871e-5da9-5290-b8ea-0ab82ad3616d` | 325-330 [crates/gwiki/src/ingest/session/codex.rs:325-330] | Indexed function `render_jsonish_or_text` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:325-330] |
| `pretty_jsonish` | function | `fn pretty_jsonish(value: &Value) -> String {` | `pretty_jsonish [function]` | `699a26e8-d40d-58c5-9447-0fcc88a1d706` | 332-339 [crates/gwiki/src/ingest/session/codex.rs:332-339] | Indexed function `pretty_jsonish` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:332-339] |
| `codex_adapter_parses_messages_and_tool_items` | function | `fn codex_adapter_parses_messages_and_tool_items() {` | `codex_adapter_parses_messages_and_tool_items [function]` | `427bc068-717b-5226-9eed-da1dc20e147f` | 352-471 [crates/gwiki/src/ingest/session/codex.rs:352-471] | Indexed function `codex_adapter_parses_messages_and_tool_items` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:352-471] |
| `codex_adapter_parses_real_archive_when_fixture_is_set` | function | `fn codex_adapter_parses_real_archive_when_fixture_is_set() {` | `codex_adapter_parses_real_archive_when_fixture_is_set [function]` | `3d667516-0cbc-5f9c-9846-71689c5f099d` | 474-541 [crates/gwiki/src/ingest/session/codex.rs:474-541] | Indexed function `codex_adapter_parses_real_archive_when_fixture_is_set` in `crates/gwiki/src/ingest/session/codex.rs`. [crates/gwiki/src/ingest/session/codex.rs:474-541] |
