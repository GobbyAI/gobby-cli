---
title: crates/gwiki/src/ingest/session/droid.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/droid.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/session/droid.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/session/droid.rs` exposes 23 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/session/droid.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DroidSessionAdapter` | class | The 'DroidSessionAdapter' is a super-module-visible unit struct designed to adapt and interface droid session operations within its parent module scope. [crates/gwiki/src/ingest/session/droid.rs:12] |
| `DroidSessionAdapter::supports` | method | The 'supports' method checks whether the provided 'envelope_type' string slice matches either '"message"' or '"session_start"', returning 'true' if supported and 'false' otherwise. [crates/gwiki/src/ingest/session/droid.rs:15-17] |
| `DroidSessionAdapter::supports_archive` | method | The 'supports_archive' method returns 'true' if any 'SessionArchiveEnvelope' in the provided slice satisfies the 'is_droid_session_start' predicate, and 'false' otherwise. [crates/gwiki/src/ingest/session/droid.rs:19-21] |
| `DroidSessionAdapter::parse` | method | The 'parse' method processes a slice of 'SessionArchiveEnvelope' references by filtering and deserializing their payloads into 'DroidRecord' structures to extract the session title, start timestamp, and a collection of parsed messages, returning a 'ParsedSession' or a 'WikiError' if deserialization fails or no valid messages are present. [crates/gwiki/src/ingest/session/droid.rs:23-77] |
| `DroidRecord` | class | The 'DroidRecord' struct is a Rust data structure configured with Serde attributes to serialize and deserialize optional metadata fields—such as type, ID, timestamp, title, session title, and visibility—alongside an optional nested 'DroidMessage'. [crates/gwiki/src/ingest/session/droid.rs:81-91] |
| `DroidMessage` | class | The 'DroidMessage' struct is a data container representing a message payload with an optional string-based 'role' and an optional arbitrary 'content' value. [crates/gwiki/src/ingest/session/droid.rs:94-97] |
| `droid_record_type` | function | The 'droid_record_type' function retrieves the string value associated with the key '"type"' in a 'SessionArchiveEnvelope''s payload, falling back to the envelope's 'envelope_type' field if the key is absent or its value is not a string. [crates/gwiki/src/ingest/session/droid.rs:99-105] |
| `is_droid_session_start` | function | The function determines if a 'SessionArchiveEnvelope' represents a valid droid session start by verifying that its record type is '"session_start"' and that its payload contains either a '"version"' or '"hostId"' field along with at least one '"cwd"', '"sessionTitle"', or '"owner"' field. [crates/gwiki/src/ingest/session/droid.rs:107-114] |
| `parsed_droid_message` | function | The function 'parsed_droid_message' converts a 'DroidRecord' into a 'ParsedSessionMessage' by extracting the role, rendering the content, identifying tool names, and resolving a timestamp with a provided fallback, returning 'None' if the record is hidden or lacks necessary message content. [crates/gwiki/src/ingest/session/droid.rs:116-137] |
| `is_hidden_context_record` | function | The 'is_hidden_context_record' function returns 'true' if the 'DroidRecord' has an ID starting with '"context-"' or a visibility property of '"llm_only"', and 'false' otherwise. [crates/gwiki/src/ingest/session/droid.rs:139-148] |
| `droid_message_role` | function | The 'droid_message_role' function returns the string '"tool result"' if the message content contains a '"tool_result"' block type; otherwise, it returns the message's non-empty cloned role, defaulting to '"message"' if the role is empty or absent. [crates/gwiki/src/ingest/session/droid.rs:150-160] |
| `render_droid_content` | function | The 'render_droid_content' function processes a 'Value' reference by appending its content components into a vector, joining them with double newlines, and returning the resulting string wrapped in 'Some' if it is non-empty, or 'None' otherwise. [crates/gwiki/src/ingest/session/droid.rs:162-166] |
| `append_droid_content` | function | The 'append_droid_content' function processes a 'Value' enum to append its content to a mutable vector of strings, pushing non-empty string values directly or rendering array elements and object values via 'render_droid_content_block'. [crates/gwiki/src/ingest/session/droid.rs:168-189] |
| `render_droid_content_block` | function | The 'render_droid_content_block' function evaluates a JSON content block reference based on its '"type"' field, returning 'None' for thinking or reasoning blocks, delegating to specialized renderers for tool use and results, and falling back to extracting text/content or pretty-printing the JSON. [crates/gwiki/src/ingest/session/droid.rs:191-202] |
| `render_droid_tool_use` | function | The function extracts the tool name, optional ID, and non-null input parameters from a JSON value reference, formats them into a structured string containing the tool's identification and its pretty-printed JSON input block, and returns this formatted string wrapped in 'Option::Some'. [crates/gwiki/src/ingest/session/droid.rs:204-217] |
| `droid_tool_names` | function | The 'droid_tool_names' function extracts and returns a vector of tool name strings from a referenced 'Value' structure by delegating the traversal and collection to the helper function 'collect_droid_tool_names'. [crates/gwiki/src/ingest/session/droid.rs:219-223] |
| `collect_droid_tool_names` | function | This function recursively traverses a JSON 'Value' structure to identify objects of type '"tool_use"' and appends their corresponding '"name"' field values to a mutable vector of strings. [crates/gwiki/src/ingest/session/droid.rs:225-244] |
| `render_droid_tool_result` | function | The 'render_droid_tool_result' function parses a JSON block representing a tool execution result, formatting its success/error status and optional tool use ID alongside its rendered content into a single string wrapped in 'Some'. [crates/gwiki/src/ingest/session/droid.rs:246-277] |
| `render_jsonish_or_text` | function | The 'render_jsonish_or_text' function returns the raw string content of a JSON 'Value' if it is a string variant, and otherwise returns the pretty-printed JSON representation of the value formatted within a triple-single-quoted JSON code block. [crates/gwiki/src/ingest/session/droid.rs:279-284] |
| `content_has_block_type` | function | The 'content_has_block_type' function recursively traverses a JSON-like 'Value' to determine if any nested object, or item within nested arrays, has a '"type"' key with a string value matching 'expected_type'. [crates/gwiki/src/ingest/session/droid.rs:286-297] |

_Verified by 3 in-file unit tests._

