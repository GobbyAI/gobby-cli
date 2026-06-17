---
title: crates/gwiki/src/commands/ask/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/ask/render.rs
  ranges:
  - 6-16
  - 18-68
  - 79-114
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/ask/render.rs:6-16](crates/gwiki/src/commands/ask/render.rs#L6-L16), [crates/gwiki/src/commands/ask/render.rs:18-68](crates/gwiki/src/commands/ask/render.rs#L18-L68), [crates/gwiki/src/commands/ask/render.rs:79-114](crates/gwiki/src/commands/ask/render.rs#L79-L114)

</details>

# crates/gwiki/src/commands/ask/render.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file renders `AskOutput` into a scoped `CommandOutcome` for the `ask` command. `render` clones the scope, builds the display text with `render_text`, serializes the full output as JSON for the payload, and wraps both in `scoped_outcome("ask", ...)`.

`render_text` handles the two output shapes: when a synthesis exists, it formats an answer header and body, and adds an `[unverified]` warning if the citation check is not supported; otherwise it formats wiki search results, including degraded source notices, hit titles and page names, and any code citations with file, line, and symbol details.
[crates/gwiki/src/commands/ask/render.rs:6-16]
[crates/gwiki/src/commands/ask/render.rs:18-68]
[crates/gwiki/src/commands/ask/render.rs:79-114]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `render` | function | `pub(super) fn render(output: AskOutput) -> Result<CommandOutcome, WikiError> {` | `render [function]` | `3515d132-bcdd-58f9-9478-af47aba308a4` | 6-16 [crates/gwiki/src/commands/ask/render.rs:6-16] | Indexed function `render` in `crates/gwiki/src/commands/ask/render.rs`. [crates/gwiki/src/commands/ask/render.rs:6-16] |
| `render_text` | function | `fn render_text(query: &str, scope: &ScopeIdentity, output: &AskOutput) -> String {` | `render_text [function]` | `f32548e9-2828-545b-8e30-5f5ba50c0a5a` | 18-68 [crates/gwiki/src/commands/ask/render.rs:18-68] | Indexed function `render_text` in `crates/gwiki/src/commands/ask/render.rs`. [crates/gwiki/src/commands/ask/render.rs:18-68] |
| `unverified_synthesis_is_flagged_in_text_render` | function | `fn unverified_synthesis_is_flagged_in_text_render() {` | `unverified_synthesis_is_flagged_in_text_render [function]` | `3757f62e-aee8-5fc0-8be3-59c018a9fd64` | 79-114 [crates/gwiki/src/commands/ask/render.rs:79-114] | Indexed function `unverified_synthesis_is_flagged_in_text_render` in `crates/gwiki/src/commands/ask/render.rs`. [crates/gwiki/src/commands/ask/render.rs:79-114] |
