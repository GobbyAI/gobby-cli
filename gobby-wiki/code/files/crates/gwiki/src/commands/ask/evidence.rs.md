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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/ask/evidence.rs:14-16](crates/gwiki/src/commands/ask/evidence.rs#L14-L16), [crates/gwiki/src/commands/ask/evidence.rs:20-26](crates/gwiki/src/commands/ask/evidence.rs#L20-L26), [crates/gwiki/src/commands/ask/evidence.rs:31-83](crates/gwiki/src/commands/ask/evidence.rs#L31-L83), [crates/gwiki/src/commands/ask/evidence.rs:95-121](crates/gwiki/src/commands/ask/evidence.rs#L95-L121), [crates/gwiki/src/commands/ask/evidence.rs:124-133](crates/gwiki/src/commands/ask/evidence.rs#L124-L133), [crates/gwiki/src/commands/ask/evidence.rs:136-149](crates/gwiki/src/commands/ask/evidence.rs#L136-L149), [crates/gwiki/src/commands/ask/evidence.rs:152-158](crates/gwiki/src/commands/ask/evidence.rs#L152-L158)

</details>

# crates/gwiki/src/commands/ask/evidence.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Builds the evidence bundle for an `ask` query: it estimates prompt size, slices search hits into query-centered excerpts, and assembles a bounded synthesis prompt that stops before the token budget is exceeded. `plan_evidence` drives the process by walking retrieval results in rank order, using `query_window` and `estimate_tokens` to decide what fits, while `EvidencePlan` carries the selected `AskEvidenceOutput` items, their excerpts, the final prompt, and any dropped-hit count. The test helpers cover the budget limit, chunk-sized excerpts, and the empty-results case.
[crates/gwiki/src/commands/ask/evidence.rs:14-16]
[crates/gwiki/src/commands/ask/evidence.rs:20-26]
[crates/gwiki/src/commands/ask/evidence.rs:31-83]
[crates/gwiki/src/commands/ask/evidence.rs:95-121]
[crates/gwiki/src/commands/ask/evidence.rs:124-133]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `estimate_tokens` | function | `pub(super) fn estimate_tokens(chars: usize) -> usize {` | `estimate_tokens [function]` | `4e18237e-0bed-5b31-b695-d43e5509a508` | 14-16 [crates/gwiki/src/commands/ask/evidence.rs:14-16] | Indexed function `estimate_tokens` in `crates/gwiki/src/commands/ask/evidence.rs`. [crates/gwiki/src/commands/ask/evidence.rs:14-16] |
| `EvidencePlan` | class | `pub(super) struct EvidencePlan {` | `EvidencePlan [class]` | `32e99ef6-99bc-51ff-a482-b5248d300f5e` | 20-26 [crates/gwiki/src/commands/ask/evidence.rs:20-26] | Indexed class `EvidencePlan` in `crates/gwiki/src/commands/ask/evidence.rs`. [crates/gwiki/src/commands/ask/evidence.rs:20-26] |
| `plan_evidence` | function | `pub(super) fn plan_evidence(retrieval: &SearchRetrieval) -> EvidencePlan {` | `plan_evidence [function]` | `9c21d8f6-5f23-5adc-8b1a-c1b171148ce2` | 31-83 [crates/gwiki/src/commands/ask/evidence.rs:31-83] | Indexed function `plan_evidence` in `crates/gwiki/src/commands/ask/evidence.rs`. [crates/gwiki/src/commands/ask/evidence.rs:31-83] |
| `retrieval_with_bodies` | function | `fn retrieval_with_bodies(bodies: Vec<String>) -> SearchRetrieval {` | `retrieval_with_bodies [function]` | `388904ad-d580-5cf2-aa6c-a852a27a8469` | 95-121 [crates/gwiki/src/commands/ask/evidence.rs:95-121] | Indexed function `retrieval_with_bodies` in `crates/gwiki/src/commands/ask/evidence.rs`. [crates/gwiki/src/commands/ask/evidence.rs:95-121] |
| `prompt_never_exceeds_token_budget` | function | `fn prompt_never_exceeds_token_budget() {` | `prompt_never_exceeds_token_budget [function]` | `b5235f70-a1c3-5472-9787-7db5bd40f447` | 124-133 [crates/gwiki/src/commands/ask/evidence.rs:124-133] | Indexed function `prompt_never_exceeds_token_budget` in `crates/gwiki/src/commands/ask/evidence.rs`. [crates/gwiki/src/commands/ask/evidence.rs:124-133] |
| `evidence_excerpts_are_chunk_sized_not_full_bodies` | function | `fn evidence_excerpts_are_chunk_sized_not_full_bodies() {` | `evidence_excerpts_are_chunk_sized_not_full_bodies [function]` | `5b6daa82-a53d-59eb-beb5-4f8cfe7c5da8` | 136-149 [crates/gwiki/src/commands/ask/evidence.rs:136-149] | Indexed function `evidence_excerpts_are_chunk_sized_not_full_bodies` in `crates/gwiki/src/commands/ask/evidence.rs`. [crates/gwiki/src/commands/ask/evidence.rs:136-149] |
| `empty_results_state_missing_evidence` | function | `fn empty_results_state_missing_evidence() {` | `empty_results_state_missing_evidence [function]` | `b8914db1-548c-55b0-9cc7-f0036dddaa66` | 152-158 [crates/gwiki/src/commands/ask/evidence.rs:152-158] | Indexed function `empty_results_state_missing_evidence` in `crates/gwiki/src/commands/ask/evidence.rs`. [crates/gwiki/src/commands/ask/evidence.rs:152-158] |
