---
title: crates/gwiki/src/commands/init.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/init.rs
  ranges:
  - 9-20
  - 22-40
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/init.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

Implements the `init` command for a wiki scope: `execute` resolves the requested scope, initializes the vault, and if scope registration fails it rolls back the created paths before returning the error. On success it derives the resolved scope identity and hands the root path plus created directories/files to `render`, which packages them into a JSON payload, formats the initialization status text, and delegates to `super::scoped_outcome` to produce the final `CommandOutcome`.
[crates/gwiki/src/commands/init.rs:9-20]
[crates/gwiki/src/commands/init.rs:22-40]

## API Symbols

- `execute` (function) component `execute [function]` (`14fc1143-adc3-5c81-adf6-f1b4513f3b65`) lines 9-20 [crates/gwiki/src/commands/init.rs:9-20]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Resolves the command scope from the selection, initializes the vault for that scope, rolls back created paths if scope registration fails, and otherwise returns a rendered 'CommandOutcome' for the resolved scope identity and created paths. [crates/gwiki/src/commands/init.rs:9-20]
- `render` (function) component `render [function]` (`b2ef46a2-b1e1-5219-af7c-0bbd643befb0`) lines 22-40 [crates/gwiki/src/commands/init.rs:22-40]
  - Signature: `fn render(scope: ScopeIdentity, root: &Path, created_paths: &CreatedVaultPaths) -> CommandOutcome {`
  - Purpose: Builds an 'init' command outcome by serializing the scope, root path, and created directories/files into a JSON payload, formatting an initialization status message, and delegating to 'super::scoped_outcome'. [crates/gwiki/src/commands/init.rs:22-40]

