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

# crates/gcode/src/commands/index.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

`crates/gcode/src/commands/index.rs` exposes 17 indexed API symbols.
[crates/gcode/src/commands/index.rs:10-60]
[crates/gcode/src/commands/index.rs:62-92]
[crates/gcode/src/commands/index.rs:96-104]
[crates/gcode/src/commands/index.rs:107-117]
[crates/gcode/src/commands/index.rs:119-132]

## API Symbols

- `run` (function) component `run [function]` (`7721bdec-8426-5866-bf95-2e88bc949bd6`) lines 10-60 [crates/gcode/src/commands/index.rs:10-60]
  - Signature: `pub fn run(`
  - Purpose: Acquires an exclusive project lock and indexes files with optional path/file filtering and C++ semantic analysis, outputting the index outcome or synchronized projections in the requested format. [crates/gcode/src/commands/index.rs:10-60]
- `index_text` (function) component `index_text [function]` (`052f4c96-2fb2-5fc7-b302-67e1723fa7a6`) lines 62-92 [crates/gcode/src/commands/index.rs:62-92]
  - Signature: `fn index_text(outcome: &IndexOutcome) -> String {`
  - Purpose: Generates a formatted string summarizing indexing metrics—indexed and skipped file counts, symbol and chunk counts, execution duration, and details of any unsupported file types—from an `IndexOutcome`. [crates/gcode/src/commands/index.rs:62-92]
- `pluralize` (function) component `pluralize [function]` (`efa941fc-614f-5dfb-89b1-c2183a246a73`) lines 96-104 [crates/gcode/src/commands/index.rs:96-104]
  - Signature: `fn pluralize(count: usize, singular: &str) -> &str {`
  - Purpose: Returns the plural form of a noun based on count for hardcoded cases ("file" and "example"), otherwise returns the singular form unchanged. [crates/gcode/src/commands/index.rs:96-104]
- `IndexSyncProjectionsOutput` (class) component `IndexSyncProjectionsOutput [class]` (`427a1009-6d54-5890-8f63-3991d51a152b`) lines 107-117 [crates/gcode/src/commands/index.rs:107-117]
  - Signature: `pub(crate) struct IndexSyncProjectionsOutput {`
  - Purpose: `IndexSyncProjectionsOutput` aggregates indexing statistics (file and symbol/chunk counts), unsupported file type metadata, degradation diagnostics, and projection synchronization reports from an index sync operation. [crates/gcode/src/commands/index.rs:107-117]
- `sync_projections_payload` (function) component `sync_projections_payload [function]` (`5deed216-d2ce-5241-ae89-3b058e7ca658`) lines 119-132 [crates/gcode/src/commands/index.rs:119-132]
  - Signature: `pub(crate) fn sync_projections_payload(`
  - Purpose: Constructs an `IndexSyncProjectionsOutput` by aggregating indexing metrics from an `IndexOutcome` with projection synchronization reports. [crates/gcode/src/commands/index.rs:119-132]
- `sync_projections_text` (function) component `sync_projections_text [function]` (`878dbfc7-6098-5d33-9c14-0d9e002fb015`) lines 134-138 [crates/gcode/src/commands/index.rs:134-138]
  - Signature: `pub(crate) fn sync_projections_text(`
  - Purpose: Serializes an `IndexSyncProjectionsOutput` payload to a JSON string, returning the result wrapped in an `anyhow::Result` for error handling. [crates/gcode/src/commands/index.rs:134-138]
- `resolve_index_context` (function) component `resolve_index_context [function]` (`30262d9a-aca4-531a-8e4c-88ba5eadf5a8`) lines 140-195 [crates/gcode/src/commands/index.rs:140-195]
  - Signature: `fn resolve_index_context(`
  - Purpose: Resolves or re-resolves project context (root, identity, and index scope) for an optional file path, detecting cross-project membership and returning the appropriate context with a path filter if needed. [crates/gcode/src/commands/index.rs:140-195]
- `clone_context` (function) component `clone_context [function]` (`20b94c5c-ca03-57a3-9a66-ffb0cd5b60c6`) lines 197-216 [crates/gcode/src/commands/index.rs:197-216]
  - Signature: `fn clone_context(`
  - Purpose: Creates a new `Context` by cloning shared configuration fields from an existing context while substituting project-specific parameters (project_root, project_id, and index_scope). [crates/gcode/src/commands/index.rs:197-216]
