---
title: crates/gwiki/src/synthesis/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/synthesis/render.rs
  ranges:
  - 3-37
  - 39-57
  - 59-73
  - 75-93
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/synthesis/render.rs:3-37](crates/gwiki/src/synthesis/render.rs#L3-L37), [crates/gwiki/src/synthesis/render.rs:39-57](crates/gwiki/src/synthesis/render.rs#L39-L57), [crates/gwiki/src/synthesis/render.rs:59-73](crates/gwiki/src/synthesis/render.rs#L59-L73), [crates/gwiki/src/synthesis/render.rs:75-93](crates/gwiki/src/synthesis/render.rs#L75-L93)

</details>

# crates/gwiki/src/synthesis/render.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file contains helper renderers for building synthesis markdown output. `render_frontmatter` writes the YAML header with title, source kind, compile handoff ID, synthesis mode, fixed tags, and optional degraded-source metadata; `render_source_excerpts` emits either a fallback note or a bullet list of accepted source titles with their first extracted chunk; `render_list_section` formats named sections as markdown lists with a `None recorded` fallback; and `yaml_scalar` escapes string values so frontmatter fields can be safely embedded as YAML scalars.
[crates/gwiki/src/synthesis/render.rs:3-37]
[crates/gwiki/src/synthesis/render.rs:39-57]
[crates/gwiki/src/synthesis/render.rs:59-73]
[crates/gwiki/src/synthesis/render.rs:75-93]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `render_frontmatter` | function | `pub(super) fn render_frontmatter(` | `render_frontmatter [function]` | `13e54dbd-8af5-5b39-b995-b8669f055ea5` | 3-37 [crates/gwiki/src/synthesis/render.rs:3-37] | Indexed function `render_frontmatter` in `crates/gwiki/src/synthesis/render.rs`. [crates/gwiki/src/synthesis/render.rs:3-37] |
| `render_source_excerpts` | function | `pub(super) fn render_source_excerpts(markdown: &mut String, sources: &[SynthesisSource]) {` | `render_source_excerpts [function]` | `dbf2584a-c570-5cf9-b80c-860b50707bd8` | 39-57 [crates/gwiki/src/synthesis/render.rs:39-57] | Indexed function `render_source_excerpts` in `crates/gwiki/src/synthesis/render.rs`. [crates/gwiki/src/synthesis/render.rs:39-57] |
| `render_list_section` | function | `pub(super) fn render_list_section(markdown: &mut String, title: &str, values: &[String]) {` | `render_list_section [function]` | `e443c3fa-b93b-52b9-bf71-4b2227ad2a45` | 59-73 [crates/gwiki/src/synthesis/render.rs:59-73] | Indexed function `render_list_section` in `crates/gwiki/src/synthesis/render.rs`. [crates/gwiki/src/synthesis/render.rs:59-73] |
| `yaml_scalar` | function | `pub(super) fn yaml_scalar(value: &str) -> String {` | `yaml_scalar [function]` | `e51004e1-278a-56d8-b5c2-3614bd320813` | 75-93 [crates/gwiki/src/synthesis/render.rs:75-93] | Indexed function `yaml_scalar` in `crates/gwiki/src/synthesis/render.rs`. [crates/gwiki/src/synthesis/render.rs:75-93] |
