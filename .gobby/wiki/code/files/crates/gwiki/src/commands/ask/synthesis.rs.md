---
title: crates/gwiki/src/commands/ask/synthesis.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/ask/synthesis.rs
  ranges:
  - 15-45
  - 47-60
  - 62-75
  - 77-111
  - 113-145
  - 147-149
  - 151-158
  - 171-217
  - 220-245
  - 248-254
  - 257-277
  - 280-303
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/ask/synthesis.rs

Module: [[code/modules/crates/gwiki/src/commands/ask|crates/gwiki/src/commands/ask]]

## Purpose

Implements the ask-command synthesis stage: it resolves the effective AI route from hub config, initializes `AskOutput.ai` as a pending request, then either generates a response through the direct text endpoint or the daemon path, or records AI as unavailable when routing is `Auto`/`Off` or generation fails. The helper functions normalize and store the final synthesis, strip leading model narration, run citation checks against retrieved evidence, and downgrade or error out when AI is unavailable, while the included tests verify grounded-answer enforcement, unsupported-claim flagging, narration stripping, system-prompt wording, and degraded-output handling.
[crates/gwiki/src/commands/ask/synthesis.rs:15-45]
[crates/gwiki/src/commands/ask/synthesis.rs:47-60]
[crates/gwiki/src/commands/ask/synthesis.rs:62-75]
[crates/gwiki/src/commands/ask/synthesis.rs:77-111]
[crates/gwiki/src/commands/ask/synthesis.rs:113-145]

## API Symbols

- `synthesize` (function) component `synthesize [function]` (`fd5e87a1-c0cb-52d6-9843-ca5ab53b4627`) lines 15-45 [crates/gwiki/src/commands/ask/synthesis.rs:15-45]
  - Signature: `pub(super) fn synthesize(`
  - Purpose: Resolves AI routing from hub config and the requested mode, initializes 'output.ai' as a pending/unavailable request record, then dispatches to direct or daemon generation based on the effective route, or marks AI unavailable for 'Auto'/'Off'. [crates/gwiki/src/commands/ask/synthesis.rs:15-45]
- `generate_direct` (function) component `generate_direct [function]` (`c99eb5b8-46e9-5d7f-ae1a-45f2fb281090`) lines 47-60 [crates/gwiki/src/commands/ask/synthesis.rs:47-60]
  - Signature: `fn generate_direct(`
  - Purpose: Calls 'text::generate_text' with the plan prompt and synthesis system, records the resulting direct synthesis into 'output' on success, and otherwise marks AI as unavailable based on 'require_ai'. [crates/gwiki/src/commands/ask/synthesis.rs:47-60]
- `generate_daemon` (function) component `generate_daemon [function]` (`5be2b4f6-cb79-5252-a678-9e84c4bd476f`) lines 62-75 [crates/gwiki/src/commands/ask/synthesis.rs:62-75]
  - Signature: `fn generate_daemon(`
  - Purpose: Calls 'daemon::generate_via_daemon' with the plan prompt and synthesis system, records the returned text/model into 'output' on success, and otherwise marks AI as unavailable based on the error and 'require_ai'. [crates/gwiki/src/commands/ask/synthesis.rs:62-75]
- `record_synthesis` (function) component `record_synthesis [function]` (`20699db2-0f81-5bd7-ac75-99f831d74be1`) lines 77-111 [crates/gwiki/src/commands/ask/synthesis.rs:77-111]
  - Signature: `pub(super) fn record_synthesis(`
  - Purpose: 'record_synthesis' normalizes the synthesized answer, marks the 'AskOutput' as answered with available AI metadata, runs citation validation against the retrieved evidence, appends warnings for any unsupported claims, and stores the final synthesis payload with the answer, model, and citation check. [crates/gwiki/src/commands/ask/synthesis.rs:77-111]
- `mark_ai_unavailable` (function) component `mark_ai_unavailable [function]` (`a1647851-0d94-5e8d-b03c-3a886728617a`) lines 113-145 [crates/gwiki/src/commands/ask/synthesis.rs:113-145]
  - Signature: `fn mark_ai_unavailable(`
  - Purpose: Sets 'AskOutput' to a degraded partial state when AI is unavailable by recording a model-provider warning/error and, if 'require_ai' is true, instead returns a 'WikiError::Config' with the provided or default message. [crates/gwiki/src/commands/ask/synthesis.rs:113-145]
