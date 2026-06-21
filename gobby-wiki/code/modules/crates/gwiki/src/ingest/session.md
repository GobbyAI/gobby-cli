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

## crates/gwiki/src/ingest/session

This module is the multi-provider transcript ingestion layer for gwiki. It defines the `SessionTranscriptAdapter` trait and a family of concrete adapters — one per supported AI system — that each take a slice of raw `SessionArchiveEnvelope` records and produce a normalised `ParsedSession` containing `ParsedSessionMessage` items and `ParsedSessionMetadata`. Supporting files handle shared concerns: `metadata.rs` manages model and git-branch state that accumulates across envelope types, `redaction.rs` provides post-parse sanitisation, and `derived.rs` computes secondary fields from the normalised output.

Each adapter is exposed as a module-level static singleton and implements two discrimination methods before parsing begins. `supports(&str)` declares which `envelope_type` string values the adapter recognises. `supports_archive(&[SessionArchiveEnvelope])` performs a deeper heuristic scan of the full envelope list to break ties when multiple adapters share envelope-type names — for example, `GrokSessionAdapter` inspects payload fields such as `tool_calls`, `tool_call_id`, and `model_id` for the substring `"grok"` (grok.rs:26-34), while `DroidSessionAdapter` checks for a `session_start` record with Droid-specific shape (droid.rs:18-20) and `QwenSessionAdapter` uses an `is_qwen_record` predicate (qwen.rs:23-25). The `parse` method on each adapter iterates only the envelopes it recognises, deserialises each payload into a provider-specific record struct (`DroidRecord`, `GrokRecord`, `QwenRecord`, `CodexSessionMeta`, etc.), and populates the shared `ParsedSessionMetadata` builder — calling `set_model_once` and `set_git_branch_once` so that the first credible value wins — before pushing `ParsedSessionMessage` entries.

All adapters share a set of helper utilities imported from the parent `super` scope: `json_string_field`, `non_empty_optional`, `non_empty_string`, and `pretty_json` (codex.rs:6, droid.rs:6, grok.rs:6, qwen.rs:6). Errors propagate as `WikiError::Json` with a human-readable `action` string, or as `WikiError::InvalidInput` when a parsed archive yields zero visible messages (droid.rs:59-64, qwen.rs:56-60). The module is consumed by the wider `ingest` layer, which selects the appropriate adapter, drives the parse call, and forwards the resulting `ParsedSession` into downstream wiki-page generation.

### Provider Adapters

| Static Singleton | Struct | File | Recognised `envelope_type` values |
|---|---|---|---|
| `CODEX_SESSION_ADAPTER` | `CodexSessionAdapter` | codex.rs:10 | `event_msg`, `response_item`, `session_meta`, `turn_context` |
| `DROID_SESSION_ADAPTER` | `DroidSessionAdapter` | droid.rs:10 | `message`, `session_start` |
| `GROK_SESSION_ADAPTER` | `GrokSessionAdapter` | grok.rs:10 | `assistant`, `end`, `error`, `system`, `text`, `thought`, `tool_result`, `user` |
| `QWEN_SESSION_ADAPTER` | `QwenSessionAdapter` | qwen.rs:10 | `assistant`, `system`, `tool_result`, `user` |
| `GEMINI_SESSION_ADAPTER` | `GeminiSessionAdapter` | gemini.rs | *(see gemini.rs)* |

### `SessionTranscriptAdapter` Trait Methods

| Method | Signature | Purpose |
|---|---|---|
| `supports` | `(&self, envelope_type: &str) -> bool` | Quick per-envelope-type filter |
| `supports_archive` | `(&self, envelopes: &[SessionArchiveEnvelope]) -> bool` | Deep heuristic for archive-level disambiguation |
| `parse` | `(&self, envelopes: &[SessionArchiveEnvelope]) -> Result<ParsedSession, WikiError>` | Full deserialization and normalization |

### Shared Normalised Types

| Type | Role |
|---|---|
| `SessionArchiveEnvelope` | Raw input record with `envelope_type`, `timestamp`, and `payload: Value` |
| `ParsedSession` | Adapter output: title, `started_at`, messages, metadata |
| `ParsedSessionMessage` | Normalised single turn: role, content, timestamp |
| `ParsedSessionMetadata` | Accumulated model name, git branch, and similar session-level facts |
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

