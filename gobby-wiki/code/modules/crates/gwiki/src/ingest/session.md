---
title: crates/gwiki/src/ingest/session
type: code_module
provenance:
- file: crates/gwiki/src/ingest/session/codex.rs
- file: crates/gwiki/src/ingest/session/derived.rs
- file: crates/gwiki/src/ingest/session/droid.rs
- file: crates/gwiki/src/ingest/session/gemini.rs
- file: crates/gwiki/src/ingest/session/grok.rs
- file: crates/gwiki/src/ingest/session/metadata.rs
- file: crates/gwiki/src/ingest/session/qwen.rs
- file: crates/gwiki/src/ingest/session/redaction.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/session

Parent: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Overview

The session ingest module normalizes archived assistant-session records into shared `ParsedSession` structures. Its adapters import the common session contract and helpers from the parent module, including `ParsedSession`, `ParsedSessionMessage`, `ParsedSessionMetadata`, `SessionArchiveEnvelope`, `SessionTranscriptAdapter`, JSON/string helpers, and `pretty_json`, while surfacing failures through `crate::WikiError` (`crates/gwiki/src/ingest/session/codex.rs:1-9`, `crates/gwiki/src/ingest/session/droid.rs:1-9`).

Each provider adapter declares which envelope types it understands, filters archives to those records, deserializes payloads with `serde_json::from_value`, extracts timestamps/metadata, and emits visible messages. Codex handles `event_msg`, `response_item`, `session_meta`, and `turn_context`, using metadata records to set model and git branch (`crates/gwiki/src/ingest/session/codex.rs:11-100`). Droid identifies archives by `session_start`, accepts `message` and `session_start`, derives a title from session metadata, and rejects archives without visible messages (`crates/gwiki/src/ingest/session/droid.rs:11-100`).

Grok and Qwen follow the same adapter contract but add provider-specific archive detection and metadata extraction. Grok recognizes chat, thought, tool, error, and terminal records, can detect Grok archives from `model_id` or tool-call fields, and appends parsed chat messages into the session stream (`crates/gwiki/src/ingest/session/grok.rs:11-100`). Qwen recognizes assistant/system/tool/user records, detects archives with `is_qwen_record`, records model and git branch, and requires at least one visible message (`crates/gwiki/src/ingest/session/qwen.rs:11-100`). Supporting files round out the module with derived fields, metadata handling, and redaction.

| File | Indexed API symbols |
| --- | ---: |
| `codex.rs` | 23 |
| `derived.rs` | 4 |
| `droid.rs` | 23 |
| `gemini.rs` | 15 |
| `grok.rs` | 20 |
| `metadata.rs` | 13 |
| `qwen.rs` | 20 |
| `redaction.rs` | 8 |

| Adapter | Archive/envelope signals |
| --- | --- |
| Codex | `event_msg`, `response_item`, `session_meta`, `turn_context` (`crates/gwiki/src/ingest/session/codex.rs:11-100`) |
| Droid | `message`, `session_start` (`crates/gwiki/src/ingest/session/droid.rs:11-100`) |
| Grok | `assistant`, `end`, `error`, `system`, `text`, `thought`, `tool_result`, `user`; also `tool_calls`, `tool_call_id`, or Grok `model_id` (`crates/gwiki/src/ingest/session/grok.rs:11-100`) |
| Qwen | `assistant`, `system`, `tool_result`, `user` (`crates/gwiki/src/ingest/session/qwen.rs:11-100`) |
[crates/gwiki/src/ingest/session/codex.rs:12]
[crates/gwiki/src/ingest/session/derived.rs:10-26]
[crates/gwiki/src/ingest/session/droid.rs:12]
[crates/gwiki/src/ingest/session/gemini.rs:12]
[crates/gwiki/src/ingest/session/grok.rs:12]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ingest/session/codex.rs\|crates/gwiki/src/ingest/session/codex.rs]] | `crates/gwiki/src/ingest/session/codex.rs` exposes 23 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session/derived.rs\|crates/gwiki/src/ingest/session/derived.rs]] | `crates/gwiki/src/ingest/session/derived.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session/droid.rs\|crates/gwiki/src/ingest/session/droid.rs]] | `crates/gwiki/src/ingest/session/droid.rs` exposes 23 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session/gemini.rs\|crates/gwiki/src/ingest/session/gemini.rs]] | `crates/gwiki/src/ingest/session/gemini.rs` exposes 15 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session/grok.rs\|crates/gwiki/src/ingest/session/grok.rs]] | `crates/gwiki/src/ingest/session/grok.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session/metadata.rs\|crates/gwiki/src/ingest/session/metadata.rs]] | `crates/gwiki/src/ingest/session/metadata.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session/qwen.rs\|crates/gwiki/src/ingest/session/qwen.rs]] | `crates/gwiki/src/ingest/session/qwen.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session/redaction.rs\|crates/gwiki/src/ingest/session/redaction.rs]] | `crates/gwiki/src/ingest/session/redaction.rs` exposes 8 indexed API symbols. |