- `synthesis_system` (function) component `synthesis_system [function]` (`3e93e0e3-f139-5a92-b4ac-3b749a665786`) lines 147-149 [crates/gwiki/src/commands/ask/synthesis.rs:147-149]
  - Signature: `fn synthesis_system() -> &'static str {`
  - Purpose: Returns a static system-prompt string instructing the model to answer using only provided evidence excerpts and code citations, output only the final answer, stay concise, and state when evidence is insufficient. [crates/gwiki/src/commands/ask/synthesis.rs:147-149]
- `routing_label` (function) component `routing_label [function]` (`f094fb17-a2a5-537e-929f-a2a0cb328f5d`) lines 151-158 [crates/gwiki/src/commands/ask/synthesis.rs:151-158]
  - Signature: `fn routing_label(route: AiRouting) -> &'static str {`
  - Purpose: Returns the static string label for an 'AiRouting' variant, mapping 'Auto' to '"auto"', 'Daemon' to '"daemon"', 'Direct' to '"direct"', and 'Off' to '"off"'. [crates/gwiki/src/commands/ask/synthesis.rs:151-158]
- `synthesis_with_ungrounded_claim_is_flagged_in_json` (function) component `synthesis_with_ungrounded_claim_is_flagged_in_json [function]` (`f08657da-76fe-5250-89f7-3950266dc0c6`) lines 171-217 [crates/gwiki/src/commands/ask/synthesis.rs:171-217]
  - Signature: `fn synthesis_with_ungrounded_claim_is_flagged_in_json() {`
  - Purpose: Verifies that a synthesized response containing one unsupported claim is marked 'unsupported_claims', records the unsupported statement in 'citation_check.unsupported_claims', emits a warning, and preserves those fields in the serialized JSON output. [crates/gwiki/src/commands/ask/synthesis.rs:171-217]
- `synthesis_strips_leading_model_narration_before_recording` (function) component `synthesis_strips_leading_model_narration_before_recording [function]` (`51911b4b-c75a-56e8-a19a-48909a159ebe`) lines 220-245 [crates/gwiki/src/commands/ask/synthesis.rs:220-245]
  - Signature: `fn synthesis_strips_leading_model_narration_before_recording() {`
  - Purpose: Verifies that 'record_synthesis' removes leading model narration from the synthesized answer before recording it, preserving only the substantive claim and yielding a supported citation check with no warnings. [crates/gwiki/src/commands/ask/synthesis.rs:220-245]
- `synthesis_system_requests_answer_only_output` (function) component `synthesis_system_requests_answer_only_output [function]` (`aa51a0a7-cc99-555d-babc-d8301a21c709`) lines 248-254 [crates/gwiki/src/commands/ask/synthesis.rs:248-254]
  - Signature: `fn synthesis_system_requests_answer_only_output() {`
  - Purpose: Verifies that 'synthesis_system()' returns a system prompt containing the phrases “Write only the final answer,” “do not describe your process,” and “retrieval steps.” [crates/gwiki/src/commands/ask/synthesis.rs:248-254]
- `synthesis_grounded_in_hits_passes_citation_check` (function) component `synthesis_grounded_in_hits_passes_citation_check [function]` (`24e6d087-3056-5596-a4c5-950563fac45f`) lines 257-277 [crates/gwiki/src/commands/ask/synthesis.rs:257-277]
  - Signature: `fn synthesis_grounded_in_hits_passes_citation_check() {`
  - Purpose: Creates a retrieval-backed output synthesis, records a daemon synthesis with one thin-evidence claim, and asserts the citation check marks the claim as supported with no unsupported claims or warnings. [crates/gwiki/src/commands/ask/synthesis.rs:257-277]
- `ask_model_unavailable_marks_degraded` (function) component `ask_model_unavailable_marks_degraded [function]` (`2f25f6e3-97c4-5410-8214-5b9f83bb98c9`) lines 280-303 [crates/gwiki/src/commands/ask/synthesis.rs:280-303]
  - Signature: `fn ask_model_unavailable_marks_degraded() {`
  - Purpose: Verifies that calling 'mark_ai_unavailable' with 'require_ai = false' and a missing-model reason marks the output as degraded, records 'model_provider_unavailable' in 'degraded_sources', and adds an 'ai_unavailable' warning. [crates/gwiki/src/commands/ask/synthesis.rs:280-303]

