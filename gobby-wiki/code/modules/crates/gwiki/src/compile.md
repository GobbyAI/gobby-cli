---
title: crates/gwiki/src/compile
type: code_module
provenance:
- file: crates/gwiki/src/compile/collect.rs
- file: crates/gwiki/src/compile/index.rs
- file: crates/gwiki/src/compile/mod.rs
- file: crates/gwiki/src/compile/render.rs
- file: crates/gwiki/src/compile/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/compile

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

## Module: `crates/gwiki/src/compile`

The `compile` module is the synthesis-to-wiki pipeline for gwiki. It transforms a `ResearchSession` — including its set of accepted research notes — into a `CompileBundle` and, when a write intent is present, into rendered Obsidian-flavoured Markdown pages on disk. The module is split into three focused sub-files (`collect`, `index`, `render`) re-exported privately through `mod.rs`, which owns all public types and the two primary entry points: `prepare_handoff` (non-destructive bundling) and the full `wiki_compile` path (page writing plus index update). The compile process enforces path-scope safety at every step: notes outside the research scope root are rejected, and target-page paths that are absolute, escape via `..`, or traverse a symlinked parent are refused before any I/O occurs (`compile_rejects_absolute_or_escaping_target_pages`, `compile_rejects_target_page_through_symlinked_parent` — `tests.rs`).

`collect.rs` drives the first phase. `collect_accepted_sources` iterates every `AcceptedResearchNote` in the session, confirms the file exists and lies within `scope.root()` via `require_path_in_scope`, reads the raw Markdown, and delegates to `parse_note_sections` to extract structured fields (`ParsedNoteSections`). The helper `extend_unique` deduplicates citations, conflicting claims, and missing-evidence items across all notes before they are folded into the `CompileBundle` (`collect.rs:1-100`). `index.rs` handles the second phase: after a compiled page is written, `update_wiki_index` atomically appends or upserts a wiki-link under a `## Compiled pages` heading in `_index.md` at the vault root. Concurrent writers are serialised through a lock file at `.gwiki/state/index.lock`, with an advisory spin loop bounded by the `GWIKI_INDEX_LOCK_TIMEOUT_MS` environment variable (`index.rs:1-100`, `mod.rs:24-25`). `render.rs` supplies the final-form Markdown output consumed by `write_synthesized_page` from `crate::synthesis`.

The module integrates tightly with several sibling crates. It imports `ProvenanceGraph`, `ProvenanceLink`, `SourceChunkRef`, and `WikiSectionRef` from `crate::provenance`; citation helpers from `crate::citations`; `SynthesizedPage`, `write_synthesized_page`, and `synthesize_article` from `crate::synthesis`; and `ExplainerGenerator` / `build_explainer_prompt` / `generate_explainer` from `crate::explainer` (`mod.rs:1-23`). When an `ExplainerGenerator` is provided at compile time, it populates prose sections around the structural skeleton; if generation fails, the module degrades gracefully and preserves the skeleton without marking a hard failure (`compile_explainer_failure_degrades_and_keeps_structural_skeleton`, `tests.rs`). Sessions without a generator skip prose generation entirely without entering a degraded state (`compile_without_generator_stays_structural_without_degradation`, `tests.rs`).

### Public API types

| Type | Role |
| --- | --- |
| `CompileRequest` | Input: `topic`, `outline`, optional `target_page`, `write_intent` flag |
| `CompileBundle` | Intermediate bundle: accepted sources, citations, conflicts, missing evidence, path |
| `CompileOutcome` | Result of `prepare_handoff`: bundle + `CompileState` |
| `WikiCompileOptions` | Options: `target_kind` (`ArticleKind`), `daemon_synthesis_available` |
| `WikiCompileOutcome` | Full compile result: `article_path`, `source_paths`, `index_path`, `page_writes`, `prompt`, optional `explainer` |
| `AcceptedCompileSource` | Per-note container: `title`, `path`, `chunks`, `chunk_offsets` |
| `AcceptedCompileChunkOffset` | Byte/line offset metadata for a single accepted chunk |

### Key internal functions

| Symbol | File | Description |
| --- | --- | --- |
| `collect_accepted_sources` | `collect.rs` | Validates, reads, and parses all accepted notes into a `CollectedSources` value |
| `parse_note_sections` | `collect.rs` | Parses raw Markdown into `ParsedNoteSections` (citations, conflicts, gaps, body chunks) |
| `extend_unique` | `collect.rs` | Merges a `Vec` while preserving order and removing all duplicates |
| `require_path_in_scope` | `collect.rs` | Errors if a resolved path escapes the vault root |
| `update_wiki_index` | `index.rs` | Acquires lock, reads `_index.md`, upserts link, writes back |
| `insert_compiled_page_link` | `index.rs` | Appends link under `## Compiled pages`, creating the heading if absent |

### Configuration / environment

| Variable | Default | Purpose |
| --- | --- | --- |
| `GWIKI_INDEX_LOCK_TIMEOUT_MS` | `5000` | Maximum milliseconds to wait for the `index.lock` advisory lock (`mod.rs:24-25`) |
[crates/gwiki/src/compile/collect.rs:10-82]
[crates/gwiki/src/compile/index.rs:16-63]
[crates/gwiki/src/compile/mod.rs:30-35]
[crates/gwiki/src/compile/render.rs:11-47]
[crates/gwiki/src/compile/tests.rs:7-25]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/compile/collect.rs\|crates/gwiki/src/compile/collect.rs]] | `crates/gwiki/src/compile/collect.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/compile/index.rs\|crates/gwiki/src/compile/index.rs]] | `crates/gwiki/src/compile/index.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gwiki/src/compile/mod.rs\|crates/gwiki/src/compile/mod.rs]] | `crates/gwiki/src/compile/mod.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gwiki/src/compile/render.rs\|crates/gwiki/src/compile/render.rs]] | `crates/gwiki/src/compile/render.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/compile/tests.rs\|crates/gwiki/src/compile/tests.rs]] | `crates/gwiki/src/compile/tests.rs` exposes 16 indexed API symbols. |

