---
title: crates/gcode/src/commands/codewiki/text/citations.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/citations.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text/citations.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Overview

`crates/gcode/src/commands/codewiki/text/citations.rs` exposes 19 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/text/citations.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

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
| `contains_valid_citation` | function | This function determines if a given text contains at least one valid citation by first searching for bracketed citation patterns that fall within the specified valid source spans and, if none are found, falling back to checking for bare inline citations. [crates/gcode/src/commands/codewiki/text/citations.rs:227-249] |
| `contains_bare_citation` | function | Returns 'true' if any token in 'text', after splitting on whitespace and common punctuation and trimming trailing punctuation, parses as a citation-like reference whose '(file, start, end)' range is contained in any 'SourceSpan' in 'valid_spans'. [crates/gcode/src/commands/codewiki/text/citations.rs:256-268] |
| `citation_parts` | function | Parses a 'file:line' or 'file:start-end' citation string into '(file, start_line, end_line)' only if the file path is nonempty and whitespace-free, the numeric range parses successfully, and 'start_line' is positive and not greater than 'end_line'. [crates/gcode/src/commands/codewiki/text/citations.rs:270-283] |
| `citation_inner` | function | Returns a citation string formatted as 'file:line' when 'line_start == line_end', otherwise as 'file:line_start-line_end'. [crates/gcode/src/commands/codewiki/text/citations.rs:288-294] |
| `CitationResolver` | type | Indexed type `CitationResolver` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:301-311] |
| `ReanchorResult` | class | 'ReanchorResult' is an internal result type that carries the reanchored 'text' plus counts of 'repaired' items and 'unresolved' items. [crates/gcode/src/commands/codewiki/text/citations.rs:316-320] |
| `reanchor_citations` | function | 'reanchor_citations' scans 'text' for bracketed citation-like spans, uses 'resolver' to update any out-of-date file line ranges while counting repaired and unresolved citations, and returns the rewritten text plus those counts in a 'ReanchorResult'. [crates/gcode/src/commands/codewiki/text/citations.rs:329-384] |

