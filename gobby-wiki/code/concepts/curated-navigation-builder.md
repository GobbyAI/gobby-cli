---
title: Curated Navigation Builder
type: code_concept
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
- file: crates/gcode/src/commands/codewiki/build_parts/audit.rs
- file: crates/gcode/src/commands/codewiki/build_parts/changes.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs
- file: crates/gcode/src/commands/codewiki/build_parts/curated_content.rs
- file: crates/gcode/src/commands/codewiki/build_parts/features.rs
- file: crates/gcode/src/commands/codewiki/build_parts/file.rs
- file: crates/gcode/src/commands/codewiki/build_parts/hotspots.rs
- file: crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs
- file: crates/gcode/src/commands/codewiki/build_parts/modules.rs
- file: crates/gcode/src/commands/codewiki/build_parts/onboarding.rs
- file: crates/gcode/src/commands/codewiki/build_parts/snapshot.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
verify_notes:
- id: 5
  reason: Claims doc emission and planning scope not shown in the provided render.rs excerpt.
- id: 6
  reason: Cites architecture.rs and lists exclusions, but no supporting excerpt was provided.
- id: 10
  reason: '`final document emission` is not shown in the render.rs excerpt.'
- id: 17
  reason: The excerpt does not show storing degradation and verification fields back onto `ConceptModule`.
- id: 18
  reason: Narrative-page handling is not shown in the provided render.rs excerpt.
- id: 19
  reason: The narrative-page flow is not shown; only `CuratedPageKind` is evidenced.
- id: 21
  reason: '`append_curated_body` behavior is not shown in the provided excerpts.'
- id: 24
  reason: The `append_curated_body` row is unsupported because that symbol is not evidenced here.
- id: 26
  reason: '`emit built docs` is not shown in the provided render.rs excerpt.'
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/build_parts/architecture.rs](crates/gcode/src/commands/codewiki/build_parts/architecture.rs)
- [crates/gcode/src/commands/codewiki/build_parts/audit.rs](crates/gcode/src/commands/codewiki/build_parts/audit.rs)
- [crates/gcode/src/commands/codewiki/build_parts/changes.rs](crates/gcode/src/commands/codewiki/build_parts/changes.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts.rs](crates/gcode/src/commands/codewiki/build_parts/concepts.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs)
- [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs](crates/gcode/src/commands/codewiki/build_parts/curated_content.rs)
- [crates/gcode/src/commands/codewiki/build_parts/features.rs](crates/gcode/src/commands/codewiki/build_parts/features.rs)
- [crates/gcode/src/commands/codewiki/build_parts/file.rs](crates/gcode/src/commands/codewiki/build_parts/file.rs)

_5 more source files omitted._

</details>

# Curated Navigation Builder

## Purpose

The Curated Navigation Builder is the layer that turns the grounded codewiki reference into a more readable set of concept and narrative pages. Instead of duplicating source documentation, it plans user-facing concept modules, section groupings, and guided-tour chapters that link back to existing modules and files [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:6-38].

It solves the gap between exhaustive reference pages and newcomer comprehension. The structure pass names concepts and chapters with one-line summaries; the later content pass expands those into grounded multi-section bodies, while preserving deterministic fallback behavior when AI generation is off or unavailable .

## Covers / Does not cover

This concept covers the curated documentation layer: planning `concept_modules`, `sections`, and `narrative_pages`; normalizing those planned objects; generating or falling back to page bodies; and emitting concept and narrative docs on top of the existing reference wiki [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:10-133].

It does not cover the lower-level reference index itself, source parsing, hub schemas, or unrelated build-parts outputs such as audits, changes, hotspots, infrastructure, onboarding, snapshots, file pages, or module pages. Those live in the broader `build_parts` document-generation toolkit, while curated concepts are one specialized flow inside it [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-170].

## Architecture

The builder is split into a structure pass and a content/render pass. The structure pass lives in `concepts/plan.rs`: it builds a prompt from available `ModuleDoc` and `FileDoc` summaries, asks for JSON with `concept_modules`, `sections`, and `narrative_pages`, parses that JSON into `CuratedNavigationPlan`, and provides a fallback plan when generation cannot supply one [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:6-38].

