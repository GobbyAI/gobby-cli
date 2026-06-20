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
| `build_repo_doc` | function | This function compiles a repository-level overview document by filtering and mapping top-level modules and root-level files, returning a cached on-disk page verbatim from a reuse plan if the underlying source spans are unchanged, or otherwise preparing to generate a new overview. [crates/gcode/src/commands/codewiki/render/repo.rs:4-75] |
| `repo_source_excerpts` | function | The 'repo_source_excerpts' function filters a list of files for those with empty module names, sorts them prioritizing README files followed by descending symbol count and lexicographical path, and then maps the top candidates to a limited vector of source excerpts using a leading chunks lookup map. [crates/gcode/src/commands/codewiki/render/repo.rs:80-100] |
| `render_repo_doc` | function | The 'render_repo_doc' function constructs a Markdown-formatted repository overview document containing metadata frontmatter, a guided narrative tour, a citation-processed summary, and a reference appendix listing modules and files. [crates/gcode/src/commands/codewiki/render/repo.rs:102-174] |

