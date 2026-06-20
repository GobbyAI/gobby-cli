---
title: crates/gwiki/src/commands/refresh/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/refresh/render.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh/render.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Overview

`crates/gwiki/src/commands/refresh/render.rs` exposes 2 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/refresh/render.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_refresh` | function | Builds a refresh 'CommandOutcome' by deriving a status from dry-run and result counts, emitting a JSON/text summary of scope, planned/refreshed/unchanged/failed/skipped/indexing data, and setting a nonzero exit code only for an explicit non-dry-run single-source refresh in which every attempted source failed. [crates/gwiki/src/commands/refresh/render.rs:3-49] |
| `refresh_status` | function | Returns a static status string based on the refresh outcome: '"dry_run"' if 'dry_run' is true, '"failed"' if all items failed, '"partial"' if any failures occurred alongside other results, '"refreshed"' if at least one item was refreshed, otherwise '"unchanged"'. [crates/gwiki/src/commands/refresh/render.rs:51-68] |

