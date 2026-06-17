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

<details>
<summary>Relevant source files</summary>

- [docs/evidence/wiki-parity-2026-06/wp3-audit.json:1-100](docs/evidence/wiki-parity-2026-06/wp3-audit.json#L1-L100)
- [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:3-47](docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json#L3-L47)
- [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-44](docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json#L3-L44)
- [docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:2-3](docs/evidence/wiki-parity-2026-06/wp3-compile-source.json#L2-L3)
- [docs/evidence/wiki-parity-2026-06/wp3-deposit-ingest.json:3-24](docs/evidence/wiki-parity-2026-06/wp3-deposit-ingest.json#L3-L24)
- [docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json:2-90](docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json#L2-L90)
- [docs/evidence/wiki-parity-2026-06/wp3-health.json:3-71](docs/evidence/wiki-parity-2026-06/wp3-health.json#L3-L71)
- [docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json:3-299](docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json#L3-L299)
- [docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-direct.json:3-295](docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-direct.json#L3-L295)
- [docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-search.json:2-113](docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-search.json#L2-L113)
- [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json:3-341](docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json#L3-L341)
- [docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json:2-84](docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json#L2-L84)
- [docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-ask-daemon.json:3-327](docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-ask-daemon.json#L3-L327)
- [docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-search.json:2-78](docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-search.json#L2-L78)
- [docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-ask-daemon.json:3-341](docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-ask-daemon.json#L3-L341)
- [docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-search.json:2-84](docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-search.json#L2-L84)
- [docs/evidence/wiki-parity-2026-06/wp3-search-hybrid.json:3-137](docs/evidence/wiki-parity-2026-06/wp3-search-hybrid.json#L3-L137)
- [docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-227](docs/evidence/wiki-parity-2026-06/wp3-search-sources.json#L3-L227)

</details>

# docs

Parent: [[code/repo|Repository Overview]]

## Overview

The docs module is a parent directory hosting documentation-related tracing and diagnostics, primarily realized through its docs/evidence child module. It coordinates the capturing of structured JSON snapshots from pipeline executions, such as the gwiki and wiki-parity pipelines, serving as a comprehensive audit trail. The module’s main responsibility is to support tracing, post-run analysis, quality control, and diagnostic evaluation of these pipelines.

Key flows within this module involve logging execution artifacts, AI model routes, token estimations, prompt budget allocations, and citation statuses (such as kept or stripped citations) during a pipeline run. It collaborates with external pipeline execution nodes to document pipeline integrity metrics, recording diagnostics like broken links, stale pages, duplicate concepts, and stale citations. This structured telemetry allows developers and automated tools to audit pipeline parity and verify the consistency of the generated wiki output.

### Key Schema Properties and API Symbols

| Property | Component ID | Description |
| --- | --- | --- |
| ai | df826027-066c-58cc-bdbf-f938bfec12ce | Tracks AI route, status, model, and requested mode |
| page_writes | d8125856-3fa8-58c5-ba69-ecbb2da09c7c | Documents page write operations during pipeline execution |
| prompt_token_budget | 90d6af89-c288-5933-9f9b-2c4c2eb6c20c | Monitors prompt token limits allocated for model runs |
| citations_kept | 3e4c955a-d9e7-540c-bfdf-b3c17044ad11 | Traces source citations retained in synthesized pages |
| citations_stripped | f46d2c75-a8de-563a-af83-d37abbe6d19a | Logs citations removed due to filtering or fallback logic |
| broken_links | 350fdfa9-e60e-579c-926b-d59f37e25b07 | Telemetry capturing link validation failures |
| stale_citations | f0aa7938-dd61-5210-be65-f63b47cac8cf | Logs outdated citations during post-run analysis |
| stale_pages | 8f79c7c6-3684-5c47-8936-3973feac23c7 | Tracks wiki pages that need to be recompiled or updated |
| duplicate_concepts | 0bce6fef-a95f-51eb-9f93-524eb6347a1b | Detects and logs duplicate concepts across pipelines |
| synthesis | 227a76a0-b812-5dde-bb55-5c31b5104c9d | Traces AI synthesis output, checked claims, and unsupported claims |
[docs/evidence/wiki-parity-2026-06/wp3-audit.json:1-100]
[docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:2]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:3-12]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12]
[docs/evidence/wiki-parity-2026-06/wp3-deposit-ingest.json:3]

## Dependency Diagram

`degraded: graph-truncated`

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/docs/evidence\|docs/evidence]] | The docs/evidence module serves as the central directory and primary repository for tracing execution artifacts and diagnostic outcomes across project pipeline runs. Although this parent directory contains no direct files, its responsibilities are realized via the docs/evidence/wiki-parity-2026-06 sub-module, which functions as an audit trail for the gwiki and wiki-parity pipelines. This module is responsible for capturing structured JSON snapshots of system executions, facilitating thorough tracing, quality control, and post-run analysis. Key flows managed within this module involve tracking project health metrics—specifically broken links, duplicate concepts, and stale citations [docs/evidence/wiki-parity-2026-06/wp3-health.json:3-16]—as well as logging file ingestion statistics [docs/evidence/wiki-parity-2026-06/wp3-deposit-ingest.json:5-11] and recording reciprocal rank fusion search outcomes [docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16]. Collaboration points focus on error monitoring and verification, capturing critical execution failures and error messages when vital dependencies like research session checkpoints are missing. \| Key Schema Property \| Stable Component ID \| Associated Flow / Context \| Cite Reference \| \| --- \| --- \| --- \| --- \| \| broken_links \| 350fdfa9-e60e-579c-926b-d59f37e25b07 \| Logs broken hyperlinks within system documents \| [docs/evidence/wiki-parity-2026-06/wp3-health.json:3-16] \| \| duplicate_concepts \| 0bce6fef-a95f-51eb-9f93-524eb6347a1b \| Detects redundant conceptual mappings in audits \| [docs/evidence/wiki-parity-2026-06/wp3-health.json:3-16] \| \| stale_citations \| f0aa7938-dd61-5210-be65-f63b47cac8cf \| Monitors outdated or invalid source references \| [docs/evidence/wiki-parity-2026-06/wp3-health.json:3-16] \| \| ingestions \| ce8f50a3-67e5-5703-8836-3f9e959f2344 \| Tracks file uploads and metadata registration \| [docs/evidence/wiki-parity-2026-06/wp3-deposit-ingest.json:5-11] \| \| results \| 27abe5f8-b3ed-5561-950e-e70ec219e749 \| Stores output lists from fusion search runs \| [docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16] \| |
