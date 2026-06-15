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

# crates/gwiki/src/synthesis/render.rs

Module: [[code/modules/crates/gwiki/src/synthesis|crates/gwiki/src/synthesis]]

## Purpose

This file provides helper routines for rendering synthesis output into Markdown. `render_frontmatter` writes a YAML frontmatter block with escaped metadata fields, fixed `gwiki` and `compiled` tags, and optional degraded-source markers; `render_source_excerpts` emits a bullet list of accepted sources and their first extracted chunk, or a fallback message when none exist; `render_list_section` formats titled `##` sections for string lists with a “None recorded” fallback; and `yaml_scalar` supplies the safe YAML string escaping used by the frontmatter writer.
[crates/gwiki/src/synthesis/render.rs:3-37]
[crates/gwiki/src/synthesis/render.rs:39-57]
[crates/gwiki/src/synthesis/render.rs:59-73]
[crates/gwiki/src/synthesis/render.rs:75-93]

## API Symbols

- `render_frontmatter` (function) component `render_frontmatter [function]` (`13e54dbd-8af5-5b39-b995-b8669f055ea5`) lines 3-37 [crates/gwiki/src/synthesis/render.rs:3-37]
  - Signature: `pub(super) fn render_frontmatter(`
  - Purpose: Appends a YAML frontmatter block to the given Markdown buffer containing escaped 'title', 'source_kind', 'compile_handoff', and 'synthesis_mode' fields, fixed 'gwiki' and 'compiled' tags, and optional 'degraded'/'degraded_sources' entries when any degraded sources are provided. [crates/gwiki/src/synthesis/render.rs:3-37]
- `render_source_excerpts` (function) component `render_source_excerpts [function]` (`dbf2584a-c570-5cf9-b80c-860b50707bd8`) lines 39-57 [crates/gwiki/src/synthesis/render.rs:39-57]
  - Signature: `pub(super) fn render_source_excerpts(markdown: &mut String, sources: &[SynthesisSource]) {`
  - Purpose: Appends a Markdown bullet list of each 'SynthesisSource' title and its first extracted chunk to 'markdown', or a fixed no-sources/no-body message when the input is empty or a source has no chunks. [crates/gwiki/src/synthesis/render.rs:39-57]
- `render_list_section` (function) component `render_list_section [function]` (`e443c3fa-b93b-52b9-bf71-4b2227ad2a45`) lines 59-73 [crates/gwiki/src/synthesis/render.rs:59-73]
  - Signature: `pub(super) fn render_list_section(markdown: &mut String, title: &str, values: &[String]) {`
  - Purpose: Appends a Markdown '##' section header with the given title to 'markdown', then writes either '- None recorded.' if 'values' is empty or one bullet per string value followed by a trailing blank line. [crates/gwiki/src/synthesis/render.rs:59-73]
- `yaml_scalar` (function) component `yaml_scalar [function]` (`e51004e1-278a-56d8-b5c2-3614bd320813`) lines 75-93 [crates/gwiki/src/synthesis/render.rs:75-93]
  - Signature: `pub(super) fn yaml_scalar(value: &str) -> String {`
  - Purpose: Returns a double-quoted YAML scalar string with backslashes, quotes, and control characters escaped using YAML/JSON-style escape sequences, including '\uXXXX' for remaining control code points. [crates/gwiki/src/synthesis/render.rs:75-93]

