# Gwiki/Gcode Parity+ Plan

## O1: Objective

`kind: framing`

Make gwiki+gcode an agent-native knowledge system at **parity+ with OpenDeepWiki,
graphify, and LLM-wiki**, rendered through **Obsidian** as the frontend. gcode
generates code-architecture pages and diagrams; gwiki owns one **unified Obsidian
vault** plus indexing, trust, freshness, graph export/analytics, hybrid search, and
grounded Q&A spanning code and knowledge. Markdown stays canonical; PostgreSQL stays
the core store; Qdrant/FalkorDB/embedding+model providers stay optional and degrade
explicitly. A richer standalone browser surface is deferred and out of scope here.

## C1: Common Rules

`kind: framing`

- **Unified Obsidian vault**: gcode codewiki output and gwiki synthesis write into one
  vault using Obsidian-native `[[wikilinks]]`, YAML frontmatter, and ```` ```mermaid ````
  fenced diagrams so Obsidian's graph view, backlinks, and previews work with no custom UI.
- **Producer/consumer split**: gcode **produces** — it indexes code, generates codewiki
  pages into the vault, and writes the code graph. gwiki **consumes** — it is the sole
  query/answer surface (search, `ask`, graph-context, trust, reports) over the unified vault
  and the shared graph. gcode does not add query/answer surfaces over the vault; gwiki does
  not generate code pages. Q&A is a gwiki surface.
- **Reuse, don't duplicate**: extend gcode `codewiki/`, gcode `graph` payload/report,
  and gwiki `exports.rs`/`graph.rs`/trust stack. No parallel export, graph, or vault systems.
- **Strangler-fig migrations**: when consolidating duplicated logic into a shared home
  (e.g. graph analytics into gobby-core), stand the new path up alongside the legacy path,
  prove parity with a test on seeded data, and only cut over + delete the legacy code and
  compatibility shims once parity is green. No big-bang replacement; no dead code left behind.
- Agent-facing JSON stays compact and stable; breaking shape changes bump the contract version.
- Every query/read/context/report surface carries source, freshness, trust, audit, and
  degradation state where applicable. Trust/audit/freshness are explicit machine-readable state.
- **No silent librarian rewrites**: autonomous flows propose tasks/patches and mark stale
  state; canonical content changes require an accepted action.
- Optional stores/providers fail closed into explicit degraded output; never fake graph,
  semantic, model, diagram, or citation data.
- gcore layering preserved: no `reqwest` in always-compiled modules; new graph/analytics
  logic respects the feature-gated `falkor`/`qdrant`/`search` boundaries.
- Non-destructive to the Gobby hub schema; never alter `project.json`, `config_store`,
  or Gobby-managed tables/indexes.
- Daemon/MCP follow-up tracked separately; this plan must not create a duplicate
  `gobby-cli` task for daemon/MCP implementation.

## R1: Dependency Order

`kind: framing`

1. **P1 Graph & Vault Foundation** — unified vault contract + graph export/analytics/
   context + agent contract + benchmark.
2. **P2 Architecture Pages & Diagrams** — depends on P1 (consumes graph + vault contract).
3. **P3 Grounded Code Q&A** — depends on P1, P2 (Q&A cites pages + graph context).
4. **P4 Freshness, Librarian & Reports** — depends on P1–P3.

## P1: Graph & Vault Foundation

`kind: framing`

**Goal**: One Obsidian-native vault shared by gcode + gwiki, with reproducible graph
export, **shared graph analytics in gobby-core** (with gcode's existing hotspot/bridge
logic migrated onto it via parity-gated strangler-fig cutover), compact graph-context
packs for agents, a stabilized agent contract, and a benchmark surface — all degrading
explicitly when optional stores are off.

### 1.1 Define the unified Obsidian vault contract [category: code]

`kind: deliverable`

Targets: `crates/gwiki/src/vault.rs`, `crates/gwiki/src/frontmatter.rs`, `crates/gwiki/src/links.rs`, `crates/gcode/src/commands/codewiki/io.rs`, `crates/gcode/src/commands/codewiki/paths.rs`, `crates/gcode/src/commands/codewiki/render.rs`

Establish one vault layout and frontmatter/link convention so gcode-generated code pages
and gwiki-synthesized knowledge pages live in the same Obsidian vault and form one graph.

Reuse `gwiki::frontmatter::WikiFrontmatter` / `parse_frontmatter` and `gwiki::links`
(`extract_links`, `parse_wikilink`) as the canonical schema. gcode codewiki adopts the
same frontmatter keys (provenance, source, trust, freshness) and emits Obsidian
`[[wikilinks]]` (not relative `.md` links) so gwiki backlinks/graph resolve code pages.

- Vault layout: a `code/` subtree for code-derived pages, a `knowledge/` subtree for
  synthesized pages, shared `_meta/`. gcode `--out` resolves to the gwiki vault root.
- Frontmatter: shared required keys (`source`, `provenance`, `generated_by`,
  `trust`, `freshness`/`indexed_at`). gcode pages set `generated_by: gcode-codewiki`.
- Links: gcode codewiki cross-references emit `[[code/<module>/<symbol>]]` wikilinks.

**Acceptance:**

- 1.1.1 - A shared vault-layout + frontmatter contract is documented and consumed by both crates. file: `crates/gwiki/src/vault.rs`.
- 1.1.2 - gcode codewiki emits Obsidian `[[wikilinks]]` and gwiki-compatible frontmatter keys. file: `crates/gcode/src/commands/codewiki/render.rs`.
- 1.1.3 - gwiki indexing resolves gcode-generated pages into the link graph (backlinks/related-paths see code pages). symbol: `gobby_wiki::links::extract_links`.
- 1.1.4 - Round-trip test: a gcode codewiki page placed in the vault is indexed and backlinked by gwiki. test: `cargo test -p gobby-wiki --no-default-features unified_vault`.

### 1.2 Extend gwiki graph export artifacts [category: code] (depends: 1.1)

`kind: deliverable`

Targets: `crates/gwiki/src/graph.rs`, `crates/gwiki/src/exports.rs`, `crates/gwiki/src/commands/graph.rs`, `crates/gwiki/src/main.rs`, `graph.json`, `GRAPH_REPORT.md`

Add a `graph` subcommand that exports the unified graph as `graph.json` and `GRAPH_REPORT.md`,
reproducible from canonical Markdown + indexed provenance. Reuse `WikiGraphFacts` /
`MemoryWikiGraph` (`graph.rs`) as the model and the `ExportKind` / `ExportArtifact` /
`write_export` machinery (`exports.rs`); do not build a parallel export path. No standalone
`graph.html` — Obsidian's graph view + an embedded mermaid index in `GRAPH_REPORT.md` is the
render surface (custom browser deferred).

**Acceptance:**

- 1.2.1 - Seeded export includes wiki page, code, document, source, and citation nodes. file: `crates/gwiki/src/commands/graph.rs`.
- 1.2.2 - Export includes links, imports, calls, trust, audit, and degradation fields, built from the `graph.rs` model. file: `crates/gwiki/src/graph.rs`.
- 1.2.3 - `graph.json` and `GRAPH_REPORT.md` (with an embedded mermaid overview) are produced from one model via the `exports.rs` artifact path. file: `crates/gwiki/src/exports.rs`.
- 1.2.4 - No-default-features coverage verifies export output and degraded optional stores. test: `cargo test -p gobby-wiki --no-default-features graph_export`.

### 1.3 Add a shared graph-analytics module in gobby-core [category: code]

`kind: deliverable`

Targets: `crates/gcore/src/graph_analytics.rs`, `crates/gcore/src/lib.rs`, `crates/gcore/Cargo.toml`

Add a feature-gated `graph-analytics` module to gobby-core that is the single home for
graphify-style measures, consumed by both gwiki and gcode. Keep gcore dependency-light:
implement pure algorithms over an in-memory graph; if a graph library is used it stays
behind the new `graph-analytics` feature, and the module pulls **no** datastore/`reqwest`
deps (respects the gcore always-compiled vs feature-gated layering).

Neutral, transport-free types so any caller can convert into them:

```rust
pub struct AnalyticsNode { pub id: String, pub kind: String, pub weight: f64 }
pub struct AnalyticsEdge { pub source: String, pub target: String, pub kind: String }
pub struct AnalyticsGraph { pub nodes: Vec<AnalyticsNode>, pub edges: Vec<AnalyticsEdge> }

