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

`crates/gcode/src/commands/codewiki/text/frontmatter.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/text/frontmatter.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Frontmatter` | class | 'Frontmatter<'a>' is a Serde-serializable metadata struct that captures a document’s title, type, provenance sources, generation and trust/freshness status, and optional degradation and verification details, with selective omission of empty or absent fields during serialization. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:7-23] |
| `FrontmatterSourceFile` | class | 'FrontmatterSourceFile<'a>' is a borrowed source-file record containing a 'file' path/name and an optional serialized 'ranges' list of strings, with empty ranges omitted from serialization. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:26-30] |
| `FrontmatterVerifyNote` | class | 'FrontmatterVerifyNote<'a>' is a borrowed note record that stores a 'usize' identifier and a '&'a str' reason string for frontmatter verification output. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:33-36] |
| `frontmatter_with_degradation` | function | The 'frontmatter_with_degradation' function generates a frontmatter string by delegating to 'frontmatter_with_options' with the provided title, kind, source spans, and degraded sources, while passing 'true' as the fifth argument and an empty slice as the final argument. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:50-57] |
| `frontmatter_with_degradation_without_ranges` | function | This function generates frontmatter by calling 'frontmatter_with_options' with the specified title, kind, source spans, and degraded sources, while disabling range output and passing an empty options slice. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:59-66] |
| `frontmatter_with_degradation_and_verify_notes_without_ranges` | function | This function generates a frontmatter string by calling 'frontmatter_with_options' with the provided title, kind, source spans, degraded sources, and verification notes, passing 'false' to disable the ranges option. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:68-83] |
| `frontmatter_with_options` | function | This function constructs and returns a YAML-formatted frontmatter block as a string by serializing metadata, including source file provenance, degradation details, and verification notes, into a structured YAML format bounded by standard delimiters. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:85-124] |
| `append_relevant_source_files` | function | This function extracts source file paths and line ranges from a slice of 'SourceSpan's and appends them to a mutable 'String' formatted as a collapsible Markdown '<details>' block containing hyperlinked list items and an omission notice if the file list was truncated. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:126-163] |
| `append_curated_source_files` | function | This function extracts source files from a slice of 'SourceSpan' structs, limits the list to a specified size, and appends a collapsible HTML '<details>' element containing formatted Markdown links to the source files, along with a note indicating the count of any omitted files, to a mutable string buffer. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:170-198] |
| `frontmatter_source_files` | function | The 'frontmatter_source_files' function aggregates and groups a slice of source spans by file, optionally formats their line ranges, truncates the resulting file list to a maximum allowed limit by prioritizing those with the most spans, and returns the compiled list of 'FrontmatterSourceFile' structs alongside the count of omitted files. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:200-246] |
| `format_frontmatter_ranges` | function | The function normalizes and merges overlapping or adjacent line ranges from a 'BTreeSet' and formats the resulting merged intervals into a vector of strings representing single line numbers or hyphenated line ranges. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:248-272] |
| `source_range_href` | function | This function constructs a URL string by appending a GitHub-style line anchor—formatted from either a single line or a hyphen-separated range—to a markdown-encoded representation of the specified file path. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:274-280] |
| `encode_markdown_path` | function | The function URL-encodes each segment of a forward-slash-delimited path string while preserving the forward-slash separators. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:282-291] |
| `escape_markdown_link_label` | function | The 'escape_markdown_link_label' function escapes backslashes, opening square brackets, and closing square brackets within a string slice by prepending each with a backslash, returning the result as a new 'String'. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:293-298] |
| `spans` | function | The 'spans' function returns a 'Vec<SourceSpan>' containing a single 'SourceSpan' struct representing lines 1 through 4 of the file ''src/lib.rs''. [crates/gcode/src/commands/codewiki/text/frontmatter.rs:304-310] |

_Verified by 3 in-file unit tests._

