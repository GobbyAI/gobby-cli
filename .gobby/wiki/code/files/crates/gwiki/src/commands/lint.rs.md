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

`crates/gwiki/src/commands/lint.rs` exposes 1 indexed API symbol. [crates/gwiki/src/commands/lint.rs:3-11]

## API Symbols

- `execute` (function) component `execute [function]` (`949aa991-1cf4-5206-852b-95b77e80dfbe`) lines 3-11 [crates/gwiki/src/commands/lint.rs:3-11]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Executes a linting analysis command on the provided scope selection by delegating to a generic analysis command runner with lint-specific analysis and text rendering functions. [crates/gwiki/src/commands/lint.rs:3-11]

