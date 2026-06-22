---
title: crates/gwiki/src/ingest/session/metadata.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/metadata.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/session/metadata.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/session/metadata.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/session/metadata.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ParsedSessionMetadata` | class | The 'ParsedSessionMetadata' struct is a crate-private data structure that aggregates session metadata, containing optional model and Git branch identifiers, a map of token totals, and a boolean flag indicating whether the session belongs to a subagent. [crates/gwiki/src/ingest/session/metadata.rs:10-15] |
| `ParsedSessionMetadata::set_model_once` | method | The 'set_model_once' method conditionally updates the struct's 'model' field with a non-empty representation of the provided optional string slice if and only if the field is currently 'None'. [crates/gwiki/src/ingest/session/metadata.rs:18-22] |
| `ParsedSessionMetadata::set_git_branch_once` | method | The 'set_git_branch_once' method mutably updates the struct's 'git_branch' field with a non-empty representation of the provided 'Option<&str>' argument, but only if the field is currently 'None'. [crates/gwiki/src/ingest/session/metadata.rs:24-28] |
| `ParsedSessionMetadata::mark_subagent` | method | The 'mark_subagent' method mutably borrows the receiver to set its internal 'is_subagent' boolean flag to 'true'. [crates/gwiki/src/ingest/session/metadata.rs:30-32] |
| `ParsedSessionMetadata::add_token_usage` | method | The 'add_token_usage' method mutably updates the struct's 'token_totals' by aggregating the numeric fields from a given JSON 'Value' representation of token usage. [crates/gwiki/src/ingest/session/metadata.rs:34-36] |
| `ParsedSessionMetadata::set_token_totals` | method | This method parses numeric fields from a JSON representation of token usage into a 'BTreeMap' and, if the resulting map is non-empty, updates the struct's 'token_totals' field with it. [crates/gwiki/src/ingest/session/metadata.rs:38-44] |
| `session_metadata_fields` | function | The 'session_metadata_fields' function processes a 'ParsedSession' reference to construct and return a vector of static string keys and 'MetadataValue' pairs containing session properties such as model, tool invocation counts, token usage, elapsed duration, hour distribution, subagent designation, and active git branch. [crates/gwiki/src/ingest/session/metadata.rs:47-87] |
| `add_json_number_fields` | function | The function iterates over the key-value pairs of a JSON object and accumulates any numeric values convertible to 'u64' into a mutable 'BTreeMap<String, u64>', grouped by key. [crates/gwiki/src/ingest/session/metadata.rs:89-100] |
| `json_u64` | function | The 'json_u64' function extracts a 64-bit unsigned integer from a JSON 'Value' by first attempting to retrieve it directly as a 'u64', falling back to converting its 'i64' representation into a 'u64' if the value is non-negative. [crates/gwiki/src/ingest/session/metadata.rs:102-106] |
| `tool_counts` | function | This function aggregates and returns the frequencies of non-empty tool names used across all messages in a parsed session as a 'BTreeMap<String, u64>'. [crates/gwiki/src/ingest/session/metadata.rs:108-119] |
| `duration_seconds` | function | This function calculates the total duration in seconds between the earliest and latest successfully parsed message timestamps in a 'ParsedSession', returning 'None' if the session contains no valid timestamps. [crates/gwiki/src/ingest/session/metadata.rs:121-132] |
| `hour_buckets` | function | The 'hour_buckets' function aggregates the timestamps of messages within a 'ParsedSession' into hourly intervals, returning a 'BTreeMap' that maps chronological UTC hour strings formatted as '%Y-%m-%dT%H:00:00Z' to their respective message counts. [crates/gwiki/src/ingest/session/metadata.rs:134-146] |
| `parse_timestamp` | function | Parses an RFC 3339 formatted string slice, returning the corresponding UTC date and time as a 'DateTime<Utc>' wrapped in an 'Option'. [crates/gwiki/src/ingest/session/metadata.rs:148-152] |

