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

# crates/gwiki/src/commands/audit.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

Provides the `audit` command entry point for wiki analysis. It delegates to the shared analysis-command runner with the `audit` label, uses environment-derived `AuditOptions` to run the audit over the selected scope, and renders the resulting report as plain text. [crates/gwiki/src/commands/audit.rs:3-13]

## API Symbols

- `execute` (function) component `execute [function]` (`120069a4-7de5-57d0-8c26-8107d8dc8144`) lines 3-13 [crates/gwiki/src/commands/audit.rs:3-13]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Executes an audit analysis command on the specified scope selection using environment-configured audit options and renders the output as text. [crates/gwiki/src/commands/audit.rs:3-13]

