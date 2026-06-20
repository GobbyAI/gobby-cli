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
- file: crates/gcode/src/commands/codewiki/reuse.rs
- file: crates/gcode/src/commands/codewiki/system_model.rs
- file: crates/gcode/src/commands/codewiki/text.rs
- file: crates/gcode/src/commands/codewiki/text/citations.rs
- file: crates/gcode/src/commands/codewiki/text/frontmatter.rs
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

`crates/gcode/src/commands` is the CLI command layer for indexing, search, inspection, setup, status, graph/vector lifecycle, and CodeWiki generation. Command handlers consistently take resolved configuration context, connect to backing services, apply scope/visibility filters, and render through the shared output layer: `grep` imports `Context`, `ProjectIndexScope`, `db`, `output::Format`, FTS helpers, and visibility controls before its `run` opens a readonly database connection, builds filters, loads indexed chunks, and applies the matcher (`crates/gcode/src/commands/grep.rs:1-100`). `search` follows the same orchestration pattern for hybrid symbol search, importing token budgets, models, FTS, graph boost, RRF, vector symbols, and visibility before expanding paths and merging exact/FTS/vector/graph-style results (`crates/gcode/src/commands/search.rs:1-100`).

The module’s read flows divide between content search, symbol lookup, and status reporting. `symbol_at` parses a user location, normalizes it through `scope`, reads visible symbols from the database, then reads the source file to translate line/column input into byte offsets for containing or nearest-symbol selection (`crates/gcode/src/commands/symbol_at.rs:1-100`). `status` reads indexed-project state and collaborates with config, database, graph, indexer, vector, and visibility modules while formatting timestamps and project health for text or structured output (`crates/gcode/src/commands/status.rs:1-100`). The graph child module provides graph read/query and lifecycle handlers, importing configuration, database access, graph APIs, symbol resolution, token-budget helpers, models, and output formatting; it degrades to hints and empty paged responses when FalkorDB is unavailable, while lifecycle code emits structured sync-contract errors (`reads.rs:1-100`, `lifecycle.rs:1-100`).

The module also hosts supporting subsystems rather than only direct command handlers. The grep child matcher owns regex compilation, fixed-string escaping, case-insensitive mode, word-boundary filtering, and returns `GrepSpan` byte ranges to the parent command for consistent rendering (`crates/gcode/src/commands/grep/grep_matcher.rs:3`, `crates/gcode/src/commands/grep/grep_matcher.rs:6-42`). CodeWiki is the documentation-generation subsystem: it gathers indexed files, symbols, graph edges, graph availability, and leading chunks into `CodewikiInput`, ranks source excerpts by symbol density, and defines prompt contracts that require evidence-only output, citations, cross-file relationship descriptions, and tables for enumerable facts (`crates/gcode/src/commands/codewiki/types.rs:1-100`, `crates/gcode/src/commands/codewiki/prompts.rs:1-100`).

| Area | Public surface / role | Evidence |
| --- | --- | --- |
| `grep` | 44 indexed symbols; content grep over indexed chunks with paths, globs, fixed strings, case, word mode, context, max count, and output format | `crates/gcode/src/commands/grep.rs:1-100` |
| `search` | 39 indexed symbols; hybrid/fuzzy concept search with exact-first, FTS, vector, graph boost, pagination, filters, and token budget | `crates/gcode/src/commands/search.rs:1-100` |
| `symbol_at` | 41 indexed symbols; location parsing and containing/nearest symbol lookup | `crates/gcode/src/commands/symbol_at.rs:1-100` |
| `status` | 38 indexed symbols; indexed-project, graph, index, vector, and visibility status reporting | `crates/gcode/src/commands/status.rs:1-100` |
| `graph` | Graph read/query and lifecycle handling with graceful unavailable-service behavior | `reads.rs:1-100`, `lifecycle.rs:1-100` |
| `codewiki` | Documentation generation from indexed files, symbols, graph relationships, and source excerpts | `crates/gcode/src/commands/codewiki/types.rs:1-100`, `crates/gcode/src/commands/codewiki/prompts.rs:1-100` |
[crates/gcode/src/commands/codewiki/relationship_facts.rs:29-41]
[crates/gcode/src/commands/codewiki/text/citations.rs:26-34]
[crates/gcode/src/commands/codewiki/text/generation.rs:23-79]
[crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:10-133]
[crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:6-13]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/commands/codewiki\|crates/gcode/src/commands/codewiki]] | `crates/gcode/src/commands/codewiki` is the documentation-generation subsystem for CodeWiki. It gathers indexed files, symbols, graph edges, graph availability, and leading source chunks into `CodewikiInput`; those leading chunks are converted into prompt excerpts and ranked by symbol density for module-level context (`crates/gcode/src/commands/codewiki/types.rs:1-100`). Its prompt layer defines the contract for symbol, file, content-file, and module briefs, including the requirement to use supplied evidence only, cite anchors, describe cross-file callers/callees/imports when present, and… |
| [[code/modules/crates/gcode/src/commands/graph\|crates/gcode/src/commands/graph]] | The `crates/gcode/src/commands/graph` module implements graph-oriented command handlers for both lifecycle operations and read/query output. Its read path imports configuration, database access, graph read APIs, full-text symbol resolution, token-budget helpers, shared models, and output formatting, then degrades gracefully when FalkorDB is absent or unreachable by emitting hints and empty paged JSON/text responses where appropriate (`reads.rs:1-100`). Lifecycle handling owns graph sync contract errors, including structured JSON payloads and a dedicated exit code for sync-file contract… |
| [[code/modules/crates/gcode/src/commands/grep\|crates/gcode/src/commands/grep]] | `grep_matcher.rs` implements the internal matcher behind `gcode grep`: it owns a compiled `regex::Regex` plus the `word` matching mode, validates non-empty patterns, optionally escapes fixed-string input, applies case-insensitive compilation, and wraps regex build failures as “invalid gcode grep pattern” errors (`crates/gcode/src/commands/grep/grep_matcher.rs:6-30`). It collaborates with the parent grep command module through `super::GrepSpan`, returning byte spans for matches instead of text so callers can render or process matches consistently… |

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

