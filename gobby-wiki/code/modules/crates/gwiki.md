---
title: crates/gwiki
type: code_module
provenance:
- file: crates/gwiki/contract/gwiki.contract.json
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
provenance_truncated: 159
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki

Parent: [[code/modules/crates|crates]]

## Overview

## Module: `crates/gwiki`

`crates/gwiki` is the top-level crate for the **gwiki** command-line tool, a multimodal personal knowledge-management system built on an Obsidian-compatible Markdown vault. The crate is split into two sub-modules: `contract`, which publishes a machine-readable JSON description of every command, flag, and output key so that daemon and shell integrations can introspect the tool without parsing help text; and `src`, which contains the full runtime — CLI parsing, command dispatch, ingest orchestration, search, AI synthesis, graph analytics, and vault maintenance. The `contract` function assembles `contract_version`, `global_flags`, `commands`, `identity_keys`, and `error_codes` into a structured payload consumed by the daemon probe layer (`probe_contract`) and integration tests such as `crate_has_no_gcode_dependency`.

The ingestion pipeline accepts a wide variety of content kinds — Markdown files, URLs, audio, video, images, PDFs, Office documents, Git repositories, AI session archives (Claude Code, Codex, Droid, Gemini, Grok, Qwen), and MediaWiki pages — each routed through a dedicated orchestrator (`ingest_path`, `ingest_audio`, `ingest_video`, `ingest_document`, `ingest_image`, `ingest_repository`, `ingest_snapshot`, `sync_session_transcript_archives`). Raw assets are written atomically via `write_raw_then_index` before being handed to `index_vault`, which upserts documents, chunks, links, and source records into either a `MemoryWikiStore` or a `PostgresWikiStore`. Optional services — Qdrant for semantic vectors (`sync_scope_vectors`, `GwikiQdrantVectorStore`) and FalkorDB for graph analytics (`WikiGraphFacts`, `FalkorGraphBoostBackend`) — are treated as degradable dependencies; missing or unreachable backends produce structured `DaemonDegradation` values rather than hard failures.

Query and synthesis features are layered on top of the index. The `search` entry point fuses BM25 keyword results (`search_bm25`), semantic vector results (`search_semantic`), and graph-neighbourhood boosts (`search_graph_boost`) using reciprocal-rank fusion (`fuse_sources`). The `ask` command plans evidence (`plan_evidence`, `EvidencePlan`), calls an LLM for synthesis, strips model narration (`strip_leading_model_narration`), runs a citation check, and emits `AskOutput` with grounded claims. `compile_to_wiki` drives the research-to-wiki compilation loop, invoking an `ExplainerTransport` to generate prose sections and recording provenance via `ProvenanceGraph`. Audit, health, lint, normalize, benchmark, and citation-quality commands each produce typed report objects (`AuditReport`, `HealthReport`, `LintReport`, `BenchmarkReport`, `CitationQualityReport`) that are rendered as both JSON and plain text.

| CLI command | Key options struct | Output type |
|---|---|---|
| `setup` | `SetupArgs` / `SetupOptions` | `PostgresSetupResult` |
| `index` | `IndexOptions` | `IndexReport` |
| `ingest file` | `IngestFileOptions` | `IndexReport` |
| `ingest url` | `UrlBatchIngest` | `UrlBatchIngest` |
| `search` | `SearchArgs` | `SearchOutput` |
| `ask` | `AskArgs` | `AskOutput` |
| `read` | `ReadArgs` | `ReadOutput` |
| `compile` | `CompileArgs` | `WikiCompileOutcome` |
| `refresh` | `RefreshArgs` | `RefreshRender` |
| `collect` | — | `CollectReport` |
| `audit` | `AuditOptions` | `AuditOutput` |
| `health` | — | `HealthReport` |
| `lint` | — | `LintReport` |
| `normalize` | `NormalizeArgs` | `NormalizeReport` |
| `benchmark` | `BenchmarkArgs` / `BenchmarkOptions` | `BenchmarkReport` |
| `review` | `ReviewReportArgs` / `ReviewReportOptions` | `ReviewReport` |
| `export` | `ExportArgs` | `ExportOutput` |
| `sync-sessions` | `SyncSessionsArgs` | `SessionArchiveBatchIngest` |
| `backlinks` | `BacklinksArgs` | wiki backlink list |
| `link-suggest` | `LinkSuggestArgs` | `LinkSuggestion` list |
| `source list/remove` | `RemoveSourceArgs` | `RemoveSourceRender` |
| `status` | — | `RuntimeStatus` |

| Key environment variable | Purpose |
|---|---|
| `GOBBY_HOME` | Root directory for hub config and registry (`gobby_home`) |
| `DATABASE_URL` | PostgreSQL connection string (`database_url_from_env`) |
| `GWIKI_STALE_CITATION_YEARS` | Override stale-citation age threshold (`stale_citation_years_from_env`) |
| `GWIKI_MAX_INBOX_ITEM_BYTES` | Cap on inbox item size (`max_inbox_item_bytes_from_env`) |
[crates/gwiki/src/commands/ask/citation.rs:25-46]
[crates/gwiki/src/commands/ask/evidence.rs:14-16]
[crates/gwiki/src/commands/ask/narration.rs:7-58]
[crates/gwiki/src/commands/ask/synthesis.rs:15-45]
[crates/gwiki/src/commands/citation_quality.rs:26-33]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gwiki/contract\|crates/gwiki/contract]] | ## crates/gwiki/contract |
| [[code/modules/crates/gwiki/src\|crates/gwiki/src]] | ## Module: `crates/gwiki/src` |

