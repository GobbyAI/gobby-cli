---
title: crates/gwiki/src/ingest/session/metadata.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/metadata.rs
  ranges:
  - 10-15
  - 18-22
  - 24-28
  - 30-32
  - 34-36
  - 38-44
  - 47-87
  - 89-100
  - 102-106
  - 108-119
  - 121-132
  - 134-146
  - 148-152
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/session/metadata.rs:10-15](crates/gwiki/src/ingest/session/metadata.rs#L10-L15), [crates/gwiki/src/ingest/session/metadata.rs:18-22](crates/gwiki/src/ingest/session/metadata.rs#L18-L22), [crates/gwiki/src/ingest/session/metadata.rs:24-28](crates/gwiki/src/ingest/session/metadata.rs#L24-L28), [crates/gwiki/src/ingest/session/metadata.rs:30-32](crates/gwiki/src/ingest/session/metadata.rs#L30-L32), [crates/gwiki/src/ingest/session/metadata.rs:34-36](crates/gwiki/src/ingest/session/metadata.rs#L34-L36), [crates/gwiki/src/ingest/session/metadata.rs:38-44](crates/gwiki/src/ingest/session/metadata.rs#L38-L44), [crates/gwiki/src/ingest/session/metadata.rs:47-87](crates/gwiki/src/ingest/session/metadata.rs#L47-L87), [crates/gwiki/src/ingest/session/metadata.rs:89-100](crates/gwiki/src/ingest/session/metadata.rs#L89-L100), [crates/gwiki/src/ingest/session/metadata.rs:102-106](crates/gwiki/src/ingest/session/metadata.rs#L102-L106), [crates/gwiki/src/ingest/session/metadata.rs:108-119](crates/gwiki/src/ingest/session/metadata.rs#L108-L119), [crates/gwiki/src/ingest/session/metadata.rs:121-132](crates/gwiki/src/ingest/session/metadata.rs#L121-L132), [crates/gwiki/src/ingest/session/metadata.rs:134-146](crates/gwiki/src/ingest/session/metadata.rs#L134-L146), [crates/gwiki/src/ingest/session/metadata.rs:148-152](crates/gwiki/src/ingest/session/metadata.rs#L148-L152)

</details>

# crates/gwiki/src/ingest/session/metadata.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines `ParsedSessionMetadata`, a small accumulator for ingesting session-level metadata like model, git branch, token totals, and subagent status, with setters that only fill fields once and helpers that merge token usage data. It also builds the exported metadata field list for a `ParsedSession` by conditionally emitting model, tool counts, token totals, duration, hour buckets, subagent flag, and git branch, using shared utilities to coerce JSON number fields, compute counts and time-based summaries, and parse timestamps.
[crates/gwiki/src/ingest/session/metadata.rs:10-15]
[crates/gwiki/src/ingest/session/metadata.rs:18-22]
[crates/gwiki/src/ingest/session/metadata.rs:24-28]
[crates/gwiki/src/ingest/session/metadata.rs:30-32]
[crates/gwiki/src/ingest/session/metadata.rs:34-36]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ParsedSessionMetadata` | class | `pub(crate) struct ParsedSessionMetadata {` | `ParsedSessionMetadata [class]` | `3650e669-80be-5f64-b69b-a26c4e1c70f9` | 10-15 [crates/gwiki/src/ingest/session/metadata.rs:10-15] | Indexed class `ParsedSessionMetadata` in `crates/gwiki/src/ingest/session/metadata.rs`. [crates/gwiki/src/ingest/session/metadata.rs:10-15] |
| `ParsedSessionMetadata::set_model_once` | method | `pub(crate) fn set_model_once(&mut self, model: Option<&str>) {` | `ParsedSessionMetadata::set_model_once [method]` | `55d1f20a-9adf-5f1d-b109-110b0e8bc038` | 18-22 [crates/gwiki/src/ingest/session/metadata.rs:18-22] | Indexed method `ParsedSessionMetadata::set_model_once` in `crates/gwiki/src/ingest/session/metadata.rs`. [crates/gwiki/src/ingest/session/metadata.rs:18-22] |
| `ParsedSessionMetadata::set_git_branch_once` | method | `pub(crate) fn set_git_branch_once(&mut self, git_branch: Option<&str>) {` | `ParsedSessionMetadata::set_git_branch_once [method]` | `09880663-c897-5aef-a7e8-ff19422c3ebb` | 24-28 [crates/gwiki/src/ingest/session/metadata.rs:24-28] | Indexed method `ParsedSessionMetadata::set_git_branch_once` in `crates/gwiki/src/ingest/session/metadata.rs`. [crates/gwiki/src/ingest/session/metadata.rs:24-28] |
| `ParsedSessionMetadata::mark_subagent` | method | `pub(crate) fn mark_subagent(&mut self) {` | `ParsedSessionMetadata::mark_subagent [method]` | `b90eed6b-5e22-5157-97db-0c8f43a2df1c` | 30-32 [crates/gwiki/src/ingest/session/metadata.rs:30-32] | Indexed method `ParsedSessionMetadata::mark_subagent` in `crates/gwiki/src/ingest/session/metadata.rs`. [crates/gwiki/src/ingest/session/metadata.rs:30-32] |
| `ParsedSessionMetadata::add_token_usage` | method | `pub(crate) fn add_token_usage(&mut self, usage: &Value) {` | `ParsedSessionMetadata::add_token_usage [method]` | `5b01053e-60c1-5588-9245-683ecb6aa95d` | 34-36 [crates/gwiki/src/ingest/session/metadata.rs:34-36] | Indexed method `ParsedSessionMetadata::add_token_usage` in `crates/gwiki/src/ingest/session/metadata.rs`. [crates/gwiki/src/ingest/session/metadata.rs:34-36] |
| `ParsedSessionMetadata::set_token_totals` | method | `pub(crate) fn set_token_totals(&mut self, usage: &Value) {` | `ParsedSessionMetadata::set_token_totals [method]` | `6659d1c9-e9eb-5964-a0c8-a199789b6f39` | 38-44 [crates/gwiki/src/ingest/session/metadata.rs:38-44] | Indexed method `ParsedSessionMetadata::set_token_totals` in `crates/gwiki/src/ingest/session/metadata.rs`. [crates/gwiki/src/ingest/session/metadata.rs:38-44] |
| `session_metadata_fields` | function | `pub(crate) fn session_metadata_fields(` | `session_metadata_fields [function]` | `338d6874-d9fb-55d2-a939-41df90807614` | 47-87 [crates/gwiki/src/ingest/session/metadata.rs:47-87] | Indexed function `session_metadata_fields` in `crates/gwiki/src/ingest/session/metadata.rs`. [crates/gwiki/src/ingest/session/metadata.rs:47-87] |
| `add_json_number_fields` | function | `fn add_json_number_fields(totals: &mut BTreeMap<String, u64>, usage: &Value) {` | `add_json_number_fields [function]` | `9d0484bb-c033-572f-bd67-8df2c434d56f` | 89-100 [crates/gwiki/src/ingest/session/metadata.rs:89-100] | Indexed function `add_json_number_fields` in `crates/gwiki/src/ingest/session/metadata.rs`. [crates/gwiki/src/ingest/session/metadata.rs:89-100] |
| `json_u64` | function | `fn json_u64(value: &Value) -> Option<u64> {` | `json_u64 [function]` | `6d6d7c3c-c1b2-518a-b534-15a6d5aede66` | 102-106 [crates/gwiki/src/ingest/session/metadata.rs:102-106] | Indexed function `json_u64` in `crates/gwiki/src/ingest/session/metadata.rs`. [crates/gwiki/src/ingest/session/metadata.rs:102-106] |
| `tool_counts` | function | `fn tool_counts(parsed: &ParsedSession) -> BTreeMap<String, u64> {` | `tool_counts [function]` | `126d18c4-fe24-5546-b3da-829617f7a295` | 108-119 [crates/gwiki/src/ingest/session/metadata.rs:108-119] | Indexed function `tool_counts` in `crates/gwiki/src/ingest/session/metadata.rs`. [crates/gwiki/src/ingest/session/metadata.rs:108-119] |
| `duration_seconds` | function | `fn duration_seconds(parsed: &ParsedSession) -> Option<i64> {` | `duration_seconds [function]` | `121b9252-1e46-5624-96c6-d2c1c45d9a64` | 121-132 [crates/gwiki/src/ingest/session/metadata.rs:121-132] | Indexed function `duration_seconds` in `crates/gwiki/src/ingest/session/metadata.rs`. [crates/gwiki/src/ingest/session/metadata.rs:121-132] |
| `hour_buckets` | function | `fn hour_buckets(parsed: &ParsedSession) -> BTreeMap<String, u64> {` | `hour_buckets [function]` | `e2e25698-28cc-5e61-be8c-cfa440f60bb3` | 134-146 [crates/gwiki/src/ingest/session/metadata.rs:134-146] | Indexed function `hour_buckets` in `crates/gwiki/src/ingest/session/metadata.rs`. [crates/gwiki/src/ingest/session/metadata.rs:134-146] |
| `parse_timestamp` | function | `fn parse_timestamp(value: &str) -> Option<DateTime<Utc>> {` | `parse_timestamp [function]` | `d6a11f1a-6893-5bcc-8c13-a94dcf6a24c0` | 148-152 [crates/gwiki/src/ingest/session/metadata.rs:148-152] | Indexed function `parse_timestamp` in `crates/gwiki/src/ingest/session/metadata.rs`. [crates/gwiki/src/ingest/session/metadata.rs:148-152] |
