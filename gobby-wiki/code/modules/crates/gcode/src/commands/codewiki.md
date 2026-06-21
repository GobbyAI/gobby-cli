---
title: crates/gcode/src/commands/codewiki
type: code_module
provenance:
- file: crates/gcode/src/commands/codewiki/architecture_diagrams.rs
- file: crates/gcode/src/commands/codewiki/build_parts/audit.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs
- file: crates/gcode/src/commands/codewiki/build_parts/curated_content.rs
- file: crates/gcode/src/commands/codewiki/build_parts/features.rs
- file: crates/gcode/src/commands/codewiki/build_parts/onboarding.rs
- file: crates/gcode/src/commands/codewiki/cluster.rs
- file: crates/gcode/src/commands/codewiki/generation.rs
- file: crates/gcode/src/commands/codewiki/io.rs
- file: crates/gcode/src/commands/codewiki/ownership.rs
- file: crates/gcode/src/commands/codewiki/ownership/analysis.rs
- file: crates/gcode/src/commands/codewiki/ownership/render.rs
- file: crates/gcode/src/commands/codewiki/ownership/tests.rs
- file: crates/gcode/src/commands/codewiki/paths.rs
- file: crates/gcode/src/commands/codewiki/progress.rs
- file: crates/gcode/src/commands/codewiki/prompts.rs
- file: crates/gcode/src/commands/codewiki/relationship_facts.rs
- file: crates/gcode/src/commands/codewiki/repair.rs
- file: crates/gcode/src/commands/codewiki/reuse.rs
- file: crates/gcode/src/commands/codewiki/run.rs
- file: crates/gcode/src/commands/codewiki/system_model.rs
- file: crates/gcode/src/commands/codewiki/text.rs
- file: crates/gcode/src/commands/codewiki/text/citations.rs
- file: crates/gcode/src/commands/codewiki/text/frontmatter.rs
- file: crates/gcode/src/commands/codewiki/text/generation.rs
- file: crates/gcode/src/commands/codewiki/text/sanitize.rs
- file: crates/gcode/src/commands/codewiki/text/structural.rs
- file: crates/gcode/src/commands/codewiki/text/verify.rs
- file: crates/gcode/src/commands/codewiki/types.rs
provenance_truncated: 25
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki

Parent: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

## Module: `crates/gcode/src/commands/codewiki`

The `codewiki` module implements the `codewiki` CLI command, which generates a comprehensive wiki-style Markdown documentation site from a Rust workspace. Its central responsibility is orchestrating AI-assisted prose generation across four granularities — symbols, files, modules, and cross-cutting architectural pages — then writing the results to disk with frontmatter provenance and incremental-build support. The module is self-contained with respect to documentation logic: it reads workspace manifests and the code index, assembles structured prompt inputs, calls out to AI text generators, validates and cleans the output, and persists only the pages that have changed since the last run.

The primary execution path begins in `run.rs:run`, which delegates to `generation.rs:generate_hierarchical_docs` and its capability-layering variants (`_with_graph_availability`, `_with_ownership`, `_with_reuse`, `_with_verify`, `_with_progress`, `_core`). These compose `CodewikiInput` (types.rs:10-20) — a bundle of source file paths, call/import graph edges fetched from FalkorDB via `fetch_codewiki_graph_edges`, indexed `Symbol` records, and per-file `LeadingChunk` source excerpts — then drive per-file and per-module doc builds through the `build_parts` child module. Prompt assembly lives in `prompts.rs`, which exposes system-prompt constants (`SYMBOL_SYSTEM`, `FILE_SYSTEM`, `MODULE_SYSTEM`, etc.) and builder functions such as `file_prompt`, `module_prompt`, and `build_entity_prompt` that inject cross-file `RelationshipFacts` (relationship_facts.rs), symbol tables, and bounded source excerpts (prompts.rs:1-20). Generated text passes through `maybe_generate` → `clean_generated` → `ground_text` (text module) to strip invalid citations, re-anchor line references, and append fallback source provenance.

