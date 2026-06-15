---
title: crates/gcode/src/commands/codewiki/text/citations.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/citations.rs
  ranges:
  - 26-34
  - 38-44
  - 46-51
  - 58-98
  - 100-106
  - 108-128
  - 130-142
  - 144-153
  - 155-161
  - 166-179
  - 181-197
  - 199-225
  - 227-244
  - 246-259
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text/citations.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Purpose

Utilities for citation handling in codewiki text generation. The file parses `file:line[-line]` citation strings, validates and strips invalid bracketed citations, and checks whether any valid citation already exists in text. It also ranks `SourceSpan`s for fallback use by lexical overlap with the generated text, preferring source files over asset/data files and capping the number of fallback citations. Those selected spans are then rendered as citation lists or numbered markers, wrapped to line width, and optionally appended as a `## References` section when the document already contains matching marker references.
[crates/gcode/src/commands/codewiki/text/citations.rs:26-34]
[crates/gcode/src/commands/codewiki/text/citations.rs:38-44]
[crates/gcode/src/commands/codewiki/text/citations.rs:46-51]
[crates/gcode/src/commands/codewiki/text/citations.rs:58-98]
[crates/gcode/src/commands/codewiki/text/citations.rs:100-106]

## API Symbols

- `is_asset_or_data_file` (function) component `is_asset_or_data_file [function]` (`fa943380-0501-5373-a714-5ab4987af8b7`) lines 26-34 [crates/gcode/src/commands/codewiki/text/citations.rs:26-34]
  - Signature: `fn is_asset_or_data_file(file: &str) -> bool {`
  - Purpose: Returns 'true' if 'file' has a UTF-8 extension whose lowercase form is present in 'ASSET_DATA_EXTENSIONS', and 'false' otherwise. [crates/gcode/src/commands/codewiki/text/citations.rs:26-34]
- `lexical_tokens` (function) component `lexical_tokens [function]` (`c02cf790-b9de-5278-9fa8-5777daa87eca`) lines 38-44 [crates/gcode/src/commands/codewiki/text/citations.rs:38-44]
  - Signature: `fn lexical_tokens(value: &str) -> BTreeSet<String> {`
  - Purpose: Returns a 'BTreeSet<String>' of unique, ASCII-alphanumeric substrings from 'value' by splitting on non-ASCII-alphanumeric characters, discarding tokens shorter than 3 characters, lowercasing the rest, and collecting them into a sorted set. [crates/gcode/src/commands/codewiki/text/citations.rs:38-44]
- `citation_relevance` (function) component `citation_relevance [function]` (`a4e632c0-3e80-5fc7-90c3-616b20540091`) lines 46-51 [crates/gcode/src/commands/codewiki/text/citations.rs:46-51]
  - Signature: `fn citation_relevance(text_tokens: &BTreeSet<String>, file: &str) -> usize {`
  - Purpose: Returns the count of lexical tokens extracted from 'file' that also appear in 'text_tokens'. [crates/gcode/src/commands/codewiki/text/citations.rs:46-51]
- `fallback_spans` (function) component `fallback_spans [function]` (`ba5263ac-e540-51e0-a016-a88d65285fb9`) lines 58-98 [crates/gcode/src/commands/codewiki/text/citations.rs:58-98]
  - Signature: `pub(super) fn fallback_spans(spans: &[SourceSpan], text: &str) -> Vec<SourceSpan> {`
  - Purpose: 'fallback_spans' deduplicates the input spans, ranks their files by non-asset status, citation relevance to 'text', and filename, then returns up to 'MAX_FALLBACK_CITATIONS' spans by first selecting one span per file and filling any remaining slots with additional unique spans from those ranked files. [crates/gcode/src/commands/codewiki/text/citations.rs:58-98]
- `citation_list` (function) component `citation_list [function]` (`3259ccdb-4bbb-5ca5-8a94-1672a0888c7e`) lines 100-106 [crates/gcode/src/commands/codewiki/text/citations.rs:100-106]
  - Signature: `pub(crate) fn citation_list(spans: &[SourceSpan], text: &str) -> String {`
  - Purpose: Returns a newline-separated 'String' of citation strings produced by calling 'citation()' on each span from 'fallback_spans(spans, text)'. [crates/gcode/src/commands/codewiki/text/citations.rs:100-106]
- `wrap_citation_items` (function) component `wrap_citation_items [function]` (`d14e37d2-ce3c-533e-9bf7-ebb42cef4aa2`) lines 108-128 [crates/gcode/src/commands/codewiki/text/citations.rs:108-128]
  - Signature: `pub(super) fn wrap_citation_items<I>(items: I, max_line_width: usize) -> String`
  - Purpose: Joins an iterator of citation item strings into newline-separated lines, greedily wrapping to a new line before adding an item would make the current line exceed 'max_line_width', with items on the same line separated by single spaces. [crates/gcode/src/commands/codewiki/text/citations.rs:108-128]
