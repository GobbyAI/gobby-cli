---
title: crates/gwiki/src/commands/refresh/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/refresh/mod.rs
  ranges:
  - 29-37
  - 39-49
  - 51-140
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh/mod.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Purpose

Implements the `refresh` command for gwiki source re-ingestion and index maintenance. `execute` is the public entry point, `execute_with_fetcher` resolves the command scope and injects URL fetching, and `execute_resolved_with_fetcher` does the real work: it validates the scope, reads the source manifest, selects requested sources, handles dry-run rendering, and then coordinates the refresh/update flow using the module’s helper subcomponents.
[crates/gwiki/src/commands/refresh/mod.rs:29-37]
[crates/gwiki/src/commands/refresh/mod.rs:39-49]
[crates/gwiki/src/commands/refresh/mod.rs:51-140]

## API Symbols

- `execute` (function) component `execute [function]` (`8da3eaa0-5c03-5427-89ae-c1f0d1e62003`) lines 29-37 [crates/gwiki/src/commands/refresh/mod.rs:29-37]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Indexed function `execute` in `crates/gwiki/src/commands/refresh/mod.rs`. [crates/gwiki/src/commands/refresh/mod.rs:29-37]
- `execute_with_fetcher` (function) component `execute_with_fetcher [function]` (`d74e7588-1bd5-5eb1-86df-553481328145`) lines 39-49 [crates/gwiki/src/commands/refresh/mod.rs:39-49]
  - Signature: `fn execute_with_fetcher(`
  - Purpose: Indexed function `execute_with_fetcher` in `crates/gwiki/src/commands/refresh/mod.rs`. [crates/gwiki/src/commands/refresh/mod.rs:39-49]
- `execute_resolved_with_fetcher` (function) component `execute_resolved_with_fetcher [function]` (`874650ac-0dff-502a-8035-6405ea9310d4`) lines 51-140 [crates/gwiki/src/commands/refresh/mod.rs:51-140]
  - Signature: `fn execute_resolved_with_fetcher(`
  - Purpose: Indexed function `execute_resolved_with_fetcher` in `crates/gwiki/src/commands/refresh/mod.rs`. [crates/gwiki/src/commands/refresh/mod.rs:51-140]

