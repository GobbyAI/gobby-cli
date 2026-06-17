---
title: crates/gwiki/src/commands/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/mod.rs
  ranges:
  - 31-104
  - 106-117
  - 119-143
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/mod.rs:31-104](crates/gwiki/src/commands/mod.rs#L31-L104), [crates/gwiki/src/commands/mod.rs:106-117](crates/gwiki/src/commands/mod.rs#L106-L117), [crates/gwiki/src/commands/mod.rs:119-143](crates/gwiki/src/commands/mod.rs#L119-L143)

</details>

# crates/gwiki/src/commands/mod.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This module is the command dispatcher for `gwiki`: it declares the individual command submodules and centralizes how CLI commands are executed. `run` matches each `Command` variant to the appropriate module-level `execute` function, while `scoped_outcome` and `run_analysis_command` provide shared helpers for running commands with resolved scope and for handling analysis-related command execution.
[crates/gwiki/src/commands/mod.rs:31-104]
[crates/gwiki/src/commands/mod.rs:106-117]
[crates/gwiki/src/commands/mod.rs:119-143]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `run` | function | `pub(crate) fn run(command: Command) -> Result<CommandOutcome, WikiError> {` | `run [function]` | `eaea66ca-7b18-5903-bfff-5f90b653a921` | 31-104 [crates/gwiki/src/commands/mod.rs:31-104] | Indexed function `run` in `crates/gwiki/src/commands/mod.rs`. [crates/gwiki/src/commands/mod.rs:31-104] |
| `scoped_outcome` | function | `pub(crate) fn scoped_outcome(` | `scoped_outcome [function]` | `d1f3c366-c1da-5c4d-8832-578c1ad7cafe` | 106-117 [crates/gwiki/src/commands/mod.rs:106-117] | Indexed function `scoped_outcome` in `crates/gwiki/src/commands/mod.rs`. [crates/gwiki/src/commands/mod.rs:106-117] |
| `run_analysis_command` | function | `pub(crate) fn run_analysis_command<T>(` | `run_analysis_command [function]` | `1e962369-237f-543b-ae5c-deb1d4dd596c` | 119-143 [crates/gwiki/src/commands/mod.rs:119-143] | Indexed function `run_analysis_command` in `crates/gwiki/src/commands/mod.rs`. [crates/gwiki/src/commands/mod.rs:119-143] |
