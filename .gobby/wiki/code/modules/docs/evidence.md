---
title: docs/evidence
type: code_module
provenance:
- file: docs/evidence/wiki-parity-2026-06/wp3-audit.json
  ranges:
  - 1-100
- file: docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json
  ranges:
  - 3-47
- file: docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json
  ranges:
  - 3-44
- file: docs/evidence/wiki-parity-2026-06/wp3-compile-source.json
  ranges:
  - 2-3
- file: docs/evidence/wiki-parity-2026-06/wp3-deposit-ingest.json
  ranges:
  - 3-24
- file: docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json
  ranges:
  - 2-90
- file: docs/evidence/wiki-parity-2026-06/wp3-health.json
  ranges:
  - 3-71
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json
  ranges:
  - 3-299
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-direct.json
  ranges:
  - 3-295
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-search.json
  ranges:
  - 2-113
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json
  ranges:
  - 3-341
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json
  ranges:
  - 2-84
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-ask-daemon.json
  ranges:
  - 3-327
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-search.json
  ranges:
  - 2-78
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-ask-daemon.json
  ranges:
  - 3-341
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-search.json
  ranges:
  - 2-84
- file: docs/evidence/wiki-parity-2026-06/wp3-search-hybrid.json
  ranges:
  - 3-137
- file: docs/evidence/wiki-parity-2026-06/wp3-search-sources.json
  ranges:
  - 3-227
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# docs/evidence

Parent: [[code/modules/docs|docs]]

## Overview

The docs/evidence module has no direct files of its own; it serves as the parent container for generated evidence bundles. Its current child, docs/evidence/wiki-parity-2026-06, captures the 2026-06 wiki-parity workstream for the wp3 scope, preserving auditable outputs from gwiki and ghook flows across compilation, ingestion, search, and ask operations [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12] [docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16] [docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json:3-10].

The key flow begins with compile records that retain AI synthesis metadata, prompts, article and index paths, and page writes, then ingestion records bind markdown source notes to raw paths, content hashes, and indexed totals. Search records add query metadata, degradation state, ranked results, snippets, scores, source paths, wiki pages, and code citations, while ask records capture route status, cited evidence, ranked hits, final synthesis, citation checks, truncation, and warnings [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12] [docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16] [docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json:3-10].

Together these generated JSON artifacts collaborate as a traceable evidence ledger: compile outputs describe what was written, ingestion outputs describe what source material entered the index, search outputs explain how evidence was retrieved and ranked, and ask outputs show how the retrieved evidence was used and checked in final answers. The parent module’s responsibility is therefore organizational rather than executable, grouping the evidence bundle so downstream reviewers can audit wiki parity behavior from source capture through synthesis.

## Child Modules

- [[code/modules/docs/evidence/wiki-parity-2026-06|docs/evidence/wiki-parity-2026-06]] - This module is a generated evidence bundle for the 2026-06 wiki-parity workstream, centered on the `wp3` project scope. Its files record auditable outputs from `gwiki` and `ghook` flows: compile runs that preserve AI synthesis metadata, prompts, article/index paths, and page writes; ingestion runs that tie markdown source notes to raw paths, content hashes, and indexed totals; search runs that store query metadata, degradations, ranked results, snippets, scores, source paths, wiki pages, and code citations; and ask runs that capture AI route status, cited evidence, ranked hits, final synthesis, citation checks, truncation, and warnings [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12]  [docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16] [docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json:3-10].

The key flows are parity verification, retrieval auditability, and generated-article traceability. Search evidence files capture the command, query, limit, degradations, and ranked result explanations, while ask evidence files layer daemon or direct AI metadata over citations, evidence excerpts, hits, and synthesis; the source excerpts show daemon ask records resolving the same project scope, using `gpt-5.4-mini`, routing through `daemon`, and marking the route available before listing code citations and evidence entries    .

The files collaborate as a flat, no-child-module evidence directory: compile and ingest records establish what content was produced or indexed, search and ask bundles show how answers were retrieved and synthesized, and health/audit reports summarize quality gaps such as broken links, stale or uncited sources, uncompiled sources, and unsupported claims. Error capture is also part of the contract, with `wp3-compile-source.json` recording an `io_error` when `research-session.json` is missing, so failed pipeline steps remain machine-readable alongside successful evidence artifacts [docs/evidence/wiki-parity-2026-06/wp3-health.json:3-16] [docs/evidence/wiki-parity-2026-06/wp3-audit.json:1-100] .

