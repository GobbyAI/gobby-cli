---
title: crates/gwiki/src/commands/status.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/status.rs
  ranges:
  - 6-9
  - 11-30
  - 32-36
  - 38-88
  - 90-94
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/status.rs:6-9](crates/gwiki/src/commands/status.rs#L6-L9), [crates/gwiki/src/commands/status.rs:11-30](crates/gwiki/src/commands/status.rs#L11-L30), [crates/gwiki/src/commands/status.rs:32-36](crates/gwiki/src/commands/status.rs#L32-L36), [crates/gwiki/src/commands/status.rs:38-88](crates/gwiki/src/commands/status.rs#L38-L88), [crates/gwiki/src/commands/status.rs:90-94](crates/gwiki/src/commands/status.rs#L90-L94)

</details>

# crates/gwiki/src/commands/status.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the `gwiki status` command by resolving the requested scope and turning it into a scoped status outcome. `execute` delegates scope resolution, while `render` assembles the JSON payload and human-readable text with the current daemon URL and runtime status. `runtime_status_for` derives the runtime mode and enabled services from the database and gobby home configuration, falling back to a shell-ready in-memory status when no database is configured. `RuntimeStatus` carries the status label, mode, and service details, and `gobby_home` supplies the base config location used during runtime inspection.
[crates/gwiki/src/commands/status.rs:6-9]
[crates/gwiki/src/commands/status.rs:11-30]
[crates/gwiki/src/commands/status.rs:32-36]
[crates/gwiki/src/commands/status.rs:38-88]
[crates/gwiki/src/commands/status.rs:90-94]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {` | `execute [function]` | `f49f4521-f67a-58c2-b06e-a790c40ade78` | 6-9 [crates/gwiki/src/commands/status.rs:6-9] | Indexed function `execute` in `crates/gwiki/src/commands/status.rs`. [crates/gwiki/src/commands/status.rs:6-9] |
| `render` | function | `fn render(scope: ScopeIdentity) -> Result<CommandOutcome, WikiError> {` | `render [function]` | `55b76411-5000-5411-a751-0b2024c75df4` | 11-30 [crates/gwiki/src/commands/status.rs:11-30] | Indexed function `render` in `crates/gwiki/src/commands/status.rs`. [crates/gwiki/src/commands/status.rs:11-30] |
| `RuntimeStatus` | class | `pub(crate) struct RuntimeStatus {` | `RuntimeStatus [class]` | `9cf4b19f-c80c-53b4-93b9-c4d37b348aec` | 32-36 [crates/gwiki/src/commands/status.rs:32-36] | Indexed class `RuntimeStatus` in `crates/gwiki/src/commands/status.rs`. [crates/gwiki/src/commands/status.rs:32-36] |
| `runtime_status_for` | function | `pub(crate) fn runtime_status_for(command: &'static str) -> Result<RuntimeStatus, WikiError> {` | `runtime_status_for [function]` | `88ccfa60-d0bb-5806-9c9e-4342f4e32c88` | 38-88 [crates/gwiki/src/commands/status.rs:38-88] | Indexed function `runtime_status_for` in `crates/gwiki/src/commands/status.rs`. [crates/gwiki/src/commands/status.rs:38-88] |
| `gobby_home` | function | `fn gobby_home() -> Result<std::path::PathBuf, WikiError> {` | `gobby_home [function]` | `04716bd7-08c6-56f1-957e-637d5a257494` | 90-94 [crates/gwiki/src/commands/status.rs:90-94] | Indexed function `gobby_home` in `crates/gwiki/src/commands/status.rs`. [crates/gwiki/src/commands/status.rs:90-94] |
