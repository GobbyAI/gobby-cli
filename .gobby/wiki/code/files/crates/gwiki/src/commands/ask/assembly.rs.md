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

# crates/gwiki/src/commands/ask/assembly.rs

Module: [[code/modules/crates/gwiki/src/commands/ask|crates/gwiki/src/commands/ask]]

## Purpose

Builds the `AskOutput` returned from retrieval-backed `ask` commands. `ask_output_from_retrieval` converts a `SearchOutput` plus an `EvidencePlan` into a bounded response shape: it derives a deduplicated source list, records degradation warnings, sets status based on whether any hits were found, marks truncation when evidence was dropped, and copies through the retrieved hits, code citations, and planned evidence. `unique_sources` collects unique source paths from both hit origins and per-hit source lists, while `ordered_unique_strings` removes duplicates from warning/degradation strings without changing their first-seen order. The test verifies the assembled output preserves the expected retrieval shape and bounded evidence metadata.
[crates/gwiki/src/commands/ask/assembly.rs:6-39]
[crates/gwiki/src/commands/ask/assembly.rs:41-50]
[crates/gwiki/src/commands/ask/assembly.rs:52-58]
[crates/gwiki/src/commands/ask/assembly.rs:72-120]

## API Symbols

- `ask_output_from_retrieval` (function) component `ask_output_from_retrieval [function]` (`78236031-e711-5a4a-adcf-5aad42ecb73c`) lines 6-39 [crates/gwiki/src/commands/ask/assembly.rs:6-39]
  - Signature: `pub(super) fn ask_output_from_retrieval(search: SearchOutput, plan: &EvidencePlan) -> AskOutput {`
  - Purpose: Indexed function `ask_output_from_retrieval` in `crates/gwiki/src/commands/ask/assembly.rs`. [crates/gwiki/src/commands/ask/assembly.rs:6-39]
- `unique_sources` (function) component `unique_sources [function]` (`a1e580a1-5c5a-5f60-ab2c-2852b53707e9`) lines 41-50 [crates/gwiki/src/commands/ask/assembly.rs:41-50]
  - Signature: `fn unique_sources(search: &SearchOutput) -> Vec<String> {`
  - Purpose: Indexed function `unique_sources` in `crates/gwiki/src/commands/ask/assembly.rs`. [crates/gwiki/src/commands/ask/assembly.rs:41-50]
- `ordered_unique_strings` (function) component `ordered_unique_strings [function]` (`009a2eef-df4f-582b-9727-973efaf8ff55`) lines 52-58 [crates/gwiki/src/commands/ask/assembly.rs:52-58]
  - Signature: `pub(super) fn ordered_unique_strings(values: Vec<String>) -> Vec<String> {`
  - Purpose: Indexed function `ordered_unique_strings` in `crates/gwiki/src/commands/ask/assembly.rs`. [crates/gwiki/src/commands/ask/assembly.rs:52-58]
- `ask_output_keeps_bounded_retrieval_shape` (function) component `ask_output_keeps_bounded_retrieval_shape [function]` (`68e793eb-64ce-5c2f-b12c-dd6a7914c778`) lines 72-120 [crates/gwiki/src/commands/ask/assembly.rs:72-120]
  - Signature: `fn ask_output_keeps_bounded_retrieval_shape() {`
  - Purpose: Indexed function `ask_output_keeps_bounded_retrieval_shape` in `crates/gwiki/src/commands/ask/assembly.rs`. [crates/gwiki/src/commands/ask/assembly.rs:72-120]

