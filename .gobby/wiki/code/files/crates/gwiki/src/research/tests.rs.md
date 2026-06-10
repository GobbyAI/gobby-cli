---
title: crates/gwiki/src/research/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/research/tests.rs
  ranges:
  - 8-21
  - 23-27
  - 29-37
  - 40-46
  - 49-60
  - 63-72
  - 75-107
  - 110-121
  - 124-168
  - 171-211
  - 214-254
  - 257-279
  - 282-322
  - 325-342
  - 345-378
  - 381-404
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/research/tests.rs

Module: [[code/modules/crates/gwiki/src/research|crates/gwiki/src/research]]

## Purpose

`crates/gwiki/src/research/tests.rs` exposes 16 indexed API symbols.
[crates/gwiki/src/research/tests.rs:8-21]
[crates/gwiki/src/research/tests.rs:23-27]
[crates/gwiki/src/research/tests.rs:29-37]
[crates/gwiki/src/research/tests.rs:40-46]
[crates/gwiki/src/research/tests.rs:49-60]
[crates/gwiki/src/research/tests.rs:63-72]
[crates/gwiki/src/research/tests.rs:75-107]
[crates/gwiki/src/research/tests.rs:110-121]
[crates/gwiki/src/research/tests.rs:124-168]
[crates/gwiki/src/research/tests.rs:171-211]
[crates/gwiki/src/research/tests.rs:214-254]
[crates/gwiki/src/research/tests.rs:257-279]
[crates/gwiki/src/research/tests.rs:282-322]
[crates/gwiki/src/research/tests.rs:325-342]
[crates/gwiki/src/research/tests.rs:345-378]
[crates/gwiki/src/research/tests.rs:381-404]

## API Symbols

- `default_options` (function) component `default_options [function]` (`13b5734b-5766-58af-81ec-d3c9db0e3828`) lines 8-21 [crates/gwiki/src/research/tests.rs:8-21]
  - Signature: `fn default_options(question: &str, scope: ResearchScope) -> ResearchOptions {`
  - Purpose: Constructs a `ResearchOptions` struct with default parameters (12 max_steps, 24,000 max_tokens, 8 max_sources, direct AI routing) initialized with the provided research question and scope. [crates/gwiki/src/research/tests.rs:8-21]
- `write_test_source` (function) component `write_test_source [function]` (`b12680e4-8e3f-59ad-a57e-ee6f35c02c20`) lines 23-27 [crates/gwiki/src/research/tests.rs:23-27]
  - Signature: `fn write_test_source(root: &Path) {`
  - Purpose: Creates a 'raw' subdirectory under the specified root path and writes a file named 'source.md' containing the string "source", panicking on any I/O failure. [crates/gwiki/src/research/tests.rs:23-27]
- `write_project_identity` (function) component `write_project_identity [function]` (`0f10de80-17f0-5662-8e92-b3ad1f74b9a0`) lines 29-37 [crates/gwiki/src/research/tests.rs:29-37]
  - Signature: `fn write_project_identity(project_root: &Path, project_id: &str) {`
  - Purpose: Writes a `gcode.json` file to a `.gobby` directory containing a JSON object with the provided project ID and a hardcoded "test" name field. [crates/gwiki/src/research/tests.rs:29-37]
- `frontmatter_block_accepts_crlf_delimiters` (function) component `frontmatter_block_accepts_crlf_delimiters [function]` (`11374150-465b-5b1b-a9c9-e5761f2e5757`) lines 40-46 [crates/gwiki/src/research/tests.rs:40-46]
  - Signature: `fn frontmatter_block_accepts_crlf_delimiters() {`
  - Purpose: This test function verifies that `frontmatter_block()` correctly parses YAML frontmatter delimited by `---` markers when the input uses CRLF line endings. [crates/gwiki/src/research/tests.rs:40-46]
- `yaml_field_eq_requires_exact_key_and_value` (function) component `yaml_field_eq_requires_exact_key_and_value [function]` (`7d97c472-54ca-5f2e-ba9b-107806d8cd1c`) lines 49-60 [crates/gwiki/src/research/tests.rs:49-60]
  - Signature: `fn yaml_field_eq_requires_exact_key_and_value() {`
  - Purpose: This test verifies that the `yaml_field_eq` function performs exact string matching on both YAML field keys and values, rejecting partial or suffix matches. [crates/gwiki/src/research/tests.rs:49-60]
- `yaml_field_eq_rejects_block_scalar_prefix_match` (function) component `yaml_field_eq_rejects_block_scalar_prefix_match [function]` (`b21f4c12-f9cd-5388-946f-ddc70ab64506`) lines 63-72 [crates/gwiki/src/research/tests.rs:63-72]
  - Signature: `fn yaml_field_eq_rejects_block_scalar_prefix_match() {`
  - Purpose: Verifies that `yaml_field_eq` rejects matching block scalar YAML field values while accepting exact comparisons on plain scalar fields. [crates/gwiki/src/research/tests.rs:63-72]
- `research_reloads_checkpoint_without_daemon_dispatch` (function) component `research_reloads_checkpoint_without_daemon_dispatch [function]` (`9dde5b11-f509-5812-87a4-d4420c1bcb1c`) lines 75-107 [crates/gwiki/src/research/tests.rs:75-107]
  - Signature: `fn research_reloads_checkpoint_without_daemon_dispatch() {`
  - Purpose: Verifies that reloading a research session checkpoint clears daemon dispatch metadata (dispatch_task_id and dispatch fields) while preserving the session identifier. [crates/gwiki/src/research/tests.rs:75-107]
