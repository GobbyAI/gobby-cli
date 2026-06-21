---
title: crates/gwiki/src
type: code_module
provenance:
- file: crates/gwiki/src/ai/chunk.rs
- file: crates/gwiki/src/api.rs
- file: crates/gwiki/src/benchmark.rs
- file: crates/gwiki/src/collect.rs
- file: crates/gwiki/src/commands/citation_quality.rs
- file: crates/gwiki/src/commands/index.rs
- file: crates/gwiki/src/commands/read.rs
- file: crates/gwiki/src/commands/review_report.rs
- file: crates/gwiki/src/commands/sources.rs
- file: crates/gwiki/src/frontmatter.rs
- file: crates/gwiki/src/graph/context.rs
- file: crates/gwiki/src/graph/mod.rs
- file: crates/gwiki/src/health.rs
- file: crates/gwiki/src/indexer.rs
- file: crates/gwiki/src/ingest/audio.rs
- file: crates/gwiki/src/ingest/mod.rs
- file: crates/gwiki/src/ingest/session.rs
- file: crates/gwiki/src/ingest/wayback.rs
- file: crates/gwiki/src/librarian.rs
- file: crates/gwiki/src/links.rs
- file: crates/gwiki/src/lint.rs
- file: crates/gwiki/src/main.rs
- file: crates/gwiki/src/markdown.rs
- file: crates/gwiki/src/output.rs
- file: crates/gwiki/src/search/graph_boost.rs
- file: crates/gwiki/src/search/mod.rs
- file: crates/gwiki/src/search/semantic.rs
- file: crates/gwiki/src/session.rs
- file: crates/gwiki/src/vector.rs
- file: crates/gwiki/src/vision.rs
provenance_truncated: 158
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src

Parent: [[code/modules/crates/gwiki|crates/gwiki]]

## Overview

## Module: `crates/gwiki/src`

`gwiki` is the top-level crate for a knowledge-management system that ingests heterogeneous content, indexes it in PostgreSQL and vector stores, models it as a graph, and surfaces it through a unified CLI and API. The binary entry point is `main.rs`, which parses a `Cli`/`CliCommand` struct and dispatches to one of roughly twenty sub-commands housed under `commands/`. All commands share a common `ScopeSelection` and `ScopeIdentity` abstraction that routes operations to a global, project-scoped, or topic-scoped view of the vault. The error type is the crate-wide `WikiError`, and structured command results flow through `CommandOutcome`/`CommandResult` before being serialised as JSON or rendered as plain text by `output.rs`.

The ingest subsystem (`ingest/`) accepts audio, video, images, PDFs, Office documents, HTML URLs, Wayback captures, git repositories, MediaWiki pages, local files, stdin, and AI session transcripts (Claude Code, Codex, Gemini, Grok, Droid, Qwen). Each sub-pipeline writes an immutable raw asset under `raw/` via `write_immutable`/`write_asset` helpers in `ingest/mod.rs`, registers the source in a `SourceManifest`, then calls `index_after_ingest` to upsert rows into a `WikiIndexStore`. The store is backed by either a `MemoryWikiStore` (for tests) or a `PostgresWikiStore`; vector embeddings are synced separately to Qdrant via `vector.rs`. Graph facts are maintained in FalkorDB through `falkor_graph/` and mirrored in a `MemoryWikiGraph` for offline analytics.

Search is a multi-source fusion pipeline assembled in `search/`. BM25 keyword queries are issued against PostgreSQL (`search/bm25.rs`), semantic queries are embedded and dispatched to Qdrant (`search/semantic`), and a graph-boost signal derived from link-neighbourhood scoring is layered on top (`search/graph_boost.rs`). The `ask` command extends search with an LLM synthesis stage: evidence is planned and token-budgeted in `commands/ask/evidence.rs`, a synthesis prompt is submitted via `commands/ask/synthesis.rs`, leading narration is stripped in `commands/ask/narration.rs`, and citation grounding is validated in `commands/ask/assembly.rs`. The `compile` command runs a similar flow—`compile_to_wiki` in `compile/mod.rs` assembles source chunks, invokes an optional `ExplainerGenerator`, grounds citations, and writes a target wiki page; `compile/index.rs` keeps the top-level wiki index in sync.

