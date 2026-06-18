---
title: Build Parts
type: code_concept
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
- file: crates/gcode/src/commands/codewiki/build_parts/changes.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs
- file: crates/gcode/src/commands/codewiki/build_parts/curated_content.rs
- file: crates/gcode/src/commands/codewiki/build_parts/file.rs
- file: crates/gcode/src/commands/codewiki/build_parts/hotspots.rs
- file: crates/gcode/src/commands/codewiki/build_parts/modules.rs
- file: crates/gcode/src/commands/codewiki/build_parts/onboarding.rs
- file: crates/gcode/src/commands/codewiki/build_parts/snapshot.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/build_parts/architecture.rs](crates/gcode/src/commands/codewiki/build_parts/architecture.rs)
- [crates/gcode/src/commands/codewiki/build_parts/changes.rs](crates/gcode/src/commands/codewiki/build_parts/changes.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts.rs](crates/gcode/src/commands/codewiki/build_parts/concepts.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs)
- [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs](crates/gcode/src/commands/codewiki/build_parts/curated_content.rs)
- [crates/gcode/src/commands/codewiki/build_parts/file.rs](crates/gcode/src/commands/codewiki/build_parts/file.rs)
- [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs](crates/gcode/src/commands/codewiki/build_parts/hotspots.rs)
- [crates/gcode/src/commands/codewiki/build_parts/modules.rs](crates/gcode/src/commands/codewiki/build_parts/modules.rs)

_2 more source files omitted._

</details>

# Build Parts

## Purpose

Build Parts groups the related modules and files listed below; read the key components for the grounded detail.

## Key components

| Symbol | Kind | Source | Role |
| --- | --- | --- | --- |
| ChangesFrontmatter | class | [crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113] | 'ChangesFrontmatter' is a borrowed frontmatter record that captures change-metadata fields for a document, including title, kind, generator, trust and freshness status, a baseline/degraded flag pair, and a list of degraded sources. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113] |
| CuratedBody | class | [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:34-43] | 'CuratedBody' is a crate-visible container for the generated page body text and a 'degraded' flag that records whether content-pass generation failed and the output fell back to the structural body. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:34-43] |
| CuratedPageKind | type | [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:28-31] | Indexed type `CuratedPageKind` in `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs`. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:28-31] |
| FileDocPosition | class | [crates/gcode/src/commands/codewiki/build_parts/file.rs:13-16] | 'FileDocPosition' is a crate-visible struct that stores a document’s zero-based 'index' and its 'total' count as 'usize' values. [crates/gcode/src/commands/codewiki/build_parts/file.rs:13-16] |
| append_ask_hint | function | [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:278-282] | Appends a fixed help hint to the provided document string, instructing the user to use 'gwiki ask' to query the vault and 'gwiki search' to locate pages. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:278-282] |
| append_guided_tour | function | [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:262-275] | Appends a “Start here” guided-tour section to the document by adding a heading, an optional introductory link to the first chapter, an enumerated list of chapter links, a trailing blank line, and the standard ask-hint footer. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:262-275] |
| append_tour_nav | function | [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:287-303] | Appends a “Continue the tour” navigation section to 'doc' with optional previous and next narrative links formatted as wiki-style list items, and leaves 'doc' unchanged when both are absent. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:287-303] |
| build_architecture_doc | function | [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169] | Constructs an 'ArchitectureDoc' by identifying subsystem roots from file paths, marking graph data as degraded when truncated or unavailable, and then iterating over matching subsystem modules to assemble subsystem-level summaries and structure for the document. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169] |
| build_codewiki_changes_doc | function | [crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101] | Generates a markdown change report for a 'CodewikiIndexSnapshot', including frontmatter status, current snapshot counts, and, when a previous snapshot exists, lists of added, removed, and modified files and symbols. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101] |
| build_curated_navigation_docs | function | [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:35-85] | Builds curated navigation documentation by reusing previously generated pages when source spans are unchanged, otherwise generating or falling back to a navigation plan and rendering the resulting docs with optional verification and degraded-mode tracking. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:35-85] |
| build_file_body | function | [crates/gcode/src/commands/codewiki/build_parts/file.rs:172-230] | Build_file_body conditionally generates an aggregate file narrative from either content or symbol evidence, verifies and grounds the generated text against source spans with citations, and falls back to 'structural_file_body' while marking 'degraded' on generation or verification failure. [crates/gcode/src/commands/codewiki/build_parts/file.rs:172-230] |
| build_file_doc | function | [crates/gcode/src/commands/codewiki/build_parts/file.rs:19-162] | Builds a 'FileDoc' for a source file by optionally reusing a cached page summary, emitting progress, and generating or skipping per-symbol documentation and verification work according to 'ai_depth' and the provided generator/verifier/reuse plans. [crates/gcode/src/commands/codewiki/build_parts/file.rs:19-162] |

## Members

- `crates/gcode/src/commands/codewiki/build_parts` (module) [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169]
- `crates/gcode/src/commands/codewiki/build_parts/architecture.rs` (file) [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169]
- `crates/gcode/src/commands/codewiki/build_parts/changes.rs` (file) [crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101]
- `crates/gcode/src/commands/codewiki/build_parts/concepts.rs` (file) [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:35-85]
- `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs` (file) [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:28-31]
- `crates/gcode/src/commands/codewiki/build_parts/file.rs` (file) [crates/gcode/src/commands/codewiki/build_parts/file.rs:13-16]
- `crates/gcode/src/commands/codewiki/build_parts/hotspots.rs` (file) [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-134]


## Explore

- [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

