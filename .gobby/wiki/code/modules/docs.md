---
title: docs
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

# docs

Parent: [[code/repo|Repository Overview]]

## Overview

The docs module is currently a container rather than an implementation-bearing package: it has no direct files, and its documented responsibility is expressed through child documentation artifacts. Its active child path, docs/evidence, is likewise a parent for generated evidence bundles, with the current docs/evidence/wiki-parity-2026-06 bundle preserving the 2026-06 wiki-parity workstream for the wp3 scope [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12].

The key flow captured under this module is audit evidence collection across wiki-parity operations. The evidence bundle records outputs from gwiki and ghook flows spanning compilation, ingestion, search, and ask behavior, so the docs tree functions as a traceable documentation and verification surface rather than runtime code [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12] [docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16] [docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json:3-10].

The collaboration model is simple: docs delegates all current responsibility to docs/evidence, and docs/evidence organizes timestamped or workstream-specific bundles beneath it. Those bundles carry structured records with shared fields such as command, status, source paths, search results, synthesis, citation checks, and warnings, allowing compile, search, and ask outputs to be inspected together as an auditable chain for the wiki-parity scope [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12] [docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16] [docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json:3-10].

## Child Modules

- [[code/modules/docs/evidence|docs/evidence]] - The docs/evidence module has no direct files of its own; it serves as the parent container for generated evidence bundles. Its current child, docs/evidence/wiki-parity-2026-06, captures the 2026-06 wiki-parity workstream for the wp3 scope, preserving auditable outputs from gwiki and ghook flows across compilation, ingestion, search, and ask operations [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12] [docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16] [docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json:3-10].

The key flow begins with compile records that retain AI synthesis metadata, prompts, article and index paths, and page writes, then ingestion records bind markdown source notes to raw paths, content hashes, and indexed totals. Search records add query metadata, degradation state, ranked results, snippets, scores, source paths, wiki pages, and code citations, while ask records capture route status, cited evidence, ranked hits, final synthesis, citation checks, truncation, and warnings [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12] [docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16] [docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json:3-10].

Together these generated JSON artifacts collaborate as a traceable evidence ledger: compile outputs describe what was written, ingestion outputs describe what source material entered the index, search outputs explain how evidence was retrieved and ranked, and ask outputs show how the retrieved evidence was used and checked in final answers. The parent module’s responsibility is therefore organizational rather than executable, grouping the evidence bundle so downstream reviewers can audit wiki parity behavior from source capture through synthesis.

