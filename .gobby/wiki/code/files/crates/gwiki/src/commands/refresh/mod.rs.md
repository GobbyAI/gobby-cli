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

This module implements the `refresh` command for a wiki scope: it resolves the requested scope, loads the source manifest, selects which sources to process, and either renders a dry-run plan or executes the refresh pipeline. `execute` wires the default URL snapshot fetcher into `execute_with_fetcher`, which passes through to `execute_resolved_with_fetcher`; that core function handles scope validation, source selection, per-source refresh logic for URL and local replay kinds, and accumulation of refreshed, unchanged, failed, skipped, and degradation results into a `CommandOutcome` or `WikiError`.
[crates/gwiki/src/commands/refresh/mod.rs:29-37]
[crates/gwiki/src/commands/refresh/mod.rs:39-49]
[crates/gwiki/src/commands/refresh/mod.rs:51-140]

## API Symbols

- `execute` (function) component `execute [function]` (`8da3eaa0-5c03-5427-89ae-c1f0d1e62003`) lines 29-37 [crates/gwiki/src/commands/refresh/mod.rs:29-37]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Dispatches scope-based wiki ingestion by forwarding the selection, source ID list, and dry-run flag to 'execute_with_fetcher', using a URL snapshot fetcher built from 'refresh_url(record)' and 'fetched_at', and returns the resulting 'CommandOutcome' or 'WikiError'. [crates/gwiki/src/commands/refresh/mod.rs:29-37]
- `execute_with_fetcher` (function) component `execute_with_fetcher [function]` (`d74e7588-1bd5-5eb1-86df-553481328145`) lines 39-49 [crates/gwiki/src/commands/refresh/mod.rs:39-49]
  - Signature: `fn execute_with_fetcher(`
  - Purpose: Resolves the command scope from 'selection' and delegates to 'execute_resolved_with_fetcher', passing through 'source_ids', 'dry_run', and the provided mutable fetch callback unchanged. [crates/gwiki/src/commands/refresh/mod.rs:39-49]
- `execute_resolved_with_fetcher` (function) component `execute_resolved_with_fetcher [function]` (`874650ac-0dff-502a-8035-6405ea9310d4`) lines 51-140 [crates/gwiki/src/commands/refresh/mod.rs:51-140]
  - Signature: `fn execute_resolved_with_fetcher(`
  - Purpose: 'execute_resolved_with_fetcher' validates the scope, loads the source manifest, selects requested sources, returns a dry-run render if requested, otherwise timestamps the run and refreshes each planned source by replay kind using the injected fetcher for URL candidates and local refresh logic for local files while accumulating refreshed, unchanged, failed, and degradation results into a 'CommandOutcome'/'WikiError' result. [crates/gwiki/src/commands/refresh/mod.rs:51-140]

