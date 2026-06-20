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

`docs/evidence/wiki-parity-2026-06` is an evidence archive for the June 2026 wiki-parity workstream. Its JSON artifacts cover compile, deposit, search, health, audit, and QA scenarios; most are indexed evidence objects, ranging from small compile-source records to large ask/search captures. The ask-daemon excerpts show a common output contract: `gwiki ask` resolves a project scope, records AI routing metadata, captures command/degradation status, and stores code citations plus evidence source paths (docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json:1-35).

The module’s key flow is “query, cite, preserve”: QA fixtures run `ask` in daemon mode against topics such as RRF search, Falkor graph integration, UUID5 compilation behavior, and ghook transport schemas, then persist the model route, citation set, and source excerpts. RRF QA ties the evidence back to `gcode`, `gwiki`, and `gcore` search modules (docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json:12-35), while Falkor QA crosses graph connection/read code, core Falkor support, graph boost, codewiki graph commands, and setup (docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-ask-daemon.json:12-35). UUID5 QA links the generated compile explainer artifact back into codewiki snapshot/change/io/model/rendering code (docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-ask-daemon.json:12-35).

Collaboration-wise, this directory sits downstream of `gwiki` query/answer tooling and upstream of documentation/audit consumers that need reproducible proof of parity. Its artifacts import evidence from generated wiki pages and code-file markdown mirrors: ghook QA, for example, cites schema, transport, envelope, and diagnostic files, then stores supporting module pages and ownership context as evidence (docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json:12-53).

| Fact | Values |
| --- | --- |
| Commands captured | `ask` (docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json:31-33) |
| AI route modes shown | `requested_mode: daemon`, `route: daemon` (docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json:3-10) |
| Model shown | `gpt-5.4-mini` (docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json:5-10) |
| Degradation status shown | `degraded: false`, `degraded_sources: []` (docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-ask-daemon.json:31-33) |
| Major artifact families | compile, deposit, health, audit, QA ask/search, hybrid search, source search |
| External systems cited | `crates/gcode`, `crates/gwiki`, `crates/gcore`, `crates/ghook` (docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json:12-29; docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json:12-29) |

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