Several cross-cutting subsystems provide quality and observability. `health.rs` detects stale pages and citations, uncited sources, and broken links. `audit/` analyses claim-level source support for codewiki pages, classifying lines as structural or prose claims and checking each for inline source spans. `benchmark.rs` measures token compression, graph coverage, and retrieval precision against a PostgreSQL backend. `librarian.rs` proposes patch diffs for pages with weak provenance or outdated codewiki content. `lint.rs` enforces wikilink hygiene and backlink reciprocity. All of these subsystems receive their configuration from `support/config.rs` and `support/env.rs`, which resolve values from a layered configuration source that includes a local `gcore.yaml` and environment variables.

### CLI commands

| Subcommand | Primary handler |
|---|---|
| `setup` | `commands/setup.rs` |
| `index` | `commands/index.rs` |
| `search` | `commands/search.rs` |
| `ask` | `commands/ask/` |
| `read` | `commands/read.rs` |
| `compile` | `commands/compile.rs` |
| `sources` / `remove-source` | `commands/sources.rs` |
| `refresh` | `commands/sources.rs` |
| `backlinks` / `link-suggest` | `commands/backlinks.rs` |
| `graph` | `commands/graph.rs` |
| `health` | `commands/health.rs` |
| `lint` | `commands/lint.rs` |
| `normalize` | `commands/normalize.rs` |
| `collect` | `commands/collect.rs` |
| `benchmark` | `commands/benchmark.rs` |
| `review-report` | `commands/review_report.rs` |
| `export` | `commands/export.rs` |
| `sync-sessions` | `commands/session_sync.rs` |
| `status` | `commands/status.rs` |
| `trust` | `commands/trust.rs` |
| `init` | `commands/init.rs` |

### Key public types and traits

| Symbol | File | Role |
|---|---|---|
| `WikiError` | `error.rs` | Crate-wide error type with typed variants |
| `ScopeSelection` / `ScopeIdentity` | `api.rs` | Scope resolution for global / project / topic |
| `WikiIndexStore` | `store/mod.rs` | Storage trait over memory and Postgres backends |
| `SourceManifest` / `SourceRecord` | `sources/manifest.rs` | Source registry and per-entry metadata |
| `WikiGraphFacts` | `graph/mod.rs` | In-memory document/link/source/code-edge graph |
| `IngestResult` | `ingest/mod.rs` | Return value from all ingestion paths |
| `BenchmarkReport` | `benchmark.rs` | Serialisable quality metrics |
| `HealthReport` | `health.rs` | Stale citations, broken links, duplicate concepts |
| `AuditReport` / `AuditOptions` | `audit/mod.rs` | Claim-level source audit result |
| `TranscriptionClient` | `transcribe.rs` | Trait for audio transcription and translation |
| `VisionClient` | `vision.rs` | Trait for image/frame description |

### Selected environment variables

| Variable | Consumer | Purpose |
|---|---|---|
| `GWIKI_STALE_CITATION_YEARS` | `health.rs` | Threshold for stale citation warnings |
| `GOBBY_HOME` | `support/env.rs` | Root directory for hub config and vault discovery |
| `GWIKI_MAX_INBOX_ITEM_BYTES` | `support/env.rs` | Size cap for collect inbox items |
| `GWIKI_SHARED_CODE_GRAPH_*` | `support/config.rs` | Limits on code-edge queries |

### Storage and service dependencies

