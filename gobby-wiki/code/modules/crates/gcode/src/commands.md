---
title: crates/gcode/src/commands
type: code_module
provenance:
- file: crates/gcode/src/commands/codewiki/architecture_diagrams.rs
- file: crates/gcode/src/commands/codewiki/build_parts/audit.rs
- file: crates/gcode/src/commands/codewiki/cluster.rs
- file: crates/gcode/src/commands/codewiki/io.rs
- file: crates/gcode/src/commands/codewiki/ownership/analysis.rs
- file: crates/gcode/src/commands/codewiki/ownership/tests.rs
- file: crates/gcode/src/commands/codewiki/paths.rs
- file: crates/gcode/src/commands/codewiki/prompts.rs
- file: crates/gcode/src/commands/codewiki/relationship_facts.rs
- file: crates/gcode/src/commands/codewiki/system_model.rs
- file: crates/gcode/src/commands/codewiki/text.rs
- file: crates/gcode/src/commands/codewiki/text/citations.rs
- file: crates/gcode/src/commands/codewiki/text/frontmatter.rs
- file: crates/gcode/src/commands/codewiki/text/generation.rs
- file: crates/gcode/src/commands/codewiki/text/sanitize.rs
- file: crates/gcode/src/commands/codewiki/text/verify.rs
- file: crates/gcode/src/commands/codewiki/types.rs
- file: crates/gcode/src/commands/embeddings_doctor.rs
- file: crates/gcode/src/commands/graph/lifecycle.rs
- file: crates/gcode/src/commands/graph/reads.rs
- file: crates/gcode/src/commands/graph/tests.rs
- file: crates/gcode/src/commands/grep.rs
- file: crates/gcode/src/commands/grep/grep_matcher.rs
- file: crates/gcode/src/commands/index.rs
- file: crates/gcode/src/commands/search.rs
- file: crates/gcode/src/commands/setup.rs
- file: crates/gcode/src/commands/status.rs
- file: crates/gcode/src/commands/symbol_at.rs
- file: crates/gcode/src/commands/symbols.rs
- file: crates/gcode/src/commands/vector.rs
provenance_truncated: 43
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

## Module: `crates/gcode/src/commands`

This module is the command-dispatch layer of the `gcode` CLI. Each file implements one top-level user-facing subcommand: `grep`, `search`, `symbol-at`, `status`, `index`, `init`, `setup`, `vector`, `scope`, `symbols`, and `embeddings-doctor`. The public boundary is thin — callers outside this module invoke a `run` (or equivalent) free function that accepts a `Context` carrying `database_url` and `project_root`, then handles formatting and output internally. `mod.rs` wires these files together but exposes no additional symbols of its own; the three child modules (`codewiki`, `graph`, `grep`) house sub-subcommand trees that are rooted here.

The dominant runtime flow is: CLI entry point resolves a `Context`, calls the relevant `run` function, which opens a read-only Postgres connection via `db::connect_readonly` (grep.rs:90, search.rs:30, symbol_at.rs:70, status.rs:63), runs the domain logic, then writes to stdout in the requested `output::Format` (text or JSON). The `grep` command loads `IndexedContentChunk` rows from the database up to a 100 000-row safety limit (grep.rs:18), compiles the caller's pattern via an internal `GrepMatcher` with optional fixed-string, case-insensitive, and word-boundary modes, then applies `GrepFilters` (path and glob predicates) before collecting `GrepMatch` results with before/after context lines. The `search` command fans out across three ranked sources — BM25 full-text search (`fts::search_symbols_fts_visible`), vector nearest-neighbour (`code_symbols`), and graph-boosted results (`graph_boost`) — then merges them with Reciprocal Rank Fusion via `rrf` (search.rs:8–9). `symbol-at` parses a `file:line[:column]` location string, fetches all visible symbols for the file from `visibility::visible_symbols_for_file`, and selects the best match using a containment-first, nearest-fallback comparison that disambiguates ties by byte distance (symbol_at.rs:1–100).

The `scope` submodule provides shared path-normalisation helpers (`normalize_file_arg`, `path_filter_for`, `clean_relative_path`) called by `grep`, `symbol-at`, `search`, and `init` to canonicalise user-supplied file arguments against the project root. The `setup` command drives first-time database provisioning and embedding-provider configuration (`resolve_or_provision_database`, `write_gcore_config`, `resolve_embedding_bootstrap`), while `vector` owns the embedding lifecycle (`sync_file`, `rebuild`, `cleanup_orphans`). `status` queries an `IndexedProject` row and formats timestamps with a self-contained epoch-to-date algorithm (status.rs:18–56). `embeddings-doctor` probes the embedding daemon's declared dimension against actual stored vectors and reports drift fields, optionally fetching a peer report from the daemon (embeddings_doctor.rs).

The module imports heavily from sibling crates and internal library modules; it does not export domain types upward — it is a leaf in the dependency direction.

### Public `run` / entry-point functions

