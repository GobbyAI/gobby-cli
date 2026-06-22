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

`crates/gcode/src/commands/codewiki/render/repo.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_repo_doc` | function | # Summary 'build_repo_doc' generates a repository overview document by aggregating top-level file and module documentation, with source-aware provenance caching to conditionally reuse previously-generated content when source files are unchanged. [crates/gcode/src/commands/codewiki/render/repo.rs:4-83] |
| `repo_source_excerpts` | function | This function filters repository files with empty modules, sorts them by README priority and descending symbol count, and returns up to MAX_PROMPT_SOURCE_EXCERPTS source excerpts extracted from the prioritized files. [crates/gcode/src/commands/codewiki/render/repo.rs:88-108] |
| `render_repo_doc` | function | # Summary 'render_repo_doc' generates a markdown String for a code repository overview document with guided narrative tour chapters, source-span-annotated summary content, and audit catalogs. [crates/gcode/src/commands/codewiki/render/repo.rs:110-193] |

