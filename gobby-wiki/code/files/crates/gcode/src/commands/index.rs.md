---
title: crates/gcode/src/commands/index.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/index.rs
  ranges:
  - 10-60
  - 62-92
  - 96-104
  - 107-117
  - 119-132
  - 134-138
  - 140-195
  - 197-216
  - 218-240
  - 252-257
  - 260-262
  - 264-272
  - 274-294
  - 297-301
  - 304-309
  - 312-338
  - 341-364
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/index.rs:10-60](crates/gcode/src/commands/index.rs#L10-L60), [crates/gcode/src/commands/index.rs:62-92](crates/gcode/src/commands/index.rs#L62-L92), [crates/gcode/src/commands/index.rs:96-104](crates/gcode/src/commands/index.rs#L96-L104), [crates/gcode/src/commands/index.rs:107-117](crates/gcode/src/commands/index.rs#L107-L117), [crates/gcode/src/commands/index.rs:119-132](crates/gcode/src/commands/index.rs#L119-L132), [crates/gcode/src/commands/index.rs:134-138](crates/gcode/src/commands/index.rs#L134-L138), [crates/gcode/src/commands/index.rs:140-195](crates/gcode/src/commands/index.rs#L140-L195), [crates/gcode/src/commands/index.rs:197-216](crates/gcode/src/commands/index.rs#L197-L216), [crates/gcode/src/commands/index.rs:218-240](crates/gcode/src/commands/index.rs#L218-L240), [crates/gcode/src/commands/index.rs:252-257](crates/gcode/src/commands/index.rs#L252-L257), [crates/gcode/src/commands/index.rs:260-262](crates/gcode/src/commands/index.rs#L260-L262), [crates/gcode/src/commands/index.rs:264-272](crates/gcode/src/commands/index.rs#L264-L272), [crates/gcode/src/commands/index.rs:274-294](crates/gcode/src/commands/index.rs#L274-L294), [crates/gcode/src/commands/index.rs:297-301](crates/gcode/src/commands/index.rs#L297-L301), [crates/gcode/src/commands/index.rs:304-309](crates/gcode/src/commands/index.rs#L304-L309), [crates/gcode/src/commands/index.rs:312-338](crates/gcode/src/commands/index.rs#L312-L338), [crates/gcode/src/commands/index.rs:341-364](crates/gcode/src/commands/index.rs#L341-L364)

</details>

# crates/gcode/src/commands/index.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

Implements the `gcode` indexing command end to end: `run` resolves the target project context, builds an `IndexRequest`, runs indexing under the project lock, optionally syncs projections afterward, and prints either JSON or text output. The rest of the file is support code for that flow, including human-readable formatting helpers, context/path resolution, projection-sync payload/text construction, path filtering, noun pluralization, and tests that lock down output contracts and edge cases like unsupported file types and duration redaction.
[crates/gcode/src/commands/index.rs:10-60]
[crates/gcode/src/commands/index.rs:62-92]
[crates/gcode/src/commands/index.rs:96-104]
[crates/gcode/src/commands/index.rs:107-117]
[crates/gcode/src/commands/index.rs:119-132]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `run` | function | `pub fn run(` | `run [function]` | `7721bdec-8426-5866-bf95-2e88bc949bd6` | 10-60 [crates/gcode/src/commands/index.rs:10-60] | Indexed function `run` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:10-60] |
| `index_text` | function | `fn index_text(outcome: &IndexOutcome) -> String {` | `index_text [function]` | `052f4c96-2fb2-5fc7-b302-67e1723fa7a6` | 62-92 [crates/gcode/src/commands/index.rs:62-92] | Indexed function `index_text` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:62-92] |
| `pluralize` | function | `fn pluralize(count: usize, singular: &str) -> &str {` | `pluralize [function]` | `efa941fc-614f-5dfb-89b1-c2183a246a73` | 96-104 [crates/gcode/src/commands/index.rs:96-104] | Indexed function `pluralize` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:96-104] |
| `IndexSyncProjectionsOutput` | class | `pub(crate) struct IndexSyncProjectionsOutput {` | `IndexSyncProjectionsOutput [class]` | `427a1009-6d54-5890-8f63-3991d51a152b` | 107-117 [crates/gcode/src/commands/index.rs:107-117] | Indexed class `IndexSyncProjectionsOutput` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:107-117] |
| `sync_projections_payload` | function | `pub(crate) fn sync_projections_payload(` | `sync_projections_payload [function]` | `5deed216-d2ce-5241-ae89-3b058e7ca658` | 119-132 [crates/gcode/src/commands/index.rs:119-132] | Indexed function `sync_projections_payload` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:119-132] |
| `sync_projections_text` | function | `pub(crate) fn sync_projections_text(` | `sync_projections_text [function]` | `878dbfc7-6098-5d33-9c14-0d9e002fb015` | 134-138 [crates/gcode/src/commands/index.rs:134-138] | Indexed function `sync_projections_text` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:134-138] |
| `resolve_index_context` | function | `fn resolve_index_context(` | `resolve_index_context [function]` | `30262d9a-aca4-531a-8e4c-88ba5eadf5a8` | 140-195 [crates/gcode/src/commands/index.rs:140-195] | Indexed function `resolve_index_context` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:140-195] |
| `clone_context` | function | `fn clone_context(` | `clone_context [function]` | `20b94c5c-ca03-57a3-9a66-ffb0cd5b60c6` | 197-216 [crates/gcode/src/commands/index.rs:197-216] | Indexed function `clone_context` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:197-216] |
| `path_filter_for` | function | `fn path_filter_for(` | `path_filter_for [function]` | `5fb206ef-fa5d-5f7a-ab9b-59349d682e73` | 218-240 [crates/gcode/src/commands/index.rs:218-240] | Indexed function `path_filter_for` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:218-240] |
| `pluralize_handles_index_status_nouns` | function | `fn pluralize_handles_index_status_nouns() {` | `pluralize_handles_index_status_nouns [function]` | `cd4e684f-2b22-570d-b030-91ee582055fc` | 252-257 [crates/gcode/src/commands/index.rs:252-257] | Indexed function `pluralize_handles_index_status_nouns` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:252-257] |
| `pluralize_leaves_unknown_nouns_unchanged` | function | `fn pluralize_leaves_unknown_nouns_unchanged() {` | `pluralize_leaves_unknown_nouns_unchanged [function]` | `5d2392ab-bf6b-5728-8913-62ccf8cc4d42` | 260-262 [crates/gcode/src/commands/index.rs:260-262] | Indexed function `pluralize_leaves_unknown_nouns_unchanged` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:260-262] |
| `sample_outcome` | function | `fn sample_outcome() -> IndexOutcome {` | `sample_outcome [function]` | `17c10e50-6a1f-5bd3-b523-fbd5cd687f8d` | 264-272 [crates/gcode/src/commands/index.rs:264-272] | Indexed function `sample_outcome` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:264-272] |
| `sample_reports` | function | `fn sample_reports() -> ProjectionSyncReports {` | `sample_reports [function]` | `cdadc9d7-493a-5a55-a6c9-d58fb31dd2e8` | 274-294 [crates/gcode/src/commands/index.rs:274-294] | Indexed function `sample_reports` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:274-294] |
| `sync_projections_json_contract` | function | `fn sync_projections_json_contract() {` | `sync_projections_json_contract [function]` | `49cf0335-27a3-5466-93f5-7a1de8317e90` | 297-301 [crates/gcode/src/commands/index.rs:297-301] | Indexed function `sync_projections_json_contract` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:297-301] |
| `sync_projections_text_contract` | function | `fn sync_projections_text_contract() {` | `sync_projections_text_contract [function]` | `c112c5d2-65cc-5e28-8e45-4e36b7aaa969` | 304-309 [crates/gcode/src/commands/index.rs:304-309] | Indexed function `sync_projections_text_contract` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:304-309] |
| `index_outcome_json_contract_redacts_durations` | function | `fn index_outcome_json_contract_redacts_durations() {` | `index_outcome_json_contract_redacts_durations [function]` | `0c12a52b-3a21-5032-9c62-45e82d7b449a` | 312-338 [crates/gcode/src/commands/index.rs:312-338] | Indexed function `index_outcome_json_contract_redacts_durations` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:312-338] |
| `index_text_reports_unsupported_file_types` | function | `fn index_text_reports_unsupported_file_types() {` | `index_text_reports_unsupported_file_types [function]` | `17cd1983-18b6-506b-99d5-37f6bce36648` | 341-364 [crates/gcode/src/commands/index.rs:341-364] | Indexed function `index_text_reports_unsupported_file_types` in `crates/gcode/src/commands/index.rs`. [crates/gcode/src/commands/index.rs:341-364] |
