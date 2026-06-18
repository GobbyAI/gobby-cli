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

`crates/gwiki/src/markdown.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

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
| `extracts_heading_ranges` | function | Verifies that 'parse_markdown' correctly identifies top-level headings, assigns each heading a 'section_byte_start'/'section_byte_end' spanning its section, and splits the markdown body into ordered chunks with the expected heading metadata. [crates/gwiki/src/markdown.rs:434-483] |
| `headings_ignore_code_until_matching_fence_length_closes` | function | Verifies that markdown headings inside a fenced code block remain ignored until a closing fence of matching length appears, so only the heading after the fence is parsed. [crates/gwiki/src/markdown.rs:486-498] |
| `index_parse_is_read_only` | function | Verifies that 'parse_index_file' parses a Markdown page’s path, frontmatter title, and outgoing links without modifying the underlying file contents. [crates/gwiki/src/markdown.rs:501-517] |
| `atx_heading_keeps_hash_without_preceding_space` | function | Verifies that 'parse_atx_heading' preserves a '#' character in heading text when it is not preceded by a space, while still stripping valid trailing ATX closing hashes like in '# Title ###'. [crates/gwiki/src/markdown.rs:520-529] |
| `normalize_strips_trailing_whitespace_and_collapses_blank_lines` | function | Verifies that 'normalize' removes trailing whitespace from lines and collapses runs of multiple blank lines into a single blank line, turning '"alpha \n\n\n\nbeta\t\n"' into '"alpha\n\nbeta\n"'. [crates/gwiki/src/markdown.rs:532-535] |
| `normalize_surrounds_headings_with_blank_lines` | function | Ensures Markdown headings are surrounded by blank lines by inserting a blank line before and after a heading when adjacent text is present. [crates/gwiki/src/markdown.rs:538-544] |
| `normalize_does_not_insert_blank_before_leading_heading` | function | Verifies that 'normalize' preserves a document that starts with a heading without inserting a blank line before the leading heading, while still normalizing the following paragraph separation. [crates/gwiki/src/markdown.rs:547-550] |
| `normalize_surrounds_fenced_code_with_blank_lines` | function | Verifies that fenced code blocks are surrounded by blank lines by normalizing a markdown string so that blank lines are inserted before and after a fenced code block when adjacent text would otherwise violate MD031. [crates/gwiki/src/markdown.rs:553-559] |
| `normalize_preserves_fenced_code_content_verbatim` | function | Verifies that 'normalize' leaves the contents of a fenced code block unchanged, including trailing whitespace and consecutive blank lines. [crates/gwiki/src/markdown.rs:562-566] |
| `normalize_ends_with_exactly_one_trailing_newline` | function | Verifies that 'normalize' appends a single trailing newline to text that lacks one and collapses multiple trailing newlines down to exactly one. [crates/gwiki/src/markdown.rs:569-573] |
| `normalize_preserves_frontmatter_and_separates_first_heading` | function | Verifies that 'normalize' preserves YAML frontmatter and inserts blank-line separation so the first Markdown heading is isolated from the frontmatter and the following body text. [crates/gwiki/src/markdown.rs:576-581] |
| `normalize_keeps_wikilink_and_table_pipes_intact` | function | Verifies that 'normalize' inserts a blank line after a heading while preserving wikilink pipe syntax ('`[[Page\|Alias]]`') and Markdown table pipe characters unchanged. [crates/gwiki/src/markdown.rs:584-591] |
| `normalize_is_idempotent` | function | Verifies that 'normalize' is idempotent by asserting 'normalize(normalize(input)) == normalize(input)' for a sample document containing front matter, excess whitespace, and a code block. [crates/gwiki/src/markdown.rs:594-598] |

