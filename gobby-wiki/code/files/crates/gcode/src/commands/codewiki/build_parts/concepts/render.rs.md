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

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_curated_navigation_docs` | function | The 'render_curated_navigation_docs' function normalizes a curated navigation plan into structured concepts, sections, and narrative pages using module and file metadata, expands each concept's summary into a grounded, multi-section body utilizing text generation and verification utilities, and returns a vector of built documentation structures. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:10-133] |
| `chapter_link` | function | The 'chapter_link' function takes a reference to a 'NarrativePage' and returns a tuple containing string slice representations of the page's slug and title, respectively. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:136-138] |
| `render_concept_tree` | function | The 'render_concept_tree' function constructs and returns a Markdown-formatted document string that serves as a curated concept navigation guide, incorporating frontmatter metadata, a guided tour of narrative chapters, and a hierarchical concept tree displaying section summaries and associated concept module links. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:140-186] |
| `render_concept_page` | function | The 'render_concept_page' function generates a Markdown-formatted string representing a concept page by constructing frontmatter, appending curated source file links and an overview header, embedding the concept body grounded in its summary, and adding an exploration section for its associated modules and files. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:188-208] |
| `render_narrative_page` | function | The 'render_narrative_page' function generates a Markdown-formatted document string by compiling frontmatter metadata, curated source links, grounded narrative body content, a list of associated concepts, exploration modules, and page navigation controls while accounting for content degradation. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:210-252] |
| `append_curated_body` | function | Appends the provided optional body string to a mutable document buffer with trailing newline formatting, falling back to writing a structured fallback section if the body is absent or whitespace-only. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:254-270] |
| `append_explore_section` | function | This function appends a markdown "Explore" section to a mutable string, formatting and listing up to 'MAX_CURATED_KEY_COMPONENTS' wikilinks derived from the provided slice of modules, or falling back to the provided slice of files if no module links are generated. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:277-298] |
| `narrative_members` | function | This function aggregates, sorts, and deduplicates the lists of modules and files defined directly within a 'NarrativePage' and those inherited from its matching 'ConceptModule's, returning them as a tuple of two vectors. [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:303-323] |

