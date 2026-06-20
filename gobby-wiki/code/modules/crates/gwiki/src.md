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

`crates/gwiki/src` is the gwiki application crate: it turns scoped wiki vaults into ingestible, searchable, auditable knowledge bases. The core ingest boundary writes immutable raw markdown/assets and returns an `IngestResult` with the registered `SourceRecord`, raw path, and optional asset path, while child ingest modules handle files, URLs, PDFs, audio, video, images, sessions, git, MediaWiki, and Wayback captures . Commands sit above these subsystems, resolving scoped inputs, reading vault state, invoking shared services, and rendering `CommandOutcome`s; the command layer pulls together scope, manifests, provenance, health/lint, search, and `gobby_core` AI/config/database facilities .

The main runtime flows are source ingestion, indexing/search, graph enrichment, and trust/reporting. Search centralizes BM25, graph boost, reciprocal-rank fusion, semantic search, scoped filtering, hit kinds, provenance, request/response types, and backend error handling . The graph layer defines wiki graph facts for documents, sources, links, and code edges, plus export options and graph reports, then downstream FalkorDB support loads/syncs those facts for graph search , . Health and benchmark flows read lint reports, manifests, provenance, Postgres counts, Falkor/Qdrant availability, and AI routing state to produce persisted health snapshots and degradation-aware performance reports , .

AI-backed collaboration is split by responsibility rather than buried in commands. `ai` owns chunked transcription and audio translation, including direct English translation with transcription-plus-segment fallback [crates/gwiki/src/ai/mod.rs:1-4]. `compile` bridges accepted research notes into wiki synthesis inputs, importing session state, synthesis APIs, citation rendering, and explainer generation , while `synthesis` defines article targets, source bundles, prompt telemetry, synthesized pages, write policies, and optional explainer reports . Runtime configuration is hub-aware: `HubPrimary` reads config through PostgreSQL when available, resolves `$secret:` values through the hub, and rejects secret references without a hub; `hub_ai_config_source` wires that into command execution by resolving Gobby home, finding a hub DSN, and constructing an `AiConfigSource` .

