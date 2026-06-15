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

# crates/gwiki/src/commands/ask.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

This file implements the `ask` command as a thin retrieval-augmented generation flow: it rejects `--llm` when AI routing is `Off`, retrieves top-k search results for the query and scope selection, builds an evidence plan, assembles a grounded answer from the retrieval output, optionally runs AI synthesis over that draft, and renders the final `CommandOutcome`. The test verifies the input validation path returns `WikiError::InvalidInput` for the `ask` field before retrieval starts.
[crates/gwiki/src/commands/ask.rs:20-41]
[crates/gwiki/src/commands/ask.rs:48-62]

## API Symbols

- `execute` (function) component `execute [function]` (`28b6729a-0852-5e9f-a99e-2ab4ff125f3f`) lines 20-41 [crates/gwiki/src/commands/ask.rs:20-41]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Validates that '--llm' is not used with 'AiRouting::Off', retrieves search results for the query and selection, builds an evidence plan and base ask output, optionally synthesizes it with the AI router, and renders the final 'CommandOutcome'. [crates/gwiki/src/commands/ask.rs:20-41]
- `llm_ai_off_is_invalid_input` (function) component `llm_ai_off_is_invalid_input [function]` (`16d5d749-8099-5844-a52a-58353fb9f49e`) lines 48-62 [crates/gwiki/src/commands/ask.rs:48-62]
  - Signature: `fn llm_ai_off_is_invalid_input() {`
  - Purpose: Verifies that calling 'execute' with 'AiRouting::Off' while asking with '--llm' returns 'WikiError::InvalidInput' for the 'ask' field before retrieval begins. [crates/gwiki/src/commands/ask.rs:48-62]