- `citation_markers` (function) component `citation_markers [function]` (`1bd8f5f4-499b-5e57-b8e6-55e2a27e6bd7`) lines 130-142 [crates/gcode/src/commands/codewiki/text/citations.rs:130-142]
  - Signature: `pub(crate) fn citation_markers(spans: &[SourceSpan], text: &str) -> String {`
  - Purpose: Builds a wrapped citation-marker string by collecting fallback citation IDs from 'fallback_spans', filtering 'citation_references(spans)' to those IDs, formatting their indices as '"[{index}]"', and passing the result to 'wrap_citation_items' with 'FALLBACK_CITATION_LINE_WIDTH'. [crates/gcode/src/commands/codewiki/text/citations.rs:130-142]
- `citation_references` (function) component `citation_references [function]` (`2da98224-d432-58ca-b667-5d59e63082e4`) lines 144-153 [crates/gcode/src/commands/codewiki/text/citations.rs:144-153]
  - Signature: `fn citation_references(spans: &[SourceSpan]) -> Vec<(usize, String)> {`
  - Purpose: Deduplicates the input 'SourceSpan' values by collecting them into a 'BTreeSet', then returns a 1-based indexed 'Vec' of '(citation_number, span.citation())' pairs in sorted order. [crates/gcode/src/commands/codewiki/text/citations.rs:144-153]
- `replace_citations_with_markers` (function) component `replace_citations_with_markers [function]` (`88b1c0c3-5b9a-544c-8f02-85353cbd72ef`) lines 155-161 [crates/gcode/src/commands/codewiki/text/citations.rs:155-161]
  - Signature: `pub(crate) fn replace_citations_with_markers(text: &str, spans: &[SourceSpan]) -> String {`
  - Purpose: Replaces each citation substring found by 'citation_references(spans)' in 'text' with a numbered marker of the form '"[{index}]"', returning the transformed string. [crates/gcode/src/commands/codewiki/text/citations.rs:155-161]
- `write_references` (function) component `write_references [function]` (`c2f3f5c4-e3cf-5a98-9300-273ba3e26af1`) lines 166-179 [crates/gcode/src/commands/codewiki/text/citations.rs:166-179]
  - Signature: `pub(crate) fn write_references(doc: &mut String, spans: &[SourceSpan]) {`
  - Purpose: Appends a '## References' section to 'doc' containing only citation entries whose '[index]' markers already appear in the document, formatting each as a bullet line and leaving 'doc' unchanged if no such references exist. [crates/gcode/src/commands/codewiki/text/citations.rs:166-179]
- `ground_text` (function) component `ground_text [function]` (`8ca67329-d972-5fbf-9ff1-927845074c11`) lines 181-197 [crates/gcode/src/commands/codewiki/text/citations.rs:181-197]
  - Signature: `pub(crate) fn ground_text(`
  - Purpose: Returns the input text with invalid citations stripped and markdown links sanitized, then appends the fallback citation only if no valid citation remains, using a newline when the fallback contains one or a space otherwise. [crates/gcode/src/commands/codewiki/text/citations.rs:181-197]
- `strip_invalid_citations` (function) component `strip_invalid_citations [function]` (`c52bbeb5-443f-5293-9ee1-d48ed1c4eb91`) lines 199-225 [crates/gcode/src/commands/codewiki/text/citations.rs:199-225]
  - Signature: `fn strip_invalid_citations(text: &str, valid_spans: &[SourceSpan]) -> String {`
  - Purpose: Scans the input text for bracketed citation-like substrings and removes any that are not parsed as citations or do not fall within one of the provided 'valid_spans', preserving all other text unchanged. [crates/gcode/src/commands/codewiki/text/citations.rs:199-225]
- `contains_valid_citation` (function) component `contains_valid_citation [function]` (`0dc90579-6e54-5bc4-964e-47624afcd042`) lines 227-244 [crates/gcode/src/commands/codewiki/text/citations.rs:227-244]
  - Signature: `fn contains_valid_citation(text: &str, valid_spans: &[SourceSpan]) -> bool {`
  - Purpose: Scans the input text for bracketed citation fragments and returns 'true' as soon as one parses into '(file, start, end)' and matches any 'SourceSpan' in 'valid_spans', otherwise returns 'false' if no valid citation is found or a '[' lacks a closing ']'. [crates/gcode/src/commands/codewiki/text/citations.rs:227-244]
- `citation_parts` (function) component `citation_parts [function]` (`c26c2e95-c4af-53b5-8b8e-106e5065ccc1`) lines 246-259 [crates/gcode/src/commands/codewiki/text/citations.rs:246-259]
  - Signature: `fn citation_parts(value: &str) -> Option<(&str, usize, usize)> {`
  - Purpose: Parses a 'file:line[-line]' citation string into '(file, start_line, end_line)', rejecting empty or whitespace-containing file names, non-numeric or invalid line ranges, and any range where 'start_line' is zero or greater than 'end_line'. [crates/gcode/src/commands/codewiki/text/citations.rs:246-259]

