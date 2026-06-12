---
title: crates/gwiki/src/markdown.rs
type: code_file
provenance:
- file: crates/gwiki/src/markdown.rs
  ranges:
  - 11-19
  - 22-29
  - 32-35
  - 38-41
  - 43-55
  - 57-68
  - 70-77
  - '79'
  - 81-85
  - 87-91
  - 93-116
  - 119-130
  - 132-185
  - 187-206
  - 208-230
  - 232-274
  - 276-296
  - 304-353
  - 356-368
  - 371-387
  - 390-399
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/markdown.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/markdown.rs` exposes 24 indexed API symbols.
[crates/gwiki/src/markdown.rs:11-19]
[crates/gwiki/src/markdown.rs:22-29]
[crates/gwiki/src/markdown.rs:32-35]
[crates/gwiki/src/markdown.rs:38-41]
[crates/gwiki/src/markdown.rs:43-55]

## API Symbols

- `MarkdownHeading` (class) component `MarkdownHeading [class]` (`f8871d89-a4b9-577d-b70c-8fe152ce549d`) lines 11-19 [crates/gwiki/src/markdown.rs:11-19]
  - Signature: `pub struct MarkdownHeading {`
  - Purpose: `MarkdownHeading` is a parsed Markdown heading record that captures its heading level, title text, hierarchical path, and byte-range offsets for both the heading itself and the enclosing section in the source document. [crates/gwiki/src/markdown.rs:11-19]
- `MarkdownDomainRecord` (class) component `MarkdownDomainRecord [class]` (`fd0bda02-0120-5a4f-a4fe-ca4ee8bf1e32`) lines 22-29 [crates/gwiki/src/markdown.rs:22-29]
  - Signature: `pub struct MarkdownDomainRecord {`
  - Purpose: `MarkdownDomainRecord` is a parsed Markdown document representation that stores the source `PathBuf`, extracted `WikiFrontmatter`, the byte offset where body content begins, and indexed structural data for headings, wiki links, and content chunks. [crates/gwiki/src/markdown.rs:22-29]
- `MarkdownParseError` (type) component `MarkdownParseError [type]` (`e71121cc-2253-570c-977e-c9f8ab9a36fe`) lines 32-35 [crates/gwiki/src/markdown.rs:32-35]
  - Signature: `pub enum MarkdownParseError {`
  - Purpose: Indexed type `MarkdownParseError` in `crates/gwiki/src/markdown.rs`. [crates/gwiki/src/markdown.rs:32-35]
- `MarkdownFence` (class) component `MarkdownFence [class]` (`44f0fa0a-726c-5afe-9ed9-dff0a0513b9e`) lines 38-41 [crates/gwiki/src/markdown.rs:38-41]
  - Signature: `pub(crate) struct MarkdownFence {`
  - Purpose: `MarkdownFence` is an internal value type that captures a Markdown fence delimiter by storing the fence marker byte and the delimiter run length for parsing or rendering fenced blocks. [crates/gwiki/src/markdown.rs:38-41]
- `markdown_fence_start` (function) component `markdown_fence_start [function]` (`ac9abea2-aa28-59ee-b26d-f4bc83caad23`) lines 43-55 [crates/gwiki/src/markdown.rs:43-55]
  - Signature: `pub(crate) fn markdown_fence_start(line: &str) -> Option<MarkdownFence> {`
  - Purpose: Returns `Some(MarkdownFence { marker, len })` only when `line` starts with at most three leading spaces followed immediately by a run of at least three identical fence characters (`\`` or `~`), otherwise returns `None`. [crates/gwiki/src/markdown.rs:43-55]
- `markdown_fence_closes` (function) component `markdown_fence_closes [function]` (`36b7d1c7-2be0-57f7-8bbb-dda7e4ca991f`) lines 57-68 [crates/gwiki/src/markdown.rs:57-68]
  - Signature: `pub(crate) fn markdown_fence_closes(line: &str, fence: MarkdownFence) -> bool {`
  - Purpose: Returns `true` when `line` has at most three leading spaces, begins with at least `fence.len` consecutive `fence.marker` bytes, and contains nothing but whitespace after that closing marker run. [crates/gwiki/src/markdown.rs:57-68]
- `MarkdownParseError` (class) component `MarkdownParseError [class]` (`f110c3de-5abe-5005-927a-a25828000900`) lines 70-77 [crates/gwiki/src/markdown.rs:70-77]
  - Signature: `impl fmt::Display for MarkdownParseError {`
  - Purpose: `MarkdownParseError` implements `fmt::Display` by delegating string formatting to the contained `Frontmatter` or `Io` error, emitting the inner error’s display text unchanged. [crates/gwiki/src/markdown.rs:70-77]
- `MarkdownParseError.fmt` (method) component `MarkdownParseError.fmt [method]` (`fbdd7c9b-0485-59c4-ad45-779dccba74bf`) lines 71-76 [crates/gwiki/src/markdown.rs:71-76]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: It matches on `Self::Frontmatter` and `Self::Io` and forwards formatting to the contained error via `write!(f, "{error}")`, so the enum’s textual representation is exactly its inner error’s display output. [crates/gwiki/src/markdown.rs:71-76]
- `MarkdownParseError` (class) component `MarkdownParseError [class]` (`17c4eb02-c42f-5c57-893c-de6501d35db9`) lines 79-79 [crates/gwiki/src/markdown.rs:79]
  - Signature: `impl std::error::Error for MarkdownParseError {}`
  - Purpose: `MarkdownParseError` is a Rust error type that implements the standard `std::error::Error` trait, making it compatible with idiomatic error propagation and trait-object error handling. [crates/gwiki/src/markdown.rs:79]
- `MarkdownParseError` (class) component `MarkdownParseError [class]` (`387e1030-9be5-5144-abb2-d4bd012c202f`) lines 81-85 [crates/gwiki/src/markdown.rs:81-85]
  - Signature: `impl From<FrontmatterError> for MarkdownParseError {`
  - Purpose: `MarkdownParseError` implements `From<FrontmatterError>` by converting any `FrontmatterError` into the `MarkdownParseError::Frontmatter` variant. [crates/gwiki/src/markdown.rs:81-85]
- `MarkdownParseError.from` (method) component `MarkdownParseError.from [method]` (`b090e9f3-d9a4-5b31-beca-ddca92450e72`) lines 82-84 [crates/gwiki/src/markdown.rs:82-84]
  - Signature: `fn from(error: FrontmatterError) -> Self {`
  - Purpose: Converts a `FrontmatterError` into `Self` by wrapping it in the `Frontmatter` variant. [crates/gwiki/src/markdown.rs:82-84]
- `MarkdownParseError` (class) component `MarkdownParseError [class]` (`b500fc9a-73d0-5357-a1e5-e688dd0bc450`) lines 87-91 [crates/gwiki/src/markdown.rs:87-91]
  - Signature: `impl From<std::io::Error> for MarkdownParseError {`
  - Purpose: Implements `From<std::io::Error>` for `MarkdownParseError`, mapping any I/O error directly into the `MarkdownParseError::Io` variant. [crates/gwiki/src/markdown.rs:87-91]
- `MarkdownParseError.from` (method) component `MarkdownParseError.from [method]` (`223e0c06-2ba8-55b5-a787-9901c110f662`) lines 88-90 [crates/gwiki/src/markdown.rs:88-90]
  - Signature: `fn from(error: std::io::Error) -> Self {`
  - Purpose: Converts a `std::io::Error` into this type by wrapping it in the `Self::Io` variant. [crates/gwiki/src/markdown.rs:88-90]
- `parse_markdown` (function) component `parse_markdown [function]` (`ce5e52b0-f295-5da1-beb1-9d46fc7a1081`) lines 93-116 [crates/gwiki/src/markdown.rs:93-116]
  - Signature: `pub fn parse_markdown<I, S>(`
  - Purpose: Parses the provided markdown string for a given path by extracting frontmatter, known-target links, headings from the body start offset, and content chunks, then returns a `MarkdownDomainRecord` populated with those fields or a `MarkdownParseError` if parsing fails. [crates/gwiki/src/markdown.rs:93-116]
- `parse_index_file` (function) component `parse_index_file [function]` (`89afdf74-873c-5f78-82e9-b5faea06790a`) lines 119-130 [crates/gwiki/src/markdown.rs:119-130]
  - Signature: `pub fn parse_index_file<I, S>(`
  - Purpose: Reads the index file at `path` into a string and delegates parsing to `parse_markdown` with the path, contents, and `known_targets`, returning a `MarkdownDomainRecord` or propagating I/O/parse errors as `MarkdownParseError`. [crates/gwiki/src/markdown.rs:119-130]
- `extract_headings` (function) component `extract_headings [function]` (`4acb5620-41a1-5f51-ab93-f13c5a216413`) lines 132-185 [crates/gwiki/src/markdown.rs:132-185]
  - Signature: `fn extract_headings(markdown: &str, body_start: usize) -> Vec<MarkdownHeading> {`
  - Purpose: Scans the markdown body line by line from `body_start`, skipping content inside fenced code blocks, parsing ATX headings into a hierarchical `path`, and returning `MarkdownHeading` entries with byte offsets for each heading and its section span up to the next heading or end of input. [crates/gwiki/src/markdown.rs:132-185]
- `parse_atx_heading` (function) component `parse_atx_heading [function]` (`195e7aee-5dd7-5119-ab53-98bcb2308cd6`) lines 187-206 [crates/gwiki/src/markdown.rs:187-206]
  - Signature: `pub(crate) fn parse_atx_heading(line: &str) -> Option<(u8, String)> {`
  - Purpose: Parses a Markdown ATX heading line that has at most three leading spaces, requires 1 to 6 leading `#` characters followed by whitespace or end-of-line, and returns `(heading_level, stripped_title)` with any closing `#` sequence removed, otherwise `None`. [crates/gwiki/src/markdown.rs:187-206]
- `strip_atx_closing_sequence` (function) component `strip_atx_closing_sequence [function]` (`47a5d906-49ab-5666-9385-6fa127651597`) lines 208-230 [crates/gwiki/src/markdown.rs:208-230]
  - Signature: `fn strip_atx_closing_sequence(title: &str) -> &str {`
  - Purpose: Returns the input slice unchanged unless it ends with one or more `#` characters preceded by whitespace, in which case it strips that trailing ATX closing sequence and any whitespace before it. [crates/gwiki/src/markdown.rs:208-230]
- `build_chunks` (function) component `build_chunks [function]` (`8565bca7-06f4-5c44-bc35-1f329d7fc187`) lines 232-274 [crates/gwiki/src/markdown.rs:232-274]
  - Signature: `fn build_chunks(`
  - Purpose: It builds an ordered `Vec<Chunk>` covering `markdown[body_start..]` by emitting a plain chunk for each inter-heading gap, a titled/path-bearing chunk for each heading’s `[section_byte_start, section_byte_end)` section, and a final trailing chunk through `markdown.len()`. [crates/gwiki/src/markdown.rs:232-274]
- `push_chunk` (function) component `push_chunk [function]` (`06baa7e2-2f66-58f7-a8e4-877dcbe4f073`) lines 276-296 [crates/gwiki/src/markdown.rs:276-296]
  - Signature: `fn push_chunk(`
  - Purpose: Appends a `Chunk` for the given `markdown` byte range to `chunks` only if `byte_start < byte_end` and the slice is not all whitespace, recording the file path, byte bounds, optional heading, and `heading_path` metadata. [crates/gwiki/src/markdown.rs:276-296]
- `extracts_heading_ranges` (function) component `extracts_heading_ranges [function]` (`0ecf31b1-78e8-5228-8eb2-3e22ee84b756`) lines 304-353 [crates/gwiki/src/markdown.rs:304-353]
  - Signature: `fn extracts_heading_ranges() {`
  - Purpose: It verifies that `parse_markdown` correctly detects front matter and body start, extracts two top-level headings, assigns each heading and chunk the expected byte ranges and heading path metadata, and spans the first heading section up to the next heading and the second to EOF. [crates/gwiki/src/markdown.rs:304-353]
- `headings_ignore_code_until_matching_fence_length_closes` (function) component `headings_ignore_code_until_matching_fence_length_closes [function]` (`78b65cdb-2809-552b-9389-ece8288d51d1`) lines 356-368 [crates/gwiki/src/markdown.rs:356-368]
  - Signature: `fn headings_ignore_code_until_matching_fence_length_closes() {`
  - Purpose: Verifies that `parse_markdown` ignores `#` lines inside a four-backtick fenced code block until the matching four-backtick closing fence is seen, so only the trailing `# Heading` is parsed as a heading. [crates/gwiki/src/markdown.rs:356-368]
- `index_parse_is_read_only` (function) component `index_parse_is_read_only [function]` (`f39f917b-e02b-546c-b33a-1ba6b3842c7d`) lines 371-387 [crates/gwiki/src/markdown.rs:371-387]
  - Signature: `fn index_parse_is_read_only() {`
  - Purpose: Creates a temporary markdown page with frontmatter and a wiki link, parses it with `parse_index_file`, and verifies the parsed path, title, link count, and on-disk contents are unchanged, confirming the parse is read-only. [crates/gwiki/src/markdown.rs:371-387]
- `atx_heading_keeps_hash_without_preceding_space` (function) component `atx_heading_keeps_hash_without_preceding_space [function]` (`90226c7c-0678-5af3-92c8-70f2cb9bc096`) lines 390-399 [crates/gwiki/src/markdown.rs:390-399]
  - Signature: `fn atx_heading_keeps_hash_without_preceding_space() {`
  - Purpose: This test verifies that `parse_atx_heading` retains a `#` that is part of the heading text (`# C#`) while trimming trailing closing hashes and whitespace from ATX headings (`# Title ###` parses to `Title`). [crates/gwiki/src/markdown.rs:390-399]

