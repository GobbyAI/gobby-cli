---
title: crates/gwiki/src/commands/session_sync.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/session_sync.rs
  ranges:
  - 22-70
  - 72-83
  - 85-162
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/session_sync.rs:22-70](crates/gwiki/src/commands/session_sync.rs#L22-L70), [crates/gwiki/src/commands/session_sync.rs:72-83](crates/gwiki/src/commands/session_sync.rs#L72-L83), [crates/gwiki/src/commands/session_sync.rs:85-162](crates/gwiki/src/commands/session_sync.rs#L85-L162)

</details>

# crates/gwiki/src/commands/session_sync.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the `gwiki sync-sessions` command, which initializes the vault for the selected scope, resolves an archive directory, and syncs session transcript archives into either the Postgres-backed index path or an in-memory fallback. `execute` coordinates the flow, `archive_dir_or_default` picks the archive location, and `render_sync_sessions` turns the sync result plus index counts into the final command outcome, including a digest of accepted, skipped, and failed sessions.
[crates/gwiki/src/commands/session_sync.rs:22-70]
[crates/gwiki/src/commands/session_sync.rs:72-83]
[crates/gwiki/src/commands/session_sync.rs:85-162]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(` | `execute [function]` | `3cb3cef2-70de-5919-ba75-9e25b4b7c687` | 22-70 [crates/gwiki/src/commands/session_sync.rs:22-70] | Indexed function `execute` in `crates/gwiki/src/commands/session_sync.rs`. [crates/gwiki/src/commands/session_sync.rs:22-70] |
| `archive_dir_or_default` | function | `fn archive_dir_or_default(archive_dir: Option<PathBuf>) -> Result<PathBuf, WikiError> {` | `archive_dir_or_default [function]` | `083665da-db88-593a-829e-841820e38a04` | 72-83 [crates/gwiki/src/commands/session_sync.rs:72-83] | Indexed function `archive_dir_or_default` in `crates/gwiki/src/commands/session_sync.rs`. [crates/gwiki/src/commands/session_sync.rs:72-83] |
| `render_sync_sessions` | function | `fn render_sync_sessions(` | `render_sync_sessions [function]` | `0ca238ae-5698-5686-92a0-8f94ed932529` | 85-162 [crates/gwiki/src/commands/session_sync.rs:85-162] | Indexed function `render_sync_sessions` in `crates/gwiki/src/commands/session_sync.rs`. [crates/gwiki/src/commands/session_sync.rs:85-162] |
