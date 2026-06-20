---
title: crates/gwiki/src/commands/benchmark.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/benchmark.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/benchmark.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/benchmark.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/benchmark.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Validates that 'retrieval_candidates' is nonzero, requires a configured PostgreSQL database, and then runs the 'benchmark' analysis command over the selected scope using a read-only PostgreSQL connection to produce a benchmark report. [crates/gwiki/src/commands/benchmark.rs:11-44] |
| `run_attached` | function | Resolves Gobby home and AI/config optional sources from a PostgreSQL-backed config source, then builds and returns a 'benchmark::BenchmarkReport' by calling 'benchmark::report_from_postgres' with the provided connection, scopes, and retrieval candidate count. [crates/gwiki/src/commands/benchmark.rs:46-73] |
| `search_scope_for_identity` | function | Converts a 'ScopeIdentity' into the corresponding 'crate::search::SearchScope' by matching on 'scope.kind' and constructing a global, topic, or project scope using 'scope.id.clone()' for the non-global cases. [crates/gwiki/src/commands/benchmark.rs:75-81] |
| `benchmark_text` | function | Formats a 'BenchmarkReport' into a newline-separated summary string containing the benchmark scope, token-compression ratio or unavailability, graph coverage and retrieval precision availability, source-mix counts, and any degraded sources. [crates/gwiki/src/commands/benchmark.rs:83-121] |

