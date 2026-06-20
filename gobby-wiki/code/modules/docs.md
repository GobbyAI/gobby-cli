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

The `docs` module is a documentation/evidence area with no direct files in the supplied view. Its active responsibility is delegated to `docs/evidence`, which is described as an archive rather than code-bearing module, represented by `docs/evidence/wiki-parity-2026-06`.

That child archive stores JSON evidence for the June 2026 wiki-parity workstream. The captured flows include compile, deposit, search, health, audit, and QA scenarios, with records ranging from small compile-source evidence to larger ask/search captures. No cross-file relationships or file:line anchors were supplied, so caller/import collaboration cannot be cited more specifically.

| Area | Supplied Facts |
| --- | --- |
| Direct files | None |
| Child module | `docs/evidence` |
| Archive path | `docs/evidence/wiki-parity-2026-06` |
| Evidence format | JSON |
| Workstream | June 2026 wiki parity |
| Scenario coverage | compile, deposit, search, health, audit, QA |

| Property Group | Representative Fields |
| --- | --- |
| AI/synthesis status | `ai`, `model`, `requested_mode`, `route`, `status`, `error` |
| Compile/output tracking | `citations_kept`, `citations_stripped`, `fallback_sections`, `article_path`, `index_path`, `outline`, `page_writes` |
| Source/index metadata | `source_paths`, `source_path`, `raw_path`, `content_hash`, `wiki_page`, `sources` |
| Search evidence | `query`, `limit`, `results`, `rank`, `score`, `snippet`, `fusion_key`, `result_type` |
| Audit/QA evidence | `broken_links`, `duplicate_concepts`, `stale_citations`, `stale_pages`, `uncited_sources`, `uncompiled_sources` |
| Citation checks | `citation_check`, `checked_claims`, `unsupported_claims`, `code_citations` |
[docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:2]
[docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:2-11]
[docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-direct.json:3-10]
[docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16]
[docs/evidence/wiki-parity-2026-06/wp3-audit.json:1-100]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/docs/evidence\|docs/evidence]] | `docs/evidence` is an evidence archive module rather than a code-bearing module; the supplied view has no direct files and is represented by the child archive `docs/evidence/wiki-parity-2026-06`. That child module stores JSON evidence for the June 2026 wiki-parity workstream, covering compile, deposit, search, health, audit, and QA scenarios, with indexed objects ranging from small compile-source records to larger ask/search captures. |

