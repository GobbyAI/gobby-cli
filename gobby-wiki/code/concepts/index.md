---
title: Curated Concept Navigation
type: code_concept_tree
provenance:
- file: crates/gcode/contract/gcode.contract.json
- file: crates/gcode/src/commands/codewiki/prompts.rs
- file: crates/gcode/src/commands/codewiki/types.rs
- file: crates/gcode/src/config/services.rs
- file: crates/gcode/src/db/resolution.rs
- file: crates/gcode/src/index/semantic.rs
- file: crates/gcode/src/models.rs
- file: crates/gcore/assets/docker-compose.services.yml
- file: crates/gcore/src/ai_context.rs
- file: crates/ghook/schemas/diagnose-output.v2.schema.json
- file: crates/gwiki/contract/gwiki.contract.json
- file: crates/gwiki/src/benchmark.rs
- file: crates/gwiki/src/graph/mod.rs
- file: crates/gwiki/src/health.rs
- file: crates/gwiki/src/ingest/audio.rs
- file: crates/gwiki/src/ingest/mod.rs
- file: crates/gwiki/src/search/semantic.rs
- file: crates/gwiki/src/vector.rs
- file: docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json
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
provenance_truncated: 461
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/contract/gcode.contract.json](crates/gcode/contract/gcode.contract.json)
- [crates/gcode/src/commands/codewiki/prompts.rs](crates/gcode/src/commands/codewiki/prompts.rs)
- [crates/gcode/src/commands/codewiki/types.rs](crates/gcode/src/commands/codewiki/types.rs)
- [crates/gcode/src/config/services.rs](crates/gcode/src/config/services.rs)
- [crates/gcode/src/db/resolution.rs](crates/gcode/src/db/resolution.rs)
- [crates/gcode/src/index/semantic.rs](crates/gcode/src/index/semantic.rs)
- [crates/gcode/src/models.rs](crates/gcode/src/models.rs)
- [crates/gcore/assets/docker-compose.services.yml](crates/gcore/assets/docker-compose.services.yml)
- [crates/gcore/src/ai_context.rs](crates/gcore/src/ai_context.rs)
- [crates/ghook/schemas/diagnose-output.v2.schema.json](crates/ghook/schemas/diagnose-output.v2.schema.json)
- [crates/gwiki/contract/gwiki.contract.json](crates/gwiki/contract/gwiki.contract.json)
- [crates/gwiki/src/benchmark.rs](crates/gwiki/src/benchmark.rs)

_479 more source files omitted._

</details>

# Curated Concept Navigation

Reader-first paths into the grounded code reference.

## Start here — guided tour

New to this codebase? Begin with [[code/narrative/introduction|System Orientation]].

1. [[code/narrative/introduction|System Orientation]]
2. [[code/narrative/architecture|Architecture]]
3. [[code/narrative/data-flow|Data Flow]]
4. [[code/narrative/cli-runtime-foundation|CLI Runtime Foundation]]
5. [[code/narrative/building-the-code-index|Building the Code Index]]
6. [[code/narrative/resolving-relationships|Resolving Relationships]]
7. [[code/narrative/projecting-graph-and-vectors|Projecting Graph and Vectors]]

Ask questions across this vault with `gwiki ask "..."`, or find pages with `gwiki search "..."`.

## Concept Tree

### Foundations

The workspace, shared services, contract surface, configuration, and database setup that every higher-level workflow relies on.

- [[code/concepts/workspace-map|Workspace Map]] - Start with the workspace-level view: the crates divide responsibilities between shared core services, code indexing, hook intake, and wiki tooling.
- [[code/concepts/shared-service-substrate|Shared Service Substrate]] - Ground the system in the shared core layer that provides AI routing, configuration, provisioning, storage adapters, search primitives, and local service assets.
- [[code/concepts/cli-contracts-and-dispatch|CLI Contracts and Dispatch]] - Understand how gcode exposes a versioned command contract, parses commands, selects early dispatch paths, and keeps CLI leaves aligned with documented command metadata.
- [[code/concepts/configuration-and-postgresql-setup|Configuration and PostgreSQL Setup]] - Follow how project context, service configuration, hub database resolution, and standalone PostgreSQL schema setup give commands a consistent runtime base.

### Code Intelligence Index

The indexing, resolution, projection, vector, and retrieval layers that turn source files into searchable and navigable code knowledge.

- [[code/concepts/file-discovery-and-indexing|File Discovery and Indexing]] - See how gcode discovers project files, classifies them, parses indexable code, writes code facts, and handles freshness or overlay state.
- [[code/concepts/import-and-call-resolution|Import and Call Resolution]] - Explore the language-aware layer that turns imports and call sites into local or external relationships for later search, graph, and documentation use.
- [[code/concepts/graph-projection-and-reports|Graph Projection and Reports]] - Trace how indexed facts are projected into FalkorDB, queried as graph payloads or relationships, cleaned up through projection sync, and summarized into project reports.
- [[code/concepts/vector-symbol-search|Vector Symbol Search]] - Follow the semantic symbol path from indexed symbols to embedding text, Qdrant payloads, vector lifecycle operations, and semantic search results.
- [[code/concepts/hybrid-search-and-lookup-commands|Hybrid Search and Lookup Commands]] - Connect indexed content, PostgreSQL BM25 search, graph boosting, reciprocal rank fusion, grep matching, symbol lookup, and user-facing search commands.

### Grounded Documentation

The CodeWiki generation, curated navigation, and repository-insight layers that build human-readable documentation from the indexed reference.

- [[code/concepts/codewiki-generation-pipeline|CodeWiki Generation Pipeline]] - Learn how CodeWiki gathers indexed facts, graph relationships, source excerpts, AI prompts, verification, rendering, and persistence into grounded documentation pages.
- [[code/concepts/curated-navigation-builder|Curated Navigation Builder]] - Focus on the layer that plans concept modules, sections, and narrative pages, then renders grounded concept and tour documentation on top of the reference wiki.
- [[code/concepts/repository-insight-pages|Repository Insight Pages]] - Round out the documentation surface with ownership, audits, feature catalogs, onboarding, architecture, hotspots, and infrastructure pages built from indexed and repository metadata.

