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

Implements the `gwiki status` command by resolving the requested scope, gathering daemon and runtime state, and returning a scoped `CommandOutcome` with both JSON payload and human-readable text. The command reports the resolved scope identity, daemon URL, and runtime mode/status together so callers can see whether the app is running in a shell-only memory mode or backed by PostgreSQL with configured services. `runtime_status_for` handles that runtime probe, while `gobby_home` adapts Gobby home resolution into a `WikiError` for status reporting.
[crates/gwiki/src/commands/status.rs:6-9]
[crates/gwiki/src/commands/status.rs:11-30]
[crates/gwiki/src/commands/status.rs:32-36]
[crates/gwiki/src/commands/status.rs:38-88]
[crates/gwiki/src/commands/status.rs:90-94]

## API Symbols

- `execute` (function) component `execute [function]` (`f49f4521-f67a-58c2-b06e-a790c40ade78`) lines 6-9 [crates/gwiki/src/commands/status.rs:6-9]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Resolves the command scope from the provided 'ScopeSelection' and renders the resolved scope identity, returning the resulting 'CommandOutcome' or a 'WikiError'. [crates/gwiki/src/commands/status.rs:6-9]
- `render` (function) component `render [function]` (`55b76411-5000-5411-a751-0b2024c75df4`) lines 11-30 [crates/gwiki/src/commands/status.rs:11-30]
  - Signature: `fn render(scope: ScopeIdentity) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Constructs and returns a scoped 'CommandOutcome' for the 'status' command by reading the daemon URL and runtime status, packaging them into a JSON payload, and formatting a human-readable summary string. [crates/gwiki/src/commands/status.rs:11-30]
- `RuntimeStatus` (class) component `RuntimeStatus [class]` (`9cf4b19f-c80c-53b4-93b9-c4d37b348aec`) lines 32-36 [crates/gwiki/src/commands/status.rs:32-36]
  - Signature: `pub(crate) struct RuntimeStatus {`
  - Purpose: 'RuntimeStatus' is an internal Rust struct that carries three runtime reporting fields: a static status string, a static mode string, and a JSON value containing service data. [crates/gwiki/src/commands/status.rs:32-36]
- `runtime_status_for` (function) component `runtime_status_for [function]` (`88ccfa60-d0bb-5806-9c9e-4342f4e32c88`) lines 38-88 [crates/gwiki/src/commands/status.rs:38-88]
  - Signature: `pub(crate) fn runtime_status_for(command: &'static str) -> Result<RuntimeStatus, WikiError> {`
  - Purpose: 'runtime_status_for' returns a 'RuntimeStatus' that reports '"shell-ready"' with '"memory"' mode and no services when no database URL is configured, otherwise connects read-only to PostgreSQL, resolves runtime config from Gobby home, and returns '"datastore-ready"' with '"postgres"' mode plus configuration status for PostgreSQL, FalkorDB, Qdrant, and embeddings. [crates/gwiki/src/commands/status.rs:38-88]
- `gobby_home` (function) component `gobby_home [function]` (`04716bd7-08c6-56f1-957e-637d5a257494`) lines 90-94 [crates/gwiki/src/commands/status.rs:90-94]
  - Signature: `fn gobby_home() -> Result<std::path::PathBuf, WikiError> {`
  - Purpose: Resolves the Gobby home directory by delegating to 'gobby_core::gobby_home()' and converts any resolution error into a 'WikiError::Config' with a 'failed to resolve Gobby home for gwiki status' message. [crates/gwiki/src/commands/status.rs:90-94]

