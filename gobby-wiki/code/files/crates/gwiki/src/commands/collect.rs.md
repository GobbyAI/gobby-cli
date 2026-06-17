---
title: crates/gwiki/src/commands/collect.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/collect.rs
  ranges:
  - 10-20
  - 22-43
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/collect.rs:10-20](crates/gwiki/src/commands/collect.rs#L10-L20), [crates/gwiki/src/commands/collect.rs:22-43](crates/gwiki/src/commands/collect.rs#L22-L43)

</details>

# crates/gwiki/src/commands/collect.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the `collect` command for a wiki scope: `execute` resolves the requested scope, ensures the vault paths exist, creates an in-memory store, captures a collection timestamp, and runs inbox/index collection over the scope root. `render` turns the resulting `CollectReport` into a scoped `CommandOutcome` with JSON payload and human-readable status text, including accepted and skipped counts.
[crates/gwiki/src/commands/collect.rs:10-20]
[crates/gwiki/src/commands/collect.rs:22-43]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {` | `execute [function]` | `b82f162e-63a4-5a97-b033-94faa99f166d` | 10-20 [crates/gwiki/src/commands/collect.rs:10-20] | Indexed function `execute` in `crates/gwiki/src/commands/collect.rs`. [crates/gwiki/src/commands/collect.rs:10-20] |
| `render` | function | `fn render(scope: ScopeIdentity, root: &Path, report: CollectReport) -> CommandOutcome {` | `render [function]` | `e6c80f4c-f0f7-5dfc-b6f6-1903106e80b6` | 22-43 [crates/gwiki/src/commands/collect.rs:22-43] | Indexed function `render` in `crates/gwiki/src/commands/collect.rs`. [crates/gwiki/src/commands/collect.rs:22-43] |
