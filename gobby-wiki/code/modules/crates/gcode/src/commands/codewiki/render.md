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

## Module: crates/gcode/src/commands/codewiki/render

This module is the Markdown rendering layer of the `codewiki` command. It takes structured documentation data types produced by the parent `codewiki` subsystem — `ArchitectureDoc`, `ModuleDoc`, `FileDoc`, `RepoDoc`, and equivalents for features, audit, infrastructure, and hotspots — and serialises them into Obsidian-compatible wiki pages with YAML frontmatter, wikilinks, and Markdown tables. Every file in the module imports the parent namespace via `use super::super::*` (overview.rs:3, pages.rs:3, repo.rs:1) to access shared helpers such as `frontmatter_with_degradation_*`, `write_section`, `write_markdown_table_header`, `module_wikilink`, and `file_wikilink`. The two utilities shared across all render files — `cell_summary` and `model_degraded_sources` — live in `common.rs` and are re-exported inward (repo.rs:2).

`common.rs` contains the central prose-trimming logic used whenever a multi-paragraph summary must fit inside a single table cell (common.rs:22–60). `cell_summary` reads a summary line-by-line, stops at the first Markdown table row (`|`) or blank line after prose has started, falls back to whitespace-flattened full text when the summary opens directly with a table, and hard-caps the result at 600 characters on a word boundary (common.rs:11). This is called uniformly by `render_architecture_doc` when building the subsystems table (overview.rs:47), by `render_module_doc` for child-module rows (pages.rs:33), and by `build_repo_doc` for top-module rows (repo.rs:2). `model_degraded_sources` converts a boolean degradation flag into a string tag list consumed by frontmatter builders (common.rs:1–6).

The page-level render functions map one-to-one to wiki page categories:

| Function | File | Page type |
|---|---|---|
| `render_repo_doc` / `build_repo_doc` | repo.rs | Repository overview (`code/repo`) |
| `render_module_doc` | pages.rs | Module page (`code_module`) |
| `render_file_doc` | pages.rs | File page (`code_file`) |
| `render_architecture_doc` | overview.rs | Architecture overview (`code_architecture`) |
| `render_onboarding_doc` | overview.rs | Onboarding guide |
| `render_hotspots_doc` | overview.rs | Hotspots page |
| `render_feature_catalog_doc` | features.rs | Feature catalog |
| `render_ghook_section` | features.rs | Git-hook section fragment |
| `render_infrastructure_doc` | infrastructure.rs | Infrastructure page |
| `render_deprecations_doc` | audit.rs | Deprecations audit |
| `render_dead_code_doc` | audit.rs | Dead-code audit |
| `collect_subsystem_dependency_edges` | diagrams.rs | Diagram edge data |

`build_repo_doc` in `repo.rs` is the most orchestration-heavy entry point: it filters `ModuleDoc` and `FileDoc` slices to top-level entries, checks a `ReusePlan` for an unchanged cached page, calls `maybe_generate` with a `TextGenerator` when regeneration is needed, and tracks progress via `CodewikiProgress` (repo.rs:4–70). The hotspot rendering in `overview.rs` decomposes into `write_hotspot_section` and `write_hotspot_section_with_cross_refs` to handle files with and without cross-reference metadata. `push_test_summary_line` in `pages.rs` appends a compact test-coverage line to file pages.

The module exposes no public API surface outside its crate; all symbols are `pub(crate)`. It does not own any I/O, AI generation, or data-fetching logic — those concerns stay in the parent `codewiki` module and are injected through the structured doc types and the `TextGenerator` / `ReusePlan` handles passed by reference into `build_repo_doc`.
[crates/gcode/src/commands/codewiki/render/audit.rs:8-57]
[crates/gcode/src/commands/codewiki/render/common.rs:1-7]
[crates/gcode/src/commands/codewiki/render/diagrams.rs:7-34]
[crates/gcode/src/commands/codewiki/render/features.rs:11-73]
[crates/gcode/src/commands/codewiki/render/infrastructure.rs:10-43]

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

