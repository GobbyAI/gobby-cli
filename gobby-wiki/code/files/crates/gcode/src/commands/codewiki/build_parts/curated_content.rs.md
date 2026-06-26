---
title: crates/gcode/src/commands/codewiki/build_parts/curated_content.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/curated_content.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/curated_content.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/curated_content.rs` exposes 31 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/curated_content.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CuratedPageKind` | type | Indexed type `CuratedPageKind` in `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs`. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:28-31] |
| `CuratedBody` | class | 'CuratedBody' stores the finalized page body text as an optional multi-section string, a 'degraded' flag indicating whether AI content-pass generation failed and the structural fallback was used, and a list of 'VerifyNote' validation notes. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:34-44] |
| `curated_page_body` | function | 'curated_page_body' builds evidence rows from member modules/files, returns an empty non-degraded 'CuratedBody' when no evidence exists, otherwise selects kind-specific excerpt limits and prompts/system text, generates a curated page body via 'maybe_generate', and prepares grounded verification notes for unsupported claims. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:51-138] |
| `member_evidence_rows` | function | Builds a 'Vec<PageEvidenceRow>' by resolving each module name and file path through the provided lookup maps, appending a row for each found 'ModuleDoc' or 'FileDoc' with its name/path, kind, citation from 'source_spans', and cloned summary, while silently skipping missing entries. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:140-168] |
| `symbol_evidence_rows` | function | Builds a 'Vec<PageEvidenceRow>' by looking up each 'member_files' entry in 'file_lookup', flattening all symbols from matched documents into rows containing name, kind, citation, and purpose, then sorting by symbol name and truncating to 'MAX_PAGE_SYMBOL_ROWS'. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:170-191] |
| `span_citation` | function | Returns the citation string for the first 'SourceSpan' in 'spans', or 'fallback.to_string()' if 'spans' is empty. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:193-198] |
| `structural_body` | function | 'structural_body' constructs a Markdown string for a curated page by emitting a kind-specific intro section, a “Key components” table from 'symbols' or a fallback note if empty, and an optional “Members” bullet list from 'members'. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:204-261] |
| `append_guided_tour` | function | Appends a “guided tour” section to 'doc' by inserting a header, an optional introductory link to the first chapter, a numbered list of wiki-style links for all provided chapters, a trailing blank line, and the ask hint footer. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:268-281] |
| `append_ask_hint` | function | Appends a fixed help hint to the provided string, instructing users to query the vault with 'gwiki ask "..."' or locate pages with 'gwiki search "..."'. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:284-288] |
| `append_tour_nav` | function | Appends a “Continue the tour” navigation section to 'doc' with optional previous and next narrative links in wiki markup, and does nothing if both links are absent. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:293-309] |
| `FlowComponent` | class | FlowComponent is a struct that represents a stage in a data-flow analysis chain, identified by normalized module/file keys for alignment with documented flows, a descriptive label, and an optional role designation. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:312-318] |
| `curated_flow_diagram` | function | Returns an optional rendered conceptual flow diagram of module and file components ordered by documentation hints and annotated with architectural roles. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:338-373] |
| `flow_components` | function | Creates a vector of FlowComponents by looking up documentation for member modules first, then supplementing with member files if fewer than two components are generated. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:378-398] |
| `component_from` | function | Constructs a 'FlowComponent' with deduplicated normalized keys derived from the input name and its flow-label variant, and a role phrase computed from the summary. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:400-413] |
| `flow_hint_text` | function | Concatenates documentation summaries for specified modules and files with truncated source code excerpts retrieved from lookup maps into a single hint string. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:417-447] |
| `order_components_by_hint` | function | Reorders FlowComponents in-place according to indices parsed from a hint string, placing chain-matched components first in specified order followed by remaining components, returning false if the parsed chain contains fewer than two elements. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:452-473] |
| `parse_flow_chain` | function | **Parses an arrow-delimited flow hint to extract and return the indices of the first chain containing at least two unique components.** [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:477-494] |
| `first_component_in` | function | Finds and returns the index of the first 'FlowComponent' whose keys collection contains a match for any normalized, non-empty alphanumeric token extracted from the segment. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:497-507] |
| `push_unique` | function | Appends the given 'usize' index to the vector only if it is not already present, ensuring no duplicate entries. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:509-513] |
| `flow_label` | function | Extracts the rightmost segment of a string delimited by '/' or ':', strips a trailing '.rs' suffix and whitespace, and returns the result as an owned String. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:517-524] |
| `normalize_key` | function | Extracts the filename stem from the last path/URI segment and normalizes it by filtering to ASCII alphanumeric characters and converting to lowercase. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:528-535] |
| `role_phrase` | function | This function extracts and returns the first 'FLOW_ROLE_WORDS' whitespace-separated tokens from the first clause (delimited by '.', ';', or ':') of a trimmed input string, or 'None' if the input or resulting phrase is empty. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:540-556] |
| `module_doc` | function | Constructs a new 'ModuleDoc' struct with the provided 'name' and 'summary' fields while initializing all other fields to empty collections, 'false', and 'None'. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:562-574] |
| `file_doc` | function | This function constructs a 'FileDoc' struct with the provided path and summary strings, initializing all remaining fields to empty collections or default values. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:576-590] |

_2 more symbol(s) not shown — run `gcode outline crates/gcode/src/commands/codewiki/build_parts/curated_content.rs` for the full list._

_Verified by 5 in-file unit tests._

