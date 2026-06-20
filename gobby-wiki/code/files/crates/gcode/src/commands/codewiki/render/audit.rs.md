---
title: crates/gcode/src/commands/codewiki/render/audit.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render/audit.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/render/audit.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/render|crates/gcode/src/commands/codewiki/render]]

## Overview

`crates/gcode/src/commands/codewiki/render/audit.rs` exposes 2 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/render/audit.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_deprecations_doc` ⚠️ **deprecated** | function | ⚠️ **deprecated** — deprecated symbol grouped by file; renders a clear "none found" line when 'render_deprecations_doc' builds a markdown deprecations report from a 'DeprecationsDoc' by emitting frontmatter, an explanatory header, a grouped per-file table of deprecated symbols with kind, location, and reason, or a “No deprecated symbols found” message when empty. [crates/gcode/src/commands/codewiki/render/audit.rs:8-57] |
| `render_dead_code_doc` | function | Builds a Markdown dead-code report string by emitting frontmatter and explanatory sections, then either returns an unavailable-analysis notice when 'doc.skipped' is set or includes the heuristic criteria used to list dead-code candidates. [crates/gcode/src/commands/codewiki/render/audit.rs:63-148] |

