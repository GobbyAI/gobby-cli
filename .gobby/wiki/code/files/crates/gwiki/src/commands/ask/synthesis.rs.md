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

This file implements the ask-command synthesis step: it resolves the active AI route, runs one bounded prompt over the prepared evidence, records the result on the output, and falls back cleanly when AI is unavailable. `synthesize` is the entry point; it builds AI context, chooses direct versus daemon generation via `effective_route`, initializes the AI status on `AskOutput`, and dispatches to `generate_direct`, `generate_daemon`, or `mark_ai_unavailable`. The generation helpers call the appropriate backend, then hand successful text to `record_synthesis`, which stores the synthesized answer along with excerpts and model metadata after stripping leading model narration. The remaining helpers provide the system prompt and route labels, and the tests verify that ungrounded claims are flagged in JSON, narration is removed before recording, the system prompt requests answer-only output, grounded synthesis passes citation checks, and model unavailability marks the response as degraded.
[crates/gwiki/src/commands/ask/synthesis.rs:15-45]
[crates/gwiki/src/commands/ask/synthesis.rs:47-60]
[crates/gwiki/src/commands/ask/synthesis.rs:62-75]
[crates/gwiki/src/commands/ask/synthesis.rs:77-111]
[crates/gwiki/src/commands/ask/synthesis.rs:113-145]

## API Symbols

- `synthesize` (function) component `synthesize [function]` (`fd5e87a1-c0cb-52d6-9843-ca5ab53b4627`) lines 15-45 [crates/gwiki/src/commands/ask/synthesis.rs:15-45]
  - Signature: `pub(super) fn synthesize(`
  - Purpose: Indexed function `synthesize` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:15-45]
- `generate_direct` (function) component `generate_direct [function]` (`c99eb5b8-46e9-5d7f-ae1a-45f2fb281090`) lines 47-60 [crates/gwiki/src/commands/ask/synthesis.rs:47-60]
  - Signature: `fn generate_direct(`
  - Purpose: Indexed function `generate_direct` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:47-60]
- `generate_daemon` (function) component `generate_daemon [function]` (`5be2b4f6-cb79-5252-a678-9e84c4bd476f`) lines 62-75 [crates/gwiki/src/commands/ask/synthesis.rs:62-75]
  - Signature: `fn generate_daemon(`
  - Purpose: Indexed function `generate_daemon` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:62-75]
- `record_synthesis` (function) component `record_synthesis [function]` (`20699db2-0f81-5bd7-ac75-99f831d74be1`) lines 77-111 [crates/gwiki/src/commands/ask/synthesis.rs:77-111]
  - Signature: `pub(super) fn record_synthesis(`
  - Purpose: Indexed function `record_synthesis` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:77-111]
- `mark_ai_unavailable` (function) component `mark_ai_unavailable [function]` (`a1647851-0d94-5e8d-b03c-3a886728617a`) lines 113-145 [crates/gwiki/src/commands/ask/synthesis.rs:113-145]
  - Signature: `fn mark_ai_unavailable(`
  - Purpose: Indexed function `mark_ai_unavailable` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:113-145]
- `synthesis_system` (function) component `synthesis_system [function]` (`3e93e0e3-f139-5a92-b4ac-3b749a665786`) lines 147-149 [crates/gwiki/src/commands/ask/synthesis.rs:147-149]
  - Signature: `fn synthesis_system() -> &'static str {`
  - Purpose: Indexed function `synthesis_system` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:147-149]
- `routing_label` (function) component `routing_label [function]` (`f094fb17-a2a5-537e-929f-a2a0cb328f5d`) lines 151-158 [crates/gwiki/src/commands/ask/synthesis.rs:151-158]
  - Signature: `fn routing_label(route: AiRouting) -> &'static str {`
  - Purpose: Indexed function `routing_label` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:151-158]
- `synthesis_with_ungrounded_claim_is_flagged_in_json` (function) component `synthesis_with_ungrounded_claim_is_flagged_in_json [function]` (`f08657da-76fe-5250-89f7-3950266dc0c6`) lines 171-217 [crates/gwiki/src/commands/ask/synthesis.rs:171-217]
  - Signature: `fn synthesis_with_ungrounded_claim_is_flagged_in_json() {`
  - Purpose: Indexed function `synthesis_with_ungrounded_claim_is_flagged_in_json` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:171-217]
- `synthesis_strips_leading_model_narration_before_recording` (function) component `synthesis_strips_leading_model_narration_before_recording [function]` (`51911b4b-c75a-56e8-a19a-48909a159ebe`) lines 220-245 [crates/gwiki/src/commands/ask/synthesis.rs:220-245]
  - Signature: `fn synthesis_strips_leading_model_narration_before_recording() {`
  - Purpose: Indexed function `synthesis_strips_leading_model_narration_before_recording` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:220-245]
- `synthesis_system_requests_answer_only_output` (function) component `synthesis_system_requests_answer_only_output [function]` (`aa51a0a7-cc99-555d-babc-d8301a21c709`) lines 248-254 [crates/gwiki/src/commands/ask/synthesis.rs:248-254]
  - Signature: `fn synthesis_system_requests_answer_only_output() {`
  - Purpose: Indexed function `synthesis_system_requests_answer_only_output` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:248-254]
- `synthesis_grounded_in_hits_passes_citation_check` (function) component `synthesis_grounded_in_hits_passes_citation_check [function]` (`24e6d087-3056-5596-a4c5-950563fac45f`) lines 257-277 [crates/gwiki/src/commands/ask/synthesis.rs:257-277]
  - Signature: `fn synthesis_grounded_in_hits_passes_citation_check() {`
  - Purpose: Indexed function `synthesis_grounded_in_hits_passes_citation_check` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:257-277]
- `ask_model_unavailable_marks_degraded` (function) component `ask_model_unavailable_marks_degraded [function]` (`2f25f6e3-97c4-5410-8214-5b9f83bb98c9`) lines 280-303 [crates/gwiki/src/commands/ask/synthesis.rs:280-303]
  - Signature: `fn ask_model_unavailable_marks_degraded() {`
  - Purpose: Indexed function `ask_model_unavailable_marks_degraded` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:280-303]

