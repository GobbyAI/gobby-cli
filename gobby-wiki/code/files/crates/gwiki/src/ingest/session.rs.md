---
title: crates/gwiki/src/ingest/session.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/session.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/session.rs` exposes 45 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/session.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SessionFileSnapshot` | class | Indexed class `SessionFileSnapshot` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:34-40] |
| `ParsedSession` | class | Indexed class `ParsedSession` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:43-49] |
| `ParsedSessionMessage` | class | Indexed class `ParsedSessionMessage` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:52-57] |
| `SessionArchiveEnvelope` | class | Indexed class `SessionArchiveEnvelope` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:60-65] |
| `SessionTranscriptAdapter` | type | Indexed type `SessionTranscriptAdapter` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:67-77] |
| `SessionTranscriptAdapter.supports_archive` | method | Indexed method `SessionTranscriptAdapter.supports_archive` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:70-74] |
| `ingest_session_file_without_index` | function | Indexed function `ingest_session_file_without_index` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:79-114] |
| `parse_session_archive` | function | Indexed function `parse_session_archive` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:116-137] |
| `read_session_archive` | function | Indexed function `read_session_archive` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:139-166] |
| `normalize_session_archive_value` | function | Indexed function `normalize_session_archive_value` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:168-196] |
| `default_session_adapters` | function | Indexed function `default_session_adapters` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:198-208] |
| `CommonSessionAdapter` | class | Indexed class `CommonSessionAdapter` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:213] |
| `CommonSessionAdapter::supports` | method | Indexed method `CommonSessionAdapter::supports` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:216-221] |
| `CommonSessionAdapter::parse` | method | Indexed method `CommonSessionAdapter::parse` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:223-271] |
| `CommonSessionPayload` | class | Indexed class `CommonSessionPayload` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:275-281] |
| `CommonSessionMessage` | class | Indexed class `CommonSessionMessage` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:284-288] |
| `parsed_common_message` | function | Indexed function `parsed_common_message` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:290-302] |
| `parsed_common_payload_message` | function | Indexed function `parsed_common_payload_message` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:304-315] |
| `ClaudeCodeAdapter` | class | Indexed class `ClaudeCodeAdapter` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:317] |
| `ClaudeCodeAdapter::supports` | method | Indexed method `ClaudeCodeAdapter::supports` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:320-333] |
| `ClaudeCodeAdapter::parse` | method | Indexed method `ClaudeCodeAdapter::parse` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:335-402] |
| `ClaudeCodeRecord` | class | Indexed class `ClaudeCodeRecord` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:407-417] |
| `ClaudeCodeMessage` | class | Indexed class `ClaudeCodeMessage` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:420-426] |
| `parsed_claude_code_message` | function | Indexed function `parsed_claude_code_message` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:428-445] |
| `claude_code_message_role` | function | Indexed function `claude_code_message_role` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:447-459] |
| `record_has_tool_result` | function | Indexed function `record_has_tool_result` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:461-471] |
| `claude_code_tool_names` | function | Indexed function `claude_code_tool_names` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:473-477] |
| `collect_claude_code_tool_names` | function | Indexed function `collect_claude_code_tool_names` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:479-498] |
| `render_claude_code_content` | function | Indexed function `render_claude_code_content` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:500-514] |
| `append_claude_code_content` | function | Indexed function `append_claude_code_content` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:516-537] |
| `render_claude_code_content_block` | function | Indexed function `render_claude_code_content_block` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:539-550] |
| `render_claude_code_tool_use` | function | Indexed function `render_claude_code_tool_use` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:552-561] |
| `render_claude_code_tool_result` | function | Indexed function `render_claude_code_tool_result` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:563-590] |
| `content_has_block_type` | function | Indexed function `content_has_block_type` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:592-605] |
| `pretty_json` | function | Indexed function `pretty_json` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:607-609] |
| `render_session_markdown` | function | Indexed function `render_session_markdown` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:611-673] |
| `message_heading` | function | Indexed function `message_heading` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:675-677] |
| `non_empty_optional` | function | Indexed function `non_empty_optional` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:679-681] |
| `non_empty_string` | function | Indexed function `non_empty_string` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:683-686] |
| `json_string_field` | function | Indexed function `json_string_field` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:688-693] |
| `render_session_markdown_emits_deterministic_session_frontmatter` | function | Indexed function `render_session_markdown_emits_deterministic_session_frontmatter` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:700-750] |
| `common_session_adapter_accepts_fixture_payload_messages` | function | Indexed function `common_session_adapter_accepts_fixture_payload_messages` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:753-779] |
| `read_session_archive_accepts_raw_claude_code_records` | function | Indexed function `read_session_archive_accepts_raw_claude_code_records` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:782-798] |
| `claude_code_adapter_parses_messages_tools_and_sidechains` | function | Indexed function `claude_code_adapter_parses_messages_tools_and_sidechains` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:801-904] |
| `claude_code_adapter_parses_real_archive_when_fixture_is_set` | function | Indexed function `claude_code_adapter_parses_real_archive_when_fixture_is_set` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:907-968] |

