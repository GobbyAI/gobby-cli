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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/ask/synthesis.rs:15-45](crates/gwiki/src/commands/ask/synthesis.rs#L15-L45), [crates/gwiki/src/commands/ask/synthesis.rs:47-60](crates/gwiki/src/commands/ask/synthesis.rs#L47-L60), [crates/gwiki/src/commands/ask/synthesis.rs:62-75](crates/gwiki/src/commands/ask/synthesis.rs#L62-L75), [crates/gwiki/src/commands/ask/synthesis.rs:77-111](crates/gwiki/src/commands/ask/synthesis.rs#L77-L111), [crates/gwiki/src/commands/ask/synthesis.rs:113-145](crates/gwiki/src/commands/ask/synthesis.rs#L113-L145), [crates/gwiki/src/commands/ask/synthesis.rs:147-149](crates/gwiki/src/commands/ask/synthesis.rs#L147-L149), [crates/gwiki/src/commands/ask/synthesis.rs:151-158](crates/gwiki/src/commands/ask/synthesis.rs#L151-L158), [crates/gwiki/src/commands/ask/synthesis.rs:171-217](crates/gwiki/src/commands/ask/synthesis.rs#L171-L217), [crates/gwiki/src/commands/ask/synthesis.rs:220-245](crates/gwiki/src/commands/ask/synthesis.rs#L220-L245), [crates/gwiki/src/commands/ask/synthesis.rs:248-254](crates/gwiki/src/commands/ask/synthesis.rs#L248-L254), [crates/gwiki/src/commands/ask/synthesis.rs:257-277](crates/gwiki/src/commands/ask/synthesis.rs#L257-L277), [crates/gwiki/src/commands/ask/synthesis.rs:280-303](crates/gwiki/src/commands/ask/synthesis.rs#L280-L303)

</details>

# crates/gwiki/src/commands/ask/synthesis.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements the `ask` synthesis step: it resolves the active AI route, initializes AI status on the output, and then either runs a direct text generation call, routes through the daemon, or marks AI as unavailable when routing is off or unsupported. The helper functions split that flow into route-specific generation, result recording, and error/degraded-state handling, while small utilities provide the synthesis system prompt and human-readable routing labels. The tests show the intended behavior: ungrounded claims are flagged, leading model narration is stripped before recording, grounded answers pass citation checks, and model unavailability degrades the ask result.
[crates/gwiki/src/commands/ask/synthesis.rs:15-45]
[crates/gwiki/src/commands/ask/synthesis.rs:47-60]
[crates/gwiki/src/commands/ask/synthesis.rs:62-75]
[crates/gwiki/src/commands/ask/synthesis.rs:77-111]
[crates/gwiki/src/commands/ask/synthesis.rs:113-145]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `synthesize` | function | `pub(super) fn synthesize(` | `synthesize [function]` | `fd5e87a1-c0cb-52d6-9843-ca5ab53b4627` | 15-45 [crates/gwiki/src/commands/ask/synthesis.rs:15-45] | Indexed function `synthesize` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:15-45] |
| `generate_direct` | function | `fn generate_direct(` | `generate_direct [function]` | `c99eb5b8-46e9-5d7f-ae1a-45f2fb281090` | 47-60 [crates/gwiki/src/commands/ask/synthesis.rs:47-60] | Indexed function `generate_direct` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:47-60] |
| `generate_daemon` | function | `fn generate_daemon(` | `generate_daemon [function]` | `5be2b4f6-cb79-5252-a678-9e84c4bd476f` | 62-75 [crates/gwiki/src/commands/ask/synthesis.rs:62-75] | Indexed function `generate_daemon` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:62-75] |
| `record_synthesis` | function | `pub(super) fn record_synthesis(` | `record_synthesis [function]` | `20699db2-0f81-5bd7-ac75-99f831d74be1` | 77-111 [crates/gwiki/src/commands/ask/synthesis.rs:77-111] | Indexed function `record_synthesis` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:77-111] |
| `mark_ai_unavailable` | function | `fn mark_ai_unavailable(` | `mark_ai_unavailable [function]` | `a1647851-0d94-5e8d-b03c-3a886728617a` | 113-145 [crates/gwiki/src/commands/ask/synthesis.rs:113-145] | Indexed function `mark_ai_unavailable` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:113-145] |
| `synthesis_system` | function | `fn synthesis_system() -> &'static str {` | `synthesis_system [function]` | `3e93e0e3-f139-5a92-b4ac-3b749a665786` | 147-149 [crates/gwiki/src/commands/ask/synthesis.rs:147-149] | Indexed function `synthesis_system` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:147-149] |
| `routing_label` | function | `fn routing_label(route: AiRouting) -> &'static str {` | `routing_label [function]` | `f094fb17-a2a5-537e-929f-a2a0cb328f5d` | 151-158 [crates/gwiki/src/commands/ask/synthesis.rs:151-158] | Indexed function `routing_label` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:151-158] |
| `synthesis_with_ungrounded_claim_is_flagged_in_json` | function | `fn synthesis_with_ungrounded_claim_is_flagged_in_json() {` | `synthesis_with_ungrounded_claim_is_flagged_in_json [function]` | `f08657da-76fe-5250-89f7-3950266dc0c6` | 171-217 [crates/gwiki/src/commands/ask/synthesis.rs:171-217] | Indexed function `synthesis_with_ungrounded_claim_is_flagged_in_json` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:171-217] |
| `synthesis_strips_leading_model_narration_before_recording` | function | `fn synthesis_strips_leading_model_narration_before_recording() {` | `synthesis_strips_leading_model_narration_before_recording [function]` | `51911b4b-c75a-56e8-a19a-48909a159ebe` | 220-245 [crates/gwiki/src/commands/ask/synthesis.rs:220-245] | Indexed function `synthesis_strips_leading_model_narration_before_recording` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:220-245] |
| `synthesis_system_requests_answer_only_output` | function | `fn synthesis_system_requests_answer_only_output() {` | `synthesis_system_requests_answer_only_output [function]` | `aa51a0a7-cc99-555d-babc-d8301a21c709` | 248-254 [crates/gwiki/src/commands/ask/synthesis.rs:248-254] | Indexed function `synthesis_system_requests_answer_only_output` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:248-254] |
| `synthesis_grounded_in_hits_passes_citation_check` | function | `fn synthesis_grounded_in_hits_passes_citation_check() {` | `synthesis_grounded_in_hits_passes_citation_check [function]` | `24e6d087-3056-5596-a4c5-950563fac45f` | 257-277 [crates/gwiki/src/commands/ask/synthesis.rs:257-277] | Indexed function `synthesis_grounded_in_hits_passes_citation_check` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:257-277] |
| `ask_model_unavailable_marks_degraded` | function | `fn ask_model_unavailable_marks_degraded() {` | `ask_model_unavailable_marks_degraded [function]` | `2f25f6e3-97c4-5410-8214-5b9f83bb98c9` | 280-303 [crates/gwiki/src/commands/ask/synthesis.rs:280-303] | Indexed function `ask_model_unavailable_marks_degraded` in `crates/gwiki/src/commands/ask/synthesis.rs`. [crates/gwiki/src/commands/ask/synthesis.rs:280-303] |
