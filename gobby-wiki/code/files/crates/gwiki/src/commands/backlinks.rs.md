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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/backlinks.rs:10-18](crates/gwiki/src/commands/backlinks.rs#L10-L18), [crates/gwiki/src/commands/backlinks.rs:20-28](crates/gwiki/src/commands/backlinks.rs#L20-L28), [crates/gwiki/src/commands/backlinks.rs:30-53](crates/gwiki/src/commands/backlinks.rs#L30-L53), [crates/gwiki/src/commands/backlinks.rs:55-78](crates/gwiki/src/commands/backlinks.rs#L55-L78), [crates/gwiki/src/commands/backlinks.rs:80-99](crates/gwiki/src/commands/backlinks.rs#L80-L99), [crates/gwiki/src/commands/backlinks.rs:101-126](crates/gwiki/src/commands/backlinks.rs#L101-L126)

</details>

# crates/gwiki/src/commands/backlinks.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements backlink-related commands for the wiki. `execute` resolves the selected store and scope, builds an in-memory graph from indexed data, finds pages linking to a given page, and hands the results to `render_backlinks`. `execute_link_suggest` follows the same pattern for link recommendations, asking the graph for suggestions and passing them to `render_link_suggest`. The render functions package each result set into structured JSON payloads and also generate plain-text output via `render_backlinks_text` and `render_link_suggest_text`, then wrap both into a scoped `CommandOutcome` through `super::scoped_outcome`.
[crates/gwiki/src/commands/backlinks.rs:10-18]
[crates/gwiki/src/commands/backlinks.rs:20-28]
[crates/gwiki/src/commands/backlinks.rs:30-53]
[crates/gwiki/src/commands/backlinks.rs:55-78]
[crates/gwiki/src/commands/backlinks.rs:80-99]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(` | `execute [function]` | `9221ea26-3d62-54ec-a050-21b36b815b78` | 10-18 [crates/gwiki/src/commands/backlinks.rs:10-18] | Indexed function `execute` in `crates/gwiki/src/commands/backlinks.rs`. [crates/gwiki/src/commands/backlinks.rs:10-18] |
| `execute_link_suggest` | function | `pub(crate) fn execute_link_suggest(` | `execute_link_suggest [function]` | `586b2147-ca79-5c2d-891a-3ac1a13a3d54` | 20-28 [crates/gwiki/src/commands/backlinks.rs:20-28] | Indexed function `execute_link_suggest` in `crates/gwiki/src/commands/backlinks.rs`. [crates/gwiki/src/commands/backlinks.rs:20-28] |
| `render_backlinks` | function | `fn render_backlinks(` | `render_backlinks [function]` | `ef596b5a-3e01-5dd0-9709-5b73e44b8fe4` | 30-53 [crates/gwiki/src/commands/backlinks.rs:30-53] | Indexed function `render_backlinks` in `crates/gwiki/src/commands/backlinks.rs`. [crates/gwiki/src/commands/backlinks.rs:30-53] |
| `render_link_suggest` | function | `fn render_link_suggest(` | `render_link_suggest [function]` | `a27f4270-b445-5818-8fc6-95c5409f229c` | 55-78 [crates/gwiki/src/commands/backlinks.rs:55-78] | Indexed function `render_link_suggest` in `crates/gwiki/src/commands/backlinks.rs`. [crates/gwiki/src/commands/backlinks.rs:55-78] |
| `render_backlinks_text` | function | `fn render_backlinks_text(page: &str, scope: &ScopeIdentity, backlinks: &[WikiBacklink]) -> String {` | `render_backlinks_text [function]` | `1de27c32-8341-5a02-964c-f383d1ee83ab` | 80-99 [crates/gwiki/src/commands/backlinks.rs:80-99] | Indexed function `render_backlinks_text` in `crates/gwiki/src/commands/backlinks.rs`. [crates/gwiki/src/commands/backlinks.rs:80-99] |
| `render_link_suggest_text` | function | `fn render_link_suggest_text(scope: &ScopeIdentity, suggestions: &[LinkSuggestion]) -> String {` | `render_link_suggest_text [function]` | `766ccf2a-8fbf-5a10-88c2-495f86754355` | 101-126 [crates/gwiki/src/commands/backlinks.rs:101-126] | Indexed function `render_link_suggest_text` in `crates/gwiki/src/commands/backlinks.rs`. [crates/gwiki/src/commands/backlinks.rs:101-126] |
