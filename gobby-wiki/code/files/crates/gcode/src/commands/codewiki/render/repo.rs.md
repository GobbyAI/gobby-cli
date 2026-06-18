---
title: crates/gcode/src/commands/codewiki/render/repo.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render/repo.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/render/repo.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/render|crates/gcode/src/commands/codewiki/render]]

## Overview

`crates/gcode/src/commands/codewiki/render/repo.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/render/repo.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_repo_doc` | function | Builds the repository overview page by collecting top-level modules and root files into summary links, preparing fallback structural summary and source spans, and either reusing the existing 'code/repo.md' page when all provenance sources are unchanged or generating a new document. [crates/gcode/src/commands/codewiki/render/repo.rs:5-91] |
| `repo_source_excerpts` | function | Builds a prioritized list of source excerpts by selecting only top-level files, sorting README-like paths first then by descending symbol count and path, extracting leading chunks for each file path, and returning at most 'prompts::MAX_PROMPT_SOURCE_EXCERPTS' excerpts. [crates/gcode/src/commands/codewiki/render/repo.rs:96-116] |
| `render_repo_doc` | function | Builds a repository overview Markdown document by emitting frontmatter and source-file metadata, inserting a guided-tour intro and summary section with citations converted to markers, and optionally appending a reference appendix containing a module map plus module/file listings. [crates/gcode/src/commands/codewiki/render/repo.rs:118-193] |

