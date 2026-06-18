---
title: crates/gcode/src/commands/codewiki/text/citations.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/citations.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/text/citations.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

To prevent excessive citations in generated summaries, the file enforces a strict limit on the number of fallback references via `MAX_FALLBACK_CITATIONS` . The module extracts lexical tokens from the generated text and calculates a relevance score to rank candidate paths, prioritizing actual source code over static asset files [crates/gcode/src/commands/codewiki/text/citations.rs:26-34, crates/gcode/src/commands/codewiki/text/citations.rs:38-44, crates/gcode/src/commands/codewiki/text/citations.rs:46-51, crates/gcode/src/commands/codewiki/text/citations.rs:58-98].

## How it fits
This file is part of the `codewiki::text` submodule, working alongside sibling modules like `sanitize` and utilizing the `SourceSpan` type to process textual spans . It operates as an intermediary validation step between the raw text generation flow and the final documented output.
[crates/gcode/src/commands/codewiki/text/citations.rs:26-34]
[crates/gcode/src/commands/codewiki/text/citations.rs:38-44]
[crates/gcode/src/commands/codewiki/text/citations.rs:46-51]
[crates/gcode/src/commands/codewiki/text/citations.rs:58-98]
[crates/gcode/src/commands/codewiki/text/citations.rs:100-106]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `is_asset_or_data_file` | function | Returns 'true' if the input path has a file extension that can be converted to UTF-8, lowercased, and found in 'ASSET_DATA_EXTENSIONS'; otherwise returns 'false'. [crates/gcode/src/commands/codewiki/text/citations.rs:26-34] |
| `lexical_tokens` | function | Returns a 'BTreeSet' of unique, lowercase ASCII alphanumeric tokens extracted from 'value' by splitting on any non-alphanumeric character and keeping only tokens with length at least 3. [crates/gcode/src/commands/codewiki/text/citations.rs:38-44] |
| `citation_relevance` | function | Counts how many lexically extracted tokens from 'file' are present in 'text_tokens' and returns that match count as a 'usize'. [crates/gcode/src/commands/codewiki/text/citations.rs:46-51] |
| `fallback_spans` | function | Deduplicates the input 'SourceSpan's, ranks their files by asset/data status and lexical relevance to 'text', and returns up to 'MAX_FALLBACK_CITATIONS' spans by selecting one span per file first and then filling remaining slots with additional unique spans from the ranked files. [crates/gcode/src/commands/codewiki/text/citations.rs:58-98] |
| `citation_list` | function | Returns a newline-separated string of 'citation()' values for the spans produced by 'fallback_spans(spans, text)'. [crates/gcode/src/commands/codewiki/text/citations.rs:100-106] |
| `wrap_citation_items` | function | 'wrap_citation_items' joins an iterator of 'String' items into a newline-separated string by greedily packing space-delimited items onto each line without exceeding 'max_line_width' in bytes, starting a new line as needed. [crates/gcode/src/commands/codewiki/text/citations.rs:108-128] |
| `citation_markers` | function | Builds a wrapped citation-marker string by collecting citation IDs from fallback spans, filtering the input citations to those present in that fallback set, formatting the surviving indices as '"[{index}]"', and passing them to 'wrap_citation_items' with 'FALLBACK_CITATION_LINE_WIDTH'. [crates/gcode/src/commands/codewiki/text/citations.rs:130-142] |
| `citation_references` | function | Returns a deduplicated, sorted list of citation strings from the input 'SourceSpan' slice, numbering each unique span starting at 1 by collecting them into a 'BTreeSet' and mapping each span to '(index + 1, span.citation())'. [crates/gcode/src/commands/codewiki/text/citations.rs:144-153] |
| `replace_citations_with_markers` | function | Returns a new 'String' in which each citation substring identified by 'citation_references(spans)' is globally replaced with its corresponding bracketed numeric marker, e.g. '"[index]"', in the input text. [crates/gcode/src/commands/codewiki/text/citations.rs:155-161] |
| `write_references` | function | Appends a '## References' section to 'doc' containing only citation entries whose '[index]' markers already appear in the document, otherwise leaves 'doc' unchanged. [crates/gcode/src/commands/codewiki/text/citations.rs:166-179] |
| `ground_text` | function | 'ground_text' sanitizes the input by stripping invalid citations and model markdown links, then appends the provided fallback citation with either a newline or space if no valid citation remains in the cleaned text. [crates/gcode/src/commands/codewiki/text/citations.rs:181-197] |
| `strip_invalid_citations` | function | Scans 'text' for bracketed citation-like substrings and returns a copy with only those citations kept whose parsed 'file/start/end' range matches at least one 'valid_spans' entry, while leaving non-citation text unchanged and preserving unmatched '[' sequences verbatim. [crates/gcode/src/commands/codewiki/text/citations.rs:199-225] |
| `contains_valid_citation` | function | Scans 'text' for bracketed citation-like substrings and returns 'true' if any parses into '(file, start, end)' that is fully contained by at least one 'SourceSpan' in 'valid_spans', otherwise 'false'. [crates/gcode/src/commands/codewiki/text/citations.rs:227-244] |
| `citation_parts` | function | Parses a 'file:line' or 'file:start-end' citation string into '(file, line_start, line_end)' only if the file part is nonempty and whitespace-free, the line values parse as integers, and 'line_start' is positive and not greater than 'line_end'. [crates/gcode/src/commands/codewiki/text/citations.rs:246-259] |
| `citation_inner` | function | Returns a 'file:line' string when 'line_start == line_end', otherwise returns a 'file:line_start-line_end' range string. [crates/gcode/src/commands/codewiki/text/citations.rs:264-270] |
| `CitationResolver` | type | Indexed type `CitationResolver` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:277-287] |
| `ReanchorResult` | class | 'ReanchorResult' is a crate-visible result record that stores the reanchored 'text' plus counts of 'repaired' and 'unresolved' items. [crates/gcode/src/commands/codewiki/text/citations.rs:292-296] |
| `reanchor_citations` | function | 'reanchor_citations' scans 'text' for bracketed citation-like spans, uses 'resolver' to update any stale file/line anchors to current spans, and returns the rewritten text along with counts of repaired and unresolved citations. [crates/gcode/src/commands/codewiki/text/citations.rs:305-360] |

