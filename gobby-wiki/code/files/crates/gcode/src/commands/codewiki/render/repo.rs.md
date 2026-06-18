---
title: crates/gcode/src/commands/codewiki/render/repo.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render/repo.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/render/repo.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/render|crates/gcode/src/commands/codewiki/render]]

## Overview

The file crates/gcode/src/commands/codewiki/render/repo.rs is responsible for building and rendering the repository-level overview page in the CodeWiki document generation process. This overview provides a structured entry point for the codebase, serving as a guided tour for engineers exploring the repository.

The primary entry point is the build_repo_doc function at crates/gcode/src/commands/codewiki/render/repo.rs:5-91, which checks if all source files are unchanged and attempts to reuse the existing code/repo.md page. If changes are detected, it compiles structured summaries of root modules and files, and generates a new overview document.

## How it fits

This file fits into the broader CodeWiki rendering subsystem by pulling in utilities and parent-level types imported at crates/gcode/src/commands/codewiki/render/repo.rs:1-3. It sits at the top of the render pipeline, orchestrating repository-wide metadata rather than detailing individual submodules or files.

Data flows into build_repo_doc in the form of completed FileDoc and ModuleDoc lists. The function filters these collections to extract top-level modules where parent_module is none at crates/gcode/src/commands/codewiki/render/repo.rs:13-21, and root-level files that belong to no submodule at crates/gcode/src/commands/codewiki/render/repo.rs:22-30.
[crates/gcode/src/commands/codewiki/render/repo.rs:5-91]
[crates/gcode/src/commands/codewiki/render/repo.rs:96-116]
[crates/gcode/src/commands/codewiki/render/repo.rs:118-193]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_repo_doc` | function | Builds the repository overview page by collecting top-level modules and root files into summary links, preparing fallback structural summary and source spans, and either reusing the existing 'code/repo.md' page when all provenance sources are unchanged or generating a new document. [crates/gcode/src/commands/codewiki/render/repo.rs:5-91] |
| `repo_source_excerpts` | function | Builds a prioritized list of source excerpts by selecting only top-level files, sorting README-like paths first then by descending symbol count and path, extracting leading chunks for each file path, and returning at most 'prompts::MAX_PROMPT_SOURCE_EXCERPTS' excerpts. [crates/gcode/src/commands/codewiki/render/repo.rs:96-116] |
| `render_repo_doc` | function | Builds a repository overview Markdown document by emitting frontmatter and source-file metadata, inserting a guided-tour intro and summary section with citations converted to markers, and optionally appending a reference appendix containing a module map plus module/file listings. [crates/gcode/src/commands/codewiki/render/repo.rs:118-193] |

