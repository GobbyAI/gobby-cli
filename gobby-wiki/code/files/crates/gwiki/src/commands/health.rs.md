---
title: crates/gwiki/src/commands/health.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/health.rs
  ranges:
  - 4-19
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/health.rs:4-19](crates/gwiki/src/commands/health.rs#L4-L19)

</details>

# crates/gwiki/src/commands/health.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Resolves the command’s target scope from the caller’s selection, runs the wiki health check for that scope, serializes the resulting report to JSON, and wraps both the structured payload and rendered text into a scoped `CommandOutcome`. The pieces work together in a small pipeline: scope resolution, health report generation, JSON conversion, and final outcome construction. [crates/gwiki/src/commands/health.rs:4-19]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {` | `execute [function]` | `1bfb51ea-113b-5885-af3d-f5ac0d32b8fc` | 4-19 [crates/gwiki/src/commands/health.rs:4-19] | Indexed function `execute` in `crates/gwiki/src/commands/health.rs`. [crates/gwiki/src/commands/health.rs:4-19] |
