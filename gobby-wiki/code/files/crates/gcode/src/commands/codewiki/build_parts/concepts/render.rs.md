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

`crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_curated_navigation_docs` | function | Normalizes the curated navigation plan against the supplied file/module docs, generates grounded bodies for curated pages using the optional text generator/verifier, and returns the resulting 'BuiltDoc' list. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:12-138] |
| `chapter_link` | function | Returns a tuple of string slices containing the page’s slug and title, in that order. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:141-143] |
| `render_concept_tree` | function | Builds and returns a markdown document titled “Curated Concept Navigation” by adding frontmatter and curated source links, inserting a guided tour of narrative chapters, and then emitting each concept section with linked concepts and summaries in section order. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:145-191] |
| `render_concept_page` | function | Builds and returns a Markdown concept page by merging degradation state, adding frontmatter and curated source links, emitting the title, appending the curated body overview, optional dependency diagram, and explore section for the concept’s modules and files. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:193-218] |
| `render_narrative_page` | function | Builds and returns a markdown narrative page string by assembling frontmatter, curated source links and body text, an optional concepts list with title lookup, an optional dependency diagram, an explore section, and previous/next tour navigation, while propagating degradation metadata from the page. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:220-263] |
| `append_curated_body` | function | Appends a non-empty 'body' string to 'doc', ensuring it ends with two newlines, or otherwise appends a fallback section built from 'fallback_heading' and 'fallback_text' via 'write_section'. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:265-281] |
| `append_explore_section` | function | Appends an '## Explore' section to 'doc' containing up to 'MAX_CURATED_KEY_COMPONENTS' wiki links for 'modules', or if none exist, for 'files', and returns without modification if both inputs yield no links. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:288-309] |
| `narrative_members` | function | Returns the deduplicated, sorted union of a narrative page’s own 'modules' and 'files' with those from any referenced concepts whose 'slug' matches 'page.concepts', preserving only discovered concept entries. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:314-334] |
| `append_dependency_diagram` | function | Appends an "Architecture diagram" section to 'doc' containing the module's dependency diagram, but only when 'module' exists, has a diagram, and graph availability is not 'Unavailable', adding a 'degraded: graph-truncated' marker first if availability is 'Truncated'. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:340-356] |