| Service | Integration point |
|---|---|
| PostgreSQL | `store/postgres.rs`, `search/bm25.rs`, `benchmark.rs` |
| Qdrant | `vector.rs`, `search/semantic` |
| FalkorDB | `falkor_graph/` |
| ffmpeg | `media.rs`, `ingest/audio.rs`, `ingest/video/` |
| pdfium | `ingest/pdf/render.rs` |
| gobby daemon (AI) | `daemon.rs`, `support/env.rs` |
[crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98]
[crates/gwiki/src/commands/ask/assembly.rs:6-39]
[crates/gwiki/src/commands/ask/citation.rs:25-46]
[crates/gwiki/src/commands/ask/evidence.rs:14-16]
[crates/gwiki/src/commands/ask/narration.rs:7-58]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gwiki/src/ai\|crates/gwiki/src/ai]] | ## Module: crates/gwiki/src/ai |
| [[code/modules/crates/gwiki/src/audit\|crates/gwiki/src/audit]] | ## Module: `crates/gwiki/src/audit` |
| [[code/modules/crates/gwiki/src/commands\|crates/gwiki/src/commands]] | ## Module: crates/gwiki/src/commands |
| [[code/modules/crates/gwiki/src/compile\|crates/gwiki/src/compile]] | ## Module: `crates/gwiki/src/compile` |
| [[code/modules/crates/gwiki/src/falkor_graph\|crates/gwiki/src/falkor_graph]] | ## crates/gwiki/src/falkor_graph |
| [[code/modules/crates/gwiki/src/graph\|crates/gwiki/src/graph]] | ## crates/gwiki/src/graph |
| [[code/modules/crates/gwiki/src/ingest\|crates/gwiki/src/ingest]] | ## `crates/gwiki/src/ingest` |
| [[code/modules/crates/gwiki/src/search\|crates/gwiki/src/search]] | ## crates/gwiki/src/search |
| [[code/modules/crates/gwiki/src/sources\|crates/gwiki/src/sources]] | ## crates/gwiki/src/sources |
| [[code/modules/crates/gwiki/src/store\|crates/gwiki/src/store]] | ## crates/gwiki/src/store |
| [[code/modules/crates/gwiki/src/support\|crates/gwiki/src/support]] | ## crates/gwiki/src/support |
| [[code/modules/crates/gwiki/src/synthesis\|crates/gwiki/src/synthesis]] | ## crates/gwiki/src/synthesis |
| [[code/modules/crates/gwiki/src/video\|crates/gwiki/src/video]] | ## crates/gwiki/src/video |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ai/chunk.rs\|crates/gwiki/src/ai/chunk.rs]] | `crates/gwiki/src/ai/chunk.rs` exposes 42 indexed API symbols. |
| [[code/files/crates/gwiki/src/ai/translate.rs\|crates/gwiki/src/ai/translate.rs]] | `crates/gwiki/src/ai/translate.rs` exposes 22 indexed API symbols. |
| [[code/files/crates/gwiki/src/api.rs\|crates/gwiki/src/api.rs]] | `crates/gwiki/src/api.rs` exposes 31 indexed API symbols. |
| [[code/files/crates/gwiki/src/audit.rs\|crates/gwiki/src/audit.rs]] | `crates/gwiki/src/audit.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gwiki/src/audit/claims.rs\|crates/gwiki/src/audit/claims.rs]] | `crates/gwiki/src/audit/claims.rs` exposes 23 indexed API symbols. |
| [[code/files/crates/gwiki/src/audit/tests.rs\|crates/gwiki/src/audit/tests.rs]] | `crates/gwiki/src/audit/tests.rs` exposes 14 indexed API symbols. |
| [[code/files/crates/gwiki/src/benchmark.rs\|crates/gwiki/src/benchmark.rs]] | `crates/gwiki/src/benchmark.rs` exposes 52 indexed API symbols. |
| [[code/files/crates/gwiki/src/citations.rs\|crates/gwiki/src/citations.rs]] | `crates/gwiki/src/citations.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/code_graph.rs\|crates/gwiki/src/code_graph.rs]] | `crates/gwiki/src/code_graph.rs` exposes 30 indexed API symbols. |
| [[code/files/crates/gwiki/src/collect.rs\|crates/gwiki/src/collect.rs]] | `crates/gwiki/src/collect.rs` exposes 43 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/ask/assembly.rs\|crates/gwiki/src/commands/ask/assembly.rs]] | `crates/gwiki/src/commands/ask/assembly.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/ask/evidence.rs\|crates/gwiki/src/commands/ask/evidence.rs]] | `crates/gwiki/src/commands/ask/evidence.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/ask/narration.rs\|crates/gwiki/src/commands/ask/narration.rs]] | `crates/gwiki/src/commands/ask/narration.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/ask/render.rs\|crates/gwiki/src/commands/ask/render.rs]] | `crates/gwiki/src/commands/ask/render.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/ask/synthesis.rs\|crates/gwiki/src/commands/ask/synthesis.rs]] | `crates/gwiki/src/commands/ask/synthesis.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/backlinks.rs\|crates/gwiki/src/commands/backlinks.rs]] | `crates/gwiki/src/commands/backlinks.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/benchmark.rs\|crates/gwiki/src/commands/benchmark.rs]] | `crates/gwiki/src/commands/benchmark.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/citation_quality/contradictions.rs\|crates/gwiki/src/commands/citation_quality/contradictions.rs]] | `crates/gwiki/src/commands/citation_quality/contradictions.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/collect.rs\|crates/gwiki/src/commands/collect.rs]] | `crates/gwiki/src/commands/collect.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/compile.rs\|crates/gwiki/src/commands/compile.rs]] | `crates/gwiki/src/commands/compile.rs` exposes 23 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/export.rs\|crates/gwiki/src/commands/export.rs]] | `crates/gwiki/src/commands/export.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/commands/graph.rs\|crates/gwiki/src/commands/graph.rs]] | `crates/gwiki/src/commands/graph.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/graph_context.rs\|crates/gwiki/src/commands/graph_context.rs]] | `crates/gwiki/src/commands/graph_context.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/health.rs\|crates/gwiki/src/commands/health.rs]] | `crates/gwiki/src/commands/health.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/commands/index.rs\|crates/gwiki/src/commands/index.rs]] | `crates/gwiki/src/commands/index.rs` exposes 35 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/init.rs\|crates/gwiki/src/commands/init.rs]] | `crates/gwiki/src/commands/init.rs` exposes 2 indexed API symbols. |
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
| [[code/files/crates/gwiki/src/compile/index.rs\|crates/gwiki/src/compile/index.rs]] | `crates/gwiki/src/compile/index.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gwiki/src/compile/mod.rs\|crates/gwiki/src/compile/mod.rs]] | `crates/gwiki/src/compile/mod.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gwiki/src/compile/render.rs\|crates/gwiki/src/compile/render.rs]] | `crates/gwiki/src/compile/render.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/contract.rs\|crates/gwiki/src/contract.rs]] | `crates/gwiki/src/contract.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/credibility.rs\|crates/gwiki/src/credibility.rs]] | `crates/gwiki/src/credibility.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/daemon.rs\|crates/gwiki/src/daemon.rs]] | `crates/gwiki/src/daemon.rs` exposes 29 indexed API symbols. |
| [[code/files/crates/gwiki/src/document.rs\|crates/gwiki/src/document.rs]] | `crates/gwiki/src/document.rs` exposes 15 indexed API symbols. |
| [[code/files/crates/gwiki/src/error.rs\|crates/gwiki/src/error.rs]] | `crates/gwiki/src/error.rs` exposes 14 indexed API symbols. |
| [[code/files/crates/gwiki/src/explainer.rs\|crates/gwiki/src/explainer.rs]] | `crates/gwiki/src/explainer.rs` exposes 28 indexed API symbols. |
| [[code/files/crates/gwiki/src/exports.rs\|crates/gwiki/src/exports.rs]] | `crates/gwiki/src/exports.rs` exposes 22 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph.rs\|crates/gwiki/src/falkor_graph.rs]] | `crates/gwiki/src/falkor_graph.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/boost.rs\|crates/gwiki/src/falkor_graph/boost.rs]] | `crates/gwiki/src/falkor_graph/boost.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/code_edges.rs\|crates/gwiki/src/falkor_graph/code_edges.rs]] | `crates/gwiki/src/falkor_graph/code_edges.rs` exposes 15 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/query.rs\|crates/gwiki/src/falkor_graph/query.rs]] | `crates/gwiki/src/falkor_graph/query.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/sync.rs\|crates/gwiki/src/falkor_graph/sync.rs]] | `crates/gwiki/src/falkor_graph/sync.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/tests.rs\|crates/gwiki/src/falkor_graph/tests.rs]] | `crates/gwiki/src/falkor_graph/tests.rs` exposes 14 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/wiki_facts.rs\|crates/gwiki/src/falkor_graph/wiki_facts.rs]] | `crates/gwiki/src/falkor_graph/wiki_facts.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/frontmatter.rs\|crates/gwiki/src/frontmatter.rs]] | `crates/gwiki/src/frontmatter.rs` exposes 31 indexed API symbols. |
| [[code/files/crates/gwiki/src/graph/analytics.rs\|crates/gwiki/src/graph/analytics.rs]] | `crates/gwiki/src/graph/analytics.rs` exposes 21 indexed API symbols. |
| [[code/files/crates/gwiki/src/graph/context.rs\|crates/gwiki/src/graph/context.rs]] | `crates/gwiki/src/graph/context.rs` exposes 35 indexed API symbols. |
| [[code/files/crates/gwiki/src/graph/export.rs\|crates/gwiki/src/graph/export.rs]] | `crates/gwiki/src/graph/export.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/graph/mod.rs\|crates/gwiki/src/graph/mod.rs]] | `crates/gwiki/src/graph/mod.rs` exposes 59 indexed API symbols. |
| [[code/files/crates/gwiki/src/health.rs\|crates/gwiki/src/health.rs]] | `crates/gwiki/src/health.rs` exposes 55 indexed API symbols. |
| [[code/files/crates/gwiki/src/indexer.rs\|crates/gwiki/src/indexer.rs]] | `crates/gwiki/src/indexer.rs` exposes 33 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/audio.rs\|crates/gwiki/src/ingest/audio.rs]] | `crates/gwiki/src/ingest/audio.rs` exposes 46 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/document/html.rs\|crates/gwiki/src/ingest/document/html.rs]] | `crates/gwiki/src/ingest/document/html.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/document/mod.rs\|crates/gwiki/src/ingest/document/mod.rs]] | `crates/gwiki/src/ingest/document/mod.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/document/office.rs\|crates/gwiki/src/ingest/document/office.rs]] | `crates/gwiki/src/ingest/document/office.rs` exposes 26 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/document/render.rs\|crates/gwiki/src/ingest/document/render.rs]] | `crates/gwiki/src/ingest/document/render.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/file.rs\|crates/gwiki/src/ingest/file.rs]] | `crates/gwiki/src/ingest/file.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/file/degradation.rs\|crates/gwiki/src/ingest/file/degradation.rs]] | `crates/gwiki/src/ingest/file/degradation.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/file/dispatch.rs\|crates/gwiki/src/ingest/file/dispatch.rs]] | `crates/gwiki/src/ingest/file/dispatch.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/ingest/file/generic.rs\|crates/gwiki/src/ingest/file/generic.rs]] | `crates/gwiki/src/ingest/file/generic.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/ingest/file/render.rs\|crates/gwiki/src/ingest/file/render.rs]] | `crates/gwiki/src/ingest/file/render.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/ingest/file/replay.rs\|crates/gwiki/src/ingest/file/replay.rs]] | `crates/gwiki/src/ingest/file/replay.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/ingest/file/source.rs\|crates/gwiki/src/ingest/file/source.rs]] | `crates/gwiki/src/ingest/file/source.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/file/tests.rs\|crates/gwiki/src/ingest/file/tests.rs]] | `crates/gwiki/src/ingest/file/tests.rs` exposes 21 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/git.rs\|crates/gwiki/src/ingest/git.rs]] | `crates/gwiki/src/ingest/git.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/image.rs\|crates/gwiki/src/ingest/image.rs]] | `crates/gwiki/src/ingest/image.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/mediawiki.rs\|crates/gwiki/src/ingest/mediawiki.rs]] | `crates/gwiki/src/ingest/mediawiki.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/mod.rs\|crates/gwiki/src/ingest/mod.rs]] | `crates/gwiki/src/ingest/mod.rs` exposes 61 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/pdf/ingest.rs\|crates/gwiki/src/ingest/pdf/ingest.rs]] | `crates/gwiki/src/ingest/pdf/ingest.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/pdf/markdown.rs\|crates/gwiki/src/ingest/pdf/markdown.rs]] | `crates/gwiki/src/ingest/pdf/markdown.rs` exposes 14 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/pdf/render.rs\|crates/gwiki/src/ingest/pdf/render.rs]] | `crates/gwiki/src/ingest/pdf/render.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/pdf/tests.rs\|crates/gwiki/src/ingest/pdf/tests.rs]] | `crates/gwiki/src/ingest/pdf/tests.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/pdf/text.rs\|crates/gwiki/src/ingest/pdf/text.rs]] | `crates/gwiki/src/ingest/pdf/text.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/pdf/types.rs\|crates/gwiki/src/ingest/pdf/types.rs]] | `crates/gwiki/src/ingest/pdf/types.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session.rs\|crates/gwiki/src/ingest/session.rs]] | `crates/gwiki/src/ingest/session.rs` exposes 45 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session/codex.rs\|crates/gwiki/src/ingest/session/codex.rs]] | `crates/gwiki/src/ingest/session/codex.rs` exposes 23 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session/derived.rs\|crates/gwiki/src/ingest/session/derived.rs]] | `crates/gwiki/src/ingest/session/derived.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session/droid.rs\|crates/gwiki/src/ingest/session/droid.rs]] | `crates/gwiki/src/ingest/session/droid.rs` exposes 23 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session/gemini.rs\|crates/gwiki/src/ingest/session/gemini.rs]] | `crates/gwiki/src/ingest/session/gemini.rs` exposes 15 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session/grok.rs\|crates/gwiki/src/ingest/session/grok.rs]] | `crates/gwiki/src/ingest/session/grok.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session/metadata.rs\|crates/gwiki/src/ingest/session/metadata.rs]] | `crates/gwiki/src/ingest/session/metadata.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session/qwen.rs\|crates/gwiki/src/ingest/session/qwen.rs]] | `crates/gwiki/src/ingest/session/qwen.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session/redaction.rs\|crates/gwiki/src/ingest/session/redaction.rs]] | `crates/gwiki/src/ingest/session/redaction.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session_archive.rs\|crates/gwiki/src/ingest/session_archive.rs]] | `crates/gwiki/src/ingest/session_archive.rs` exposes 19 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/url.rs\|crates/gwiki/src/ingest/url.rs]] | `crates/gwiki/src/ingest/url.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/url/fetch.rs\|crates/gwiki/src/ingest/url/fetch.rs]] | `crates/gwiki/src/ingest/url/fetch.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/url/render.rs\|crates/gwiki/src/ingest/url/render.rs]] | `crates/gwiki/src/ingest/url/render.rs` exposes 15 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/url/tests.rs\|crates/gwiki/src/ingest/url/tests.rs]] | `crates/gwiki/src/ingest/url/tests.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/video/mod.rs\|crates/gwiki/src/ingest/video/mod.rs]] | `crates/gwiki/src/ingest/video/mod.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/video/processing.rs\|crates/gwiki/src/ingest/video/processing.rs]] | `crates/gwiki/src/ingest/video/processing.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/wayback.rs\|crates/gwiki/src/ingest/wayback.rs]] | `crates/gwiki/src/ingest/wayback.rs` exposes 31 indexed API symbols. |
| [[code/files/crates/gwiki/src/lib.rs\|crates/gwiki/src/lib.rs]] | `crates/gwiki/src/lib.rs` has no indexed API symbols. |
| [[code/files/crates/gwiki/src/librarian.rs\|crates/gwiki/src/librarian.rs]] | `crates/gwiki/src/librarian.rs` exposes 35 indexed API symbols. |
| [[code/files/crates/gwiki/src/links.rs\|crates/gwiki/src/links.rs]] | `crates/gwiki/src/links.rs` exposes 39 indexed API symbols. |
| [[code/files/crates/gwiki/src/lint.rs\|crates/gwiki/src/lint.rs]] | `crates/gwiki/src/lint.rs` exposes 36 indexed API symbols. |
| [[code/files/crates/gwiki/src/log.rs\|crates/gwiki/src/log.rs]] | `crates/gwiki/src/log.rs` exposes 14 indexed API symbols. |
| [[code/files/crates/gwiki/src/main.rs\|crates/gwiki/src/main.rs]] | `crates/gwiki/src/main.rs` exposes 39 indexed API symbols. |
| [[code/files/crates/gwiki/src/markdown.rs\|crates/gwiki/src/markdown.rs]] | `crates/gwiki/src/markdown.rs` exposes 33 indexed API symbols. |
| [[code/files/crates/gwiki/src/media.rs\|crates/gwiki/src/media.rs]] | `crates/gwiki/src/media.rs` exposes 29 indexed API symbols. |
| [[code/files/crates/gwiki/src/models.rs\|crates/gwiki/src/models.rs]] | `crates/gwiki/src/models.rs` exposes 21 indexed API symbols. |
| [[code/files/crates/gwiki/src/normalize.rs\|crates/gwiki/src/normalize.rs]] | `crates/gwiki/src/normalize.rs` exposes 14 indexed API symbols. |
| [[code/files/crates/gwiki/src/obsidian.rs\|crates/gwiki/src/obsidian.rs]] | `crates/gwiki/src/obsidian.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/output.rs\|crates/gwiki/src/output.rs]] | `crates/gwiki/src/output.rs` exposes 32 indexed API symbols. |
| [[code/files/crates/gwiki/src/paths.rs\|crates/gwiki/src/paths.rs]] | `crates/gwiki/src/paths.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/provenance.rs\|crates/gwiki/src/provenance.rs]] | `crates/gwiki/src/provenance.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gwiki/src/registry.rs\|crates/gwiki/src/registry.rs]] | `crates/gwiki/src/registry.rs` exposes 14 indexed API symbols. |
| [[code/files/crates/gwiki/src/runner.rs\|crates/gwiki/src/runner.rs]] | `crates/gwiki/src/runner.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/schema.rs\|crates/gwiki/src/schema.rs]] | `crates/gwiki/src/schema.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/scope.rs\|crates/gwiki/src/scope.rs]] | `crates/gwiki/src/scope.rs` exposes 26 indexed API symbols. |
| [[code/files/crates/gwiki/src/search/bm25.rs\|crates/gwiki/src/search/bm25.rs]] | `crates/gwiki/src/search/bm25.rs` exposes 31 indexed API symbols. |
| [[code/files/crates/gwiki/src/search/graph_boost.rs\|crates/gwiki/src/search/graph_boost.rs]] | `crates/gwiki/src/search/graph_boost.rs` exposes 35 indexed API symbols. |
| [[code/files/crates/gwiki/src/session.rs\|crates/gwiki/src/session.rs]] | `crates/gwiki/src/session.rs` exposes 39 indexed API symbols. |
| [[code/files/crates/gwiki/src/setup.rs\|crates/gwiki/src/setup.rs]] | `crates/gwiki/src/setup.rs` exposes 25 indexed API symbols. |
| [[code/files/crates/gwiki/src/sources/atomic.rs\|crates/gwiki/src/sources/atomic.rs]] | `crates/gwiki/src/sources/atomic.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gwiki/src/sources/manifest.rs\|crates/gwiki/src/sources/manifest.rs]] | `crates/gwiki/src/sources/manifest.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gwiki/src/sources/render.rs\|crates/gwiki/src/sources/render.rs]] | `crates/gwiki/src/sources/render.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/gwiki/src/sources/tests.rs\|crates/gwiki/src/sources/tests.rs]] | `crates/gwiki/src/sources/tests.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gwiki/src/store.rs\|crates/gwiki/src/store.rs]] | `crates/gwiki/src/store.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/store/helpers.rs\|crates/gwiki/src/store/helpers.rs]] | `crates/gwiki/src/store/helpers.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/gwiki/src/store/memory.rs\|crates/gwiki/src/store/memory.rs]] | `crates/gwiki/src/store/memory.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/store/postgres.rs\|crates/gwiki/src/store/postgres.rs]] | `crates/gwiki/src/store/postgres.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/config.rs\|crates/gwiki/src/support/config.rs]] | `crates/gwiki/src/support/config.rs` exposes 30 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/counts.rs\|crates/gwiki/src/support/counts.rs]] | `crates/gwiki/src/support/counts.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/env.rs\|crates/gwiki/src/support/env.rs]] | `crates/gwiki/src/support/env.rs` exposes 22 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/graph.rs\|crates/gwiki/src/support/graph.rs]] | `crates/gwiki/src/support/graph.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/postgres.rs\|crates/gwiki/src/support/postgres.rs]] | `crates/gwiki/src/support/postgres.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/scope.rs\|crates/gwiki/src/support/scope.rs]] | `crates/gwiki/src/support/scope.rs` exposes 10 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/search.rs\|crates/gwiki/src/support/search.rs]] | `crates/gwiki/src/support/search.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/text.rs\|crates/gwiki/src/support/text.rs]] | `crates/gwiki/src/support/text.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/time.rs\|crates/gwiki/src/support/time.rs]] | `crates/gwiki/src/support/time.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis.rs\|crates/gwiki/src/synthesis.rs]] | `crates/gwiki/src/synthesis.rs` has no indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis/generate.rs\|crates/gwiki/src/synthesis/generate.rs]] | `crates/gwiki/src/synthesis/generate.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis/paths.rs\|crates/gwiki/src/synthesis/paths.rs]] | `crates/gwiki/src/synthesis/paths.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis/render.rs\|crates/gwiki/src/synthesis/render.rs]] | `crates/gwiki/src/synthesis/render.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis/tests.rs\|crates/gwiki/src/synthesis/tests.rs]] | `crates/gwiki/src/synthesis/tests.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis/write.rs\|crates/gwiki/src/synthesis/write.rs]] | `crates/gwiki/src/synthesis/write.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gwiki/src/transcribe.rs\|crates/gwiki/src/transcribe.rs]] | `crates/gwiki/src/transcribe.rs` exposes 27 indexed API symbols. |
| [[code/files/crates/gwiki/src/vault.rs\|crates/gwiki/src/vault.rs]] | `crates/gwiki/src/vault.rs` exposes 15 indexed API symbols. |
| [[code/files/crates/gwiki/src/vector.rs\|crates/gwiki/src/vector.rs]] | `crates/gwiki/src/vector.rs` exposes 47 indexed API symbols. |
| [[code/files/crates/gwiki/src/video.rs\|crates/gwiki/src/video.rs]] | `crates/gwiki/src/video.rs` has no indexed API symbols. |
| [[code/files/crates/gwiki/src/video/alignment.rs\|crates/gwiki/src/video/alignment.rs]] | `crates/gwiki/src/video/alignment.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gwiki/src/video/markdown.rs\|crates/gwiki/src/video/markdown.rs]] | `crates/gwiki/src/video/markdown.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gwiki/src/video/sampling.rs\|crates/gwiki/src/video/sampling.rs]] | `crates/gwiki/src/video/sampling.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gwiki/src/video/tests.rs\|crates/gwiki/src/video/tests.rs]] | `crates/gwiki/src/video/tests.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gwiki/src/video/timestamps.rs\|crates/gwiki/src/video/timestamps.rs]] | `crates/gwiki/src/video/timestamps.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gwiki/src/video/write.rs\|crates/gwiki/src/video/write.rs]] | `crates/gwiki/src/video/write.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gwiki/src/vision.rs\|crates/gwiki/src/vision.rs]] | `crates/gwiki/src/vision.rs` exposes 32 indexed API symbols. |

