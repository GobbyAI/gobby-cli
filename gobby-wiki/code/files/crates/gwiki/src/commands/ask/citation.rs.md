---
title: crates/gwiki/src/commands/ask/citation.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/ask/citation.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/ask/citation.rs

Module: [[code/modules/crates/gwiki/src/commands/ask|crates/gwiki/src/commands/ask]]

## Overview

`crates/gwiki/src/commands/ask/citation.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/ask/citation.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `citation_check` | function | Builds evidence tokens from the output and excerpts, extracts claims from the answer, filters out unsupported claims, and returns an 'AskCitationCheckOutput' indicating supported or unsupported status along with the number of claims checked and any unsupported claim strings. [crates/gwiki/src/commands/ask/citation.rs:25-46] |
| `answer_claims` | function | It normalizes each non-empty input line by stripping common list/quote prefixes and surrounding whitespace, splits it into sentence-like fragments on '. ! ?', trims trailing punctuation, and returns only those fragments whose 'significant_tokens' count meets 'MIN_CLAIM_TOKENS'. [crates/gwiki/src/commands/ask/citation.rs:50-64] |
| `claim_is_supported` | function | Returns 'true' when the claim has no significant tokens or when at least 'CLAIM_SUPPORT_THRESHOLD' fraction of its significant tokens are present in the 'evidence' set. [crates/gwiki/src/commands/ask/citation.rs:66-76] |
| `evidence_tokens` | function | Builds a 'HashSet<String>' of normalized tokens collected from each search hit’s title, snippet, wiki page path, and source path, plus all provided evidence excerpts and the file and optional symbol fields of each code citation. [crates/gwiki/src/commands/ask/citation.rs:78-98] |
| `significant_tokens` | function | Collects all tokens from 'text' by passing each token produced by 'collect_tokens_into' into a 'Vec<String>' and returns that vector. [crates/gwiki/src/commands/ask/citation.rs:100-104] |
| `collect_tokens` | function | 'collect_tokens' scans 'text' for tokens via 'collect_tokens_into' and inserts each token into the provided 'HashSet<String>' evidence set. [crates/gwiki/src/commands/ask/citation.rs:106-110] |
| `collect_tokens_into` | function | Splits 'text' on non-alphanumeric boundaries, lowercases each token of length at least 4, filters out a fixed English stopword list, and passes each remaining token to 'push'. [crates/gwiki/src/commands/ask/citation.rs:114-131] |

