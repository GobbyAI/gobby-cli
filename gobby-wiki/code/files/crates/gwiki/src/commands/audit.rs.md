---
title: crates/gwiki/src/commands/audit.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/audit.rs
  ranges:
  - 3-13
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/audit.rs:3-13](crates/gwiki/src/commands/audit.rs#L3-L13)

</details>

# crates/gwiki/src/commands/audit.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Provides the `audit` command entrypoint. `execute` delegates to `super::run_analysis_command`, supplying the command name, the caller’s `ScopeSelection`, a short analysis description, and an audit runner closure that builds `AuditOptions` from the environment before calling `audit::run_with_options`; it then formats the result with `audit::render_text` and returns a `CommandOutcome` or `WikiError`. [crates/gwiki/src/commands/audit.rs:3-13]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {` | `execute [function]` | `120069a4-7de5-57d0-8c26-8107d8dc8144` | 3-13 [crates/gwiki/src/commands/audit.rs:3-13] | Indexed function `execute` in `crates/gwiki/src/commands/audit.rs`. [crates/gwiki/src/commands/audit.rs:3-13] |
