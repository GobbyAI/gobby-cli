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

`crates/gcode/src/commands/codewiki/build_parts/curated_content.rs` exposes 10 indexed API symbols.

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

