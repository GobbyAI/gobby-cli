---
title: crates/gwiki/src/commands/refresh/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/refresh/render.rs
  ranges:
  - 3-49
  - 51-68
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh/render.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Purpose

Builds the command output for a refresh run. `render_refresh` gathers the refresh results, derives a status string with `refresh_status`, and packages everything into a scoped `CommandOutcome` containing both JSON and human-readable text. The JSON payload includes the command name, scope, dry-run flag, planned/refreshed/unchanged/failed/skipped lists, indexed data, index status, and degradations, while the text summary reports counts for the main result buckets. It only returns exit code `1` for an explicit non-dry-run single-source refresh that failed completely; all other cases exit successfully. `refresh_status` encodes the outcome priority as `dry_run`, `failed`, `partial`, `refreshed`, or `unchanged` based on the counts.
[crates/gwiki/src/commands/refresh/render.rs:3-49]
[crates/gwiki/src/commands/refresh/render.rs:51-68]

## API Symbols

- `render_refresh` (function) component `render_refresh [function]` (`7dd40a3d-6099-54f0-b0b3-9f8263f090ce`) lines 3-49 [crates/gwiki/src/commands/refresh/render.rs:3-49]
  - Signature: `pub(crate) fn render_refresh(render: RefreshRender) -> CommandOutcome {`
  - Purpose: Constructs and returns a CommandOutcome for a refresh operation, encoding metrics (planned/refreshed/unchanged/failed/skipped sources) in JSON and text formats, with exit code 1 exclusively for explicit single-source refreshes that fail completely. [crates/gwiki/src/commands/refresh/render.rs:3-49]
- `refresh_status` (function) component `refresh_status [function]` (`7e5a9b6f-d731-5e28-a03c-79bcbc382a6e`) lines 51-68 [crates/gwiki/src/commands/refresh/render.rs:51-68]
  - Signature: `fn refresh_status(`
  - Purpose: Returns a static status string representing the refresh operation outcome, determined by dry-run flag and outcome counts, with priority ordering: dry_run → all-failed → partial-failed → refreshed → unchanged. [crates/gwiki/src/commands/refresh/render.rs:51-68]

