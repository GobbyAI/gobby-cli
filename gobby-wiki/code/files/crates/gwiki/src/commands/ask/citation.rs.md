---
title: crates/gwiki/src/commands/ask/citation.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/ask/citation.rs
  ranges:
  - 25-46
  - 50-64
  - 66-76
  - 78-98
  - 100-104
  - 106-110
  - 114-131
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/ask/citation.rs:25-46](crates/gwiki/src/commands/ask/citation.rs#L25-L46), [crates/gwiki/src/commands/ask/citation.rs:50-64](crates/gwiki/src/commands/ask/citation.rs#L50-L64), [crates/gwiki/src/commands/ask/citation.rs:66-76](crates/gwiki/src/commands/ask/citation.rs#L66-L76), [crates/gwiki/src/commands/ask/citation.rs:78-98](crates/gwiki/src/commands/ask/citation.rs#L78-L98), [crates/gwiki/src/commands/ask/citation.rs:100-104](crates/gwiki/src/commands/ask/citation.rs#L100-L104), [crates/gwiki/src/commands/ask/citation.rs:106-110](crates/gwiki/src/commands/ask/citation.rs#L106-L110), [crates/gwiki/src/commands/ask/citation.rs:114-131](crates/gwiki/src/commands/ask/citation.rs#L114-L131)

</details>

# crates/gwiki/src/commands/ask/citation.rs

Module: [[code/modules/crates/gwiki/src/commands/ask|crates/gwiki/src/commands/ask]]

## Purpose

This file implements citation verification for synthesized answers. `citation_check` builds a tokenized evidence set from the retrieved `AskOutput` plus supplied evidence excerpts, splits the answer into sentence-level claims, and marks the result as `supported` only when every checkable claim meets the overlap threshold; otherwise it returns `unsupported_claims` with the failing claims. The helper functions work together to make that decision: `answer_claims` extracts and cleans candidate claims from headings, bullets, and sentences; `claim_is_supported` compares each claim against the evidence; `evidence_tokens` gathers tokens from evidence sources; and the token helpers (`significant_tokens`, `collect_tokens`, `collect_tokens_into`) normalize and filter the text down to the words used for overlap checking.
[crates/gwiki/src/commands/ask/citation.rs:25-46]
[crates/gwiki/src/commands/ask/citation.rs:50-64]
[crates/gwiki/src/commands/ask/citation.rs:66-76]
[crates/gwiki/src/commands/ask/citation.rs:78-98]
[crates/gwiki/src/commands/ask/citation.rs:100-104]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `citation_check` | function | `pub(super) fn citation_check(` | `citation_check [function]` | `6906a252-6636-5d29-b9a2-7df146396ee9` | 25-46 [crates/gwiki/src/commands/ask/citation.rs:25-46] | Indexed function `citation_check` in `crates/gwiki/src/commands/ask/citation.rs`. [crates/gwiki/src/commands/ask/citation.rs:25-46] |
| `answer_claims` | function | `fn answer_claims(answer: &str) -> Vec<String> {` | `answer_claims [function]` | `b1cbe20f-b39f-523a-b118-3f51ac6334ae` | 50-64 [crates/gwiki/src/commands/ask/citation.rs:50-64] | Indexed function `answer_claims` in `crates/gwiki/src/commands/ask/citation.rs`. [crates/gwiki/src/commands/ask/citation.rs:50-64] |
| `claim_is_supported` | function | `fn claim_is_supported(claim: &str, evidence: &HashSet<String>) -> bool {` | `claim_is_supported [function]` | `74690c59-a9a7-5189-8d98-8dacd8d9c802` | 66-76 [crates/gwiki/src/commands/ask/citation.rs:66-76] | Indexed function `claim_is_supported` in `crates/gwiki/src/commands/ask/citation.rs`. [crates/gwiki/src/commands/ask/citation.rs:66-76] |
| `evidence_tokens` | function | `fn evidence_tokens(output: &AskOutput, evidence_excerpts: &[String]) -> HashSet<String> {` | `evidence_tokens [function]` | `a76ed9a4-6a2f-51e8-9e5e-1202ab997204` | 78-98 [crates/gwiki/src/commands/ask/citation.rs:78-98] | Indexed function `evidence_tokens` in `crates/gwiki/src/commands/ask/citation.rs`. [crates/gwiki/src/commands/ask/citation.rs:78-98] |
| `significant_tokens` | function | `fn significant_tokens(text: &str) -> Vec<String> {` | `significant_tokens [function]` | `fc2c20c2-ec40-5a81-874e-977e12fae75c` | 100-104 [crates/gwiki/src/commands/ask/citation.rs:100-104] | Indexed function `significant_tokens` in `crates/gwiki/src/commands/ask/citation.rs`. [crates/gwiki/src/commands/ask/citation.rs:100-104] |
| `collect_tokens` | function | `fn collect_tokens(text: &str, evidence: &mut HashSet<String>) {` | `collect_tokens [function]` | `da565ccb-759b-5d84-b2e2-8e61b883ed59` | 106-110 [crates/gwiki/src/commands/ask/citation.rs:106-110] | Indexed function `collect_tokens` in `crates/gwiki/src/commands/ask/citation.rs`. [crates/gwiki/src/commands/ask/citation.rs:106-110] |
| `collect_tokens_into` | function | `fn collect_tokens_into(text: &str, mut push: impl FnMut(String)) {` | `collect_tokens_into [function]` | `cdc993d5-dfbb-5d16-874c-baff31f5d2d2` | 114-131 [crates/gwiki/src/commands/ask/citation.rs:114-131] | Indexed function `collect_tokens_into` in `crates/gwiki/src/commands/ask/citation.rs`. [crates/gwiki/src/commands/ask/citation.rs:114-131] |
