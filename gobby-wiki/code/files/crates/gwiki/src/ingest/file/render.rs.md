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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/file/render.rs:6-51](crates/gwiki/src/ingest/file/render.rs#L6-L51)

</details>

# crates/gwiki/src/ingest/file/render.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Builds a Markdown representation of an ingested file, attaching source metadata, a title heading, and either the decoded text content or a note about where the original artifact was stored. It assembles the front matter from source kind, location, fetch time, hash, and optional asset path, then switches behavior based on file type and whether a raw asset exists so text-like inputs embed their contents while other inputs only reference the recorded artifact. [crates/gwiki/src/ingest/file/render.rs:6-51]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `render_file_markdown` | function | `pub(super) fn render_file_markdown(` | `render_file_markdown [function]` | `4564f049-6c18-59cd-9578-af3f8c0754c9` | 6-51 [crates/gwiki/src/ingest/file/render.rs:6-51] | Indexed function `render_file_markdown` in `crates/gwiki/src/ingest/file/render.rs`. [crates/gwiki/src/ingest/file/render.rs:6-51] |