Two supporting pipelines run alongside prose generation. The architecture pipeline reads every `Cargo.toml` in `build_system_model` (system_model.rs) to produce a deterministic `SystemModel` of crates, edges, service boundaries, and runtime modes, then `render_architecture_diagrams` (architecture_diagrams.rs:44-56) converts it into Mermaid `flowchart` / `sequenceDiagram` blocks validated by `is_valid_mermaid` before emission — invalid blocks are silently omitted rather than written as broken fences. The ownership pipeline in the `ownership` child module combines a parsed `CODEOWNERS` file with `git blame` contributor analysis (`blame_file_contributors_with_timeout`) to produce per-file and per-module ownership pages, caching results in `OwnershipMeta` to avoid redundant shell invocations. Incremental builds are governed by `ReusePlan` (reuse.rs), which hashes existing doc frontmatter and neighbor fingerprints and skips regeneration for unchanged pages; `DocSink` (io.rs:~60-) manages atomic writes, prune scoping, and symlink safety, while `DocPruneScope` restricts deletions to the targeted file or module subtree.

The module is called into by the parent `crates/gcode/src/commands` dispatcher and imports `gobby_core::config::AiRouting` for AI provider routing (types.rs:3). It calls out to FalkorDB via `codewiki_call_edges_query` / `codewiki_import_edges_query`, to the filesystem and git toolchain for ownership data, and to the configured `TextGenerator` / `TextVerifier` async closures for prose and verification respectively.

### Core types

| Type | File | Description |
|---|---|---|
| `CodewikiInput` | types.rs:10 | Input bundle: file paths, graph edges, symbols, leading chunks |
| `LeadingChunk` | types.rs:24 | First indexed content chunk of a file with line range |
| `CodewikiGraphEdge` / `CodewikiGraph` | types.rs | Call/import edge records and availability wrapper |
| `SystemModel` | system_model.rs | Deterministic crate + service topology from workspace manifests |
| `DocSink` | io.rs | Incremental writer with prune scope, snapshot, and flush/finish lifecycle |
| `DocPruneScope` | io.rs:45 | Scoped or unscoped delete boundary for stale docs |
| `ReusePlan` | reuse.rs | Hash-based reuse check; `reusable_page*` methods gate AI calls |
| `RelationshipFacts` | relationship_facts.rs | Per-file inbound/outbound call and import relations |
| `CodewikiProgress` | progress.rs | Silent / stderr / capture progress sink |
| `AuditContext` | cluster.rs | Subsystem clustering state for dependency topology |

### Key public functions

| Function | File | Description |
|---|---|---|
| `run` | run.rs | Top-level command entry point |
| `generate_hierarchical_docs` | generation.rs | Full orchestration; delegates to `_core` via capability wrappers |
| `write_incremental_doc_set` | io.rs | Writes only changed docs; calls `write_incremental_doc_set_with_snapshot` |
| `build_system_model` | system_model.rs | Parses `Cargo.toml` manifests into `SystemModel` |
| `render_architecture_diagrams` | architecture_diagrams.rs:44 | Emits only valid Mermaid fences from `SystemModel` |
| `build_ownership_doc` | ownership.rs | Combines CODEOWNERS + blame into ownership page |
| `fetch_codewiki_graph_edges` | generation.rs | Queries FalkorDB for call/import edges |
| `ground_text` | text module | Strips unsafe links, re-anchors citations, appends fallback spans |
| `repair_citations` | repair.rs | Post-hoc stale-citation repair using `IndexCitationResolver` |
| `cluster_file_modules` | cluster.rs | Groups files under subsystem roots for topology diagrams |

### AI prompt system constants (prompts.rs:9-13)

