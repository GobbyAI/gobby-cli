---
title: crates/gwiki/src/ingest/session/codex.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/codex.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/session/codex.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/session/codex.rs` exposes 23 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/session/codex.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CodexSessionAdapter` | class | The 'CodexSessionAdapter' is a parent-module-visible ('pub(super)') Rust unit struct that acts as an adapter or marker for a Codex session. [crates/gwiki/src/ingest/session/codex.rs:12] |
| `CodexSessionAdapter::supports` | method | The 'supports' method returns a boolean indicating whether the provided 'envelope_type' string slice matches one of the supported types: "event_msg", "response_item", "session_meta", or "turn_context". [crates/gwiki/src/ingest/session/codex.rs:15-20] |
| `CodexSessionAdapter::parse` | method | The 'parse' method processes a slice of supported 'SessionArchiveEnvelope' payloads to extract and aggregate the session start timestamp, originator type, messages, and metadata (such as model and Git branch configuration) into a structured 'ParsedSession'. [crates/gwiki/src/ingest/session/codex.rs:22-96] |
| `CodexSessionMeta` | class | The 'CodexSessionMeta' struct represents session metadata, containing optional fields for the timestamp, originator, model identifier, and associated Git repository metadata. [crates/gwiki/src/ingest/session/codex.rs:100-105] |
| `CodexGitMetadata` | class | The 'CodexGitMetadata' struct represents Git-related metadata, containing a single field that stores an optional string representing a repository branch name. [crates/gwiki/src/ingest/session/codex.rs:108-110] |
| `CodexEventPayload` | class | The 'CodexEventPayload' struct represents a serialized event payload containing a required string-based event type mapped to the key 'type' and an optional string message. [crates/gwiki/src/ingest/session/codex.rs:113-117] |
| `CodexResponseItem` | class | 'CodexResponseItem' is a deserializable Rust structure representing an individual interaction or execution event from a language model, encapsulating its type along with optional fields for roles, execution phases, textual content, and tool-call lifecycle metadata like arguments, identifiers, and outputs. [crates/gwiki/src/ingest/session/codex.rs:120-131] |
| `parsed_codex_event_message` | function | This function deserializes the payload of a 'SessionArchiveEnvelope' into a 'CodexEventPayload' and, if the event type is '"user_message"', maps its non-empty message content and timestamp into a 'ParsedSessionMessage' struct with a user role. [crates/gwiki/src/ingest/session/codex.rs:133-156] |
| `parsed_codex_response_item` | function | This function deserializes a 'SessionArchiveEnvelope' payload into a 'CodexResponseItem' using serde_json, and routes it based on its type string to parse and return an optional 'ParsedSessionMessage' or a JSON deserialization 'WikiError'. [crates/gwiki/src/ingest/session/codex.rs:158-180] |
| `parsed_codex_response_message` | function | The 'parsed_codex_response_message' function converts a 'CodexResponseItem' and an optional timestamp into a 'ParsedSessionMessage', returning 'None' if the item is not from an assistant or lacks renderable content, and appends any execution phase metadata to the formatted role string. [crates/gwiki/src/ingest/session/codex.rs:182-204] |
| `parsed_codex_function_call` | function | The 'parsed_codex_function_call' function parses a 'CodexResponseItem' and an optional timestamp into a 'ParsedSessionMessage' with the role of "tool call," formatting the function's name, call ID, and serialized JSON-like arguments into its structured content payload. [crates/gwiki/src/ingest/session/codex.rs:206-226] |
| `parsed_codex_function_output` | function | This function parses a 'CodexResponseItem' and an optional timestamp into a 'ParsedSessionMessage' with the role "tool result" by constructing a string containing the item's call ID and output body, returning 'None' if the output body cannot be successfully appended. [crates/gwiki/src/ingest/session/codex.rs:228-242] |
| `parsed_codex_tool_search_call` | function | The function 'parsed_codex_tool_search_call' parses a 'CodexResponseItem' and an optional timestamp into a 'ParsedSessionMessage' representing a 'tool_search' tool call, incorporating the formatted call ID and arguments into the message content. [crates/gwiki/src/ingest/session/codex.rs:244-258] |
| `parsed_codex_tool_search_output` | function | The function 'parsed_codex_tool_search_output' parses a 'CodexResponseItem' and an optional timestamp into a 'ParsedSessionMessage' with a "tool result" role by appending the item's call ID and tool body content, returning 'None' if the tool body is missing. [crates/gwiki/src/ingest/session/codex.rs:260-274] |
| `render_codex_content` | function | The 'render_codex_content' function processes a structured 'Value' reference to collect its content parts, joins them with double newlines, and returns the aggregated text as a 'Some(String)' if it is non-empty, or 'None' otherwise. [crates/gwiki/src/ingest/session/codex.rs:276-280] |
| `append_codex_content` | function | The 'append_codex_content' function mutates a vector of strings by appending a direct non-empty string value or rendering and appending content blocks from JSON arrays and objects using 'render_codex_content_block'. [crates/gwiki/src/ingest/session/codex.rs:282-303] |
| `render_codex_content_block` | function | This function extracts and returns the string value of either the "text" or "content" field from a JSON block, falling back to a pretty-printed JSON representation of the block if neither field exists. [crates/gwiki/src/ingest/session/codex.rs:305-309] |
| `append_call_id` | function | The function 'append_call_id' mutably appends a colon delimiter followed by the 'call_id' string slice to the end of the 'content' buffer, provided the optional 'call_id' is present and non-empty. [crates/gwiki/src/ingest/session/codex.rs:311-316] |
| `append_value_body` | function | Appends two newlines and the rendered string representation of a non-null 'Value' to a mutable 'String' buffer if the provided 'Option<&Value>' is present and non-null, returning 'Some(())', or returns 'None' otherwise. [crates/gwiki/src/ingest/session/codex.rs:318-323] |
| `render_jsonish_or_text` | function | The function returns the raw string representation of the input 'Value' if it is a string, and otherwise serializes it into a pretty-printed JSON format enclosed within triple-single-quote markdown code block delimiters. [crates/gwiki/src/ingest/session/codex.rs:325-330] |
| `pretty_jsonish` | function | The 'pretty_jsonish' function converts a JSON 'Value' into a pretty-printed string by attempting to parse and format its content if it is a string variant representing valid JSON, and otherwise falling back to either the unparseable string or a pretty-printed representation of the original value. [crates/gwiki/src/ingest/session/codex.rs:332-339] |

_Verified by 2 in-file unit tests._

