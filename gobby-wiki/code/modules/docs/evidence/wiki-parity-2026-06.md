---
title: docs/evidence/wiki-parity-2026-06
type: code_module
provenance:
- file: docs/evidence/wiki-parity-2026-06/wp3-audit.json
- file: docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json
- file: docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json
- file: docs/evidence/wiki-parity-2026-06/wp3-compile-source.json
- file: docs/evidence/wiki-parity-2026-06/wp3-deposit-ingest.json
- file: docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json
- file: docs/evidence/wiki-parity-2026-06/wp3-health.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-direct.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-search.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-ask-daemon.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-search.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-ask-daemon.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-search.json
- file: docs/evidence/wiki-parity-2026-06/wp3-search-hybrid.json
- file: docs/evidence/wiki-parity-2026-06/wp3-search-sources.json
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# docs/evidence/wiki-parity-2026-06

Parent: [[code/modules/docs/evidence|docs/evidence]]

## Overview

## docs/evidence/wiki-parity-2026-06

This module is a frozen set of JSON evidence artifacts captured during the third wiki-parity evaluation run (wp3) in June 2026. Each file is a structured snapshot of one `gwiki` subsystem or QA scenario, recording the exact inputs, routing decisions, retrieved evidence, search hit rankings, and synthesized AI answers produced at capture time. Taken together, the artifacts document the end-to-end behavior of the wiki pipeline — from compile and deposit through health monitoring and question-answering — against a fixed project scope (`project:3bf57fe7-2a0c-4074-8912-a83d9cd4df01`). The audit file `wp3-audit.json` carries no indexed symbols and serves as a bare-bones baseline record, while the remaining seventeen files expose between 2 and 205 indexed API properties depending on the depth of the captured operation.

The QA artifacts are the largest group and each targets a distinct capability. The ghook pair (`wp3-qa-ghook-ask-daemon.json`, `wp3-qa-ghook-ask-direct.json`) probes GitHub webhook inbox-envelope handling, pulling citations from `crates/ghook/src/envelope.rs`, `transport.rs`, and the v1 schema. The RRF pair (`wp3-qa-q2-rrf-*`) exercises Reciprocal Rank Fusion search, citing `crates/gcode/src/search/rrf.rs` and `crates/gwiki/src/search/rrf.rs`. The UUID5 pair (`wp3-qa-q3-uuid5-*`) targets content-identity hashing in the `codewiki` build pipeline, drawing on `build_parts/snapshot.rs`, `changes.rs`, and `io.rs`. The Falkor pair (`wp3-qa-q4-falkor-*`) covers graph-database integration via `crates/gcore/src/falkor.rs` and `crates/gcode/src/search/graph_boost.rs`. Each `ask-daemon` file routes through the AI daemon and records a full `synthesis` block including the generated answer, a citation-check result, truncation flags, and warnings; the corresponding `search` files record ranked hit lists without synthesis.

The ask-daemon and ask-direct response schemas share a common shape. Key top-level properties are shown below, alongside the search-hit fields that appear uniformly across all search and QA artifacts.

| Ask/daemon response property | Description |
|---|---|
| `ai.model` | Model used, e.g. `gpt-5.4-mini` |
| `ai.requested_mode` | Caller-requested routing (`daemon` or `direct`) |
| `ai.route` | Actual route taken |
| `ai.status` | AI availability (`available`, etc.) |
| `command` | Operation type (`ask` or `search`) |
| `degraded` / `degraded_sources` | Quality-degradation flag and affected sources |
| `evidence[].excerpt_chars` | Byte length of the retrieved excerpt |
| `evidence[].source_path` | Path to the raw source document |
| `evidence[].wiki_page` | Corresponding wiki-page path |
| `synthesis.answer` | AI-generated prose answer |
| `synthesis.citation_check.status` | Outcome of citation verification |
| `synthesis.citation_check.unsupported_claims` | Claims that could not be grounded |
| `synthesis.truncated` | Whether the context window was exceeded |
| `synthesis.truncated_components` | Which components were cut |
| `synthesis.warnings` | Runtime warnings |

| Search hit property | Description |
|---|---|
| `hits[].fusion_key` | Identifier used for cross-signal fusion |
| `hits[].result_type` | Result category |
| `hits[].score` | Combined fusion score |
| `hits[].snippet` | Text excerpt |
| `hits[].source_path` | Source file path |
| `hits[].title` | Result title |
| `hits[].wiki_page` | Associated wiki page |
| `hits[].explanations[].source` | Ranking signal name (e.g. `bm25`) |
| `hits[].explanations[].rank` | Per-signal rank |
| `hits[].explanations[].score` | Per-signal score |

