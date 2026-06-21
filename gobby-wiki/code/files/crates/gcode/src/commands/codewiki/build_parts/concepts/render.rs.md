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

`crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_curated_navigation_docs` | function | Generates curated documentation by normalizing input files and modules against a navigation plan and expanding concept/narrative summaries into multi-section bodies with optional text generation and verification. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:10-138] |
| `chapter_link` | function | This function extracts a 'NarrativePage''s slug and title fields and returns them as a tuple of string slices. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:141-143] |
| `render_concept_tree` | function | Produces a markdown-formatted string containing a hierarchical concept navigation document organized by ConceptSections with narrative chapter links and formatted cross-references to ConceptModules. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:145-191] |
| `render_concept_page` | function | Renders a ConceptModule into a formatted documentation string by composing frontmatter, curated body content, source file references, and exploration sections with optional degraded source handling. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:193-213] |
| `render_narrative_page` | function | 'render_narrative_page' generates a markdown-formatted documentation string by assembling a NarrativePage's frontmatter, title, body content, concept links, module exploration sections, and navigation metadata. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:215-257] |
| `append_curated_body` | function | Appends a trimmed non-empty body string to a mutable document with ensured trailing newlines, otherwise invokes 'write_section' with fallback heading and text. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:259-275] |
| `append_explore_section` | function | Appends a markdown "Explore" section to a mutable string document containing up to MAX_CURATED_KEY_COMPONENTS wikilinks, prioritizing modules over files. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:282-303] |
| `narrative_members` | function | Aggregates and returns deduplicated, lexicographically-sorted vectors of module and file names from a NarrativePage combined with those from its referenced ConceptModules. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:308-328] |

