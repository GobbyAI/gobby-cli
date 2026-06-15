---
title: crates/gwiki/src/audit/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/audit/render.rs
  ranges:
  - 3-32
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/audit/render.rs

Module: [[code/modules/crates/gwiki/src/audit|crates/gwiki/src/audit]]

## Purpose

Formats an `AuditReport` into a plain-text wiki audit report. `render_text` writes the report scope, then a section of unsupported claims; it emits `- none` when there are no unsupported claims, otherwise it lists each claim as `path:line claim` and appends `[sources: ...]` with comma-separated source IDs when source context is present. [crates/gwiki/src/audit/render.rs:3-32]

## API Symbols

- `render_text` (function) component `render_text [function]` (`d261ce57-7b10-5b29-8e5f-6f103999a468`) lines 3-32 [crates/gwiki/src/audit/render.rs:3-32]
  - Signature: `pub fn render_text(report: &AuditReport) -> String {`
  - Purpose: Builds and returns a plain-text wiki audit report string for 'report.scope', listing each unsupported claim as 'path:line claim' with optional '[sources: ...]' source IDs, or '- none' when there are no unsupported claims. [crates/gwiki/src/audit/render.rs:3-32]

