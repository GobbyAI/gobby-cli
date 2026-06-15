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

# crates/gwiki/src/video/markdown.rs

Module: [[code/modules/crates/gwiki/src/video|crates/gwiki/src/video]]

## Purpose

This file turns a video source record plus transcript and frame data into derived markdown and writes it into the vault. `write_video_derived_markdown` aligns transcript segments with frame descriptions, resolves and creates the output path, renders the markdown, and atomically saves it, returning the relative path and aligned segments. `render_video_derived_markdown` builds the markdown content itself by collecting normalized metadata from the scope, source record, request paths, audio reference, and aligned video segments.
[crates/gwiki/src/video/markdown.rs:15-40]
[crates/gwiki/src/video/markdown.rs:42-300]

## API Symbols

- `write_video_derived_markdown` (function) component `write_video_derived_markdown [function]` (`5872cc23-1676-599d-b273-32a4f1b149ba`) lines 15-40 [crates/gwiki/src/video/markdown.rs:15-40]
  - Signature: `pub fn write_video_derived_markdown(`
  - Purpose: Computes aligned transcript/frame segments, resolves the record’s derived markdown path under 'vault_root', ensures its parent directory exists, renders the video-derived markdown, writes it atomically to disk, and վերադարձs the relative path plus aligned segments in a 'VideoMarkdownResult'. [crates/gwiki/src/video/markdown.rs:15-40]
- `render_video_derived_markdown` (function) component `render_video_derived_markdown [function]` (`4150cec7-1348-5e19-864c-054dfe51b997`) lines 42-300 [crates/gwiki/src/video/markdown.rs:42-300]
  - Signature: `fn render_video_derived_markdown(`
  - Purpose: Builds a markdown string for a video-derived record by collecting normalized title/path/audio metadata and video/transcript/frame counts from the scope, source record, request, and aligned segments. [crates/gwiki/src/video/markdown.rs:42-300]

