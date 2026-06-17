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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/init.rs:9-20](crates/gwiki/src/commands/init.rs#L9-L20), [crates/gwiki/src/commands/init.rs:22-40](crates/gwiki/src/commands/init.rs#L22-L40)

</details>

# crates/gwiki/src/commands/init.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the `init` command for creating a wiki scope. `execute` resolves the requested scope, initializes the vault, and then registers the scope in the registry; if registration fails, it cleans up any paths created during initialization before returning the error. `render` packages the successful result into a scoped `CommandOutcome` with JSON metadata and a human-readable message, including the command name, resolved scope, root path, status, and created directories/files.
[crates/gwiki/src/commands/init.rs:9-20]
[crates/gwiki/src/commands/init.rs:22-40]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {` | `execute [function]` | `14fc1143-adc3-5c81-adf6-f1b4513f3b65` | 9-20 [crates/gwiki/src/commands/init.rs:9-20] | Indexed function `execute` in `crates/gwiki/src/commands/init.rs`. [crates/gwiki/src/commands/init.rs:9-20] |
| `render` | function | `fn render(scope: ScopeIdentity, root: &Path, created_paths: &CreatedVaultPaths) -> CommandOutcome {` | `render [function]` | `b2ef46a2-b1e1-5219-af7c-0bbd643befb0` | 22-40 [crates/gwiki/src/commands/init.rs:22-40] | Indexed function `render` in `crates/gwiki/src/commands/init.rs`. [crates/gwiki/src/commands/init.rs:22-40] |
