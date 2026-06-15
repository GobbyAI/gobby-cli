---
title: crates/gwiki/src/compile/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/compile/tests.rs
  ranges:
  - 7-25
  - 28-72
  - 75-102
  - 105-131
  - 134-170
  - 173-219
  - 223-243
  - 247-277
  - 280-349
  - 352-379
  - 382-411
  - 414-421
  - 424-443
  - 446-514
  - 517-552
  - 555-583
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/compile/tests.rs

Module: [[code/modules/crates/gwiki/src/compile|crates/gwiki/src/compile]]

## Purpose

Test module for the compile/handoff pipeline in the wiki compiler. It builds a reusable `ResearchSession` fixture and then exercises `prepare_handoff`, `compile_to_wiki`, `compile_to_wiki_with_options`, `update_wiki_index`, `insert_compiled_page_link`, and `write_target_page` across success and failure cases. The tests check that generated bundles preserve required sections and provenance, that wiki output is written in the expected Obsidian-style format, and that path safety and overwrite rules are enforced for accepted notes and target pages, including symlink traversal and non-destructive write intent behavior.
[crates/gwiki/src/compile/tests.rs:7-25]
[crates/gwiki/src/compile/tests.rs:28-72]
[crates/gwiki/src/compile/tests.rs:75-102]
[crates/gwiki/src/compile/tests.rs:105-131]
[crates/gwiki/src/compile/tests.rs:134-170]

## API Symbols

- `session_with_note` (function) component `session_with_note [function]` (`3e2a0d2e-acba-52ef-a278-4615cf9b68ec`) lines 7-25 [crates/gwiki/src/compile/tests.rs:7-25]
  - Signature: `fn session_with_note(scope: &ResearchScope, title: &str, relative_path: &str) -> ResearchSession {`
  - Purpose: Constructs a 'ResearchSession' test fixture with fixed session metadata, a cloned 'ResearchScope', one accepted note whose title and path are derived from the arguments, and all other optional fields left unset. [crates/gwiki/src/compile/tests.rs:7-25]
- `compile_bundle_contains_required_sections` (function) component `compile_bundle_contains_required_sections [function]` (`5ce1504f-2807-58f0-999d-3b92fe5ba5b5`) lines 28-72 [crates/gwiki/src/compile/tests.rs:28-72]
  - Signature: `fn compile_bundle_contains_required_sections() {`
  - Purpose: Creates a temporary research note, runs 'prepare_handoff' for a compile-behavior request, and verifies the generated bundle preserves the outline, accepted source, citations, conflicts, missing evidence, and rendered section headers. [crates/gwiki/src/compile/tests.rs:28-72]
- `compile_handoff_is_non_destructive_by_default` (function) component `compile_handoff_is_non_destructive_by_default [function]` (`7eeebf91-8b12-5be1-9ec1-8c0f6e2eccc6`) lines 75-102 [crates/gwiki/src/compile/tests.rs:75-102]
  - Signature: `fn compile_handoff_is_non_destructive_by_default() {`
  - Purpose: Verifies that 'prepare_handoff' with 'write_intent: false' leaves an existing human-authored target page unchanged, produces a bundle path distinct from that page, and preserves the session state’s non-destructive write intent flag. [crates/gwiki/src/compile/tests.rs:75-102]
- `prepare_handoff_does_not_write_target_page` (function) component `prepare_handoff_does_not_write_target_page [function]` (`40448d26-2ef7-5649-886b-efc9cf8d17a9`) lines 105-131 [crates/gwiki/src/compile/tests.rs:105-131]
  - Signature: `fn prepare_handoff_does_not_write_target_page() {`
  - Purpose: Verifies that 'prepare_handoff' preserves an existing target wiki page unchanged when 'write_intent' is true, while still producing an outcome whose 'state.write_intent' remains enabled. [crates/gwiki/src/compile/tests.rs:105-131]
- `compile_fails_on_out_of_scope_accepted_note` (function) component `compile_fails_on_out_of_scope_accepted_note [function]` (`fc4c6394-28ab-527d-aa7e-9b94e7dff653`) lines 134-170 [crates/gwiki/src/compile/tests.rs:134-170]
  - Signature: `fn compile_fails_on_out_of_scope_accepted_note() {`
  - Purpose: Verifies that 'prepare_handoff' returns 'WikiError::InvalidInput { field: "accepted_note", .. }' when a session contains an accepted research note whose path lies outside the scope root, even if the out-of-scope file exists on disk. [crates/gwiki/src/compile/tests.rs:134-170]
- `compile_rejects_absolute_or_escaping_target_pages` (function) component `compile_rejects_absolute_or_escaping_target_pages [function]` (`4d29851b-be3b-5e20-887b-c8c6debad7b5`) lines 173-219 [crates/gwiki/src/compile/tests.rs:173-219]
  - Signature: `fn compile_rejects_absolute_or_escaping_target_pages() {`
  - Purpose: Verifies that 'prepare_handoff' rejects 'CompileRequest.target_page' values that are either absolute paths or path-traversing relative paths by returning 'WikiError::InvalidInput' for the 'target_page' field. [crates/gwiki/src/compile/tests.rs:173-219]
- `compile_rejects_target_page_through_symlinked_parent` (function) component `compile_rejects_target_page_through_symlinked_parent [function]` (`37a7864a-d0b3-523d-b9fb-2e1e9568b9dd`) lines 223-243 [crates/gwiki/src/compile/tests.rs:223-243]
  - Signature: `fn compile_rejects_target_page_through_symlinked_parent() {`
  - Purpose: Verifies that 'write_target_page' rejects a target page whose parent path traverses a symlink out of the vault by returning 'WikiError::InvalidInput' for 'target_page'. [crates/gwiki/src/compile/tests.rs:223-243]
