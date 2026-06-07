# Gwiki Parity+ Strategy Plan

**Plan ID:** gwiki-parity-plus
**Plan kind:** strategy
**Root epic:** #513 (`Gwiki Parity+ Roadmap`)
**Registration task:** #514 (`Register Gwiki Parity+ strategy plan`)

## O1: Objective
`kind: framing`

Gwiki Parity+ makes `gwiki` an agent-native knowledge system, not only a Markdown vault with search. The roadmap layers
stable contracts, optional/degradable datastores, provenance, trust state, canonical Markdown storage, derived graph and
report artifacts, compact context packs, and benchmark signals over the existing `gwiki` foundation.

Markdown remains canonical. PostgreSQL remains the core store. Qdrant, FalkorDB, embedding/model providers, browser
surfaces, and multimodal providers are optional runtime capabilities that must degrade explicitly. Derived JSON, HTML,
graph, report, and context-pack artifacts must be reproducible from canonical Markdown plus indexed provenance.

The daemon/MCP follow-up is tracked separately. This strategy may reference that integration boundary, but it must not
create a duplicate `gobby-cli` task for daemon or MCP implementation.

## C1: Common Rules
`kind: framing`

- Agent-facing JSON stays compact and stable. Breaking shape changes require explicit versioning or compatibility.
- Every query/read/context/report surface carries source, freshness, trust, audit, and degradation state where applicable.
- Trust and audit are explicit state, not prose. Reports may summarize them, but the machine-readable outputs own the
  source of truth.
- No silent librarian rewrites. Autonomous flows may propose tasks or patches, mark stale state, and record audit data;
  canonical content changes require an accepted action.
- Optional stores and providers must fail closed into degraded output, never fake graph, semantic, model, or citation data.
- Planning leaves must become implementation-ready plan artifacts before code tasks are expanded from them.

## R1: Dependency Order
`kind: framing`

1. Draft and validate this strategy plan.
2. Add graph export artifacts.
3. Add analytics over exported graph data.
4. Build graph context packs from export plus analytics.
5. Stabilize compact contracts for `search`, `read`, `trust`, `audit`, and `graph-context`.
6. Add benchmark reporting after graph export and compact contracts exist.
7. Expand later planning tracks independently into implementation plans.

## P1: Strategy Draft
`kind: framing`

**Goal**: Produce a contract-valid first draft that later agents can register or expand without guessing scope,
dependencies, or roadmap rules.

### 1.1 Register Gwiki Parity+ strategy plan [category: planning]
`kind: deliverable`

Targets: `.gobby/plans/gwiki-parity-plus.md`, `gobby-plans`

Create the tracker-native strategy plan draft for the Gwiki Parity+ roadmap. The first draft must be valid under the
Plan-Coverage Contract and carry enough structure for later agents to register or expand without guessing the dependency
order.

**Acceptance:**

- 1.1.1 - The strategy plan references root epic #513, registration task #514, common rules, dependency order, and the
  draft capability registry. file: `.gobby/plans/gwiki-parity-plus.md`.
- 1.1.2 - The plan uses contract-valid framing and deliverable sections with artifact-backed acceptance criteria. file:
  `.gobby/plans/gwiki-parity-plus.md`.
- 1.1.3 - Plan validation passes for the first draft. test: `gobby-plans.validate_plan .gobby/plans/gwiki-parity-plus.md`.

## P2: Graph And Agent Contracts
`kind: framing`

**Goal**: Add graph artifacts, analytics, agent context packs, compact contracts, and benchmark signals while preserving
explicit degradation for optional stores.

### 2.1 Add gwiki graph export artifacts [category: code] (depends: 1.1)
`kind: deliverable`

Targets: `crates/gwiki/src/graph.rs`, `crates/gwiki/src/commands/graph.rs`, `graph.json`, `graph.html`,
`GRAPH_REPORT.md`

Add export artifacts that render the same seeded wiki graph model as JSON, local HTML, and a Markdown report. The export
must include wiki pages, code/doc/source/citation nodes, links/imports/calls, trust fields, audit fields, and degradation
fields.

**Acceptance:**

- 2.1.1 - Seeded export includes wiki page, code, document, source, and citation nodes. file: `graph.json`.
- 2.1.2 - Seeded export includes links, imports, calls, trust, audit, and degradation fields. file: `graph.json`.
- 2.1.3 - `graph.json`, `graph.html`, and `GRAPH_REPORT.md` are generated from one graph model. file:
  `crates/gwiki/src/graph.rs`.
- 2.1.4 - No-default-features coverage verifies export output and degraded optional stores. test:
  `cargo test -p gobby-wiki --no-default-features graph_export`.

