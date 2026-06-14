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

# crates/gwiki/src/commands/collect.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

Implements the `collect` command for a wiki scope. `execute` resolves the requested scope, initializes the vault so required paths exist, creates a fresh `MemoryWikiStore`, captures a collect timestamp, and runs `collect_inbox_and_index` against the scope root to produce a `CollectReport`. `render` turns that report into a `CommandOutcome` with a ready status, the scope and root path, accepted/skipped counts, and the full report payload, emitting both JSON and human-readable text through the shared scoped outcome helper.
[crates/gwiki/src/commands/collect.rs:10-20]
[crates/gwiki/src/commands/collect.rs:22-43]

## API Symbols

- `execute` (function) component `execute [function]` (`b82f162e-63a4-5a97-b033-94faa99f166d`) lines 10-20 [crates/gwiki/src/commands/collect.rs:10-20]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Resolves a wiki scope, initializes its vault, collects inbox and index contents into a MemoryWikiStore with a current timestamp, and renders the resulting report. [crates/gwiki/src/commands/collect.rs:10-20]
- `render` (function) component `render [function]` (`e6c80f4c-f0f7-5dfc-b6f6-1903106e80b6`) lines 22-43 [crates/gwiki/src/commands/collect.rs:22-43]
  - Signature: `fn render(scope: ScopeIdentity, root: &Path, report: CollectReport) -> CommandOutcome {`
  - Purpose: This function constructs a `CommandOutcome` that reports a collect operation's ready status with accepted/skipped item metrics in both JSON and formatted text representations. [crates/gwiki/src/commands/collect.rs:22-43]