| Constant | Audience |
|---|---|
| `SYMBOL_SYSTEM` | One-sentence API reference for a single symbol |
| `FILE_SYSTEM` | Multi-section explainer page for a source file |
| `CONTENT_FILE_SYSTEM` | Explainer page for non-code files (markdown, config) |
| `MODULE_SYSTEM` | Two-to-four paragraph module documentation brief |
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-170]
[crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:10-138]
[crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:4-13]
[crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:1-7]
[crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:6-13]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/commands/codewiki/build_parts\|crates/gcode/src/commands/codewiki/build_parts]] | ## Module: `crates/gcode/src/commands/codewiki/build_parts` |
| [[code/modules/crates/gcode/src/commands/codewiki/ownership\|crates/gcode/src/commands/codewiki/ownership]] | ## Module: `crates/gcode/src/commands/codewiki/ownership` |
| [[code/modules/crates/gcode/src/commands/codewiki/render\|crates/gcode/src/commands/codewiki/render]] | ## Module: crates/gcode/src/commands/codewiki/render |
| [[code/modules/crates/gcode/src/commands/codewiki/text\|crates/gcode/src/commands/codewiki/text]] | ## Module: `crates/gcode/src/commands/codewiki/text` |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/codewiki/architecture_diagrams.rs\|crates/gcode/src/commands/codewiki/architecture_diagrams.rs]] | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs` exposes 35 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build.rs\|crates/gcode/src/commands/codewiki/build.rs]] | `crates/gcode/src/commands/codewiki/build.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/cluster.rs\|crates/gcode/src/commands/codewiki/cluster.rs]] | `crates/gcode/src/commands/codewiki/cluster.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/generation.rs\|crates/gcode/src/commands/codewiki/generation.rs]] | `crates/gcode/src/commands/codewiki/generation.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/graph.rs\|crates/gcode/src/commands/codewiki/graph.rs]] | `crates/gcode/src/commands/codewiki/graph.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/io.rs\|crates/gcode/src/commands/codewiki/io.rs]] | `crates/gcode/src/commands/codewiki/io.rs` exposes 35 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/mod.rs\|crates/gcode/src/commands/codewiki/mod.rs]] | `crates/gcode/src/commands/codewiki/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/ownership.rs\|crates/gcode/src/commands/codewiki/ownership.rs]] | `crates/gcode/src/commands/codewiki/ownership.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/ownership/analysis.rs\|crates/gcode/src/commands/codewiki/ownership/analysis.rs]] | `crates/gcode/src/commands/codewiki/ownership/analysis.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/ownership/codeowners.rs\|crates/gcode/src/commands/codewiki/ownership/codeowners.rs]] | `crates/gcode/src/commands/codewiki/ownership/codeowners.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/ownership/render.rs\|crates/gcode/src/commands/codewiki/ownership/render.rs]] | `crates/gcode/src/commands/codewiki/ownership/render.rs` exposes 10 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/paths.rs\|crates/gcode/src/commands/codewiki/paths.rs]] | `crates/gcode/src/commands/codewiki/paths.rs` exposes 19 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/progress.rs\|crates/gcode/src/commands/codewiki/progress.rs]] | `crates/gcode/src/commands/codewiki/progress.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/prompts.rs\|crates/gcode/src/commands/codewiki/prompts.rs]] | `crates/gcode/src/commands/codewiki/prompts.rs` exposes 51 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/relationship_facts.rs\|crates/gcode/src/commands/codewiki/relationship_facts.rs]] | `crates/gcode/src/commands/codewiki/relationship_facts.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/render.rs\|crates/gcode/src/commands/codewiki/render.rs]] | `crates/gcode/src/commands/codewiki/render.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/repair.rs\|crates/gcode/src/commands/codewiki/repair.rs]] | `crates/gcode/src/commands/codewiki/repair.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/reuse.rs\|crates/gcode/src/commands/codewiki/reuse.rs]] | `crates/gcode/src/commands/codewiki/reuse.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/run.rs\|crates/gcode/src/commands/codewiki/run.rs]] | `crates/gcode/src/commands/codewiki/run.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/system_model.rs\|crates/gcode/src/commands/codewiki/system_model.rs]] | `crates/gcode/src/commands/codewiki/system_model.rs` exposes 28 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/tests.rs\|crates/gcode/src/commands/codewiki/tests.rs]] | `crates/gcode/src/commands/codewiki/tests.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gcode/src/commands/codewiki/text.rs\|crates/gcode/src/commands/codewiki/text.rs]] | `crates/gcode/src/commands/codewiki/text.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/types.rs\|crates/gcode/src/commands/codewiki/types.rs]] | `crates/gcode/src/commands/codewiki/types.rs` exposes 65 indexed API symbols. |

