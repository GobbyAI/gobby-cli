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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/lint.rs:3-11](crates/gwiki/src/commands/lint.rs#L3-L11)

</details>

# crates/gwiki/src/commands/lint.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file exposes the `lint` command entry point. Its `execute` function takes a `ScopeSelection` and delegates to `super::run_analysis_command`, wiring together the command name, selection, a report-serialization label, and the `lint::run` and `lint::render_text` helpers so lint analysis is executed and formatted into a `CommandOutcome` or `WikiError`. [crates/gwiki/src/commands/lint.rs:3-11]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {` | `execute [function]` | `949aa991-1cf4-5206-852b-95b77e80dfbe` | 3-11 [crates/gwiki/src/commands/lint.rs:3-11] | Indexed function `execute` in `crates/gwiki/src/commands/lint.rs`. [crates/gwiki/src/commands/lint.rs:3-11] |