- `compile_rejects_target_page_through_symlinked_parent` (function) component `compile_rejects_target_page_through_symlinked_parent [function]` (`f9f75b81-c9a3-5462-abca-c38ad86f24a5`) lines 247-277 [crates/gwiki/src/compile/tests.rs:247-277]
  - Signature: `fn compile_rejects_target_page_through_symlinked_parent() {`
  - Purpose: Verifies that 'write_target_page' rejects a target page whose parent directory resolves through a symlink outside the vault by returning 'WikiError::InvalidInput' for the 'target_page' field. [crates/gwiki/src/compile/tests.rs:247-277]
- `compile_writes_obsidian_markdown` (function) component `compile_writes_obsidian_markdown [function]` (`dd6a8a02-156b-5f78-9d0d-63d8fce7e208`) lines 280-349 [crates/gwiki/src/compile/tests.rs:280-349]
  - Signature: `fn compile_writes_obsidian_markdown() {`
  - Purpose: Creates a temporary project note, runs 'compile_to_wiki' for the topic '"Durable Compile"', and verifies that it emits an Obsidian-style topic markdown article with the expected frontmatter and source link, creates the corresponding source page, and records provenance metadata. [crates/gwiki/src/compile/tests.rs:280-349]
- `index_update_preserves_unrelated_entries` (function) component `index_update_preserves_unrelated_entries [function]` (`c05ce18a-4c02-59f5-918b-ddfde99d7abd`) lines 352-379 [crates/gwiki/src/compile/tests.rs:352-379]
  - Signature: `fn index_update_preserves_unrelated_entries() {`
  - Purpose: Verifies that compiling a wiki article updates '_index.md' to add the new topic entry without removing existing unrelated index links. [crates/gwiki/src/compile/tests.rs:352-379]
- `index_update_uses_structural_heading_and_link_checks` (function) component `index_update_uses_structural_heading_and_link_checks [function]` (`cadb477d-cd23-51f1-87cf-e57053166d5d`) lines 382-411 [crates/gwiki/src/compile/tests.rs:382-411]
  - Signature: `fn index_update_uses_structural_heading_and_link_checks() {`
  - Purpose: Verifies that 'update_wiki_index' normalizes an existing '## Compiled pages archive' heading to '## Compiled pages' and ensures the article link '- `[[knowledge/topics/exact|Exact]]`' appears exactly once in '_index.md'. [crates/gwiki/src/compile/tests.rs:382-411]
- `insert_compiled_page_link_creates_missing_compiled_heading` (function) component `insert_compiled_page_link_creates_missing_compiled_heading [function]` (`e4379204-bef0-5cbf-96fe-71220cab3675`) lines 414-421 [crates/gwiki/src/compile/tests.rs:414-421]
  - Signature: `fn insert_compiled_page_link_creates_missing_compiled_heading() {`
  - Purpose: Verifies that 'insert_compiled_page_link' creates a missing '## Compiled pages' section in the wiki index and inserts the given compiled page link into it. [crates/gwiki/src/compile/tests.rs:414-421]
- `write_target_page_rejects_existing_page_without_overwrite_race` (function) component `write_target_page_rejects_existing_page_without_overwrite_race [function]` (`5e03b29a-f217-568b-a090-a7db2753dc62`) lines 424-443 [crates/gwiki/src/compile/tests.rs:424-443]
  - Signature: `fn write_target_page_rejects_existing_page_without_overwrite_race() {`
  - Purpose: Verifies that 'write_target_page' rejects overwriting an already existing target page by returning 'WikiError::InvalidInput { field: "write_intent" }' and leaving the original file contents unchanged. [crates/gwiki/src/compile/tests.rs:424-443]
- `compile_explainer_generates_grounded_prose_sections` (function) component `compile_explainer_generates_grounded_prose_sections [function]` (`35f09869-be27-53b4-960a-ad6d0711ee17`) lines 446-514 [crates/gwiki/src/compile/tests.rs:446-514]
  - Signature: `fn compile_explainer_generates_grounded_prose_sections() {`
  - Purpose: Verifies that 'compile_to_wiki_with_options' generates a grounded article from accepted notes using the daemon route, emits the expected overview section with source-backed prose links, and omits degraded-mode markers. [crates/gwiki/src/compile/tests.rs:446-514]
- `compile_explainer_failure_degrades_and_keeps_structural_skeleton` (function) component `compile_explainer_failure_degrades_and_keeps_structural_skeleton [function]` (`f3fbfee6-97ae-5501-aa4c-6f281690290b`) lines 517-552 [crates/gwiki/src/compile/tests.rs:517-552]
  - Signature: `fn compile_explainer_failure_degrades_and_keeps_structural_skeleton() {`
  - Purpose: Verifies that when the explainer generator returns an error, 'compile_to_wiki_with_options' still produces a wiki article with a fallback degraded synthesis mode, preserves the structural outline skeleton, records degraded source metadata, and surfaces a failed explainer report with the original error and zero kept citations. [crates/gwiki/src/compile/tests.rs:517-552]
- `compile_without_generator_stays_structural_without_degradation` (function) component `compile_without_generator_stays_structural_without_degradation [function]` (`f91f7584-f90f-5f48-9e7a-82f94a8158b4`) lines 555-583 [crates/gwiki/src/compile/tests.rs:555-583]
  - Signature: `fn compile_without_generator_stays_structural_without_degradation() {`
  - Purpose: Compiles a wiki article from a session note with 'write_intent' disabled and asserts the output remains structurally generated using 'synthesis_mode: "fallback"' without any 'degraded:' marker, includes the requested '## Overview' section, and returns an explainer report with status 'skipped'. [crates/gwiki/src/compile/tests.rs:555-583]

