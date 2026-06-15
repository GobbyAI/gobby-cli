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
  - 254-288
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

# crates/gwiki/src/commands/compile.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

This file implements the `compile` command for `gwiki`. It resolves the command scope, derives or loads a research session, optionally applies source selections, and determines the final compile topic before calling `wiki_compile::compile_to_wiki_with_options` to build the wiki article outcome. It also wires in an `ExplainerTransport` that routes AI explainer prompts through daemon or text-generation backends when available, and then prepares the command’s JSON status payload. The helper functions handle topic seeding and fallback, session checkpoint loading, source selector resolution and deduplication, raw-source validation and persistence, and AI routing label/transport resolution; the tests cover those resolution and error cases.
[crates/gwiki/src/commands/compile.rs:18-100]
[crates/gwiki/src/commands/compile.rs:102-110]
[crates/gwiki/src/commands/compile.rs:112-132]
[crates/gwiki/src/commands/compile.rs:134-142]
[crates/gwiki/src/commands/compile.rs:144-151]

## API Symbols

- `execute` (function) component `execute [function]` (`831825ea-cfa2-5fab-b255-68c954ee93d8`) lines 18-100 [crates/gwiki/src/commands/compile.rs:18-100]
  - Signature: `pub(crate) fn execute(`
  - Purpose: 'execute' resolves the command scope, loads and optionally filters a research session, determines the compile topic, probes daemon synthesis support, optionally wires in an explainer generator, invokes 'wiki_compile::compile_to_wiki_with_options' to produce the wiki article outcome, and then prepares a JSON status payload for the compile command. [crates/gwiki/src/commands/compile.rs:18-100]
- `compile_topic_seed` (function) component `compile_topic_seed [function]` (`a897184a-e3db-5661-bb51-1fd1483ebf37`) lines 102-110 [crates/gwiki/src/commands/compile.rs:102-110]
  - Signature: `fn compile_topic_seed(`
  - Purpose: Returns the provided 'topic' as an owned 'String', or if 'topic' is 'None' and 'research_scope' is 'ResearchScope::Topic', returns a clone of that scope’s 'name'; otherwise returns 'None'. [crates/gwiki/src/commands/compile.rs:102-110]
- `load_compile_session` (function) component `load_compile_session [function]` (`38548bd8-8f18-56b3-971c-1845f84ab1f3`) lines 112-132 [crates/gwiki/src/commands/compile.rs:112-132]
  - Signature: `fn load_compile_session(`
  - Purpose: Loads an existing research session checkpoint or creates a new 'ResearchSession' using the provided topic seed if no checkpoint exists, otherwise returns a 'WikiError'. [crates/gwiki/src/commands/compile.rs:112-132]
- `resolve_compile_topic` (function) component `resolve_compile_topic [function]` (`88d106c6-d1b8-5b36-8d54-0357070f6fc4`) lines 134-142 [crates/gwiki/src/commands/compile.rs:134-142]
  - Signature: `fn resolve_compile_topic(topic_seed: Option<String>, session: &session::ResearchSession) -> String {`
  - Purpose: Resolves a compile topic string using a cascading fallback strategy: returns the provided 'topic_seed' if 'Some', otherwise the topic from 'session.compile_state' if present, else the 'session.question'. [crates/gwiki/src/commands/compile.rs:134-142]
- `apply_source_selection` (function) component `apply_source_selection [function]` (`284597a9-5aa1-5e0c-8828-2faf90cf5248`) lines 144-151 [crates/gwiki/src/commands/compile.rs:144-151]
  - Signature: `fn apply_source_selection(`
  - Purpose: This function resolves source notes from a manifest based on provided selector strings, populates the research session's accepted notes with the results, and persists the session state via checkpoint. [crates/gwiki/src/commands/compile.rs:144-151]
- `resolve_source_notes` (function) component `resolve_source_notes [function]` (`3f438980-0b66-5818-ba0c-eeaa63fcf8c9`) lines 153-167 [crates/gwiki/src/commands/compile.rs:153-167]
  - Signature: `fn resolve_source_notes(`
  - Purpose: # Summary Resolves an array of selector strings against a source manifest, deduplicates the resulting records by ID, and converts them to 'AcceptedResearchNote' objects. [crates/gwiki/src/commands/compile.rs:153-167]
- `resolve_source_selector` (function) component `resolve_source_selector [function]` (`294aa713-3090-52b8-b853-e0dbe3cf6e7d`) lines 169-203 [crates/gwiki/src/commands/compile.rs:169-203]
  - Signature: `fn resolve_source_selector<'a>(`
  - Purpose: This function resolves a source selector string to a matching 'SourceRecord' reference from a 'SourceManifest' using cascading strategies (direct ID match, filesystem path match, then location match), returning an error if no match is found or if multiple matches are ambiguous. [crates/gwiki/src/commands/compile.rs:169-203]
