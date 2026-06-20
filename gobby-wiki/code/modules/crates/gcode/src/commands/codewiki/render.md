---
title: crates/gcode/src/commands/codewiki/render
type: code_module
provenance:
- file: crates/gcode/src/commands/codewiki/render/audit.rs
- file: crates/gcode/src/commands/codewiki/render/common.rs
- file: crates/gcode/src/commands/codewiki/render/diagrams.rs
- file: crates/gcode/src/commands/codewiki/render/features.rs
- file: crates/gcode/src/commands/codewiki/render/infrastructure.rs
- file: crates/gcode/src/commands/codewiki/render/overview.rs
- file: crates/gcode/src/commands/codewiki/render/pages.rs
- file: crates/gcode/src/commands/codewiki/render/repo.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/render

Parent: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

The `render` module turns Codewiki data models into human-readable Markdown pages for repository, architecture, module, file, audit, feature, diagram, and infrastructure documentation. Its renderers build range-free frontmatter, attach degradation and verification metadata, and emit navigable wiki links instead of raw provenance dumps; module pages, for example, write parent navigation, an overview, child-module rows, and direct-file rows from `ModuleDoc` input (`crates/gcode/src/commands/codewiki/render/pages.rs:1-55`). Architecture pages similarly combine model narrative, validated diagram/service-matrix strings, and deterministic subsystem tables (`crates/gcode/src/commands/codewiki/render/overview.rs:1-55`).

A central flow is summary compaction for parent tables. `cell_summary` keeps only the leading prose paragraph, stops before embedded Markdown tables, flattens whitespace, and caps long text at 600 characters on a word boundary (`crates/gcode/src/commands/codewiki/render/common.rs:9-49`). That helper is used by architecture subsystem rows and module child rows so full structured briefs remain on linked pages while parent pages stay scannable (`crates/gcode/src/commands/codewiki/render/overview.rs:32-55`, `crates/gcode/src/commands/codewiki/render/pages.rs:20-35`). `model_degraded_sources` provides the simple degradation marker used when generation is unavailable (`crates/gcode/src/commands/codewiki/render/common.rs:1-7`).

At the repository level, `build_repo_doc` gathers top-level modules and root files, derives prompt child summaries, rolls up source spans, consults `ReusePlan` for an unchanged `code/repo.md`, and otherwise calls `maybe_generate` with `prompts::repo_prompt` before falling back to structural summaries on failure (`crates/gcode/src/commands/codewiki/render/repo.rs:1-65`). This places the module between upstream Codewiki collection/generation types such as `FileDoc`, `ModuleDoc`, `LeadingChunk`, `TextGenerator`, `ReusePlan`, and `CodewikiProgress`, and downstream Markdown wiki output. It imports sibling helpers `cell_summary` and `model_degraded_sources`, plus shared parent-module, wikilink, prompt, span, table, and frontmatter utilities through `super::super::*` (`crates/gcode/src/commands/codewiki/render/repo.rs:1-2`, `crates/gcode/src/commands/codewiki/render/pages.rs:1-8`, `crates/gcode/src/commands/codewiki/render/overview.rs:1-8`).

| Public API symbol | Responsibility |
| --- | --- |
| `render_module_doc` | Render a module wiki page from `ModuleDoc` with parent, overview, child modules, and files (`crates/gcode/src/commands/codewiki/render/pages.rs:5-47`) |
| `render_file_doc` | Render a file wiki page from `FileDoc` (`crates/gcode/src/commands/codewiki/render/pages.rs:49-55`) |
| `render_architecture_doc` | Render architecture overview narrative, diagrams, service matrix, and subsystem table (`crates/gcode/src/commands/codewiki/render/overview.rs:5-55`) |
| `build_repo_doc` | Build or reuse the repository overview page, optionally using text generation (`crates/gcode/src/commands/codewiki/render/repo.rs:4-65`) |
| `cell_summary` | Compact generated summaries for table cells (`crates/gcode/src/commands/codewiki/render/common.rs:18-49`) |
| `model_degraded_sources` | Return `model-unavailable` when model generation degraded (`crates/gcode/src/commands/codewiki/render/common.rs:1-7`) |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/codewiki/render/audit.rs\|crates/gcode/src/commands/codewiki/render/audit.rs]] | `crates/gcode/src/commands/codewiki/render/audit.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/render/common.rs\|crates/gcode/src/commands/codewiki/render/common.rs]] | `crates/gcode/src/commands/codewiki/render/common.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/render/diagrams.rs\|crates/gcode/src/commands/codewiki/render/diagrams.rs]] | `crates/gcode/src/commands/codewiki/render/diagrams.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gcode/src/commands/codewiki/render/features.rs\|crates/gcode/src/commands/codewiki/render/features.rs]] | `crates/gcode/src/commands/codewiki/render/features.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/render/infrastructure.rs\|crates/gcode/src/commands/codewiki/render/infrastructure.rs]] | `crates/gcode/src/commands/codewiki/render/infrastructure.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gcode/src/commands/codewiki/render/overview.rs\|crates/gcode/src/commands/codewiki/render/overview.rs]] | `crates/gcode/src/commands/codewiki/render/overview.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/render/pages.rs\|crates/gcode/src/commands/codewiki/render/pages.rs]] | `crates/gcode/src/commands/codewiki/render/pages.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/render/repo.rs\|crates/gcode/src/commands/codewiki/render/repo.rs]] | `crates/gcode/src/commands/codewiki/render/repo.rs` exposes 3 indexed API symbols. |

