---
title: crates/gcode/src/commands/codewiki/render/repo.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render/repo.rs
  ranges:
  - 5-91
  - 96-116
  - 118-172
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/render/repo.rs:5-91](crates/gcode/src/commands/codewiki/render/repo.rs#L5-L91), [crates/gcode/src/commands/codewiki/render/repo.rs:96-116](crates/gcode/src/commands/codewiki/render/repo.rs#L96-L116), [crates/gcode/src/commands/codewiki/render/repo.rs:118-172](crates/gcode/src/commands/codewiki/render/repo.rs#L118-L172)

</details>

# crates/gcode/src/commands/codewiki/render/repo.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/render|crates/gcode/src/commands/codewiki/render]]

## Purpose

Builds and renders the repository-level Codewiki overview. `build_repo_doc` collects top-level modules and root files, assembles summaries and source spans, reuses a cached page when the repo’s provenance is unchanged, otherwise generates the overview from a repo prompt and source excerpts. `repo_source_excerpts` gathers the source snippets fed into that prompt, and `render_repo_doc` turns the resulting document into the final rendered repo page.
[crates/gcode/src/commands/codewiki/render/repo.rs:5-91]
[crates/gcode/src/commands/codewiki/render/repo.rs:96-116]
[crates/gcode/src/commands/codewiki/render/repo.rs:118-172]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `build_repo_doc` | function | `pub(crate) fn build_repo_doc(` | `build_repo_doc [function]` | `4e5c8df9-7942-5e59-a2f5-1aac2dc17fad` | 5-91 [crates/gcode/src/commands/codewiki/render/repo.rs:5-91] | Indexed function `build_repo_doc` in `crates/gcode/src/commands/codewiki/render/repo.rs`. [crates/gcode/src/commands/codewiki/render/repo.rs:5-91] |
| `repo_source_excerpts` | function | `fn repo_source_excerpts(` | `repo_source_excerpts [function]` | `d7299570-8cf6-5084-8a99-8973bda5f280` | 96-116 [crates/gcode/src/commands/codewiki/render/repo.rs:96-116] | Indexed function `repo_source_excerpts` in `crates/gcode/src/commands/codewiki/render/repo.rs`. [crates/gcode/src/commands/codewiki/render/repo.rs:96-116] |
| `render_repo_doc` | function | `pub(crate) fn render_repo_doc(` | `render_repo_doc [function]` | `5bac84e0-5092-5474-ac4d-91d656324116` | 118-172 [crates/gcode/src/commands/codewiki/render/repo.rs:118-172] | Indexed function `render_repo_doc` in `crates/gcode/src/commands/codewiki/render/repo.rs`. [crates/gcode/src/commands/codewiki/render/repo.rs:118-172] |
