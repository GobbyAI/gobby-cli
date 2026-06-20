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

`crates/gwiki` is the top-level gwiki module, combining a static CLI contract with the application crate that implements it. The contract defines gwiki’s identity as a local-first wiki CLI for capture, search, upkeep, and synthesis, along with contract version, global flags, scope selection, commands, JSON output shapes, and error codes (`crates/gwiki/contract/gwiki.contract.json:2-4`).

The application flow runs through command handling: commands resolve the active scope, invoke domain work, and return `CommandOutcome`. Ingestion accepts immutable raw sources from files, URLs, audio, video, images, PDFs, documents, sessions, MediaWiki, Wayback, and git, then writes raw Markdown/assets and returns an `IngestResult` containing source metadata and paths. Downstream flows index vault content, build/search graph and vector/keyword indexes, run health/audit checks, refresh stale sources, and synthesize or compile wiki pages.

Collaboration points are broad: the command layer calls into ingestion, indexing, search, graph, audit, health, source manifest, and synthesis subsystems; external callers interact through the CLI contract and public command/output types. The contract child module supplies the stable daemon/CLI-facing surface, while `src` owns the operational behavior behind that surface (`crates/gwiki/contract/gwiki.contract.json:2-4`).

| Area | Representative Symbols |
| --- | --- |
| CLI/contract | `contract`, `Cli`, `CliCommand`, `Command`, `CommandOutcome`, `CommandResult` |
| Scope | `ScopeSelection`, `ScopeIdentity`, `WikiScope`, `ResolvedScope`, `SearchScope` |
| Ingestion/source state | `IngestResult`, `SourceManifest`, `SourceRecord`, `SourceDraft`, `SourceKind`, `SourceReplay` |
| Search/index | `SearchRequest`, `WikiSearchResponse`, `WikiSearchResult`, `IndexOptions`, `WikiIndexStore` |
| Graph | `WikiGraphFacts`, `MemoryWikiGraph`, `GraphExport`, `GraphContextPack`, `CodeGraphQuery` |
| Quality/upkeep | `AuditOptions`, `AuditReport`, `HealthReport`, `TrustReport`, `LintReport` |
| Synthesis/compile | `CompileRequest`, `CompileOutcome`, `WikiCompileOptions`, `SynthesisInput`, `SynthesizedPage` |
[crates/gwiki/src/commands/refresh/selection.rs:4-75]
[crates/gwiki/src/commands/refresh/vault.rs:7-9]
[crates/gwiki/src/commands/ask/synthesis.rs:15-45]
[crates/gwiki/src/commands/audit.rs:3-13]
[crates/gwiki/src/commands/citation_quality.rs:26-33]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gwiki/contract\|crates/gwiki/contract]] | The `crates/gwiki/contract` module defines the static CLI contract for `gwiki`: tool identity, contract version, global flags, scope selection, commands, JSON output shapes, and error-code surface. The contract identifies `gwiki` as a local-first wiki CLI for capture, search, upkeep, and synthesis (`crates/gwiki/contract/gwiki.contract.json:2-4`), with the supplied file summary indicating 429 indexed API symbols. |
| [[code/modules/crates/gwiki/src\|crates/gwiki/src]] | `crates/gwiki/src` is the gwiki application crate: it combines CLI command handling, source ingestion, vault indexing, search, graph construction, audit/health checks, and synthesis. The ingestion layer owns immutable raw-source intake across audio, documents, files, git, images, MediaWiki, PDF, sessions, URLs, video, and Wayback captures, with shared helpers that write raw Markdown/assets and return an `IngestResult` containing a `SourceRecord`, raw path, and optional asset path . The command layer is the user-facing orchestration boundary: commands resolve active scope, perform domain work,… |

