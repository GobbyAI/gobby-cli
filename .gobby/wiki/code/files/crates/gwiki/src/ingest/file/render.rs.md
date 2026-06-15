---
title: crates/gwiki/src/ingest/file/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file/render.rs
  ranges:
  - 6-51
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/file/render.rs

Module: [[code/modules/crates/gwiki/src/ingest/file|crates/gwiki/src/ingest/file]]

## Purpose

Renders an ingested file into a markdown document. It first assembles source metadata front matter from the file kind, location, fetch time, hash, and optional asset path, then adds a title header and either inlines lossy UTF-8 text for Markdown, text, or stdin sources or emits a short note pointing to the stored artifact for other inputs. [crates/gwiki/src/ingest/file/render.rs:6-51]

## API Symbols

- `render_file_markdown` (function) component `render_file_markdown [function]` (`4564f049-6c18-59cd-9578-af3f8c0754c9`) lines 6-51 [crates/gwiki/src/ingest/file/render.rs:6-51]
  - Signature: `pub(super) fn render_file_markdown(`
  - Purpose: Builds a markdown document with source metadata front matter, a शीर्ष header, and either lossy UTF-8 text content for inline markdown/text/stdin sources or a placeholder note pointing to the stored artifact for non-inline sources. [crates/gwiki/src/ingest/file/render.rs:6-51]

