---
title: crates/gwiki/src/ingest/session/qwen.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/qwen.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/session/qwen.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/session/qwen.rs` exposes 20 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/session/qwen.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `QwenSessionAdapter` | class | Indexed class `QwenSessionAdapter` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:12] |
| `QwenSessionAdapter::supports` | method | Indexed method `QwenSessionAdapter::supports` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:15-20] |
| `QwenSessionAdapter::supports_archive` | method | Indexed method `QwenSessionAdapter::supports_archive` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:22-24] |
| `QwenSessionAdapter::parse` | method | Indexed method `QwenSessionAdapter::parse` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:26-77] |
| `QwenRecord` | class | Indexed class `QwenRecord` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:81-89] |
| `QwenMessage` | class | Indexed class `QwenMessage` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:92-96] |
| `qwen_record_type` | function | Indexed function `qwen_record_type` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:98-104] |
| `is_qwen_record` | function | Indexed function `is_qwen_record` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:106-126] |
| `parsed_qwen_message` | function | Indexed function `parsed_qwen_message` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:128-145] |
| `qwen_message_role` | function | Indexed function `qwen_message_role` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:147-159] |
| `render_qwen_parts` | function | Indexed function `render_qwen_parts` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:161-169] |
| `render_qwen_part` | function | Indexed function `render_qwen_part` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:171-196] |
| `render_qwen_function_call` | function | Indexed function `render_qwen_function_call` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:198-211] |
| `render_qwen_function_response` | function | Indexed function `render_qwen_function_response` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:213-228] |
| `qwen_tool_names` | function | Indexed function `qwen_tool_names` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:230-236] |
| `render_jsonish_or_text` | function | Indexed function `render_jsonish_or_text` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:238-243] |
| `qwen_part_has_function_response` | function | Indexed function `qwen_part_has_function_response` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:245-247] |
| `qwen_adapter_parses_messages_tools_and_skips_thoughts` | function | Indexed function `qwen_adapter_parses_messages_tools_and_skips_thoughts` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:257-382] |
| `qwen_adapter_accepts_envelope_wrapped_payload_records` | function | Indexed function `qwen_adapter_accepts_envelope_wrapped_payload_records` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:385-407] |
| `qwen_adapter_parses_real_archive_when_fixture_is_set` | function | Indexed function `qwen_adapter_parses_real_archive_when_fixture_is_set` in `crates/gwiki/src/ingest/session/qwen.rs`. [crates/gwiki/src/ingest/session/qwen.rs:410-430] |

