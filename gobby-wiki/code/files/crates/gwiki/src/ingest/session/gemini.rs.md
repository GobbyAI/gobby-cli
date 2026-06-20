---
title: crates/gwiki/src/ingest/session/gemini.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/gemini.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/session/gemini.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/session/gemini.rs` exposes 15 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/session/gemini.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GeminiSessionAdapter` | class | The 'GeminiSessionAdapter' is a Rust unit struct with module-private visibility ('pub(super)') that serves as an adapter or interface for representing a Gemini session. [crates/gwiki/src/ingest/session/gemini.rs:12] |
| `GeminiSessionAdapter::supports` | method | The 'supports' method determines whether the provided 'envelope_type' string slice matches any of the supported types—"init", "message", "result", "tool_call", "tool_result", or "tool_error"—and returns a boolean indicating the result. [crates/gwiki/src/ingest/session/gemini.rs:15-20] |
| `GeminiSessionAdapter::parse` | method | The 'parse' method filters and deserializes a slice of 'SessionArchiveEnvelope' payloads into Gemini records to extract metadata and reconstruct an aggregated sequence of parsed messages, tool calls, and tool results, returning a 'ParsedSession' or a 'WikiError' if no valid messages are processed. [crates/gwiki/src/ingest/session/gemini.rs:22-83] |
| `GeminiRecord` | class | 'GeminiRecord' is a Rust struct that represents a serialized event or interaction record containing optional metadata for chat messages, model parameters, tool executions, and their corresponding inputs, outputs, or errors. [crates/gwiki/src/ingest/session/gemini.rs:87-102] |
| `parsed_gemini_message` | function | This function attempts to parse a 'GeminiRecord' and an optional fallback timestamp into a 'ParsedSessionMessage' containing a cloned role, rendered content, resolved timestamp, and an empty list of tool names, returning 'None' if either the record's role is empty or its content cannot be rendered. [crates/gwiki/src/ingest/session/gemini.rs:104-119] |
| `parsed_gemini_tool_call` | function | The 'parsed_gemini_tool_call' function transforms a 'GeminiRecord' and an optional fallback timestamp into a 'ParsedSessionMessage' with a "tool call" role, formatting the tool's name, call ID, and pretty-printed JSON arguments into its content string. [crates/gwiki/src/ingest/session/gemini.rs:121-147] |
| `parsed_gemini_tool_result` | function | The 'parsed_gemini_tool_result' function parses a 'GeminiRecord' and an optional fallback timestamp into a 'ParsedSessionMessage' by formatting the record's output, result, content, or error payload into a structured text representation with its associated tool call ID and labeling it with a 'tool result' role. [crates/gwiki/src/ingest/session/gemini.rs:149-175] |
| `push_gemini_message` | function | This function appends a 'ParsedSessionMessage' to a vector, either by merging its content and timestamp into the last message if 'is_delta' is true and the roles match, or by pushing it as a new element. [crates/gwiki/src/ingest/session/gemini.rs:177-192] |
| `render_gemini_content` | function | The 'render_gemini_content' function extracts text segments from a structured 'Value' reference into a vector and returns an 'Option<String>' containing the segments joined by double newlines, or 'None' if the resulting string is empty. [crates/gwiki/src/ingest/session/gemini.rs:194-198] |
| `append_gemini_content` | function | The 'append_gemini_content' function processes a JSON-like 'Value' reference to extract and append non-empty text strings, array items, or object representations as rendered content blocks to a mutable vector of strings. [crates/gwiki/src/ingest/session/gemini.rs:200-221] |
| `render_gemini_content_block` | function | The 'render_gemini_content_block' function extracts and returns a string from either the '"text"' or '"content"' field of a JSON block, falling back to a pretty-printed JSON representation of the entire block if neither field is present. [crates/gwiki/src/ingest/session/gemini.rs:223-227] |
| `append_call_id` | function | The 'append_call_id' function appends a colon, a space, and the provided 'call_id' to a mutable 'String' if the 'call_id' is a non-empty string slice. [crates/gwiki/src/ingest/session/gemini.rs:229-234] |
| `render_jsonish_or_text` | function | This function returns the underlying string if the provided JSON value is a string, and otherwise formats the value as a pretty-printed JSON representation enclosed within a triple-single-quoted markdown code block. [crates/gwiki/src/ingest/session/gemini.rs:236-241] |

_Verified by 2 in-file unit tests._

