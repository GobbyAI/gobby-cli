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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/benchmark.rs:11-44](crates/gwiki/src/commands/benchmark.rs#L11-L44), [crates/gwiki/src/commands/benchmark.rs:46-73](crates/gwiki/src/commands/benchmark.rs#L46-L73), [crates/gwiki/src/commands/benchmark.rs:75-81](crates/gwiki/src/commands/benchmark.rs#L75-L81), [crates/gwiki/src/commands/benchmark.rs:83-121](crates/gwiki/src/commands/benchmark.rs#L83-L121)

</details>

# crates/gwiki/src/commands/benchmark.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the `gwiki benchmark` command by validating options, requiring a PostgreSQL-backed indexed project, and then running the benchmark as an analysis command. `execute` prepares the database connection and delegates into `run_attached`, which resolves Gobby/AI config from the Gobby home, builds the search and retrieval context, and produces a `BenchmarkReport`; `search_scope_for_identity` maps the output scope into the search scope used for evaluation, and `benchmark_text` serializes the final benchmark report for command output.
[crates/gwiki/src/commands/benchmark.rs:11-44]
[crates/gwiki/src/commands/benchmark.rs:46-73]
[crates/gwiki/src/commands/benchmark.rs:75-81]
[crates/gwiki/src/commands/benchmark.rs:83-121]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(` | `execute [function]` | `36eb3cfa-0140-5fec-bfcc-78a5fd48e11c` | 11-44 [crates/gwiki/src/commands/benchmark.rs:11-44] | Indexed function `execute` in `crates/gwiki/src/commands/benchmark.rs`. [crates/gwiki/src/commands/benchmark.rs:11-44] |
| `run_attached` | function | `fn run_attached(` | `run_attached [function]` | `3c7f7188-f600-57c0-8608-e946c8dd7210` | 46-73 [crates/gwiki/src/commands/benchmark.rs:46-73] | Indexed function `run_attached` in `crates/gwiki/src/commands/benchmark.rs`. [crates/gwiki/src/commands/benchmark.rs:46-73] |
| `search_scope_for_identity` | function | `fn search_scope_for_identity(scope: &ScopeIdentity) -> crate::search::SearchScope {` | `search_scope_for_identity [function]` | `147862a7-e4ad-5a29-bcf5-28ef1c506b95` | 75-81 [crates/gwiki/src/commands/benchmark.rs:75-81] | Indexed function `search_scope_for_identity` in `crates/gwiki/src/commands/benchmark.rs`. [crates/gwiki/src/commands/benchmark.rs:75-81] |
| `benchmark_text` | function | `fn benchmark_text(report: &benchmark::BenchmarkReport) -> String {` | `benchmark_text [function]` | `5ffc67db-8128-5a37-8622-d1a397a94dd6` | 83-121 [crates/gwiki/src/commands/benchmark.rs:83-121] | Indexed function `benchmark_text` in `crates/gwiki/src/commands/benchmark.rs`. [crates/gwiki/src/commands/benchmark.rs:83-121] |
