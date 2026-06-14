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

# crates/gwiki/src/commands/status.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

This file implements the `gwiki status` command. `execute` resolves the requested scope and passes it to `render`, which gathers the daemon URL and runtime details, builds both structured JSON and a human-readable summary, and returns a scoped command outcome. `RuntimeStatus` is the small data carrier for the status fields. `runtime_status_for` determines runtime mode by first checking whether a database URL is available: if not, it reports a shell-ready, memory-only state; otherwise it opens a read-only PostgreSQL connection, loads configuration from the Gobby home directory, and derives service configuration such as FalkorDB, Qdrant, and embeddings. `gobby_home` supplies the local Gobby home path used during that config resolution.
[crates/gwiki/src/commands/status.rs:6-9]
[crates/gwiki/src/commands/status.rs:11-30]
[crates/gwiki/src/commands/status.rs:32-36]
[crates/gwiki/src/commands/status.rs:38-88]
[crates/gwiki/src/commands/status.rs:90-94]

## API Symbols

- `execute` (function) component `execute [function]` (`f49f4521-f67a-58c2-b06e-a790c40ade78`) lines 6-9 [crates/gwiki/src/commands/status.rs:6-9]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Indexed function `execute` in `crates/gwiki/src/commands/status.rs`. [crates/gwiki/src/commands/status.rs:6-9]
- `render` (function) component `render [function]` (`55b76411-5000-5411-a751-0b2024c75df4`) lines 11-30 [crates/gwiki/src/commands/status.rs:11-30]
  - Signature: `fn render(scope: ScopeIdentity) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Indexed function `render` in `crates/gwiki/src/commands/status.rs`. [crates/gwiki/src/commands/status.rs:11-30]
- `RuntimeStatus` (class) component `RuntimeStatus [class]` (`9cf4b19f-c80c-53b4-93b9-c4d37b348aec`) lines 32-36 [crates/gwiki/src/commands/status.rs:32-36]
  - Signature: `pub(crate) struct RuntimeStatus {`
  - Purpose: Indexed class `RuntimeStatus` in `crates/gwiki/src/commands/status.rs`. [crates/gwiki/src/commands/status.rs:32-36]
- `runtime_status_for` (function) component `runtime_status_for [function]` (`88ccfa60-d0bb-5806-9c9e-4342f4e32c88`) lines 38-88 [crates/gwiki/src/commands/status.rs:38-88]
  - Signature: `pub(crate) fn runtime_status_for(command: &'static str) -> Result<RuntimeStatus, WikiError> {`
  - Purpose: Indexed function `runtime_status_for` in `crates/gwiki/src/commands/status.rs`. [crates/gwiki/src/commands/status.rs:38-88]
- `gobby_home` (function) component `gobby_home [function]` (`04716bd7-08c6-56f1-957e-637d5a257494`) lines 90-94 [crates/gwiki/src/commands/status.rs:90-94]
  - Signature: `fn gobby_home() -> Result<std::path::PathBuf, WikiError> {`
  - Purpose: Indexed function `gobby_home` in `crates/gwiki/src/commands/status.rs`. [crates/gwiki/src/commands/status.rs:90-94]

