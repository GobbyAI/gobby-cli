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

`crates/gcode/src/commands/codewiki` is the documentation-generation subsystem for CodeWiki. It gathers indexed files, symbols, graph edges, graph availability, and leading source chunks into `CodewikiInput`; those leading chunks are converted into prompt excerpts and ranked by symbol density for module-level context (`crates/gcode/src/commands/codewiki/types.rs:1-100`). Its prompt layer defines the contract for symbol, file, content-file, and module briefs, including the requirement to use supplied evidence only, cite anchors, describe cross-file callers/callees/imports when present, and prefer tables for enumerable facts (`crates/gcode/src/commands/codewiki/prompts.rs:1-100`).

The main generation flow builds typed docs for repository, architecture, modules, files, audits, features, onboarding, hotspots, infrastructure, curated concepts, and ownership, then renders them to Markdown and persists them. The child `build_parts` module supplies deterministic and AI-assisted builders, including LLM-free audit pages and a two-step curated-navigation flow that plans concepts before rendering grounded pages with fallbacks (`audit.rs:1-8`, `plan.rs:1-43`, `render.rs:9-33`). The render layer turns these data models into Markdown pages with frontmatter, degradation/verification metadata, and wiki links for navigation (`crates/gcode/src/commands/codewiki/render/pages.rs:1-55`, `crates/gcode/src/commands/codewiki/render/overview.rs:1-55`).

The module collaborates outward with the broader indexing, graph, AI, and filesystem layers. It imports `gobby_core::config::AiRouting`, serde serialization, and indexed `Symbol` records, then calls into prompt construction, graph/model building, text generation, citation grounding, verification, and doc writing (`crates/gcode/src/commands/codewiki/types.rs:1-100`). Architecture diagrams are deliberately seeded from the deterministic `SystemModel`, not per-symbol graph dumps, and each Mermaid block is validated before being emitted; sparse models simply omit diagrams without marking the page degraded (`crates/gcode/src/commands/codewiki/architecture_diagrams.rs:1-100`). Persistence is handled through full or incremental doc-set writes, with `DocSink` and `DocPruneScope` deciding what to write or prune by file/module scope (`crates/gcode/src/commands/codewiki/io.rs:1-100`).

Ownership documentation is a collaboration point with repository metadata: it combines CODEOWNERS declarations with Git blame-derived contributors, emits `type: code_ownership`, module wikilinks, declared owners, contributor summaries, and degradation markers when sources are unavailable (`tests.rs:1-100`). The text submodule completes the prose pipeline by sanitizing generated Markdown links and rewriting relative citation targets into resolvable line anchors, so rendered pages can be linted and navigated reliably (`crates/gcode/src/commands/codewiki/text/sanitize.rs:1-100`).

| Area | Representative public symbols |
| --- | --- |
| Generation orchestration | `generate_hierarchical_docs`, `generate_hierarchical_docs_core`, `run`, `run_repair` |
| Input and data models | `CodewikiInput`, `CodewikiGraphEdge`, `FileDoc`, `ModuleDoc`, `ArchitectureDoc`, `BuiltDoc` |
| Prompting and prose | `symbol_prompt`, `file_prompt`, `module_prompt`, `architecture_prompt`, `verify_prompt` |
| Rendering | `render_repo_doc`, `render_architecture_doc`, `render_module_doc`, `render_file_doc` |
| Persistence and reuse | `write_doc_set`, `write_incremental_doc_set_with_snapshot`, `DocPruneScope`, `ReusePlan` |
| Ownership | `build_ownership_doc`, `OwnershipOptions`, `OwnershipMeta`, `read_codeowners` |
| Architecture model/diagrams | `build_system_model`, `render_architecture_diagrams`, `render_service_matrix`, `is_valid_mermaid` |
[crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:6-38]
[crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:10-133]
[crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:6-13]
[crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:28-31]
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-170]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/commands/codewiki/build_parts\|crates/gcode/src/commands/codewiki/build_parts]] | The `build_parts` module is the document-generation toolkit behind codewiki pages: architecture, audits, changes, curated concepts, feature catalogs, file/module pages, hotspots, infrastructure, onboarding, and snapshots. Its audit path is deterministic and LLM-free, building deprecation and dead-code pages from indexed symbols, call graph edges, and bounded source scans, while keeping index parsing and hub schemas untouched (`audit.rs:1-8`). Curated concepts use a two-step flow: first they plan concept modules, sections, and narrative pages from file/module summaries, then render grounded… |
| [[code/modules/crates/gcode/src/commands/codewiki/ownership\|crates/gcode/src/commands/codewiki/ownership]] | The ownership module builds CodeWiki ownership documentation by combining declared CODEOWNERS data with derived Git blame contributors. Its tests show the main flow through `build_ownership_doc`, which receives a project root, file list, module map, mutable `OwnershipMeta`, and `OwnershipOptions`, then emits `type: code_ownership`, module wikilinks, declared owners, contributor summaries, and degradation markers when sources are unavailable (`tests.rs:1-100`). |
| [[code/modules/crates/gcode/src/commands/codewiki/render\|crates/gcode/src/commands/codewiki/render]] | The `render` module turns Codewiki data models into human-readable Markdown pages for repository, architecture, module, file, audit, feature, diagram, and infrastructure documentation. Its renderers build range-free frontmatter, attach degradation and verification metadata, and emit navigable wiki links instead of raw provenance dumps; module pages, for example, write parent navigation, an overview, child-module rows, and direct-file rows from `ModuleDoc` input (`crates/gcode/src/commands/codewiki/render/pages.rs:1-55`). Architecture pages similarly combine model narrative, validated… |
| [[code/modules/crates/gcode/src/commands/codewiki/text\|crates/gcode/src/commands/codewiki/text]] | The `codewiki/text` module owns the prose pipeline for generated wiki pages: deterministic structural summaries, AI-assisted generation, citation grounding, Markdown sanitization, YAML frontmatter, and optional verifier notes. `sanitize_model_markdown_links` first strips unsafe link targets, then rewrites relative citation targets from `path:line[-end]` to resolvable `path#Lline[-Lend]` anchors so downstream linting can validate them (crates/gcode/src/commands/codewiki/text/sanitize.rs:1-100). |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/codewiki/architecture_diagrams.rs\|crates/gcode/src/commands/codewiki/architecture_diagrams.rs]] | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs` exposes 35 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build.rs\|crates/gcode/src/commands/codewiki/build.rs]] | `crates/gcode/src/commands/codewiki/build.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/cluster.rs\|crates/gcode/src/commands/codewiki/cluster.rs]] | `crates/gcode/src/commands/codewiki/cluster.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/generation.rs\|crates/gcode/src/commands/codewiki/generation.rs]] | `crates/gcode/src/commands/codewiki/generation.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/graph.rs\|crates/gcode/src/commands/codewiki/graph.rs]] | `crates/gcode/src/commands/codewiki/graph.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/io.rs\|crates/gcode/src/commands/codewiki/io.rs]] | `crates/gcode/src/commands/codewiki/io.rs` exposes 33 indexed API symbols. |
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
| [[code/files/crates/gcode/src/commands/codewiki/text.rs\|crates/gcode/src/commands/codewiki/text.rs]] | `crates/gcode/src/commands/codewiki/text.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/types.rs\|crates/gcode/src/commands/codewiki/types.rs]] | `crates/gcode/src/commands/codewiki/types.rs` exposes 65 indexed API symbols. |

