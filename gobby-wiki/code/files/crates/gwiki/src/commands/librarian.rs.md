---
title: crates/gwiki/src/commands/librarian.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/librarian.rs
  ranges:
  - 3-11
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/librarian.rs:3-11](crates/gwiki/src/commands/librarian.rs#L3-L11)

</details>

# crates/gwiki/src/commands/librarian.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Provides the `librarian` command entry point for the wiki CLI. It delegates to the shared analysis-command runner with the `"librarian"` label, the selected scope, the description `"serialize librarian proposals report"`, the default librarian options, and the librarian text renderer so the command analyzes the wiki data and renders the resulting report. [crates/gwiki/src/commands/librarian.rs:3-11]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {` | `execute [function]` | `ce00f6fd-84c3-5e9b-940b-9e677acbac9c` | 3-11 [crates/gwiki/src/commands/librarian.rs:3-11] | Indexed function `execute` in `crates/gwiki/src/commands/librarian.rs`. [crates/gwiki/src/commands/librarian.rs:3-11] |