- `accepted_note_from_source` (function) component `accepted_note_from_source [function]` (`58876afd-b532-5f90-a686-bb255cce4793`) lines 205-237 [crates/gwiki/src/commands/compile.rs:205-237]
  - Signature: `fn accepted_note_from_source(`
  - Purpose: This function validates that a raw source file exists for a given SourceRecord and returns an AcceptedResearchNote containing the record's title and path, or a WikiError if the file is not found or inaccessible. [crates/gwiki/src/commands/compile.rs:205-237]
- `ExplainerTransport` (type) component `ExplainerTransport [type]` (`17dd195a-523a-50e3-b25f-ca1c0e008138`) lines 242-252 [crates/gwiki/src/commands/compile.rs:242-252]
  - Signature: `enum ExplainerTransport {`
  - Purpose: Indexed type `ExplainerTransport` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:242-252]
- `ExplainerTransport` (class) component `ExplainerTransport [class]` (`e5dea59f-0c6e-5c51-b292-bea8a582cd3c`) lines 254-288 [crates/gwiki/src/commands/compile.rs:254-288]
  - Signature: `impl ExplainerTransport {`
  - Purpose: # Summary 'ExplainerTransport' implements stateful routing and generation of AI-synthesized responses, dispatching prompts to either a daemon or text-based backend with configuration-dependent error handling for Off, Unresolved, and Resolved states. [crates/gwiki/src/commands/compile.rs:254-288]
- `ExplainerTransport.is_active` (method) component `ExplainerTransport.is_active [method]` (`7c2b4fda-1d3d-59fe-86c3-58e0a65709c6`) lines 255-257 [crates/gwiki/src/commands/compile.rs:255-257]
  - Signature: `fn is_active(&self) -> bool {`
  - Purpose: Returns 'true' if the enum variant is not 'Self::Off', and 'false' otherwise. [crates/gwiki/src/commands/compile.rs:255-257]
- `ExplainerTransport.route_label` (method) component `ExplainerTransport.route_label [method]` (`5a4ca3fc-fc89-51a1-ad00-5e815e65dee0`) lines 259-264 [crates/gwiki/src/commands/compile.rs:259-264]
  - Signature: `fn route_label(&self) -> &'static str {`
  - Purpose: Returns a static string route label by returning '"off"' for the 'Off' variant or delegating to 'routing_label()' for 'Unresolved' and 'Resolved' variants containing a route field. [crates/gwiki/src/commands/compile.rs:259-264]
- `ExplainerTransport.generate` (method) component `ExplainerTransport.generate [method]` (`fefc525b-f85a-5e2c-a72e-92ed6bfcd1df`) lines 266-287 [crates/gwiki/src/commands/compile.rs:266-287]
  - Signature: `fn generate(&self, prompt: &ExplainerPrompt) -> Result<ExplainerResponse, String> {`
  - Purpose: Routes an 'ExplainerPrompt' to either a daemon or text generation service based on internal 'AiRouting' state, returning a synthesized 'ExplainerResponse' or an error string. [crates/gwiki/src/commands/compile.rs:266-287]
- `resolve_explainer_transport` (function) component `resolve_explainer_transport [function]` (`b4f41ccf-6169-5249-8389-820d9a09c7d4`) lines 293-323 [crates/gwiki/src/commands/compile.rs:293-323]
  - Signature: `fn resolve_explainer_transport(requested: AiRouting) -> ExplainerTransport {`
  - Purpose: Resolves an AI text-generation transport by loading hub configuration, validating the requested routing against the effective route for the TextGenerate capability, and returning a resolved context, unresolved error state, or Off. [crates/gwiki/src/commands/compile.rs:293-323]
- `routing_label` (function) component `routing_label [function]` (`080cbcd4-7fa9-5953-afdd-3acce0d1034f`) lines 325-332 [crates/gwiki/src/commands/compile.rs:325-332]
  - Signature: `fn routing_label(route: AiRouting) -> &'static str {`
  - Purpose: This function maps an 'AiRouting' enum variant to its corresponding static string label via pattern matching. [crates/gwiki/src/commands/compile.rs:325-332]
- `source_record` (function) component `source_record [function]` (`796f2c65-1b95-5c3b-8eff-1df8664553aa`) lines 340-360 [crates/gwiki/src/commands/compile.rs:340-360]
  - Signature: `fn source_record(`
  - Purpose: Constructs a SourceRecord from identifier, location, and optional title parameters, hardcoding markdown kind, a fixed fetch timestamp, and pending compilation status. [crates/gwiki/src/commands/compile.rs:340-360]
