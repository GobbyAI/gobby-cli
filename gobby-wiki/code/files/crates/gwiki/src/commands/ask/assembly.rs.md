---
title: crates/gwiki/src/commands/ask/assembly.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/ask/assembly.rs
  ranges:
  - 6-39
  - 41-50
  - 52-58
  - 72-120
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/ask/assembly.rs:6-39](crates/gwiki/src/commands/ask/assembly.rs#L6-L39), [crates/gwiki/src/commands/ask/assembly.rs:41-50](crates/gwiki/src/commands/ask/assembly.rs#L41-L50), [crates/gwiki/src/commands/ask/assembly.rs:52-58](crates/gwiki/src/commands/ask/assembly.rs#L52-L58), [crates/gwiki/src/commands/ask/assembly.rs:72-120](crates/gwiki/src/commands/ask/assembly.rs#L72-L120)

</details>

# crates/gwiki/src/commands/ask/assembly.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Builds an `AskOutput` from search retrieval and an evidence plan. `ask_output_from_retrieval` maps the raw `SearchOutput` plus `EvidencePlan` into the final ask response, setting status from whether hits exist, marking degraded/truncated states, carrying through hits, citations, evidence, and prompt-budget metadata. `unique_sources` collects a sorted deduplicated list of source paths from the retrieved hits and their nested sources, while `ordered_unique_strings` deduplicates string lists without changing order. The test verifies the assembled output preserves the expected bounded retrieval shape when evidence is dropped.
[crates/gwiki/src/commands/ask/assembly.rs:6-39]
[crates/gwiki/src/commands/ask/assembly.rs:41-50]
[crates/gwiki/src/commands/ask/assembly.rs:52-58]
[crates/gwiki/src/commands/ask/assembly.rs:72-120]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ask_output_from_retrieval` | function | `pub(super) fn ask_output_from_retrieval(search: SearchOutput, plan: &EvidencePlan) -> AskOutput {` | `ask_output_from_retrieval [function]` | `78236031-e711-5a4a-adcf-5aad42ecb73c` | 6-39 [crates/gwiki/src/commands/ask/assembly.rs:6-39] | Indexed function `ask_output_from_retrieval` in `crates/gwiki/src/commands/ask/assembly.rs`. [crates/gwiki/src/commands/ask/assembly.rs:6-39] |
| `unique_sources` | function | `fn unique_sources(search: &SearchOutput) -> Vec<String> {` | `unique_sources [function]` | `a1e580a1-5c5a-5f60-ab2c-2852b53707e9` | 41-50 [crates/gwiki/src/commands/ask/assembly.rs:41-50] | Indexed function `unique_sources` in `crates/gwiki/src/commands/ask/assembly.rs`. [crates/gwiki/src/commands/ask/assembly.rs:41-50] |
| `ordered_unique_strings` | function | `pub(super) fn ordered_unique_strings(values: Vec<String>) -> Vec<String> {` | `ordered_unique_strings [function]` | `009a2eef-df4f-582b-9727-973efaf8ff55` | 52-58 [crates/gwiki/src/commands/ask/assembly.rs:52-58] | Indexed function `ordered_unique_strings` in `crates/gwiki/src/commands/ask/assembly.rs`. [crates/gwiki/src/commands/ask/assembly.rs:52-58] |
| `ask_output_keeps_bounded_retrieval_shape` | function | `fn ask_output_keeps_bounded_retrieval_shape() {` | `ask_output_keeps_bounded_retrieval_shape [function]` | `68e793eb-64ce-5c2f-b12c-dd6a7914c778` | 72-120 [crates/gwiki/src/commands/ask/assembly.rs:72-120] | Indexed function `ask_output_keeps_bounded_retrieval_shape` in `crates/gwiki/src/commands/ask/assembly.rs`. [crates/gwiki/src/commands/ask/assembly.rs:72-120] |