The four QA scenario pairs and two standalone search files are summarized below alongside the remaining operational snapshots.

| File | Scenario / subsystem | Indexed symbols |
|---|---|---|
| `wp3-audit.json` | Baseline audit | 0 |
| `wp3-compile-source.json` | Source-compilation state | 2 |
| `wp3-compile-explainer.json` | Compile-pipeline explainer v1 | 32 |
| `wp3-compile-explainer-v2.json` | Compile-pipeline explainer v2 | 32 |
| `wp3-deposit-ingest.json` | Deposit ingestion | 19 |
| `wp3-deposit-search.json` | Deposit search | 55 |
| `wp3-health.json` | System health | 45 |
| `wp3-qa-ghook-ask-daemon.json` | ghook QA — daemon ask | 177 |
| `wp3-qa-ghook-ask-direct.json` | ghook QA — direct ask | 177 |
| `wp3-qa-ghook-search.json` | ghook QA — search | 69 |
| `wp3-qa-q2-rrf-ask-daemon.json` | RRF search QA — daemon ask | 205 |
| `wp3-qa-q2-rrf-search.json` | RRF search QA — search | 52 |
| `wp3-qa-q3-uuid5-ask-daemon.json` | UUID5 identity QA — daemon ask | 196 |
| `wp3-qa-q3-uuid5-search.json` | UUID5 identity QA — search | 49 |
| `wp3-qa-q4-falkor-ask-daemon.json` | Falkor graph QA — daemon ask | 205 |
| `wp3-qa-q4-falkor-search.json` | Falkor graph QA — search | 52 |
| `wp3-search-hybrid.json` | Hybrid search results | 83 |
| `wp3-search-sources.json` | Multi-source search results | 138 |

As a pure evidence store, this module does not import or export live code; it is consumed by evaluation and regression harnesses elsewhere in the project that compare wp3 snapshots against later runs to detect regressions in retrieval quality, citation accuracy, or AI routing behavior.
[docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json:3-10]
[docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-direct.json:3-10]
[docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json:3-10]
[docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-ask-daemon.json:3-10]
[docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-ask-daemon.json:3-10]

## Files

| File | Summary |
| --- | --- |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-audit.json\|docs/evidence/wiki-parity-2026-06/wp3-audit.json]] | `docs/evidence/wiki-parity-2026-06/wp3-audit.json` has no indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json\|docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json]] | `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json` exposes 32 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json\|docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json]] | `docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json` exposes 32 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-compile-source.json\|docs/evidence/wiki-parity-2026-06/wp3-compile-source.json]] | `docs/evidence/wiki-parity-2026-06/wp3-compile-source.json` exposes 2 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-deposit-ingest.json\|docs/evidence/wiki-parity-2026-06/wp3-deposit-ingest.json]] | `docs/evidence/wiki-parity-2026-06/wp3-deposit-ingest.json` exposes 19 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json\|docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json]] | `docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json` exposes 55 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-health.json\|docs/evidence/wiki-parity-2026-06/wp3-health.json]] | `docs/evidence/wiki-parity-2026-06/wp3-health.json` exposes 45 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json\|docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json]] | `docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json` exposes 177 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-direct.json\|docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-direct.json]] | `docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-direct.json` exposes 177 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-search.json\|docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-search.json]] | `docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-search.json` exposes 69 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json\|docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json]] | `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json` exposes 205 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json\|docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json]] | `docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json` exposes 52 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-ask-daemon.json\|docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-ask-daemon.json]] | `docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-ask-daemon.json` exposes 196 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-search.json\|docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-search.json]] | `docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-search.json` exposes 49 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-ask-daemon.json\|docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-ask-daemon.json]] | `docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-ask-daemon.json` exposes 205 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-search.json\|docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-search.json]] | `docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-search.json` exposes 52 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-search-hybrid.json\|docs/evidence/wiki-parity-2026-06/wp3-search-hybrid.json]] | `docs/evidence/wiki-parity-2026-06/wp3-search-hybrid.json` exposes 83 indexed API symbols. |
| [[code/files/docs/evidence/wiki-parity-2026-06/wp3-search-sources.json\|docs/evidence/wiki-parity-2026-06/wp3-search-sources.json]] | `docs/evidence/wiki-parity-2026-06/wp3-search-sources.json` exposes 138 indexed API symbols. |

