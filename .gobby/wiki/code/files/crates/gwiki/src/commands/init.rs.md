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

Implements the `init` command for wiki setup. `execute` resolves the requested scope, initializes the vault, and then registers that scope in the registry; if registration fails, it cleans up any newly created vault paths before returning the error. `render` packages the successful result into a structured JSON payload and a human-readable status message, then delegates to the shared scoped outcome formatter so the command reports the initialized scope, root path, and created directories/files consistently.
[crates/gwiki/src/commands/init.rs:9-20]
[crates/gwiki/src/commands/init.rs:22-40]

## API Symbols

- `execute` (function) component `execute [function]` (`14fc1143-adc3-5c81-adf6-f1b4513f3b65`) lines 9-20 [crates/gwiki/src/commands/init.rs:9-20]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Indexed function `execute` in `crates/gwiki/src/commands/init.rs`. [crates/gwiki/src/commands/init.rs:9-20]
- `render` (function) component `render [function]` (`b2ef46a2-b1e1-5219-af7c-0bbd643befb0`) lines 22-40 [crates/gwiki/src/commands/init.rs:22-40]
  - Signature: `fn render(scope: ScopeIdentity, root: &Path, created_paths: &CreatedVaultPaths) -> CommandOutcome {`
  - Purpose: Indexed function `render` in `crates/gwiki/src/commands/init.rs`. [crates/gwiki/src/commands/init.rs:22-40]

