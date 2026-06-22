---
title: crates/gwiki/src/synthesis/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/synthesis/render.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/synthesis/render.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/synthesis/render.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gwiki/src/synthesis/render.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_frontmatter` | function | Writes a YAML frontmatter block into 'markdown' with escaped 'title', 'source_kind', 'compile_handoff', and 'synthesis_mode' fields, fixed 'gwiki'/'compiled' tags, and optional 'degraded' metadata listing nonempty 'degraded_sources', then terminates the block with '---' and a blank line. [crates/gwiki/src/synthesis/render.rs:3-37] |
| `render_source_excerpts` | function | Appends a markdown bullet list of accepted source titles and their first extracted chunk to 'markdown', or a fallback message when no sources or no body text are available. [crates/gwiki/src/synthesis/render.rs:39-57] |
| `render_list_section` | function | Appends a Markdown '##' heading for 'title' to 'markdown', then renders 'values' as a bullet list or '- None recorded.' if empty, followed by a trailing blank line. [crates/gwiki/src/synthesis/render.rs:59-73] |
| `yaml_scalar` | function | Returns a YAML double-quoted scalar by escaping backslashes, quotes, common control characters, and other control code points as YAML-compatible escape sequences, then wrapping the result in '"' delimiters. [crates/gwiki/src/synthesis/render.rs:75-93] |

