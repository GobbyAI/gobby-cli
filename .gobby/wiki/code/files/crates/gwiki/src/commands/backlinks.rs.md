---
title: crates/gwiki/src/commands/backlinks.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/backlinks.rs
  ranges:
  - 10-18
  - 20-28
  - 30-53
  - 55-78
  - 80-99
  - 101-126
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/backlinks.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

This file implements the wiki backlink and link-suggestion commands. Both entry points first resolve the selected scope into an indexed store, build a memory graph from that store, and query it either for backlinks to a page or for link suggestions up to a limit. The rendering helpers then package those results into scoped `CommandOutcome` values with JSON payloads for machine use and formatted text summaries for human output, using separate text renderers for backlinks and suggestions.
[crates/gwiki/src/commands/backlinks.rs:10-18]
[crates/gwiki/src/commands/backlinks.rs:20-28]
[crates/gwiki/src/commands/backlinks.rs:30-53]
[crates/gwiki/src/commands/backlinks.rs:55-78]
[crates/gwiki/src/commands/backlinks.rs:80-99]

## API Symbols

- `execute` (function) component `execute [function]` (`9221ea26-3d62-54ec-a050-21b36b815b78`) lines 10-18 [crates/gwiki/src/commands/backlinks.rs:10-18]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Retrieves and renders backlinks for a specified wiki page by constructing a memory graph from a scope-filtered indexed store. [crates/gwiki/src/commands/backlinks.rs:10-18]
- `execute_link_suggest` (function) component `execute_link_suggest [function]` (`586b2147-ca79-5c2d-891a-3ac1a13a3d54`) lines 20-28 [crates/gwiki/src/commands/backlinks.rs:20-28]
  - Signature: `pub(crate) fn execute_link_suggest(`
  - Purpose: Constructs a memory graph from an indexed scoped store and returns rendered link suggestions limited to the specified count. [crates/gwiki/src/commands/backlinks.rs:20-28]
- `render_backlinks` (function) component `render_backlinks [function]` (`ef596b5a-3e01-5dd0-9709-5b73e44b8fe4`) lines 30-53 [crates/gwiki/src/commands/backlinks.rs:30-53]
  - Signature: `fn render_backlinks(`
  - Purpose: Serializes a collection of wiki backlinks into a JSON command payload with rendered text representation, returning a scoped CommandOutcome. [crates/gwiki/src/commands/backlinks.rs:30-53]
- `render_link_suggest` (function) component `render_link_suggest [function]` (`a27f4270-b445-5818-8fc6-95c5409f229c`) lines 55-78 [crates/gwiki/src/commands/backlinks.rs:55-78]
  - Signature: `fn render_link_suggest(`
  - Purpose: Renders a scoped "link-suggest" command outcome by serializing an array of `LinkSuggestion` objects with their targets, mention counts, and source paths into a JSON payload. [crates/gwiki/src/commands/backlinks.rs:55-78]
- `render_backlinks_text` (function) component `render_backlinks_text [function]` (`1de27c32-8341-5a02-964c-f383d1ee83ab`) lines 80-99 [crates/gwiki/src/commands/backlinks.rs:80-99]
  - Signature: `fn render_backlinks_text(page: &str, scope: &ScopeIdentity, backlinks: &[WikiBacklink]) -> String {`
  - Purpose: Generates a formatted text summary listing the source paths and raw targets of backlinks referencing a given page within a specified scope. [crates/gwiki/src/commands/backlinks.rs:80-99]
- `render_link_suggest_text` (function) component `render_link_suggest_text [function]` (`766ccf2a-8fbf-5a10-88c2-495f86754355`) lines 101-126 [crates/gwiki/src/commands/backlinks.rs:101-126]
  - Signature: `fn render_link_suggest_text(scope: &ScopeIdentity, suggestions: &[LinkSuggestion]) -> String {`
  - Purpose: Renders a formatted string of link suggestions for a given scope, listing each suggestion's target and mention count, or "No suggestions" if the list is empty. [crates/gwiki/src/commands/backlinks.rs:101-126]

