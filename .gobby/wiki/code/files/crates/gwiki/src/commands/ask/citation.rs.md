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

This file implements the citation-grounding check for `ask` answers. `citation_check` builds an evidence token set from retrieved hits, evidence excerpts, and code citations, then breaks the generated answer into sentence-like claims, checks each claim for sufficient token overlap with the evidence, and returns an `AskCitationCheckOutput` with a supported or unsupported status plus any unsupported claims.

The helper functions handle the pieces of that pipeline: `answer_claims` normalizes markdown-like lines and extracts checkable claim fragments, `claim_is_supported` applies the overlap threshold, and the token helpers lower-case, filter stopwords, and collect significant tokens from evidence and claims.
[crates/gwiki/src/commands/ask/citation.rs:25-46]
[crates/gwiki/src/commands/ask/citation.rs:50-64]
[crates/gwiki/src/commands/ask/citation.rs:66-76]
[crates/gwiki/src/commands/ask/citation.rs:78-98]
[crates/gwiki/src/commands/ask/citation.rs:100-104]

## API Symbols

- `citation_check` (function) component `citation_check [function]` (`6906a252-6636-5d29-b9a2-7df146396ee9`) lines 25-46 [crates/gwiki/src/commands/ask/citation.rs:25-46]
  - Signature: `pub(super) fn citation_check(`
  - Purpose: 'citation_check' derives evidence tokens from the output and excerpts, extracts claims from the answer, counts them, filters out unsupported claims via 'claim_is_supported', and returns an 'AskCitationCheckOutput' whose status indicates whether any unsupported claims remain. [crates/gwiki/src/commands/ask/citation.rs:25-46]
- `answer_claims` (function) component `answer_claims [function]` (`b1cbe20f-b39f-523a-b118-3f51ac6334ae`) lines 50-64 [crates/gwiki/src/commands/ask/citation.rs:50-64]
  - Signature: `fn answer_claims(answer: &str) -> Vec<String> {`
  - Purpose: It normalizes each non-empty line by stripping leading markdown quote/list markers and whitespace, splits the text into sentence-like fragments on '.', '!', and '?', trims trailing punctuation, and returns only those fragments whose significant-token count meets 'MIN_CLAIM_TOKENS'. [crates/gwiki/src/commands/ask/citation.rs:50-64]
- `claim_is_supported` (function) component `claim_is_supported [function]` (`74690c59-a9a7-5189-8d98-8dacd8d9c802`) lines 66-76 [crates/gwiki/src/commands/ask/citation.rs:66-76]
  - Signature: `fn claim_is_supported(claim: &str, evidence: &HashSet<String>) -> bool {`
  - Purpose: Returns 'true' when the claim yields no significant tokens or when at least 'CLAIM_SUPPORT_THRESHOLD' of its significant tokens are present in the 'evidence' set, otherwise 'false'. [crates/gwiki/src/commands/ask/citation.rs:66-76]
- `evidence_tokens` (function) component `evidence_tokens [function]` (`a76ed9a4-6a2f-51e8-9e5e-1202ab997204`) lines 78-98 [crates/gwiki/src/commands/ask/citation.rs:78-98]
  - Signature: `fn evidence_tokens(output: &AskOutput, evidence_excerpts: &[String]) -> HashSet<String> {`
  - Purpose: Builds a 'HashSet<String>' of tokens collected from every search hit’s title, snippet, wiki page path, and source path, plus all provided evidence excerpts and each code citation’s file and optional symbol. [crates/gwiki/src/commands/ask/citation.rs:78-98]
- `significant_tokens` (function) component `significant_tokens [function]` (`fc2c20c2-ec40-5a81-874e-977e12fae75c`) lines 100-104 [crates/gwiki/src/commands/ask/citation.rs:100-104]
  - Signature: `fn significant_tokens(text: &str) -> Vec<String> {`
  - Purpose: 'significant_tokens' collects all tokens from 'text' via 'collect_tokens_into', appends each emitted token into a 'Vec<String>', and returns the resulting token list. [crates/gwiki/src/commands/ask/citation.rs:100-104]
- `collect_tokens` (function) component `collect_tokens [function]` (`da565ccb-759b-5d84-b2e2-8e61b883ed59`) lines 106-110 [crates/gwiki/src/commands/ask/citation.rs:106-110]
  - Signature: `fn collect_tokens(text: &str, evidence: &mut HashSet<String>) {`
  - Purpose: 'collect_tokens' tokenizes the provided 'text' via 'collect_tokens_into' and inserts each emitted token into the mutable 'HashSet<String>' 'evidence'. [crates/gwiki/src/commands/ask/citation.rs:106-110]
- `collect_tokens_into` (function) component `collect_tokens_into [function]` (`cdc993d5-dfbb-5d16-874c-baff31f5d2d2`) lines 114-131 [crates/gwiki/src/commands/ask/citation.rs:114-131]
  - Signature: `fn collect_tokens_into(text: &str, mut push: impl FnMut(String)) {`
  - Purpose: Splits 'text' on non-alphanumeric characters, lowercases each token of length at least 4, filters out a fixed English stopword list, and passes each remaining token to 'push' as an owned 'String'. [crates/gwiki/src/commands/ask/citation.rs:114-131]

