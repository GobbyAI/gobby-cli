---
title: crates/gcode/src/commands/codewiki/render/pages.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render/pages.rs
  ranges:
  - 6-72
  - 74-133
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/render/pages.rs:6-72](crates/gcode/src/commands/codewiki/render/pages.rs#L6-L72), [crates/gcode/src/commands/codewiki/render/pages.rs:74-133](crates/gcode/src/commands/codewiki/render/pages.rs#L74-L133)

</details>

# crates/gcode/src/commands/codewiki/render/pages.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/render|crates/gcode/src/commands/codewiki/render]]

## Purpose

Builds CodeWiki page text for module and file documentation. `render_module_doc` assembles a module page with frontmatter, linked source files, headings, parent navigation, summary, dependency and call diagrams, and tables for child modules and direct files, while `render_file_doc` does the same for a single file by combining its metadata, source context, summary, and related links into the final markdown output.
[crates/gcode/src/commands/codewiki/render/pages.rs:6-72]
[crates/gcode/src/commands/codewiki/render/pages.rs:74-133]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `render_module_doc` | function | `pub(crate) fn render_module_doc(module: &ModuleDoc) -> String {` | `render_module_doc [function]` | `1b8187f4-6e9a-5ef2-8abf-135f44de6a76` | 6-72 [crates/gcode/src/commands/codewiki/render/pages.rs:6-72] | Indexed function `render_module_doc` in `crates/gcode/src/commands/codewiki/render/pages.rs`. [crates/gcode/src/commands/codewiki/render/pages.rs:6-72] |
| `render_file_doc` | function | `pub(crate) fn render_file_doc(file: &FileDoc) -> String {` | `render_file_doc [function]` | `4054dafa-79aa-5928-8d06-3cb6d27221a4` | 74-133 [crates/gcode/src/commands/codewiki/render/pages.rs:74-133] | Indexed function `render_file_doc` in `crates/gcode/src/commands/codewiki/render/pages.rs`. [crates/gcode/src/commands/codewiki/render/pages.rs:74-133] |