The plan shape is defined in `concepts/types.rs`. `CuratedNavigationPlan` aggregates concepts, sections, and narrative pages with default-empty vectors so missing JSON fields do not break deserialization [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:6-13]. `ConceptModule` and `NarrativePage` contain serializable metadata from the planning pass, plus skipped fields for body text, degradation state, and verification notes that are populated later [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:16-37] [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:49-69].

Rendering lives in `concepts/render.rs`. It builds module and file lookup maps, normalizes concepts, sections, and narrative pages, computes source spans, then runs a per-page content pass before final document emission [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:10-133]. The per-page body logic is deliberately decoupled into `curated_content.rs`, which accepts primitive member lists and returns a `CuratedBody`; this keeps concept planning/rendering separate from content generation and fallback logic .

Small support helpers keep naming and path conventions centralized: concept docs are written under `code/concepts/{slug}.md`, narrative docs under `code/narrative/{slug}.md`, and degraded generation can be recorded as `model-unavailable` .

## Data flow

1. The builder starts from existing file and module documentation. `curated_navigation_prompt` formats up to 40 modules and 80 representative files into a prompt asking for JSON concept modules, sections, and narrative pages [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:6-38].

2. The raw model response is parsed by `parse_plan`. It trims optional Markdown JSON fences and deserializes into `CuratedNavigationPlan`; invalid JSON produces `None` rather than a partial plan .

3. If planning output is unavailable, `fallback_plan` builds a deterministic plan from modules that have direct files or child modules, bounded by the curated concept limits [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:52-100].

4. Rendering receives the plan and creates lookup maps for modules and files. It then normalizes concepts, sections, and narrative pages against the available reference data before attempting page-body generation [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:10-33].

5. For each concept, rendering computes item spans from the concept’s modules and files, calls `curated_page_body` with `CuratedPageKind::Concept`, then stores the returned body, degradation flag, and verification notes back onto the `ConceptModule` [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:34-100].

6. For each narrative page, the same content-pass pattern is used with narrative-specific inputs and `CuratedPageKind::Narrative`; `CuratedPageKind` selects whether the generated voice is a reference explainer or a guided-tour chapter .

7. If a content generation attempt fails, `CuratedBody.degraded` records that fallback was used. If AI is off, the structural body is the intended output and is not treated as degraded [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:34-44].

8. Final document assembly appends the generated body when present. If the body is absent or whitespace-only, `append_curated_body` writes a structured fallback section instead [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:254-270].

9. Rendered pages add navigation affordances such as “Explore” links for related modules or files, guided-tour chapter lists, previous/next tour navigation, and the fixed `gwiki ask` / `gwiki search` hint [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:277-298] .

## Key components

These are the central symbols to read as the smallest useful map of the feature.

| Symbol | Role |
| --- | --- |
| `CuratedNavigationPlan` | Top-level plan containing concept modules, sections, and narrative pages, with default-empty deserialization fields [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:6-13]. |
| `ConceptModule` | Planned concept page metadata plus post-normalization body, degradation state, and verification notes [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:16-37]. |
| `NarrativePage` | Guided-tour chapter metadata plus generated body state and verification notes [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:49-69]. |
| `CuratedBody` | Result of the per-page content pass: optional body text, degradation flag, and verification notes [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:34-44]. |
| `CuratedPageKind` | Selects whether a curated page is rendered as a concept explainer or narrative tour chapter [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:28-31]. |
| `append_curated_body` | Emits generated body text or a structured fallback when no usable body exists [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:254-270]. |

## Where to start

Start with `render_curated_navigation_docs` in `concepts/render.rs`, because it shows the whole runtime pipeline in one place: normalize the plan, compute spans, call the per-page body generator, and emit built docs [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:10-133].

After that, read `CuratedNavigationPlan`, `ConceptModule`, and `NarrativePage` in `concepts/types.rs` to understand the data model, then `curated_page_body` and `CuratedBody` in `curated_content.rs` to understand how the thin plan becomes grounded page content  [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:34-44].

## Explore

- [[code/modules/crates/gcode/src/commands/codewiki/build_parts/concepts|crates/gcode/src/commands/codewiki/build_parts/concepts]]
- [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

