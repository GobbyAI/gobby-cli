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

Builds `AskOutput` for the `ask` command from search retrieval and evidence planning data, turning `SearchOutput` plus an `EvidencePlan` into a normalized result with deduplicated source paths, deduplicated degradations/warnings, derived retrieval status and truncation fields, and copied hits, evidence, and prompt-budget metadata. The helper functions `unique_sources` and `ordered_unique_strings` handle source and string deduplication, and the test verifies that a bounded retrieval is assembled into the expected retrieved/ask shape without truncating the prompt budget.
[crates/gwiki/src/commands/ask/assembly.rs:6-39]
[crates/gwiki/src/commands/ask/assembly.rs:41-50]
[crates/gwiki/src/commands/ask/assembly.rs:52-58]
[crates/gwiki/src/commands/ask/assembly.rs:72-120]

## API Symbols

- `ask_output_from_retrieval` (function) component `ask_output_from_retrieval [function]` (`78236031-e711-5a4a-adcf-5aad42ecb73c`) lines 6-39 [crates/gwiki/src/commands/ask/assembly.rs:6-39]
  - Signature: `pub(super) fn ask_output_from_retrieval(search: SearchOutput, plan: &EvidencePlan) -> AskOutput {`
  - Purpose: Builds an 'AskOutput' from 'SearchOutput' and an 'EvidencePlan' by deduplicating sources and degradations, deriving retrieval status and truncation flags, copying search/evidence fields, and initializing prompt-budget, warning, and AI synthesis fields. [crates/gwiki/src/commands/ask/assembly.rs:6-39]
- `unique_sources` (function) component `unique_sources [function]` (`a1e580a1-5c5a-5f60-ab2c-2852b53707e9`) lines 41-50 [crates/gwiki/src/commands/ask/assembly.rs:41-50]
  - Signature: `fn unique_sources(search: &SearchOutput) -> Vec<String> {`
  - Purpose: Returns a sorted 'Vec<String>' of all distinct source path strings found in 'search.results', combining each hit’s 'source_path' and every string in its 'sources' field. [crates/gwiki/src/commands/ask/assembly.rs:41-50]
- `ordered_unique_strings` (function) component `ordered_unique_strings [function]` (`009a2eef-df4f-582b-9727-973efaf8ff55`) lines 52-58 [crates/gwiki/src/commands/ask/assembly.rs:52-58]
  - Signature: `pub(super) fn ordered_unique_strings(values: Vec<String>) -> Vec<String> {`
  - Purpose: Returns the input 'Vec<String>' with duplicates removed, preserving the first occurrence of each string in original order by filtering through a 'BTreeSet' of seen values. [crates/gwiki/src/commands/ask/assembly.rs:52-58]
- `ask_output_keeps_bounded_retrieval_shape` (function) component `ask_output_keeps_bounded_retrieval_shape [function]` (`68e793eb-64ce-5c2f-b12c-dd6a7914c778`) lines 72-120 [crates/gwiki/src/commands/ask/assembly.rs:72-120]
  - Signature: `fn ask_output_keeps_bounded_retrieval_shape() {`
  - Purpose: Verifies that 'ask_output_from_retrieval' converts a bounded 'SearchRetrieval' into an 'ask'/'retrieved' output while preserving the query, one hit and one evidence item, normalizing sources and warnings, and keeping the prompt budget untruncated. [crates/gwiki/src/commands/ask/assembly.rs:72-120]