| Public Surface | Role | Evidence |
| --- | --- | --- |
| `IngestResult` | Shared ingest return value for registered source, raw markdown path, and optional asset path |  |
| `WikiGraphFacts` | In-memory fact bundle for graph export/search: documents, links, sources, code edges | [crates/gwiki/src/graph/mod.rs:52-59] |
| `GraphExportOptions` | Marks graph exports available or degraded with source labels |  |
| `HealthReport` | Serialized health output for stale pages/citations, uncited/uncompiled sources, links, duplicates, and report paths |  |
| `BenchmarkReport` | Serialized benchmark output for compression, graph coverage, retrieval precision, source mix, model availability, and degradations |  |

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gwiki/src/ai\|crates/gwiki/src/ai]] | `crates/gwiki/src/ai` is the gwiki AI integration layer. Its module root exposes three internal submodules, `chunk`, `clients`, and `translate` [crates/gwiki/src/ai/mod.rs:1-4]. `chunk` owns audio chunk sizing and splitting abstractions, including upload/window constants, `AudioChunk`, `ChunkedTranscription`, `ChunkTranscriptionMode`, and the `AudioChunker` trait backed by `MediaAudioChunker` . `translate` owns language-normalization flow for audio translation: it prefers direct English translation, falls back to transcription plus segment translation on failure, and marks degraded output… |
| [[code/modules/crates/gwiki/src/audit\|crates/gwiki/src/audit]] | The `crates/gwiki/src/audit` module audits wiki pages for unsupported claims and renders the resulting report. Its claim pass takes a `WikiPage`, `ProvenanceGraph`, shared `AuditSourceContext`, and `AuditOptions`, derives candidate claim lines, computes provenance-supported lines, checks CodeWiki frontmatter support, and filters out claims that already have provenance or inline citations before emitting `UnsupportedClaim` records with path, line, heading, reason, and source context . |
| [[code/modules/crates/gwiki/src/commands\|crates/gwiki/src/commands]] | The `crates/gwiki/src/commands` module is the CLI command layer for gwiki: it resolves scoped wiki inputs, reads vault state, calls shared subsystems, and renders `CommandOutcome`s. Command files cover reading pages, source management, indexing/search, graph/reporting, citation quality, refresh, setup/status, and AI-backed flows such as ask and librarian. The layer imports core concerns from `crate::support::scope`, manifests, provenance, health/lint, search, and `gobby_core` AI/config/database facilities, then adapts them into command-specific outputs (for example, citation quality pulls… |
| [[code/modules/crates/gwiki/src/compile\|crates/gwiki/src/compile]] | `crates/gwiki/src/compile` prepares research-session handoffs into wiki-ready synthesis inputs. Its core data surface is defined in `mod.rs`: `CompileRequest` captures topic, outline, optional target page, and write intent, while `CompileBundle`, `CompileOutcome`, and `WikiCompileOutcome` carry accepted sources, citations, conflict/gap notes, generated prompts, write results, and optional explainer output (crates/gwiki/src/compile/mod.rs:24-95). The module imports session state, synthesis APIs, citation rendering, and explainer generation, so it sits between accepted research notes and the… |
| [[code/modules/crates/gwiki/src/falkor_graph\|crates/gwiki/src/falkor_graph]] | `crates/gwiki/src/falkor_graph` builds and consumes FalkorDB-backed graph data for wiki search. It loads wiki documents, links, and sources from PostgreSQL into `WikiGraphFacts`, resolving internal link targets while preserving unresolved wiki targets and skipping external URLs (`wiki_facts.rs:12-63`, `tests.rs:24-73`). It also loads graph boost data from FalkorDB, querying scoped or global `WikiDoc` nodes and links with caps that report partial degradation when limits are exceeded (`boost.rs:10-60`). |
| [[code/modules/crates/gwiki/src/graph\|crates/gwiki/src/graph]] | `crates/gwiki/src/graph` defines the wiki graph model and the serializable products built from it. The root module exposes graph vocabulary constants, document/source/link/code-edge fact types, `WikiGraphFacts`, export options, and `GraphExport`; it also publishes `analytics` and `context`, keeps `export` private, and re-exports `render_graph_report` for outside callers (`crates/gwiki/src/graph/mod.rs:7-19`, `crates/gwiki/src/graph/mod.rs:21-92`). |
| [[code/modules/crates/gwiki/src/ingest\|crates/gwiki/src/ingest]] | The `ingest` module is the shared boundary for turning external inputs into immutable wiki sources. Its root declares the ingest submodules and central result type, `IngestResult`, which carries the registered `SourceRecord`, raw markdown path, and optional asset path; it also provides common helpers for extension normalization, raw markdown writes, asset writes, suffixed asset writes, and source-path asset preservation (`crates/gwiki/src/ingest/mod.rs:1-100`). Child modules specialize that pattern for local files, URLs, documents, PDFs, audio, video, images, session archives, MediaWiki/git… |
| [[code/modules/crates/gwiki/src/search\|crates/gwiki/src/search]] | The `crates/gwiki/src/search` module is the shared search layer for wiki content. It exposes lexical BM25, graph-boost, reciprocal-rank fusion, and semantic search submodules from one namespace (`mod.rs:1-4`), while centralizing common concepts such as `SearchScope`, `SearchSource`, hit kinds, provenance, results, requests, responses, and errors (`mod.rs:11-100`). Scopes support global, project, and topic filtering, with helper methods that produce a kind/value pair or an optional filter tuple for downstream backends (`mod.rs:11-51`). |
| [[code/modules/crates/gwiki/src/sources\|crates/gwiki/src/sources]] | The `sources` module owns raw source tracking for a gwiki vault: it defines source metadata types, renders source entries into the generated manifest section, reads existing manifest markers back from the raw source index, and writes updates safely. Core metadata covers source kind, ingestion method, and compile status, all serialized with snake-case names and displayed as stable strings (`crates/gwiki/src/sources/types.rs:9-72`). |
| [[code/modules/crates/gwiki/src/store\|crates/gwiki/src/store]] | The `store` module defines the gwiki indexing boundary: shared document/chunk/link/source models, ingestion bookkeeping, scoped identity, validation helpers, and interchangeable `WikiIndexStore` implementations. `types.rs` owns the core data contracts such as `WikiDocument`, `WikiChunk`, `WikiLink`, `WikiSource`, ingestion events, `StoreError`, and `WikiStoreScope`; scope wraps `crate::models::WikiScope` and exposes project/topic identity helpers for storage backends (`crates/gwiki/src/store/types.rs:1-100`). |
| [[code/modules/crates/gwiki/src/support\|crates/gwiki/src/support]] | `crates/gwiki/src/support` is the utility layer for gwiki runtime plumbing: configuration, environment discovery, graph shaping, and text/search helpers. Config is hub-aware: `HubPrimary` implements `ConfigSource`, reads values through PostgreSQL when available, resolves `$secret:` values through the hub, and rejects secret references when no hub exists (crates/gwiki/src/support/config.rs:18-43). `hub_ai_config_source` ties this to command execution by resolving Gobby home, asking `support::env::database_url_for` for a hub DSN, optionally connecting to Postgres, and building an… |
| [[code/modules/crates/gwiki/src/synthesis\|crates/gwiki/src/synthesis]] | `crates/gwiki/src/synthesis` owns the data and safety envelope for turning accepted knowledge handoffs into vault pages. Its types define article targets, source bundles, generation input, prompt telemetry, synthesized pages, and write outcomes; synthesized concept/topic pages can carry an `ExplainerReport`, while source pages leave it absent (`crates/gwiki/src/synthesis/types.rs:1-67`). `ArticleKind` provides the stable mapping from logical article type to vault directory and source-kind metadata (`crates/gwiki/src/synthesis/types.rs:7-30`). |
| [[code/modules/crates/gwiki/src/video\|crates/gwiki/src/video]] | The `crates/gwiki/src/video` module models and assembles video-derived wiki content: sampled frames, frame descriptions, transcript alignment, audio references, media metadata/degradations, and the final markdown result. Its central request type, `VideoMarkdownRequest`, carries the original asset/raw paths, MIME and duration metadata, degradation records, frame samples/images/descriptions, transcript segments, and optional transcription output into markdown generation (`crates/gwiki/src/video/types.rs:55-74`). |

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

