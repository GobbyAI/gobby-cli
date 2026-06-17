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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/audit/render.rs:3-32](crates/gwiki/src/audit/render.rs#L3-L32)

</details>

# crates/gwiki/src/audit/render.rs

Module: [[code/modules/crates/gwiki/src/audit|crates/gwiki/src/audit]]

## Purpose

This file provides a plain-text renderer for `AuditReport`. `render_text` builds a human-readable wiki audit report starting with the report scope, then appends an “Unsupported claims” section that either says `none` or lists each unsupported claim with its file path, line number, claim text, and optional source IDs from `source_context`. [crates/gwiki/src/audit/render.rs:3-32]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `render_text` | function | `pub fn render_text(report: &AuditReport) -> String {` | `render_text [function]` | `d261ce57-7b10-5b29-8e5f-6f103999a468` | 3-32 [crates/gwiki/src/audit/render.rs:3-32] | Indexed function `render_text` in `crates/gwiki/src/audit/render.rs`. [crates/gwiki/src/audit/render.rs:3-32] |
