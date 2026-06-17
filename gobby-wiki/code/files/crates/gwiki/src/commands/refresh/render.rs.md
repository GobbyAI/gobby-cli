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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/refresh/render.rs:3-49](crates/gwiki/src/commands/refresh/render.rs#L3-L49), [crates/gwiki/src/commands/refresh/render.rs:51-68](crates/gwiki/src/commands/refresh/render.rs#L51-L68)

</details>

# crates/gwiki/src/commands/refresh/render.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Purpose

Formats the result of a refresh command into a scoped `CommandOutcome` with both JSON and human-readable text. `render_refresh` copies the indexed status, derives a status label via `refresh_status`, decides whether the command should exit nonzero only for an explicit non-dry-run single-source refresh where every attempted source failed, and then assembles the payload, summary text, and final outcome. `refresh_status` centralizes the top-level status classification from dry-run and per-source counts, distinguishing `dry_run`, `failed`, `partial`, `refreshed`, and `unchanged`.
[crates/gwiki/src/commands/refresh/render.rs:3-49]
[crates/gwiki/src/commands/refresh/render.rs:51-68]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `render_refresh` | function | `pub(crate) fn render_refresh(render: RefreshRender) -> CommandOutcome {` | `render_refresh [function]` | `7dd40a3d-6099-54f0-b0b3-9f8263f090ce` | 3-49 [crates/gwiki/src/commands/refresh/render.rs:3-49] | Indexed function `render_refresh` in `crates/gwiki/src/commands/refresh/render.rs`. [crates/gwiki/src/commands/refresh/render.rs:3-49] |
| `refresh_status` | function | `fn refresh_status(` | `refresh_status [function]` | `7e5a9b6f-d731-5e28-a03c-79bcbc382a6e` | 51-68 [crates/gwiki/src/commands/refresh/render.rs:51-68] | Indexed function `refresh_status` in `crates/gwiki/src/commands/refresh/render.rs`. [crates/gwiki/src/commands/refresh/render.rs:51-68] |
