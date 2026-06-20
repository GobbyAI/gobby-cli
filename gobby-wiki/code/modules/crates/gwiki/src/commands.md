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

The `crates/gwiki/src/commands` module is the command layer for gwiki: each file implements a user-facing operation, resolves the active wiki scope, performs domain work, and returns a `CommandOutcome`. Commands cover retrieval and reading, source management, indexing/search/graph workflows, trust and citation review, setup/status, export/compile, and AI-assisted answering. For example, `read` resolves scope, dispatches by `ReadTarget::Path` or `ReadTarget::Title`, validates scoped paths, and renders structured read output (`crates/gwiki/src/commands/read.rs:16-28`, `crates/gwiki/src/commands/read.rs:30-58`). `sources` lists and removes manifest-backed sources, guarding scope roots and staging raw/source asset deletion before re-indexing when not in dry-run mode (`crates/gwiki/src/commands/sources.rs:12-21`, `crates/gwiki/src/commands/sources.rs:23-74`).

Several commands coordinate richer multi-step flows. `ask` turns search retrieval into grounded answers by building a bounded `EvidencePlan` from `SearchRetrieval`, centering excerpts around query terms, estimating tokens, enforcing a 12,000-token prompt budget, then routing text generation through shared AI configuration and recording requested/effective route metadata. `citation_quality` builds a report with dependency metadata and sections for credibility, coverage gaps, contradictions, stale sources, and confidence (`crates/gwiki/src/commands/citation_quality.rs:21-48`); its contradiction submodule accepts a `ProvenanceGraph`, AI availability, and an injected detector, and explicitly returns an unavailable section rather than fabricating findings when AI is off (`crates/gwiki/src/commands/citation_quality/contradictions.rs:27-65`, `crates/gwiki/src/commands/citation_quality/contradictions.rs:31-41`). `refresh` plans source replays from manifest records, validates raw source paths, serializes replay metadata, and reports skipped or failed refreshes for unsupported or malformed source records (`crates/gwiki/src/commands/refresh/selection.rs:1`, `crates/gwiki/src/commands/refresh/selection.rs:5`, `crates/gwiki/src/commands/refresh/selection.rs:36`, `crates/gwiki/src/commands/refresh/model.rs:39`, `crates/gwiki/src/commands/refresh/model.rs:46`, `crates/gwiki/src/commands/refresh/model.rs:54`).

The command layer sits between CLI-facing request types and lower-level gwiki subsystems. It imports shared scope helpers such as `resolve_command_scope`, `resolved_scope_identity`, and `resolve_selection_context` to constrain all operations to the selected vault (`crates/gwiki/src/commands/sources.rs:9-10`, `crates/gwiki/src/commands/read.rs:7-8`, `crates/gwiki/src/commands/review_report.rs:16`). It calls out to manifests, provenance, health/lint, PostgreSQL, FalkorDB/code graph analytics, search, exports, and AI routing depending on the command (`crates/gwiki/src/commands/citation_quality.rs:5-18`, `crates/gwiki/src/commands/review_report.rs:5-21`). `review_report` illustrates the wider integration point: it resolves selection context, requires PostgreSQL index configuration, optionally loads FalkorDB config, loads wiki graph facts and provenance, then asks the code graph subsystem for affected pages (`crates/gwiki/src/commands/review_report.rs:24-61`).

| Public API / Type | Role |
| --- | --- |
| `execute` | Common command entry point name used across command files. |
| `CitationQualityReport` | Serialized citation-quality report root (`crates/gwiki/src/commands/citation_quality.rs:21-28`). |
| `DependencyMetadata` | Captures hard, optional, and multimodal dependencies (`crates/gwiki/src/commands/citation_quality.rs:30-35`). |
| `CitationQualitySections` | Groups credibility, coverage, contradiction, stale-source, and confidence sections (`crates/gwiki/src/commands/citation_quality.rs:37-45`). |
| `SourceCredibility` | Per-source credibility score and signals (`crates/gwiki/src/commands/citation_quality.rs:55-62`). |
| `RefreshPlan::from_record` / `RefreshPlan::serialize` | Build and report refresh replay plans (`crates/gwiki/src/commands/refresh/model.rs:39`, `crates/gwiki/src/commands/refresh/model.rs:46`). |

| Environment Variable | Purpose |
| --- | --- |
| `GWIKI_READ_MAX_BYTES` | Caps bytes read by the `read` command; defaults to 1 MiB (`crates/gwiki/src/commands/read.rs:12-13`). |

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gwiki/src/commands/ask\|crates/gwiki/src/commands/ask]] | The `ask` module turns search retrieval into a grounded answer. `evidence.rs` builds a bounded `EvidencePlan` from `SearchRetrieval`, centering excerpts around query terms with `query_window`, estimating tokens conservatively, and dropping later hits once the prompt would exceed the 12,000-token budget . `synthesis.rs` then resolves gwiki’s shared AI routing, records requested and effective route metadata on `AskOutput`, and dispatches the single text-generation call through either the direct OpenAI-compatible path or the daemon path . |
| [[code/modules/crates/gwiki/src/commands/citation_quality\|crates/gwiki/src/commands/citation_quality]] | `crates/gwiki/src/commands/citation_quality/contradictions.rs` builds the contradiction-detection portion of citation quality reporting. Its main entry point, `contradiction_section`, accepts a `ProvenanceGraph`, an AI availability flag, and an injected detector callback, then returns a `ContradictionSection` for the parent command layer (crates/gwiki/src/commands/citation_quality/contradictions.rs:27-65). It explicitly avoids inventing results when AI is unavailable, returning an unavailable section with a note and no findings… |
| [[code/modules/crates/gwiki/src/commands/refresh\|crates/gwiki/src/commands/refresh]] | The `refresh` module plans and executes source replays for the wiki vault. Selection turns manifest records into `RefreshPlan`s, either for all refreshable records or for explicit source IDs; unsupported source kinds are skipped in broad refreshes, while missing explicit IDs and replay-metadata problems become `RefreshFailure`s ((crates/gwiki/src/commands/refresh/selection.rs:1), (crates/gwiki/src/commands/refresh/selection.rs:5), (crates/gwiki/src/commands/refresh/selection.rs:36)). Plans validate that a stored source ID maps to a raw source path before entering the refresh flow, and… |

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

