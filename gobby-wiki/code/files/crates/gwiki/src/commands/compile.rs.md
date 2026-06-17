---
title: crates/gwiki/src/commands/compile.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/compile.rs
  ranges:
  - 18-100
  - 102-110
  - 112-132
  - 134-142
  - 144-151
  - 153-167
  - 169-203
  - 205-237
  - 242-252
  - 255-257
  - 259-264
  - 266-287
  - 293-323
  - 325-332
  - 340-360
  - 362-366
  - 369-423
  - 426-458
  - 461-479
  - 482-501
  - 504-525
  - 528-538
  - 541-557
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/compile.rs:18-100](crates/gwiki/src/commands/compile.rs#L18-L100), [crates/gwiki/src/commands/compile.rs:102-110](crates/gwiki/src/commands/compile.rs#L102-L110), [crates/gwiki/src/commands/compile.rs:112-132](crates/gwiki/src/commands/compile.rs#L112-L132), [crates/gwiki/src/commands/compile.rs:134-142](crates/gwiki/src/commands/compile.rs#L134-L142), [crates/gwiki/src/commands/compile.rs:144-151](crates/gwiki/src/commands/compile.rs#L144-L151), [crates/gwiki/src/commands/compile.rs:153-167](crates/gwiki/src/commands/compile.rs#L153-L167), [crates/gwiki/src/commands/compile.rs:169-203](crates/gwiki/src/commands/compile.rs#L169-L203), [crates/gwiki/src/commands/compile.rs:205-237](crates/gwiki/src/commands/compile.rs#L205-L237), [crates/gwiki/src/commands/compile.rs:242-252](crates/gwiki/src/commands/compile.rs#L242-L252), [crates/gwiki/src/commands/compile.rs:255-257](crates/gwiki/src/commands/compile.rs#L255-L257), [crates/gwiki/src/commands/compile.rs:259-264](crates/gwiki/src/commands/compile.rs#L259-L264), [crates/gwiki/src/commands/compile.rs:266-287](crates/gwiki/src/commands/compile.rs#L266-L287), [crates/gwiki/src/commands/compile.rs:293-323](crates/gwiki/src/commands/compile.rs#L293-L323), [crates/gwiki/src/commands/compile.rs:325-332](crates/gwiki/src/commands/compile.rs#L325-L332), [crates/gwiki/src/commands/compile.rs:340-360](crates/gwiki/src/commands/compile.rs#L340-L360), [crates/gwiki/src/commands/compile.rs:362-366](crates/gwiki/src/commands/compile.rs#L362-L366), [crates/gwiki/src/commands/compile.rs:369-423](crates/gwiki/src/commands/compile.rs#L369-L423), [crates/gwiki/src/commands/compile.rs:426-458](crates/gwiki/src/commands/compile.rs#L426-L458), [crates/gwiki/src/commands/compile.rs:461-479](crates/gwiki/src/commands/compile.rs#L461-L479), [crates/gwiki/src/commands/compile.rs:482-501](crates/gwiki/src/commands/compile.rs#L482-L501), [crates/gwiki/src/commands/compile.rs:504-525](crates/gwiki/src/commands/compile.rs#L504-L525), [crates/gwiki/src/commands/compile.rs:528-538](crates/gwiki/src/commands/compile.rs#L528-L538), [crates/gwiki/src/commands/compile.rs:541-557](crates/gwiki/src/commands/compile.rs#L541-L557)

</details>

# crates/gwiki/src/commands/compile.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements the `compile` command for wiki generation. `execute` resolves the requested scope, builds or loads a compile session from an optional topic seed, applies any explicit source selections, chooses the explainer transport for AI-driven narration, and then calls `compile_to_wiki_with_options` to produce the final compile outcome. The helper functions break that flow into focused steps: topic and session resolution, source selector parsing and deduplication, source record construction and raw-source writes, explainer routing, and the specific error paths for missing or ambiguous sources and for checkpoint/session initialization when no prior compile state exists.
[crates/gwiki/src/commands/compile.rs:18-100]
[crates/gwiki/src/commands/compile.rs:102-110]
[crates/gwiki/src/commands/compile.rs:112-132]
[crates/gwiki/src/commands/compile.rs:134-142]
[crates/gwiki/src/commands/compile.rs:144-151]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(` | `execute [function]` | `831825ea-cfa2-5fab-b255-68c954ee93d8` | 18-100 [crates/gwiki/src/commands/compile.rs:18-100] | Indexed function `execute` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:18-100] |
| `compile_topic_seed` | function | `fn compile_topic_seed(` | `compile_topic_seed [function]` | `a897184a-e3db-5661-bb51-1fd1483ebf37` | 102-110 [crates/gwiki/src/commands/compile.rs:102-110] | Indexed function `compile_topic_seed` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:102-110] |
| `load_compile_session` | function | `fn load_compile_session(` | `load_compile_session [function]` | `38548bd8-8f18-56b3-971c-1845f84ab1f3` | 112-132 [crates/gwiki/src/commands/compile.rs:112-132] | Indexed function `load_compile_session` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:112-132] |
| `resolve_compile_topic` | function | `fn resolve_compile_topic(topic_seed: Option<String>, session: &session::ResearchSession) -> String {` | `resolve_compile_topic [function]` | `88d106c6-d1b8-5b36-8d54-0357070f6fc4` | 134-142 [crates/gwiki/src/commands/compile.rs:134-142] | Indexed function `resolve_compile_topic` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:134-142] |
| `apply_source_selection` | function | `fn apply_source_selection(` | `apply_source_selection [function]` | `284597a9-5aa1-5e0c-8828-2faf90cf5248` | 144-151 [crates/gwiki/src/commands/compile.rs:144-151] | Indexed function `apply_source_selection` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:144-151] |
| `resolve_source_notes` | function | `fn resolve_source_notes(` | `resolve_source_notes [function]` | `3f438980-0b66-5818-ba0c-eeaa63fcf8c9` | 153-167 [crates/gwiki/src/commands/compile.rs:153-167] | Indexed function `resolve_source_notes` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:153-167] |
| `resolve_source_selector` | function | `fn resolve_source_selector<'a>(` | `resolve_source_selector [function]` | `294aa713-3090-52b8-b853-e0dbe3cf6e7d` | 169-203 [crates/gwiki/src/commands/compile.rs:169-203] | Indexed function `resolve_source_selector` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:169-203] |
| `accepted_note_from_source` | function | `fn accepted_note_from_source(` | `accepted_note_from_source [function]` | `58876afd-b532-5f90-a686-bb255cce4793` | 205-237 [crates/gwiki/src/commands/compile.rs:205-237] | Indexed function `accepted_note_from_source` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:205-237] |
| `ExplainerTransport` | type | `enum ExplainerTransport {` | `ExplainerTransport [type]` | `17dd195a-523a-50e3-b25f-ca1c0e008138` | 242-252 [crates/gwiki/src/commands/compile.rs:242-252] | Indexed type `ExplainerTransport` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:242-252] |
| `ExplainerTransport::is_active` | method | `fn is_active(&self) -> bool {` | `ExplainerTransport::is_active [method]` | `7c2b4fda-1d3d-59fe-86c3-58e0a65709c6` | 255-257 [crates/gwiki/src/commands/compile.rs:255-257] | Indexed method `ExplainerTransport::is_active` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:255-257] |
| `ExplainerTransport::route_label` | method | `fn route_label(&self) -> &'static str {` | `ExplainerTransport::route_label [method]` | `5a4ca3fc-fc89-51a1-ad00-5e815e65dee0` | 259-264 [crates/gwiki/src/commands/compile.rs:259-264] | Indexed method `ExplainerTransport::route_label` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:259-264] |
| `ExplainerTransport::generate` | method | `fn generate(&self, prompt: &ExplainerPrompt) -> Result<ExplainerResponse, String> {` | `ExplainerTransport::generate [method]` | `fefc525b-f85a-5e2c-a72e-92ed6bfcd1df` | 266-287 [crates/gwiki/src/commands/compile.rs:266-287] | Indexed method `ExplainerTransport::generate` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:266-287] |
| `resolve_explainer_transport` | function | `fn resolve_explainer_transport(requested: AiRouting) -> ExplainerTransport {` | `resolve_explainer_transport [function]` | `b4f41ccf-6169-5249-8389-820d9a09c7d4` | 293-323 [crates/gwiki/src/commands/compile.rs:293-323] | Indexed function `resolve_explainer_transport` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:293-323] |
| `routing_label` | function | `fn routing_label(route: AiRouting) -> &'static str {` | `routing_label [function]` | `080cbcd4-7fa9-5953-afdd-3acce0d1034f` | 325-332 [crates/gwiki/src/commands/compile.rs:325-332] | Indexed function `routing_label` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:325-332] |
| `source_record` | function | `fn source_record(` | `source_record [function]` | `796f2c65-1b95-5c3b-8eff-1df8664553aa` | 340-360 [crates/gwiki/src/commands/compile.rs:340-360] | Indexed function `source_record` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:340-360] |
| `write_raw_source` | function | `fn write_raw_source(root: &Path, record: &SourceRecord) {` | `write_raw_source [function]` | `cfffe95f-7481-551c-992f-fec0fc592d99` | 362-366 [crates/gwiki/src/commands/compile.rs:362-366] | Indexed function `write_raw_source` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:362-366] |
| `source_selectors_resolve_id_raw_path_location_and_canonical_location` | function | `fn source_selectors_resolve_id_raw_path_location_and_canonical_location() {` | `source_selectors_resolve_id_raw_path_location_and_canonical_location [function]` | `b10f95d1-c7da-5b10-aa18-1ad617148cd4` | 369-423 [crates/gwiki/src/commands/compile.rs:369-423] | Indexed function `source_selectors_resolve_id_raw_path_location_and_canonical_location` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:369-423] |
| `source_selection_dedupes_by_source_id_in_selector_order` | function | `fn source_selection_dedupes_by_source_id_in_selector_order() {` | `source_selection_dedupes_by_source_id_in_selector_order [function]` | `d7ae7ce9-64f7-5345-8a2f-7b6ce1f5258b` | 426-458 [crates/gwiki/src/commands/compile.rs:426-458] | Indexed function `source_selection_dedupes_by_source_id_in_selector_order` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:426-458] |
| `missing_source_selector_reports_source_not_found` | function | `fn missing_source_selector_reports_source_not_found() {` | `missing_source_selector_reports_source_not_found [function]` | `adcca1e0-01f7-517c-a7fb-2ae68a83849f` | 461-479 [crates/gwiki/src/commands/compile.rs:461-479] | Indexed function `missing_source_selector_reports_source_not_found` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:461-479] |
| `ambiguous_non_id_selector_reports_invalid_input` | function | `fn ambiguous_non_id_selector_reports_invalid_input() {` | `ambiguous_non_id_selector_reports_invalid_input [function]` | `396b2484-b909-50f6-9085-983088b0b9d0` | 482-501 [crates/gwiki/src/commands/compile.rs:482-501] | Indexed function `ambiguous_non_id_selector_reports_invalid_input` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:482-501] |
| `missing_raw_file_for_selected_source_reports_raw_source_not_found` | function | `fn missing_raw_file_for_selected_source_reports_raw_source_not_found() {` | `missing_raw_file_for_selected_source_reports_raw_source_not_found [function]` | `2290db0f-ad2a-5bac-9664-a8a9cca9c564` | 504-525 [crates/gwiki/src/commands/compile.rs:504-525] | Indexed function `missing_raw_file_for_selected_source_reports_raw_source_not_found` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:504-525] |
| `missing_checkpoint_with_topic_seed_creates_fresh_compile_session` | function | `fn missing_checkpoint_with_topic_seed_creates_fresh_compile_session() {` | `missing_checkpoint_with_topic_seed_creates_fresh_compile_session [function]` | `25b24946-a87d-5f02-a56a-437dd93a9629` | 528-538 [crates/gwiki/src/commands/compile.rs:528-538] | Indexed function `missing_checkpoint_with_topic_seed_creates_fresh_compile_session` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:528-538] |
| `missing_checkpoint_without_topic_seed_requires_topic` | function | `fn missing_checkpoint_without_topic_seed_requires_topic() {` | `missing_checkpoint_without_topic_seed_requires_topic [function]` | `e17fd907-7348-5b0f-826f-f7c18f984a72` | 541-557 [crates/gwiki/src/commands/compile.rs:541-557] | Indexed function `missing_checkpoint_without_topic_seed_requires_topic` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:541-557] |
