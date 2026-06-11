# gwiki CLI Contract

The machine-readable contract lives at `crates/gwiki/contract/gwiki.contract.json`.
`gwiki contract --format json` must emit the same contract version and contents.

## Version

`contract_version`: 4

Version 4 covers the daemon-consumed surface:

- `contract`
- `index`
- `search`
- `ask`
- `read`
- `refresh`
- `ingest-file`
- `ingest-url`
- `collect`
- `research`
- `compile`
- `audit`
- `graph`
- `graph-context`
- `health`
- `librarian`
- `review-report`
- `citation-quality`
- `sources`
- `backlinks`
- `status`
- `trust`
- `remove-source`

Version 4 adds the `librarian`, `review-report`, and `citation-quality`
surfaces to the daemon contract. These entries pin dependency/degradation
classification fields and advertise trust, freshness, audit, source, and
degradation payload keys where the surface emits them.

Version 3 added code-grounded payload fields to `ask` and `graph-context`.
`ask` returns `code_edges` and `code_citations` alongside wiki hits and source
citations when code graph signals are available. `graph-context` returns
`code_edges` and `code_citations` alongside `context`, `source_bundle`, `trust`,
`freshness`, `audit`, `warnings`, and `degradation`.

The `ask`, `graph-context`, `research`, `librarian`, `review-report`, and
`citation-quality` entries pin their dependency and degradation rows in the
machine-readable contract. `ask` treats model synthesis, code graph, semantic
vectors, and FalkorDB as optional signals, and can degrade to an extractive
citation-list answer. `research` treats the model synthesis loop, code
graph/index, and semantic vectors as optional, and can degrade to a
retrieval-only research scaffold. `librarian` keeps deterministic upkeep
proposals available while skipping unavailable checks. `review-report` can emit
a report without the risky-shift section when graph analytics are unavailable.
`citation-quality` can skip unavailable quality sections independently.

## Scope

`gwiki` accepts `--project <ROOT>` and `--topic <NAME>`.

No scope flag means detect the project from the current working directory. Bare
`--project` means the current directory. `--scope` is not part of this contract.

Every scoped JSON result consumed by Gobby carries a resolved `scope` identity
with `kind` and `id`.

## AI Routing

AI route flags use `auto|daemon|direct|off`. `direct` means any
OpenAI-compatible endpoint, local or remote. There is no `local` route.

## Research

`gwiki research` is governed by the standalone research contract in
[`gwiki-research.md`](gwiki-research.md). That contract defines the replacement
reason-act loop, audit mode, provenance rules, budgets, and the boundary between
gwiki-owned wiki mutation and Gobby-owned daemon enhancement.

## Dependency & Degradation Classification

PostgreSQL and canonical Markdown are hard dependencies for every Parity+
surface. Their absence is a command failure, not a degraded result. The tables
below classify the remaining hard dependencies, optional dependencies, degraded
output shape, and user-visible degradation metadata for every Parity+ command
surface and generated-page output surface.

Multimodal providers for transcription, vision, and video are not dependencies
of any Parity+ command or generated-page surface. They are used only by source
ingest (`gwiki collect` of audio, image, or video inputs) and therefore never
change Parity+ output. Every row records this as `none - not used` so the
non-dependency is explicit.

Each command deliverable must embed its row inline, and contract-registered
command surfaces must pin the same classification in
`crates/gwiki/contract/gwiki.contract.json`. Each generated-page deliverable must
embed its row inline; generated-page degradation metadata lives in page YAML
frontmatter rather than the CLI JSON contract.

The machine-readable side of the generated-page frontmatter contract lives in
`gobby_core::codewiki_contract`: the shared key/value constants (`provenance`,
`generated_by: gcode-codewiki`, `trust: generated`, `freshness: indexed`,
`degraded`/`degraded_sources`) and a golden page fixture. gcode pins its
frontmatter emitter against the golden fixture and gwiki pins its
frontmatter/audit parsers against it, so producer and consumer cannot drift
silently.

### Command Surfaces

