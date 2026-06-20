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

`docs/evidence` is an evidence archive module rather than a code-bearing module; the supplied view has no direct files and is represented by the child archive `docs/evidence/wiki-parity-2026-06`. That child module stores JSON evidence for the June 2026 wiki-parity workstream, covering compile, deposit, search, health, audit, and QA scenarios, with indexed objects ranging from small compile-source records to larger ask/search captures.

The key flow captured here is the `gwiki ask` evidence contract: an ask-daemon run resolves project scope, records AI routing metadata, captures command and degradation status, and stores both code citations and evidence source paths (`docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json:1-35`). In the wider system, external wiki/QA commands write evidence into this archive, while review, audit, and parity checks can read the stored status, citation, source, and search-result fields to validate behavior.

| Fact Type | Values |
| --- | --- |
| Child archive | `docs/evidence/wiki-parity-2026-06` |
| Evidence scenarios | Compile, deposit, search, health, audit, QA |
| CLI command evidenced | `gwiki ask` |
| Ask output fields | `scope`, `ai`, `route`, `model`, `status`, `command`, `degradations`, `code_citations`, `source_paths` |
| Search/evidence fields | `query`, `limit`, `results`, `rank`, `score`, `snippet`, `source_path`, `wiki_page` |
| Audit/health fields | `broken_links`, `duplicate_concepts`, `stale_citations`, `stale_pages`, `uncited_sources`, `uncompiled_sources` |
[docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json:3-10]
[docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:2]
[docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:2-11]
[docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json:3-10]
[docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-direct.json:3-10]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/docs/evidence/wiki-parity-2026-06\|docs/evidence/wiki-parity-2026-06]] | `docs/evidence/wiki-parity-2026-06` is an evidence archive for the June 2026 wiki-parity workstream. Its JSON artifacts cover compile, deposit, search, health, audit, and QA scenarios; most are indexed evidence objects, ranging from small compile-source records to large ask/search captures. The ask-daemon excerpts show a common output contract: `gwiki ask` resolves a project scope, records AI routing metadata, captures command/degradation status, and stores code citations plus evidence source paths (docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json:1-35). |

