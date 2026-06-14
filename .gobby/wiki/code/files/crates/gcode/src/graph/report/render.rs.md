---
title: crates/gcode/src/graph/report/render.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/render.rs
  ranges:
  - 8-18
  - 20-99
  - 101-121
  - 123-141
  - 143-150
  - 152-164
  - 166-177
  - 179-185
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/report/render.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

This file provides markdown rendering for graph analysis reports. The `RenderMarkdownInput` struct packages report data, and `render_markdown` orchestrates the output by building a markdown string containing project metadata, high-degree hotspots (files, modules, symbols), incoming-call hotspots, and target frequency information. Helper functions handle specific formatting: `append_hotspot_section` and `append_target_section` structure report sections, `inline_code` and `markdown_text` manage content escaping, `max_backtick_run` supports proper backtick fence generation, and `named_counts_inline` formats categorical counts inline.
[crates/gcode/src/graph/report/render.rs:8-18]
[crates/gcode/src/graph/report/render.rs:20-99]
[crates/gcode/src/graph/report/render.rs:101-121]
[crates/gcode/src/graph/report/render.rs:123-141]
[crates/gcode/src/graph/report/render.rs:143-150]

## API Symbols

- `RenderMarkdownInput` (class) component `RenderMarkdownInput [class]` (`22688337-5529-53a1-a581-7127412b4536`) lines 8-18 [crates/gcode/src/graph/report/render.rs:8-18]
  - Signature: `pub(super) struct RenderMarkdownInput<'a> {`
  - Purpose: Indexed class `RenderMarkdownInput` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:8-18]
- `render_markdown` (function) component `render_markdown [function]` (`2e342435-0b6b-52b8-a5a2-7b5d60d0aa52`) lines 20-99 [crates/gcode/src/graph/report/render.rs:20-99]
  - Signature: `pub(super) fn render_markdown(input: RenderMarkdownInput<'_>) -> String {`
  - Purpose: Indexed function `render_markdown` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:20-99]
- `append_hotspot_section` (function) component `append_hotspot_section [function]` (`3328327f-db95-569d-b43b-e21f8dbab0db`) lines 101-121 [crates/gcode/src/graph/report/render.rs:101-121]
  - Signature: `fn append_hotspot_section(`
  - Purpose: Indexed function `append_hotspot_section` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:101-121]
- `append_target_section` (function) component `append_target_section [function]` (`5a0d8348-6520-5220-8a67-4e7ee729f212`) lines 123-141 [crates/gcode/src/graph/report/render.rs:123-141]
  - Signature: `fn append_target_section(`
  - Purpose: Indexed function `append_target_section` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:123-141]
- `inline_code` (function) component `inline_code [function]` (`531d48a4-bf59-5f2c-b1b8-a91f6fdc3277`) lines 143-150 [crates/gcode/src/graph/report/render.rs:143-150]
  - Signature: `fn inline_code(value: &str) -> String {`
  - Purpose: Indexed function `inline_code` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:143-150]
- `max_backtick_run` (function) component `max_backtick_run [function]` (`fddfe140-2357-52a4-aa5c-15bd86f74cf6`) lines 152-164 [crates/gcode/src/graph/report/render.rs:152-164]
  - Signature: `fn max_backtick_run(value: &str) -> usize {`
  - Purpose: Indexed function `max_backtick_run` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:152-164]
- `markdown_text` (function) component `markdown_text [function]` (`2d26d80c-6a5e-5df6-8be8-94cc957b3464`) lines 166-177 [crates/gcode/src/graph/report/render.rs:166-177]
  - Signature: `fn markdown_text(value: &str) -> String {`
  - Purpose: Indexed function `markdown_text` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:166-177]
- `named_counts_inline` (function) component `named_counts_inline [function]` (`c925723a-1915-5fea-bec4-205cbe0d78b1`) lines 179-185 [crates/gcode/src/graph/report/render.rs:179-185]
  - Signature: `fn named_counts_inline(counts: &BTreeMap<String, usize>) -> String {`
  - Purpose: Indexed function `named_counts_inline` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:179-185]

