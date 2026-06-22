---
title: crates/gwiki/src/commands/backlinks.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/backlinks.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/backlinks.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/backlinks.rs` exposes 6 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/backlinks.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Resolves the indexed store for the selected scope, builds an in-memory graph from it, computes backlinks for the given page within the search scope, and returns the rendered backlink command outcome. [crates/gwiki/src/commands/backlinks.rs:10-18] |
| `execute_link_suggest` | function | Resolves the indexed store and search scope for a selection, builds an in-memory graph from that store, computes up to 'limit' link suggestions for the search scope, and returns the rendered 'CommandOutcome' in the output scope. [crates/gwiki/src/commands/backlinks.rs:20-28] |
| `render_backlinks` | function | Builds a JSON payload and human-readable text for a page’s backlink list, then returns a scoped 'CommandOutcome' via 'scoped_outcome'. [crates/gwiki/src/commands/backlinks.rs:30-53] |
| `render_link_suggest` | function | Builds a 'link-suggest' JSON payload from the provided scope, limit, and suggestions, generates human-readable suggestion text, and returns a scoped 'CommandOutcome' via 'super::scoped_outcome'. [crates/gwiki/src/commands/backlinks.rs:55-78] |
| `render_backlinks_text` | function | Builds a human-readable backlinks report string for a page and scope, returning a header plus either 'No backlinks' when the list is empty or one '- source_path via raw_target' line per 'WikiBacklink'. [crates/gwiki/src/commands/backlinks.rs:80-99] |
| `render_link_suggest_text` | function | Builds a human-readable link-suggestion report string that includes the scope header, returns 'No suggestions' when the slice is empty, and otherwise lists each suggestion target with its mention count using singular/plural “mention(s)”. [crates/gwiki/src/commands/backlinks.rs:101-126] |

