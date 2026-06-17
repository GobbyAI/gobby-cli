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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/refresh/mod.rs:29-37](crates/gwiki/src/commands/refresh/mod.rs#L29-L37), [crates/gwiki/src/commands/refresh/mod.rs:39-49](crates/gwiki/src/commands/refresh/mod.rs#L39-L49), [crates/gwiki/src/commands/refresh/mod.rs:51-140](crates/gwiki/src/commands/refresh/mod.rs#L51-L140)

</details>

# crates/gwiki/src/commands/refresh/mod.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This module implements the `refresh` command for gwiki, with a small entrypoint layer and a core resolver that drives the refresh workflow. `execute` accepts a scope selection and source IDs, delegates URL fetching through `execute_with_fetcher`, and the resolved path in `execute_resolved_with_fetcher` validates the scope root, reads the source manifest, selects matching sources, and either renders a dry-run result or proceeds with refresh processing, tracking planned, skipped, failed, and index-related outcomes.
[crates/gwiki/src/commands/refresh/mod.rs:29-37]
[crates/gwiki/src/commands/refresh/mod.rs:39-49]
[crates/gwiki/src/commands/refresh/mod.rs:51-140]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(` | `execute [function]` | `8da3eaa0-5c03-5427-89ae-c1f0d1e62003` | 29-37 [crates/gwiki/src/commands/refresh/mod.rs:29-37] | Indexed function `execute` in `crates/gwiki/src/commands/refresh/mod.rs`. [crates/gwiki/src/commands/refresh/mod.rs:29-37] |
| `execute_with_fetcher` | function | `fn execute_with_fetcher(` | `execute_with_fetcher [function]` | `d74e7588-1bd5-5eb1-86df-553481328145` | 39-49 [crates/gwiki/src/commands/refresh/mod.rs:39-49] | Indexed function `execute_with_fetcher` in `crates/gwiki/src/commands/refresh/mod.rs`. [crates/gwiki/src/commands/refresh/mod.rs:39-49] |
| `execute_resolved_with_fetcher` | function | `fn execute_resolved_with_fetcher(` | `execute_resolved_with_fetcher [function]` | `874650ac-0dff-502a-8035-6405ea9310d4` | 51-140 [crates/gwiki/src/commands/refresh/mod.rs:51-140] | Indexed function `execute_resolved_with_fetcher` in `crates/gwiki/src/commands/refresh/mod.rs`. [crates/gwiki/src/commands/refresh/mod.rs:51-140] |
