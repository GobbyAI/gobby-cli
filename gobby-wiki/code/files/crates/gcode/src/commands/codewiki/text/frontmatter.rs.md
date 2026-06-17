---
title: crates/gcode/src/commands/codewiki/text/frontmatter.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/frontmatter.rs
  ranges:
  - 7-21
  - 24-28
  - 36-38
  - 42-49
  - 51-58
  - 60-91
  - 93-130
  - 132-178
  - 180-204
  - 206-212
  - 214-223
  - 225-230
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/text/frontmatter.rs:7-21](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L7-L21), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:24-28](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L24-L28), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:36-38](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L36-L38), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:42-49](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L42-L49), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:51-58](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L51-L58), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:60-91](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L60-L91), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:93-130](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L93-L130), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:132-178](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L132-L178), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:180-204](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L180-L204), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:206-212](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L206-L212), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:214-223](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L214-L223), [crates/gcode/src/commands/codewiki/text/frontmatter.rs:225-230](crates/gcode/src/commands/codewiki/text/frontmatter.rs#L225-L230)

</details>

# crates/gcode/src/commands/codewiki/text/frontmatter.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Purpose

Builds the serialized frontmatter for codewiki pages, combining a title, page type, provenance, and fixed metadata like generated_by, trust, and freshness, with optional degradation fields when inputs are incomplete. The core builder `frontmatter_with_options` gathers and caps provenance files from source spans, optionally includes range links, and relies on helpers to format ranges and safely encode markdown paths and link labels.
[crates/gcode/src/commands/codewiki/text/frontmatter.rs:7-21]
[crates/gcode/src/commands/codewiki/text/frontmatter.rs:24-28]
[crates/gcode/src/commands/codewiki/text/frontmatter.rs:36-38]
[crates/gcode/src/commands/codewiki/text/frontmatter.rs:42-49]
[crates/gcode/src/commands/codewiki/text/frontmatter.rs:51-58]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Frontmatter` | class | `struct Frontmatter<'a> {` | `Frontmatter [class]` | `2dbefc28-73f8-5576-ba77-caad49f10b19` | 7-21 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:7-21] | Indexed class `Frontmatter` in `crates/gcode/src/commands/codewiki/text/frontmatter.rs`. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:7-21] |
| `FrontmatterSourceFile` | class | `struct FrontmatterSourceFile<'a> {` | `FrontmatterSourceFile [class]` | `a07d25fa-911d-5052-8ad2-9e59577e9de0` | 24-28 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:24-28] | Indexed class `FrontmatterSourceFile` in `crates/gcode/src/commands/codewiki/text/frontmatter.rs`. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:24-28] |
| `frontmatter` | function | `pub(crate) fn frontmatter(title: &str, kind: &str, source_spans: &[SourceSpan]) -> String {` | `frontmatter [function]` | `343c9901-569b-5506-9d88-739c18e80a0c` | 36-38 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:36-38] | Indexed function `frontmatter` in `crates/gcode/src/commands/codewiki/text/frontmatter.rs`. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:36-38] |
| `frontmatter_with_degradation` | function | `pub(crate) fn frontmatter_with_degradation(` | `frontmatter_with_degradation [function]` | `2757dfe1-7833-59cd-83c3-7ec4715793c1` | 42-49 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:42-49] | Indexed function `frontmatter_with_degradation` in `crates/gcode/src/commands/codewiki/text/frontmatter.rs`. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:42-49] |
| `frontmatter_with_degradation_without_ranges` | function | `pub(crate) fn frontmatter_with_degradation_without_ranges(` | `frontmatter_with_degradation_without_ranges [function]` | `8cf33b97-9ec5-5160-9fb6-655951e15b22` | 51-58 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:51-58] | Indexed function `frontmatter_with_degradation_without_ranges` in `crates/gcode/src/commands/codewiki/text/frontmatter.rs`. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:51-58] |
| `frontmatter_with_options` | function | `fn frontmatter_with_options(` | `frontmatter_with_options [function]` | `9d20e8cc-ed24-50bc-9913-a7f67e8e1725` | 60-91 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:60-91] | Indexed function `frontmatter_with_options` in `crates/gcode/src/commands/codewiki/text/frontmatter.rs`. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:60-91] |
| `append_relevant_source_files` | function | `pub(crate) fn append_relevant_source_files(doc: &mut String, source_spans: &[SourceSpan]) {` | `append_relevant_source_files [function]` | `73b0f073-3628-5541-bb2c-1786719fb919` | 93-130 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:93-130] | Indexed function `append_relevant_source_files` in `crates/gcode/src/commands/codewiki/text/frontmatter.rs`. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:93-130] |
| `frontmatter_source_files` | function | `fn frontmatter_source_files(` | `frontmatter_source_files [function]` | `88d2dc3a-c34b-5513-997c-1b5d037dfe08` | 132-178 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:132-178] | Indexed function `frontmatter_source_files` in `crates/gcode/src/commands/codewiki/text/frontmatter.rs`. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:132-178] |
| `format_frontmatter_ranges` | function | `fn format_frontmatter_ranges(ranges: BTreeSet<(usize, usize)>) -> Vec<String> {` | `format_frontmatter_ranges [function]` | `e3bb590f-9aaa-5363-b9fe-53b6457b7259` | 180-204 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:180-204] | Indexed function `format_frontmatter_ranges` in `crates/gcode/src/commands/codewiki/text/frontmatter.rs`. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:180-204] |
| `source_range_href` | function | `fn source_range_href(file: &str, range: &str) -> String {` | `source_range_href [function]` | `ff740c94-a578-5053-a88f-484c1da6900e` | 206-212 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:206-212] | Indexed function `source_range_href` in `crates/gcode/src/commands/codewiki/text/frontmatter.rs`. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:206-212] |
| `encode_markdown_path` | function | `fn encode_markdown_path(path: &str) -> String {` | `encode_markdown_path [function]` | `59516e4b-f55e-50ab-b80a-6534b9607174` | 214-223 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:214-223] | Indexed function `encode_markdown_path` in `crates/gcode/src/commands/codewiki/text/frontmatter.rs`. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:214-223] |
| `escape_markdown_link_label` | function | `fn escape_markdown_link_label(value: &str) -> String {` | `escape_markdown_link_label [function]` | `8088ded6-e281-5a00-822c-ad718fd1df5c` | 225-230 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:225-230] | Indexed function `escape_markdown_link_label` in `crates/gcode/src/commands/codewiki/text/frontmatter.rs`. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:225-230] |
