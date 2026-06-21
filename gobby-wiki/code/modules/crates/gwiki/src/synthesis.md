---
title: crates/gwiki/src/synthesis
type: code_module
provenance:
- file: crates/gwiki/src/synthesis/generate.rs
- file: crates/gwiki/src/synthesis/paths.rs
- file: crates/gwiki/src/synthesis/render.rs
- file: crates/gwiki/src/synthesis/tests.rs
- file: crates/gwiki/src/synthesis/types.rs
- file: crates/gwiki/src/synthesis/write.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/synthesis

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

## crates/gwiki/src/synthesis

The `synthesis` module is responsible for turning structured research inputs into finished wiki pages. It owns the full pipeline from raw material assembly through LLM prompt construction, markdown rendering, safe path resolution, and atomic file writing. The module is organised into five collaborating files — `types`, `paths`, `generate`, `render`, and `write` — plus an integration test suite in `tests.rs`.

### Public API surface

| Symbol | Kind | File |
|---|---|---|
| `ArticleKind` | enum | types.rs:8 |
| `SynthesisSource` | struct | types.rs:36 |
| `SynthesisInput` | struct | types.rs:43 |
| `SynthesisPrompt` | struct | types.rs:54 |
| `SynthesizedPage` | struct | types.rs:62 |
| `WritePolicy` | enum | types.rs:69 |
| `PageWriteKind` | enum | types.rs:75 |
| `PageWriteOutcome` | struct | types.rs:82 |
| `synthesize_article` | fn | generate.rs |
| `write_synthesized_page` | fn | write.rs:32 |
| `ensure_page_write_allowed` | fn | write.rs:14 |
| `slugify_unique` | fn | paths.rs |

### Article kinds and vault layout

`ArticleKind` controls which subdirectory a page lands in and the `source_kind` front-matter field injected by the renderer (types.rs:8–32).

| Variant | Directory | source\_kind |
|---|---|---|
| `Source` | `knowledge/sources` | `source_note` |
| `Concept` | `knowledge/concepts` | `concept` |
| `Topic` | `knowledge/topics` | `topic` |

### Core data flow

Callers assemble a `SynthesisInput` (types.rs:43) carrying the `handoff_id`, `topic`, outline bullet points, accepted `SynthesisSource` chunks, citation strings, conflicting-claims notes, and missing-evidence annotations. `generate.rs` consumes that struct, builds a `SynthesisPrompt` (types.rs:54) that records the rendered `system`/`user` strings, a `daemon_synthesis_available` flag, an estimated token count, and the number of sources that were truncated to fit the context window, then calls out to the LLM layer. The resulting markdown comes back as a `SynthesizedPage` (types.rs:62), which adds the resolved `path`, `title`, normalised `markdown`, and an optional `ExplainerReport` (absent for source notes, present for compiled concept/topic pages).

### Path safety and write policy

`paths.rs` enforces that every path produced by synthesis stays inside the vault root. `ensure_synthesized_path_inside_vault` (paths.rs:9) canonicalises the existing path prefix via `canonicalize_existing_prefix` (paths.rs:40) and rejects any result that escapes the vault via `..`, absolute segments, or prefix components. `ensure_existing_parent_inside_vault` (paths.rs:65) applies the same guard to the target directory before `fs::create_dir_all` is called.

`write.rs` enforces two write modes through `WritePolicy`:

| Variant | Behaviour |
|---|---|
| `RequireMergeIntent` | Opens with `create_new(true)`; fails with `WikiError::InvalidInput { field: "write_intent" }` if the file already exists (write.rs:47–65) |
| `AllowOverwriteAfterMerge` | Performs an atomic replacement; classifies the outcome as `PageWriteKind::Created` or `PageWriteKind::Overwritten` |

`ensure_page_write_allowed` (write.rs:14) is an advisory preflight for callers who want to surface conflicts before spending tokens on synthesis; the race-free protection lives inside `write_synthesized_page` itself. `write_synthesized_page` also normalises whitespace via `crate::markdown::normalize` before writing (write.rs:33).

### Test coverage

`tests.rs` imports directly from the module's public surface (tests.rs:8–11) and exercises three invariants: that `RequireMergeIntent` leaves an existing file untouched and returns the correct error field (tests.rs:14–43); that `AllowOverwriteAfterMerge` correctly classifies first-write vs. overwrite outcomes (tests.rs:45–68); and that `slugify_unique` terminates within `MAX_SLUG_TRIES` (paths.rs:8) even when every candidate collides, returning a bounded fallback slug.
[crates/gwiki/src/synthesis/generate.rs:13-100]
[crates/gwiki/src/synthesis/paths.rs:10-38]
[crates/gwiki/src/synthesis/render.rs:3-37]
[crates/gwiki/src/synthesis/tests.rs:15-42]
[crates/gwiki/src/synthesis/types.rs:9-13]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/synthesis/generate.rs\|crates/gwiki/src/synthesis/generate.rs]] | `crates/gwiki/src/synthesis/generate.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis/paths.rs\|crates/gwiki/src/synthesis/paths.rs]] | `crates/gwiki/src/synthesis/paths.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis/render.rs\|crates/gwiki/src/synthesis/render.rs]] | `crates/gwiki/src/synthesis/render.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis/tests.rs\|crates/gwiki/src/synthesis/tests.rs]] | `crates/gwiki/src/synthesis/tests.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis/types.rs\|crates/gwiki/src/synthesis/types.rs]] | `crates/gwiki/src/synthesis/types.rs` exposes 10 indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis/write.rs\|crates/gwiki/src/synthesis/write.rs]] | `crates/gwiki/src/synthesis/write.rs` exposes 6 indexed API symbols. |

