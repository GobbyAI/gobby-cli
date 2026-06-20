---
title: crates/gcode/src/commands/codewiki/build_parts/concepts
type: code_module
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/concepts

Parent: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

This module builds the curated “concepts” navigation layer for codewiki. It defines the JSON plan shape for concept modules, sections, and narrative pages, then turns file/module summaries into a prompt, parses model output, and provides fallback planning when needed (`plan.rs:1-43`, `types.rs:5-70`). Rendering normalizes the plan, expands each concept/narrative summary into grounded page bodies, and emits built documentation, tracking degraded body generation and verification notes (`render.rs:9-33`, `types.rs:20-31`, `types.rs:56-69`).

The main flow starts with `curated_navigation_prompt`, which asks for JSON containing `concept_modules`, `sections`, and `narrative_pages`, seeded from available modules and representative files (`plan.rs:6-35`). `parse_plan` accepts either raw JSON or fenced JSON and deserializes it into `CuratedNavigationPlan` (`plan.rs:41-51`). `render_curated_navigation_docs` then builds module/file lookups, normalizes concepts, sections, and narrative pages, gathers spans, and calls `curated_content::curated_page_body` for each page using generator/verifier collaborators (`render.rs:1-7`, `render.rs:16-39`).

Collaboration is mostly internal to the codewiki build pipeline: this module imports shared build types from its grandparent, imports curated page generation from `curated_content`, uses local `plan`, `spans`, `support`, and `types` helpers, and returns `BuiltDoc` pages to its caller (`render.rs:1-9`). Support functions provide deterministic names, slugs, output paths, and degradation metadata so generated concept and narrative pages stay stable even when model-backed content is unavailable (`support.rs:1-54`).

| Symbol | Kind | Responsibility |
| --- | --- | --- |
| `CuratedNavigationPlan` | struct | Holds concept modules, sections, and narrative pages (`types.rs:5-15`) |
| `ConceptModule` | struct | Represents a concept page plus linked modules/files and generated body state (`types.rs:17-35`) |
| `ConceptSection` | struct | Groups concepts under a user-facing section (`types.rs:37-44`) |
| `NarrativePage` | struct | Represents chapter-style narrative docs linked to concepts/modules/files (`types.rs:46-70`) |
| `render_curated_navigation_docs` | function | Renders normalized curated navigation docs into `BuiltDoc` output (`render.rs:9-18`) |
| `curated_navigation_prompt` | function | Builds the model prompt for navigation planning (`plan.rs:6-39`) |
| `parse_plan` | function | Parses raw or fenced JSON into a plan (`plan.rs:41-51`) |
| `concept_doc_path` / `narrative_doc_path` | functions | Produce concept and narrative Markdown paths (`support.rs:25-35`) |
| `slugify` | function | Converts display text into stable ASCII slugs (`support.rs:37-53`) |
[crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:6-38]
[crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:10-133]
[crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:4-13]
[crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:1-7]
[crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:6-13]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs` exposes 4 indexed API symbols. |

