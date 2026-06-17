---
title: crates/gwiki/src/video/markdown.rs
type: code_file
provenance:
- file: crates/gwiki/src/video/markdown.rs
  ranges:
  - 15-40
  - 42-300
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/video/markdown.rs:15-40](crates/gwiki/src/video/markdown.rs#L15-L40), [crates/gwiki/src/video/markdown.rs:42-300](crates/gwiki/src/video/markdown.rs#L42-L300)

</details>

# crates/gwiki/src/video/markdown.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file generates derived markdown for a video source. `write_video_derived_markdown` aligns transcript segments with frame descriptions, resolves the derived output path under the vault, creates parent directories if needed, renders the markdown, writes it atomically, and returns the output path plus the aligned segments. `render_video_derived_markdown` assembles the actual markdown text by combining scope, source record, request data, audio/video references, metadata fields, timestamps, and aligned segment content into a single document.
[crates/gwiki/src/video/markdown.rs:15-40]
[crates/gwiki/src/video/markdown.rs:42-300]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `write_video_derived_markdown` | function | `pub fn write_video_derived_markdown(` | `write_video_derived_markdown [function]` | `5872cc23-1676-599d-b273-32a4f1b149ba` | 15-40 [crates/gwiki/src/video/markdown.rs:15-40] | Indexed function `write_video_derived_markdown` in `crates/gwiki/src/video/markdown.rs`. [crates/gwiki/src/video/markdown.rs:15-40] |
| `render_video_derived_markdown` | function | `fn render_video_derived_markdown(` | `render_video_derived_markdown [function]` | `4150cec7-1348-5e19-864c-054dfe51b997` | 42-300 [crates/gwiki/src/video/markdown.rs:42-300] | Indexed function `render_video_derived_markdown` in `crates/gwiki/src/video/markdown.rs`. [crates/gwiki/src/video/markdown.rs:42-300] |