### 2.2 Add gwiki graph analytics [category: code] (depends: 2.1)
`kind: deliverable`

Targets: `crates/gwiki/src/graph.rs`, `crates/gwiki/src/graph/analytics.rs`, `graph.json`, `GRAPH_REPORT.md`

Add graph analytics derived from the exported graph model: communities, centrality, bridge nodes, god nodes, unexpected
links, and hotspots.

**Acceptance:**

- 2.2.1 - Analytics are represented in the JSON graph export. file: `graph.json`.
- 2.2.2 - Analytics are summarized in the Markdown graph report. file: `GRAPH_REPORT.md`.
- 2.2.3 - Communities, centrality, bridge nodes, god nodes, unexpected links, and hotspots are produced from seeded graph
  data. file: `crates/gwiki/src/graph/analytics.rs`.
- 2.2.4 - Seeded tests cover analytics output and degraded optional stores. test:
  `cargo test -p gobby-wiki --no-default-features graph_analytics`.

### 2.3 Add gwiki graph context packs [category: code] (depends: 2.1, 2.2)
`kind: deliverable`

Targets: `crates/gwiki/src/commands/graph_context.rs`, `crates/gwiki/src/graph/context.rs`,
`gwiki graph-context --format json`

Add compact graph context packs for agents. The command must return local neighborhoods plus provenance and warnings
without forcing agents to parse full graph exports.

**Acceptance:**

- 2.3.1 - `gwiki graph-context --format json` includes neighbors, calls, imports, doc links, and citations. file:
  `crates/gwiki/src/graph/context.rs`.
- 2.3.2 - Context packs include stale, audit, and degradation warnings. file: `crates/gwiki/src/graph/context.rs`.
- 2.3.3 - Context packs recommend next files or pages to inspect. file: `crates/gwiki/src/commands/graph_context.rs`.
- 2.3.4 - Seeded tests cover JSON output and degraded optional stores. test:
  `cargo test -p gobby-wiki --no-default-features graph_context`.

### 2.4 Stabilize compact gwiki agent contracts [category: code] (depends: 2.3)
`kind: deliverable`

Targets: `crates/gwiki/contract/gwiki.contract.json`, `docs/contracts/gwiki.md`, `docs/contracts/gwiki-research.md`

Stabilize compact JSON contracts for `search`, `read`, `trust`, `audit`, and `graph-context`. Contract examples and docs
must match behavior and prevent accidental drift.

**Acceptance:**

- 2.4.1 - Compact contract JSON covers `search`, `read`, `trust`, `audit`, and `graph-context`. file:
  `crates/gwiki/contract/gwiki.contract.json`.
- 2.4.2 - Each contract includes trust, freshness, audit, source bundle, and degradation data where applicable. file:
  `crates/gwiki/contract/gwiki.contract.json`.
- 2.4.3 - Docs and examples match implemented behavior. file: `docs/contracts/gwiki.md`.
- 2.4.4 - Contract drift tests pin command output shape. test:
  `cargo test -p gobby-wiki --no-default-features contract`.

### 2.5 Add gwiki benchmark reporting [category: code] (depends: 2.1, 2.4)
`kind: deliverable`

Targets: `crates/gwiki/src/commands/benchmark.rs`, `crates/gwiki/src/benchmark.rs`

Add benchmark reporting for token compression ratio, graph coverage counts, retrieval precision examples, and source mix.
The report must run on a seeded project and degrade when optional stores or providers are unavailable.

**Acceptance:**

- 2.5.1 - Benchmark output includes token compression ratio, graph coverage counts, retrieval precision examples, and
  source mix. file: `crates/gwiki/src/benchmark.rs`.
- 2.5.2 - Benchmark command runs against a seeded project fixture. test:
  `cargo test -p gobby-wiki --no-default-features benchmark_seeded_project`.
- 2.5.3 - Missing optional stores or providers produce explicit degraded benchmark output. file:
  `crates/gwiki/src/commands/benchmark.rs`.
- 2.5.4 - Focused no-default-features tests cover benchmark reporting and degradation behavior. test:
  `cargo test -p gobby-wiki --no-default-features benchmark`.

## P3: Expansion Planning
`kind: framing`

**Goal**: Produce implementation-ready plan artifacts for larger later tracks before expanding them into code work.

### 3.1 Plan engineering architecture pages and diagrams [category: planning]
`kind: deliverable`

Targets: `.gobby/plans/gwiki-architecture-pages.md`

Produce an implementation-ready plan for architecture overview pages, subsystem maps, onboarding paths, diagrams,
ownership and hotspot summaries, and a "what changed since last index" view.

**Acceptance:**

