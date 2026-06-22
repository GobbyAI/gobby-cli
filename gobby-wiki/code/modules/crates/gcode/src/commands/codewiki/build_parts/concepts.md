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

## Module: `crates/gcode/src/commands/codewiki/build_parts/concepts`

This module is responsible for building the curated concepts layer of the codewiki — a user-facing navigation structure that sits above the raw grounded reference docs. Its core job is to take arrays of `FileDoc` and `ModuleDoc` records, ask a language model to organise them into concept modules, sections, and narrative pages, then render those groups into Markdown documents on disk. The pipeline runs in three broad phases: prompt construction and plan acquisition (`plan.rs`), source-span collection (`spans.rs`), and per-page rendering (`render.rs`), supported throughout by path/slug helpers (`support.rs`) and shared type definitions (`types.rs`).

The planning phase in `plan.rs` drives the LLM interaction. `curated_navigation_prompt` assembles a natural-language prompt from up to 40 modules and 80 representative files, requesting JSON that matches the `CuratedNavigationPlan` schema (plan.rs:5–36). `parse_plan` strips optional Markdown fences and deserialises the response; if parsing fails, `fallback_plan` synthesises a minimal plan directly from the input docs so rendering can still proceed (plan.rs:38–end). After the plan is obtained, the three `normalize_*` functions (`normalize_concepts`, `normalize_sections`, `normalize_narrative_pages`) cross-reference the plan's free-text references back to real module and file names before any rendering begins.

`render_curated_navigation_docs` in `render.rs` is the main entry point used by the parent `build_parts` layer (render.rs:9–18). It builds `module_lookup` and `file_lookup` maps, calls all three normalizers, then iterates over concepts and narrative pages to invoke `curated_content::curated_page_body` for each, storing the resulting body or flagging `body_degraded` when the content pass falls back to a structural skeleton (render.rs:35–65). Span helpers (`all_input_spans`, `item_spans`, `narrative_spans`) in `spans.rs` collect the source excerpt references that ground each page. Final per-page Markdown is produced by `render_concept_page`, `render_concept_tree`, `render_narrative_page`, `append_curated_body`, and `append_explore_section`. The module imports from the parent `curated_content` sibling and the grandparent wildcard re-export (`super::super::super::*`) for `FileDoc`, `ModuleDoc`, `LeadingChunk`, `BuiltDoc`, `TextGenerator`, `TextVerifier`, and `VerifyNote`.

### Public types (`types.rs`)

| Type | Key fields | Notes |
| --- | --- | --- |
| `CuratedNavigationPlan` | `concept_modules`, `sections`, `narrative_pages` | Top-level JSON-deserialisable plan |
| `ConceptModule` | `slug`, `title`, `summary`, `modules`, `files`, `body`, `body_degraded`, `verify_notes` | `body*` and `verify_notes` are `#[serde(skip)]`; populated post-normalisation |
| `ConceptSection` | `title`, `summary`, `concepts` | Groups concept titles under a heading |
| `NarrativePage` | `slug`, `title`, `summary`, `concepts`, `modules`, `files`, `body`, `body_degraded`, `verify_notes` | Same skip pattern as `ConceptModule` |

### Public API symbols by file

| File | Functions |
| --- | --- |
| `plan.rs` | `curated_navigation_prompt`, `parse_plan`, `fallback_plan`, `normalize_concepts`, `normalize_sections`, `normalize_narrative_pages`, `concept_key_map`, `narrative_page`, `narrative_extras_get_readable_ordinal_slugs`, `re_titled_extra_tracks_its_title_slug` |
| `render.rs` | `render_curated_navigation_docs`, `chapter_link`, `render_concept_tree`, `render_concept_page`, `render_narrative_page`, `append_curated_body`, `append_explore_section`, `narrative_members` |
| `spans.rs` | `all_input_spans`, `narrative_spans`, `item_spans` |
| `support.rs` | `degraded_sources`, `concept_title`, `concept_doc_path`, `concept_doc_stem`, `narrative_doc_path`, `slugify` |

### Path conventions (`support.rs`)

| Helper | Output pattern |
| --- | --- |
| `concept_doc_stem(slug)` | `code/concepts/{slug}` |
| `concept_doc_path(slug)` | `code/concepts/{slug}.md` |
| `narrative_doc_path(slug)` | `code/narrative/{slug}.md` |
| `concept_title(module_path)` | Title-cased last path segment, splitting on `_` and `-` |
| `slugify(value)` | Lowercase alphanumeric with `-` separators, no leading/trailing dashes |
| `degraded_sources(degraded)` | `["model-unavailable"]` when true, else empty vec |
[crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:6-38]
[crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:10-138]
[crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:4-13]
[crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:1-7]
[crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:6-13]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs` exposes 10 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs` exposes 4 indexed API symbols. |

