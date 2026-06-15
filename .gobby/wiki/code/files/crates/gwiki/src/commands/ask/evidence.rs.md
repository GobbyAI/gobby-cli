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

Builds the evidence-selection pipeline for `ask`: it estimates prompt size, assembles ranked wiki excerpts into an `EvidencePlan`, and stops before the synthesis prompt exceeds the hard token budget while counting dropped hits. It uses `query_window` to keep excerpts chunk-sized around the query, formats each retained hit into the final prompt with metadata, and exposes a helper to synthesize `SearchRetrieval` inputs from raw bodies for tests. The tests verify budget enforcement, excerpt sizing, and the empty-results fallback message.
[crates/gwiki/src/commands/ask/evidence.rs:14-16]
[crates/gwiki/src/commands/ask/evidence.rs:20-26]
[crates/gwiki/src/commands/ask/evidence.rs:31-83]
[crates/gwiki/src/commands/ask/evidence.rs:95-121]
[crates/gwiki/src/commands/ask/evidence.rs:124-133]

## API Symbols

- `estimate_tokens` (function) component `estimate_tokens [function]` (`4e18237e-0bed-5b31-b695-d43e5509a508`) lines 14-16 [crates/gwiki/src/commands/ask/evidence.rs:14-16]
  - Signature: `pub(super) fn estimate_tokens(chars: usize) -> usize {`
  - Purpose: Returns the token estimate for a character count by rounding up 'chars / 4' using integer ceiling division. [crates/gwiki/src/commands/ask/evidence.rs:14-16]
- `EvidencePlan` (class) component `EvidencePlan [class]` (`32e99ef6-99bc-51ff-a482-b5248d300f5e`) lines 20-26 [crates/gwiki/src/commands/ask/evidence.rs:20-26]
  - Signature: `pub(super) struct EvidencePlan {`
  - Purpose: 'EvidencePlan' is an internal plan object that aggregates evidence items and text excerpts with the generated prompt, estimated prompt token count, and a count of dropped hits. [crates/gwiki/src/commands/ask/evidence.rs:20-26]
- `plan_evidence` (function) component `plan_evidence [function]` (`9c21d8f6-5f23-5adc-8b1a-c1b171148ce2`) lines 31-83 [crates/gwiki/src/commands/ask/evidence.rs:31-83]
  - Signature: `pub(super) fn plan_evidence(retrieval: &SearchRetrieval) -> EvidencePlan {`
  - Purpose: 'plan_evidence' builds an 'EvidencePlan' from 'SearchRetrieval' by assembling a token-budgeted prompt with ranked wiki evidence excerpts, recording per-item metadata and excerpts, estimating prompt tokens, and stopping at the first hit that would exceed the prompt budget while counting the remaining dropped hits. [crates/gwiki/src/commands/ask/evidence.rs:31-83]
- `retrieval_with_bodies` (function) component `retrieval_with_bodies [function]` (`388904ad-d580-5cf2-aa6c-a852a27a8469`) lines 95-121 [crates/gwiki/src/commands/ask/evidence.rs:95-121]
  - Signature: `fn retrieval_with_bodies(bodies: Vec<String>) -> SearchRetrieval {`
  - Purpose: Constructs a 'SearchRetrieval' from the provided body strings by creating one synthetic wiki 'SearchResultOutput' per body with indexed metadata, descending scores, and 'bm25' as the sole source, then packages those results into a 'SearchOutput' and stores the original bodies as 'evidence'. [crates/gwiki/src/commands/ask/evidence.rs:95-121]
- `prompt_never_exceeds_token_budget` (function) component `prompt_never_exceeds_token_budget [function]` (`b5235f70-a1c3-5472-9787-7db5bd40f447`) lines 124-133 [crates/gwiki/src/commands/ask/evidence.rs:124-133]
  - Signature: `fn prompt_never_exceeds_token_budget() {`
  - Purpose: Tests that 'plan_evidence' enforces 'ASK_PROMPT_TOKEN_BUDGET' by dropping excess retrieval hits when 40 oversized bodies would otherwise exceed the prompt-token limit, while preserving the invariant that retained items plus dropped hits equals 40. [crates/gwiki/src/commands/ask/evidence.rs:124-133]
- `evidence_excerpts_are_chunk_sized_not_full_bodies` (function) component `evidence_excerpts_are_chunk_sized_not_full_bodies [function]` (`5b6daa82-a53d-59eb-beb5-4f8cfe7c5da8`) lines 136-149 [crates/gwiki/src/commands/ask/evidence.rs:136-149]
  - Signature: `fn evidence_excerpts_are_chunk_sized_not_full_bodies() {`
  - Purpose: Verifies that 'plan_evidence' produces a single chunk-sized evidence excerpt, capped at 'EVIDENCE_BEFORE_CHARS + EVIDENCE_AFTER_CHARS' and smaller than the full body while still containing the matching '"enqueue failure"' text. [crates/gwiki/src/commands/ask/evidence.rs:136-149]
- `empty_results_state_missing_evidence` (function) component `empty_results_state_missing_evidence [function]` (`b8914db1-548c-55b0-9cc7-f0036dddaa66`) lines 152-158 [crates/gwiki/src/commands/ask/evidence.rs:152-158]
  - Signature: `fn empty_results_state_missing_evidence() {`
  - Purpose: Verifies that 'plan_evidence' on an empty retrieval with bodies produces a prompt containing "No wiki evidence was found.", with 'dropped_hits' equal to '0' and no plan items. [crates/gwiki/src/commands/ask/evidence.rs:152-158]

