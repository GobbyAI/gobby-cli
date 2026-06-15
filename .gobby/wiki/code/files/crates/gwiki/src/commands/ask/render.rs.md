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

# crates/gwiki/src/commands/ask/render.rs

Module: [[code/modules/crates/gwiki/src/commands/ask|crates/gwiki/src/commands/ask]]

## Purpose

This file turns an `AskOutput` into a scoped `CommandOutcome` for the `ask` command. `render` clones the scope, builds the user-facing text with `render_text`, serializes the full output to JSON for the payload, and maps serialization failures to `WikiError::Json`; `render_text` formats either a synthesized answer with an `[unverified]` warning when citation support is insufficient, or a wiki-hit report that includes degraded sources, empty-result handling, and code citations.
[crates/gwiki/src/commands/ask/render.rs:6-16]
[crates/gwiki/src/commands/ask/render.rs:18-68]
[crates/gwiki/src/commands/ask/render.rs:79-114]

## API Symbols

- `render` (function) component `render [function]` (`3515d132-bcdd-58f9-9478-af47aba308a4`) lines 6-16 [crates/gwiki/src/commands/ask/render.rs:6-16]
  - Signature: `pub(super) fn render(output: AskOutput) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Clones 'output.scope', renders display text from the query, scope, and full output, serializes the entire 'AskOutput' to JSON with 'WikiError::Json' on failure, and returns a scoped 'CommandOutcome' for '"ask"'. [crates/gwiki/src/commands/ask/render.rs:6-16]
- `render_text` (function) component `render_text [function]` (`f32548e9-2828-545b-8e30-5f5ba50c0a5a`) lines 18-68 [crates/gwiki/src/commands/ask/render.rs:18-68]
  - Signature: `fn render_text(query: &str, scope: &ScopeIdentity, output: &AskOutput) -> String {`
  - Purpose: 'render_text' formats an 'AskOutput' into a plain-text report for a given query and scope, emitting either a synthesized answer with an optional unverified-claims notice when synthesis exists, or a wiki-hit listing with degraded-source, empty-result, and code-citation sections otherwise. [crates/gwiki/src/commands/ask/render.rs:18-68]
- `unverified_synthesis_is_flagged_in_text_render` (function) component `unverified_synthesis_is_flagged_in_text_render [function]` (`3757f62e-aee8-5fc0-8be3-59c018a9fd64`) lines 79-114 [crates/gwiki/src/commands/ask/render.rs:79-114]
  - Signature: `fn unverified_synthesis_is_flagged_in_text_render() {`
  - Purpose: Verifies that 'render_text' emits an '[unverified]' warning when synthesis contains an unsupported claim and omits that marker when the synthesis is citation-grounded. [crates/gwiki/src/commands/ask/render.rs:79-114]

