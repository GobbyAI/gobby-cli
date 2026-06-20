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

`crates/gwiki/src/ingest/session/qwen.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `QwenSessionAdapter` | class | The 'QwenSessionAdapter' is a unit struct with parent-module visibility ('pub(super)') that serves as an adapter for managing session-specific operations and interactions for Qwen models. [crates/gwiki/src/ingest/session/qwen.rs:12] |
| `QwenSessionAdapter::supports` | method | The 'supports' method determines whether a given 'envelope_type' string slice matches any of the supported types: "assistant", "system", "tool_result", or "user". [crates/gwiki/src/ingest/session/qwen.rs:15-20] |
| `QwenSessionAdapter::supports_archive` | method | The 'supports_archive' method checks if a slice of 'SessionArchiveEnvelope' contains at least one envelope that is classified as a Qwen record by the 'is_qwen_record' function. [crates/gwiki/src/ingest/session/qwen.rs:22-24] |
| `QwenSessionAdapter::parse` | method | This method parses a slice of 'SessionArchiveEnvelope's by filtering for supported envelope types, deserializing their JSON payloads into 'QwenRecord' structures, extracting session-wide metadata, converting valid record types into a chronological sequence of messages, and returning a populated 'ParsedSession' or a 'WikiError' if JSON deserialization fails or if no messages are successfully parsed. [crates/gwiki/src/ingest/session/qwen.rs:26-77] |
| `QwenRecord` | class | 'QwenRecord' is a Serde-deserializable Rust struct representing a record that contains optional metadata fields—specifically record type, timestamp, model, and Git branch—along with an optional nested 'QwenMessage'. [crates/gwiki/src/ingest/session/qwen.rs:81-89] |
| `QwenMessage` | class | The 'QwenMessage' struct represents a chat message consisting of an optional string defining the sender's 'role' and a deserializable vector of generic 'Value' elements representing the message's 'parts', which defaults to an empty vector if omitted. [crates/gwiki/src/ingest/session/qwen.rs:92-96] |
| `qwen_record_type` | function | The function 'qwen_record_type' extracts and returns the string slice representing the record type from the 'SessionArchiveEnvelope''s payload under the key "type", falling back to the envelope's own 'envelope_type' field if the key is absent or not a valid string. [crates/gwiki/src/ingest/session/qwen.rs:98-104] |
| `is_qwen_record` | function | The 'is_qwen_record' function determines if a 'SessionArchiveEnvelope' is a valid Qwen record by verifying that its record type matches one of the specified variants ("assistant", "system", "tool_result", or "user") and that its payload contains required metadata fields ('sessionId', 'uuid', 'parentUuid', 'cwd', 'version') along with at least one message content, system payload, or tool call result field. [crates/gwiki/src/ingest/session/qwen.rs:106-126] |
| `parsed_qwen_message` | function | The 'parsed_qwen_message' function parses a 'QwenRecord' into an optional 'ParsedSessionMessage' by resolving its role, extracting its tool names, rendering its content parts, and determining its timestamp with a fallback option. [crates/gwiki/src/ingest/session/qwen.rs:128-145] |
| `qwen_message_role` | function | The 'qwen_message_role' function determines a message's normalized role string, classifying it as '"tool result"' if the record type is '"tool_result"' or a function response is detected, mapping a message role of '"model"' to '"assistant"', and otherwise falling back to the message's defined role or a default derived from the 'record_type'. [crates/gwiki/src/ingest/session/qwen.rs:147-159] |
| `render_qwen_parts` | function | The function 'render_qwen_parts' iterates over a slice of 'Value' elements, renders each valid part via 'render_qwen_part', joins the successfully rendered parts with double newlines, and returns the resulting string wrapped in 'Some' if it is non-empty, or 'None' otherwise. [crates/gwiki/src/ingest/session/qwen.rs:161-169] |
| `render_qwen_part` | function | The 'render_qwen_part' function processes a JSON value representing a message part, returning 'None' if the part is flagged as a thought, or otherwise rendering it into an optional string by extracting its text, delegation-rendering its function call or response, or formatting it as a pretty-printed JSON code block. [crates/gwiki/src/ingest/session/qwen.rs:171-196] |
| `render_qwen_function_call` | function | This function formats a JSON-value representation of a function call into a structured string containing the tool name, an optional identifier, and pretty-printed arguments enclosed in a code block. [crates/gwiki/src/ingest/session/qwen.rs:198-211] |
| `render_qwen_function_response` | function | The 'render_qwen_function_response' function formats a JSON 'Value' representing a tool execution response by concatenating its optional name, ID, and rendered response payload into a structured string wrapped in 'Some'. [crates/gwiki/src/ingest/session/qwen.rs:213-228] |
| `qwen_tool_names` | function | The 'qwen_tool_names' function iterates over a slice of JSON values to extract and collect the 'name' string fields from any nested 'functionCall' objects into a vector of strings. [crates/gwiki/src/ingest/session/qwen.rs:230-236] |
| `render_jsonish_or_text` | function | This function returns the underlying string representation if the given 'Value' is a string, and otherwise returns the pretty-printed JSON representation of the value enclosed in a markdown-formatted JSON code block. [crates/gwiki/src/ingest/session/qwen.rs:238-243] |
| `qwen_part_has_function_response` | function | The function 'qwen_part_has_function_response' determines whether a given 'Value' reference contains the key '"functionResponse"', returning 'true' if the key exists and 'false' otherwise. [crates/gwiki/src/ingest/session/qwen.rs:245-247] |

_Verified by 3 in-file unit tests._

