---
title: crates/gcode/src/commands/codewiki/text/frontmatter.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/frontmatter.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text/frontmatter.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Overview

`crates/gcode/src/commands/codewiki/text/frontmatter.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/text/frontmatter.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Frontmatter` | class | 'Frontmatter<'a>' is a serde-serializable metadata struct that captures a document’s title and type, provenance sources with optional truncation, generator and trust/freshness labels, and optional degradation flags and source identifiers. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:7-21] |
| `FrontmatterSourceFile` | class | 'FrontmatterSourceFile<'a>' is a borrowed data structure that stores a source file path as '&'a str' and an optional serialized list of string ranges, omitting 'ranges' from output when it is empty. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:24-28] |
| `frontmatter` | function | Returns the result of 'frontmatter_with_degradation(title, kind, source_spans, &[])', i.e. generates frontmatter without any degradation options. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:36-38] |
| `frontmatter_with_degradation` | function | Creates a frontmatter string by delegating to 'frontmatter_with_options' with 'include_degradation' set to 'true', using the provided title, kind, source spans, and degraded source list. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:42-49] |
| `frontmatter_with_degradation_without_ranges` | function | Calls 'frontmatter_with_options' with the provided 'title', 'kind', 'source_spans', and 'degraded_sources', forcing the 'without_ranges' option to 'false' and returning the resulting 'String'. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:51-58] |
| `frontmatter_with_options` | function | Builds a YAML frontmatter block for a codewiki entry from the given title, kind, source spans, and degraded-source list by assembling provenance metadata, serializing it, normalizing the YAML document markers, and returning it wrapped in '---' delimiters with a trailing blank line. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:60-91] |
| `append_relevant_source_files` | function | Appends a collapsible Markdown “Relevant source files” section to 'doc' by formatting source files and ranges from 'source_spans' as links, and optionally adds an omission note when provenance was truncated. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:93-130] |
| `append_curated_source_files` | function | Appends a collapsible “Relevant source files” section to 'doc' containing up to 'limit' curated Markdown links from 'source_spans', and adds an omitted-count note when provenance or truncation hides additional files. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:137-165] |
| `frontmatter_source_files` | function | Deduplicates 'SourceSpan's by file and line range, optionally formats their ranges, truncates provenance to the 'MAX_FRONTMATTER_PROVENANCE_FILES' most-span-heavy files while returning the number omitted, and yields the resulting 'FrontmatterSourceFile' list. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:167-213] |
| `format_frontmatter_ranges` | function | It normalizes each '(usize, usize)' range so 'start <= end', merges overlapping or adjacent ranges in ascending 'BTreeSet' order, and returns each merged range as either a single line number or a 'start-end' string. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:215-239] |
| `source_range_href` | function | Constructs a Markdown source-link URL by percent-encoding the file path and appending a line-range anchor of the form '#Lstart-Lend' when 'range' contains '-', or '#Lrange' otherwise. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:241-247] |
| `encode_markdown_path` | function | Returns a new path string by splitting 'path' on '/', URL-encoding each segment independently, and rejoining the encoded segments with '/'. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:249-258] |
| `escape_markdown_link_label` | function | Returns a new 'String' with backslashes doubled and '[' and ']' escaped with a leading backslash so the value is safe to use as a Markdown link label. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:260-265] |

