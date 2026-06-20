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

_16 more symbol(s) not shown — run `gcode outline crates/gwiki/src/ingest/session.rs` for the full list._

_Verified by 5 in-file unit tests._