pub struct GraphAnalytics {
    pub communities: Vec<Community>,
    pub centrality: Vec<CentralityScore>,
    pub bridges: Vec<NodeRef>,
    pub god_nodes: Vec<NodeRef>,
    pub unexpected_links: Vec<EdgeRef>,
    pub hotspots: Vec<Hotspot>,
}

pub fn analyze(graph: &AnalyticsGraph) -> GraphAnalytics { /* communities, centrality,
    articulation-point bridges, high-degree god nodes, cross-community unexpected links,
    frequency hotspots */ }
```

**Acceptance:**

- 1.3.1 - gobby-core exposes a `graph-analytics` feature and module with neutral `AnalyticsGraph` input and `GraphAnalytics` output. file: `crates/gcore/src/graph_analytics.rs`.
- 1.3.2 - `analyze` computes communities, centrality, bridge nodes, god nodes, unexpected links, and hotspots with no datastore/`reqwest` deps in the module. symbol: `gobby_core::graph_analytics::analyze`.
- 1.3.3 - Heavy graph deps (if any) are gated behind the `graph-analytics` feature so small binaries do not inherit them. file: `crates/gcore/Cargo.toml`.
- 1.3.4 - Unit tests cover each measure on a fixed seeded graph. test: `cargo test -p gobby-core --features graph-analytics graph_analytics`.

### 1.4 Consume gobby-core analytics in gwiki graph export [category: code] (depends: 1.2, 1.3)

`kind: deliverable`

Targets: `crates/gwiki/src/graph.rs`, `crates/gwiki/src/graph/analytics.rs`, `crates/gwiki/Cargo.toml`, `graph.json`, `GRAPH_REPORT.md`

gwiki has no prior analytics, so it consumes gobby-core directly (no strangler needed).
Convert `WikiGraphFacts` / `MemoryWikiGraph` into `gobby_core::graph_analytics::AnalyticsGraph`,
call `analyze`, and surface results in `graph.json` + `GRAPH_REPORT.md`. (`graph.rs` becomes
`graph/mod.rs` with an `analytics` sibling.) Enable the gobby-core `graph-analytics` feature.

**Acceptance:**

- 1.4.1 - gwiki converts its graph model to `AnalyticsGraph` and computes analytics via gobby-core. file: `crates/gwiki/src/graph/analytics.rs`.
- 1.4.2 - Analytics appear in `graph.json` and are summarized in `GRAPH_REPORT.md`. file: `graph.json`.
- 1.4.3 - gwiki enables the gobby-core `graph-analytics` feature. file: `crates/gwiki/Cargo.toml`.
- 1.4.4 - Seeded tests cover analytics output and degraded optional stores. test: `cargo test -p gobby-wiki --no-default-features graph_analytics`.

### 1.5 Add gcode→gobby-core analytics adapter with parity verification [category: code] (depends: 1.3)

`kind: deliverable`

Targets: `crates/gcode/src/graph/code_graph/payload.rs`, `crates/gcode/src/graph/report/summary.rs`, `crates/gcode/src/graph/report/tests.rs`, `crates/gcode/Cargo.toml`

Strangler-fig step 1 — stand the new path up beside the legacy one. gcode `graph/report/`
already computes hotspots (`GraphReportHotspots`) and bridges (`BridgeReportSummary`) over a
loaded snapshot. Add an adapter mapping `GraphPayload` / the report snapshot into
`AnalyticsGraph`, compute via `gobby_core::graph_analytics::analyze`, and add a **parity
test** asserting gcore output equals the legacy hotspots + bridge summary on a seeded
snapshot. The legacy `graph/report` computation stays the live source of truth in this
deliverable; both paths coexist. Enable the gobby-core `graph-analytics` feature.

**Acceptance:**

- 1.5.1 - A gcode adapter maps `GraphPayload` / the report snapshot to `gobby_core::graph_analytics::AnalyticsGraph`. file: `crates/gcode/src/graph/code_graph/payload.rs`.
- 1.5.2 - The legacy `GraphReportHotspots` + `BridgeReportSummary` path remains the live output; the gobby-core path runs alongside it. file: `crates/gcode/src/graph/report/summary.rs`.
- 1.5.3 - gcode enables the gobby-core `graph-analytics` feature. file: `crates/gcode/Cargo.toml`.
- 1.5.4 - A parity test asserts gobby-core analytics equal legacy hotspots + bridges on a seeded snapshot. test: `cargo test -p gobby-code --no-default-features graph_analytics_parity`.

### 1.6 Cut gcode over to gobby-core analytics and remove legacy code [category: refactor] (depends: 1.5)

`kind: deliverable`

Targets: `crates/gcode/src/graph/report/summary.rs`, `crates/gcode/src/graph/report/generation.rs`, `crates/gcode/src/graph/report/types.rs`, `crates/gcode/src/graph/report/tests.rs`

Strangler-fig step 2 — only after 1.5's parity test is green. Make `graph/report` compute
hotspots + bridges via `gobby_core::graph_analytics` and delete the now-dead legacy
computation and any compatibility shims (report loading/queries/rendering that fetch and
present the graph stay). Output shape is unchanged — the parity test (now asserting the
gcore-only path matches the previously-pinned output) guards against regression.

**Acceptance:**

- 1.6.1 - `graph/report` computes hotspots and bridges via gobby-core; the duplicated legacy computation is removed. file: `crates/gcode/src/graph/report/summary.rs`.
- 1.6.2 - No compatibility shim or dead analytics code remains in the report module. file: `crates/gcode/src/graph/report/generation.rs`.
- 1.6.3 - `gcode graph report` output shape is unchanged after cutover. behavior: "graph report hotspots and bridge summary match pre-cutover output" in `crates/gcode/src/graph/report/types.rs`.
- 1.6.4 - The parity/characterization test passes against the gcore-only path. test: `cargo test -p gobby-code --no-default-features graph_report`.

### 1.7 Add gwiki graph context packs [category: code] (depends: 1.4)

`kind: deliverable`

Targets: `crates/gwiki/src/graph/context.rs`, `crates/gwiki/src/commands/graph_context.rs`, `crates/gwiki/src/main.rs`

Add a `graph-context` subcommand returning compact local neighborhoods plus provenance and
warnings, so agents do not parse full graph exports. Wire the new subcommand into `main.rs`.

**Acceptance:**

- 1.7.1 - `gwiki graph-context --format json` includes neighbors, calls, imports, doc links, and citations. file: `crates/gwiki/src/graph/context.rs`.
- 1.7.2 - Context packs include stale, audit, and degradation warnings. file: `crates/gwiki/src/graph/context.rs`.
- 1.7.3 - Context packs recommend next files or pages to inspect, and the subcommand is registered. file: `crates/gwiki/src/commands/graph_context.rs`.
- 1.7.4 - Seeded tests cover JSON output and degraded optional stores. test: `cargo test -p gobby-wiki --no-default-features graph_context`.

### 1.8 Add graph-context to the gwiki agent contract [category: code] (depends: 1.7)

`kind: deliverable`

Targets: `crates/gwiki/src/contract.rs`, `crates/gwiki/contract/gwiki.contract.json`, `crates/gwiki/tests/cli_contract.rs`, `docs/contracts/gwiki-cli.md`

`search`/`read`/`trust`/`audit` already exist in the code-built contract (`contract.rs`) and
pinned JSON (`contract_version: 1`); `cli_contract.rs` already drift-tests builder == JSON.
Add the `graph-context` command to the builder, re-pin `gwiki.contract.json`, bump
`contract_version`, extend the drift test, and document it in `gwiki-cli.md` (the real file —
the old plan's `docs/contracts/gwiki.md` does not exist).

**Acceptance:**

- 1.8.1 - `graph-context` is added to the contract builder and pinned JSON. file: `crates/gwiki/src/contract.rs`.
- 1.8.2 - Pinned contract bumps `contract_version`; the `graph-context` entry carries trust, freshness, audit, source-bundle, and degradation fields. file: `crates/gwiki/contract/gwiki.contract.json`.
- 1.8.3 - `docs/contracts/gwiki-cli.md` documents `graph-context` and matches behavior. file: `docs/contracts/gwiki-cli.md`.
- 1.8.4 - Drift test asserts builder == pinned JSON and `gwiki contract --format json` match for the new shape. test: `cargo test -p gobby-wiki --no-default-features --test cli_contract`.

### 1.9 Add gwiki benchmark reporting [category: code] (depends: 1.2)

`kind: deliverable`

Targets: `crates/gwiki/src/benchmark.rs`, `crates/gwiki/src/commands/benchmark.rs`, `crates/gwiki/src/main.rs`

Add a `benchmark` subcommand reporting token-compression ratio, graph-coverage counts,
retrieval-precision examples, and source mix on a seeded project; degrade explicitly when
optional stores/providers are unavailable. Reuse the seeded-fixture pattern from
`crates/gwiki/tests/common` + `crates/gwiki/tests/cli_smoke`.

**Acceptance:**

- 1.9.1 - Benchmark output includes token-compression ratio, graph-coverage counts, retrieval-precision examples, and source mix. file: `crates/gwiki/src/benchmark.rs`.
- 1.9.2 - The benchmark subcommand runs against a seeded project fixture and is registered. file: `crates/gwiki/src/commands/benchmark.rs`.
- 1.9.3 - Missing optional stores/providers produce explicit degraded benchmark output. file: `crates/gwiki/src/commands/benchmark.rs`.
- 1.9.4 - Focused no-default-features tests cover benchmark reporting and degradation. test: `cargo test -p gobby-wiki --no-default-features benchmark`.

## P2: Architecture Pages & Diagrams

`kind: framing`

**Goal**: DeepWiki-parity code-architecture pages in the unified Obsidian vault. Extend the
gcode `codewiki` command (which already emits file/module/repo docs with mermaid + AI
summaries) to also generate an architecture overview + subsystem map, onboarding paths,
ownership + hotspot pages, and a "what changed since last index" view. Every new page writes
through the P1.1 unified-vault contract (Obsidian `[[wikilinks]]` + gwiki-indexable
frontmatter) and through the existing incremental writer (`write_incremental_doc_set` /
`CodewikiMeta`), so gwiki indexes, searches, and trust-tracks them with no extra wiring.
Reuse: `cluster.rs` (subsystem grouping), `render_module_dependency_mermaid` /
`render_module_call_mermaid` (mermaid), `prompts::*` with `structural_*_summary` fallbacks,
and `gobby_core::graph_analytics` (P1.3) for centrality/hotspots/bridges.

### 2.1 Add architecture overview + subsystem map page [category: code] (depends: P1)

`kind: deliverable`

Targets: `crates/gcode/src/commands/codewiki/build.rs`, `crates/gcode/src/commands/codewiki/render.rs`, `crates/gcode/src/commands/codewiki/cluster.rs`, `crates/gcode/src/commands/codewiki/prompts.rs`, `crates/gcode/src/commands/codewiki/mod.rs`

Generate a top-level architecture overview page (`code/_architecture.md`) that names the
repo's subsystems (from `cluster.rs` clustering), describes each subsystem's responsibility
(AI summary via a new `prompts::architecture_prompt`, with `structural_module_summary`
fallback), and renders a repo-level **subsystem mermaid** diagram of cross-cluster
dependencies (bounded by the existing `--edge-limit`). Reuse `cluster_file_modules` /
`common_module_for_files` for grouping and the `render_module_dependency_mermaid` /
`mermaid_node_id` / `mermaid_label` helpers for the diagram. Cross-link every subsystem to its
module doc via `module_wikilink`.

**Acceptance:**

- 2.1.1 - An architecture overview page is generated naming subsystems derived from `cluster.rs`. file: `crates/gcode/src/commands/codewiki/build.rs`.
- 2.1.2 - The page renders a bounded repo-level subsystem mermaid diagram of cross-cluster dependencies. file: `crates/gcode/src/commands/codewiki/render.rs`.
- 2.1.3 - Each subsystem links to its module doc via Obsidian `[[wikilinks]]` and carries gwiki-indexable frontmatter (per P1.1). symbol: `gobby_code::commands::codewiki::module_wikilink`.
- 2.1.4 - No-default-features test covers the overview page + diagram bounding + structural fallback. test: `cargo test -p gobby-code --no-default-features codewiki_architecture`.

### 2.2 Add onboarding-path generation [category: code] (depends: 2.1)

`kind: deliverable`

Targets: `crates/gcode/src/commands/codewiki/build.rs`, `crates/gcode/src/commands/codewiki/prompts.rs`, `crates/gcode/src/commands/codewiki/render.rs`

Generate an onboarding page (`code/_onboarding.md`): detect entry points (`main.rs` / `lib.rs`
/ exported public API symbols), then produce a recommended "start here" reading order by
ranking modules with `gobby_core::graph_analytics` centrality (P1.3) over the module
dependency graph, breaking ties by dependency topology. Each step links to the relevant module
or file doc. Degrade to a structural entry-point list when graph analytics are unavailable.

**Acceptance:**

- 2.2.1 - The onboarding page lists detected entry points (`main.rs`/`lib.rs`/public API). file: `crates/gcode/src/commands/codewiki/build.rs`.
- 2.2.2 - A reading order is derived from `gobby_core::graph_analytics` centrality over the module graph. symbol: `gobby_core::graph_analytics::analyze`.
- 2.2.3 - Steps link to module/file docs via wikilinks; the page degrades to a structural list without graph analytics. file: `crates/gcode/src/commands/codewiki/render.rs`.
- 2.2.4 - No-default-features test covers ordering and the degraded path. test: `cargo test -p gobby-code --no-default-features codewiki_onboarding`.

### 2.3 Add hotspot page [category: code] (depends: 2.1)

`kind: deliverable`

Targets: `crates/gcode/src/commands/codewiki/build.rs`, `crates/gcode/src/commands/codewiki/render.rs`, `crates/gcode/src/commands/codewiki/mod.rs`

Generate a hotspots page (`code/_hotspots.md`) surfacing `gobby_core::graph_analytics`
hotspots, god nodes, and bridges (from P1) as a wiki page with Obsidian `[[wikilinks]]` to the
implicated symbols/files and gwiki-indexable frontmatter (per P1.1). Degrade to an explicit
"analytics unavailable" note when graph analytics cannot be computed.

**Acceptance:**

- 2.3.1 - A hotspots page surfaces hotspots, god nodes, and bridges from `gobby_core::graph_analytics` with wikilinks. file: `crates/gcode/src/commands/codewiki/build.rs`.
- 2.3.2 - The page carries gwiki-indexable frontmatter and wikilinks per P1.1. file: `crates/gcode/src/commands/codewiki/render.rs`.
- 2.3.3 - The page degrades to an explicit "analytics unavailable" note when analytics are off. file: `crates/gcode/src/commands/codewiki/build.rs`.
- 2.3.4 - No-default-features test covers the page and the degraded path. test: `cargo test -p gobby-code --no-default-features codewiki_hotspots`.

### 2.4 Add ownership page from CODEOWNERS + git blame [category: code] (depends: 2.1)

`kind: deliverable`

Targets: `crates/gcode/src/commands/codewiki/ownership.rs`, `crates/gcode/src/commands/codewiki/build.rs`, `crates/gcode/src/commands/codewiki/io.rs`, `crates/gcode/src/commands/codewiki/mod.rs`, `crates/gcode/Cargo.toml`

Generate an ownership page (`code/_ownership.md`) from two sources in a new `ownership.rs`
module:

- **Declared** owners from a repo `CODEOWNERS` file (when present), mapped to modules/files.
- **Derived** owners from **git blame** — top committers per file, aggregated to module level,
  using `gix` (gitoxide; pure-Rust, no system libgit2). Add `gix` as a gcode dependency.

Merge declared + derived (declared precedence; derived fills gaps and adds a "top contributors"
list). Blame is expensive, so cache per-file blame summaries keyed by file content hash in
`_meta/ownership.json` (reuse the `io.rs` meta read/write pattern), bounded by a file cap; mark
ownership **partial** when the cap is hit or blame times out. Degrade explicitly: a non-git
repo (or blame failure) falls back to CODEOWNERS-only; neither source present → "unknown
ownership". Runtime degradation only — no compile-time feature gate (gix is a normal dep, so
`--no-default-features` builds still include it).

**Acceptance:**

- 2.4.1 - Declared owners are parsed from `CODEOWNERS` and mapped to modules/files. file: `crates/gcode/src/commands/codewiki/ownership.rs`.
- 2.4.2 - Derived owners (top committers per file/module) are computed from git blame via `gix`; `gix` is added to gcode. file: `crates/gcode/Cargo.toml`.
- 2.4.3 - Blame summaries are cached by content hash and bounded; hitting the cap or a blame timeout marks ownership "partial". file: `crates/gcode/src/commands/codewiki/io.rs`.
- 2.4.4 - A non-git repo with no `CODEOWNERS` degrades to explicit "unknown ownership" rather than failing. file: `crates/gcode/src/commands/codewiki/ownership.rs`.
- 2.4.5 - Tests cover CODEOWNERS-only, blame-derived (temp git fixture), the merge, and degradation. test: `cargo test -p gobby-code --no-default-features codewiki_ownership`.

### 2.5 Add "what changed since last index" view [category: code] (depends: 2.1)

`kind: deliverable`

Targets: `crates/gcode/src/commands/codewiki/io.rs`, `crates/gcode/src/commands/codewiki/build.rs`, `crates/gcode/src/commands/codewiki/mod.rs`

Extend `CodewikiMeta` to persist an index snapshot (per-file content hashes + symbol counts +
a graph-neighborhood fingerprint) and generate a changes page (`code/_changes.md`) diffing the
current index against the previous snapshot: added/removed/changed files, new/removed symbols,
and changed graph neighborhoods. Reuse `read_codewiki_meta` / `write_codewiki_meta` /
`write_incremental_doc_set`. On first run (no prior snapshot) emit an explicit "baseline" page.

**Acceptance:**

- 2.5.1 - `CodewikiMeta` persists an index snapshot (file hashes, symbol counts, graph fingerprint). file: `crates/gcode/src/commands/codewiki/io.rs`.
- 2.5.2 - A changes page lists added/removed/changed files, new/removed symbols, and changed graph neighborhoods vs the prior snapshot. file: `crates/gcode/src/commands/codewiki/build.rs`.
- 2.5.3 - First run with no prior snapshot emits an explicit baseline page rather than a spurious diff. file: `crates/gcode/src/commands/codewiki/build.rs`.
- 2.5.4 - No-default-features test covers diff output and the baseline case. test: `cargo test -p gobby-code --no-default-features codewiki_changes`.

## P3: Grounded Code Q&A

`kind: framing`

**Goal**: gwiki `ask` is the **sole** Q&A surface — conversational, citation-grounded answers
over the unified vault (code pages from P2) and the **shared code graph**. gcode produces; it
gains no `ask`. The producer side makes the code graph consumable; the consumer side (gwiki
`ask`, graph-context, research loop) grounds answers in code call/import/caller edges with code
citations + explicit degradation. Realization of "shared store": gcode and gwiki keep their
own FalkorDB graphs (gcode `CodeSymbol`/`CodeFile`/`CALLS`/`IMPORTS`; gwiki `WikiDoc`/
`WIKI_LINKS_TO`, guarded by `falkordb_graph_name_is_wiki_owned`), and gwiki reads gcode's
**live** code graph by name via `gobby_core::falkor` (`from_config`/`with_graph`), merging code
edges into graph-context at query time — no export artifact, no risky single-graph merge. (A
full single physical graph is a heavier deferred option.) Reuse: gwiki `commands/ask.rs`
(`ask_output_from_search`/`synthesize`/`synthesis_prompt`), `graph/context.rs` (P1.7),
`research_loop`; gcode `graph/code_graph/write.rs` is the producer (schema pinned, unchanged).

### 3.1 Make the gcode code graph live-consumable by gwiki [category: code] (depends: P1)

`kind: deliverable`

Targets: `crates/gwiki/src/code_graph.rs`, `docs/contracts/shared-graph-schema.md`, `crates/gcode/src/graph/code_graph/write.rs`, `crates/gcode/tests/contract.rs`

Pin the gcode code-graph schema as a shared producer/consumer contract and add a gwiki read
adapter. `docs/contracts/shared-graph-schema.md` documents the consumed labels/edges
(`CodeFile`/`CodeModule`/`CodeSymbol`/`ExternalSymbol`/`UnresolvedCallee`; `IMPORTS`/`DEFINES`/
`CALLS`; `project` scoping). A new gwiki `code_graph.rs` resolves the code graph name from the
shared config and opens it live via `gobby_core::falkor` to query CALLS/IMPORTS/DEFINES and
callers for given code symbols/files. A gcode schema-pin test guards the produced labels/edges
against drift from the documented contract.

**Acceptance:**

- 3.1.1 - gwiki opens the live gcode code graph (shared FalkorDB, code graph name from shared config) and queries CALLS/IMPORTS/DEFINES + callers for code symbols/files. file: `crates/gwiki/src/code_graph.rs`.
- 3.1.2 - The shared code-graph schema (labels, edges, `project` scoping) is pinned as a contract. file: `docs/contracts/shared-graph-schema.md`.
- 3.1.3 - A gcode test pins the written labels/edges to the documented schema so producer/consumer cannot drift. test: `cargo test -p gobby-code --no-default-features --test contract`.
- 3.1.4 - gwiki degrades explicitly when the code graph is unavailable (empty code edges + degradation note). file: `crates/gwiki/src/code_graph.rs`.
- 3.1.5 - No-default-features test covers gwiki code-graph reads and degradation. test: `cargo test -p gobby-wiki --no-default-features code_graph`.

### 3.2 Consume the shared code+knowledge graph in gwiki ask + graph-context [category: code] (depends: 3.1)

`kind: deliverable`

Targets: `crates/gwiki/src/graph/context.rs`, `crates/gwiki/src/commands/ask.rs`, `crates/gwiki/src/graph.rs`

Extend graph-context (P1.7) to merge code edges (from 3.1) with wiki-link edges into one
neighborhood — page links + code calls/imports/callers — carrying provenance + degradation.
gwiki `ask` grounds its synthesis in the unified neighborhood + code pages and emits code
citations (`file:line`/symbol) alongside source citations. Reuse `ask_output_from_search`,
`synthesize`, `synthesis_prompt`, `unique_sources`.

**Acceptance:**

- 3.2.1 - graph-context merges code edges (calls/imports/callers) with wiki-link edges into one neighborhood. file: `crates/gwiki/src/graph/context.rs`.
- 3.2.2 - gwiki `ask` grounds answers in the unified neighborhood + code pages, with code citations (`file:line`/symbol). file: `crates/gwiki/src/commands/ask.rs`.
- 3.2.3 - Both surfaces degrade to wiki-only with an explicit note when the code graph is unavailable. file: `crates/gwiki/src/graph/context.rs`.
- 3.2.4 - No-default-features test covers unified grounding and the degraded path. test: `cargo test -p gobby-wiki --no-default-features ask_unified_graph`.

### 3.3 Bring the gwiki research loop to the shared graph [category: code] (depends: 3.2)

`kind: deliverable`

Targets: `crates/gwiki/src/research_loop/engine.rs`, `crates/gwiki/src/research_loop/types.rs`

Extend the multi-step research loop so its Search/Read actions reach code pages + the unified
graph-context (P3.2) as first-class sources, accumulating code citations (`file:line`/symbol)
with provenance into accepted notes. Reuse `ResearchAction`, `execute_action`,
`write_validated_note`. Degrade to docs-only research when the code graph/index is unavailable.

**Acceptance:**

- 3.3.1 - The research loop retrieves/reads code pages + unified graph-context as first-class sources. file: `crates/gwiki/src/research_loop/engine.rs`.
- 3.3.2 - Accepted notes carry code citations (`file:line`/symbol) with provenance. file: `crates/gwiki/src/research_loop/types.rs`.
- 3.3.3 - Research degrades to docs-only when the code graph/index is unavailable. file: `crates/gwiki/src/research_loop/engine.rs`.
- 3.3.4 - No-default-features test covers code-grounded research and the degraded path. test: `cargo test -p gobby-wiki --no-default-features research_code`.

### 3.4 Update the gwiki agent contract for code-grounded ask + graph-context [category: code] (depends: 3.2)

`kind: deliverable`

Targets: `crates/gwiki/src/contract.rs`, `crates/gwiki/contract/gwiki.contract.json`, `crates/gwiki/tests/cli_contract.rs`, `docs/contracts/gwiki-cli.md`

Extend the gwiki `ask` and `graph-context` contract entries with code-edge + code-citation
fields, re-pin `gwiki.contract.json`, bump `contract_version`, extend the drift test, and update
`gwiki-cli.md`. gcode's contract gains no query/answer command; the shared code-graph schema is
owned by `docs/contracts/shared-graph-schema.md` (3.1).

**Acceptance:**

- 3.4.1 - The `ask` and `graph-context` entries gain code-edge + code-citation fields in the builder + pinned JSON; `contract_version` is bumped. file: `crates/gwiki/src/contract.rs`.
- 3.4.2 - `gwiki.contract.json` is re-pinned with the new shape. file: `crates/gwiki/contract/gwiki.contract.json`.
- 3.4.3 - `docs/contracts/gwiki-cli.md` documents the code-grounded `ask`/`graph-context` behavior. file: `docs/contracts/gwiki-cli.md`.
- 3.4.4 - The gwiki contract drift test passes for the new shape. test: `cargo test -p gobby-wiki --no-default-features --test cli_contract`.

## P4: Freshness, Librarian & Reports

`kind: framing`

**Goal**: Keep the unified vault current and trustworthy without silent rewrites.
Change-triggered staleness/refresh, an autonomous librarian that detects vault problems and
proposes tasks/patches (never silent canonical edits), PR/review reports, and research
citation-quality reports. All consumer-side (gwiki). Reuse gwiki `health.rs` (`inspect`/
`HealthReport`), `lint.rs` (`LintReport`/`LinkIssue`), `audit.rs` (`UnsupportedClaim`),
`credibility.rs` (`evaluate`/`CredibilityScore`), `provenance.rs` (`ProvenanceGraph`),
`commands/refresh/` (selection/candidate), `exports.rs` (artifacts); the P3 shared code-graph
adapter (`code_graph.rs`) for blast-radius/affected-code; gcore analytics (P1.3) for
risky-shift detection; P2.5 "what changed" for the change set. Per C1, the librarian and
change-triggered flow only mark stale / annotate / propose — canonical content changes require
an accepted action; daemon/MCP task creation is out of scope (proposals are artifacts).

### 4.1 Add change-triggered affected-page detection + mark-stale/refresh [category: code] (depends: P3)

`kind: deliverable`

Targets: `crates/gwiki/src/health.rs`, `crates/gwiki/src/commands/refresh/mod.rs`, `crates/gwiki/src/commands/refresh/selection.rs`, `crates/gwiki/src/code_graph.rs`, `crates/gwiki/src/provenance.rs`, `crates/gwiki/src/frontmatter.rs`

Map a change set (changed files/symbols from P2.5 + blast-radius via the P3 `code_graph`
adapter) to affected vault pages through provenance, then **mark affected pages stale**
(frontmatter `stale: true` + reason) or, for derived pages reproducible from canonical Markdown
+ provenance, trigger the existing `refresh` path. Canonical (hand-authored) pages are only
marked stale, never silently rewritten. Degrade to provenance-only mapping when the code graph
is unavailable.

**Acceptance:**

- 4.1.1 - Changed code files/symbols map to affected vault pages via provenance + shared-graph blast-radius. file: `crates/gwiki/src/code_graph.rs`.
- 4.1.2 - Affected pages are marked stale with a reason in frontmatter rather than silently rewritten. file: `crates/gwiki/src/frontmatter.rs`.
- 4.1.3 - Derived pages reproducible from canonical Markdown are refreshed via the existing refresh path; canonical pages are only marked stale. file: `crates/gwiki/src/commands/refresh/selection.rs`.
- 4.1.4 - Degrades to provenance-only mapping when the code graph/index is unavailable. file: `crates/gwiki/src/health.rs`.
- 4.1.5 - No-default-features test covers affected-page mapping, mark-stale, refresh, and degradation. test: `cargo test -p gobby-wiki --no-default-features change_triggered_refresh`.

### 4.2 Add autonomous librarian (detect + propose, no silent rewrites) [category: code] (depends: 4.1)

`kind: deliverable`

Targets: `crates/gwiki/src/librarian.rs`, `crates/gwiki/src/commands/librarian.rs`, `crates/gwiki/src/main.rs`, `crates/gwiki/src/health.rs`, `crates/gwiki/src/audit.rs`, `crates/gwiki/src/lint.rs`, `crates/gwiki/src/provenance.rs`

Add a `librarian` subcommand that scans the vault for stale pages (`health.rs`), missing
citations / unsupported claims (`audit.rs`), broken links (`lint.rs`), weak provenance
(`provenance.rs`), and outdated codewiki pages (P2.5 + shared graph). It emits a **proposals
report** (suggested tasks + suggested patch diffs) and writes only metadata/audit state
(mark-stale, audit annotations) — never canonical content. Proposals are artifacts for a human
or the daemon to accept; the librarian does not create daemon/MCP tasks itself. Each check
degrades independently when its datastore/provider is unavailable.

**Acceptance:**

- 4.2.1 - The librarian detects stale pages, missing citations, broken links, weak provenance, and outdated codewiki pages. file: `crates/gwiki/src/librarian.rs`.
- 4.2.2 - It emits a proposals report (suggested tasks + patch diffs) without rewriting canonical content. file: `crates/gwiki/src/commands/librarian.rs`.
- 4.2.3 - Only metadata/audit state is written (mark-stale, audit annotations); canonical changes require an accepted action. file: `crates/gwiki/src/librarian.rs`.
- 4.2.4 - The subcommand is registered and each check degrades independently when a datastore/provider is unavailable. file: `crates/gwiki/src/main.rs`.
- 4.2.5 - No-default-features test covers detection, propose-not-rewrite, and degradation. test: `cargo test -p gobby-wiki --no-default-features librarian`.

### 4.3 Add PR / review reports [category: code] (depends: 4.1)

`kind: deliverable`

Targets: `crates/gwiki/src/commands/review_report.rs`, `crates/gwiki/src/exports.rs`, `crates/gwiki/src/code_graph.rs`, `crates/gwiki/src/main.rs`

Add a `review-report` subcommand that, given a change set (changed files/symbols, e.g. a PR diff
or P2.5 changes), reports affected wiki pages, stale docs, changed graph neighborhoods, and
**risky dependency shifts** — high-centrality/bridge nodes touched, via `gobby_core::graph_analytics`
(P1.3) over the shared code graph (P3). Emit as a Markdown report artifact through `exports.rs`.
Degrade explicitly when graph/analytics are unavailable.

**Acceptance:**

- 4.3.1 - The report covers affected wiki pages, stale docs, changed graph neighborhoods, and risky dependency shifts. file: `crates/gwiki/src/commands/review_report.rs`.
- 4.3.2 - Risky shifts use `gobby_core::graph_analytics` (centrality/bridges) over the shared code graph. symbol: `gobby_core::graph_analytics::analyze`.
- 4.3.3 - The report is emitted as a Markdown artifact via the export machinery. file: `crates/gwiki/src/exports.rs`.
- 4.3.4 - The report degrades explicitly when graph/analytics are unavailable. file: `crates/gwiki/src/commands/review_report.rs`.
- 4.3.5 - No-default-features test covers the report and the degraded path. test: `cargo test -p gobby-wiki --no-default-features review_report`.

### 4.4 Add research citation-quality reports [category: code] (depends: 4.1)

`kind: deliverable`

Targets: `crates/gwiki/src/commands/citation_quality.rs`, `crates/gwiki/src/credibility.rs`, `crates/gwiki/src/provenance.rs`, `crates/gwiki/src/audit.rs`, `crates/gwiki/src/health.rs`, `crates/gwiki/src/main.rs`

Add a `citation-quality` subcommand reporting source credibility (`credibility.rs`), coverage
gaps (sections lacking sources via `provenance.rs`/`audit.rs`), contradictions (conflicting
sources for a claim — AI-assisted detection), stale-source warnings (`health.rs`), and
confidence per output. Emit as a Markdown artifact. Degrade explicitly when credibility signals
or AI are unavailable.

**Acceptance:**

- 4.4.1 - The report covers credibility, coverage gaps, contradictions, stale-source warnings, and confidence per output. file: `crates/gwiki/src/commands/citation_quality.rs`.
- 4.4.2 - Credibility, coverage, and staleness reuse `credibility.rs` / `provenance.rs` / `health.rs`. file: `crates/gwiki/src/credibility.rs`.
- 4.4.3 - Contradiction detection flags conflicting sources for a claim and degrades when AI is unavailable. file: `crates/gwiki/src/commands/citation_quality.rs`.
- 4.4.4 - Coverage-gap detection uses provenance section→source links. file: `crates/gwiki/src/provenance.rs`.
- 4.4.5 - No-default-features test covers the report and degradation. test: `cargo test -p gobby-wiki --no-default-features citation_quality`.

### 4.5 Add librarian/review/citation surfaces to the gwiki agent contract [category: code] (depends: 4.2, 4.3, 4.4)

`kind: deliverable`

Targets: `crates/gwiki/src/contract.rs`, `crates/gwiki/contract/gwiki.contract.json`, `crates/gwiki/tests/cli_contract.rs`, `docs/contracts/gwiki-cli.md`

Add `librarian`, `review-report`, and `citation-quality` to the contract builder + pinned JSON
(each carrying trust/freshness/audit/source/degradation fields as applicable), bump
`contract_version`, extend the drift test, and update `gwiki-cli.md`.

**Acceptance:**

- 4.5.1 - `librarian`, `review-report`, and `citation-quality` are added to the contract builder + pinned JSON; `contract_version` is bumped. file: `crates/gwiki/src/contract.rs`.
- 4.5.2 - Each new command carries trust/freshness/audit/source/degradation fields where applicable. file: `crates/gwiki/contract/gwiki.contract.json`.
- 4.5.3 - `docs/contracts/gwiki-cli.md` documents the three commands and matches behavior. file: `docs/contracts/gwiki-cli.md`.
- 4.5.4 - The gwiki contract drift test passes for the new shape. test: `cargo test -p gobby-wiki --no-default-features --test cli_contract`.

## V1: Verification

`kind: verification`

Whole-plan verification, applied per phase as designed:

- `uv run gobby plans validate .gobby/plans/gwiki-parity-plus.md` passes (structure,
  consumer sweep); every acceptance `file:`/`test:` ref appears in its section `Targets:`.
- Per code deliverable: `cargo test -p gobby-wiki --no-default-features <name>` (and
  `-p gobby-code` for gcode-side phases) proves behavior + explicit degradation.
- Unified-vault end-to-end: generate gcode codewiki into the gwiki vault, `gwiki index`,
  confirm Obsidian graph view + gwiki backlinks/graph-context see code pages.