- `enrichment_require_ai_rejects_ai_off` (function) component `enrichment_require_ai_rejects_ai_off [function]` (`3a4a270e-8dab-5f9a-b9eb-ae77b7ec380c`) lines 110-121 [crates/gwiki/src/research/tests.rs:110-121]
  - Signature: `fn enrichment_require_ai_rejects_ai_off() {`
  - Purpose: This test validates that enrichment rejects the contradictory configuration of requiring AI (`require_ai = true`) while simultaneously disabling AI routing (`AiRouting::Off`), asserting it raises a `WikiError::Config`. [crates/gwiki/src/research/tests.rs:110-121]
- `accepted_notes_land_in_raw_research` (function) component `accepted_notes_land_in_raw_research [function]` (`ac78227a-61dc-546f-9cca-af5959828709`) lines 124-168 [crates/gwiki/src/research/tests.rs:124-168]
  - Signature: `fn accepted_notes_land_in_raw_research() {`
  - Purpose: # Summary

Tests that pre-accepted notes are written to the `raw/research` directory with proper metadata and indexed correctly without executing additional research steps. [crates/gwiki/src/research/tests.rs:124-168]
- `accepted_note_collisions_use_numeric_suffixes` (function) component `accepted_note_collisions_use_numeric_suffixes [function]` (`9f6b4c1c-a3aa-5ad1-bf7c-cfc633cac90d`) lines 171-211 [crates/gwiki/src/research/tests.rs:171-211]
  - Signature: `fn accepted_note_collisions_use_numeric_suffixes() {`
  - Purpose: This function tests that writing multiple accepted notes with identical titles generates numeric suffixes for disambiguation (e.g., `same-title-2.md`) without triggering write conflicts. [crates/gwiki/src/research/tests.rs:171-211]
- `accepted_note_draft_collision_with_changed_body_is_write_conflict` (function) component `accepted_note_draft_collision_with_changed_body_is_write_conflict [function]` (`10392a73-4fb7-5493-a33e-02de7abdca95`) lines 214-254 [crates/gwiki/src/research/tests.rs:214-254]
  - Signature: `fn accepted_note_draft_collision_with_changed_body_is_write_conflict() {`
  - Purpose: This test verifies that `write_accepted_note()` correctly detects and prevents overwriting an existing note when an `AcceptedNoteDraft` with an identical draft ID but modified body content is concurrently written, triggering a write conflict. [crates/gwiki/src/research/tests.rs:214-254]
- `accepted_notes_are_idempotent_by_draft_id` (function) component `accepted_notes_are_idempotent_by_draft_id [function]` (`f4481eab-b66e-5c65-a9ba-b1cce99e4ab4`) lines 257-279 [crates/gwiki/src/research/tests.rs:257-279]
  - Signature: `fn accepted_notes_are_idempotent_by_draft_id() {`
  - Purpose: Verifies that `write_accepted_note` is idempotent by draft ID, ensuring identical consecutive writes produce a single file with the same path and no duplicates or conflicts. [crates/gwiki/src/research/tests.rs:257-279]
- `accepted_note_waits_for_materializing_marker_to_complete` (function) component `accepted_note_waits_for_materializing_marker_to_complete [function]` (`41e5c4e1-dc14-5784-bd05-52e948963b96`) lines 282-322 [crates/gwiki/src/research/tests.rs:282-322]
  - Signature: `fn accepted_note_waits_for_materializing_marker_to_complete() {`
  - Purpose: This test verifies that `write_accepted_note` blocks until a "materializing" marker in the target file is replaced with a "completed" marker before returning. [crates/gwiki/src/research/tests.rs:282-322]
- `research_scope_from_resolved_carries_project_id` (function) component `research_scope_from_resolved_carries_project_id [function]` (`9185e3dd-392b-5e25-b471-f6a8a0a02ce5`) lines 325-342 [crates/gwiki/src/research/tests.rs:325-342]
  - Signature: `fn research_scope_from_resolved_carries_project_id() {`
  - Purpose: Tests that `research_scope_from_resolved()` correctly converts a project-scoped `ResolvedScope` into a `ResearchScope::Project` variant with the expected project ID and root path. [crates/gwiki/src/research/tests.rs:325-342]
- `deterministic_audit_reports_untracked_completed_note` (function) component `deterministic_audit_reports_untracked_completed_note [function]` (`72642458-367b-58eb-94d3-9c56dae32ad5`) lines 345-378 [crates/gwiki/src/research/tests.rs:345-378]
  - Signature: `fn deterministic_audit_reports_untracked_completed_note() {`
  - Purpose: Tests that the audit system correctly identifies and reports an orphaned (untracked) research note with completed status as a finding when running in audit mode with AI routing disabled. [crates/gwiki/src/research/tests.rs:345-378]
- `deterministic_audit_uses_checkpoint_inventory` (function) component `deterministic_audit_uses_checkpoint_inventory [function]` (`056d29d3-15b2-524f-806f-4036adacd1ef`) lines 381-404 [crates/gwiki/src/research/tests.rs:381-404]
  - Signature: `fn deterministic_audit_uses_checkpoint_inventory() {`
  - Purpose: Tests that a deterministic offline audit produces no findings when verifying a research scope's checkpoint inventory against a pre-recorded accepted note. [crates/gwiki/src/research/tests.rs:381-404]

