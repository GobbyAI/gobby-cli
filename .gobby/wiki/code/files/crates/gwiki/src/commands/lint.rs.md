---
title: crates/gwiki/src/commands/lint.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/lint.rs
  ranges:
  - 3-11
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/lint.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

This file defines the `lint` command entry point for the wiki CLI. Its `execute` function takes a `ScopeSelection` and hands off to the shared analysis-command runner with the `lint` label, the lint analyzer, and the text renderer so lint results are generated and formatted consistently. [crates/gwiki/src/commands/lint.rs:3-11]

## API Symbols

- `execute` (function) component `execute [function]` (`949aa991-1cf4-5206-852b-95b77e80dfbe`) lines 3-11 [crates/gwiki/src/commands/lint.rs:3-11]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Executes a linting analysis command on the provided scope selection by delegating to a generic analysis command runner with lint-specific analysis and text rendering functions. [crates/gwiki/src/commands/lint.rs:3-11]

