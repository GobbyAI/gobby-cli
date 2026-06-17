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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/compile/tests.rs:7-25](crates/gwiki/src/compile/tests.rs#L7-L25), [crates/gwiki/src/compile/tests.rs:28-72](crates/gwiki/src/compile/tests.rs#L28-L72), [crates/gwiki/src/compile/tests.rs:75-102](crates/gwiki/src/compile/tests.rs#L75-L102), [crates/gwiki/src/compile/tests.rs:105-131](crates/gwiki/src/compile/tests.rs#L105-L131), [crates/gwiki/src/compile/tests.rs:134-170](crates/gwiki/src/compile/tests.rs#L134-L170), [crates/gwiki/src/compile/tests.rs:173-219](crates/gwiki/src/compile/tests.rs#L173-L219), [crates/gwiki/src/compile/tests.rs:223-243](crates/gwiki/src/compile/tests.rs#L223-L243), [crates/gwiki/src/compile/tests.rs:247-277](crates/gwiki/src/compile/tests.rs#L247-L277), [crates/gwiki/src/compile/tests.rs:280-349](crates/gwiki/src/compile/tests.rs#L280-L349), [crates/gwiki/src/compile/tests.rs:352-379](crates/gwiki/src/compile/tests.rs#L352-L379), [crates/gwiki/src/compile/tests.rs:382-411](crates/gwiki/src/compile/tests.rs#L382-L411), [crates/gwiki/src/compile/tests.rs:414-421](crates/gwiki/src/compile/tests.rs#L414-L421), [crates/gwiki/src/compile/tests.rs:424-443](crates/gwiki/src/compile/tests.rs#L424-L443), [crates/gwiki/src/compile/tests.rs:446-514](crates/gwiki/src/compile/tests.rs#L446-L514), [crates/gwiki/src/compile/tests.rs:517-552](crates/gwiki/src/compile/tests.rs#L517-L552), [crates/gwiki/src/compile/tests.rs:555-583](crates/gwiki/src/compile/tests.rs#L555-L583)

</details>

# crates/gwiki/src/compile/tests.rs

Module: [[code/modules/crates/gwiki/src/compile|crates/gwiki/src/compile]]

## Purpose

This file is a compile test suite for `gwiki` that exercises handoff preparation, target-page safety, markdown writing, index updates, and explainer generation. A small `session_with_note` helper builds a `ResearchSession` with one accepted note, and the tests use it to verify that compile bundles include required sections, remain non-destructive by default, reject out-of-scope or escaping targets and symlinked paths, preserve unrelated index entries, create missing compiled headings, enforce overwrite races, and either generate grounded prose or fall back to a structural skeleton when explainer generation is unavailable.
[crates/gwiki/src/compile/tests.rs:7-25]
[crates/gwiki/src/compile/tests.rs:28-72]
[crates/gwiki/src/compile/tests.rs:75-102]
[crates/gwiki/src/compile/tests.rs:105-131]
[crates/gwiki/src/compile/tests.rs:134-170]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `session_with_note` | function | `fn session_with_note(scope: &ResearchScope, title: &str, relative_path: &str) -> ResearchSession {` | `session_with_note [function]` | `3e2a0d2e-acba-52ef-a278-4615cf9b68ec` | 7-25 [crates/gwiki/src/compile/tests.rs:7-25] | Indexed function `session_with_note` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:7-25] |
| `compile_bundle_contains_required_sections` | function | `fn compile_bundle_contains_required_sections() {` | `compile_bundle_contains_required_sections [function]` | `5ce1504f-2807-58f0-999d-3b92fe5ba5b5` | 28-72 [crates/gwiki/src/compile/tests.rs:28-72] | Indexed function `compile_bundle_contains_required_sections` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:28-72] |
| `compile_handoff_is_non_destructive_by_default` | function | `fn compile_handoff_is_non_destructive_by_default() {` | `compile_handoff_is_non_destructive_by_default [function]` | `7eeebf91-8b12-5be1-9ec1-8c0f6e2eccc6` | 75-102 [crates/gwiki/src/compile/tests.rs:75-102] | Indexed function `compile_handoff_is_non_destructive_by_default` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:75-102] |
| `prepare_handoff_does_not_write_target_page` | function | `fn prepare_handoff_does_not_write_target_page() {` | `prepare_handoff_does_not_write_target_page [function]` | `40448d26-2ef7-5649-886b-efc9cf8d17a9` | 105-131 [crates/gwiki/src/compile/tests.rs:105-131] | Indexed function `prepare_handoff_does_not_write_target_page` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:105-131] |
| `compile_fails_on_out_of_scope_accepted_note` | function | `fn compile_fails_on_out_of_scope_accepted_note() {` | `compile_fails_on_out_of_scope_accepted_note [function]` | `fc4c6394-28ab-527d-aa7e-9b94e7dff653` | 134-170 [crates/gwiki/src/compile/tests.rs:134-170] | Indexed function `compile_fails_on_out_of_scope_accepted_note` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:134-170] |
| `compile_rejects_absolute_or_escaping_target_pages` | function | `fn compile_rejects_absolute_or_escaping_target_pages() {` | `compile_rejects_absolute_or_escaping_target_pages [function]` | `4d29851b-be3b-5e20-887b-c8c6debad7b5` | 173-219 [crates/gwiki/src/compile/tests.rs:173-219] | Indexed function `compile_rejects_absolute_or_escaping_target_pages` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:173-219] |
| `compile_rejects_target_page_through_symlinked_parent` | function | `fn compile_rejects_target_page_through_symlinked_parent() {` | `compile_rejects_target_page_through_symlinked_parent [function]` | `37a7864a-d0b3-523d-b9fb-2e1e9568b9dd` | 223-243 [crates/gwiki/src/compile/tests.rs:223-243] | Indexed function `compile_rejects_target_page_through_symlinked_parent` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:223-243] |
| `compile_rejects_target_page_through_symlinked_parent` | function | `fn compile_rejects_target_page_through_symlinked_parent() {` | `compile_rejects_target_page_through_symlinked_parent [function]` | `f9f75b81-c9a3-5462-abca-c38ad86f24a5` | 247-277 [crates/gwiki/src/compile/tests.rs:247-277] | Indexed function `compile_rejects_target_page_through_symlinked_parent` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:247-277] |
| `compile_writes_obsidian_markdown` | function | `fn compile_writes_obsidian_markdown() {` | `compile_writes_obsidian_markdown [function]` | `dd6a8a02-156b-5f78-9d0d-63d8fce7e208` | 280-349 [crates/gwiki/src/compile/tests.rs:280-349] | Indexed function `compile_writes_obsidian_markdown` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:280-349] |
| `index_update_preserves_unrelated_entries` | function | `fn index_update_preserves_unrelated_entries() {` | `index_update_preserves_unrelated_entries [function]` | `c05ce18a-4c02-59f5-918b-ddfde99d7abd` | 352-379 [crates/gwiki/src/compile/tests.rs:352-379] | Indexed function `index_update_preserves_unrelated_entries` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:352-379] |
| `index_update_uses_structural_heading_and_link_checks` | function | `fn index_update_uses_structural_heading_and_link_checks() {` | `index_update_uses_structural_heading_and_link_checks [function]` | `cadb477d-cd23-51f1-87cf-e57053166d5d` | 382-411 [crates/gwiki/src/compile/tests.rs:382-411] | Indexed function `index_update_uses_structural_heading_and_link_checks` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:382-411] |
| `insert_compiled_page_link_creates_missing_compiled_heading` | function | `fn insert_compiled_page_link_creates_missing_compiled_heading() {` | `insert_compiled_page_link_creates_missing_compiled_heading [function]` | `e4379204-bef0-5cbf-96fe-71220cab3675` | 414-421 [crates/gwiki/src/compile/tests.rs:414-421] | Indexed function `insert_compiled_page_link_creates_missing_compiled_heading` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:414-421] |
| `write_target_page_rejects_existing_page_without_overwrite_race` | function | `fn write_target_page_rejects_existing_page_without_overwrite_race() {` | `write_target_page_rejects_existing_page_without_overwrite_race [function]` | `5e03b29a-f217-568b-a090-a7db2753dc62` | 424-443 [crates/gwiki/src/compile/tests.rs:424-443] | Indexed function `write_target_page_rejects_existing_page_without_overwrite_race` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:424-443] |
| `compile_explainer_generates_grounded_prose_sections` | function | `fn compile_explainer_generates_grounded_prose_sections() {` | `compile_explainer_generates_grounded_prose_sections [function]` | `35f09869-be27-53b4-960a-ad6d0711ee17` | 446-514 [crates/gwiki/src/compile/tests.rs:446-514] | Indexed function `compile_explainer_generates_grounded_prose_sections` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:446-514] |
| `compile_explainer_failure_degrades_and_keeps_structural_skeleton` | function | `fn compile_explainer_failure_degrades_and_keeps_structural_skeleton() {` | `compile_explainer_failure_degrades_and_keeps_structural_skeleton [function]` | `f3fbfee6-97ae-5501-aa4c-6f281690290b` | 517-552 [crates/gwiki/src/compile/tests.rs:517-552] | Indexed function `compile_explainer_failure_degrades_and_keeps_structural_skeleton` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:517-552] |
| `compile_without_generator_stays_structural_without_degradation` | function | `fn compile_without_generator_stays_structural_without_degradation() {` | `compile_without_generator_stays_structural_without_degradation [function]` | `f91f7584-f90f-5f48-9e7a-82f94a8158b4` | 555-583 [crates/gwiki/src/compile/tests.rs:555-583] | Indexed function `compile_without_generator_stays_structural_without_degradation` in `crates/gwiki/src/compile/tests.rs`. [crates/gwiki/src/compile/tests.rs:555-583] |