- 3.1.1 - The expansion plan defines architecture overview, subsystem map, onboarding paths, diagrams, ownership and
  hotspot summaries, and changed-since-last-index outputs. file: `.gobby/plans/gwiki-architecture-pages.md`.
- 3.1.2 - The expansion plan identifies data sources, generated artifacts, validation steps, and implementation task
  boundaries. file: `.gobby/plans/gwiki-architecture-pages.md`.

### 3.2 Plan PR and review workflow reports [category: planning]
`kind: deliverable`

Targets: `.gobby/plans/gwiki-pr-review-reports.md`

Produce an implementation-ready plan for review reports covering affected wiki pages, stale docs, changed graph
neighborhoods, and risky dependency shifts.

**Acceptance:**

- 3.2.1 - The expansion plan covers affected wiki pages, stale docs, changed graph neighborhoods, and risky dependency
  shifts. file: `.gobby/plans/gwiki-pr-review-reports.md`.
- 3.2.2 - The expansion plan identifies data sources, generated artifacts, validation steps, and implementation task
  boundaries. file: `.gobby/plans/gwiki-pr-review-reports.md`.

### 3.3 Plan research citation-quality reporting [category: planning]
`kind: deliverable`

Targets: `.gobby/plans/gwiki-citation-quality-reporting.md`

Produce an implementation-ready plan for research reporting around credibility, coverage gaps, contradictions,
stale-source warnings, and confidence per output.

**Acceptance:**

- 3.3.1 - The expansion plan covers credibility, coverage gaps, contradictions, stale-source warnings, and confidence per
  output. file: `.gobby/plans/gwiki-citation-quality-reporting.md`.
- 3.3.2 - The expansion plan identifies data sources, generated artifacts, validation steps, and implementation task
  boundaries. file: `.gobby/plans/gwiki-citation-quality-reporting.md`.

### 3.4 Plan expanded source and multimodal ingestion [category: planning]
`kind: deliverable`

Targets: `.gobby/plans/gwiki-expanded-ingestion.md`

Produce an implementation-ready plan for expanded ingestion: PDFs, URLs, Git documentation repositories, MediaWiki dumps,
datasets, screenshots, diagrams, audio, and video.

**Acceptance:**

- 3.4.1 - The expansion plan covers PDFs, URLs, Git doc repos, MediaWiki dumps, datasets, screenshots, diagrams, audio,
  and video. file: `.gobby/plans/gwiki-expanded-ingestion.md`.
- 3.4.2 - The expansion plan identifies data sources, generated artifacts, validation steps, degradation behavior, and
  implementation task boundaries. file: `.gobby/plans/gwiki-expanded-ingestion.md`.

### 3.5 Plan autonomous librarian workflows [category: planning]
`kind: deliverable`

Targets: `.gobby/plans/gwiki-autonomous-librarian.md`

Produce an implementation-ready plan for librarian workflows that detect stale pages, missing citations, broken links,
weak provenance, outdated codewiki pages, and proposed task or patch generation.

**Acceptance:**

- 3.5.1 - The expansion plan covers stale pages, missing citations, broken links, weak provenance, outdated codewiki
  pages, and proposed task or patch generation. file: `.gobby/plans/gwiki-autonomous-librarian.md`.
- 3.5.2 - The expansion plan preserves the no-silent-rewrites rule and defines audit, review, and validation gates. file:
  `.gobby/plans/gwiki-autonomous-librarian.md`.

### 3.6 Plan change-triggered wiki refresh [category: planning]
`kind: deliverable`

Targets: `.gobby/plans/gwiki-change-triggered-refresh.md`

Produce an implementation-ready plan for affected-page detection after code or documentation changes and
refresh-or-mark-stale behavior.

**Acceptance:**

- 3.6.1 - The expansion plan covers affected-page detection after code and documentation changes. file:
  `.gobby/plans/gwiki-change-triggered-refresh.md`.
- 3.6.2 - The expansion plan covers refresh-or-mark-stale behavior, provenance updates, validation steps, and
  implementation task boundaries. file: `.gobby/plans/gwiki-change-triggered-refresh.md`.

### 3.7 Plan browser graph surface [category: planning]
`kind: deliverable`

Targets: `.gobby/plans/gwiki-browser-graph-surface.md`

Produce an implementation-ready plan for a local HTML-first graph surface, a richer browser app later, graph status
badges, citations, and shareable views.

**Acceptance:**

- 3.7.1 - The expansion plan covers local HTML first, richer browser app later, graph status badges, citations, and
  shareable views. file: `.gobby/plans/gwiki-browser-graph-surface.md`.
- 3.7.2 - The expansion plan identifies data sources, generated artifacts, validation steps, and implementation task
  boundaries. file: `.gobby/plans/gwiki-browser-graph-surface.md`.
