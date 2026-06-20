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

`crates/gwiki/src/ingest/session/grok.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GrokSessionAdapter` | class | The 'GrokSessionAdapter' is a Rust unit struct with parent-module visibility ('pub(super)') that serves as an adapter for representing or managing Grok session interactions. [crates/gwiki/src/ingest/session/grok.rs:12] |
| `GrokSessionAdapter::supports` | method | The 'supports' method determines whether a given 'envelope_type' string slice matches one of the supported values: "assistant", "end", "error", "system", "text", "thought", "tool_result", or "user". [crates/gwiki/src/ingest/session/grok.rs:15-20] |
| `GrokSessionAdapter::supports_archive` | method | This method determines if a slice of session archive envelopes is supported by checking if any envelope has an envelope type of "end" or "text", or if any envelope contains "tool_calls", "tool_call_id", or a "model_id" field containing "grok" in its payload. [crates/gwiki/src/ingest/session/grok.rs:22-32] |
| `GrokSessionAdapter::parse` | method | The 'parse' method processes a slice of session archive envelopes by filtering for supported types, deserializing their payloads into Grok records, extracting metadata, and reconstructing a structured sequence of session messages from user, assistant, tool, and stream records. [crates/gwiki/src/ingest/session/grok.rs:34-104] |
| `GrokRecord` | class | The 'GrokRecord' struct is a Rust data structure designed to deserialize and represent structured logs or interaction records, containing a mandatory record type alongside optional fields for timestamps, model identification, content, messages, and tool call execution details. [crates/gwiki/src/ingest/session/grok.rs:108-118] |
| `GrokToolCall` | class | The 'GrokToolCall' struct represents a tool invocation call, containing optional fields for a unique identifier, the name of the tool to be called, and its corresponding arguments. [crates/gwiki/src/ingest/session/grok.rs:121-125] |
| `parsed_grok_chat_message` | function | This function converts a 'GrokRecord' into a 'ParsedSessionMessage' by rendering its content, cloning its record type as the message role, resolving its timestamp with an optional fallback, and initializing an empty vector of tool names. [crates/gwiki/src/ingest/session/grok.rs:127-139] |
| `parsed_grok_stream_text` | function | The 'parsed_grok_stream_text' function processes a 'GrokRecord' and an optional fallback timestamp to return a 'ParsedSessionMessage' with an 'assistant' role and rendered content, falling back on the provided timestamp if the record's timestamp is missing, or returning 'None' if the source content cannot be rendered. [crates/gwiki/src/ingest/session/grok.rs:141-153] |
| `parsed_grok_tool_calls` | function | The 'parsed_grok_tool_calls' function transforms a list of tool calls from a 'GrokRecord' into a vector of 'ParsedSessionMessage' structs, formatting each tool's name, ID, and optional JSON-serialized arguments into the message content while resolving timestamps with a fallback. [crates/gwiki/src/ingest/session/grok.rs:155-188] |
| `parsed_grok_tool_result` | function | The 'parsed_grok_tool_result' function parses a 'GrokRecord' and an optional fallback timestamp into a 'ParsedSessionMessage' with a 'tool result' role by formatting the record's tool call ID, rendering its JSON or text content, and resolving its timestamp, returning 'None' if no content body is found. [crates/gwiki/src/ingest/session/grok.rs:190-212] |
| `parsed_grok_error` | function | The 'parsed_grok_error' function parses a 'GrokRecord' and an optional fallback timestamp into a 'ParsedSessionMessage' with an "error" role, extracting the message content from the record's available message, data, or content fields, and resolving the timestamp from either the record or the fallback. [crates/gwiki/src/ingest/session/grok.rs:214-232] |
| `push_or_append_message` | function | This function appends a 'ParsedSessionMessage''s content, timestamp, and tool names to the last message in the vector if 'append_to_previous' is true and their roles match, otherwise pushing the message as a new entry. [crates/gwiki/src/ingest/session/grok.rs:234-250] |
| `render_grok_content` | function | The 'render_grok_content' function processes a reference to a JSON 'Value' by appending its content parts to a vector using a helper function, joining those parts with double newlines, and returning the resulting string wrapped in an 'Option' if it is non-empty. [crates/gwiki/src/ingest/session/grok.rs:252-256] |
| `append_grok_content` | function | The 'append_grok_content' function inspects a JSON 'Value' and appends either its non-empty string content or its rendered block representations (for arrays and objects) to a mutable vector of strings. [crates/gwiki/src/ingest/session/grok.rs:258-279] |
| `render_grok_content_block` | function | This function extracts and returns the string value of either the "text" or "content" field from a JSON 'Value' block, falling back to a pretty-printed JSON representation of the entire block if neither field is present. [crates/gwiki/src/ingest/session/grok.rs:281-285] |
| `append_call_id` | function | The 'append_call_id' function appends a colon delimiter followed by the 'call_id' to the mutable 'content' string if the provided 'call_id' option is 'Some' and contains a non-empty string. [crates/gwiki/src/ingest/session/grok.rs:287-292] |
| `render_jsonish_or_text` | function | The 'render_jsonish_or_text' function returns the raw string value of a serialization 'Value' if it is a string variant, and otherwise returns its pretty-printed JSON representation wrapped in a triple-quote Markdown-like 'json' code block. [crates/gwiki/src/ingest/session/grok.rs:294-299] |

_Verified by 3 in-file unit tests._

