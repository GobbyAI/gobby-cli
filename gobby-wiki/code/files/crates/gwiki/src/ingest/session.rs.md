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

`crates/gwiki/src/ingest/session.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SessionFileSnapshot` | class | The 'SessionFileSnapshot' struct represents a snapshot of a file from a session, encapsulating its location, file name, fetch timestamp, filesystem path, and raw binary content. [crates/gwiki/src/ingest/session.rs:34-40] |
| `ParsedSession` | class | The 'ParsedSession' struct is a crate-private data structure that represents a parsed conversation or session, containing its title, type, optional start timestamp, metadata, and an ordered collection of messages. [crates/gwiki/src/ingest/session.rs:43-49] |
| `ParsedSessionMessage` | class | The 'ParsedSessionMessage' struct is a package-private ('pub(crate)') Rust data structure that represents a parsed session message, encapsulating public fields for the sender's role, an optional timestamp, the textual content, and a vector of associated tool names. [crates/gwiki/src/ingest/session.rs:52-57] |
| `SessionArchiveEnvelope` | class | The 'SessionArchiveEnvelope' is a crate-private Rust struct that encapsulates a serialized JSON payload, an optional timestamp, and an envelope type identifier for session archiving. [crates/gwiki/src/ingest/session.rs:60-65] |
| `SessionTranscriptAdapter` | type | Indexed type `SessionTranscriptAdapter` in `crates/gwiki/src/ingest/session.rs`. [crates/gwiki/src/ingest/session.rs:67-77] |
| `SessionTranscriptAdapter.supports_archive` | method | The 'supports_archive' method returns 'true' if the implementing type supports the envelope type of at least one 'SessionArchiveEnvelope' in the provided slice, evaluated via the 'supports' method. [crates/gwiki/src/ingest/session.rs:70-74] |
| `ingest_session_file_without_index` | function | This function processes a session file snapshot by parsing its archive, registering its metadata and payload as a borrowed draft in the vault's source manifest, rendering and redacting its contents as Markdown, and persisting the resulting raw and derived Markdown files to the file system. [crates/gwiki/src/ingest/session.rs:79-114] |
| `parse_session_archive` | function | This function identifies the first 'SessionTranscriptAdapter' that supports the provided slice of 'SessionArchiveEnvelope's and delegates the parsing to it, returning the resulting 'ParsedSession' or a 'WikiError' if no compatible adapter is found. [crates/gwiki/src/ingest/session.rs:116-137] |
| `read_session_archive` | function | The 'read_session_archive' function parses line-delimited JSON from a lossy UTF-8 decoded byte slice, normalizes each non-empty line into a 'SessionArchiveEnvelope', and returns a vector of these envelopes, returning a 'WikiError' if JSON deserialization fails or if the resulting vector is empty. [crates/gwiki/src/ingest/session.rs:139-166] |
| `normalize_session_archive_value` | function | This function parses and validates a JSON 'Value' into a 'SessionArchiveEnvelope' by ensuring it is an object with a required '"type"' field, optionally extracting a '"timestamp"', and assigning either the nested '"payload"' field or the original object itself as the envelope's payload. [crates/gwiki/src/ingest/session.rs:168-196] |
| `default_session_adapters` | function | The 'default_session_adapters' function returns a statically allocated array of seven references to implementations of the 'SessionTranscriptAdapter' trait. [crates/gwiki/src/ingest/session.rs:198-208] |
| `CommonSessionAdapter` | class | The 'CommonSessionAdapter' is a unit struct designed to serve as a standardized adapter for managing and coordinating common session operations. [crates/gwiki/src/ingest/session.rs:213] |
| `CommonSessionAdapter::supports` | method | This method returns 'true' if the provided 'envelope_type' string slice matches '"session"', '"gobby.session"', or '"gobby.session.v1"', and 'false' otherwise. [crates/gwiki/src/ingest/session.rs:216-221] |
| `CommonSessionAdapter::parse` | method | The 'parse' method filters a slice of 'SessionArchiveEnvelope's by supported types, deserializes their payloads to aggregate the session's title, timestamp, type, and messages, and returns a 'ParsedSession' or a 'WikiError' if the resulting message list is empty. [crates/gwiki/src/ingest/session.rs:223-271] |
| `CommonSessionPayload` | class | 'CommonSessionPayload' is a Rust structure containing optional title, role, and content string fields, along with a vector of 'CommonSessionMessage' elements that defaults to an empty collection during deserialization. [crates/gwiki/src/ingest/session.rs:275-281] |
| `CommonSessionMessage` | class | The 'CommonSessionMessage' struct represents a session message containing optional 'role' and 'timestamp' fields alongside a required 'content' string. [crates/gwiki/src/ingest/session.rs:284-288] |
| `parsed_common_message` | function | This function parses a 'CommonSessionMessage' into a 'ParsedSessionMessage' by validating that the content is non-empty, defaulting its role to '"speaker"', resolving its timestamp with an optional fallback value, and initializing an empty list of tool names. [crates/gwiki/src/ingest/session.rs:290-302] |
| `parsed_common_payload_message` | function | The 'parsed_common_payload_message' function converts a 'CommonSessionPayload' and an optional fallback timestamp into a 'ParsedSessionMessage' if the payload has non-empty content, defaulting the role to "speaker" if none is specified and initializing an empty vector for tool names. [crates/gwiki/src/ingest/session.rs:304-315] |
| `ClaudeCodeAdapter` | class | The 'ClaudeCodeAdapter' is a structure designed to serve as an adapter interface for integrating or interacting with Claude-related APIs or components. [crates/gwiki/src/ingest/session.rs:317] |
| `ClaudeCodeAdapter::supports` | method | The 'supports' method determines whether a given 'envelope_type' string slice is supported by returning 'true' if it matches one of several specified literal values—specifically 'ai-title', 'assistant', 'attachment', 'last-prompt', 'mode', 'permission-mode', 'queue-operation', 'system', or 'user'—and 'false' otherwise. [crates/gwiki/src/ingest/session.rs:320-333] |
| `ClaudeCodeAdapter::parse` | method | This method deserializes and aggregates supported 'SessionArchiveEnvelope' payloads into 'ClaudeCodeRecord' instances to extract and compile session metadata—including the title, start timestamp, git branch, subagent status, and unique message token usage—returning a 'ParsedSession' result or a 'WikiError'. [crates/gwiki/src/ingest/session.rs:335-402] |
| `ClaudeCodeRecord` | class | 'ClaudeCodeRecord' is a serialized record struct that stores a record type plus optional metadata and payload fields for timestamp, sidechain status, message content, tool-use results, AI-generated title, last prompt, and git branch. [crates/gwiki/src/ingest/session.rs:407-417] |
| `ClaudeCodeMessage` | class | The 'ClaudeCodeMessage' struct is a Rust data structure representing a message payload with optional fields for its identifier, associated model, sender role, content, and token usage details. [crates/gwiki/src/ingest/session.rs:420-426] |
| `parsed_claude_code_message` | function | The 'parsed_claude_code_message' function processes a 'ClaudeCodeRecord' and an optional fallback timestamp to construct and return a 'ParsedSessionMessage' containing the resolved message role, timestamp, rendered content integrating tool use results, and extracted tool names. [crates/gwiki/src/ingest/session.rs:428-445] |

_16 more symbol(s) not shown — run `gcode outline crates/gwiki/src/ingest/session.rs` for the full list._

_Verified by 5 in-file unit tests._

