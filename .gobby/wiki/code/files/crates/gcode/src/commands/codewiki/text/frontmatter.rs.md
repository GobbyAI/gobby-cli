---
title: crates/gcode/src/commands/codewiki/text/frontmatter.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/frontmatter.rs
  ranges:
  - 6-20
  - 23-27
  - 35-37
  - 41-48
  - 50-57
  - 59-126
  - 128-152
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text/frontmatter.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Purpose

Defines the YAML-serializable frontmatter model for codewiki pages and the helpers that assemble it from source spans. `Frontmatter` and `FrontmatterSourceFile` capture the page title, kind, provenance files and ranges, truncation count, generator/trust/freshness flags, and optional degradation metadata, while `frontmatter`, `frontmatter_with_degradation`, and `frontmatter_with_degradation_without_ranges` are thin entry points into `frontmatter_with_options`. The main builder deduplicates spans per file, optionally formats and includes line ranges, caps provenance to the top contributing files, and records omitted files plus degraded-source information before serializing to a string.
[crates/gcode/src/commands/codewiki/text/frontmatter.rs:6-20]
[crates/gcode/src/commands/codewiki/text/frontmatter.rs:23-27]
[crates/gcode/src/commands/codewiki/text/frontmatter.rs:35-37]
[crates/gcode/src/commands/codewiki/text/frontmatter.rs:41-48]
[crates/gcode/src/commands/codewiki/text/frontmatter.rs:50-57]

## API Symbols

- `Frontmatter` (class) component `Frontmatter [class]` (`96d27a60-2203-517d-a457-d28146a44f5c`) lines 6-20 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:6-20]
  - Signature: `struct Frontmatter<'a> {`
  - Purpose: 'Frontmatter<'a>' is a serde-serializable metadata struct holding a document title, a renamed 'type' field ('kind'), provenance source files and truncation count, generator and quality flags ('generated_by', 'trust', 'freshness'), and optional degradation indicators plus a list of degraded source identifiers. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:6-20]
- `FrontmatterSourceFile` (class) component `FrontmatterSourceFile [class]` (`285c7889-0a14-50fd-a08a-c7c0d3945293`) lines 23-27 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:23-27]
  - Signature: `struct FrontmatterSourceFile<'a> {`
  - Purpose: 'FrontmatterSourceFile<'a>' is a borrowed data structure that stores a source file path or contents as '&'a str' plus an optional serialized list of string ranges, omitting 'ranges' when empty. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:23-27]
- `frontmatter` (function) component `frontmatter [function]` (`470f0083-66fa-5b58-9a60-b7a5b4235349`) lines 35-37 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:35-37]
  - Signature: `pub(crate) fn frontmatter(title: &str, kind: &str, source_spans: &[SourceSpan]) -> String {`
  - Purpose: Returns the result of 'frontmatter_with_degradation(title, kind, source_spans, &[])', producing a frontmatter 'String' with no degradation data. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:35-37]
- `frontmatter_with_degradation` (function) component `frontmatter_with_degradation [function]` (`69e2d276-fb21-5535-9cfd-92d150d1afd6`) lines 41-48 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:41-48]
  - Signature: `pub(crate) fn frontmatter_with_degradation(`
  - Purpose: Builds a frontmatter string by delegating to 'frontmatter_with_options' with the given title, kind, source spans, and degraded sources, always enabling degradation handling via the final 'true' flag. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:41-48]
- `frontmatter_with_degradation_without_ranges` (function) component `frontmatter_with_degradation_without_ranges [function]` (`a51421b9-0367-5d96-9aad-ad1f44bcf512`) lines 50-57 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:50-57]
  - Signature: `pub(crate) fn frontmatter_with_degradation_without_ranges(`
  - Purpose: Returns a frontmatter string by delegating to 'frontmatter_with_options' with the given 'title', 'kind', 'source_spans', and 'degraded_sources', while hard-coding 'include_ranges' to 'false'. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:50-57]
- `frontmatter_with_options` (function) component `frontmatter_with_options [function]` (`55b43f31-1621-5c76-919e-b5da8dd5e780`) lines 59-126 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:59-126]
  - Signature: `fn frontmatter_with_options(`
  - Purpose: Builds a 'Frontmatter' string from the title/kind and source spans by deduplicating and optionally range-formatting per-file provenance, truncating to the top contributing files when necessary, and setting generated/trust/freshness/degraded metadata. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:59-126]
- `format_frontmatter_ranges` (function) component `format_frontmatter_ranges [function]` (`f8f7b69c-d71e-5e3f-bc25-69d6193ac88a`) lines 128-152 [crates/gcode/src/commands/codewiki/text/frontmatter.rs:128-152]
  - Signature: `fn format_frontmatter_ranges(ranges: BTreeSet<(usize, usize)>) -> Vec<String> {`
  - Purpose: Converts a sorted set of line-range tuples into a merged list of canonical string ranges, normalizing each pair to ascending order, coalescing overlapping or adjacent ranges, and rendering single-line ranges as '"n"' and multi-line ranges as '"start-end"'. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:128-152]