| File | Entry function | Key parameters |
|---|---|---|
| `grep.rs` | `run(ctx, GrepOptions)` | pattern, paths, globs, fixed_strings, ignore_case, word, context, max_count, format |
| `search.rs` | `search(ctx, query, SearchOptions)` | limit, offset, kind, language, paths, format, with_graph, token_budget |
| `symbol_at.rs` | `run(ctx, location, line, format)` | `file[:line[:col]]` location string |
| `status.rs` | `run(ctx, format)` | — |
| `index.rs` | `run(…)` | path filter, clone context |
| `vector.rs` | `run(…)` | sync / rebuild / cleanup sub-action |
| `setup.rs` | `run(…)` | DB URL, embedding provider options |
| `embeddings_doctor.rs` | `run(…)` | — |
| `init.rs` | `run(…)` | — |
| `symbols.rs` | `run(…)` / `outline` / `summarize_outline` | format, kind filter, AI depth |

### Key types

| Type | File | Role |
|---|---|---|
| `GrepOptions` | `grep.rs` | Carries all grep flags per invocation |
| `GrepMatch` / `GrepSpan` / `GrepContextLine` | `grep.rs` | Serialisable match result with before/after context |
| `GrepFilters` / `CompiledGlob` | `grep.rs` | Path & glob predicate compilation |
| `SearchOptions` | `search.rs` | Search parameters including RRF source toggles |
| `ParsedLocation` / `SymbolAtTarget` / `SelectedSymbol` | `symbol_at.rs` | Location parsing and symbol-selection state |
| `MatchKind` (`Containing` / `Nearest`) | `symbol_at.rs` | Reports how the winning symbol was chosen |
| `EmbeddingsDoctorReport` / `EmbeddingsDoctorDrift` | `embeddings_doctor.rs` | Drift and peer diagnostics |
| `IndexSyncProjectionsOutput` | `index.rs` | JSON contract for index sync results |
| `VectorLifecycleJsonPayload` | `vector.rs` | JSON output for vector lifecycle commands |

### Cross-module collaboration

| This module calls into | Purpose |
|---|---|
| `crate::db` (`connect_readonly`) | Open Postgres connections |
| `crate::visibility` | Filter symbols by project visibility rules |
| `crate::search::{fts, graph_boost, rrf}` | BM25, graph-boosted, and RRF ranking for `search` |
| `crate::vector::code_symbols` | Vector nearest-neighbour for `search` and `status` |
| `crate::graph::code_graph` | Call/import graph data for `status` and child `graph` module |
| `crate::index::indexer` | Underlying indexing pipeline used by `index` and `status` |
| `crate::output` (`Format`) | Text vs. JSON serialisation |
| `crate::models` (`Symbol`, `IndexedProject`, …) | Database row types |
| `crate::config::Context` | Project root, database URL, AI options |
[crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:6-13]
[crates/gcode/src/commands/codewiki/build_parts/file.rs:14-17]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-24]
[crates/gcode/src/commands/codewiki/graph.rs:5-110]
[crates/gcode/src/commands/codewiki/mod.rs:1-100]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/commands/codewiki\|crates/gcode/src/commands/codewiki]] | ## Module: `crates/gcode/src/commands/codewiki` |
| [[code/modules/crates/gcode/src/commands/graph\|crates/gcode/src/commands/graph]] | ## crates/gcode/src/commands/graph |
| [[code/modules/crates/gcode/src/commands/grep\|crates/gcode/src/commands/grep]] | ## crates/gcode/src/commands/grep |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/embeddings_doctor.rs\|crates/gcode/src/commands/embeddings_doctor.rs]] | `crates/gcode/src/commands/embeddings_doctor.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/graph.rs\|crates/gcode/src/commands/graph.rs]] | `crates/gcode/src/commands/graph.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/commands/grep.rs\|crates/gcode/src/commands/grep.rs]] | `crates/gcode/src/commands/grep.rs` exposes 44 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/index.rs\|crates/gcode/src/commands/index.rs]] | `crates/gcode/src/commands/index.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/init.rs\|crates/gcode/src/commands/init.rs]] | `crates/gcode/src/commands/init.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gcode/src/commands/mod.rs\|crates/gcode/src/commands/mod.rs]] | `crates/gcode/src/commands/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/commands/scope.rs\|crates/gcode/src/commands/scope.rs]] | `crates/gcode/src/commands/scope.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/search.rs\|crates/gcode/src/commands/search.rs]] | `crates/gcode/src/commands/search.rs` exposes 39 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/setup.rs\|crates/gcode/src/commands/setup.rs]] | `crates/gcode/src/commands/setup.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/status.rs\|crates/gcode/src/commands/status.rs]] | `crates/gcode/src/commands/status.rs` exposes 38 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/symbol_at.rs\|crates/gcode/src/commands/symbol_at.rs]] | `crates/gcode/src/commands/symbol_at.rs` exposes 41 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/symbols.rs\|crates/gcode/src/commands/symbols.rs]] | `crates/gcode/src/commands/symbols.rs` exposes 24 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/vector.rs\|crates/gcode/src/commands/vector.rs]] | `crates/gcode/src/commands/vector.rs` exposes 17 indexed API symbols. |

