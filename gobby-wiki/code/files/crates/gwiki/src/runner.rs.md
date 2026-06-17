---
title: crates/gwiki/src/runner.rs
type: code_file
provenance:
- file: crates/gwiki/src/runner.rs
  ranges:
  - 7-9
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/runner.rs:7-9](crates/gwiki/src/runner.rs#L7-L9)

</details>

# crates/gwiki/src/runner.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Provides a thin public entry point for executing a parsed `gwiki` command. `run` simply forwards the `Command` to `commands::run` and returns its `CommandOutcome` or `WikiError`, so embedders use the same dispatch path as the CLI. [crates/gwiki/src/runner.rs:7-9]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `run` | function | `pub fn run(command: Command) -> Result<CommandOutcome, WikiError> {` | `run [function]` | `b2e10e08-1c60-55dc-a672-6c3177316550` | 7-9 [crates/gwiki/src/runner.rs:7-9] | Indexed function `run` in `crates/gwiki/src/runner.rs`. [crates/gwiki/src/runner.rs:7-9] |
