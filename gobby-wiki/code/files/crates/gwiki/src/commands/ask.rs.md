---
title: crates/gwiki/src/commands/ask.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/ask.rs
  ranges:
  - 20-41
  - 48-62
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/ask.rs:20-41](crates/gwiki/src/commands/ask.rs#L20-L41), [crates/gwiki/src/commands/ask.rs:48-62](crates/gwiki/src/commands/ask.rs#L48-L62)

</details>

# crates/gwiki/src/commands/ask.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the `ask` command as a thin retrieval-augmented generation pipeline over `search`: it validates that `--llm` is not used with `--ai off`, retrieves the top matches for a query within the selected scope, derives an evidence plan from those results, builds an `ask` output from the retrieved text, optionally runs LLM synthesis when enabled, and then renders the final `CommandOutcome`. The test covers the input guard by asserting that `--llm` plus `AiRouting::Off` fails before retrieval.
[crates/gwiki/src/commands/ask.rs:20-41]
[crates/gwiki/src/commands/ask.rs:48-62]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(` | `execute [function]` | `28b6729a-0852-5e9f-a99e-2ab4ff125f3f` | 20-41 [crates/gwiki/src/commands/ask.rs:20-41] | Indexed function `execute` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:20-41] |
| `llm_ai_off_is_invalid_input` | function | `fn llm_ai_off_is_invalid_input() {` | `llm_ai_off_is_invalid_input [function]` | `16d5d749-8099-5844-a52a-58353fb9f49e` | 48-62 [crates/gwiki/src/commands/ask.rs:48-62] | Indexed function `llm_ai_off_is_invalid_input` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:48-62] |
