---
title: crates/gwiki/src/commands
type: code_module
provenance:
- file: crates/gwiki/src/commands/ask.rs
- file: crates/gwiki/src/commands/ask/assembly.rs
- file: crates/gwiki/src/commands/ask/citation.rs
- file: crates/gwiki/src/commands/ask/evidence.rs
- file: crates/gwiki/src/commands/ask/narration.rs
- file: crates/gwiki/src/commands/ask/render.rs
- file: crates/gwiki/src/commands/ask/synthesis.rs
- file: crates/gwiki/src/commands/backlinks.rs
- file: crates/gwiki/src/commands/benchmark.rs
- file: crates/gwiki/src/commands/citation_quality.rs
- file: crates/gwiki/src/commands/citation_quality/contradictions.rs
- file: crates/gwiki/src/commands/collect.rs
- file: crates/gwiki/src/commands/compile.rs
- file: crates/gwiki/src/commands/graph.rs
- file: crates/gwiki/src/commands/index.rs
- file: crates/gwiki/src/commands/mod.rs
- file: crates/gwiki/src/commands/read.rs
- file: crates/gwiki/src/commands/refresh/candidate.rs
- file: crates/gwiki/src/commands/refresh/mod.rs
- file: crates/gwiki/src/commands/refresh/model.rs
- file: crates/gwiki/src/commands/refresh/selection.rs
- file: crates/gwiki/src/commands/refresh/tests.rs
- file: crates/gwiki/src/commands/refresh/vault.rs
- file: crates/gwiki/src/commands/review_report.rs
- file: crates/gwiki/src/commands/search.rs
- file: crates/gwiki/src/commands/session_sync.rs
- file: crates/gwiki/src/commands/setup.rs
- file: crates/gwiki/src/commands/sources.rs
- file: crates/gwiki/src/commands/status.rs
- file: crates/gwiki/src/commands/trust.rs
provenance_truncated: 9
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

## Module: crates/gwiki/src/commands

This module is the command-dispatch layer for the `gwiki` CLI tool. Each file implements a single user-facing operation — ranging from content ingestion (`collect`, `compile`, `index`, `init`, `setup`) and source lifecycle management (`sources`, `refresh`) to analytical workflows (`citation_quality`, `review_report`, `audit`, `benchmark`) and navigation utilities (`read`, `search`, `backlinks`, `graph`, `graph_context`). The module root (`mod.rs`) publishes exactly three symbols that the binary wires into its argument parser, keeping the public surface minimal while the per-file `execute` functions carry the implementation weight. Three child modules — `ask`, `citation_quality` (with its own `contradictions` submodule), and `refresh` — encapsulate enough logic to warrant their own directory trees.

| Command file | Primary entry point | Notes |
|---|---|---|
| ask.rs | `execute` | LLM question-answering; validates AI routing |
| audit.rs | `execute` | Single-symbol surface; wiki health audit |
| backlinks.rs | `execute` | 6 symbols; reverse-link traversal |
| benchmark.rs | `execute` | Performance profiling; 4 symbols |
| citation_quality.rs | `execute` / `build_report` | 44 symbols; full citation analysis pipeline |
| collect.rs | `execute` | Source ingestion; 2 symbols |
| compile.rs | `execute` | 23 symbols; Markdown compilation |
| export.rs | `execute` | Single export symbol |
| graph.rs | `execute` | 16 symbols; graph rendering |
| health.rs | `execute` | Single health-check symbol |
| index.rs | `execute` | 35 symbols; PostgreSQL indexing core |
| init.rs | `execute` | Workspace initialisation; 2 symbols |
| librarian.rs | `execute` | Single librarian symbol |
| lint.rs | `execute` | Single lint symbol |
| normalize.rs | `execute` | Normalisation pass |
| read.rs | `execute` | 36 symbols; path- and title-based document lookup |
| review_report.rs | `execute` | 36 symbols; code-change impact report |
| search.rs | `execute` | 20 symbols; full-text search |
| session_sync.rs | `execute` | Session state synchronisation; 3 symbols |
| setup.rs | `execute` | 18 symbols; environment setup |
| sources.rs | `execute` / `execute_remove` | 41 symbols; source manifest management |
| status.rs | `execute` | 5 symbols; workspace status |
| trust.rs | `execute` | 21 symbols; source-trust scoring |
| refresh (child) | `execute` / `execute_with_fetcher` | URL and local-file refresh pipeline |

Key analytical flows are concentrated in `citation_quality.rs` and `review_report.rs`. The citation-quality pipeline reads `SourceManifest` and `ProvenanceGraph` from the vault, scores each source via `crate::credibility` (credibility_quality.rs:10), optionally dispatches AI contradiction detection through `gobby_core::ai::effective_route` (citation_quality.rs:6), then assembles a `CitationQualityReport` with five structured sections before writing a Markdown artifact to disk (citation_quality.rs:25–52). The review-report command mandates a live PostgreSQL connection via `crate::support::env::database_url_for` (review_report.rs:33–38), optionally connects to FalkorDB, loads graph analytics from `gobby_core::graph_analytics`, and joins `ProvenanceGraph` data with a `CodeChangeSet` to surface wiki pages affected by code diffs (review_report.rs:42–57). The `refresh` child module (`execute_with_fetcher` / `execute_resolved_with_fetcher`) handles URL and local-file source refreshing, distinguishing `RefreshPlan`, `ChangedRefresh`, `RefreshedSource`, `SkippedRefresh`, and `RefreshFailure` outcomes and cleaning up stale raw assets on content change.

