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
  - 75-108
  - 111-122
  - 125-169
  - 172-212
  - 215-255
  - 258-280
  - 283-323
  - 326-343
  - 346-379
  - 382-405
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

## API Symbols

- `default_options` (function) component `default_options [function]` (`13b5734b-5766-58af-81ec-d3c9db0e3828`) lines 8-21 [crates/gwiki/src/research/tests.rs:8-21]
  - Signature: `fn default_options(question: &str, scope: ResearchScope) -> ResearchOptions {`
  - Purpose: Creates a `ResearchOptions` struct with default configuration (12 max steps, 24,000 max tokens, 8 max sources, direct AI routing, no auditing) for a specified question and research scope. [crates/gwiki/src/research/tests.rs:8-21]
- `write_test_source` (function) component `write_test_source [function]` (`b12680e4-8e3f-59ad-a57e-ee6f35c02c20`) lines 23-27 [crates/gwiki/src/research/tests.rs:23-27]
  - Signature: `fn write_test_source(root: &Path) {`
  - Purpose: Creates a nested `raw` subdirectory under the given root path and writes a file named `source.md` containing the literal string "source". [crates/gwiki/src/research/tests.rs:23-27]
- `write_project_identity` (function) component `write_project_identity [function]` (`0f10de80-17f0-5662-8e92-b3ad1f74b9a0`) lines 29-37 [crates/gwiki/src/research/tests.rs:29-37]
  - Signature: `fn write_project_identity(project_root: &Path, project_id: &str) {`
  - Purpose: Writes a `.gobby/gcode.json` identity file to the project root containing the provided project ID and a static name metadata. [crates/gwiki/src/research/tests.rs:29-37]
- `frontmatter_block_accepts_crlf_delimiters` (function) component `frontmatter_block_accepts_crlf_delimiters [function]` (`11374150-465b-5b1b-a9c9-e5761f2e5757`) lines 40-46 [crates/gwiki/src/research/tests.rs:40-46]
  - Signature: `fn frontmatter_block_accepts_crlf_delimiters() {`
  - Purpose: Unit test verifying that `frontmatter_block()` correctly parses YAML frontmatter when input uses CRLF line delimiters. [crates/gwiki/src/research/tests.rs:40-46]
- `yaml_field_eq_requires_exact_key_and_value` (function) component `yaml_field_eq_requires_exact_key_and_value [function]` (`7d97c472-54ca-5f2e-ba9b-107806d8cd1c`) lines 49-60 [crates/gwiki/src/research/tests.rs:49-60]
  - Signature: `fn yaml_field_eq_requires_exact_key_and_value() {`
  - Purpose: This test validates that `yaml_field_eq()` performs exact matching on both YAML field keys and their string values, rejecting partial key name matches and value substrings. [crates/gwiki/src/research/tests.rs:49-60]
- `yaml_field_eq_rejects_block_scalar_prefix_match` (function) component `yaml_field_eq_rejects_block_scalar_prefix_match [function]` (`b21f4c12-f9cd-5388-946f-ddc70ab64506`) lines 63-72 [crates/gwiki/src/research/tests.rs:63-72]
  - Signature: `fn yaml_field_eq_rejects_block_scalar_prefix_match() {`
  - Purpose: This test verifies that `yaml_field_eq` rejects partial prefix matching against YAML fields using block scalar syntax (rejecting "abc" as a match for the block scalar value despite it being a prefix). [crates/gwiki/src/research/tests.rs:63-72]
- `research_reloads_checkpoint_without_daemon_dispatch` (function) component `research_reloads_checkpoint_without_daemon_dispatch [function]` (`9dde5b11-f509-5812-87a4-d4420c1bcb1c`) lines 75-108 [crates/gwiki/src/research/tests.rs:75-108]
  - Signature: `fn research_reloads_checkpoint_without_daemon_dispatch() {`
  - Purpose: Tests that reloading a saved research checkpoint clears daemon dispatch metadata and resets agent count when AI routing is disabled. [crates/gwiki/src/research/tests.rs:75-108]
- `enrichment_require_ai_rejects_ai_off` (function) component `enrichment_require_ai_rejects_ai_off [function]` (`818c912e-b973-5efa-a74a-7682a0d4dfc9`) lines 111-122 [crates/gwiki/src/research/tests.rs:111-122]
  - Signature: `fn enrichment_require_ai_rejects_ai_off() {`
  - Purpose: This unit test asserts that enrichment operations raise a `WikiError::Config` when AI is simultaneously required (`require_ai=true`) and disabled (`ai=AiRouting::Off`). [crates/gwiki/src/research/tests.rs:111-122]
