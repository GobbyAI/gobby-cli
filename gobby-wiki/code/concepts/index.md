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

New to this codebase? Begin with [[code/narrative/01-introduction|Introduction: The Gobby Code Intelligence Workspace]].

1. [[code/narrative/01-introduction|Introduction: The Gobby Code Intelligence Workspace]]
2. [[code/narrative/02-architecture|Architecture]]
3. [[code/narrative/03-data-flow|Data Flow]]
4. [[code/narrative/04-foundations-config-and-services|Foundations: Configuration, Connectivity, and Services]]
5. [[code/narrative/05-indexing-pipeline|Turning Source Files into Code Facts]]
6. [[code/narrative/06-graph-and-vector-stores|Projecting Facts into the Graph and Vector Stores]]
7. [[code/narrative/07-search-and-retrieval|Searching the Index: Lexical, Semantic, and Graph-Boosted]]

Ask questions across this vault with `gwiki ask "..."`, or find pages with `gwiki search "..."`.

## Concept Tree

### Foundations

The shared platform primitives, service infrastructure, and configuration layers every subsystem builds on.

- [[code/concepts/crates|Workspace Topology]] - The four-crate Rust workspace and how code intelligence, shared primitives, hook dispatch, and the wiki engine are partitioned with explicit dependency boundaries.
- [[code/concepts/crates-gcore|Shared Platform Primitives]] - The gcore foundation that every higher crate depends on: AI capability routing, Postgres/Qdrant/FalkorDB connectivity, configuration resolution, hub identity, graph analytics, and shared error types.
- [[code/concepts/crates-gcore-assets|Service Infrastructure]] - Docker Compose definitions and build artifacts for the backing services (PostgreSQL with pg_search, Qdrant, FalkorDB) the platform provisions and health-checks.
- [[code/concepts/crates-gcode-src-config|Configuration & Database Access]] - Layered configuration resolution (env → Postgres hub → standalone files), secret interpolation, runtime context building, and the validated Postgres connection and query layer.
- [[code/concepts/crates-gcode-src-setup|Schema Provisioning]] - Standalone setup that validates, resets, and creates the code-index PostgreSQL schema with redacted-secret safety and compatibility checks.

### Indexing & Resolution

How source files become structured code facts: discovery, parsing, call extraction, and cross-language import resolution.

- [[code/concepts/crates-gcode-src-index|Code Indexing Pipeline]] - File discovery, language classification, tree-sitter parsing, fact extraction, and transactional persistence of symbols, imports, calls, and content chunks.
- [[code/concepts/crates-gcode-src-index-parser|Call Extraction]] - AST-guided and textual call-site discovery, syntax-kind classification, local-binding shadowing checks, and materialization of call relations across many languages.
- [[code/concepts/crates-gcode-src-index-import-resolution|Import Resolution]] - Cross-language engine that turns raw import statements into candidate files, classifying local versus external dependencies across more than a dozen ecosystems.
- [[code/concepts/crates-gcode-assets|Dependency Root Catalog]] - Static language-specific lookup tables mapping package and require paths back to their canonical root modules for polyglot import analysis.

### Stores & Retrieval

The graph and vector projections of indexed data and the search strategies that query them.

- [[code/concepts/crates-gcode-src-graph|Code Graph Engine]] - Building, reading, writing, and managing the FalkorDB code-knowledge graph: typed Cypher serialization, batched mutations, scoped deletions, and traversal reads.
- [[code/concepts/crates-gcode-src-graph-report|Graph Analytics & Reporting]] - Degree-based hotspot rankings, bridge-edge hypotheses, dependency frequencies, and Markdown report generation over the project code graph.
- [[code/concepts/crates-gcode-src-vector|Vector Search & Embeddings]] - The Qdrant-backed vector pipeline: text embedding via daemon or direct routes, collection lifecycle management, and scored semantic search over code symbols.

