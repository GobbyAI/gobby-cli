---
title: crates/gwiki/src/ingest/session/grok.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/grok.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/session/grok.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/session/grok.rs` exposes 20 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/session/grok.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GrokSessionAdapter` | class | Indexed class `GrokSessionAdapter` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:12] |
| `GrokSessionAdapter::supports` | method | Indexed method `GrokSessionAdapter::supports` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:15-20] |
| `GrokSessionAdapter::supports_archive` | method | Indexed method `GrokSessionAdapter::supports_archive` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:22-32] |
| `GrokSessionAdapter::parse` | method | Indexed method `GrokSessionAdapter::parse` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:34-104] |
| `GrokRecord` | class | Indexed class `GrokRecord` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:108-118] |
| `GrokToolCall` | class | Indexed class `GrokToolCall` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:121-125] |
| `parsed_grok_chat_message` | function | Indexed function `parsed_grok_chat_message` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:127-139] |
| `parsed_grok_stream_text` | function | Indexed function `parsed_grok_stream_text` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:141-153] |
| `parsed_grok_tool_calls` | function | Indexed function `parsed_grok_tool_calls` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:155-188] |
| `parsed_grok_tool_result` | function | Indexed function `parsed_grok_tool_result` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:190-212] |
| `parsed_grok_error` | function | Indexed function `parsed_grok_error` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:214-232] |
| `push_or_append_message` | function | Indexed function `push_or_append_message` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:234-250] |
| `render_grok_content` | function | Indexed function `render_grok_content` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:252-256] |
| `append_grok_content` | function | Indexed function `append_grok_content` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:258-279] |
| `render_grok_content_block` | function | Indexed function `render_grok_content_block` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:281-285] |
| `append_call_id` | function | Indexed function `append_call_id` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:287-292] |
| `render_jsonish_or_text` | function | Indexed function `render_jsonish_or_text` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:294-299] |
| `grok_adapter_parses_local_chat_history_messages_and_tools` | function | Indexed function `grok_adapter_parses_local_chat_history_messages_and_tools` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:309-376] |
| `grok_adapter_parses_streaming_json_text_chunks` | function | Indexed function `grok_adapter_parses_streaming_json_text_chunks` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:379-408] |
| `grok_adapter_parses_real_archive_when_fixture_is_set` | function | Indexed function `grok_adapter_parses_real_archive_when_fixture_is_set` in `crates/gwiki/src/ingest/session/grok.rs`. [crates/gwiki/src/ingest/session/grok.rs:411-430] |

