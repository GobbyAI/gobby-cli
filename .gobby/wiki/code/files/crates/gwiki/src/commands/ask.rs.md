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

This file implements the `ask` command as a thin RAG pipeline over search: it retrieves a bounded set of hits, turns them into an evidence plan, assembles an output structure, optionally runs LLM synthesis, and then renders the final result. It also rejects `--llm` when AI routing is `Off`, and the included test verifies that invalid input is caught before retrieval.
[crates/gwiki/src/commands/ask.rs:20-41]
[crates/gwiki/src/commands/ask.rs:48-62]

## API Symbols

- `execute` (function) component `execute [function]` (`28b6729a-0852-5e9f-a99e-2ab4ff125f3f`) lines 20-41 [crates/gwiki/src/commands/ask.rs:20-41]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Indexed function `execute` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:20-41]
- `llm_ai_off_is_invalid_input` (function) component `llm_ai_off_is_invalid_input [function]` (`16d5d749-8099-5844-a52a-58353fb9f49e`) lines 48-62 [crates/gwiki/src/commands/ask.rs:48-62]
  - Signature: `fn llm_ai_off_is_invalid_input() {`
  - Purpose: Indexed function `llm_ai_off_is_invalid_input` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:48-62]