- `write_raw_source` (function) component `write_raw_source [function]` (`cfffe95f-7481-551c-992f-fec0fc592d99`) lines 362-366 [crates/gwiki/src/commands/compile.rs:362-366]
  - Signature: `fn write_raw_source(root: &Path, record: &SourceRecord) {`
  - Purpose: Constructs a filesystem path from the root and record ID, creates all necessary parent directories, and writes a markdown-formatted record ID header to the resulting file. [crates/gwiki/src/commands/compile.rs:362-366]
- `source_selectors_resolve_id_raw_path_location_and_canonical_location` (function) component `source_selectors_resolve_id_raw_path_location_and_canonical_location [function]` (`b10f95d1-c7da-5b10-aa18-1ad617148cd4`) lines 369-423 [crates/gwiki/src/commands/compile.rs:369-423]
  - Signature: `fn source_selectors_resolve_id_raw_path_location_and_canonical_location() {`
  - Purpose: This test verifies that the source note resolution system correctly resolves multiple reference formats (source IDs, raw file paths, filenames, and canonical locations) to their corresponding raw paths and titles. [crates/gwiki/src/commands/compile.rs:369-423]
- `source_selection_dedupes_by_source_id_in_selector_order` (function) component `source_selection_dedupes_by_source_id_in_selector_order [function]` (`d7ae7ce9-64f7-5345-8a2f-7b6ce1f5258b`) lines 426-458 [crates/gwiki/src/commands/compile.rs:426-458]
  - Signature: `fn source_selection_dedupes_by_source_id_in_selector_order() {`
  - Purpose: This function verifies that 'resolve_source_notes' deduplicates sources by source identifier while preserving the order of first occurrence in the selector list. [crates/gwiki/src/commands/compile.rs:426-458]
- `missing_source_selector_reports_source_not_found` (function) component `missing_source_selector_reports_source_not_found [function]` (`adcca1e0-01f7-517c-a7fb-2ae68a83849f`) lines 461-479 [crates/gwiki/src/commands/compile.rs:461-479]
  - Signature: `fn missing_source_selector_reports_source_not_found() {`
  - Purpose: This test function verifies that 'resolve_source_selector' returns a 'WikiError::NotFound' error with resource="source" when attempting to resolve a non-existent source identifier against a manifest. [crates/gwiki/src/commands/compile.rs:461-479]
- `ambiguous_non_id_selector_reports_invalid_input` (function) component `ambiguous_non_id_selector_reports_invalid_input [function]` (`396b2484-b909-50f6-9085-983088b0b9d0`) lines 482-501 [crates/gwiki/src/commands/compile.rs:482-501]
  - Signature: `fn ambiguous_non_id_selector_reports_invalid_input() {`
  - Purpose: This test verifies that resolving an ambiguous non-ID source selector against a manifest containing multiple matching records produces an 'InvalidInput' error with the field "source" and a message instructing the user to provide a source ID. [crates/gwiki/src/commands/compile.rs:482-501]
- `missing_raw_file_for_selected_source_reports_raw_source_not_found` (function) component `missing_raw_file_for_selected_source_reports_raw_source_not_found [function]` (`2290db0f-ad2a-5bac-9664-a8a9cca9c564`) lines 504-525 [crates/gwiki/src/commands/compile.rs:504-525]
  - Signature: `fn missing_raw_file_for_selected_source_reports_raw_source_not_found() {`
  - Purpose: This unit test verifies that 'resolve_source_notes()' returns a 'WikiError::NotFound' with resource type "raw_source" and file ID "raw/src-alpha.md" when the raw source file is missing for a selected source. [crates/gwiki/src/commands/compile.rs:504-525]
- `missing_checkpoint_with_topic_seed_creates_fresh_compile_session` (function) component `missing_checkpoint_with_topic_seed_creates_fresh_compile_session [function]` (`25b24946-a87d-5f02-a56a-437dd93a9629`) lines 528-538 [crates/gwiki/src/commands/compile.rs:528-538]
  - Signature: `fn missing_checkpoint_with_topic_seed_creates_fresh_compile_session() {`
  - Purpose: This unit test verifies that 'load_compile_session()' with a topic seed and no checkpoint creates a fresh 'CompileSession' with the seed as the 'question' field, an empty 'accepted_notes' collection, and the correct 'ResearchScope' root. [crates/gwiki/src/commands/compile.rs:528-538]
- `missing_checkpoint_without_topic_seed_requires_topic` (function) component `missing_checkpoint_without_topic_seed_requires_topic [function]` (`e17fd907-7348-5b0f-826f-f7c18f984a72`) lines 541-557 [crates/gwiki/src/commands/compile.rs:541-557]
  - Signature: `fn missing_checkpoint_without_topic_seed_requires_topic() {`
  - Purpose: This test function verifies that 'load_compile_session' fails with a 'WikiError::InvalidInput' for the "topic" field when invoked without a topic argument and no existing research checkpoint. [crates/gwiki/src/commands/compile.rs:541-557]

