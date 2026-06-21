---
title: docs
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

# docs

Parent: [[code/repo|Repository Overview]]

## Overview

## docs Module

The `docs` module is a schema and type-definition layer for a documentation intelligence platform. It holds no direct source files; instead it exposes a large catalogue of structured data contracts that downstream consumers—search, synthesis, indexing, and audit subsystems—share as a common vocabulary. Its single child module, `docs/evidence`, specialises in the evidence-gathering subsystem (excerpts, hit lists, and degradation tracking) that feeds the broader retrieval pipeline.

The module's component table reveals several cohesive schema families. An **indexing family** describes source ingestion state, tracking `chunks`, `documents`, `ingestions`, `links`, `sources`, `content_hash`, `raw_path`, and `location` per asset. A **search family** defines query contracts (`query`, `limit`, `degradations`) and ranked result records (`fusion_key`, `result_type`, `score`, `snippet`, `source_path`, `title`, `wiki_page`), each result carrying nested `explanations` with per-source `rank` and `score` sub-fields. A **synthesis family** captures AI-generated answers under `synthesis`, with a `citation_check` sub-record (`checked_claims`, `unsupported_claims`, `status`) and truncation metadata (`truncated`, `truncated_components`, `warnings`). An **AI-routing family** records dispatch telemetry: `ai`, `model`, `requested_mode`, `route`, `status`, `error`, `citations_kept`, `citations_stripped`, and `fallback_sections`. Finally, a **documentation-audit family** surfaces health signals: `broken_links` (keyed by `kind`, `line`, `path`, `target`), `stale_citations`, `stale_pages`, `uncited_sources`, `uncompiled_sources`, and `duplicate_concepts`.

Because no source excerpts or cross-file relationships were supplied, exact call sites cannot be cited; however, the sheer repetition of schema families across distinct component groups indicates that multiple versioned or endpoint-specific type variants coexist side by side within the module—a pattern common to contract-first systems where each API operation owns its own request/response shape while sharing a pool of leaf property types.

### Key Schema Families

| Family | Representative Properties |
| --- | --- |
| Indexing / Source | `asset_path`, `chunks`, `documents`, `ingestions`, `content_hash`, `raw_path`, `scope`, `kind`, `status` |
| Search Query | `command`, `query`, `limit`, `degradations`, `results` |
| Search Result | `fusion_key`, `result_type`, `score`, `snippet`, `source_path`, `title`, `wiki_page`, `sources` |
| Result Explanation | `rank`, `score`, `source` (nested under `explanations`) |
| AI Routing | `ai`, `model`, `requested_mode`, `route`, `status`, `error`, `citations_kept`, `citations_stripped`, `fallback_sections` |
| Synthesis Output | `synthesis`, `answer`, `model`, `truncated`, `truncated_components`, `warnings` |
| Citation Check | `citation_check`, `checked_claims`, `unsupported_claims`, `status` |
| Evidence | `evidence`, `excerpt_chars`, `source_path`, `wiki_page`, `hits`, `degraded`, `degraded_sources` |
| Code Citation | `code_citations`, `file`, `symbol` |
| Prompt Budgeting | `prompt_token_budget`, `prompt_tokens_estimated`, `tokens_estimated`, `truncated_sources` |
| Document Generation | `article_path`, `command`, `handoff_id`, `index_path`, `outline`, `page_writes`, `daemon_synthesis_available` |
| Audit / Health | `broken_links`, `stale_citations`, `stale_pages`, `uncited_sources`, `uncompiled_sources`, `duplicate_concepts`, `json_path`, `root`, `text_path` |

### Child Module

| Module | Responsibility |
| --- | --- |
| `docs/evidence` | Evidence collection subsystem — per-source excerpts, retrieval hit lists, and degraded-source tracking consumed by the synthesis pipeline |
[docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16]
[docs/evidence/wiki-parity-2026-06/wp3-audit.json:1-100]
[docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:2]
[docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:2-11]
[docs/evidence/wiki-parity-2026-06/wp3-health.json:3-16]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/docs/evidence\|docs/evidence]] | ## docs/evidence |

