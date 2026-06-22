---
title: crates/gwiki/src/markdown.rs
type: code_file
provenance:
- file: crates/gwiki/src/markdown.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/markdown.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/markdown.rs` exposes 33 indexed API symbols.

## How it fits

`crates/gwiki/src/markdown.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `MarkdownHeading` | class | 'MarkdownHeading' is a data structure representing a parsed Markdown heading, storing its heading level, title text, hierarchical path, and byte offsets for both the heading and its enclosing section. [crates/gwiki/src/markdown.rs:11-19] |
| `MarkdownDomainRecord` | class | 'MarkdownDomainRecord' is a parsed Markdown document record that stores the source path, extracted frontmatter, the byte offset where the body begins, and the document’s parsed headings, wiki links, and content chunks. [crates/gwiki/src/markdown.rs:22-29] |
| `MarkdownParseError` | type | Indexed type `MarkdownParseError` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:32-35] |
| `MarkdownFence` | class | 'MarkdownFence' is a crate-private struct that represents a Markdown fence using a single-byte marker and a fence length. [crates/gwiki/src/markdown.rs:38-41] |
| `markdown_fence_start` | function | Returns 'Some(MarkdownFence)' when 'line' has at most three leading spaces followed immediately by at least three consecutive backticks or tildes, capturing that fence’s marker byte and length, and 'None' otherwise. [crates/gwiki/src/markdown.rs:43-55] |
| `markdown_fence_closes` | function | Returns 'true' when 'line' begins with at most three spaces followed by at least 'fence.len' consecutive fence marker bytes and nothing but whitespace after them, indicating a matching closing markdown fence. [crates/gwiki/src/markdown.rs:57-68] |
| `normalize` | function | Returns a normalized copy of 'input' by preserving any parsed frontmatter prefix, normalizing the body, inserting a separating blank line when needed, and collapsing trailing newlines so the result ends with exactly one newline unless empty. [crates/gwiki/src/markdown.rs:85-110] |
| `BodyLine` | type | Indexed type `BodyLine` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:113-120] |
| `normalize_body` | function | 'normalize_body' tokenizes the input into markdown-aware line variants, preserves fenced code blocks, trims trailing whitespace on non-fence lines, and normalizes blank-line spacing around headings and fence boundaries according to markdown lint rules. [crates/gwiki/src/markdown.rs:122-190] |
| `push_blank` | function | Appends an empty 'String' to 'out' only if 'out' is nonempty and its last element is not already blank. [crates/gwiki/src/markdown.rs:194-198] |
| `MarkdownParseError::fmt` | method | Implements 'fmt::Display' by pattern-matching on 'self' and writing the inner error for either 'Frontmatter' or 'Io' directly into the provided formatter. [crates/gwiki/src/markdown.rs:201-206] |
| `MarkdownParseError::from` | method | Converts a 'FrontmatterError' into 'Self' by wrapping it in the 'Self::Frontmatter' enum variant. [crates/gwiki/src/markdown.rs:212-214] |
| `MarkdownParseError::from` | method | Converts a 'std::io::Error' into 'Self' by wrapping it in the 'Self::Io' enum variant. [crates/gwiki/src/markdown.rs:218-220] |
| `parse_markdown` | function | Parses a Markdown document into a 'MarkdownDomainRecord' by converting the input path, extracting frontmatter, links, headings, and content chunks from the markdown body, and returning any parse error from frontmatter parsing. [crates/gwiki/src/markdown.rs:223-246] |
| `parse_index_file` | function | Reads the file at 'path' into a UTF-8 string and delegates to 'parse_markdown' with the file path, contents, and 'known_targets', returning either a 'MarkdownDomainRecord' or a 'MarkdownParseError'. [crates/gwiki/src/markdown.rs:249-260] |
| `extract_headings` | function | Scans a markdown substring from 'body_start', tracking fenced code blocks and ATX headings to build a nested heading path and return 'MarkdownHeading' entries with per-heading byte ranges and section end offsets derived from the next heading or EOF. [crates/gwiki/src/markdown.rs:262-315] |
| `parse_atx_heading` | function | Parses a Markdown ATX heading line with up to three leading spaces, requiring 1 to 6 leading '#' characters followed by whitespace or end-of-line, and returns the heading level plus the trimmed title with any closing sequence stripped. [crates/gwiki/src/markdown.rs:317-336] |
| `strip_atx_closing_sequence` | function | Returns 'title' without a trailing ATX closing sequence of one or more '#' characters when those hashes are preceded by whitespace, otherwise returns the original string unchanged. [crates/gwiki/src/markdown.rs:338-360] |
| `build_chunks` | function | 'build_chunks' partitions the markdown into a 'Vec<Chunk>' by emitting an unlabelled chunk for each inter-heading gap starting at 'body_start', a labelled chunk for each heading’s section range using the heading title and path, and a final trailing chunk from the last section end to 'markdown.len()'. [crates/gwiki/src/markdown.rs:362-404] |
| `push_chunk` | function | 'push_chunk' appends a 'Chunk' to 'chunks' with the given file path, byte range, optional heading, and 'heading_path' metadata, but only if the range is non-empty and the corresponding markdown slice contains non-whitespace content. [crates/gwiki/src/markdown.rs:406-426] |

_Verified by 13 in-file unit tests._