- `accepted_notes_land_in_raw_research` (function) component `accepted_notes_land_in_raw_research [function]` (`81813d08-9294-5cfb-8220-3f4d912474ae`) lines 125-169 [crates/gwiki/src/research/tests.rs:125-169]
  - Signature: `fn accepted_notes_land_in_raw_research() {`
  - Purpose: This test verifies that pre-drafted notes provided via the `accepted_notes` parameter are persisted to the `raw/research` directory with research metadata and registered in the scope's `INDEX.md`. [crates/gwiki/src/research/tests.rs:125-169]
- `accepted_note_collisions_use_numeric_suffixes` (function) component `accepted_note_collisions_use_numeric_suffixes [function]` (`f6c359cc-e87c-53ea-9134-4c408c10364f`) lines 172-212 [crates/gwiki/src/research/tests.rs:172-212]
  - Signature: `fn accepted_note_collisions_use_numeric_suffixes() {`
  - Purpose: Tests that `write_accepted_note` resolves identical note titles by appending numeric suffixes (e.g., `-2`) to filenames without flagging write conflicts. [crates/gwiki/src/research/tests.rs:172-212]
- `accepted_note_draft_collision_with_changed_body_is_write_conflict` (function) component `accepted_note_draft_collision_with_changed_body_is_write_conflict [function]` (`805c080e-6f04-5b63-b0f9-800d869651ff`) lines 215-255 [crates/gwiki/src/research/tests.rs:215-255]
  - Signature: `fn accepted_note_draft_collision_with_changed_body_is_write_conflict() {`
  - Purpose: This test verifies that `write_accepted_note` correctly detects a write conflict when a note with the same ID already exists with a different body content (indicating concurrent modification), and preserves the existing note without overwriting or creating a suffix-bumped variant. [crates/gwiki/src/research/tests.rs:215-255]
- `accepted_notes_are_idempotent_by_draft_id` (function) component `accepted_notes_are_idempotent_by_draft_id [function]` (`6ad0a94b-a0c5-523b-a5b5-ac01de2cde0c`) lines 258-280 [crates/gwiki/src/research/tests.rs:258-280]
  - Signature: `fn accepted_notes_are_idempotent_by_draft_id() {`
  - Purpose: Verifies that writing an accepted note twice with the same draft_id and content is idempotent, where the second write reuses the existing note path without creating a duplicate file or index entry. [crates/gwiki/src/research/tests.rs:258-280]
- `accepted_note_waits_for_materializing_marker_to_complete` (function) component `accepted_note_waits_for_materializing_marker_to_complete [function]` (`023b01fc-edc8-5ea8-8169-4846891b3abf`) lines 283-323 [crates/gwiki/src/research/tests.rs:283-323]
  - Signature: `fn accepted_note_waits_for_materializing_marker_to_complete() {`
  - Purpose: # Summary

This test verifies that `write_accepted_note` correctly blocks on an in-progress materializing note marker, allows it to complete, and returns the existing note path without creating a duplicate entry. [crates/gwiki/src/research/tests.rs:283-323]
- `research_scope_from_resolved_carries_project_id` (function) component `research_scope_from_resolved_carries_project_id [function]` (`8110eb1f-5348-506a-8663-2ab887c8706e`) lines 326-343 [crates/gwiki/src/research/tests.rs:326-343]
  - Signature: `fn research_scope_from_resolved_carries_project_id() {`
  - Purpose: This unit test asserts that `research_scope_from_resolved` correctly converts a project-scoped `ResolvedScope` into a `ResearchScope::Project` variant with the expected project ID and root path. [crates/gwiki/src/research/tests.rs:326-343]
- `deterministic_audit_reports_untracked_completed_note` (function) component `deterministic_audit_reports_untracked_completed_note [function]` (`b07fac2c-81f4-5991-966f-b7d685626672`) lines 346-379 [crates/gwiki/src/research/tests.rs:346-379]
  - Signature: `fn deterministic_audit_reports_untracked_completed_note() {`
  - Purpose: Tests that the audit system detects untracked completed research notes in the raw directory and reports them as orphaned findings when run with AI disabled. [crates/gwiki/src/research/tests.rs:346-379]
- `deterministic_audit_uses_checkpoint_inventory` (function) component `deterministic_audit_uses_checkpoint_inventory [function]` (`bd4c8c5c-e055-50d9-abe2-3d3adcfa3473`) lines 382-405 [crates/gwiki/src/research/tests.rs:382-405]
  - Signature: `fn deterministic_audit_uses_checkpoint_inventory() {`
  - Purpose: Tests that an AI-disabled audit run against a project with pre-recorded accepted notes as checkpoint inventory produces zero findings, validating the audit's correctness. [crates/gwiki/src/research/tests.rs:382-405]

