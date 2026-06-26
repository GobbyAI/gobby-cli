---
title: crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts/concepts|crates/gcode/src/commands/codewiki/build_parts/concepts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs` exposes 15 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_curated_navigation_docs` | function | 'render_curated_navigation_docs' renders curated documentation by normalizing a navigation plan and expanding concept/page summaries into multi-section content bodies using optional text generation and verification. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:10-161] |
| `chapter_link` | function | Returns a tuple of string slices containing a 'NarrativePage''s slug and title fields. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:164-166] |
| `render_concept_tree` | function | # Summary Generates a markdown string rendering a hierarchical concept tree organized by sections with narrative chapters as entry points and concept module references. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:168-214] |
| `render_concept_page` | function | Renders a concept documentation page by sequentially assembling frontmatter metadata, curated source file links, title heading, overview body content, optional flow diagrams, and an exploration section of related modules and files into a single string document. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:216-244] |
| `render_narrative_page` | function | Converts a 'NarrativePage' struct into a markdown-formatted 'String' by composing the page title, curated body content, concept links (with title mapping), module exploration section, and tour navigation with source span validation and degradation metadata. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:246-292] |
| `append_curated_body` | function | Appends a body string to a document after stripping its leading H1 heading, or writes a fallback section if the body is absent or empty. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:294-314] |
| `strip_leading_model_h1` | function | Strips a leading markdown H1 heading (single '#' with up to 3 spaces indentation) and any trailing blank lines from the input string, returning the remainder or the original string if no valid H1 is found. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:327-351] |
| `append_explore_section` | function | This function appends a markdown "## Explore" section to a document string, populated with up to MAX_CURATED_KEY_COMPONENTS wikilinks derived from the modules array, or the files array as a fallback, formatted as a markdown list. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:358-379] |
| `narrative_members` | function | Aggregates and returns deduplicated, sorted modules and files from a NarrativePage and its referenced ConceptModules. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:384-404] |

_Verified by 6 in-file unit tests._

