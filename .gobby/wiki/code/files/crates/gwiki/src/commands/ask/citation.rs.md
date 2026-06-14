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

# crates/gwiki/src/commands/ask/citation.rs

Module: [[code/modules/crates/gwiki/src/commands/ask|crates/gwiki/src/commands/ask]]

## Purpose

This file implements citation grounding checks for synthesized answers. `citation_check` tokenizes the retrieved evidence, breaks the answer into sentence-level claims, filters each claim through `claim_is_supported`, and returns a status plus the list of unsupported claims.

The helper functions support that pipeline: `answer_claims` strips lightweight Markdown and splits the answer into checkable sentences, `evidence_tokens` gathers normalized tokens from evidence excerpts and retrieved output fields, `significant_tokens`/`collect_tokens`/`collect_tokens_into` extract the meaningful tokens used for overlap scoring, and `claim_is_supported` compares a claim’s token coverage against the evidence using the configured support threshold and minimum claim size.
[crates/gwiki/src/commands/ask/citation.rs:25-46]
[crates/gwiki/src/commands/ask/citation.rs:50-64]
[crates/gwiki/src/commands/ask/citation.rs:66-76]
[crates/gwiki/src/commands/ask/citation.rs:78-98]
[crates/gwiki/src/commands/ask/citation.rs:100-104]

## API Symbols

- `citation_check` (function) component `citation_check [function]` (`6906a252-6636-5d29-b9a2-7df146396ee9`) lines 25-46 [crates/gwiki/src/commands/ask/citation.rs:25-46]
  - Signature: `pub(super) fn citation_check(`
  - Purpose: Indexed function `citation_check` in `crates/gwiki/src/commands/ask/citation.rs`. [crates/gwiki/src/commands/ask/citation.rs:25-46]
- `answer_claims` (function) component `answer_claims [function]` (`b1cbe20f-b39f-523a-b118-3f51ac6334ae`) lines 50-64 [crates/gwiki/src/commands/ask/citation.rs:50-64]
  - Signature: `fn answer_claims(answer: &str) -> Vec<String> {`
  - Purpose: Indexed function `answer_claims` in `crates/gwiki/src/commands/ask/citation.rs`. [crates/gwiki/src/commands/ask/citation.rs:50-64]
- `claim_is_supported` (function) component `claim_is_supported [function]` (`74690c59-a9a7-5189-8d98-8dacd8d9c802`) lines 66-76 [crates/gwiki/src/commands/ask/citation.rs:66-76]
  - Signature: `fn claim_is_supported(claim: &str, evidence: &HashSet<String>) -> bool {`
  - Purpose: Indexed function `claim_is_supported` in `crates/gwiki/src/commands/ask/citation.rs`. [crates/gwiki/src/commands/ask/citation.rs:66-76]
- `evidence_tokens` (function) component `evidence_tokens [function]` (`a76ed9a4-6a2f-51e8-9e5e-1202ab997204`) lines 78-98 [crates/gwiki/src/commands/ask/citation.rs:78-98]
  - Signature: `fn evidence_tokens(output: &AskOutput, evidence_excerpts: &[String]) -> HashSet<String> {`
  - Purpose: Indexed function `evidence_tokens` in `crates/gwiki/src/commands/ask/citation.rs`. [crates/gwiki/src/commands/ask/citation.rs:78-98]
- `significant_tokens` (function) component `significant_tokens [function]` (`fc2c20c2-ec40-5a81-874e-977e12fae75c`) lines 100-104 [crates/gwiki/src/commands/ask/citation.rs:100-104]
  - Signature: `fn significant_tokens(text: &str) -> Vec<String> {`
  - Purpose: Indexed function `significant_tokens` in `crates/gwiki/src/commands/ask/citation.rs`. [crates/gwiki/src/commands/ask/citation.rs:100-104]
- `collect_tokens` (function) component `collect_tokens [function]` (`da565ccb-759b-5d84-b2e2-8e61b883ed59`) lines 106-110 [crates/gwiki/src/commands/ask/citation.rs:106-110]
  - Signature: `fn collect_tokens(text: &str, evidence: &mut HashSet<String>) {`
  - Purpose: Indexed function `collect_tokens` in `crates/gwiki/src/commands/ask/citation.rs`. [crates/gwiki/src/commands/ask/citation.rs:106-110]
- `collect_tokens_into` (function) component `collect_tokens_into [function]` (`cdc993d5-dfbb-5d16-874c-baff31f5d2d2`) lines 114-131 [crates/gwiki/src/commands/ask/citation.rs:114-131]
  - Signature: `fn collect_tokens_into(text: &str, mut push: impl FnMut(String)) {`
  - Purpose: Indexed function `collect_tokens_into` in `crates/gwiki/src/commands/ask/citation.rs`. [crates/gwiki/src/commands/ask/citation.rs:114-131]

