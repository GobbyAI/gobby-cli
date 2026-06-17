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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/report/render.rs:8-18](crates/gcode/src/graph/report/render.rs#L8-L18), [crates/gcode/src/graph/report/render.rs:20-99](crates/gcode/src/graph/report/render.rs#L20-L99), [crates/gcode/src/graph/report/render.rs:101-121](crates/gcode/src/graph/report/render.rs#L101-L121), [crates/gcode/src/graph/report/render.rs:123-141](crates/gcode/src/graph/report/render.rs#L123-L141), [crates/gcode/src/graph/report/render.rs:143-150](crates/gcode/src/graph/report/render.rs#L143-L150), [crates/gcode/src/graph/report/render.rs:152-164](crates/gcode/src/graph/report/render.rs#L152-L164), [crates/gcode/src/graph/report/render.rs:166-177](crates/gcode/src/graph/report/render.rs#L166-L177), [crates/gcode/src/graph/report/render.rs:179-185](crates/gcode/src/graph/report/render.rs#L179-L185)

</details>

# crates/gcode/src/graph/report/render.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

Builds a Markdown report for a project graph report. `RenderMarkdownInput` bundles the report metadata and graph statistics, and `render_markdown` turns that input into a structured document with a title, basic project/node/edge summary, optional code-edge counts, and several ranked sections for hotspots and unresolved/external targets. The helper functions keep the output safe and readable by formatting inline code and markdown text correctly, choosing backticks that do not conflict with the content, and rendering named count lists; the section appender helpers handle the repeated logic for emitting hotspot and target lists.
[crates/gcode/src/graph/report/render.rs:8-18]
[crates/gcode/src/graph/report/render.rs:20-99]
[crates/gcode/src/graph/report/render.rs:101-121]
[crates/gcode/src/graph/report/render.rs:123-141]
[crates/gcode/src/graph/report/render.rs:143-150]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `RenderMarkdownInput` | class | `pub(super) struct RenderMarkdownInput<'a> {` | `RenderMarkdownInput [class]` | `22688337-5529-53a1-a581-7127412b4536` | 8-18 [crates/gcode/src/graph/report/render.rs:8-18] | Indexed class `RenderMarkdownInput` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:8-18] |
| `render_markdown` | function | `pub(super) fn render_markdown(input: RenderMarkdownInput<'_>) -> String {` | `render_markdown [function]` | `2e342435-0b6b-52b8-a5a2-7b5d60d0aa52` | 20-99 [crates/gcode/src/graph/report/render.rs:20-99] | Indexed function `render_markdown` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:20-99] |
| `append_hotspot_section` | function | `fn append_hotspot_section(` | `append_hotspot_section [function]` | `3328327f-db95-569d-b43b-e21f8dbab0db` | 101-121 [crates/gcode/src/graph/report/render.rs:101-121] | Indexed function `append_hotspot_section` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:101-121] |
| `append_target_section` | function | `fn append_target_section(` | `append_target_section [function]` | `5a0d8348-6520-5220-8a67-4e7ee729f212` | 123-141 [crates/gcode/src/graph/report/render.rs:123-141] | Indexed function `append_target_section` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:123-141] |
| `inline_code` | function | `fn inline_code(value: &str) -> String {` | `inline_code [function]` | `531d48a4-bf59-5f2c-b1b8-a91f6fdc3277` | 143-150 [crates/gcode/src/graph/report/render.rs:143-150] | Indexed function `inline_code` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:143-150] |
| `max_backtick_run` | function | `fn max_backtick_run(value: &str) -> usize {` | `max_backtick_run [function]` | `fddfe140-2357-52a4-aa5c-15bd86f74cf6` | 152-164 [crates/gcode/src/graph/report/render.rs:152-164] | Indexed function `max_backtick_run` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:152-164] |
| `markdown_text` | function | `fn markdown_text(value: &str) -> String {` | `markdown_text [function]` | `2d26d80c-6a5e-5df6-8be8-94cc957b3464` | 166-177 [crates/gcode/src/graph/report/render.rs:166-177] | Indexed function `markdown_text` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:166-177] |
| `named_counts_inline` | function | `fn named_counts_inline(counts: &BTreeMap<String, usize>) -> String {` | `named_counts_inline [function]` | `c925723a-1915-5fea-bec4-205cbe0d78b1` | 179-185 [crates/gcode/src/graph/report/render.rs:179-185] | Indexed function `named_counts_inline` in `crates/gcode/src/graph/report/render.rs`. [crates/gcode/src/graph/report/render.rs:179-185] |
