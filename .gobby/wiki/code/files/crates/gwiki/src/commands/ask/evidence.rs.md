---
title: crates/gwiki/src/commands/ask/evidence.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/ask/evidence.rs
  ranges:
  - 14-16
  - 20-26
  - 31-83
  - 95-121
  - 124-133
  - 136-149
  - 152-158
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/ask/evidence.rs

Module: [[code/modules/crates/gwiki/src/commands/ask|crates/gwiki/src/commands/ask]]

## Purpose

Builds a bounded evidence plan for an ask command: it estimates prompt size, slices each search hit into a query-centered excerpt, and accumulates ranked evidence until adding another excerpt would exceed the synthesis token budget. `plan_evidence` produces the final prompt, excerpt list, selected `AskEvidenceOutput` items, and a count of dropped hits; the small test helpers verify the token estimator, that retrieval includes bodies, that the prompt stays within budget, that excerpts are chunk-sized rather than full documents, and that the empty-results case emits a missing-evidence state.
[crates/gwiki/src/commands/ask/evidence.rs:14-16]
[crates/gwiki/src/commands/ask/evidence.rs:20-26]
[crates/gwiki/src/commands/ask/evidence.rs:31-83]
[crates/gwiki/src/commands/ask/evidence.rs:95-121]
[crates/gwiki/src/commands/ask/evidence.rs:124-133]

## API Symbols

- `estimate_tokens` (function) component `estimate_tokens [function]` (`4e18237e-0bed-5b31-b695-d43e5509a508`) lines 14-16 [crates/gwiki/src/commands/ask/evidence.rs:14-16]
  - Signature: `pub(super) fn estimate_tokens(chars: usize) -> usize {`
  - Purpose: Indexed function `estimate_tokens` in `crates/gwiki/src/commands/ask/evidence.rs`. [crates/gwiki/src/commands/ask/evidence.rs:14-16]
- `EvidencePlan` (class) component `EvidencePlan [class]` (`32e99ef6-99bc-51ff-a482-b5248d300f5e`) lines 20-26 [crates/gwiki/src/commands/ask/evidence.rs:20-26]
  - Signature: `pub(super) struct EvidencePlan {`
  - Purpose: Indexed class `EvidencePlan` in `crates/gwiki/src/commands/ask/evidence.rs`. [crates/gwiki/src/commands/ask/evidence.rs:20-26]
- `plan_evidence` (function) component `plan_evidence [function]` (`9c21d8f6-5f23-5adc-8b1a-c1b171148ce2`) lines 31-83 [crates/gwiki/src/commands/ask/evidence.rs:31-83]
  - Signature: `pub(super) fn plan_evidence(retrieval: &SearchRetrieval) -> EvidencePlan {`
  - Purpose: Indexed function `plan_evidence` in `crates/gwiki/src/commands/ask/evidence.rs`. [crates/gwiki/src/commands/ask/evidence.rs:31-83]
- `retrieval_with_bodies` (function) component `retrieval_with_bodies [function]` (`388904ad-d580-5cf2-aa6c-a852a27a8469`) lines 95-121 [crates/gwiki/src/commands/ask/evidence.rs:95-121]
  - Signature: `fn retrieval_with_bodies(bodies: Vec<String>) -> SearchRetrieval {`
  - Purpose: Indexed function `retrieval_with_bodies` in `crates/gwiki/src/commands/ask/evidence.rs`. [crates/gwiki/src/commands/ask/evidence.rs:95-121]
- `prompt_never_exceeds_token_budget` (function) component `prompt_never_exceeds_token_budget [function]` (`b5235f70-a1c3-5472-9787-7db5bd40f447`) lines 124-133 [crates/gwiki/src/commands/ask/evidence.rs:124-133]
  - Signature: `fn prompt_never_exceeds_token_budget() {`
  - Purpose: Indexed function `prompt_never_exceeds_token_budget` in `crates/gwiki/src/commands/ask/evidence.rs`. [crates/gwiki/src/commands/ask/evidence.rs:124-133]
- `evidence_excerpts_are_chunk_sized_not_full_bodies` (function) component `evidence_excerpts_are_chunk_sized_not_full_bodies [function]` (`5b6daa82-a53d-59eb-beb5-4f8cfe7c5da8`) lines 136-149 [crates/gwiki/src/commands/ask/evidence.rs:136-149]
  - Signature: `fn evidence_excerpts_are_chunk_sized_not_full_bodies() {`
  - Purpose: Indexed function `evidence_excerpts_are_chunk_sized_not_full_bodies` in `crates/gwiki/src/commands/ask/evidence.rs`. [crates/gwiki/src/commands/ask/evidence.rs:136-149]
- `empty_results_state_missing_evidence` (function) component `empty_results_state_missing_evidence [function]` (`b8914db1-548c-55b0-9cc7-f0036dddaa66`) lines 152-158 [crates/gwiki/src/commands/ask/evidence.rs:152-158]
  - Signature: `fn empty_results_state_missing_evidence() {`
  - Purpose: Indexed function `empty_results_state_missing_evidence` in `crates/gwiki/src/commands/ask/evidence.rs`. [crates/gwiki/src/commands/ask/evidence.rs:152-158]

