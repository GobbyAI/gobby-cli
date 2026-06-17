---
title: crates/gwiki/src/ingest/session.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session.rs
  ranges:
  - 34-40
  - 43-49
  - 52-57
  - 60-65
  - 67-77
  - 79-114
  - 116-137
  - 139-166
  - 168-196
  - 198-208
  - '213'
  - 216-221
  - 223-271
  - 275-281
  - 284-288
  - 290-302
  - 304-315
  - '317'
  - 320-333
  - 335-402
  - 407-417
  - 420-426
  - 428-445
  - 447-459
  - 461-471
  - 473-477
  - 479-498
  - 500-514
  - 516-537
  - 539-550
  - 552-561
  - 563-590
  - 592-605
  - 607-609
  - 611-673
  - 675-677
  - 679-681
  - 683-686
  - 688-693
  - 700-750
  - 753-779
  - 782-798
  - 801-904
  - 907-968
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/session.rs:34-40](crates/gwiki/src/ingest/session.rs#L34-L40), [crates/gwiki/src/ingest/session.rs:43-49](crates/gwiki/src/ingest/session.rs#L43-L49), [crates/gwiki/src/ingest/session.rs:52-57](crates/gwiki/src/ingest/session.rs#L52-L57), [crates/gwiki/src/ingest/session.rs:60-65](crates/gwiki/src/ingest/session.rs#L60-L65), [crates/gwiki/src/ingest/session.rs:67-77](crates/gwiki/src/ingest/session.rs#L67-L77), [crates/gwiki/src/ingest/session.rs:79-114](crates/gwiki/src/ingest/session.rs#L79-L114), [crates/gwiki/src/ingest/session.rs:116-137](crates/gwiki/src/ingest/session.rs#L116-L137), [crates/gwiki/src/ingest/session.rs:139-166](crates/gwiki/src/ingest/session.rs#L139-L166), [crates/gwiki/src/ingest/session.rs:168-196](crates/gwiki/src/ingest/session.rs#L168-L196), [crates/gwiki/src/ingest/session.rs:198-208](crates/gwiki/src/ingest/session.rs#L198-L208), [crates/gwiki/src/ingest/session.rs:213](crates/gwiki/src/ingest/session.rs#L213), [crates/gwiki/src/ingest/session.rs:216-221](crates/gwiki/src/ingest/session.rs#L216-L221), [crates/gwiki/src/ingest/session.rs:223-271](crates/gwiki/src/ingest/session.rs#L223-L271), [crates/gwiki/src/ingest/session.rs:275-281](crates/gwiki/src/ingest/session.rs#L275-L281), [crates/gwiki/src/ingest/session.rs:284-288](crates/gwiki/src/ingest/session.rs#L284-L288), [crates/gwiki/src/ingest/session.rs:290-302](crates/gwiki/src/ingest/session.rs#L290-L302), [crates/gwiki/src/ingest/session.rs:304-315](crates/gwiki/src/ingest/session.rs#L304-L315), [crates/gwiki/src/ingest/session.rs:317](crates/gwiki/src/ingest/session.rs#L317), [crates/gwiki/src/ingest/session.rs:320-333](crates/gwiki/src/ingest/session.rs#L320-L333), [crates/gwiki/src/ingest/session.rs:335-402](crates/gwiki/src/ingest/session.rs#L335-L402), [crates/gwiki/src/ingest/session.rs:407-417](crates/gwiki/src/ingest/session.rs#L407-L417), [crates/gwiki/src/ingest/session.rs:420-426](crates/gwiki/src/ingest/session.rs#L420-L426), [crates/gwiki/src/ingest/session.rs:428-445](crates/gwiki/src/ingest/session.rs#L428-L445), [crates/gwiki/src/ingest/session.rs:447-459](crates/gwiki/src/ingest/session.rs#L447-L459), [crates/gwiki/src/ingest/session.rs:461-471](crates/gwiki/src/ingest/session.rs#L461-L471), [crates/gwiki/src/ingest/session.rs:473-477](crates/gwiki/src/ingest/session.rs#L473-L477), [crates/gwiki/src/ingest/session.rs:479-498](crates/gwiki/src/ingest/session.rs#L479-L498), [crates/gwiki/src/ingest/session.rs:500-514](crates/gwiki/src/ingest/session.rs#L500-L514), [crates/gwiki/src/ingest/session.rs:516-537](crates/gwiki/src/ingest/session.rs#L516-L537), [crates/gwiki/src/ingest/session.rs:539-550](crates/gwiki/src/ingest/session.rs#L539-L550), [crates/gwiki/src/ingest/session.rs:552-561](crates/gwiki/src/ingest/session.rs#L552-L561), [crates/gwiki/src/ingest/session.rs:563-590](crates/gwiki/src/ingest/session.rs#L563-L590), [crates/gwiki/src/ingest/session.rs:592-605](crates/gwiki/src/ingest/session.rs#L592-L605), [crates/gwiki/src/ingest/session.rs:607-609](crates/gwiki/src/ingest/session.rs#L607-L609), [crates/gwiki/src/ingest/session.rs:611-673](crates/gwiki/src/ingest/session.rs#L611-L673), [crates/gwiki/src/ingest/session.rs:675-677](crates/gwiki/src/ingest/session.rs#L675-L677), [crates/gwiki/src/ingest/session.rs:679-681](crates/gwiki/src/ingest/session.rs#L679-L681), [crates/gwiki/src/ingest/session.rs:683-686](crates/gwiki/src/ingest/session.rs#L683-L686), [crates/gwiki/src/ingest/session.rs:688-693](crates/gwiki/src/ingest/session.rs#L688-L693), [crates/gwiki/src/ingest/session.rs:700-750](crates/gwiki/src/ingest/session.rs#L700-L750), [crates/gwiki/src/ingest/session.rs:753-779](crates/gwiki/src/ingest/session.rs#L753-L779), [crates/gwiki/src/ingest/session.rs:782-798](crates/gwiki/src/ingest/session.rs#L782-L798), [crates/gwiki/src/ingest/session.rs:801-904](crates/gwiki/src/ingest/session.rs#L801-L904), [crates/gwiki/src/ingest/session.rs:907-968](crates/gwiki/src/ingest/session.rs#L907-L968)

</details>

# crates/gwiki/src/ingest/session.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the session-ingest pipeline for turning archived chat/session files into normalized session data and markdown outputs. It introduces `SessionFileSnapshot` as the input bundle, `SessionArchiveEnvelope` plus `ParsedSession`/`ParsedSessionMessage` as the intermediate parsed model, and `SessionTranscriptAdapter` as the common interface for format-specific parsers. `ingest_session_file_without_index` reads an archive, selects the first adapter that supports its envelope types, and returns an ingest result. The rest of the file wires in adapter implementations and helpers for common sessions, Claude Code sessions, content/tool rendering, JSON/field normalization, and markdown/frontmatter generation, with tests covering deterministic rendering and real or fixture archive parsing.
[crates/gwiki/src/ingest/session.rs:34-40]
[crates/gwiki/src/ingest/session.rs:43-49]
[crates/gwiki/src/ingest/session.rs:52-57]
[crates/gwiki/src/ingest/session.rs:60-65]
[crates/gwiki/src/ingest/session.rs:67-77]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `SessionFileSnapshot` | class | `pub struct SessionFileSnapshot {` | `SessionFileSnapshot [class]` | `a27da086-8e3b-5a99-9aec-342a1c69ca2b` | 34-40 [crates/gwiki/src/ingest/session.rs:34-40] | Indexed class `SessionFileSnapshot` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:34-40] |
| `ParsedSession` | class | `pub(crate) struct ParsedSession {` | `ParsedSession [class]` | `e89a2110-bc67-50ac-ae12-0373cde9f14b` | 43-49 [crates/gwiki/src/ingest/session.rs:43-49] | Indexed class `ParsedSession` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:43-49] |
| `ParsedSessionMessage` | class | `pub(crate) struct ParsedSessionMessage {` | `ParsedSessionMessage [class]` | `00086616-52cb-5f3f-bb97-c6367fb84640` | 52-57 [crates/gwiki/src/ingest/session.rs:52-57] | Indexed class `ParsedSessionMessage` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:52-57] |
| `SessionArchiveEnvelope` | class | `pub(crate) struct SessionArchiveEnvelope {` | `SessionArchiveEnvelope [class]` | `71a42c37-fc2b-52cd-b68a-fd4537a160f1` | 60-65 [crates/gwiki/src/ingest/session.rs:60-65] | Indexed class `SessionArchiveEnvelope` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:60-65] |
| `SessionTranscriptAdapter` | type | `pub(crate) trait SessionTranscriptAdapter {` | `SessionTranscriptAdapter [type]` | `cd5f39ca-4dca-5836-9f0c-dadb07194887` | 67-77 [crates/gwiki/src/ingest/session.rs:67-77] | Indexed type `SessionTranscriptAdapter` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:67-77] |
| `SessionTranscriptAdapter.supports_archive` | method | `fn supports_archive(&self, envelopes: &[SessionArchiveEnvelope]) -> bool {` | `SessionTranscriptAdapter.supports_archive [method]` | `62ed3df3-e0ba-539b-82fa-1db2d5645667` | 70-74 [crates/gwiki/src/ingest/session.rs:70-74] | Indexed method `SessionTranscriptAdapter.supports_archive` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:70-74] |
| `ingest_session_file_without_index` | function | `pub(crate) fn ingest_session_file_without_index(` | `ingest_session_file_without_index [function]` | `a8b2e586-56af-5bcb-854f-196b286e4f36` | 79-114 [crates/gwiki/src/ingest/session.rs:79-114] | Indexed function `ingest_session_file_without_index` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:79-114] |
| `parse_session_archive` | function | `pub(crate) fn parse_session_archive(` | `parse_session_archive [function]` | `d7a406c9-beb3-5454-b047-23d05eb2bc8a` | 116-137 [crates/gwiki/src/ingest/session.rs:116-137] | Indexed function `parse_session_archive` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:116-137] |
| `read_session_archive` | function | `fn read_session_archive(` | `read_session_archive [function]` | `eb95db7f-6ed3-5971-88a7-900c6d145af3` | 139-166 [crates/gwiki/src/ingest/session.rs:139-166] | Indexed function `read_session_archive` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:139-166] |
| `normalize_session_archive_value` | function | `fn normalize_session_archive_value(value: Value) -> Result<SessionArchiveEnvelope, WikiError> {` | `normalize_session_archive_value [function]` | `892ebef9-7825-5e00-8245-c98d143231e2` | 168-196 [crates/gwiki/src/ingest/session.rs:168-196] | Indexed function `normalize_session_archive_value` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:168-196] |
| `default_session_adapters` | function | `fn default_session_adapters() -> [&'static dyn SessionTranscriptAdapter; 7] {` | `default_session_adapters [function]` | `79fe357b-5114-5256-8268-6ddb5a5f6f6c` | 198-208 [crates/gwiki/src/ingest/session.rs:198-208] | Indexed function `default_session_adapters` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:198-208] |
| `CommonSessionAdapter` | class | `struct CommonSessionAdapter;` | `CommonSessionAdapter [class]` | `a98c76f4-fb90-532d-8c08-a6c24b4e90dd` | 213-213 [crates/gwiki/src/ingest/session.rs:213] | Indexed class `CommonSessionAdapter` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:213] |
| `CommonSessionAdapter::supports` | method | `fn supports(&self, envelope_type: &str) -> bool {` | `CommonSessionAdapter::supports [method]` | `fb7b6a6e-9386-56aa-a36d-5ec3624ce345` | 216-221 [crates/gwiki/src/ingest/session.rs:216-221] | Indexed method `CommonSessionAdapter::supports` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:216-221] |
| `CommonSessionAdapter::parse` | method | `fn parse(&self, envelopes: &[SessionArchiveEnvelope]) -> Result<ParsedSession, WikiError> {` | `CommonSessionAdapter::parse [method]` | `4951b9b0-bdfa-50de-b473-3c4342719d47` | 223-271 [crates/gwiki/src/ingest/session.rs:223-271] | Indexed method `CommonSessionAdapter::parse` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:223-271] |
| `CommonSessionPayload` | class | `struct CommonSessionPayload {` | `CommonSessionPayload [class]` | `01dee8e9-d98a-52e3-9659-a133ac4d3b98` | 275-281 [crates/gwiki/src/ingest/session.rs:275-281] | Indexed class `CommonSessionPayload` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:275-281] |
| `CommonSessionMessage` | class | `struct CommonSessionMessage {` | `CommonSessionMessage [class]` | `9b490ba1-4c28-502d-a3a1-ffa1f7aff186` | 284-288 [crates/gwiki/src/ingest/session.rs:284-288] | Indexed class `CommonSessionMessage` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:284-288] |
| `parsed_common_message` | function | `fn parsed_common_message(` | `parsed_common_message [function]` | `e5fe8d63-e874-5661-bd2d-f2379860593d` | 290-302 [crates/gwiki/src/ingest/session.rs:290-302] | Indexed function `parsed_common_message` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:290-302] |
| `parsed_common_payload_message` | function | `fn parsed_common_payload_message(` | `parsed_common_payload_message [function]` | `23c9ac50-acbd-55b3-a5f3-6f78b473666d` | 304-315 [crates/gwiki/src/ingest/session.rs:304-315] | Indexed function `parsed_common_payload_message` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:304-315] |
| `ClaudeCodeAdapter` | class | `struct ClaudeCodeAdapter;` | `ClaudeCodeAdapter [class]` | `7ddd0d1d-084a-53b4-907f-215da135200d` | 317-317 [crates/gwiki/src/ingest/session.rs:317] | Indexed class `ClaudeCodeAdapter` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:317] |
| `ClaudeCodeAdapter::supports` | method | `fn supports(&self, envelope_type: &str) -> bool {` | `ClaudeCodeAdapter::supports [method]` | `e230c01c-ea44-564d-acdb-cbcfc90e9888` | 320-333 [crates/gwiki/src/ingest/session.rs:320-333] | Indexed method `ClaudeCodeAdapter::supports` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:320-333] |
| `ClaudeCodeAdapter::parse` | method | `fn parse(&self, envelopes: &[SessionArchiveEnvelope]) -> Result<ParsedSession, WikiError> {` | `ClaudeCodeAdapter::parse [method]` | `37d7d36b-0843-5658-b6ad-a113c50b606e` | 335-402 [crates/gwiki/src/ingest/session.rs:335-402] | Indexed method `ClaudeCodeAdapter::parse` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:335-402] |
| `ClaudeCodeRecord` | class | `struct ClaudeCodeRecord {` | `ClaudeCodeRecord [class]` | `3f6c85fb-46a6-5b44-8e4d-6dfbc83fae1c` | 407-417 [crates/gwiki/src/ingest/session.rs:407-417] | Indexed class `ClaudeCodeRecord` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:407-417] |
| `ClaudeCodeMessage` | class | `struct ClaudeCodeMessage {` | `ClaudeCodeMessage [class]` | `bfb59dd8-b912-5944-ae17-f6b5338f7d18` | 420-426 [crates/gwiki/src/ingest/session.rs:420-426] | Indexed class `ClaudeCodeMessage` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:420-426] |
| `parsed_claude_code_message` | function | `fn parsed_claude_code_message(` | `parsed_claude_code_message [function]` | `0b8a6b6b-5e55-5ec6-ac16-d3d6b5cb9348` | 428-445 [crates/gwiki/src/ingest/session.rs:428-445] | Indexed function `parsed_claude_code_message` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:428-445] |
| `claude_code_message_role` | function | `fn claude_code_message_role(record: &ClaudeCodeRecord, message: &ClaudeCodeMessage) -> String {` | `claude_code_message_role [function]` | `f49aa63b-536d-5791-ab3e-cd54fb573528` | 447-459 [crates/gwiki/src/ingest/session.rs:447-459] | Indexed function `claude_code_message_role` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:447-459] |
| `record_has_tool_result` | function | `fn record_has_tool_result(record: &ClaudeCodeRecord) -> bool {` | `record_has_tool_result [function]` | `fdf6d751-96e4-50b6-85d8-5dff8c3b24bc` | 461-471 [crates/gwiki/src/ingest/session.rs:461-471] | Indexed function `record_has_tool_result` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:461-471] |
| `claude_code_tool_names` | function | `fn claude_code_tool_names(content: &Value) -> Vec<String> {` | `claude_code_tool_names [function]` | `53989d0a-191d-5fda-9f9c-f9e43673d153` | 473-477 [crates/gwiki/src/ingest/session.rs:473-477] | Indexed function `claude_code_tool_names` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:473-477] |
| `collect_claude_code_tool_names` | function | `fn collect_claude_code_tool_names(value: &Value, names: &mut Vec<String>) {` | `collect_claude_code_tool_names [function]` | `513d0d73-3a6c-5451-80ae-7beadb4b709b` | 479-498 [crates/gwiki/src/ingest/session.rs:479-498] | Indexed function `collect_claude_code_tool_names` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:479-498] |
| `render_claude_code_content` | function | `fn render_claude_code_content(content: &Value, tool_use_result: Option<&Value>) -> Option<String> {` | `render_claude_code_content [function]` | `c0cf29a2-c6d8-5eac-803f-56bf685bb101` | 500-514 [crates/gwiki/src/ingest/session.rs:500-514] | Indexed function `render_claude_code_content` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:500-514] |
| `append_claude_code_content` | function | `fn append_claude_code_content(value: &Value, parts: &mut Vec<String>) {` | `append_claude_code_content [function]` | `cc87057b-c879-55b4-8541-ef9ddd2d28e5` | 516-537 [crates/gwiki/src/ingest/session.rs:516-537] | Indexed function `append_claude_code_content` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:516-537] |
| `render_claude_code_content_block` | function | `fn render_claude_code_content_block(block: &Value) -> Option<String> {` | `render_claude_code_content_block [function]` | `8357d650-eff9-5ed2-b935-7054ab4cb163` | 539-550 [crates/gwiki/src/ingest/session.rs:539-550] | Indexed function `render_claude_code_content_block` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:539-550] |
| `render_claude_code_tool_use` | function | `fn render_claude_code_tool_use(block: &Value) -> Option<String> {` | `render_claude_code_tool_use [function]` | `dc4710a9-5beb-57e9-bd42-c591bd493f2e` | 552-561 [crates/gwiki/src/ingest/session.rs:552-561] | Indexed function `render_claude_code_tool_use` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:552-561] |
| `render_claude_code_tool_result` | function | `fn render_claude_code_tool_result(block: &Value) -> Option<String> {` | `render_claude_code_tool_result [function]` | `f599f2bd-506c-5693-a664-7e0014a85e5d` | 563-590 [crates/gwiki/src/ingest/session.rs:563-590] | Indexed function `render_claude_code_tool_result` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:563-590] |
| `content_has_block_type` | function | `fn content_has_block_type(value: &Value, expected_type: &str) -> bool {` | `content_has_block_type [function]` | `28cafff2-84ca-5d41-aade-d347aeb97ef7` | 592-605 [crates/gwiki/src/ingest/session.rs:592-605] | Indexed function `content_has_block_type` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:592-605] |
| `pretty_json` | function | `fn pretty_json(value: &Value) -> String {` | `pretty_json [function]` | `c05a37cd-90c1-5624-acb7-52ed757371ff` | 607-609 [crates/gwiki/src/ingest/session.rs:607-609] | Indexed function `pretty_json` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:607-609] |
| `render_session_markdown` | function | `fn render_session_markdown(` | `render_session_markdown [function]` | `2b73d62e-3ee0-553c-af9c-67f427046e59` | 611-673 [crates/gwiki/src/ingest/session.rs:611-673] | Indexed function `render_session_markdown` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:611-673] |
| `message_heading` | function | `fn message_heading(role: &str) -> String {` | `message_heading [function]` | `e3fafd85-d55e-50dc-9f35-896d93196caa` | 675-677 [crates/gwiki/src/ingest/session.rs:675-677] | Indexed function `message_heading` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:675-677] |
| `non_empty_optional` | function | `fn non_empty_optional(value: Option<String>) -> Option<String> {` | `non_empty_optional [function]` | `726b7dfe-2eca-5581-bd65-dcf94d88a23f` | 679-681 [crates/gwiki/src/ingest/session.rs:679-681] | Indexed function `non_empty_optional` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:679-681] |
| `non_empty_string` | function | `fn non_empty_string(value: &str) -> Option<String> {` | `non_empty_string [function]` | `15a4aaae-c579-5feb-bd1c-df8ac42b4e36` | 683-686 [crates/gwiki/src/ingest/session.rs:683-686] | Indexed function `non_empty_string` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:683-686] |
| `json_string_field` | function | `fn json_string_field(value: &Value, field: &str) -> Option<String> {` | `json_string_field [function]` | `39f4b285-e8d4-52ae-9b5a-752d911428a9` | 688-693 [crates/gwiki/src/ingest/session.rs:688-693] | Indexed function `json_string_field` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:688-693] |
| `render_session_markdown_emits_deterministic_session_frontmatter` | function | `fn render_session_markdown_emits_deterministic_session_frontmatter() {` | `render_session_markdown_emits_deterministic_session_frontmatter [function]` | `34f07015-867f-5a16-aa7e-05457540313a` | 700-750 [crates/gwiki/src/ingest/session.rs:700-750] | Indexed function `render_session_markdown_emits_deterministic_session_frontmatter` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:700-750] |
| `common_session_adapter_accepts_fixture_payload_messages` | function | `fn common_session_adapter_accepts_fixture_payload_messages() {` | `common_session_adapter_accepts_fixture_payload_messages [function]` | `762c8e59-0b01-5d5e-8376-0c22a65d9342` | 753-779 [crates/gwiki/src/ingest/session.rs:753-779] | Indexed function `common_session_adapter_accepts_fixture_payload_messages` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:753-779] |
| `read_session_archive_accepts_raw_claude_code_records` | function | `fn read_session_archive_accepts_raw_claude_code_records() {` | `read_session_archive_accepts_raw_claude_code_records [function]` | `ac1fb838-581b-5e62-8903-6ed14c26c5bb` | 782-798 [crates/gwiki/src/ingest/session.rs:782-798] | Indexed function `read_session_archive_accepts_raw_claude_code_records` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:782-798] |
| `claude_code_adapter_parses_messages_tools_and_sidechains` | function | `fn claude_code_adapter_parses_messages_tools_and_sidechains() {` | `claude_code_adapter_parses_messages_tools_and_sidechains [function]` | `214478e0-5fc2-5e95-a9e6-3071462271ec` | 801-904 [crates/gwiki/src/ingest/session.rs:801-904] | Indexed function `claude_code_adapter_parses_messages_tools_and_sidechains` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:801-904] |
| `claude_code_adapter_parses_real_archive_when_fixture_is_set` | function | `fn claude_code_adapter_parses_real_archive_when_fixture_is_set() {` | `claude_code_adapter_parses_real_archive_when_fixture_is_set [function]` | `6e555617-74b1-54bd-bdf5-e9a59734b6cb` | 907-968 [crates/gwiki/src/ingest/session.rs:907-968] | Indexed function `claude_code_adapter_parses_real_archive_when_fixture_is_set` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:907-968] |
