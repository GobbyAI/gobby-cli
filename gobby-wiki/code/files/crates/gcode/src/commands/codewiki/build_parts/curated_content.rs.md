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

`crates/gcode/src/commands/codewiki/build_parts/curated_content.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CuratedPageKind` | type | Indexed type `CuratedPageKind` in `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs`. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:28-31] |
| `CuratedBody` | class | 'CuratedBody' is a crate-visible container for the generated page body text and a 'degraded' flag that records whether content-pass generation failed and the output fell back to the structural body. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:34-43] |
| `curated_page_body` | function | 'curated_page_body' assembles member and symbol evidence plus ranked source excerpts, selects a concept or narrative prompt/system based on 'CuratedPageKind', invokes the text generator, and returns a 'CuratedBody' that may be grounded by verifier-based removal of unsupported content or marked degraded/empty if no evidence is available. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:50-132] |
| `member_evidence_rows` | function | Builds and returns a 'Vec<PageEvidenceRow>' by resolving the given module and file names through their lookup maps, emitting rows for each found document with the document name/path, kind ('"module"' or '"file"'), a citation derived from its source spans, and its summary, in module-then-file order. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:134-162] |
| `symbol_evidence_rows` | function | Builds a list of 'PageEvidenceRow' entries for all symbols in the specified member files using 'file_lookup', then sorts the rows by symbol name, truncates to 'MAX_PAGE_SYMBOL_ROWS', and returns the result. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:164-185] |
| `span_citation` | function | Returns the citation string for the first 'SourceSpan' in 'spans', or 'fallback.to_string()' if the slice is empty. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:187-192] |
| `structural_body` | function | 'structural_body' builds a Markdown string for a curated page by emitting a kind-specific intro section, then a “Key components” table or placeholder for 'symbols', and optionally a “Members” bullet list for 'members'. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:198-255] |
| `append_guided_tour` | function | Appends a “Start here” guided-tour section to the document by adding a heading, an optional introductory link to the first chapter, an enumerated list of chapter links, a trailing blank line, and the standard ask-hint footer. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:262-275] |
| `append_ask_hint` | function | Appends a fixed help hint to the provided document string, instructing the user to use 'gwiki ask' to query the vault and 'gwiki search' to locate pages. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:278-282] |
| `append_tour_nav` | function | Appends a “Continue the tour” navigation section to 'doc' with optional previous and next narrative links formatted as wiki-style list items, and leaves 'doc' unchanged when both are absent. [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:287-303] |