| Command | Hard dependencies | Optional dependencies | Multimodal | Degraded output shape | Degradation metadata |
| --- | --- | --- | --- | --- | --- |
| `graph` | PostgreSQL, Markdown | FalkorDB, embeddings/Qdrant | none - not used | available nodes/edges; missing edge classes empty and flagged | `degraded`, `degraded_sources[]` in `graph.json`/`GRAPH_REPORT.md` |
| `graph-context` | PostgreSQL | FalkorDB, shared code graph | none - not used | wiki-link-only neighborhood | `warnings[]`, `degradation{degraded,degraded_sources[]}` |
| `benchmark` | PostgreSQL, seeded project | FalkorDB, Qdrant+embeddings, model | none - not used | metrics for available dimensions only | per-metric `available`, `degraded_sources[]` |
| `ask` | PostgreSQL | model synthesis, code graph, Qdrant+embeddings, FalkorDB | none - not used | model off emits an extractive citation-list answer; signal loss falls back to wiki-only grounding | `degraded`, `degraded_sources[]` on answer |
| `research` | PostgreSQL | model multi-step synthesis loop, code graph/index, Qdrant+embeddings | none - not used | model off emits a retrieval-only research scaffold with candidate sources and citations but no synthesized notes; code graph/index off emits docs-only output | per-note and report `degradation` note |
| `librarian` | PostgreSQL, vault | FalkorDB/code graph, Qdrant+embeddings, model | none - not used | each check skipped independently with a note | per-check `available` in proposals report |
| `review-report` | PostgreSQL, change set | FalkorDB/code graph and analytics | none - not used | report without risky-shift section | `degraded`, `degraded_sources[]` on report |
| `citation-quality` | PostgreSQL | credibility signals, model contradiction detection | none - not used | per-section skipped with a note | per-section `available` |

### Codewiki Generated-Page Surfaces

These are gcode `codewiki` output surfaces, not commands. PostgreSQL code index
and Markdown vault are hard dependencies for every page.

| Generated page | Hard dependencies | Optional dependencies | Multimodal | Degraded output shape | Degradation metadata |
| --- | --- | --- | --- | --- | --- |
| `code/_architecture.md` | PostgreSQL code index, Markdown vault | model subsystem summaries, FalkorDB/graph cross-cluster edges | none - not used | structural module summaries plus reduced or empty subsystem diagram | frontmatter `degraded`/`degraded_sources`; `generated_by: gcode-codewiki` |
| `code/_onboarding.md` | PostgreSQL code index, Markdown vault | `gobby_core::graph_analytics` centrality | none - not used | structural entry-point list with no ranked reading order | frontmatter `degraded`/`degraded_sources` |
| `code/_hotspots.md` | PostgreSQL code index, Markdown vault | `gobby_core::graph_analytics` hotspots, god nodes, and bridges | none - not used | explicit "analytics unavailable" note | frontmatter `degraded`/`degraded_sources` |
| `code/_ownership.md` | PostgreSQL code index, Markdown vault | git repo and blame through `gix`, `CODEOWNERS` file | none - not used | CODEOWNERS-only output, "unknown ownership", or `partial` when capped or timed out | frontmatter `degraded`/`degraded_sources`; `partial` |
| `code/_changes.md` | PostgreSQL code index, Markdown vault | prior `CodewikiMeta` snapshot for diff baseline, FalkorDB/graph neighborhood fingerprint | none - not used | first run without prior snapshot emits an accepted baseline page, not a failure; graph-off output drops the neighborhood diff | frontmatter `baseline`/`degraded` |

## Drift Checks

Both the CLI and daemon tests load this contract. New daemon-facing flags or JSON
keys should update this document, the JSON contract, and the corresponding drift
tests in the same change.

The pinned `ask`, `graph-context`, `research`, `librarian`, `review-report`, and
`citation-quality` command entries record their classification rows with
top-level `hard_dependencies`, `optional_dependencies`, `multimodal`, and
`degradation` fields so daemon consumers can detect dependency and degradation
drift directly from the contract JSON.

_Last verified: 2026-06-08_
