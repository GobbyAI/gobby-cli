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

This file renders a project graph report as Markdown. `render_markdown` takes a borrowed `RenderMarkdownInput` bundle containing the project metadata, graph summary, hotspot lists, unresolved and external target frequencies, optional bridge summary, degradation details, and a `top_n` limit, then assembles the report sections in order. It emits the report header and core counts, optionally adds code-edge counts, appends ranked hotspot and target sections through dedicated helpers, includes an optional `RELATES_TO_CODE` bridge summary and degradation details, and relies on small formatting helpers to produce safe inline code, escaped markdown text, and comma-separated `name=count` summaries.
[crates/gcode/src/graph/report/render.rs:8-18]
[crates/gcode/src/graph/report/render.rs:20-99]
[crates/gcode/src/graph/report/render.rs:101-121]
[crates/gcode/src/graph/report/render.rs:123-141]
[crates/gcode/src/graph/report/render.rs:143-150]

## API Symbols

- `RenderMarkdownInput` (class) component `RenderMarkdownInput [class]` (`22688337-5529-53a1-a581-7127412b4536`) lines 8-18 [crates/gcode/src/graph/report/render.rs:8-18]
  - Signature: `pub(super) struct RenderMarkdownInput<'a> {`
  - Purpose: 'RenderMarkdownInput' is a borrowed data bundle that supplies a project report’s metadata, summary sections, target-frequency lists, optional bridge summary, degradation details, and 'top_n' limit to a markdown-rendering routine. [crates/gcode/src/graph/report/render.rs:8-18]
- `render_markdown` (function) component `render_markdown [function]` (`2e342435-0b6b-52b8-a5a2-7b5d60d0aa52`) lines 20-99 [crates/gcode/src/graph/report/render.rs:20-99]
  - Signature: `pub(super) fn render_markdown(input: RenderMarkdownInput<'_>) -> String {`
  - Purpose: Builds and returns a Markdown project graph report string containing project metadata, node and edge counts, optional code-edge counts, ranked hotspot and target sections, an optional 'RELATES_TO_CODE' bridge summary, and degradation details. [crates/gcode/src/graph/report/render.rs:20-99]
- `append_hotspot_section` (function) component `append_hotspot_section [function]` (`3328327f-db95-569d-b43b-e21f8dbab0db`) lines 101-121 [crates/gcode/src/graph/report/render.rs:101-121]
  - Signature: `fn append_hotspot_section(`
  - Purpose: Appends a blank line, a Markdown '##' section heading, and up to 'top_n' hotspot entries formatted with inline-coded names and their degree/incoming/outgoing counts, unless 'top_n' is zero or 'hotspots' is empty. [crates/gcode/src/graph/report/render.rs:101-121]
- `append_target_section` (function) component `append_target_section [function]` (`5a0d8348-6520-5220-8a67-4e7ee729f212`) lines 123-141 [crates/gcode/src/graph/report/render.rs:123-141]
  - Signature: `fn append_target_section(`
  - Purpose: Appends a blank line, a Markdown '##' heading, and up to 'top_n' bullet items formatted as inline-code target names with counts to 'lines', unless 'top_n' is zero or 'targets' is empty. [crates/gcode/src/graph/report/render.rs:123-141]
- `inline_code` (function) component `inline_code [function]` (`531d48a4-bf59-5f2c-b1b8-a91f6fdc3277`) lines 143-150 [crates/gcode/src/graph/report/render.rs:143-150]
  - Signature: `fn inline_code(value: &str) -> String {`
  - Purpose: Returns 'value' wrapped in a run of apostrophes one longer than its longest backtick run, inserting spaces inside the delimiters if the string already starts or ends with an apostrophe to avoid adjacent quote collisions. [crates/gcode/src/graph/report/render.rs:143-150]
- `max_backtick_run` (function) component `max_backtick_run [function]` (`fddfe140-2357-52a4-aa5c-15bd86f74cf6`) lines 152-164 [crates/gcode/src/graph/report/render.rs:152-164]
  - Signature: `fn max_backtick_run(value: &str) -> usize {`
  - Purpose: Returns the length of the longest contiguous run of backtick characters in 'value' by scanning its chars and tracking the current and maximum streak length. [crates/gcode/src/graph/report/render.rs:152-164]
- `markdown_text` (function) component `markdown_text [function]` (`2d26d80c-6a5e-5df6-8be8-94cc957b3464`) lines 166-177 [crates/gcode/src/graph/report/render.rs:166-177]
  - Signature: `fn markdown_text(value: &str) -> String {`
  - Purpose: Returns a new string with Markdown-sensitive characters escaped ('\', ''', '*', '_', '[', ']', '<', '>') and newline characters converted to spaces. [crates/gcode/src/graph/report/render.rs:166-177]
- `named_counts_inline` (function) component `named_counts_inline [function]` (`c925723a-1915-5fea-bec4-205cbe0d78b1`) lines 179-185 [crates/gcode/src/graph/report/render.rs:179-185]
  - Signature: `fn named_counts_inline(counts: &BTreeMap<String, usize>) -> String {`
  - Purpose: Formats the entries of a 'BTreeMap<String, usize>' into a single comma-separated string of 'name=count' pairs. [crates/gcode/src/graph/report/render.rs:179-185]

