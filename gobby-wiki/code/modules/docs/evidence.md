---
title: docs/evidence
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

# docs/evidence

Parent: [[code/modules/docs|docs]]

## Overview

## docs/evidence

The `docs/evidence` module is a structured artifact store that captures machine-readable snapshots of every significant operation performed by an AI-assisted wiki-documentation pipeline. It contains no executable source files; instead it is organized as a hierarchy of typed, self-describing evidence records—each carrying a `scope`, `id`, and `kind` discriminant—that together form a durable audit trail spanning synthesis runs, retrieval sessions, source-indexing passes, and content-quality checks. The sole child module, `docs/evidence/wiki-parity-2026-06`, groups artifacts produced during the June 2026 wiki-parity review cycle, indicating that evidence is partitioned by milestone or date range rather than by system component.

Each record belongs to one of several recognizable families distinguished by their property sets. AI synthesis records carry `ai`, `model`, `route`, `requested_mode`, `status`, and `error` alongside citation metrics (`citations_kept`, `citations_stripped`) and graceful-degradation indicators (`fallback_sections`). Wiki-generation records track `article_path`, `index_path`, `outline`, `page_writes`, and `handoff_id`, and note daemon availability via `daemon_synthesis_available`. Search-session records expose `query`, `limit`, `results`, and `degradations`, while each result entry carries hybrid-fusion scoring data (`fusion_key`, `result_type`, `score`, `snippet`, `source_path`, `title`, `wiki_page`) and per-source ranked explanations (`rank`, `score`, `source`, `explanations`). Prompt-snapshot records preserve the full prompt triple (`system`, `user`, `prompt`) together with budget and truncation metadata (`tokens_estimated`, `truncated_sources`, `prompt_token_budget`, `prompt_tokens_estimated`).

Content-quality and source-health records round out the schema. Indexing snapshots hold counts of `chunks`, `documents`, `ingestions`, `links`, and `sources` alongside `path` and `raw_path`. Citation-audit records flag `stale_citations`, `stale_pages`, `uncited_sources`, `uncompiled_sources`, and `duplicate_concepts`. Link-audit records list `broken_links` entries with `kind`, `line`, `path`, and `target` sub-fields. Synthesis-output records wrap a final `answer` together with a `citation_check` sub-object (`checked_claims`, `unsupported_claims`, `status`) and truncation warnings (`truncated`, `truncated_components`, `warnings`). Evidence-bundle records tie a wiki page to its supporting sources through `evidence`, `degraded`, `degraded_sources`, and `excerpt_chars`. Code-citation records close the loop between prose and implementation by recording `file`/`symbol` pairs under `code_citations`.

Because no direct source files are present and no cross-file relationships are supplied, the module acts purely as a data sink consumed and queried by external tooling. The consistent `scope`/`id`/`kind` envelope on every record type provides the primary indexing surface for locating, filtering, and comparing evidence artifacts across runs or milestones.

---

### Evidence record families

| Family | Distinguishing properties |
|---|---|
| Record envelope | `scope`, `id`, `kind` |
| AI synthesis | `ai`, `model`, `route`, `requested_mode`, `status`, `error`, `citations_kept`, `citations_stripped`, `fallback_sections` |
| Wiki generation | `article_path`, `index_path`, `outline`, `page_writes`, `handoff_id`, `daemon_synthesis_available` |
| Prompt snapshot | `system`, `user`, `prompt`, `tokens_estimated`, `truncated_sources`, `prompt_token_budget`, `prompt_tokens_estimated` |
| Search session | `command`, `query`, `limit`, `results`, `degradations` |
| Search result hit | `fusion_key`, `result_type`, `score`, `snippet`, `source_path`, `title`, `wiki_page`, `rank`, `explanations` |
| Source index | `asset_path`, `indexed`, `chunks`, `documents`, `ingestions`, `links`, `sources`, `path`, `raw_path` |
| Source item | `id`, `kind`, `source`, `content_hash`, `location`, `status` |
| Synthesis output | `answer`, `citation_check` (`checked_claims`, `unsupported_claims`, `status`), `model`, `truncated`, `truncated_components`, `warnings` |
| Evidence bundle | `evidence`, `degraded`, `degraded_sources`, `excerpt_chars`, `source_path`, `wiki_page` |
| Citation audit | `stale_citations`, `stale_pages`, `uncited_sources`, `uncompiled_sources`, `duplicate_concepts` |
| Link audit | `broken_links` → (`kind`, `line`, `path`, `target`) |
| Code citation | `code_citations` → (`file`, `symbol`) |

### Child modules

| Module | Purpose |
|---|---|
| `docs/evidence/wiki-parity-2026-06` | Evidence artifacts scoped to the June 2026 wiki-parity review milestone |
[docs/evidence/wiki-parity-2026-06/wp3-search-hybrid.json:3-20]
[docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16]
[docs/evidence/wiki-parity-2026-06/wp3-audit.json:1-100]
[docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:2]
[docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:2-11]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/docs/evidence/wiki-parity-2026-06\|docs/evidence/wiki-parity-2026-06]] | ## docs/evidence/wiki-parity-2026-06 |