| Environment variable | Default | Consumer |
|---|---|---|
| `GWIKI_READ_MAX_BYTES` | 1 048 576 (1 MiB) | `read.rs` (read.rs:13–14) |
| `DATABASE_URL` / PostgreSQL DSN | — | `review_report.rs`, `citation_quality.rs`, `index.rs` |

The commands module is a pure caller: it imports from `gobby_core` (AI routing, config, graph analytics, PostgreSQL, degradation), from sibling crates (`crate::credibility`, `crate::provenance`, `crate::sources`, `crate::search`, `crate::code_graph`, `crate::falkor_graph`, `crate::lint`, `crate::markdown`, `crate::frontmatter`, `crate::paths`), and from the shared helpers under `crate::support::scope`, `crate::support::counts`, `crate::support::env`, and `crate::support::search`. Nothing inside `commands` is re-exported beyond the three symbols in `mod.rs`; the binary layer calls in through those entry points, and the commands call outward into the rest of the crate and into `gobby_core`. Degradation signals follow a consistent pattern: soft failures are collected into `degradations` vectors and attached to `CommandOutcome` rather than unwinding, keeping every command tolerant of partial infrastructure (e.g., `DEGRADED_FALKORDB_UNAVAILABLE` in review_report.rs:24–26).
[crates/gwiki/src/commands/citation_quality/contradictions.rs:15-18]
[crates/gwiki/src/commands/ask/citation.rs:25-46]
[crates/gwiki/src/commands/citation_quality.rs:26-33]
[crates/gwiki/src/commands/graph_context.rs:13-83]
[crates/gwiki/src/commands/refresh/mod.rs:29-37]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gwiki/src/commands/ask\|crates/gwiki/src/commands/ask]] | ## Module: crates/gwiki/src/commands/ask |
| [[code/modules/crates/gwiki/src/commands/citation_quality\|crates/gwiki/src/commands/citation_quality]] | ## `crates/gwiki/src/commands/citation_quality/contradictions` |
| [[code/modules/crates/gwiki/src/commands/refresh\|crates/gwiki/src/commands/refresh]] | ## `crates/gwiki/src/commands/refresh` |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/commands/ask.rs\|crates/gwiki/src/commands/ask.rs]] | `crates/gwiki/src/commands/ask.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/audit.rs\|crates/gwiki/src/commands/audit.rs]] | `crates/gwiki/src/commands/audit.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/commands/backlinks.rs\|crates/gwiki/src/commands/backlinks.rs]] | `crates/gwiki/src/commands/backlinks.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/benchmark.rs\|crates/gwiki/src/commands/benchmark.rs]] | `crates/gwiki/src/commands/benchmark.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/citation_quality.rs\|crates/gwiki/src/commands/citation_quality.rs]] | `crates/gwiki/src/commands/citation_quality.rs` exposes 44 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/collect.rs\|crates/gwiki/src/commands/collect.rs]] | `crates/gwiki/src/commands/collect.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/compile.rs\|crates/gwiki/src/commands/compile.rs]] | `crates/gwiki/src/commands/compile.rs` exposes 23 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/export.rs\|crates/gwiki/src/commands/export.rs]] | `crates/gwiki/src/commands/export.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/commands/graph.rs\|crates/gwiki/src/commands/graph.rs]] | `crates/gwiki/src/commands/graph.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/graph_context.rs\|crates/gwiki/src/commands/graph_context.rs]] | `crates/gwiki/src/commands/graph_context.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/health.rs\|crates/gwiki/src/commands/health.rs]] | `crates/gwiki/src/commands/health.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/commands/index.rs\|crates/gwiki/src/commands/index.rs]] | `crates/gwiki/src/commands/index.rs` exposes 35 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/init.rs\|crates/gwiki/src/commands/init.rs]] | `crates/gwiki/src/commands/init.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/librarian.rs\|crates/gwiki/src/commands/librarian.rs]] | `crates/gwiki/src/commands/librarian.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/commands/lint.rs\|crates/gwiki/src/commands/lint.rs]] | `crates/gwiki/src/commands/lint.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/commands/mod.rs\|crates/gwiki/src/commands/mod.rs]] | `crates/gwiki/src/commands/mod.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/normalize.rs\|crates/gwiki/src/commands/normalize.rs]] | `crates/gwiki/src/commands/normalize.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/commands/read.rs\|crates/gwiki/src/commands/read.rs]] | `crates/gwiki/src/commands/read.rs` exposes 36 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/review_report.rs\|crates/gwiki/src/commands/review_report.rs]] | `crates/gwiki/src/commands/review_report.rs` exposes 36 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/search.rs\|crates/gwiki/src/commands/search.rs]] | `crates/gwiki/src/commands/search.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/session_sync.rs\|crates/gwiki/src/commands/session_sync.rs]] | `crates/gwiki/src/commands/session_sync.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/setup.rs\|crates/gwiki/src/commands/setup.rs]] | `crates/gwiki/src/commands/setup.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/sources.rs\|crates/gwiki/src/commands/sources.rs]] | `crates/gwiki/src/commands/sources.rs` exposes 41 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/status.rs\|crates/gwiki/src/commands/status.rs]] | `crates/gwiki/src/commands/status.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/trust.rs\|crates/gwiki/src/commands/trust.rs]] | `crates/gwiki/src/commands/trust.rs` exposes 21 indexed API symbols. |

