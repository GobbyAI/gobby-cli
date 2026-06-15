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

Implements the `gwiki benchmark` command pipeline: `execute` validates options, requires a configured PostgreSQL-backed project, opens a read-only connection, derives the search scope, and delegates to `run_analysis_command` to produce a serialized `CommandOutcome` or `WikiError`. The helper `run_attached` resolves benchmark inputs from Gobby home, Postgres, and optional AI/context sources before building a `BenchmarkReport`, while `search_scope_for_identity` maps scope identities into concrete search scopes and `benchmark_text` renders the report as a human-readable summary with scope, compression, graph coverage, retrieval precision, source mix, and degraded-source details.
[crates/gwiki/src/commands/benchmark.rs:11-44]
[crates/gwiki/src/commands/benchmark.rs:46-73]
[crates/gwiki/src/commands/benchmark.rs:75-81]
[crates/gwiki/src/commands/benchmark.rs:83-121]

## API Symbols

- `execute` (function) component `execute [function]` (`36eb3cfa-0140-5fec-bfcc-78a5fd48e11c`) lines 11-44 [crates/gwiki/src/commands/benchmark.rs:11-44]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Validates that 'retrieval_candidates' is nonzero, requires a configured PostgreSQL database, then runs the benchmark analysis command with a read-only Postgres connection and the derived search scope to produce a serialized 'CommandOutcome' or a 'WikiError'. [crates/gwiki/src/commands/benchmark.rs:11-44]
- `run_attached` (function) component `run_attached [function]` (`3c7f7188-f600-57c0-8608-e946c8dd7210`) lines 46-73 [crates/gwiki/src/commands/benchmark.rs:46-73]
  - Signature: `fn run_attached(`
  - Purpose: Resolves benchmark configuration and optional AI/context sources from Gobby home and Postgres, then generates and returns a 'BenchmarkReport' by calling 'benchmark::report_from_postgres' with the provided connection, scopes, and retrieval candidate limit. [crates/gwiki/src/commands/benchmark.rs:46-73]
- `search_scope_for_identity` (function) component `search_scope_for_identity [function]` (`147862a7-e4ad-5a29-bcf5-28ef1c506b95`) lines 75-81 [crates/gwiki/src/commands/benchmark.rs:75-81]
  - Signature: `fn search_scope_for_identity(scope: &ScopeIdentity) -> crate::search::SearchScope {`
  - Purpose: Maps a 'ScopeIdentity' to the corresponding 'crate::search::SearchScope' by matching 'scope.kind' and constructing a global, topic, or project scope with 'scope.id.clone()' where applicable. [crates/gwiki/src/commands/benchmark.rs:75-81]
- `benchmark_text` (function) component `benchmark_text [function]` (`5ffc67db-8128-5a37-8622-d1a397a94dd6`) lines 83-121 [crates/gwiki/src/commands/benchmark.rs:83-121]
  - Signature: `fn benchmark_text(report: &benchmark::BenchmarkReport) -> String {`
  - Purpose: Formats a 'BenchmarkReport' into a newline-separated human-readable summary string covering scope, token compression ratio or unavailability, graph coverage availability, retrieval precision availability, source mix counts, and any degraded sources. [crates/gwiki/src/commands/benchmark.rs:83-121]

