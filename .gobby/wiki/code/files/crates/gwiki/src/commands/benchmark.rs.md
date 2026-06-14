---
title: crates/gwiki/src/commands/benchmark.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/benchmark.rs
  ranges:
  - 11-44
  - 46-73
  - 75-81
  - 83-121
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/benchmark.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

This file implements the `gwiki benchmark` command flow. `execute` validates the benchmark options, resolves the PostgreSQL database URL, and delegates to `run_analysis_command` so the benchmark runs against the selected scope and produces a serialized report. `run_attached` performs the database-backed benchmark work: it builds AI/config context from Gobby home and PostgreSQL, resolves the benchmark inputs, and returns a `BenchmarkReport`. `search_scope_for_identity` derives the search scope from the selected output identity, and `benchmark_text` formats the final report into command output.
[crates/gwiki/src/commands/benchmark.rs:11-44]
[crates/gwiki/src/commands/benchmark.rs:46-73]
[crates/gwiki/src/commands/benchmark.rs:75-81]
[crates/gwiki/src/commands/benchmark.rs:83-121]

## API Symbols

- `execute` (function) component `execute [function]` (`36eb3cfa-0140-5fec-bfcc-78a5fd48e11c`) lines 11-44 [crates/gwiki/src/commands/benchmark.rs:11-44]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Indexed function `execute` in `crates/gwiki/src/commands/benchmark.rs`. [crates/gwiki/src/commands/benchmark.rs:11-44]
- `run_attached` (function) component `run_attached [function]` (`3c7f7188-f600-57c0-8608-e946c8dd7210`) lines 46-73 [crates/gwiki/src/commands/benchmark.rs:46-73]
  - Signature: `fn run_attached(`
  - Purpose: Indexed function `run_attached` in `crates/gwiki/src/commands/benchmark.rs`. [crates/gwiki/src/commands/benchmark.rs:46-73]
- `search_scope_for_identity` (function) component `search_scope_for_identity [function]` (`147862a7-e4ad-5a29-bcf5-28ef1c506b95`) lines 75-81 [crates/gwiki/src/commands/benchmark.rs:75-81]
  - Signature: `fn search_scope_for_identity(scope: &ScopeIdentity) -> crate::search::SearchScope {`
  - Purpose: Indexed function `search_scope_for_identity` in `crates/gwiki/src/commands/benchmark.rs`. [crates/gwiki/src/commands/benchmark.rs:75-81]
- `benchmark_text` (function) component `benchmark_text [function]` (`5ffc67db-8128-5a37-8622-d1a397a94dd6`) lines 83-121 [crates/gwiki/src/commands/benchmark.rs:83-121]
  - Signature: `fn benchmark_text(report: &benchmark::BenchmarkReport) -> String {`
  - Purpose: Indexed function `benchmark_text` in `crates/gwiki/src/commands/benchmark.rs`. [crates/gwiki/src/commands/benchmark.rs:83-121]