- `path_filter_for` (function) component `path_filter_for [function]` (`5fb206ef-fa5d-5f7a-ab9b-59349d682e73`) lines 218-240 [crates/gcode/src/commands/index.rs:218-240]
  - Signature: `fn path_filter_for(`
  - Purpose: Resolves a target path to an absolute, canonicalized path and returns it only if it differs from the project root, otherwise returns `None`. [crates/gcode/src/commands/index.rs:218-240]
- `pluralize_handles_index_status_nouns` (function) component `pluralize_handles_index_status_nouns [function]` (`cd4e684f-2b22-570d-b030-91ee582055fc`) lines 252-257 [crates/gcode/src/commands/index.rs:252-257]
  - Signature: `fn pluralize_handles_index_status_nouns() {`
  - Purpose: This test function verifies that the `pluralize` function returns the singular form of a noun when the count is 1, and the plural form when the count is 0 or any other value. [crates/gcode/src/commands/index.rs:252-257]
- `pluralize_leaves_unknown_nouns_unchanged` (function) component `pluralize_leaves_unknown_nouns_unchanged [function]` (`5d2392ab-bf6b-5728-8913-62ccf8cc4d42`) lines 260-262 [crates/gcode/src/commands/index.rs:260-262]
  - Signature: `fn pluralize_leaves_unknown_nouns_unchanged() {`
  - Purpose: This test verifies that the `pluralize` function returns unrecognized nouns unchanged, leaving `"symbol"` unchanged when pluralizing for a count of 2. [crates/gcode/src/commands/index.rs:260-262]
- `sample_outcome` (function) component `sample_outcome [function]` (`17c10e50-6a1f-5bd3-b523-fbd5cd687f8d`) lines 264-272 [crates/gcode/src/commands/index.rs:264-272]
  - Signature: `fn sample_outcome() -> IndexOutcome {`
  - Purpose: Returns an `IndexOutcome` struct initialized with sample metrics of 12 indexed files, 0 skipped files, 348 indexed symbols, and 921 indexed chunks. [crates/gcode/src/commands/index.rs:264-272]
- `sample_reports` (function) component `sample_reports [function]` (`cdadc9d7-493a-5a55-a6c9-d58fb31dd2e8`) lines 274-294 [crates/gcode/src/commands/index.rs:274-294]
  - Signature: `fn sample_reports() -> ProjectionSyncReports {`
  - Purpose: Returns a `ProjectionSyncReports` struct containing sample sync reports with graph projection in Ok status (12 files, 348 symbols) and vector projection in Degraded status due to missing Qdrant configuration. [crates/gcode/src/commands/index.rs:274-294]
- `sync_projections_json_contract` (function) component `sync_projections_json_contract [function]` (`49cf0335-27a3-5466-93f5-7a1de8317e90`) lines 297-301 [crates/gcode/src/commands/index.rs:297-301]
  - Signature: `fn sync_projections_json_contract() {`
  - Purpose: This function is a snapshot test that validates the JSON output of `sync_projections_payload()` against a stored snapshot using the insta testing framework. [crates/gcode/src/commands/index.rs:297-301]
- `sync_projections_text_contract` (function) component `sync_projections_text_contract [function]` (`c112c5d2-65cc-5e28-8e45-4e36b7aaa969`) lines 304-309 [crates/gcode/src/commands/index.rs:304-309]
  - Signature: `fn sync_projections_text_contract() {`
  - Purpose: This function executes a snapshot test that verifies the `sync_projections_text` function produces deterministic output from sample projection data. [crates/gcode/src/commands/index.rs:304-309]
- `index_outcome_json_contract_redacts_durations` (function) component `index_outcome_json_contract_redacts_durations [function]` (`0c12a52b-3a21-5032-9c62-45e82d7b449a`) lines 312-338 [crates/gcode/src/commands/index.rs:312-338]
  - Signature: `fn index_outcome_json_contract_redacts_durations() {`
  - Purpose: This function redacts duration metric values in a serialized indexing outcome JSON object by replacing them with a placeholder string and asserts the result via snapshot testing. [crates/gcode/src/commands/index.rs:312-338]
- `index_text_reports_unsupported_file_types` (function) component `index_text_reports_unsupported_file_types [function]` (`17cd1983-18b6-506b-99d5-37f6bce36648`) lines 341-364 [crates/gcode/src/commands/index.rs:341-364]
  - Signature: `fn index_text_reports_unsupported_file_types() {`
  - Purpose: Verifies via snapshot testing that `index_text()` correctly formats an outcome's unsupported file types metadata into text output. [crates/gcode/src/commands/index.rs:341-364]

