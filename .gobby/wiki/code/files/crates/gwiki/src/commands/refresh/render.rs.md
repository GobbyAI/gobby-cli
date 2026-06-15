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

Builds the refresh command result for output and process status. `render_refresh` takes a `RefreshRender`, derives a high-level status with `refresh_status`, assembles a JSON payload plus a human-readable summary, and wraps both in a scoped `CommandOutcome`. It only returns exit code `1` for an explicit, non-dry-run single-source refresh where every attempted source failed; all other refresh cases report success through the outcome payload. `refresh_status` maps the dry-run and result counts to a static status string, prioritizing `dry_run`, then total failure, partial failure, refreshed, and unchanged.
[crates/gwiki/src/commands/refresh/render.rs:3-49]
[crates/gwiki/src/commands/refresh/render.rs:51-68]

## API Symbols

- `render_refresh` (function) component `render_refresh [function]` (`7dd40a3d-6099-54f0-b0b3-9f8263f090ce`) lines 3-49 [crates/gwiki/src/commands/refresh/render.rs:3-49]
  - Signature: `pub(crate) fn render_refresh(render: RefreshRender) -> CommandOutcome {`
  - Purpose: Constructs and returns a CommandOutcome for a refresh operation, encoding metrics (planned/refreshed/unchanged/failed/skipped sources) in JSON and text formats, with exit code 1 exclusively for explicit single-source refreshes that fail completely. [crates/gwiki/src/commands/refresh/render.rs:3-49]
- `refresh_status` (function) component `refresh_status [function]` (`7e5a9b6f-d731-5e28-a03c-79bcbc382a6e`) lines 51-68 [crates/gwiki/src/commands/refresh/render.rs:51-68]
  - Signature: `fn refresh_status(`
  - Purpose: Returns a static status string representing the refresh operation outcome, determined by dry-run flag and outcome counts, with priority ordering: dry_run → all-failed → partial-failed → refreshed → unchanged. [crates/gwiki/src/commands/refresh/render.rs:51-68]

