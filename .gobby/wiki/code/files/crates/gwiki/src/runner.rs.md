---
title: crates/gwiki/src/runner.rs
type: code_file
provenance:
- file: crates/gwiki/src/runner.rs
  ranges:
  - 7-9
  - 12-17
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/runner.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/runner.rs` exposes 2 indexed API symbols.
[crates/gwiki/src/runner.rs:7-9]
[crates/gwiki/src/runner.rs:12-17]

## API Symbols

- `run` (function) component `run [function]` (`e8640ebb-f5be-59f5-8962-d1bb52b1e1e6`) lines 7-9 [crates/gwiki/src/runner.rs:7-9]
  - Signature: `pub fn run(command: Command) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Delegates command execution to the `commands::run` function, returning a `Result` that yields either a `CommandOutcome` on success or a `WikiError` on failure. [crates/gwiki/src/runner.rs:7-9]
- `resolve_research_scope` (function) component `resolve_research_scope [function]` (`7adca276-0c13-5f9d-b358-0ce2b28f46c5`) lines 12-17 [crates/gwiki/src/runner.rs:12-17]
  - Signature: `pub fn resolve_research_scope(`
  - Purpose: Resolves a `ScopeSelection` into a `ResearchScope` by delegating to the command scope resolver and converting the result, propagating `WikiError` on failure. [crates/gwiki/src/runner.rs:12-17]

